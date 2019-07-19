## Sid Meier's Civilization 4
## Copyright Firaxis Games 2005
##
## Implementaion of miscellaneous game functions

import CvUtil
from CvPythonExtensions import *
import CvEventInterface
import PyHelpers
import Consts as con # edead
import MercenaryUtils # edead
from RFCUtils import utils

# globals
gc = CyGlobalContext()
PyPlayer = PyHelpers.PyPlayer
objMercenaryUtils = MercenaryUtils.MercenaryUtils() # edead

class CvGameUtils:
	"Miscellaneous game functions"
	def __init__(self): 
		pass
		
	def isVictoryTest(self):
		if ( gc.getGame().getElapsedGameTurns() > 10 ):
			return True
		else:
			return False

	def isVictory(self, argsList):
		eVictory = argsList[0]
		return True

	def isPlayerResearch(self, argsList):
		ePlayer = argsList[0]
		return True

	def getExtraCost(self, argsList):
		ePlayer = argsList[0]
		return 0

	def createBarbarianCities(self):
		return False
		
	def createBarbarianUnits(self):
		return False
		
	def skipResearchPopup(self,argsList):
		ePlayer = argsList[0]
		return False
		
	def showTechChooserButton(self,argsList):
		ePlayer = argsList[0]
		return True

	def getFirstRecommendedTech(self,argsList):
		ePlayer = argsList[0]
		return TechTypes.NO_TECH

	def getSecondRecommendedTech(self,argsList):
		ePlayer = argsList[0]
		eFirstTech = argsList[1]
		return TechTypes.NO_TECH
	
	def canRazeCity(self,argsList):
		iRazingPlayer, pCity = argsList
		
		# edead: start
		if utils.getHumanID() != iRazingPlayer and (pCity.getX(), pCity.getY()) in con.lAINoRaze:
			return False
		# edead: end
		
		return True
	
	def canDeclareWar(self,argsList):
		iAttackingTeam, iDefendingTeam = argsList
		
		return True
	
	def skipProductionPopup(self,argsList):
		pCity = argsList[0]
		return False
		
	def showExamineCityButton(self,argsList):
		pCity = argsList[0]
		return True

	def getRecommendedUnit(self,argsList):
		pCity = argsList[0]
		return UnitTypes.NO_UNIT

	def getRecommendedBuilding(self,argsList):
		pCity = argsList[0]
		return BuildingTypes.NO_BUILDING

	def updateColoredPlots(self):
		return False

	def isActionRecommended(self,argsList):
		pUnit = argsList[0]
		iAction = argsList[1]
		return False

	def unitCannotMoveInto(self,argsList):
		ePlayer = argsList[0]		
		iUnitId = argsList[1]
		iPlotX = argsList[2]
		iPlotY = argsList[3]
		return False

	def cannotHandleAction(self,argsList):
		pPlot = argsList[0]
		iAction = argsList[1]
		bTestVisible = argsList[2]
		return False

	def canBuild(self,argsList):
		iX, iY, iBuild, iPlayer = argsList
		return -1	# Returning -1 means ignore; 0 means Build cannot be performed; 1 or greater means it can

	def cannotFoundCity(self,argsList):
		iPlayer, iPlotX, iPlotY = argsList
		return False

	def cannotSelectionListMove(self,argsList):
		pPlot = argsList[0]
		bAlt = argsList[1]
		bShift = argsList[2]
		bCtrl = argsList[3]
		return False

	def cannotSelectionListGameNetMessage(self,argsList):
		eMessage = argsList[0]
		iData2 = argsList[1]
		iData3 = argsList[2]
		iData4 = argsList[3]
		iFlags = argsList[4]
		bAlt = argsList[5]
		bShift = argsList[6]
		return False

	def cannotDoControl(self,argsList):
		eControl = argsList[0]
		return False

	def canResearch(self,argsList):
		ePlayer = argsList[0]
		eTech = argsList[1]
		bTrade = argsList[2]
		return False

	def cannotResearch(self,argsList):
		ePlayer = argsList[0]
		eTech = argsList[1]
		bTrade = argsList[2]
		return False

	def canDoCivic(self,argsList):
		ePlayer = argsList[0]
		eCivic = argsList[1]
		return False

	def cannotDoCivic(self,argsList):
		ePlayer = argsList[0]
		eCivic = argsList[1]
		
		#if eCivic == con.iSlaveryCivic:
			#eStateReligion = gc.getPlayer(ePlayer).getStateReligion()
			#if eStateReligion == con.iJudaism or eStateReligion == con.iConfucianism or eStateReligion == con.iHinduism:
				#return True
		
		return False
		
	def canTrain(self,argsList):
		pCity = argsList[0]
		eUnit = argsList[1]
		bContinue = argsList[2]
		bTestVisible = argsList[3]
		bIgnoreCost = argsList[4]
		bIgnoreUpgrades = argsList[5]
		return False

	def cannotTrain(self,argsList):
		pCity = argsList[0]
		eUnit = argsList[1]
		bContinue = argsList[2]
		bTestVisible = argsList[3]
		bIgnoreCost = argsList[4]
		bIgnoreUpgrades = argsList[5]
		return False
		
	def canConstruct(self,argsList):
		pCity = argsList[0]
		eBuilding = argsList[1]
		bContinue = argsList[2]
		bTestVisible = argsList[3]
		bIgnoreCost = argsList[4]
		return False

	def cannotConstruct(self,argsList):
		pCity = argsList[0]
		eBuilding = argsList[1]
		bContinue = argsList[2]
		bTestVisible = argsList[3]
		bIgnoreCost = argsList[4]
		return False
		
	def canCreate(self,argsList):
		pCity = argsList[0]
		eProject = argsList[1]
		bContinue = argsList[2]
		bTestVisible = argsList[3]
		return False

	def cannotCreate(self,argsList):
		pCity = argsList[0]
		eProject = argsList[1]
		bContinue = argsList[2]
		bTestVisible = argsList[3]
		return False

	def canMaintain(self,argsList):
		pCity = argsList[0]
		eProcess = argsList[1]
		bContinue = argsList[2]
		return False

	def cannotMaintain(self,argsList):
		pCity = argsList[0]
		eProcess = argsList[1]
		bContinue = argsList[2]
		return False

	def AI_chooseTech(self,argsList):
		ePlayer = argsList[0]
		bFree = argsList[1]
		return TechTypes.NO_TECH

	def AI_chooseProduction(self,argsList):
		pCity = argsList[0]
		
		bOverride = False
		
		return bOverride


	def AI_unitUpdate(self,argsList):
		pUnit = argsList[0]
		
		# edead: start Inquisitor AI from Charlemagne + Pilgrim AI
		iOwner = pUnit.getOwner()
		if not gc.getPlayer(iOwner).isHuman():
			if pUnit.getUnitType() == con.iInquisitor:
				self.doInquisitorCore_AI(pUnit)
				return True
			# if pUnit.getUnitType() == con.iPilgrim:
				# self.doPilgrimCore_AI(pUnit)
				# return True
		# edead: end
		
		return False


	# edead: start Inquisitor AI proper
	def doInquisitorCore_AI(self, pUnit):
		
		iOwner = pUnit.getOwner()
		iStateReligion = gc.getPlayer(iOwner).getStateReligion()
		iTolerance = con.tReligiousTolerance[iOwner]
		apCityList = PyPlayer(iOwner).getCityList()
		
		#Looks to see if the AI controls a city that is not the State Religion
		for iCity in range(len(apCityList)):
			for iReligion in range(con.iNumReligions):
				if iReligion != iStateReligion:
					
					bFound = True
					
					if bFound:
						pCity = gc.getPlayer(iOwner).getCity(apCityList[iCity].getID())
						if pCity.isHasReligion(iReligion):
							if pUnit.generatePath(pCity.plot(), 0, False, None):
								self.doInquisitorMove(pUnit, pCity)
								return


	def doInquisitorMove(self, pUnit, pCity):
		
		if pUnit.getX() != pCity.getX() or pUnit.getY() != pCity.getY():
			pUnit.getGroup().pushMission(MissionTypes.MISSION_MOVE_TO, pCity.getX(), pCity.getY(), 0, False, True, MissionAITypes.NO_MISSIONAI, pUnit.plot(), pUnit)
		else:
			utils.doPersecution(pCity.getX(), pCity.getY(), pUnit.getID())




	def AI_doWar(self,argsList):
		eTeam = argsList[0]
		return False

	def AI_doDiplo(self,argsList):
		ePlayer = argsList[0]
		return False

	def calculateScore(self,argsList):
		ePlayer = argsList[0]
		bFinal = argsList[1]
		bVictory = argsList[2]
		
		# edead: start UHV score fix
		# iPopulationScore = CvUtil.getScoreComponent(gc.getPlayer(ePlayer).getPopScore(), gc.getGame().getInitPopulation(), gc.getGame().getMaxPopulation(), gc.getDefineINT("SCORE_POPULATION_FACTOR"), True, bFinal, bVictory)
		# iLandScore = CvUtil.getScoreComponent(gc.getPlayer(ePlayer).getLandScore(), gc.getGame().getInitLand(), gc.getGame().getMaxLand(), gc.getDefineINT("SCORE_LAND_FACTOR"), True, bFinal, bVictory)
		# iTechScore = CvUtil.getScoreComponent(gc.getPlayer(ePlayer).getTechScore(), gc.getGame().getInitTech(), gc.getGame().getMaxTech(), gc.getDefineINT("SCORE_TECH_FACTOR"), True, bFinal, bVictory)
		# iWondersScore = CvUtil.getScoreComponent(gc.getPlayer(ePlayer).getWondersScore(), gc.getGame().getInitWonders(), gc.getGame().getMaxWonders(), gc.getDefineINT("SCORE_WONDER_FACTOR"), False, bFinal, bVictory)
		iPopulationScore = CvUtil.getScoreComponent(gc.getPlayer(ePlayer).getPopScore(), gc.getGame().getInitPopulation(), gc.getGame().getMaxPopulation(), gc.getDefineINT("SCORE_POPULATION_FACTOR"), True, bFinal, bVictory, ePlayer)
		iLandScore = CvUtil.getScoreComponent(gc.getPlayer(ePlayer).getLandScore(), gc.getGame().getInitLand(), gc.getGame().getMaxLand(), gc.getDefineINT("SCORE_LAND_FACTOR"), True, bFinal, bVictory, ePlayer)
		iTechScore = CvUtil.getScoreComponent(gc.getPlayer(ePlayer).getTechScore(), gc.getGame().getInitTech(), gc.getGame().getMaxTech(), gc.getDefineINT("SCORE_TECH_FACTOR"), True, bFinal, bVictory, ePlayer)
		iWondersScore = CvUtil.getScoreComponent(gc.getPlayer(ePlayer).getWondersScore(), gc.getGame().getInitWonders(), gc.getGame().getMaxWonders(), gc.getDefineINT("SCORE_WONDER_FACTOR"), False, bFinal, bVictory, ePlayer)
		# edead: end
		return int(iPopulationScore + iLandScore + iWondersScore + iTechScore)

	def doHolyCity(self):
		return False

	def doHolyCityTech(self,argsList):
		eTeam = argsList[0]
		ePlayer = argsList[1]
		eTech = argsList[2]
		bFirst = argsList[3]
		return False

	def doGold(self,argsList):
		ePlayer = argsList[0]
		return -objMercenaryUtils.getPlayerMercenaryMaintenanceCost(ePlayer) # edead

	def doResearch(self,argsList):
		ePlayer = argsList[0]
		return False

	def doGoody(self,argsList):
		ePlayer = argsList[0]
		pPlot = argsList[1]
		pUnit = argsList[2]
		return False

	def doGrowth(self,argsList):
		pCity = argsList[0]
		return False

	def doProduction(self,argsList):
		pCity = argsList[0]
		return False

	def doCulture(self,argsList):
		pCity = argsList[0]
		return False

	def doPlotCulture(self,argsList):
		pCity = argsList[0]
		bUpdate = argsList[1]
		ePlayer = argsList[2]
		iCultureRate = argsList[3]
		return False

	def doReligion(self,argsList):
		pCity = argsList[0]
		return False

	def cannotSpreadReligion(self,argsList):
		iOwner, iUnitID, iReligion, iX, iY = argsList[0]
		return False

	def doGreatPeople(self,argsList):
		pCity = argsList[0]
		return False

	def doMeltdown(self,argsList):
		pCity = argsList[0]
		return False
	
	def doReviveActivePlayer(self,argsList):
		"allows you to perform an action after an AIAutoPlay"
		iPlayer = argsList[0]
		return False
	
	def doPillageGold(self, argsList):
		"controls the gold result of pillaging"
		pPlot = argsList[0]
		pUnit = argsList[1]
		
		iPillageGold = 0
		iPillageGold = CyGame().getSorenRandNum(gc.getImprovementInfo(pPlot.getImprovementType()).getPillageGold(), "Pillage Gold 1")
		iPillageGold += CyGame().getSorenRandNum(gc.getImprovementInfo(pPlot.getImprovementType()).getPillageGold(), "Pillage Gold 2")

		iPillageGold += (pUnit.getPillageChange() * iPillageGold) / 100
		
		# edead: start UP: Plunder
		#if pUnit.getOwner() == con.iKushans:
			#iPillageGold *= 2
		# edead: end
		
		return iPillageGold
	
	def doCityCaptureGold(self, argsList):
		"controls the gold result of capturing a city"
		
		pOldCity = argsList[0]
		iPlayer = argsList[1] # edead
		
		iCaptureGold = 0
		
		iCaptureGold += gc.getDefineINT("BASE_CAPTURE_GOLD")
		iCaptureGold += (pOldCity.getPopulation() * gc.getDefineINT("CAPTURE_GOLD_PER_POPULATION"))
		iCaptureGold += CyGame().getSorenRandNum(gc.getDefineINT("CAPTURE_GOLD_RAND1"), "Capture Gold 1")
		iCaptureGold += CyGame().getSorenRandNum(gc.getDefineINT("CAPTURE_GOLD_RAND2"), "Capture Gold 2")

		# edead: start UP: Plunder
		if iPlayer == con.iSeleucids:
			iCaptureGold *= 2
		# edead: end

		if (gc.getDefineINT("CAPTURE_GOLD_MAX_TURNS") > 0):
			iCaptureGold *= cyIntRange((CyGame().getGameTurn() - pOldCity.getGameTurnAcquired()), 0, gc.getDefineINT("CAPTURE_GOLD_MAX_TURNS"))
			iCaptureGold /= gc.getDefineINT("CAPTURE_GOLD_MAX_TURNS")
		
		return iCaptureGold
	
	def citiesDestroyFeatures(self,argsList):
		iX, iY= argsList
		return True
		
	def canFoundCitiesOnWater(self,argsList):
		iX, iY= argsList
		return False
		
	def doCombat(self,argsList):
		pSelectionGroup, pDestPlot = argsList
		return False

	def getConscriptUnitType(self, argsList):
		iPlayer = argsList[0]
		iConscriptUnitType = -1 #return this with the value of the UNIT TYPE you want to be conscripted, -1 uses default system
		
		return iConscriptUnitType

	def getCityFoundValue(self, argsList):
		iPlayer, iPlotX, iPlotY = argsList
		iFoundValue = -1 # Any value besides -1 will be used
		
		return iFoundValue
		
	def canPickPlot(self, argsList):
		pPlot = argsList[0]
		return true
		
	def getUnitCostMod(self, argsList):
		iPlayer, iUnit = argsList
		iCostMod = -1 # Any value > 0 will be used
		
		return iCostMod

	def getBuildingCostMod(self, argsList):
		iPlayer, iCityID, iBuilding = argsList
		pPlayer = gc.getPlayer(iPlayer)
		pCity = pPlayer.getCity(iCityID)
		
		iCostMod = -1 # Any value > 0 will be used
		
		return iCostMod
		
	def canUpgradeAnywhere(self, argsList):
		pUnit = argsList
		
		bCanUpgradeAnywhere = 0
		
		return bCanUpgradeAnywhere
		
	def getWidgetHelp(self, argsList):
		eWidgetType, iData1, iData2, bOption = argsList
		
		# edead: Inquisitor's button
		if iData1 == 666:
			return CyTranslator().getText("TXT_KEY_ACTION_PERSECUTION", ())
		
		# edead: Great Saint's button
		if iData1 == 667:
			return CyTranslator().getText("TXT_KEY_ACTION_GREAT_SAINT", ())
		
		# srpt: Pilgrim's button
		if iData1 >= 668 and iData1 <= 679:
			return CyTranslator().getText("TXT_KEY_ACTION_PILGRIM", ())
		
		# srpt: spy's barbarian bribe button
		if iData1 == 665:
			return CyTranslator().getText("TXT_KEY_ACTION_BRIBE", ())
		
		# srpt: spy's barbarian hire button
		if iData1 == 664:
			return CyTranslator().getText("TXT_KEY_ACTION_HIRE", ())
		
		# srpt: spy's silkworm stealing buttons
		if iData1 == 680:
			return CyTranslator().getText("TXT_KEY_ACTION_STEAL_SILKWORMS", ())
		if iData1 == 681:
			return CyTranslator().getText("TXT_KEY_ACTION_CULTIVATE_SILKWORMS", ())
		
		# srpt: secret diplomacy button
		if iData1 == 682:
			return CyTranslator().getText("TXT_KEY_ACTION_SECRET_DIPLOMACY", ())
			
		
	def getUpgradePriceOverride(self, argsList):
		iPlayer, iUnitID, iUnitTypeUpgrade = argsList
		
		# edead: start Scientific trait (original code by Tsentom1)
		
		# pPlayer = gc.getPlayer(iPlayer)
		# pUnit = pPlayer.getUnit(iUnitID)

		# iPrice = gc.getDefineINT("BASE_UNIT_UPGRADE_COST")
		# iPrice += (max(0, (pPlayer.getUnitProductionNeeded(iUnitTypeUpgrade) - pPlayer.getUnitProductionNeeded(pUnit.getUnitType()))) * gc.getDefineINT("UNIT_UPGRADE_COST_PER_PRODUCTION"))

		# if ((not pPlayer.isHuman()) and (not pPlayer.isBarbarian())):
			# pHandicapInfo = gc.getHandicapInfo(gc.getGame().getHandicapType())
			# iPrice = iPrice * pHandicapInfo.getAIUnitUpgradePercent() / 100
			# iPrice = iPrice * max(0, ((pHandicapInfo.getAIPerEraModifier() * pPlayer.getCurrentEra()) + 100)) / 100

		# iPrice = iPrice - ((iPrice * pUnit.getUpgradeDiscount()) / 100)

		# if (pPlayer.hasTrait(con.iScientific)):
			# iPrice = ((gc.getDefineINT("BASE_UNIT_UPGRADE_COST"))/2)
			# iPrice += (((max(0, (pPlayer.getUnitProductionNeeded(iUnitTypeUpgrade) - pPlayer.getUnitProductionNeeded(pUnit.getUnitType()))) * gc.getDefineINT("UNIT_UPGRADE_COST_PER_PRODUCTION")))/2)

			# if ((not pPlayer.isHuman()) and (not pPlayer.isBarbarian())):
				# pHandicapInfo = gc.getHandicapInfo(gc.getGame().getHandicapType())
				# iPrice = ((iPrice * pHandicapInfo.getAIUnitUpgradePercent() / 100)/2)
				# iPrice = ((iPrice * max(0, ((pHandicapInfo.getAIPerEraModifier() * pPlayer.getCurrentEra()) + 100)) / 100)/2)

				# iPrice = ((iPrice - ((iPrice * pUnit.getUpgradeDiscount()) / 100))/2)
		
		# return iPrice
		
		# edead: end
		
		return -1	# Any value 0 or above will be used
	
	def getExperienceNeeded(self, argsList):
		# use this function to set how much experience a unit needs
		iLevel, iOwner = argsList
		
		iExperienceNeeded = 0

		# regular epic game experience		
		iExperienceNeeded = iLevel * iLevel + 1

		iModifier = gc.getPlayer(iOwner).getLevelExperienceModifier()
		if (0 != iModifier):
			iExperienceNeeded += (iExperienceNeeded * iModifier + 99) / 100   # ROUND UP
			
		return iExperienceNeeded
		