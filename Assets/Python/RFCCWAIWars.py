from CvPythonExtensions import *
import CvUtil
import PyHelpers   
import Popup
from StoredData import sd # edead
import Consts as con
import RFCUtils
import DynamicCivs
dc = DynamicCivs.DynamicCivs()
import MercenaryUtils
utils = RFCUtils.RFCUtils()
import Resources
res = Resources.Resources()


# globals
gc = CyGlobalContext()
localText = CyTranslator()
PyPlayer = PyHelpers.PyPlayer

objMercenaryUtils = MercenaryUtils.MercenaryUtils()

iEgypt = con.iEgypt
iCarthage = con.iCarthage
iSeleucids = con.iSeleucids
iPontus = con.iPontus
iMaccabees = con.iMaccabees
iRome = con.iRome
iHan = con.iHan
iBarbarian = con.iBarbarian
iGoguryeo = con.iGoguryeo
iCelts = con.iCelts
iByzantines = con.iByzantines
iRebelRome = con.iRebelRome
iAntigonids = con.iAntigonids
iBactria = con.iBactria
iArabs = con.iArabs

iHuman = utils.getHumanID()

iNumPlayers = con.iNumPlayers

pRome = gc.getPlayer(iRome)
pHan = gc.getPlayer(iHan)
pCarthage = gc.getPlayer(iCarthage)
pAntigonids = gc.getPlayer(iAntigonids)
pSeleucids = gc.getPlayer(iSeleucids)
pEgypt = gc.getPlayer(iEgypt)
pMaccabees = gc.getPlayer(iMaccabees)
pCelts = gc.getPlayer(iCelts)
pByzantines = gc.getPlayer(iByzantines)
pBarbarian = gc.getPlayer(iBarbarian)

teamRome = gc.getTeam(pRome.getTeam())
teamCarthage = gc.getTeam(pCarthage.getTeam())
teamAntigonids = gc.getTeam(pAntigonids.getTeam())
teamSeleucids = gc.getTeam(pSeleucids.getTeam())
teamEgypt = gc.getTeam(pEgypt.getTeam())
teamMaccabees = gc.getTeam(pMaccabees.getTeam())
teamCelts = gc.getTeam(pCelts.getTeam())

tGoguryeoTopLeft = (98, 35)
tGoguryeoBottomRight = (106, 47)


class RFCCWAIWars:

##################################################
### Secure storage & retrieval of script data ###
################################################   


# Roman UP

	def increaseRomanAIVictories(self):
		sd.scriptDict['iRomanAIVictories'] += 1

	def resetRomanAIVictories(self):
		sd.scriptDict['iRomanAIVictories'] = 0

	def getRomanAIVictories(self):
		return sd.scriptDict['iRomanAIVictories']

	def getRomanAIWar(self, iPlayer):
		return sd.scriptDict['lRomanAIWars'][iPlayer]

	def setRomanAIWar(self, iPlayer, iValue):
		sd.scriptDict['lRomanAIWars'][iPlayer] = iValue
		
	def getAlreadySwitched( self ):
		return sd.getAlreadySwitched()

	def setAlreadySwitched( self, bNewValue ):
		sd.setAlreadySwitched(bNewValue)
		
	def getTempFlippingCity( self ):
		return sd.getTempFlippingCity()
		
	def setTempFlippingCity( self, tNewValue ):
		sd.setTempFlippingCity(tNewValue)
		
		
#######################################
### Main methods (Event-Triggered) ###
#####################################  

       	
	def checkTurn(self, iGameTurn):
				
		# Pirates
		#if iGameTurn >= getTurnForYear(con.tBirth[iHuman]):
			#self.pirateCheck()
			
		# Distant conquest
		#for iLoopCiv in range (con.iNumPlayers):
			#if iLoopCiv != iHuman:
				#if sd.getDistantConquest(iLoopCiv, 0) == 1:
					#self.doDistantConquest (iLoopCiv, sd.getDistantConquest (iLoopCiv, 1), sd.getDistantConquest (iLoopCiv, 2))
		
		
			
		if (iGameTurn >= getTurnForYear(con.tBirth[iGoguryeo])):
			self.checkGoguryeoUP()
			
		# Roman indy city allegiance
		if (iGameTurn < getTurnForYear(100)) and (iGameTurn >= getTurnForYear(con.tBirth[iRome] + utils.getTurns(100))) and (iGameTurn % 20 == 0) and iRome != utils.getHumanID() and pRome.isAlive(): #every 20 turns starting 100 years after Rome's birth
			pTargetCity = utils.getRandomMinorCityByRegion(con.lNormalRegions[iRome])
			if (pTargetCity != None):
				iOldOwner = gc.getMap().plot(pTargetCity.getX(),pTargetCity.getY()).getOwner()
				utils.cultureManager((pTargetCity.getX(),pTargetCity.getY()), 100, iRome, iOldOwner, False, False, False)
				utils.flipUnitsInCityBefore((pTargetCity.getX(),pTargetCity.getY()), iRome, iOldOwner)
				self.setTempFlippingCity((pTargetCity.getX(),pTargetCity.getY()))
				utils.flipCity((pTargetCity.getX(),pTargetCity.getY()), 0, 0, iRome, [iOldOwner])
				utils.flipUnitsInCityAfter(self.getTempFlippingCity(), iRome)
				if gc.getPlayer(utils.getHumanID()).canContact(iRome):
					CyInterface().addMessage(utils.getHumanID(), False, con.iDuration, CyTranslator().getText("TXT_KEY_UP_ROMAN_INDY_ASSIMILATION", ()), "", 0, "", ColorTypes(con.iRed), -1, -1, True, True)
			
		# Han indy city allegiance
		if (iGameTurn < getTurnForYear(150)) and (iGameTurn >= getTurnForYear(con.tBirth[iHan] + utils.getTurns(50))) and (iGameTurn % 20 == 0) and iHan != utils.getHumanID() and pHan.isAlive(): #every 20 turns starting 100 years after Han's birth
			pTargetCity = utils.getRandomMinorCityByRegion(con.lNormalRegions[iHan])
			if (pTargetCity != None):
				iOldOwner = gc.getMap().plot(pTargetCity.getX(),pTargetCity.getY()).getOwner()
				utils.cultureManager((pTargetCity.getX(),pTargetCity.getY()), 100, iHan, iOldOwner, False, False, False)
				utils.flipUnitsInCityBefore((pTargetCity.getX(),pTargetCity.getY()), iHan, iOldOwner)
				self.setTempFlippingCity((pTargetCity.getX(),pTargetCity.getY()))
				utils.flipCity((pTargetCity.getX(),pTargetCity.getY()), 0, 0, iHan, [iOldOwner])
				utils.flipUnitsInCityAfter(self.getTempFlippingCity(), iHan)
				if gc.getPlayer(utils.getHumanID()).canContact(iHan):
					CyInterface().addMessage(utils.getHumanID(), False, con.iDuration, CyTranslator().getText("TXT_KEY_UP_HAN_INDY_ASSIMILATION", ()), "", 0, "", ColorTypes(con.iRed), -1, -1, True, True)
				
			

					
					
			
			
	def checkRomanWarTriggers (self, argsList): 
		bIsWar, iTeam, iRivalTeam = argsList
		iHuman = utils.getHumanID()
		if bIsWar:
			# Hannibal
			if (iTeam == iRome) and (iRivalTeam == iCarthage) and (self.getRomanAIWar(iRome) == 0) and (iHuman == iRome):
				self.triggerCarthageHannibalSpawn()
				self.setRomanAIWar(iRome, 1)
			# Roman conquerors
			elif (iTeam == iRome) and (iRome != iHuman) and (iRivalTeam in [iCarthage, iEgypt, iAntigonids, iPontus, iSeleucids]) and (self.getRomanAIWar(iRivalTeam) == 0):
				for regionID in con.lMediterraneanProvinces:
					if utils.checkRegionOwnedCity(iRivalTeam, regionID, True) == True:
						self.romanAIConquestUP(iRivalTeam)
						self.setRomanAIWar(iRivalTeam, 1)
						return
			# Rome defenders vs Carthage
			elif (iTeam == iCarthage) and (iRivalTeam == iRome) and (iHuman == iCarthage):
				self.triggerRomanDefenderSpawn(iTeam)
			# Rome defenders vs Celts
			elif (iTeam == iCelts) and (iRivalTeam == iRome) and (iHuman == iCelts):
				self.triggerRomanDefenderSpawn(iTeam)
			
		else:
			if (iTeam == iRome) and (iRivalTeam == iByzantines) and sd.getCivilization(iByzantines) == iRebelRome and utils.getHumanID() != iRome:
				self.endRomanCivilWar()
			

						
	def romanAIConquestUP(self, iEnemy):
	
		pTargetCity = utils.getRandomRomanTargetCity(iEnemy)
		tPlot = con.tRome

		if (pTargetCity != None):
			tPlot = utils.findNearestLandPlot((pTargetCity.getX(),pTargetCity.getY()), iRome)
		if iEnemy == utils.getHumanID() and utils.getYear() < (-200):
			utils.makeUnitAI(con.iLegionary, iRome, tPlot, UnitAITypes.UNITAI_ATTACK_CITY, 2)
			utils.makeUnitAI(con.iCatapult, iRome, tPlot, UnitAITypes.UNITAI_ATTACK_CITY, 1)
			CyInterface().addMessage(iRome, False, con.iDuration, CyTranslator().getText("TXT_KEY_UP_ROMAN_CONQUESTS",(gc.getPlayer(iEnemy).getCivilizationShortDescriptionKey(),)), "", 0, "", ColorTypes(con.iWhite), -1, -1, True, True)
			CyInterface().addMessage(iEnemy, False, con.iDuration, CyTranslator().getText("TXT_KEY_UP_ROMAN_CONQUESTS_TARGET", ()), "", 0, "", ColorTypes(con.iRed), -1, -1, True, True)
		else:
			utils.makeUnitAI(con.iLegionary, iRome, tPlot, UnitAITypes.UNITAI_ATTACK_CITY, 4)
			utils.makeUnitAI(con.iCatapult, iRome, tPlot, UnitAITypes.UNITAI_ATTACK_CITY, 2)
			CyInterface().addMessage(iRome, False, con.iDuration, CyTranslator().getText("TXT_KEY_UP_ROMAN_CONQUESTS",(gc.getPlayer(iEnemy).getCivilizationShortDescriptionKey(),)), "", 0, "", ColorTypes(con.iWhite), -1, -1, True, True)
			CyInterface().addMessage(iEnemy, False, con.iDuration, CyTranslator().getText("TXT_KEY_UP_ROMAN_CONQUESTS_TARGET", ()), "", 0, "", ColorTypes(con.iRed), -1, -1, True, True)
			print "Roman conquerors landed"
		

				
	def triggerCarthageHannibalSpawn(self):
	
		pTargetCity = utils.getRandomCarthageTargetCity(iRome)
		tPlot = con.tCarthage
		iPop = gc.getPlayer(iCarthage).getRealPopulation()
		if iPop <= 14000:
			iBonus1 = 0
		elif iPop <= 18000:
			iBonus1 = 1
		else:
			iBonus1 = 2
		iBonus2 = iBonus1 + 1
		
		if (pTargetCity != -1):
			tPlot = utils.findNearestLandPlot((pTargetCity.getX(),pTargetCity.getY()), iCarthage)
		if utils.getHumanID() == iRome:
			pUnit = utils.makeUnitAI(con.iWarElephant, iCarthage, tPlot, UnitAITypes.UNITAI_ATTACK_CITY_LEMMING, 1)
			if pUnit:
				self.makeLeader(pUnit, "Hannibal", con.iGreatGeneral5)
				pUnit.setHasPromotion(con.iCombat1, True)
				pUnit.setHasPromotion(con.iCombat2, True)
				pUnit.setHasPromotion(con.iFlanking1, True)
				pUnit.setHasPromotion(con.iFlanking2, True)
			#utils.makeUnitAI(con.iWarElephant, iCarthage, tPlot, UnitAITypes.UNITAI_ATTACK_CITY_LEMMING, (1 + iBonus1))
			utils.makeUnitAI(con.iHeavySpearman, iCarthage, tPlot, UnitAITypes.UNITAI_ATTACK_CITY_LEMMING, (1 + iBonus2))
			utils.makeUnitAI(con.iNumidianCavalry, iCarthage, tPlot, UnitAITypes.UNITAI_ATTACK_CITY_LEMMING, (iBonus2))
		else:
			pUnit = utils.makeUnitAI(con.iWarElephant, iCarthage, tPlot, UnitAITypes.UNITAI_ATTACK_CITY_LEMMING, 1)
			if pUnit:
				self.makeLeader(pUnit, "Hannibal", con.iGreatGeneral5)
				pUnit.setHasPromotion(con.iCombat1, True)
				pUnit.setHasPromotion(con.iCombat2, True)
				pUnit.setHasPromotion(con.iFlanking1, True)
				pUnit.setHasPromotion(con.iFlanking2, True)
			utils.makeUnitAI(con.iWarElephant, iCarthage, tPlot, UnitAITypes.UNITAI_ATTACK_CITY_LEMMING, 1)
			utils.makeUnitAI(con.iHeavySpearman, iCarthage, tPlot, UnitAITypes.UNITAI_ATTACK_CITY_LEMMING, 2)
			utils.makeUnitAI(con.iNumidianCavalry, iCarthage, tPlot, UnitAITypes.UNITAI_ATTACK_CITY_LEMMING, 2)
		
		CyInterface().addMessage(iRome, False, con.iDuration, CyTranslator().getText("TXT_KEY_HANNIBAL_ATTACKS", ()), "", 0, "", ColorTypes(con.iRed), -1, -1, True, True)
		
	def triggerRomanDefenderSpawn(self, iAttacker):
		print "roman defender spawn"
		pRome = gc.getMap().plot(con.tRome[0], con.tRome[1]).getPlotCity()
		iNumLegions = 2
		if pRome.getOwner() == iRome:
			if pRome.getPopulation() > 3:
				iNumLegions += 1
			elif pRome.getPopulation() > 6:
				iNumLegions += 2
			plot = gc.getMap().plot(con.tRome[0], con.tRome[1])
			iNumUnits = plot.getNumUnits()
			for i in range (iNumUnits):
				unit = plot.getUnit(i)
				if unit.getUnitType() == con.iLegionary:
					iNumLegions -= 1
			if iNumLegions >= 1:
				utils.makeUnitAI(con.iLegionary, iRome, con.tRome, UnitAITypes.UNITAI_CITY_DEFENSE, (iNumLegions))
				CyInterface().addMessage(iAttacker, False, con.iDuration, CyTranslator().getText("TXT_KEY_ROME_DEFENDS", ()), "", 0, "", ColorTypes(con.iRed), -1, -1, True, True)
		
	def onGreatPersonBorn(self, argsList):
		pUnit, iPlayer, pCity = argsList
		if pUnit.getUnitType() == con.iGreatGeneral:
			if iPlayer == iRome and iRome != utils.getHumanID():
				self.triggerRomanIndyAttack()
			if iPlayer == iAntigonids and iAntigonids != utils.getHumanID():
				self.triggerAntigonidGreeceAttack()
			if iPlayer == iBactria and iBactria != utils.getHumanID():
				self.triggerBactrianIndiaAttack()
			if iPlayer == iArabs and iArabs != utils.getHumanID():
				self.triggerArabAttack()
		elif pUnit.getUnitType() == con.iGreatProphet:
			if iPlayer == iArabs and iArabs != utils.getHumanID():
				self.triggerArabAttack()
				
	def triggerRomanIndyAttack(self):
	
		if utils.getYear() > 200:
			return
		
		# attack the rebel capital if in a civil war
		#if pByzantines.isAlive() and sd.getCivilization(iByzantines) == iRebelRome:
			#pTargetCity = utils.getRandomCity(iByzantines)
		#else:
		regionList = []
		for regionID in con.lNormalRegions[iRome]:
			if not utils.checkRegionOwnedCity(iRome, regionID):
				regionList.append(regionID)
		pTargetCity = utils.getRandomMinorCityByRegion(regionList)
		
		
		tPlot = con.tRome

		if (pTargetCity != None):
			tPlot = utils.findNearestLandPlot((pTargetCity.getX(),pTargetCity.getY()), iRome)
		utils.makeUnitAI(con.iLegionary, iRome, tPlot, UnitAITypes.UNITAI_ATTACK_CITY_LEMMING, 3)
		utils.makeUnitAI(con.iCatapult, iRome, tPlot, UnitAITypes.UNITAI_ATTACK_CITY_LEMMING, 2)
		utils.makeUnitAI(con.iLegionary, iRome, tPlot, UnitAITypes.UNITAI_ATTACK_CITY, 1)
		if gc.getPlayer(utils.getHumanID()).canContact(iRome):
			CyInterface().addMessage(utils.getHumanID(), False, con.iDuration, CyTranslator().getText("TXT_KEY_UP_ROMAN_INDY_CONQUERORS", ()), "", 0, "", ColorTypes(con.iRed), -1, -1, True, True)
		print "Roman indy attack triggered"
		
	def triggerAntigonidGreeceAttack(self):
	
		pTargetCity = utils.getRandomMinorCityByRegion([con.rGreece])

		if (pTargetCity != None):
			gc.getTeam(gc.getPlayer(iAntigonids).getTeam()).declareWar(pTargetCity.getOwner(), True, -1)
			tPlot = utils.findNearestLandPlot((pTargetCity.getX(),pTargetCity.getY()), iAntigonids)
			utils.makeUnitAI(con.iHeavySpearman, iAntigonids, tPlot, UnitAITypes.UNITAI_ATTACK_CITY_LEMMING, 2)
			utils.makeUnitAI(con.iCatapult, iAntigonids, tPlot, UnitAITypes.UNITAI_ATTACK_CITY_LEMMING, 1)
			utils.makeUnitAI(con.iAntigonidPeltast, iAntigonids, tPlot, UnitAITypes.UNITAI_ATTACK_CITY, 1)
			if gc.getPlayer(utils.getHumanID()).canContact(iAntigonids):
				CyInterface().addMessage(utils.getHumanID(), False, con.iDuration, CyTranslator().getText("TXT_KEY_UP_ANTIGONID_INDY_CONQUERORS", ()), "", 0, "", ColorTypes(con.iRed), -1, -1, True, True)
			print "Antigond Greek attack triggered"
			
	def triggerBactrianIndiaAttack(self):
	
		pTargetCity = utils.getRandomMinorCityByRegion([con.rGandhara, con.rSindh, con.rPunjab])

		if (pTargetCity != None):
			gc.getTeam(gc.getPlayer(iBactria).getTeam()).declareWar(pTargetCity.getOwner(), True, -1)
			tPlot = utils.findNearestLandPlot((pTargetCity.getX(),pTargetCity.getY()), iBactria)
			utils.makeUnitAI(con.iHetairoi, iBactria, tPlot, UnitAITypes.UNITAI_ATTACK_CITY_LEMMING, 2)
			utils.makeUnitAI(con.iCatapult, iBactria, tPlot, UnitAITypes.UNITAI_ATTACK_CITY_LEMMING, 1)
			utils.makeUnitAI(con.iArcher, iBactria, tPlot, UnitAITypes.UNITAI_ATTACK_CITY, 2)
			if gc.getPlayer(utils.getHumanID()).canContact(iBactria):
				CyInterface().addMessage(utils.getHumanID(), False, con.iDuration, CyTranslator().getText("TXT_KEY_UP_BACTRIAN_INDY_CONQUERORS", ()), "", 0, "", ColorTypes(con.iRed), -1, -1, True, True)
			print "Bactrian Gandhara attack triggered"
			
	def triggerArabAttack(self):
	
		pTargetCity = utils.getRandomMinorCityByRegion(con.lNormalRegions[con.iArabs])

		if (pTargetCity != None):
			tPlot = utils.findNearestLandPlot((pTargetCity.getX(),pTargetCity.getY()), iArabs)
			utils.makeUnitAI(con.iArabiaGhazi, iArabs, tPlot, UnitAITypes.UNITAI_ATTACK_CITY_LEMMING, 3)
			utils.makeUnitAI(con.iTrebuchet, iArabs, tPlot, UnitAITypes.UNITAI_ATTACK_CITY_LEMMING, 2)
			utils.makeUnitAI(con.iMarksman, iArabs, tPlot, UnitAITypes.UNITAI_ATTACK_CITY, 2)
			if gc.getPlayer(utils.getHumanID()).canContact(iArabs):
				CyInterface().addMessage(utils.getHumanID(), False, con.iDuration, CyTranslator().getText("TXT_KEY_UP_ARAB_CONQUERORS", ()), "", 0, "", ColorTypes(con.iRed), -1, -1, True, True)
			print "Arab attack triggered"
			

		
		
	def onCityAcquired(self, argsList):
	
		iPreviousOwner, iNewOwner, city, bConquest, bTrade = argsList
		
		pNewOwner = gc.getPlayer(iNewOwner)
		iHuman = utils.getHumanID()
		
		# backup for Roman conquerors during autoplay only
		if bConquest and iNewOwner == iRome and city.plot().getRegionID() in con.lNormalRegions[iRome] and gc.getPlayer(utils.getHumanID()).getNumCities() < 1:
			tPlot = (city.getX(), city.getY())
			utils.makeUnitAI(con.iSpearman, iRome, (tPlot), UnitAITypes.UNITAI_CITY_DEFENSE, 1)
			utils.makeUnitAI(con.iJavelinman, iRome, (tPlot), UnitAITypes.UNITAI_CITY_DEFENSE, 1)
			city.setNumRealBuilding(con.iWalls, 1)
			print "Roman defense and walls"
		
		# Roman Civil War
		if bConquest and iNewOwner == iRome and iPreviousOwner == iByzantines and sd.getCivilization(iByzantines) == iRebelRome:
			if iNewOwner != iHuman:
				self.endRomanCivilWar()
			else:
				if gc.getPlayer(iNewOwner).getNumCities() > gc.getPlayer(iPreviousOwner).getNumCities() * 2:
					self.endRomanCivilWarPopup(iRome)
			
		# freeing of slaves
		if pNewOwner.getCivics(2) != 11:
			
			for iSpecialist in range(city.getFreeSpecialistCount(con.iSettledSlave)):
				city.changeFreeSpecialistCount(con.iSettledSlave, -1)
		
		# land for elephants
		
		teamPreviousOwner = gc.getTeam(gc.getPlayer(iPreviousOwner).getTeam())
		lIndianRegions = [con.rGandhara, con.rPunjab, con.rSindh, con.rMagadha, con.rAvanti, con.rDeccan, con.rSaurashtra, con.rKerala, con.rTamilNadu, con.rKalinka, con.rBangala]
		lIndianCivs = [con.iMauryans, con.iPandyans, con.iSatavahana]
		
		if bTrade and iPreviousOwner < iNumPlayers and iNewOwner in lIndianCivs and pNewOwner.getNumAvailableBonuses(con.iIvory) > 0 and city.plot().getRegionID() in lIndianRegions and utils.getYear() <= -100 and sd.getElephants(iPreviousOwner) == 0:
			pNewOwner = gc.getPlayer(iNewOwner)
			teamPreviousOwner = gc.getTeam(gc.getPlayer(iPreviousOwner).getTeam())
			tPlot = utils.findNearestLandPlot((city.getX(),city.getY()), iPreviousOwner)
			utils.makeUnit(con.iWarElephant, iPreviousOwner, (tPlot), 3)
			utils.makeUnit(con.iSpearman, iNewOwner, (city.getX(), city.getY()), 2)
			teamPreviousOwner.signOpenBorders(iNewOwner)
			sd.setElephants(iPreviousOwner, 1)
		
		# Pyramids
		if city.getNumBuilding(con.iPyramids):
			gc.getTeam(gc.getPlayer(iPreviousOwner).getTeam()).setHasTech(con.iPyramidsFunctionTech, False, iPreviousOwner, False, False)
			apCityList = PyPlayer(iPreviousOwner).getCityList()
			for pLoopCity in apCityList:
				city = pLoopCity.GetCy()
				city.setNumRealBuilding(con.iPyramidsFunctionBuilding, 0)
		
		# Colossus
		if city.getNumBuilding(con.iColossus):
			gc.getTeam(gc.getPlayer(iPreviousOwner).getTeam()).setHasTech(con.iColossusFunctionTech, False, iPreviousOwner, False, False)
			apCityList = PyPlayer(iPreviousOwner).getCityList()
			for pLoopCity in apCityList:
				city = pLoopCity.GetCy()
				city.setNumRealBuilding(con.iColossusFunctionBuilding, 0)
				
		# Trajan's Column
		if city.getNumBuilding(con.iTrajansColumn):
			gc.getTeam(gc.getPlayer(iPreviousOwner).getTeam()).setHasTech(con.iTrajansColumnFunctionTech, False, iPreviousOwner, False, False)
			
		
	def onCityAcquiredAndKept(self, argsList):
		iOwner,pCity,bMassacre = argsList
		# start Jin UP
		if iOwner == con.iJin and pCity.plot().getRegionID() in [con.rGansu, con.rQin, con.rHan, con.rZhao, con.rYan, con.rQi, con.rShu, con.rBa, con.rWu, con.rChu, con.rNanYue]:
			tPlot = (pCity.getX(), pCity.getY())
			if gc.getGame().getSorenRandNum(100, 'chance') > 50:
				utils.makeUnit(con.iMarksman, con.iJin, (tPlot), 1)
			else:
				utils.makeUnit(con.iJinDaoInfantry, con.iJin, (tPlot), 1)
		# end Jin UP
		elif iOwner != utils.getHumanID():
			iCiv = sd.getCivilization(iOwner)
			if utils.getYear() < con.tBirth[iCiv] + 20:
				self.spawnCityDefense(iOwner, iCiv, (pCity.getX(), pCity.getY()))
		
		# Pyramids
		if pCity.getNumBuilding(con.iPyramids):
			gc.getTeam(gc.getPlayer(iOwner).getTeam()).setHasTech(con.iPyramidsFunctionTech, True, iOwner, False, False)
			apCityList = PyPlayer(iOwner).getCityList()
			for pLoopCity in apCityList:
				city = pLoopCity.GetCy()
				pCurrent = gc.getMap().plot(city.getX(),city.getY())
				if pCurrent.getRegionID() == con.rEgypt:
					city.setNumRealBuilding(con.iPyramidsFunctionBuilding, 1)
					
		elif gc.getTeam(gc.getPlayer(iOwner).getTeam()).isHasTech(con.iPyramidsFunctionTech):
			pCurrent = gc.getMap().plot(pCity.getX(),pCity.getY())
			if pCurrent.getRegionID() == con.rEgypt:
				pCity.setNumRealBuilding(con.iPyramidsFunctionBuilding, 1)
		
		# Colossus
		if pCity.getNumBuilding(con.iColossus):
			gc.getTeam(gc.getPlayer(iOwner).getTeam()).setHasTech(con.iColossusFunctionTech, True, iOwner, False, False)
			apCityList = PyPlayer(iOwner).getCityList()
			for pLoopCity in apCityList:
				city = pLoopCity.GetCy()
				regionList = [con.rMallorca, con.rCorsica, con.rSardinia, con.rSicily, con.rMalta, con.rCrete, con.rCyprus, con.rRhodes]
				pCurrent = gc.getMap().plot(city.getX(),city.getY())
				if pCurrent.getRegionID() in regionList:
					city.setNumRealBuilding(con.iColossusFunctionBuilding, 1)
					
		elif gc.getTeam(gc.getPlayer(iOwner).getTeam()).isHasTech(con.iColossusFunctionTech):
			regionList = [con.rMallorca, con.rCorsica, con.rSardinia, con.rSicily, con.rMalta, con.rCrete, con.rCyprus, con.rRhodes]
			pCurrent = gc.getMap().plot(pCity.getX(),pCity.getY())
			if pCurrent.getRegionID() in regionList:
				pCity.setNumRealBuilding(con.iColossusFunctionBuilding, 1)
		
		# Trajan's Column
		if pCity.getNumBuilding(con.iTrajansColumn):
			gc.getTeam(gc.getPlayer(iOwner).getTeam()).setHasTech(con.iTrajansColumnFunctionTech, True, iOwner, False, False)
		
		# cancellation of conquerors
		if gc.getTeam(gc.getPlayer(iOwner).getTeam()).isHasTech(con.iImperialismTech):
			iMaxNumProvinces = 0
			iCurrentNumProvinces = 0
			for regionID in utils.getCoreRegions(sd.getCivilization(iOwner)):
				iMaxNumProvinces += 1
				if utils.checkRegionControl(iOwner, regionID):
					iCurrentNumProvinces += 1
			if (iCurrentNumProvinces*10) / (iMaxNumProvinces) > 9:
				gc.getTeam(gc.getPlayer(iOwner).getTeam()).setHasTech(con.iImperialismTech, False, iOwner, False, False)
		
	
	
	def onBuildingBuilt(self, iBuildingType, city):
	
	
		#if iBuildingType == con.iInvasionProject:
			#city.setNumRealBuilding(con.iInvasionProject, 0)
			#self.triggerAIInvasion(city.getOwner())
	
		# Gokturk UB
		if iBuildingType == con.iGokturkOrkhonInscription:
			city.changeCulture(con.iGokturks, 30, True)
			
	def enslaveUnit(self, argsList): #Real Slavery by Sevo
		pWinningUnit,pLosingUnit,pAttackingUnit = argsList
		iWinningPlayer = pWinningUnit.getOwner()
		iLosingPlayer = pLosingUnit.getOwner()
		iAttackingPlayer = pAttackingUnit.getOwner()
		pWinningPlayer = gc.getPlayer(pWinningUnit.getOwner())
		pLosingPlayer = gc.getPlayer(pLosingUnit.getOwner())
		pAttackingPlayer = gc.getPlayer(pAttackingUnit.getOwner())
		iHuman = utils.getHumanID()
		
		if pWinningPlayer.getID() == con.iKhazars:
			iRandom = gc.getGame().getSorenRandNum(100, 'capture chance')
			if pLosingUnit.getOwner() == iBarbarian:
				if (iRandom < 30):
					if pLosingUnit.getUnitType() == con.iHorseman or pLosingUnit.getUnitType() == con.iHorseman_Scythian or pLosingUnit.getUnitType() == con.iHorseman_Sarmatian or pLosingUnit.getUnitType() == con.iHorseman_Xiongnu or pLosingUnit.getUnitType() == con.iHorseArcher or pLosingUnit.getUnitType() == con.iHorseArcher_Scythian or pLosingUnit.getUnitType() == con.iHorseArcher_Sarmatian or pLosingUnit.getUnitType() == con.iHorseArcher_Xiongnu:
						pNewUnit = pWinningPlayer.initUnit(pLosingUnit.getUnitType(), pWinningUnit.getX(), pWinningUnit.getY(), UnitAITypes.UNITAI_ATTACK_CITY, DirectionTypes.DIRECTION_SOUTH)
						CyInterface().addMessage(pWinningPlayer.getID(),True,15,CyTranslator().getText("TXT_KEY_UP_KHAZARS_WIN", ()),'SND_REVOLTEND',1,'Art/Units/Slave/button_slave.dds',ColorTypes(8),pWinningUnit.getX(),pWinningUnit.getY(),True,True)
						CyInterface().addMessage(pLosingPlayer.getID(),True,15,CyTranslator().getText("TXT_KEY_UP_ENSLAVE_LOSE", ()),'SND_REVOLTEND',1,'Art/Units/Slave/button_slave.dds',ColorTypes(7),pWinningUnit.getX(),pWinningUnit.getY(),True,True)
						return
						

		
		
		if (pWinningPlayer.getCivics(2) != con.iSlaveryCivic):
			return

		
		cLosingUnit = PyHelpers.PyInfo.UnitInfo(pLosingUnit.getUnitType())
		
		
		
		if (pLosingUnit.getUnitType() < con.iJavelinman):
			return
		
		# Only enslave land units!!
		if (cLosingUnit.getDomainType() == gc.getInfoTypeForString("DOMAIN_LAND")):
			iThreshold = 20
			iRandom = gc.getGame().getSorenRandNum(100, 'capture chance')
			if pLosingUnit.getOwner() == iBarbarian:
				iThreshold += 20
			if iWinningPlayer == iAttackingPlayer:
				iThreshold += 10
				#print ("pWinningPlayer.getCapitalCity().productionLeft()", pWinningPlayer.getCapitalCity().productionLeft())
				if (iRandom < iThreshold):
					if iWinningPlayer != iHuman and pWinningPlayer.getCapitalCity().isProductionBuilding() and pWinningPlayer.getCapitalCity().productionLeft() > 45:
						pWinningPlayer.getCapitalCity().changeProduction(60)
						return
					elif iWinningPlayer != iHuman and pWinningPlayer.getGold() < 10:
						pWinningPlayer.changeGold(20)
						return
					else:
						if gc.getMap().plot(pLosingUnit.getX(), pLosingUnit.getY()).getNumDefenders(iLosingPlayer) <= 1:
							pPlot = gc.getMap().plot(pLosingUnit.getX(), pLosingUnit.getY())
							if pPlot.getTerrainType() != con.iWasteland and pPlot.getFeatureType() != con.iJungle:
								pNewUnit = pWinningPlayer.initUnit(con.iSlave, pLosingUnit.getX(), pLosingUnit.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
								CyInterface().addMessage(pWinningPlayer.getID(),True,15,CyTranslator().getText("TXT_KEY_UP_ENSLAVE_WIN", ()),'SND_REVOLTEND',1,'Art/Units/Slave/button_slave.dds',ColorTypes(8),pLosingUnit.getX(),pLosingUnit.getY(),True,True)
								CyInterface().addMessage(pLosingPlayer.getID(),True,15,CyTranslator().getText("TXT_KEY_UP_ENSLAVE_LOSE", ()),'SND_REVOLTEND',1,'Art/Units/Slave/button_slave.dds',ColorTypes(7),pLosingUnit.getX(),pLosingUnit.getY(),True,True)
								pNewUnit.finishMoves()
						else:
							pPlot = gc.getMap().plot(pWinningUnit.getX(), pWinningUnit.getY())
							if pPlot.getTerrainType() != con.iWasteland and pPlot.getFeatureType() != con.iJungle:
								pNewUnit = pWinningPlayer.initUnit(con.iSlave, pWinningUnit.getX(), pWinningUnit.getY(), UnitAITypes.UNITAI_WORKER, DirectionTypes.DIRECTION_SOUTH)
								CyInterface().addMessage(pWinningPlayer.getID(),True,15,CyTranslator().getText("TXT_KEY_UP_ENSLAVE_WIN", ()),'SND_REVOLTEND',1,'Art/Units/Slave/button_slave.dds',ColorTypes(8),pWinningUnit.getX(),pWinningUnit.getY(),True,True)
								CyInterface().addMessage(pLosingPlayer.getID(),True,15,CyTranslator().getText("TXT_KEY_UP_ENSLAVE_LOSE", ()),'SND_REVOLTEND',1,'Art/Units/Slave/button_slave.dds',ColorTypes(7),pWinningUnit.getX(),pWinningUnit.getY(),True,True)
								pNewUnit.finishMoves()
					
				
			elif iAttackingPlayer == iLosingPlayer:
				if (iRandom < iThreshold):
					if iWinningPlayer != iHuman and pWinningPlayer.getCapitalCity().isProductionBuilding():
						pWinningPlayer.getCapitalCity().changeProduction(60)
						return
					elif iWinningPlayer != iHuman and pWinningPlayer.getGold() < 10:
						pWinningPlayer.changeGold(20)
						return
					else:
						pPlot = gc.getMap().plot(pWinningUnit.getX(), pWinningUnit.getY())
						if pPlot.getTerrainType() != con.iWasteland and pPlot.getFeatureType() != con.iJungle:
							pNewUnit = pWinningPlayer.initUnit(con.iSlave, pWinningUnit.getX(), pWinningUnit.getY(), UnitAITypes.UNITAI_WORKER, DirectionTypes.DIRECTION_SOUTH)
							pNewUnit.finishMoves()
							CyInterface().addMessage(pWinningPlayer.getID(),True,15,CyTranslator().getText("TXT_KEY_UP_ENSLAVE_WIN", ()),'SND_REVOLTEND',1,'Art/Units/Slave/button_slave.dds',ColorTypes(8),pWinningUnit.getX(),pWinningUnit.getY(),True,True)
							CyInterface().addMessage(pLosingPlayer.getID(),True,15,CyTranslator().getText("TXT_KEY_UP_ENSLAVE_LOSE", ()),'SND_REVOLTEND',1,'Art/Units/Slave/button_slave.dds',ColorTypes(7),pWinningUnit.getX(),pWinningUnit.getY(),True,True)
							pNewUnit.finishMoves()
					
				
	def onCityRazed(self, argsList):
	
		city, iPlayer = argsList
		iPopulation = city.getPopulation()
		if gc.getPlayer(iPlayer).getCivics(2) == con.iSlaveryCivic:
			if iPlayer != utils.getHumanID() and gc.getPlayer(iPlayer).getCapitalCity().isProductionBuilding():
				gc.getPlayer(iPlayer).getCapitalCity().changeProduction(60 * iPopulation)
				return
			elif iPlayer != utils.getHumanID() and gc.getPlayer(iPlayer).getGold() < 10:
				gc.getPlayer(iPlayer).changeGold(20 * iPopulation)
				return
			else:
				utils.makeUnit(con.iSlave, iPlayer, (city.getX(), city.getY()), iPopulation, DirectionTypes.DIRECTION_SOUTH, UnitAITypes.UNITAI_WORKER)
				
				
				
	def checkGoguryeoUP(self):
		pGoguryeo = gc.getPlayer(iGoguryeo)
		teamGoguryeo = gc.getTeam(pGoguryeo.getTeam()) 
		for x in range(tGoguryeoTopLeft[0], tGoguryeoBottomRight[0]):
			for y in range(tGoguryeoTopLeft[1], tGoguryeoBottomRight[1]):
				pCurrent = gc.getMap().plot( x, y )
				if (pCurrent.getRegionID() == con.rGoguryeo) or (pCurrent.getRegionID() == con.rJin) or (pCurrent.getRegionID() == con.rBuyeo):
					if (pCurrent.getOwner() == iGoguryeo):
						iNumUnitsInAPlot = pCurrent.getNumUnits()
						if (iNumUnitsInAPlot):
							for i in range(iNumUnitsInAPlot):
								unit = pCurrent.getUnit(i)
								if (teamGoguryeo.isAtWar(unit.getOwner())):
									unit.setDamage(unit.getDamage()+8, iGoguryeo)
									
									
	def onRevolution(self, iPlayer):  # freeing of slaves
		pPlayer = gc.getPlayer(iPlayer)
		iCivic2 = pPlayer.getCivics(2)
		if iCivic2 != 11:
			for x in range (con.iMapWidth):
				for y in range (con.iMapHeight):
					plot = gc.getMap().plot(x, y)
					iNumUnits = plot.getNumUnits()
					for i in range (iNumUnits):
						unit = plot.getUnit(i)
						if unit.getOwner() == iPlayer and unit.getUnitType() == con.iSlave:
							unit.kill(False, iPlayer)
			apCityList = PyPlayer(iPlayer).getCityList()
			for pLoopCity in apCityList:
				city = pLoopCity.GetCy()
				for iSpecialist in range(city.getFreeSpecialistCount(con.iSettledSlave)):
					city.changeFreeSpecialistCount(con.iSettledSlave, -1)
			
	def doDistantConquest(self, iCiv, iX, iY):
		
		plot = gc.getMap().plot(iX, iY)
		iNumUnits = plot.getNumUnits()
		for i in range (iNumUnits):
			unit = plot.getUnit(i)
			if unit.getOwner() == iCiv:
				unit.kill(False, iCiv)
		utils.cultureManager((iX, iY), 100, iBarbarian, iCiv, False, False, False)
		if gc.getGame().getGameTurn() < getTurnForYear(50):
			utils.makeUnit(con.iSpearman, iBarbarian, (iX, iY), 1)
			utils.makeUnit(con.iArcher, iBarbarian, (iX, iY), 1)
		else:
			utils.makeUnit(con.iHeavySpearman, iBarbarian, (iX, iY), 1)
			utils.makeUnit(con.iMarksman, iBarbarian, (iX, iY), 1)
		sd.setDistantConquest(iCiv, 0, -1)
		sd.setDistantConquest(iCiv, 1, -1)
		sd.setDistantConquest(iCiv, 2, -1)
		
	# srpt barbarian hire
	def doBarbarianMercenaryHire(self, unit, iX, iY, iPlayer):
	
		iRand = gc.getGame().getSorenRandNum(100, 'Success')
		bSuccess = True
		if iRand < 20:
			bSuccess = False
		pPlayer = gc.getPlayer(unit.getOwner())
		pPlot = CyMap().plot(iX, iY)
		iCost = 0
		iNumUnits = pPlot.getNumUnits()
		for i in range (iNumUnits):
			apUnit = pPlot.getUnit(iNumUnits - (i))
			if apUnit.getOwner() == con.iBarbarian:
				iCost -= objMercenaryUtils.getVirtualMercenaryCost(apUnit.getUnitType(), "temp")
				if bSuccess:
					apUnit.setName("%s %s %s %s %s" %(apUnit.getName(), "(","Barbarian Cohort", con.tRomanNumerals[sd.getBarbMercCount()],")"))
					sd.setBarbMercCount(sd.getBarbMercCount() + 1)
					utils.makeUnit(apUnit.getUnitType(), con.iBarbarian, (con.iFlipX, con.iFlipY), 1, name = apUnit.getName())
					apUnit.kill(0, -1)
			
		if not bSuccess:
			unit.kill(0, -1)
			szText = localText.getText("TXT_KEY_MINOR_EVENT_HIRE_FAILURE", ())
			CyInterface().addMessage(unit.getOwner(), False, con.iDuration, szText, "AS2D_LOSS_EARLY", InterfaceMessageTypes.MESSAGE_TYPE_MINOR_EVENT, "", ColorTypes(con.iRed), -1, -1, False, False)
			pPlayer.changeGold(iCost) 
		else:
			pPlot = CyMap().plot(con.iFlipX, con.iFlipY)
			iNumUnits = pPlot.getNumUnits()
			for i in range (iNumUnits):
				apUnit = pPlot.getUnit(iNumUnits - (i+1))
				if apUnit.getOwner() == con.iBarbarian:
					objMercenaryUtils.getSpecificMercenary(iPlayer, apUnit.getUnitType(), apUnit.getName(), iX, iY)
					apUnit.kill(0, -1)
				szText = localText.getText("TXT_KEY_MINOR_EVENT_HIRE_SUCCESS", ())
				CyInterface().addMessage(unit.getOwner(), False, con.iDuration, szText, "AS2D_VICTORY_EARLY", InterfaceMessageTypes.MESSAGE_TYPE_MINOR_EVENT, "", ColorTypes(con.iGreen), -1, -1, False, False)
				
				
				
	def pirateCheck(self):
	
		#print "pirateCheck"
	
		apCityList = PyPlayer(utils.getHumanID()).getCityList()
		for pCity in apCityList:
			city = pCity.GetCy()
			if city.isCoastal(0):
				x = city.getX()
				y = city.getY()
				for j in range((x-2),(x+3)):
					for k in range ((y-2), (y+3)):
						pPlot = gc.getMap().plot(j, k)
						if pPlot.isWater() and pPlot.getOwner() == iHuman and pPlot.getNumUnits() > 0: 
							iNumUnits = pPlot.getNumUnits()
							for i in range (iNumUnits):
								unit = pPlot.getUnit(i)
								if not unit.isHasPromotion(con.iOceanfaring) and unit.getOwner() == con.iBarbarian and unit.getDomainType() == 0: # barbarian sea unit
									unit.setHasPromotion(con.iOceanfaring, True)
									self.doPirateBribeAndHire(pPlot.getX(), pPlot.getY())
									return
										
		for pCity in apCityList:
			city = pCity.GetCy()
			if city.isCoastal(0):
				x = city.getX()
				y = city.getY()
				for j in range((x-1),(x+2)):
					for k in range ((y-1), (y+2)):
						pPlot = gc.getMap().plot(j, k)
						if pPlot.isWater() and pPlot.getOwner() == iHuman: 
							if pPlot.getNumUnits() > 0:
								iNumUnits = pPlot.getNumUnits()
								for i in range (iNumUnits):
									unit = pPlot.getUnit(i)
									if unit.isHasPromotion(con.iOceanfaring) and unit.getOwner() == con.iBarbarian and unit.getDomainType() == 0:
										unit.setHasPromotion(con.iOceanfaring, False)
			
			
				
	def doPirateBribeAndHire(self, x, y):
		
		plot = gc.getMap().plot(x, y)
		CyCamera().JustLookAtPlot(plot)
		iBribeCost = 0
		iHireCost = 0
		iNumUnits = plot.getNumUnits()
		for i in range (iNumUnits):
			unit = plot.getUnit(iNumUnits - (i))
			if unit.getOwner() == con.iBarbarian and unit.getDomainType() == 0: # barbarian sea unit
				iBribeCost += 10
				iHireCost += objMercenaryUtils.getVirtualMercenaryCost(unit.getUnitType(), "temp")
				if gc.getPlayer(iHuman).getGold() >= iHireCost:
					self.pirateBribeAndHirePopup(iHuman)
				elif gc.getPlayer(iHuman).getGold() >= iBribeCost:
					self.pirateBribeOnlyPopup(iHuman)
				sd.setPirateX(x)
				sd.setPirateY(y)
		
		
		
		
	def doPirateHire(self, x, y, iPlayer):
		plot = gc.getMap().plot(x, y)
		iNumUnits = plot.getNumUnits()
		for i in range (iNumUnits):
			unit = plot.getUnit((iNumUnits)-(i))
			if unit.getOwner() == con.iBarbarian and unit.getDomainType() == 0: # barbarian sea unit
				iRand = gc.getGame().getSorenRandNum(100, 'Success')
				bSuccess = true
				if iRand < 20:
					bSuccess = false
				if bSuccess:
					unit.setName("%s %s %s %s %s" %(unit.getName(), "(","Barbarian Fleet", con.tRomanNumerals[sd.getSeaBarbMercCount()],")"))
					sd.setSeaBarbMercCount(sd.getSeaBarbMercCount() + 1)
					utils.makeUnit(unit.getUnitType(), con.iBarbarian, (con.iSeaFlipX, con.iSeaFlipY), 1, name = unit.getName())
					unit.kill(0, -1)
		pPlot = CyMap().plot(con.iSeaFlipX, con.iSeaFlipY)
		iNumUnits = pPlot.getNumUnits()
		for i in range (iNumUnits):
			apUnit = pPlot.getUnit(iNumUnits - (i))
			if apUnit.getOwner() == con.iBarbarian:
				objMercenaryUtils.getSpecificMercenary(iPlayer, apUnit.getUnitType(), apUnit.getName(), x, y)
				apUnit.kill(0, -1)
				
	def doPirateBribe(self, x, y):
	
		iRand = gc.getGame().getSorenRandNum(100, 'Success')
		bSuccess = true
		if iRand < 20:
			bSuccess = false
		pPlayer = gc.getPlayer(iHuman)
		plot = gc.getMap().plot(x, y)
		iCost = 0
		iNumUnits = plot.getNumUnits()
		for i in range (iNumUnits):
			unit = plot.getUnit(iNumUnits - (i))
			if unit.getOwner() == con.iBarbarian:
				iCost -= 10
				if bSuccess:
					unit.kill(0, -1)
			
		if bSuccess == false:
			szText = localText.getText("TXT_KEY_MINOR_EVENT_BRIBE_FAILURE", ())
			CyInterface().addMessage(unit.getOwner(), False, con.iDuration, szText, "AS2D_LOSS_EARLY", InterfaceMessageTypes.MESSAGE_TYPE_MINOR_EVENT, "", ColorTypes(con.iRed), -1, -1, False, False)
			pPlayer.changeGold(iCost) 
		else:
			pPlayer.changeGold(iCost) 
			szText = localText.getText("TXT_KEY_MINOR_EVENT_BRIBE_SUCCESS", ())
			CyInterface().addMessage(unit.getOwner(), False, con.iDuration, szText, "AS2D_VICTORY_EARLY", InterfaceMessageTypes.MESSAGE_TYPE_MINOR_EVENT, "", ColorTypes(con.iGreen), -1, -1, False, False)
		
		
	# srpt barbarian bribe
	def doBarbarianBribe(self, unit, iX, iY):
	
		iPlayer = unit.getOwner()
		bWonder = False
		apCityList = PyPlayer(iPlayer).getCityList()
		for pCity in apCityList:
			if pCity.getNumBuilding(con.iHagiaSophia): 
				bWonder = True
				break
		
		
		iRand = gc.getGame().getSorenRandNum(100, 'Success')
		bSuccess = false
		if iRand > 20 or bWonder == True:
			bSuccess = true
		pPlayer = gc.getPlayer(unit.getOwner())
		pPlot = CyMap().plot(iX, iY)
		iCost = 0
		iNumUnits = pPlot.getNumUnits()
		for i in range (iNumUnits):
			apUnit = pPlot.getUnit(iNumUnits - (i))
			if apUnit.getOwner() == con.iBarbarian:
				if bWonder == True:
					iCost -= 5
				else:
					iCost -= 10
				if bSuccess:
					apUnit.kill(0, -1)
			
		if bSuccess == False:
			unit.kill(0, -1)
			szText = localText.getText("TXT_KEY_MINOR_EVENT_BRIBE_FAILURE", ())
			CyInterface().addMessage(unit.getOwner(), False, con.iDuration, szText, "AS2D_LOSS_EARLY", InterfaceMessageTypes.MESSAGE_TYPE_MINOR_EVENT, "", ColorTypes(con.iRed), -1, -1, False, False)
			pPlayer.changeGold(iCost) 
		else:
			pPlayer.changeGold(iCost) 
			szText = localText.getText("TXT_KEY_MINOR_EVENT_BRIBE_SUCCESS", ())
			CyInterface().addMessage(unit.getOwner(), False, con.iDuration, szText, "AS2D_VICTORY_EARLY", InterfaceMessageTypes.MESSAGE_TYPE_MINOR_EVENT, "", ColorTypes(con.iGreen), -1, -1, False, False)
		
		
		
	def doSecretDiplomacy(self, pUnit, iCapitalX, iCapitalY):
	
	
		iSpyOwner = pUnit.getOwner()
		pSpyOwner = gc.getPlayer(iSpyOwner)
		pPlot = CyMap().plot(iCapitalX, iCapitalY)
		iCityOwner = pPlot.getOwner()
		pCityOwner = gc.getPlayer(iCityOwner)
		bVassalize = False
		bSurrender = False
		
		if iSpyOwner == iByzantines and iCityOwner == iRome:
			if pSpyOwner.getNumCities() >= pCityOwner.getNumCities() * 3:
				bVassalize = True
		
		elif pSpyOwner.getNumCities() >= pCityOwner.getNumCities() * 4:
			iNumDefenders = 0
			iNumAttackers = 0
		
			iNumUnits = pPlot.getNumUnits()
			for i in range (iNumUnits):
				unit = pPlot.getUnit(i)
				if unit.isMilitaryHappiness() and not gc.getTeam(pSpyOwner.getTeam()).isAtWar(unit.getOwner()): 
					iNumDefenders += 1
			for x in range (iCapitalX -1, iCapitalX + 1):
				for y in range (iCapitalY - 1, iCapitalY + 1):
					kPlot = CyMap().plot(x, y)
					iNumUnits = kPlot.getNumUnits()
					for i in range (iNumUnits):
						unit = pPlot.getUnit(i)
						if unit.isMilitaryHappiness() and gc.getTeam(pCityOwner.getTeam()).isAtWar(iSpyOwner):
							iNumAttackers += 1
			if iNumAttackers >= iNumDefenders * 3:
				bVassalize = True
				
		elif pSpyOwner.getNumCities() * 3 < pCityOwner.getNumCities():
			bSurrender = True
			
		if bVassalize:
			self.secretDiplomacyVassalizePopup(iCityOwner)
		elif bSurrender:
			self.secretDiplomacySurrenderPopup(iCityOwner)
		else:
			self.secretDiplomacyFailurePopup(iSpyOwner)
							
			

	# Roman Civil Wars
	
	def startRomanCivilWar(self):
								
		print "starting Roman civil war"
		gc.getTeam(pRome.getTeam()).setHasTech(con.iStabilityCollapsing, False, iRome, False, False)
		gc.getTeam(pRome.getTeam()).setHasTech(con.iStabilityUnstable, False, iRome, False, False)
		gc.getTeam(pRome.getTeam()).setHasTech(con.iStabilityStable, True, iRome, False, False)
		gc.getTeam(gc.getPlayer(iByzantines).getTeam()).declareWar(iRome, True, -1)
		sd.setCivilization(iByzantines, iRebelRome)
		pByzantines.setCivilizationType(iRebelRome)
		pByzantines.setLeader(con.iPompey)
		tRomanCapital = (pRome.getCapitalCity().getX(), pRome.getCapitalCity().getY())
		empireCityList = PyPlayer(iRome).getCityList()
		iMaxRebelCities = (len(empireCityList) / 2)
		iMinRebelCities = (len(empireCityList) / 4)
		iRange = (iMaxRebelCities - iMinRebelCities)
		iRndNum = gc.getGame().getSorenRandNum(iRange, 'chance')
		iNumRebelCities = iMinRebelCities + iRndNum
		#print ("iMaxRebelCities", iMaxRebelCities)
		#print ("iMinRebelCities", iMinRebelCities)
		#print ("iRndNum", iRndNum)
		#print ("iNumRebelCities", iNumRebelCities)
		
		if iRome != utils.getHumanID():
			utils.makeUnit(con.iLegionary, iRome, tRomanCapital, iNumRebelCities)
		rebelCityList =[]
		if gc.getGame().getSorenRandNum(100, 'chance') > 50:
			# NW rebellion
			for x in range (con.iMapWidth):
				for y in range (con.iMapHeight):
					pCurrent = gc.getMap().plot(x, con.iMapHeight - y)
					if pCurrent.isCity() and pCurrent.getOwner() == iRome and not pCurrent.getPlotCity().getNumRealBuilding(con.iPalace) and gc.getMap().plot(pCurrent.getX(), pCurrent.getY()).getRegionID() not in con.lCoreRegions[iRome]:
						if len(rebelCityList) <= iNumRebelCities:
							rebelCityList.append(pCurrent)
		else:
			# SE rebellion
			for x in range (con.iMapWidth):
				for y in range (con.iMapHeight):
					pCurrent = gc.getMap().plot(con.iMapWidth - x, y)
					if pCurrent.isCity() and pCurrent.getOwner() == iRome and not pCurrent.getPlotCity().getNumRealBuilding(con.iPalace):
						if len(rebelCityList) <= iNumRebelCities:
							rebelCityList.append(pCurrent)
		for pCity in rebelCityList:
			utils.cultureManager((pCity.getX(),pCity.getY()), 100, iByzantines, iRome, False, False, False)
			utils.flipUnitsInCityBefore((pCity.getX(),pCity.getY()), iByzantines, iRome)
			self.setTempFlippingCity((pCity.getX(),pCity.getY()))
			utils.flipCity((pCity.getX(),pCity.getY()), 0, 0, iByzantines, [iRome])
			utils.flipUnitsInCityAfter(self.getTempFlippingCity(), iByzantines)
		regionList = []
		apCityList = PyPlayer(iByzantines).getCityList()
		for pCity in apCityList:
			regionID = gc.getMap().plot(pCity.getX(), pCity.getY()).getRegionID()
			if regionID not in regionList and not utils.checkRegionOwnedCity(iRome, regionID):
				regionList.append(regionID)
		utils.flipUnitsInArea(utils.getRegionPlotList(regionList), iByzantines, iRome, False, True)
		self.assignTechs(iRebelRome, iByzantines)
		if iRome != utils.getHumanID():
			CyInterface().addMessage(utils.getHumanID(), False, con.iDuration, CyTranslator().getText("TXT_KEY_START_ROMAN_CIVIL_WAR", ()), "", 0, "", ColorTypes(con.iRed), -1, -1, True, True)
		
	def endRomanCivilWar(self):
		print "ending Roman civil war"
		rebelCityList = PyPlayer(iByzantines).getCityList()
		for pCity in rebelCityList:
			#print ("flipping", pCity.getName())
			utils.cultureManager((pCity.getX(),pCity.getY()), 100, iRome, iByzantines, False, False, False)
			utils.flipUnitsInCityBefore((pCity.getX(),pCity.getY()), iRome, iByzantines)
			self.setTempFlippingCity((pCity.getX(),pCity.getY()))
			utils.flipCity((pCity.getX(),pCity.getY()), 0, 0, iRome, [iByzantines])
			utils.flipUnitsInCityAfter(self.getTempFlippingCity(), iRome)
		utils.flipUnitsInArea(utils.getAreaPlotList([0,0], [con.iMapWidth, con.iMapHeight]), iRome, iByzantines, True, True)
		gc.getTeam(pRome.getTeam()).setHasTech(con.iStabilityCollapsing, False, iRome, False, False)
		gc.getTeam(pRome.getTeam()).setHasTech(con.iStabilityUnstable, False, iRome, False, False)
		gc.getTeam(pRome.getTeam()).setHasTech(con.iStabilityStable, True, iRome, False, False)
		if iRome != utils.getHumanID():
			CyInterface().addMessage(utils.getHumanID(), False, con.iDuration, CyTranslator().getText("TXT_KEY_END_ROMAN_CIVIL_WAR", ()), "", 0, "", ColorTypes(con.iRed), -1, -1, True, True)
		sd.setCivilization(iByzantines, iByzantines)
		gc.getTeam(gc.getPlayer(iRome).getTeam()).makePeace(iByzantines)
		
	def assignTechs(self, iCiv, iPlayer):
		"""Assigns techs to the specific civ based on the starting tech table."""
		pTeam = gc.getTeam(gc.getPlayer(iPlayer).getTeam())
		for iLoopTech in range(len(con.lStartingTechs[iCiv])):
			pTeam.setHasTech(con.lStartingTechs[iCiv][iLoopTech], True, iPlayer, False, False)
			
	def onCityBuilt(self, city, iCiv):
	
		# Pyramids
		if gc.getTeam(gc.getPlayer(iCiv).getTeam()).isHasTech(con.iPyramidsFunctionTech):
			pCurrent = gc.getMap().plot(city.getX(),city.getY())
			if pCurrent.getRegionID() == con.rEgypt:
				city.setNumRealBuilding(con.iPyramidsFunctionBuilding, 1)
				
		# Colossus
		if gc.getTeam(gc.getPlayer(iCiv).getTeam()).isHasTech(con.iColossusFunctionTech):
			regionList = [con.rMallorca, con.rCorsica, con.rSardinia, con.rSicily, con.rMalta, con.rCrete, con.rCyprus, con.rRhodes]
			pCurrent = gc.getMap().plot(city.getX(),city.getY())
			if pCurrent.getRegionID() in regionList:
				city.setNumRealBuilding(con.iColossusFunctionBuilding, 1)
	
		# Gokturk UP
		if iCiv == con.iGokturks and gc.getMap().plot(city.getX(), city.getY()).getRegionID() in [con.rScythianSteppe, con.rSarmatianSteppe, con.rMongolianSteppe]:
			dummy, plotList = utils.plotListSearch(utils.citySquarePlotList(city.getX(), city.getY()), utils.horsePlots, [])
			rndNum = gc.getGame().getSorenRandNum(len(plotList), 'Spawn horse')
			if (len(plotList)):
				result = plotList[rndNum]
				if (result):
					res.createResource(result[0], result[1], con.iHorse)
					gc.getMap().plot(result[0], result[1]).setImprovementType(14)
		
		# hack for Ostrogoth AI stupidity
		if (iCiv != utils.getHumanID()) and (iCiv == con.iOstrogoths) and ((city.getX(), city.getY()) == con.tCapitals[con.iOstrogoths]):
			city.setNumRealBuilding(con.iWalls, 1)
			utils.makeUnitAI(con.iHeavySpearman, con.iOstrogoths, con.tCapitals[con.iOstrogoths], UnitAITypes.UNITAI_CITY_DEFENSE, 3)
			
		# hack to keep Byzantines from losing their capital
		if (iCiv != utils.getHumanID()) and (iCiv == con.iByzantines) and ((city.getX(), city.getY()) == con.tCapitals[con.iByzantines]):
			city.setNumRealBuilding(con.iWalls, 1)
			city.setNumRealBuilding(con.iCastle, 1)
			utils.makeUnitAI(con.iHeavySpearman, con.iByzantines, con.tCapitals[con.iByzantines], UnitAITypes.UNITAI_CITY_DEFENSE, 2)
		
		# Roman wall during autoplay
		if iCiv == iRome and gc.getPlayer(utils.getHumanID()).getNumCities() < 1:
			if city.plot().getRegionID() in con.lCoreRegions[iRome] or city.plot().getRegionID() in con.lNormalRegions[iRome]:
				city.setNumRealBuilding(con.iWalls, 1)
				print "Roman walls"
			
	def triggerAIInvasion(self, iPlayer):
	
		iCiv = sd.getCivilization(iPlayer)
		regionList = con.lTargetRegions[iCiv]
		targetRegion = -1
		
		for regionID in regionList:
			if targetRegion == -1:
				if not utils.checkRegionControl(iPlayer, regionID):
					targetRegion = regionID
					for iTargetPlayer in range(con.iNumTotalPlayers):
						for pyCity in PyPlayer(iTargetPlayer).getCityList():
							if gc.getMap().plot(pyCity.getX(), pyCity.getY()).getRegionID() == regionID:
								if gc.getPlayer(iPlayer).AI_getAttitude(iTargetPlayer) <= con.iCautious:
									self.cityAttack(iPlayer, iCiv, pyCity.GetCy())
									CyInterface().addMessage(utils.getHumanID(), False, con.iDuration, localText.getText("TXT_KEY_AI_INVASION1", ()) + " " + gc.getPlayer(sd.getCivilization(iPlayer)).getCivilizationShortDescription(0) + " " + localText.getText("TXT_KEY_AI_INVASION2", ()) + " " + localText.getText("TXT_KEY_REGION_TOOLTIP_%d" %(regionID), ()) + "!", "", 0, "", ColorTypes(con.iRed), -1, -1, True, True)
					
				
	def cityAttack(self, iPlayer, iCiv, city):
		# declare war on the city's owner
		if not gc.getTeam(gc.getPlayer(iPlayer).getTeam()).isAtWar(gc.getPlayer(city.getOwner()).getTeam()):
			gc.getTeam(gc.getPlayer(iPlayer).getTeam()).declareWar(gc.getPlayer(city.getOwner()).getTeam(), True, -1)
				
		# traitors open the gates... (human player not affected)
		if not city.getOwner() == utils.getHumanID():
			city.changeCultureUpdateTimer(3);
			city.changeOccupationTimer(3);
				
		# find a spot for the siege
		for tPlot in ((city.getX()-1, city.getY()), (city.getX()-1, city.getY()+1), (city.getX(), city.getY()+1), (city.getX(), city.getY()-1), (city.getX()+1, city.getY()+1), (city.getX()-1, city.getY()-1), (city.getX()+1, city.getY())):
			pPlot = gc.getMap().plot(tPlot[0], tPlot[1])
			if not pPlot.isWater(): 
				if not pPlot.isPeak():
					if pPlot.getFeatureType() not in [con.iForest, con.iMarsh, con.iJungle, con.iDenseForest, con.iIce]:
						if pPlot.getOwner() < 0 or gc.getTeam(gc.getPlayer(iPlayer).getTeam()).isAtWar(gc.getPlayer(pPlot.getOwner()).getTeam()):
							break
		startingPlot = gc.getMap().plot(tPlot[0], tPlot[1])
				
		# clear the spot
		iNumUnitsInAPlot = startingPlot.getNumUnits()
		if iNumUnitsInAPlot:
			for i in range(iNumUnitsInAPlot):
				unit = startingPlot.getUnit(0)
				if unit.getOwner() != iCiv:
					unit.kill(False, iBarbarian)
				
		#print ("birthInvasion: starting units in", tPlot[0], tPlot[1])
		#print ("createBarbarianBirthUnits, iPlayer=", iPlayer, "iCiv=", iCiv)
		self.createAIInvasionUnits(iPlayer, (tPlot[0], tPlot[1]))
		utils.setPlagueCountdown(iPlayer, -utils.getTurns(con.iImmunity))
		utils.clearPlague(iPlayer)
		#CyInterface().addMessage(utils.getHumanID(), False, con.iDuration, CyTranslator().getText("TXT_KEY_UP_ROMAN_INDY_ASSIMILATION", ()), "", 0, "", ColorTypes(con.iRed), -1, -1, True, True)
		
	def createAIInvasionUnits(self, iPlayer, tPlot):
		
		if iPlayer == iRome:
			utils.makeUnit(con.iLegionary, iPlayer, tPlot, 4)
			utils.makeUnit(con.iCatapult, iPlayer, tPlot, 2)
			
		if iPlayer == con.iHan:
			utils.makeUnit(con.iChokonu, iPlayer, tPlot, 4)
			utils.makeUnit(con.iCatapult, iPlayer, tPlot, 2)
			
		if iPlayer == con.iParthia:
			utils.makeUnit(con.iGrivpanvar, iPlayer, tPlot, 2)
			utils.makeUnit(con.iArcher, iPlayer, tPlot, 2)
			utils.makeUnit(con.iCatapult, iPlayer, tPlot, 2)
			
		if iPlayer == con.iSassanids:
			utils.makeUnit(con.iSassanidCataphract, iPlayer, tPlot, 2)
			utils.makeUnit(con.iMarksman, iPlayer, tPlot, 2)
			utils.makeUnit(con.iCatapult, iPlayer, tPlot, 2)
			
		if iPlayer == con.iArabs:
			utils.makeUnit(con.iGhazi, iPlayer, tPlot, 4)
			utils.makeUnit(con.iArcher, iPlayer, tPlot, 2)
			utils.makeUnit(con.iHeavyCatapult, iPlayer, tPlot, 2)
	
		
###############
### Popups ###
#############

	def showPopup(self, popupID, title, message, labels):
		"""popupID has to be a registered ID in CvRhyesCatapultEventManager.__init__!"""
		
		popup = Popup.PyPopup(popupID, EventContextTypes.EVENTCONTEXT_ALL)
		popup.setHeaderString(title)
		popup.setBodyString(message)
		for i in labels:
			popup.addButton(i)
		popup.launch(False)
		
		
	def eventApply7616(self, popupReturn):
		if popupReturn.getButtonClicked() == 0: # 1st button
			self.doPirateBribe(sd.getPirateX(), sd.getPirateY())
			self.pirateCheck()
		if popupReturn.getButtonClicked() == 1: # 2nd button
			self.doPirateHire(sd.getPirateX(), sd.getPirateY(), iHuman)
			self.pirateCheck()
		if popupReturn.getButtonClicked() == 2: # 3rd button
			self.pirateCheck()
		
		
	def eventApply7617(self, popupReturn):
		if popupReturn.getButtonClicked() == 0: # 1st button
			self.doPirateBribe(sd.getPirateX(), sd.getPirateY())
			self.pirateCheck()
		if popupReturn.getButtonClicked() == 1: # 2nd button
			self.pirateCheck()
			
	def eventApply7630(self, popupReturn):
		if popupReturn.getButtonClicked() == 0: # 1st button
			iVassal = sd.getSecretDiplomacyTargetCiv()
			iHuman = utils.getHumanID()
			for iLoopCiv in range (con.iNumPlayers):
				if not gc.getTeam(gc.getPlayer(iHuman).getTeam()).isAtWar(iLoopCiv):
					gc.getTeam(gc.getPlayer(iVassal).getTeam()).makePeace(iLoopCiv)
			gc.getTeam(gc.getPlayer(iVassal).getTeam()).setVassal(iHuman, True, False)
		if popupReturn.getButtonClicked() == 1: # 2nd button
			return
			
	def eventApply7631(self, popupReturn):
		if popupReturn.getButtonClicked() == 0: # 1st button
			iMaster = sd.getSecretDiplomacyTargetCiv()
			iHuman = utils.getHumanID()
			for iLoopCiv in range (con.iNumPlayers):
				if not gc.getTeam(gc.getPlayer(iMaster).getTeam()).isAtWar(iLoopCiv):
					gc.getTeam(gc.getPlayer(iHuman).getTeam()).makePeace(iLoopCiv)
			gc.getTeam(gc.getPlayer(iHuman).getTeam()).setVassal(iMaster, True, False)
		if popupReturn.getButtonClicked() == 1: # 2nd button
			return
			

			

			
	def pirateBribeOnlyPopup(self, iCiv):
		self.showPopup(7617, CyTranslator().getText("TXT_KEY_PIRATE_TITLE", ()), CyTranslator().getText("TXT_KEY_PIRATE_MESSAGE", ()), (CyTranslator().getText("TXT_KEY_POPUP_BRIBE_PIRATE", ()), CyTranslator().getText("TXT_KEY_POPUP_IGNORE_PIRATE", ())))
		
	def pirateBribeAndHirePopup(self, iCiv):
		self.showPopup(7617, CyTranslator().getText("TXT_KEY_PIRATE_TITLE", ()), CyTranslator().getText("TXT_KEY_PIRATE_MESSAGE", ()), (CyTranslator().getText("TXT_KEY_POPUP_BRIBE_PIRATE", ()), CyTranslator().getText("TXT_KEY_POPUP_IGNORE_PIRATE", ())))
			

	def startRomanCivilWarPopup(self, iCiv):
		popup = Popup.PyPopup()
		popup.setHeaderString(CyTranslator().getText("TXT_KEY_START_ROMAN_CIVIL_WAR_TITLE", ()))
		popup.setBodyString(CyTranslator().getText("TXT_KEY_START_ROMAN_CIVIL_WAR_MESSAGE", ()))
		popup.launch()
		self.startRomanCivilWar()
		
	def endRomanCivilWarPopup(self, iCiv):
		popup = Popup.PyPopup()
		popup.setHeaderString(CyTranslator().getText("TXT_KEY_END_ROMAN_CIVIL_WAR_TITLE", ()))
		popup.setBodyString(CyTranslator().getText("TXT_KEY_END_ROMAN_CIVIL_WAR_MESSAGE", ()))
		popup.launch()
		self.endRomanCivilWar()
		
	def secretDiplomacyVassalizePopup(self, iVassal):
		self.showPopup(7630, CyTranslator().getText("TXT_KEY_SECRET_DIPLOMACY_TITLE", ()), CyTranslator().getText("TXT_KEY_SECRET_DIPLOMACY_MESSAGE", ()), (CyTranslator().getText("TXT_KEY_SECRET_DIPLOMACY_VASSALIZE", ()), CyTranslator().getText("TXT_KEY_SECRET_DIPLOMACY_VASSAL_DECLINE", ())))
		sd.setSecretDiplomacyTargetCiv(iVassal)
		
		
	def secretDiplomacySurrenderPopup(self, iMaster):
		self.showPopup(7631, CyTranslator().getText("TXT_KEY_SECRET_DIPLOMACY_TITLE", ()), CyTranslator().getText("TXT_KEY_SECRET_DIPLOMACY_MESSAGE", ()), (CyTranslator().getText("TXT_KEY_SECRET_DIPLOMACY_SURRENDER", ()), CyTranslator().getText("TXT_KEY_SECRET_DIPLOMACY_SURRENDER_DECLINE", ())))
		sd.setSecretDiplomacyTargetCiv(iMaster)
		
	def secretDiplomacyFailurePopup(self, iCiv):
		popup = Popup.PyPopup()
		popup.setHeaderString(CyTranslator().getText("TXT_KEY_SECRET_DIPLOMACY_TITLE", ()))
		popup.setBodyString(CyTranslator().getText("TXT_KEY_SECRET_DIPLOMACY_FAILURE_MESSAGE", ()))
		popup.launch()
		
	def spawnCityDefense(self, iPlayer, iCiv, tPlot):
		
		pPlayer = gc.getPlayer(iPlayer)
		tTeam = gc.getTeam(pPlayer.getTeam())
		iUnitType = con.iSpearman
		if iCiv == con.iQin: iUnitType = con.iQinInfantry
		if iCiv == con.iPontus: iUnitType = con.iPonticUazali
		if iCiv == con.iAxum: iUnitType = con.iAxumSarawit
		if iCiv == con.iRome: iUnitType = con.iLegionary
		if tTeam.isHasTech(con.iArchery):
			iUnitType = con.iArcher
			if iCiv == con.iNubia: iUnitType = con.iNubiaLongbowman
			if iCiv == con.iHan: iUnitType = con.iChokonu
			if iCiv == con.iTocharians: iUnitType = con.iTarimBowman
			if iCiv == con.iPandyans: iUnitType = con.iPandyanVillavar
		if tTeam.isHasTech(con.iMarksmanship):
			iUnitType = con.iMarksman
			if iCiv == con.iVietnam: iUnitType = con.iAuLacCrossbowman
			if iCiv == con.iGupta: iUnitType = con.iBambooArcher
		utils.makeUnitAI(iUnitType, iPlayer, tPlot, UnitAITypes.UNITAI_CITY_DEFENSE, 1)
	

			