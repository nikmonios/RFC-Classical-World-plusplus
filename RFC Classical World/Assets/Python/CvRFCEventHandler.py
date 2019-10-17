from CvPythonExtensions import *
import CvUtil
import CvEventManager
import PyHelpers

from StoredData import sd
from RFCUtils import utils
import Consts as con
import Resources
import Religions
import CityNameManager
import RiseAndFall
import Barbs
import AIWars
import Victory
import Plague
import Communications
import DynamicCivs
import Companies
import UnitArtStyler
import RFCCWAIWars
import CvMainInterface

gc = CyGlobalContext()

if gc.getMap().getMapScriptName(): # Baldyr: loads stored data on module reload
	sd.load()

PyPlayer = PyHelpers.PyPlayer
PyGame = PyHelpers.PyGame()
PyInfo = PyHelpers.PyInfo


iNumPlayers = con.iNumPlayers

class CvRFCEventHandler:

	def __init__(self, eventManager):
		
		self.lastRegionID = -1
		self.bStabilityOverlay = False
		self.EventKeyDown = 6
		self.EventKeyUp = 7
		self.eventManager = eventManager
		
		# initialize base class
		eventManager.addEventHandler("GameStart", self.onGameStart)
		eventManager.addEventHandler("OnLoad", self.onLoadGame)
		eventManager.addEventHandler("OnPreSave", self.onPreSave)
		eventManager.addEventHandler("BeginGameTurn", self.onBeginGameTurn)
		eventManager.addEventHandler("EndGameTurn", self.onEndGameTurn)
		eventManager.addEventHandler("BeginPlayerTurn", self.onBeginPlayerTurn)
		eventManager.addEventHandler("EndPlayerTurn", self.onEndPlayerTurn)
		eventManager.addEventHandler("firstContact", self.onFirstContact)
		eventManager.addEventHandler("cityAcquired", self.onCityAcquired)
		eventManager.addEventHandler("goldenAge", self.onGoldenAge) # srpt
		eventManager.addEventHandler("cityAcquiredAndKept", self.onCityAcquiredAndKept)
		eventManager.addEventHandler("cityRazed", self.onCityRazed)
		eventManager.addEventHandler("cityBuilt", self.onCityBuilt)
		eventManager.addEventHandler("combatResult", self.onCombatResult)
		eventManager.addEventHandler("buildingBuilt", self.onBuildingBuilt)
		eventManager.addEventHandler("projectBuilt", self.onProjectBuilt)
		eventManager.addEventHandler("techAcquired", self.onTechAcquired)
		eventManager.addEventHandler("religionSpread", self.onReligionSpread)
		eventManager.addEventHandler("unitSpreadReligionAttempt", self.onUnitSpreadReligionAttempt)
		eventManager.addEventHandler("playerChangeStateReligion", self.onPlayerChangeStateReligion)
		eventManager.addEventHandler("vassalState", self.onVassalState)
		eventManager.addEventHandler("changeWar", self.onChangeWar)
		eventManager.addEventHandler("unitBuilt", self.onUnitBuilt)
		eventManager.addEventHandler("revolution", self.onRevolution)
		eventManager.addEventHandler("setPlayerAlive", self.onSetPlayerAlive)
		eventManager.addEventHandler("greatPersonBorn", self.onGreatPersonBorn)
		eventManager.addEventHandler("kbdEvent", self.onKbdEvent)		
		
		self.rnf = RiseAndFall.RiseAndFall()
		self.cnm = CityNameManager.CityNameManager()
		self.res = Resources.Resources()
		self.rel = Religions.Religions()
		self.barb = Barbs.Barbs()
		self.aiw = AIWars.AIWars()
		self.vic = Victory.Victory()
		self.pla = Plague.Plague()
		self.com = Communications.Communications()
		self.dc = DynamicCivs.DynamicCivs()
		self.corp = Companies.Companies()
		self.rfccwaiw = RFCCWAIWars.RFCCWAIWars()


	def onGameStart(self, argsList):
		'Called at the start of the game'
		sd.setup()
		self.rnf.setup()
		self.aiw.setup()
		self.pla.setup()
		self.dc.setup()
		self.rel.setup()
		self.barb.setup()
		sd.save()
		
		# update unit art styles of independents
		for iLoopPlayer in range(con.iIndependent, con.iNomad3):
			unitList = PyPlayer(iLoopPlayer).getUnitList()
			for pUnit in unitList:
				UnitArtStyler.updateUnitArt(pUnit)
		
		return 0


	def onPreSave(self, argsList):
		'called before a game is actually saved'
		sd.save() # pickle & save script data


	def onLoadGame(self, argsList):
		sd.load() # load & unpickle script data
		return 0


	def onBeginGameTurn(self, argsList):
		'Called at the beginning of the end of each turn'
		iGameTurn = argsList[0]
		
		#print ("onBeginGameTurn, iGameTurn=", iGameTurn)
		#self.printDebug(iGameTurn)
		
		self.rnf.checkTurn(iGameTurn)
		self.res.checkTurn(iGameTurn)
		self.barb.checkTurn(iGameTurn)
		self.rel.checkTurn(iGameTurn)
		self.aiw.checkTurn(iGameTurn)
		self.pla.checkTurn(iGameTurn)
		self.com.checkTurn(iGameTurn)
		self.corp.checkTurn(iGameTurn)
		self.rfccwaiw.checkTurn(iGameTurn)
		
		
		
		# Refugees
		if sd.getVal('tRazedCityData'):
			tRazedCityData = sd.getVal('tRazedCityData') #(city.getNameKey(), city.getX(), city.getY())
			sd.delVal('tRazedCityData')
			cityList = []
			for x in range(tRazedCityData[0]-12, tRazedCityData[0]+12, 1):
				if x >= 0 and x < con.iMapWidth:
					for y in range(tRazedCityData[1]-12, tRazedCityData[1]+12, 1):
						if y >= 0 and y < con.iMapHeight:
							pCurrent = gc.getMap().plot(x, y)
							if pCurrent.isCity():
								targetCity = pCurrent.getPlotCity()
								cityList.append(targetCity)
			if cityList:
				targetCity = cityList[gc.getGame().getSorenRandNum(len(cityList), 'Random city')]
				gc.getPlayer(targetCity.getOwner()).initTriggeredData(gc.getInfoTypeForString("EVENTTRIGGER_REFUGEES"), True, targetCity.getID(), targetCity.getX(), targetCity.getY(), -1, -1, -1, -1, -1, -1, tRazedCityData[2])
		
		


	def onEndGameTurn(self, argsList):
		'Called at the end of the end of each turn'
		iGameTurn = argsList[0]
		#print ("onEndGameTurn, iGameTurn=", iGameTurn)

	def onBeginPlayerTurn(self, argsList):
		'Called at the beginning of a players turn'
		iGameTurn, iPlayer = argsList
		#print ("onBeginPlayerTurn, iGameTurn=", iGameTurn, "iPlayer=", iPlayer)
		pPlayer = gc.getPlayer(iPlayer)
		
		if self.rnf.getDeleteMode(0) != -1:
			self.rnf.deleteMode(iPlayer)
		
		self.pla.checkPlayerTurn(iGameTurn, iPlayer)
		
		if pPlayer.isAlive() and iPlayer < iNumPlayers:
			self.vic.checkPlayerTurn(iGameTurn, iPlayer)
			sd.setLastTurnAlive(iPlayer, iGameTurn)
			


	def onEndPlayerTurn(self, argsList):
		'Called at the end of a players turn'
		iGameTurn, iPlayer = argsList
		#print ("onEndPlayerTurn, iGameTurn=", iGameTurn, "iPlayer=", iPlayer)

	def onFirstContact(self, argsList):
		'Contact'
		iTeamX,iHasMetTeamY = argsList


	def onBuildingBuilt(self, argsList):
		'Building Completed'
		city, iBuildingType = argsList
		
		iOwner = city.getOwner()
		if iOwner < iNumPlayers:
			#self.rel.onBuildingBuilt(iOwner, iBuildingType, city)
			self.vic.onBuildingBuilt(iOwner, iBuildingType, city)
			self.rfccwaiw.onBuildingBuilt(iBuildingType, city)
			#if iBuildingType >= con.iHeroicEpic:
				#if iOwner < iNumPlayers:
					#print ("STABILITY CHECK wonder, iOwner=", gc.getPlayer(iOwner).getCivilizationShortDescription(0), "year=", utils.getYear())
					#self.rnf.stabilityCheck(iOwner, True, 1)
		# Trajan's Column
		if iBuildingType == con.iTrajansColumn:
			gc.getTeam(gc.getPlayer(iOwner).getTeam()).setHasTech(con.iTrajansColumnFunctionTech, True, iOwner, False, False)

	def onProjectBuilt(self, argsList):
		'Project Completed'
		pCity, iProjectType = argsList


	def onTechAcquired(self, argsList):
		'Tech Acquired'
		iTechType, iTeam, iPlayer, bAnnounce = argsList
		
		if iPlayer < iNumPlayers and iTechType not in [con.iStabilityStable, con.iStabilityUnstable, con.iStabilityCollapsing]:
			self.vic.onTechAcquired(iTechType, iPlayer) # Franks
			self.res.onTechAcquired(iTechType)
			#self.rel.onTechAcquired(iTechType, iPlayer)
			if iPlayer < con.iNumMajPlayers and gc.getPlayer(iPlayer).getNumCities() > 1 and utils.getYear() >  (con.tBirth[sd.getCivilization(iPlayer)]) + 50 and iTechType in con.lStabilityTechs:
			#if iPlayer < con.iNumMajPlayers:
				#if gc.getPlayer(iPlayer).getNumCities() > 1:
					#print ("ERROR iPlayer=", iPlayer, "sd.getCivilization(iPlayer)", sd.getCivilization(iPlayer))
					#if utils.getYear() >  (con.tBirth[sd.getCivilization(iPlayer)]) + 50:
				if utils.getYear() < con.tFall[iPlayer]:
					if (sd.getLastRebellion(iPlayer)) < utils.getYear() - 30:
						print ("STABILITY CHECK tech, iPlayer=", gc.getPlayer(iPlayer).getCivilizationShortDescription(0), "year=", utils.getYear())
						self.rnf.stabilityCheck(iPlayer, 0)
				else:
					if (sd.getLastRebellion(iPlayer)) < utils.getYear() - 10:
						print ("STABILITY CHECK tech, iPlayer=", gc.getPlayer(iPlayer).getCivilizationShortDescription(0), "year=", utils.getYear())
						self.rnf.stabilityCheck(iPlayer, 0)
				
		if iTechType == con.iTheStirrup:
			gc.getTeam(gc.getPlayer(iPlayer).getTeam()).setHasTech(con.iTrajansColumnFunctionTech, False, utils.getHumanID(), False, False)

	def onGoldenAge(self, argsList):
		'Golden Age'
		iPlayer = argsList[0]
		if iPlayer < iNumPlayers:
			self.vic.onGoldenAge(iPlayer)
			print ("STABILITY RESET GA, iPlayer=", gc.getPlayer(iPlayer).getCivilizationShortDescription(0), "year=", utils.getYear())
			pTeam = gc.getTeam(gc.getPlayer(iPlayer).getTeam())
			pTeam.setHasTech(con.iStabilityStable, True, iPlayer, False, False) ## srpt stability conversion
			pTeam.setHasTech(con.iStabilityUnstable, False, iPlayer, False, False)
			pTeam.setHasTech(con.iStabilityCollapsing, False, iPlayer, False, False)
	
	
	def onReligionSpread(self, argsList):
		'Religion Has Spread to a City'
		iReligion, iOwner, pSpreadCity = argsList
		self.rel.onReligionSpread(iReligion, iOwner, pSpreadCity)
		self.vic.onReligionSpread()
		self.vic.maccabeanCheck()


	def onCityBuilt(self, argsList):
		'City Built'
		city = argsList[0]
		
		iOwner = city.getOwner()
		
		if iOwner == con.iByzantines and (city.getX(), city.getY()) == con.tCapitals[con.iByzantines]:
			city.changeCulture(con.iByzantines, 30, True)
		
		self.cnm.assignName(city)
		self.rel.onCityBuilt(city)
		self.rfccwaiw.onCityBuilt(city, iOwner)
		#Rhye - delete culture of barbs and minor civs to prevent weird unhappiness
		pCurrent = gc.getMap().plot(city.getX(), city.getY())
		for i in range(con.iNumTotalPlayers - iNumPlayers):
			iMinorCiv = i + iNumPlayers
			pCurrent.setCulture(iMinorCiv, 0, True)
		pCurrent.setCulture(con.iBarbarian, 0, True)
		
		if iOwner < iNumPlayers:
			utils.spreadMajorCulture(iOwner, city.getX(), city.getY())
			if gc.getPlayer(iOwner).getNumCities() < 2:
				gc.getPlayer(iOwner).AI_updateFoundValues(False); # fix for settler maps not updating after 1st city is founded


	def onCityRazed(self, argsList):
		'City Razed'
		city, iPlayer = argsList
		iPreviousOwner = city.getOwner()
		#print ("onCityRazed", city.getName(), "iPlayer=", gc.getPlayer(iPlayer).getCivilizationShortDescription(0), "iPreviousOwner=", gc.getPlayer(iPreviousOwner).getCivilizationShortDescription(0), "year=", utils.getYear())
		if iPreviousOwner == iPlayer and city.getPreviousOwner() != -1:
			iPreviousOwner = city.getPreviousOwner()
		self.pla.onCityRazed(argsList)
		self.rel.onCityRazed(argsList)
		self.rfccwaiw.onCityRazed(argsList)
		if iPlayer != con.iBarbarian or not (gc.getTeam(gc.getPlayer(iPreviousOwner).getTeam()).isHasTech(con.iTrajansColumnFunctionTech)):
			if iPreviousOwner < con.iNumPlayers and gc.getPlayer(iPreviousOwner).getNumCities() > 1 and gc.getPlayer(iPreviousOwner).getAnarchyTurns() < 1 and gc.getPlayer(iPreviousOwner).getGoldenAgeTurns() < 1:
				if utils.getYear() < con.tFall[iPreviousOwner]:
					if (sd.getLastRebellion(iPreviousOwner)) < utils.getYear() - 5:
						print ("STABILITY CHECK city razed iPreviousOwner=", gc.getPlayer(iPreviousOwner).getCivilizationShortDescription(0), "year=", utils.getYear())
						regionID = gc.getMap().plot(city.getX(), city.getY()).getRegionID()
						if regionID in utils.getCoreRegions(sd.getCivilization(iPreviousOwner)):
							self.rnf.stabilityCheck(iPreviousOwner, -3)
						elif regionID in utils.getNormalRegions(sd.getCivilization(iPreviousOwner)):
							if not (gc.getTeam(gc.getPlayer(iPreviousOwner).getTeam()).isHasTech(con.iStabilityStable)):
								self.rnf.stabilityCheck(iPreviousOwner, -2)
						else:
							if not (gc.getTeam(gc.getPlayer(iPreviousOwner).getTeam()).isHasTech(con.iStabilityStable)):
								self.rnf.stabilityCheck(iPreviousOwner, -1)
				else:
					print ("STABILITY CHECK city razed iPreviousOwner=", gc.getPlayer(iPreviousOwner).getCivilizationShortDescription(0), "year=", utils.getYear())
					regionID = gc.getMap().plot(city.getX(), city.getY()).getRegionID()
					if regionID in utils.getCoreRegions(sd.getCivilization(iPreviousOwner)):
						self.rnf.stabilityCheck(iPreviousOwner, -3)
					elif regionID in utils.getNormalRegions(sd.getCivilization(iPreviousOwner)):
						if not (gc.getTeam(gc.getPlayer(iPreviousOwner).getTeam()).isHasTech(con.iStabilityStable)):
							self.rnf.stabilityCheck(iPreviousOwner, -2)
					else:
						if not (gc.getTeam(gc.getPlayer(iPreviousOwner).getTeam()).isHasTech(con.iStabilityStable)):
							self.rnf.stabilityCheck(iPreviousOwner, -1)
				if iPlayer < con.iNumPlayers and gc.getPlayer(iPreviousOwner).getNumCities() > 1 and gc.getPlayer(iPreviousOwner).getAnarchyTurns() < 1 and gc.getPlayer(iPreviousOwner).getGoldenAgeTurns() < 1:
					print ("STABILITY CHECK city razed iPlayer=", gc.getPlayer(iPlayer).getCivilizationShortDescription(0), "year=", utils.getYear())
					regionID = gc.getMap().plot(city.getX(), city.getY()).getRegionID()
					if regionID in utils.getCoreRegions(sd.getCivilization(iPlayer)):
						self.rnf.stabilityCheck(iPlayer, -9)
					elif regionID in utils.getNormalRegions(sd.getCivilization(iPlayer)):
						self.rnf.stabilityCheck(iPlayer, -6)
					else:
						self.rnf.stabilityCheck(iPlayer, -3)
			# Refugees
			sd.setVal('tRazedCityData', (city.getX(), city.getY(), city.getNameKey()))


	def onCityAcquired(self, argsList):
		'City Acquired'
		iPreviousOwner, iNewOwner, city, bConquest, bTrade = argsList
		pNewOwner = gc.getPlayer(iNewOwner)
		#print ("city acquired", city.getName(), "year=", utils.getYear())
		#print ("iNewOwner=", gc.getPlayer(iNewOwner).getCivilizationShortDescription(0), "iPreviousOwner=", gc.getPlayer(iPreviousOwner).getCivilizationShortDescription(0))
		self.cnm.renameCity(city, iNewOwner)
		self.rnf.checkCapitalsOnCapture(city, iNewOwner) # edead: free capital move for the AI

		if bConquest:
			if iNewOwner != con.iBarbarian or not (gc.getTeam(gc.getPlayer(iPreviousOwner).getTeam()).isHasTech(con.iTrajansColumnFunctionTech)):
				if iPreviousOwner < con.iNumPlayers and gc.getPlayer(iPreviousOwner).getNumCities() >= 1 and gc.getPlayer(iPreviousOwner).getGoldenAgeTurns() < 1:
					if utils.getYear() < con.tFall[iPreviousOwner]:
						if (sd.getLastRebellion(iPreviousOwner)) < utils.getYear() - 5:
							print ("STABILITY CHECK city lost iNewOwner=", iNewOwner, "iPreviousOwner=", iPreviousOwner, "year=", utils.getYear())
							regionID = gc.getMap().plot(city.getX(), city.getY()).getRegionID()
							if regionID in utils.getCoreRegions(sd.getCivilization(iPreviousOwner)):
								self.rnf.stabilityCheck(iPreviousOwner, -3)
							elif regionID in utils.getNormalRegions(sd.getCivilization(iPreviousOwner)): 
								if not (gc.getTeam(gc.getPlayer(iPreviousOwner).getTeam()).isHasTech(con.iStabilityStable)):
									self.rnf.stabilityCheck(iPreviousOwner, -2)
							else: 
								if not (gc.getTeam(gc.getPlayer(iPreviousOwner).getTeam()).isHasTech(con.iStabilityStable)):
									self.rnf.stabilityCheck(iPreviousOwner, -1)
					else:
						print ("STABILITY CHECK city lost iNewOwner=", iNewOwner, "iPreviousOwner=", iPreviousOwner, "year=", utils.getYear())
						regionID = gc.getMap().plot(city.getX(), city.getY()).getRegionID()
						if regionID in utils.getCoreRegions(sd.getCivilization(iPreviousOwner)):
							self.rnf.stabilityCheck(iPreviousOwner, -3)
						elif regionID in utils.getNormalRegions(sd.getCivilization(iPreviousOwner)): 
							if not (gc.getTeam(gc.getPlayer(iPreviousOwner).getTeam()).isHasTech(con.iStabilityStable)):
								self.rnf.stabilityCheck(iPreviousOwner, -2)
						else: 
							if not (gc.getTeam(gc.getPlayer(iPreviousOwner).getTeam()).isHasTech(con.iStabilityStable)):
								self.rnf.stabilityCheck(iPreviousOwner, -1)
						
			
		if iNewOwner < iNumPlayers:
			utils.spreadMajorCulture(iNewOwner, city.getX(), city.getY())
			self.pla.onCityAcquired(iPreviousOwner, iNewOwner, city)
			self.dc.onCityAcquired(argsList)
				
			
		
		
		self.rel.onCityAcquired(argsList)
		
		self.vic.maccabeanCheck()
		self.corp.onCityAcquired(argsList)
		self.vic.onCityAcquired(argsList)
		self.rfccwaiw.onCityAcquired(argsList)
		self.rnf.onCityAcquired(argsList)
		
		# Move the palace to historical backup capital
		if iPreviousOwner < iNumPlayers:
			if (city.getX(), city.getY()) == con.tCapitals[iPreviousOwner]:
				self.rnf.moveCapital(con.tBackupCapitals[iPreviousOwner], iPreviousOwner, True)


	def onCityAcquiredAndKept(self, argsList):
		'City Acquired and Kept'
		iOwner,pCity,bMassacre = argsList
		iVictims = self.rel.onCityAcquiredAndKept(argsList) # massacre
		self.rfccwaiw.onCityAcquiredAndKept(argsList)
		
		sd.setNumCities(iOwner, gc.getPlayer(iOwner).getNumCities())
		


	def onCombatResult(self, argsList):
		pWinningUnit, pLosingUnit, pAttackingUnit = argsList
		
		self.vic.onCombatResult(argsList)
		self.rnf.immuneMode(argsList)
		self.rfccwaiw.enslaveUnit(argsList)


	def onPlayerChangeStateReligion(self, argsList):
		'Player changes his state religion'
		iPlayer, iNewReligion, iOldReligion = argsList
		
		if iPlayer < iNumPlayers:
			self.rel.onPlayerChangeStateReligion(argsList)
			self.dc.onPlayerChangeStateReligion(argsList)
			self.corp.onPlayerChangeStateReligion(argsList)
			self.vic.onPlayerChangeStateReligion(argsList)
			self.rnf.setCivicsStability(iPlayer)
			#if gc.getPlayer(iPlayer).getNumCities() > 1 and gc.getPlayer(iPlayer).getGoldenAgeTurns() < 1:
				#print ("STABILITY CHECK religion change, iPlayer=", gc.getPlayer(iPlayer).getCivilizationShortDescription(0), "year=", utils.getYear())
				#self.rnf.stabilityCheck(iPlayer, False, 0)


	def onVassalState(self, argsList):
		'Vassal State'
		iMaster, iVassal, bVassal = argsList
		
		self.dc.onVassalState(argsList)
		#print ("STABILITY CHECK vassal, iMaster=", gc.getPlayer(iMaster).getCivilizationShortDescription(0), "iVassal=", gc.getPlayer(iVassal).getCivilizationShortDescription(0), "year=", utils.getYear())
		#self.rnf.stabilityCheck(iMaster, True, 1)
		#self.rnf.stabilityCheck(iVassal, True, 0)

	def onChangeWar(self, argsList):
		'War Status Changes'
		bIsWar, iTeam, iRivalTeam = argsList
		'''if bIsWar:
			if iTeam < con.iNumPlayers and iRivalTeam < con.iNumPlayers:
				print ("War declared, iTeam=", gc.getPlayer(iTeam).getCivilizationShortDescription(0), "iRivalTeam=", gc.getPlayer(iRivalTeam).getCivilizationShortDescription(0), "year=", utils.getYear()) 
		else:
			if iTeam < con.iNumPlayers and iRivalTeam < con.iNumPlayers:
				print ("Peace, iTeam=", gc.getPlayer(iTeam).getCivilizationShortDescription(0), "iRivalTeam=", gc.getPlayer(iRivalTeam).getCivilizationShortDescription(0), "year=", utils.getYear())
		if iTeam < iNumPlayers and iRivalTeam < iNumPlayers:
			self.rel.onChangeWar(argsList)'''
			
		if gc.getPlayer(con.iRome).isAlive():
			print "Roman triggers"
			self.rfccwaiw.checkRomanWarTriggers(argsList)
		
		'''if iTeam < iNumPlayers and iRivalTeam < iNumPlayers:
			if bIsWar:
				if iTeam < con.iNumPlayers and gc.getPlayer(iTeam).getNumCities() > 1 and gc.getPlayer(iTeam).getAnarchyTurns() < 1 and gc.getPlayer(iTeam).getGoldenAgeTurns() < 1 and utils.getYear() >  (con.tBirth[iTeam] + 10):
					print ("STABILITY CHECK war, iTeam=", gc.getPlayer(iTeam).getCivilizationShortDescription(0), "year=", utils.getYear())
					self.rnf.stabilityCheck(iTeam, False, 1)
				if iRivalTeam < con.iNumPlayers and gc.getPlayer(iRivalTeam).getNumCities() < 2 and gc.getPlayer(iRivalTeam).getAnarchyTurns() < 1 and gc.getPlayer(iRivalTeam).getGoldenAgeTurns() < 1 and utils.getYear() >  (con.tBirth[iRivalTeam] + 10):
					print ("STABILITY CHECK war, iRivalTeam=", gc.getPlayer(iRivalTeam).getCivilizationShortDescription(0))
					self.rnf.stabilityCheck(iRivalTeam, False, -1)
			else:
				print ("STABILITY CHECK peace, iTeam=", gc.getPlayer(iTeam).getCivilizationShortDescription(0), "iRivalTeam=", gc.getPlayer(iRivalTeam).getCivilizationShortDescription(0), "year=", utils.getYear())
				self.rnf.stabilityCheck(iTeam, True, 1)
				self.rnf.stabilityCheck(iRivalTeam, True, -1)'''
		


	def onUnitSpreadReligionAttempt(self, argsList):
		'Unit tries to spread religion to a city'
		pUnit, iReligion, bSuccess = argsList
		
		self.rel.onUnitSpreadReligionAttempt(argsList)
		self.vic.onUnitSpreadReligionAttempt(argsList) 


	def onUnitBuilt(self, argsList):
		'Unit Completed'
		pCity, pUnit = argsList
		
		iPlayer = pUnit.getOwner()
		pPlayer = gc.getPlayer(iPlayer)
		iUnitType = pUnit.getUnitType()
		
		#self.rel.onUnitBuilt(argsList)
		
		# Update UnitArtStyle for independents
		if iPlayer >= con.iNumPlayers:
			UnitArtStyler.updateUnitArt(pUnit)


	def onRevolution(self, argsList):
		'Called at the start of a revolution'
		iPlayer = argsList[0]
		
		if iPlayer < iNumPlayers:
			self.dc.onRevolution(iPlayer)
		
		if iPlayer < iNumPlayers:
			self.rfccwaiw.onRevolution(iPlayer)
			if iPlayer < iNumPlayers and gc.getPlayer(iPlayer).getNumCities() > 1 and gc.getPlayer(iPlayer).getGoldenAgeTurns() < 1:
				self.rnf.setCivicsStability(iPlayer)
				print ("STABILITY CHECK revolution, iPlayer=", gc.getPlayer(iPlayer).getCivilizationShortDescription(0), "year=", utils.getYear())
				self.rnf.stabilityCheck(iPlayer, 0)


	def onSetPlayerAlive(self, argsList):
		'Set Player Alive Event'
		iPlayer, bNewValue = argsList
		if iPlayer < iNumPlayers:
			self.res.onSetPlayerAlive(argsList)
			self.dc.onSetPlayerAlive(argsList)
			
		self.vic.maccabeanCheck()


	def onGreatPersonBorn(self, argsList):
		'Unit Promoted'
		pUnit, iPlayer, pCity = argsList
		
		self.vic.onGreatPersonBorn(argsList) # Seleucids
		#self.rel.onGreatPersonBorn(iPlayer)
		self.rfccwaiw.onGreatPersonBorn(argsList)
		'''if iPlayer < iNumPlayers:
			print ("STABILITY CHECK GP, iPlayer=", gc.getPlayer(iPlayer).getCivilizationShortDescription(0), "year=", utils.getYear())
			self.rnf.stabilityCheck(iPlayer, True, 1)'''

	# This method handles the key input and will bring up the mercenary manager screen if the 
	# player has at least one city and presses the 'M' key.
	def onKbdEvent(self, argsList):
		'keypress handler - return 1 if the event was consumed'
		
		#Rhye - start debug
		eventType,key,mx,my,px,py = argsList
		theKey=int(key)
		iHuman = utils.getHumanID()
		
		if ( eventType == self.EventKeyDown and theKey == int(InputTypes.KB_B) and self.eventManager.bAlt):
			iGameTurn = gc.getGame().getGameTurn()
		
		if ( eventType == self.EventKeyDown and theKey == int(InputTypes.KB_N) and self.eventManager.bAlt):
			#print("ALT-N")
			# self.printEmbassyDebug()
			# self.printPlotsDebug()
			self.printStabilityDebug()
		
		if ( eventType == self.EventKeyDown and theKey == int(InputTypes.KB_C) and self.eventManager.bAlt and self.eventManager.bShift):
			#print("SHIFT-ALT-C") #picks a dead civ so that autoplay can be started with game.AIplay xx
			iDebugDeadCiv = iMauryans
			#gc.getTeam(gc.getPlayer(iDebugDeadCiv).getTeam()).setHasTech(con.iCalendar, True, iDebugDeadCiv, False, False)
			utils.makeUnit(con.iSpearman, iDebugDeadCiv, (0,0), 1)
			gc.getGame().setActivePlayer(iDebugDeadCiv, False)
			gc.getPlayer(iDebugDeadCiv).setPlayable(True)
		
		if ( eventType == self.EventKeyDown and theKey == int(InputTypes.KB_Q) and self.eventManager.bAlt and self.eventManager.bShift):
			#print("SHIFT-ALT-Q") #enables squatting
			self.rnf.setCheatMode(True);
			CyInterface().addMessage(iHuman, True, con.iDuration, "EXPLOITER!!! ;)", "", 0, "", ColorTypes(con.iRed), -1, -1, True, True)
		

		# keyboard event test
		#if eventType == self.EventKeyDown and px >= 0 and py >= 0 and theKey == 45 and self.eventManager.bCtrl and self.eventManager.bAlt:
			#pPlot = gc.getMap().plot(px,py)
			#iActivePlayer = gc.getGame().getActivePlayer()
			#iActiveTeam = gc.getPlayer(iActivePlayer).getTeam()
			#if pPlot.isCity():
				#CyInterface().addMessage(iHuman, True, con.iDuration, "contact", "", 0, "", ColorTypes(con.iGreen), -1, -1, True, True)
		
		# province highlight
		if eventType == self.EventKeyDown and px >= 0 and py >= 0 and theKey == 45 and self.eventManager.bCtrl and not self.eventManager.bAlt:
			
			pPlot = gc.getMap().plot(px,py)
			iActivePlayer = gc.getGame().getActivePlayer()
			iActiveTeam = gc.getPlayer(iActivePlayer).getTeam()
			iRegionID = pPlot.getRegionID()
			
			# do not show provinces of unrevealed tiles
			if not pPlot.isRevealed(iActiveTeam, False) and not gc.getGame().isDebugMode():
				return
			
			# do not redraw if already drawn
			if self.lastRegionID == iRegionID:
				return
			
			engine = CyEngine()
			
			# clear the highlight
			engine.clearAreaBorderPlots(AreaBorderLayers.AREA_BORDER_LAYER_HIGHLIGHT_PLOT)
			#engine.clearColoredPlots(PlotLandscapeLayers.PLOT_LANDSCAPE_LAYER_RECOMMENDED_PLOTS)
			
			# cache the plot's coords
			self.lastRegionID = pPlot.getRegionID()
			
			# select an appriopriate color
			if pPlot.isWater():
				#color = gc.getColorInfo(gc.getInfoTypeForString("COLOR_HIGHLIGHT_WATER")).getColor()
				return
			else:
				iLevel = utils.getRegionStabilityLevel(iHuman, iRegionID)
				if iLevel == 4:
					color = gc.getColorInfo(gc.getInfoTypeForString("COLOR_HIGHLIGHT_CORE")).getColor()
				elif iLevel == 3:
					color = gc.getColorInfo(gc.getInfoTypeForString("COLOR_HIGHLIGHT_BORDER")).getColor()
				elif iLevel == 2:
					color = gc.getColorInfo(gc.getInfoTypeForString("COLOR_HIGHLIGHT_CONTESTED")).getColor()
				elif iLevel == 1:
					color = gc.getColorInfo(gc.getInfoTypeForString("COLOR_HIGHLIGHT_OUTSIDE")).getColor()
				else:
					color = gc.getColorInfo(gc.getInfoTypeForString("COLOR_HIGHLIGHT_FOREIGN")).getColor()
			
			# apply the highlight
			for x in range(con.iMapWidth):
				for y in range(con.iMapHeight):
					pCurrent = gc.getMap().plot(x,y)
					if pCurrent.getRegionID() == iRegionID and (gc.getGame().isDebugMode() or pCurrent.isRevealed(iActiveTeam, False)):
						engine.fillAreaBorderPlot(x, y, color, AreaBorderLayers.AREA_BORDER_LAYER_HIGHLIGHT_PLOT)
			
			return
		
		# clear all hightlights
		if (eventType == self.EventKeyUp and self.eventManager.bCtrl) or (eventType == self.EventKeyDown):
			CyEngine().clearAreaBorderPlots(AreaBorderLayers.AREA_BORDER_LAYER_HIGHLIGHT_PLOT)
			#CyEngine().clearColoredPlots(PlotLandscapeLayers.PLOT_LANDSCAPE_LAYER_RECOMMENDED_PLOTS)
			self.lastRegionID = -1


	def printDebug(self, iGameTurn):
		return
		# if (iGameTurn % 50 == 1):
			# self.printEmbassyDebug()
		# if (iGameTurn % 20 == 0):
			# self.printPlotsDebug()
		#if (iGameTurn % 10 == 0): 
			#self.printStabilityDebug()


	def printStabilityDebug(self):
		print ("Stability")
		for iCiv in range(con.iNumPlayers):
			if (gc.getPlayer(iCiv).isAlive()):
				print ("Base:", sd.getBaseStabilityLastTurn(iCiv), "Modifier:", sd.getStability(iCiv)-sd.getBaseStabilityLastTurn(iCiv), "Total:", sd.getStability(iCiv), "civic", gc.getPlayer(iCiv).getCivics(5), gc.getPlayer(iCiv).getCivilizationDescription(0))
			else:
				print ("dead", iCiv)
		for i in range(con.iNumStabilityParameters):
			print("Parameter", i, utils.getStabilityParameters(i))
		for i in range(con.iNumPlayers):
			print (gc.getPlayer(i).getCivilizationShortDescription(0), "PLOT OWNERSHIP ABROAD:", self.sta.getOwnedPlotsLastTurn(i), "CITY OWNERSHIP LOST:", self.sta.getOwnedCitiesLastTurn(i) )
