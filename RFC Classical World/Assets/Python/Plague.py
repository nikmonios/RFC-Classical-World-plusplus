# Rhye's and Fall of Civilization - Historical Victory Goals


from CvPythonExtensions import *
import CvUtil
import PyHelpers   
import Consts as con
from StoredData import sd
from RFCUtils import utils

# globals
gc = CyGlobalContext()
localText = CyTranslator()
PyPlayer = PyHelpers.PyPlayer

iNumPlayers = con.iNumPlayers
iNumTotalPlayers = con.iBarbarian
iBarbarian = con.iBarbarian

iPlague = con.iPlague
iNumPlagues = 3
iPlagueDuration = 6
lPlagueStrength = [45, 65, 100]
iImmunity = con.iImmunity


class Plague:


	def setup(self):
		
		#for i in range(iNumPlayers):
			#sd.setPlagueCountdown(i, -utils.getTurns(iImmunity)) # this is only needed for late start
		
		sd.setGenericPlagueDates(0, getTurnForYear(-100 + gc.getGame().getSorenRandNum(16, 'Variation')))
		sd.setGenericPlagueDates(1, getTurnForYear(50 + gc.getGame().getSorenRandNum(40, 'Variation') - 20))
		sd.setGenericPlagueDates(2, getTurnForYear(540 + gc.getGame().getSorenRandNum(40, 'Variation') - 20))


	def checkTurn(self, iGameTurn):
		
		for i in range(iNumTotalPlayers + 1):
			if (gc.getPlayer(i).isAlive()):
				iCountdown = sd.getPlagueCountdown(i)
				if (iCountdown > 0): 
					iCountdown -= 1
					sd.setPlagueCountdown(i, iCountdown)
					if (iCountdown == 2):
						self.preStopPlague(i)
					if (iCountdown == 0):
						self.stopPlague(i)
				elif (iCountdown < 0):
					sd.setPlagueCountdown(i, iCountdown + 1)
		
		for i in range(iNumPlagues):
			if (iGameTurn == sd.getGenericPlagueDates(i)):
				self.startPlague(i)
			
			#retry if the epidemic is dead too quickly
			if iGameTurn == sd.getGenericPlagueDates(i) + 4 and i > 0:
				iInfectedCounter = 0
				for j in range(iNumTotalPlayers+1):
					if (gc.getPlayer(j).isAlive() and sd.getPlagueCountdown(j) > 0):
						iInfectedCounter += 1
				if (iInfectedCounter <= 1):
					self.startPlague(i)


	def checkPlayerTurn(self, iGameTurn, iPlayer):
		
		if (iPlayer < iNumTotalPlayers+1):
			if (sd.getPlagueCountdown(iPlayer) > 0):
				self.processPlague(iPlayer)


	def getPlagueMultiplier(self):
		
		for i in range(iNumPlagues-1, -1, -1):
			if gc.getGame().getGameTurn() >= sd.getGenericPlagueDates(i):
				break
		return lPlagueStrength[i]


	def startPlague(self, iPlagueCounter):
		
		iWorstCiv = -1
		iWorstHealth = 200
		for i in range(iNumPlayers):
			pPlayer = gc.getPlayer(i)
			if (pPlayer.isAlive()):
				if (self.isVulnerable(i) == True):
					iHealth = -30
					iHealth2 = iHealth/2
					if (pPlayer.calculateTotalCityHealthiness() > 0):
						iHealth = int((1.0 * pPlayer.calculateTotalCityHealthiness()) / (pPlayer.calculateTotalCityHealthiness() + \
							pPlayer.calculateTotalCityUnhealthiness()) * 100) - 60
						iHealth2 = iHealth/2 - 5
						iHealth2 += gc.getGame().getSorenRandNum(40, 'random modifier')
					if i in con.lBlackDeathStarters:
						iHealth2 -= 20 + gc.getGame().getSorenRandNum(20, 'random modifier')
					elif i in con.lBlackDeathSurvivors:
						iHealth2 += 20 + gc.getGame().getSorenRandNum(20, 'random modifier')
					if (iHealth2 < iWorstHealth):
						iWorstHealth = iHealth2
						iWorstCiv = i
		if (iWorstCiv != -1):
			pWorstCiv = gc.getPlayer(iWorstCiv)
			city = utils.getRandomCity(iWorstCiv)
			if (city != -1):
				self.spreadPlague(iWorstCiv)
				self.infectCity(city)
				iHuman = utils.getHumanID()
				if (gc.getPlayer(iHuman).canContact(iWorstCiv) and iHuman != iWorstCiv):
					CyInterface().addMessage(iHuman, True, con.iDuration, CyTranslator().getText("TXT_KEY_PLAGUE_SPREAD_CITY", ()) + " " + city.getName() + " (" + gc.getPlayer(city.getOwner()).getCivilizationAdjective(0) + ")!", "AS2D_PLAGUE", 0, "", ColorTypes(con.iLime), -1, -1, True, True)


	def preStopPlague(self, iPlayer):
		
		cityList = []
		apCityList = PyPlayer(iPlayer).getCityList()
		for pCity in apCityList:
			city = pCity.GetCy()
			if (city.getNumRealBuilding(iPlague) > 0):
				cityList.append(city)
		if (len(cityList)):
			iModifier = 0
			for city in cityList:
				if (gc.getGame().getSorenRandNum(100, 'roll') > 30 - 5*city.healthRate(False, 0) + iModifier):
					city.setNumRealBuilding(iPlague, 0)
					city.changeEspionageHealthCounter(-city.getEspionageHealthCounter()/2)
					iModifier += 5 #not every city should quit


	def stopPlague(self, iPlayer):
		
		sd.setPlagueCountdown(iPlayer, -utils.getTurns(iImmunity))
		apCityList = PyPlayer(iPlayer).getCityList()
		for pCity in apCityList:
			city = pCity.GetCy()
			if city.getNumRealBuilding(iPlague) > 0:
				city.setNumRealBuilding(iPlague, 0)
				city.changeEspionageHealthCounter(-city.getEspionageHealthCounter()/2)


	def processPlague(self, iPlayer):
				
		pPlayer = gc.getPlayer(iPlayer)
		#first spread to close locations
		cityList = [] #see below
		apCityList = PyPlayer(iPlayer).getCityList()
		for pCity in apCityList:
			city = pCity.GetCy()
			cityList.append(city) #see below
			if (city.getNumRealBuilding(iPlague) > 0):
				#print ("plague in city", city.getName())
				#if (pPlayer.isHuman()):
				#		CyInterface().addMessage(iPlayer, True, con.iDuration/2, CyTranslator().getText("TXT_KEY_PLAGUE_PROCESS_CITY", ()) + " " + city.getName(), "AS2D_PLAGUE", 0, "", ColorTypes(con.iLime), -1, -1, True, True)
				if (city.getPopulation() > 1):
					#print("healthRate in city", 35 + 5*city.healthRate(False, 0))
					if utils.getYear() < 1250:
						iMin = 80
					elif city.plot().getRegionID() in con.lBlackDeathRegions:
						if city.getOwner() in con.lBlackDeathSurvivors:
							iMin = 80
						else:
							iMin = 50
					else:
						iMin = 90
					if (gc.getGame().getSorenRandNum(100, 'roll') > iMin + 5*city.healthRate(False, 0)):
						city.changePopulation(-1)
				if (city.isCapital()): #delete in vanilla
					for iLoopCiv in range(iNumPlayers):
						if (gc.getTeam(pPlayer.getTeam()).isVassal(iLoopCiv) or \
						gc.getTeam(gc.getPlayer(iLoopCiv).getTeam()).isVassal(iPlayer)):
							if (gc.getPlayer(iLoopCiv).getNumCities() > 0): #this check is needed, otherwise game crashes
								capital = gc.getPlayer(iLoopCiv).getCapitalCity()
								if (self.isVulnerable(iLoopCiv) == True):
									if (sd.getPlagueCountdown(iPlayer) > 2): #don't spread the last turns
										self.spreadPlague(iLoopCiv)
										self.infectCity(capital)
										#print ("infect master/vassal", city.getName(), "to", capital.getName())
				for x in range(city.getX()-2, city.getX()+3):
					for y in range(city.getY()-2, city.getY()+3):
						#print ("plagueXY", x, y)
						pCurrent = gc.getMap().plot( x, y )
						if (pCurrent.getOwner() != iPlayer and pCurrent.getOwner() >= 0):
							if (sd.getPlagueCountdown(iPlayer) > 2): #don't spread the last turns
								if (self.isVulnerable(pCurrent.getOwner()) == True):
									self.spreadPlague(pCurrent.getOwner())
									self.infectCitiesNear(pCurrent.getOwner(), x, y)
									#print ("infect foreign near", city.getName())
						else:
							if (pCurrent.isCity() and not (x == city.getX() and y == city.getY())):
								#print ("is city", x, y)
								cityNear = pCurrent.getPlotCity() 
								if (not cityNear.getNumRealBuilding(iPlague) > 0):
									if (sd.getPlagueCountdown(iPlayer) > 2): #don't spread the last turns
										self.infectCity(cityNear)
										#print ("infect near", city.getName(), "to", cityNear.getName())
							else:
								if (x == city.getX() and y == city.getY()):
									self.killUnitsByPlague(city, pCurrent, 0, 42, 2)
								else:
									if (pCurrent.isRoute()):
										self.killUnitsByPlague(city, pCurrent, 10, 35, 0)
									elif (pCurrent.isWater()):
										self.killUnitsByPlague(city, pCurrent, 30, 35, 0)
									else:
										self.killUnitsByPlague(city, pCurrent, 30, 35, 0)
				for x in range(city.getX()-3, city.getX()+4):
					pCurrent = gc.getMap().plot( x, city.getY()-3 )
					if (pCurrent.getOwner() == iPlayer or not pCurrent.isOwned()):
						if (not pCurrent.isCity()):
							if (pCurrent.isRoute() or pCurrent.isWater()):
								self.killUnitsByPlague(city, pCurrent, 30, 35, 0)
					pCurrent = gc.getMap().plot( x, city.getY()+4 )
					if (pCurrent.getOwner() == iPlayer or not pCurrent.isOwned()):
						if (not pCurrent.isCity()):
							if (pCurrent.isRoute() or pCurrent.isWater()):
								self.killUnitsByPlague(city, pCurrent, 30, 35, 0)
				for y in range(city.getY()-2, city.getY()+3):
					pCurrent = gc.getMap().plot( city.getX()-3, y )
					if (pCurrent.getOwner() == iPlayer or not pCurrent.isOwned()):
						if (not pCurrent.isCity()):
							if (pCurrent.isRoute() or pCurrent.isWater()):
								self.killUnitsByPlague(city, pCurrent, 30, 35, 0)
					pCurrent = gc.getMap().plot( city.getX()+4, y )
					if (pCurrent.getOwner() == iPlayer or not pCurrent.isOwned()):
						if (not pCurrent.isCity()):
							if (pCurrent.isRoute() or pCurrent.isWater()):
								self.killUnitsByPlague(city, pCurrent, 30, 35, 0)
				
				#spread to trade route cities
				if (sd.getPlagueCountdown(iPlayer) > 2): #don't spread the last turns
					for i in range(city.getTradeRoutes()):
					#for i in range(gc.getDefineINT("MAX_TRADE_ROUTES")):
						loopCity = city.getTradeCity(i)
						if (not loopCity.isNone()):
							if (not loopCity.getNumRealBuilding(iPlague) > 0):
								#utils.echo("Plagued caravan arrives at %s" %(loopCity.getName()))
								iOwner = loopCity.getOwner()
								if (iPlayer == iOwner or gc.getTeam(pPlayer.getTeam()).isOpenBorders(iOwner) or \
									gc.getTeam(pPlayer.getTeam()).isVassal(iOwner) or \
									gc.getTeam(gc.getPlayer(iOwner).getTeam()).isVassal(iPlayer)): #own city, or open borders, or vassal													
										if (iPlayer != iOwner):
											if (self.isVulnerable(iOwner) == True):
												self.spreadPlague(iOwner)
												self.infectCity(loopCity)
												#utils.echo("infect by trade route: %s to %s" %(city.getName(), loopCity.getName()))
												iHuman = utils.getHumanID()
												if (gc.getPlayer(iHuman).canContact(iOwner) and iHuman != iOwner):
													CyInterface().addMessage(iHuman, True, con.iDuration/2, CyTranslator().getText("TXT_KEY_PLAGUE_SPREAD_CITY", ()) + " " + loopCity.getName() + " (" + gc.getPlayer(iOwner).getCivilizationAdjective(0) + ")", "AS2D_PLAGUE", 0, "", ColorTypes(con.iLime), -1, -1, True, True)
										else:
											self.infectCity(loopCity)
											#utils.echo("infect by trade route: %s to %s" %(city.getName(), loopCity.getName()))


		#spread to other cities of the empire
		if (len(cityList)):
			if (sd.getPlagueCountdown(iPlayer) > 2): #don't spread the last turns
				for city1 in cityList:
					#print ("citylist", city1.getName())
					if (not city1.getNumRealBuilding(iPlague) > 0):
						for city2 in cityList:
							if (city1 != city2):
								if (city2.getNumRealBuilding(iPlague) > 0):
									if (city1.isConnectedTo(city2)):
										#print ("infect distant", city1.getName(), "to", city2.getName(), utils.calculateDistance(city1.getX(), city1.getY(), city2.getX(), city2.getY()))
										if (utils.calculateDistance(city1.getX(), city1.getY(), city2.getX(), city2.getY()) <= 6):
											#print ("infect distant", city2.getName(), "to", city1.getName())
											self.infectCity(city1)
											return


	def killUnitsByPlague(self, city, pCurrent, baseValue, iDamage, iPreserveDefenders):
				
				iOwner = city.getOwner()
				pOwner = gc.getPlayer(iOwner)
				teamOwner = gc.getTeam(gc.getPlayer(city.getOwner()).getTeam())
				
				#deadly plague when human player isn't born yet, will speed up the loading
				if utils.getYear() <= getTurnForYear(con.tBirth[utils.getHumanID()]):
					iDamage += 10
					baseValue -= 5
				
				# modify strength on per-plague basis
				iDamage *= self.getPlagueMultiplier()
				iDamage /= 100
				
				# spare less urbanized civs
				if iOwner in con.lBlackDeathSurvivors:
					iDamage = (iDamage * 2) / 3
					baseValue += 5
				
				#print (city.getX(), city.getY())
				iNumUnitsInAPlot = pCurrent.getNumUnits()
				#iPreserveHumanDefenders = iPreserveDefenders -1 #human handicap
				iPreserveHumanDefenders = iPreserveDefenders
				iHuman = utils.getHumanID()
				if (iPreserveDefenders > 0): #cities only
					#handicap for civs distant from human player too
					if (not pOwner.isHuman()): #if not human and close or at war
						#iPreserveDefenders -= 1
						if (teamOwner.isAtWar(iHuman)):
							iPreserveDefenders += 2
						# else:
							# for j in range(len(con.lCivGroups)):
								# if ((iOwner in con.lCivGroups[j]) and (utils.getHumanID() in con.lCivGroups[j])):
									# iPreserveDefenders += 1
									# break
				if (iNumUnitsInAPlot):
					for j in range(iNumUnitsInAPlot):
							i = iNumUnitsInAPlot - j - 1
							unit = pCurrent.getUnit(i)
							if (gc.getPlayer(unit.getOwner()).isHuman()):
								#print ("iPreserveHumanDefenders", iPreserveHumanDefenders)
								if (iPreserveHumanDefenders > 0):
									#if (utils.isDefenderUnit(unit)):
										iPreserveHumanDefenders -= 1
										if (pCurrent.getNumUnits() > iPreserveDefenders):
											pass
										else:
											unit.setDamage(unit.getDamage() + iDamage - 20, con.iBarbarian)
										#print ("preserve")
										continue
							else:
								if (iPreserveDefenders > 0):
									#if (utils.isDefenderUnit(unit)):
										iPreserveDefenders -= 1
										if (pCurrent.getNumUnits() > iPreserveDefenders or gc.getTeam(gc.getPlayer(unit.getOwner()).getTeam()).isAtWar(iHuman)):															
											pass
										else:
											unit.setDamage(unit.getDamage() + iDamage - 20, con.iBarbarian)
										#print ("preserve")
										continue   
							if (utils.isMortalUnit(unit)):  #another human handicap inside
								iThreshold = baseValue + 5*city.healthRate(False, 0)
								#print ("iThreshold", iThreshold)
								
								if (teamOwner.isAtWar(iHuman) and iOwner < iNumPlayers):
									if (unit.getOwner() == iOwner):
										iDamage *= 3
										iDamage /= 4   
								
								if (gc.getGame().getSorenRandNum(100, 'roll') > iThreshold):
									if (iDamage == 100):
										if (unit.getOwner() != city.getOwner() and gc.getPlayer(unit.getOwner()).isHuman()):
											CyInterface().addMessage(unit.getOwner(), False, con.iDuration/2, CyTranslator().getText("TXT_KEY_PLAGUE_PROCESS_UNIT", ()) + " " + city.getName(), "AS2D_PLAGUE", 0, "", ColorTypes(con.iLime), -1, -1, True, True)
										unit.kill(False, iBarbarian)
									else:
										if (iDamage - unit.getExperience()/10 - unit.baseCombatStr()*3/7 >= 100 - unit.getDamage()):
											if (unit.getOwner() != iOwner and gc.getPlayer(unit.getOwner()).isHuman()):
												CyInterface().addMessage(unit.getOwner(), False, con.iDuration/2, CyTranslator().getText("TXT_KEY_PLAGUE_PROCESS_UNIT", ()) + " " + city.getName(), "AS2D_PLAGUE", 0, "", ColorTypes(con.iLime), -1, -1, True, True)
										unit.setDamage(unit.getDamage() + iDamage - unit.getExperience()/10 - unit.baseCombatStr()/2, con.iBarbarian)
										#print ("process")
									break


	def infectCity(self, city):
		
		if city.getNumRealBuilding(iPlague) > 0: return
		
		city.setNumRealBuilding(iPlague, 1)
		
		# from FfH
		iStrength = 2 + gc.getGame().getSorenRandNum(9, "Plague")
		iStrength += city.getPopulation()
		if city.getPopulation() < 6:
			iStrength -= 6 - city.getPopulation()
		iStrength -= city.totalGoodBuildingHealth()
		iStrength *= self.getPlagueMultiplier()
		iStrength /= 100
		city.changeEspionageHealthCounter(iStrength)
		
		if (gc.getPlayer(city.getOwner()).isHuman()):
			CyInterface().addMessage(city.getOwner(), True, con.iDuration/2, localText.getText("TXT_KEY_PLAGUE_SPREAD_CITY", ()) + " " + city.getName() + "!", "AS2D_PLAGUE", 0, "", ColorTypes(con.iLime), -1, -1, True, True)
		for x in range(city.getX()-2, city.getX()+3):
			for y in range(city.getY()-2, city.getY()+3):
				pCurrent = gc.getMap().plot( x, y )
				iImprovement = pCurrent.getImprovementType()
				if (iImprovement == con.iHamlet):
					pCurrent.setImprovementType(con.iCottage)
				if (iImprovement == con.iVillage):
					pCurrent.setImprovementType(con.iHamlet)
				if (iImprovement == con.iTown):
					pCurrent.setImprovementType(con.iVillage)
				if (pCurrent.isCity()):
					if (x == city.getX() and y == city.getY()):
						self.killUnitsByPlague(city, pCurrent, 0, 100, 0)


	def isVulnerable(self, iPlayer):
		
		iCountdown = sd.getPlagueCountdown(iPlayer) # less pickling
		
		if (iPlayer >= iNumPlayers):
			if (iCountdown <= 0 and iCountdown > -10 ): #more vulnerable
				return True
		else:
			pPlayer = gc.getPlayer(iPlayer)
			if (iCountdown == 0): #vulnerable
				#if (not gc.getTeam(pPlayer.getTeam()).isHasTech(con.iSanitation)):
					iHealth = -30
					if (pPlayer.calculateTotalCityHealthiness() > 0):
						iHealth = int((1.0 * pPlayer.calculateTotalCityHealthiness()) / (pPlayer.calculateTotalCityHealthiness() + \
							pPlayer.calculateTotalCityUnhealthiness()) * 100) - 60
					if (iHealth < 15): #no spread for iHealth >= 75 years
						return True
			return False


	def spreadPlague(self, iPlayer):
			
			#utils.echo("Spreading plague to %s" %(gc.getPlayer(iPlayer).getCivilizationShortDescription(0))) # DEBUG
			pPlayer = gc.getPlayer(iPlayer)  
			iHealth = -30
			if (pPlayer.calculateTotalCityHealthiness() > 0):
				iHealth = int((1.0 * pPlayer.calculateTotalCityHealthiness()) / (pPlayer.calculateTotalCityHealthiness() + \
					pPlayer.calculateTotalCityUnhealthiness()) * 100) - 60
			iHealth /= 7 #duration range will be -4 to +4 for 30 to 90
			sd.setPlagueCountdown(iPlayer, min(9, utils.getTurns(iPlagueDuration) - iHealth))


	def infectCitiesNear(self, iPlayer, startingX, startingY):
		
		apCityList = PyPlayer(iPlayer).getCityList()
		for pCity in apCityList:
			city = pCity.GetCy()
			if (utils.calculateDistance(city.getX(), city.getY(), startingX, startingY) <= 3):
				self.infectCity(city)
				iHuman = utils.getHumanID()
				if (gc.getPlayer(iHuman).canContact(iPlayer) and iHuman != iPlayer):
					CyInterface().addMessage(iHuman, True, con.iDuration/2, CyTranslator().getText("TXT_KEY_PLAGUE_SPREAD_CITY", ()) + " " + city.getName() + " (" + gc.getPlayer(iPlayer).getCivilizationAdjective(0) + ")", "AS2D_PLAGUE", 0, "", ColorTypes(con.iLime), -1, -1, True, True)


	def onCityAcquired(self, iOldOwner, iNewOwner, city):
		
		if (city.getNumRealBuilding(iPlague) > 0):
			if (sd.getPlagueCountdown(iNewOwner) <= 0 and gc.getGame().getGameTurn() > getTurnForYear(con.tBirth[iNewOwner]) + utils.getTurns(iImmunity)): #skip immunity in this case (to prevent expoiting of being immune to conquer weak civs), but not for the new born civs   
				self.spreadPlague(iNewOwner)
				apCityList = PyPlayer(iNewOwner).getCityList()
				for pCity in apCityList:
					cityNear = pCity.GetCy()
					if (utils.calculateDistance(city.getX(), city.getY(), cityNear.getX(), cityNear.getY()) <= 3):
						self.infectCity(cityNear)
				return
			city.setNumRealBuilding(iPlague, 0)


	def onCityRazed(self, argsList):
		city, iNewOwner = argsList
		
		if (city.getNumRealBuilding(iPlague) > 0):
			if (sd.getPlagueCountdown(iNewOwner) > 0):
				apCityList = PyPlayer(iNewOwner).getCityList()
				iNumCitiesInfected = 0
				for pCity in apCityList:
					otherCity = pCity.GetCy()
					if (otherCity.getX() != city.getX() or otherCity.getY() != city.getY()): #because the city razed still has the plague
						if (otherCity.getNumRealBuilding(iPlague) > 0):
							iNumCitiesInfected += 1
				if (iNumCitiesInfected == 0):
					sd.setPlagueCountdown(iNewOwner, 0) #undo spreadPlague called in onCityAcquired()