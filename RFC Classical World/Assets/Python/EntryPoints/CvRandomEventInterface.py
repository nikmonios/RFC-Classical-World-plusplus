# Sid Meier's Civilization 4
# Copyright Firaxis Games 2005
#
# CvRandomEventInterface.py
#
# These functions are App Entry Points from C++
# WARNING: These function names should not be changed
# WARNING: These functions can not be placed into a class
#
# No other modules should import this
#
import CvUtil
from CvPythonExtensions import *

# edead: start
import Consts as con
import PyHelpers
from RFCUtils import utils
from StoredData import sd
from CvMainInterface import CvMainInterface
# edead: end

gc = CyGlobalContext()
localText = CyTranslator()
PyPlayer = PyHelpers.PyPlayer # edead


######## BLESSED SEA ###########

def getHelpBlessedSea1(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	
	map = gc.getMap()
	iOurMinLandmass = (3 * gc.getWorldInfo(map.getWorldSize()).getDefaultPlayers()) / 2
	
	szHelp = localText.getText("TXT_KEY_EVENT_BLESSED_SEA_HELP", (iOurMinLandmass, ))	

	return szHelp

def canTriggerBlessedSea(argsList):
	kTriggeredData = argsList[0]
	map = gc.getMap()
		
	if gc.getGame().isOption(GameOptionTypes.GAMEOPTION_ONE_CITY_CHALLENGE) and gc.getPlayer(kTriggeredData.ePlayer).isHuman():
		return false

	iMapMinLandmass = 2 * gc.getWorldInfo(map.getWorldSize()).getDefaultPlayers()
	iOurMaxLandmass = gc.getWorldInfo(map.getWorldSize()).getDefaultPlayers() / 2
	
	if (map.getNumLandAreas() < iMapMinLandmass):
		return false

	iOurLandmasses = 0
	for i in range(map.getIndexAfterLastArea()):
		area = map.getArea(i)
		if not area.isNone() and not area.isWater() and area.getCitiesPerPlayer(kTriggeredData.ePlayer) > 0:
			iOurLandmasses += 1
			
	if (iOurLandmasses > iOurMaxLandmass):
		return false

	player = gc.getPlayer(kTriggeredData.ePlayer)
	if player.getUnitClassCount(CvUtil.findInfoTypeNum(gc.getUnitClassInfo, gc.getNumUnitClassInfos(), 'UNITCLASS_GALLEY')) == 0:
		if player.getUnitClassCount(CvUtil.findInfoTypeNum(gc.getUnitClassInfo, gc.getNumUnitClassInfos(), 'UNITCLASS_CARAVEL')) == 0:
			if player.getUnitClassCount(CvUtil.findInfoTypeNum(gc.getUnitClassInfo, gc.getNumUnitClassInfos(), 'UNITCLASS_GALLEON')) == 0:
				return false
			
	return true

def canTriggerBlessedSea2(argsList):

	kTriggeredData = argsList[0]
	map = gc.getMap()
	iOurMinLandmass = (3 * gc.getWorldInfo(map.getWorldSize()).getDefaultPlayers()) / 2
	
	iOurLandmasses = 0
	for i in range(map.getIndexAfterLastArea()):
		area = map.getArea(i)
		if not area.isNone() and not area.isWater() and area.getCitiesPerPlayer(kTriggeredData.ePlayer) > 0:
			iOurLandmasses += 1
			
	if (iOurLandmasses < iOurMinLandmass):
		return false
	
	return true

def applyBlessedSea2(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
		
	iBuilding = -1
	
	if (-1 != kTriggeredData.eReligion):
		for i in range(gc.getNumBuildingInfos()):
			if (gc.getBuildingInfo(i).getSpecialBuildingType() == CvUtil.findInfoTypeNum(gc.getSpecialBuildingInfo,gc.getNumSpecialBuildingInfos(),'SPECIALBUILDING_TEMPLE')):
				if (gc.getBuildingInfo(i).getReligionType() == kTriggeredData.eReligion):
					iBuilding = i
					break
		
		
	if (iBuilding == -1):
		return
	
	player = gc.getPlayer(kTriggeredData.ePlayer)
	(loopCity, iter) = player.firstCity(false)

	while(loopCity):

		if (loopCity.getPopulation() >= 5):
			if (loopCity.canConstruct(iBuilding, false, false, true)):
				loopCity.setNumRealBuilding(iBuilding, 1)
				
		(loopCity, iter) = player.nextCity(iter, false)
		

def canApplyBlessedSea2(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
		
	iBuilding = -1
	
	if (-1 != kTriggeredData.eReligion):
		for i in range(gc.getNumBuildingInfos()):
			if (gc.getBuildingInfo(i).getSpecialBuildingType() == CvUtil.findInfoTypeNum(gc.getSpecialBuildingInfo,gc.getNumSpecialBuildingInfos(),'SPECIALBUILDING_TEMPLE')):
				if (gc.getBuildingInfo(i).getReligionType() == kTriggeredData.eReligion):
					iBuilding = i
					break
		
		
	if (iBuilding == -1):
		return false
	
	player = gc.getPlayer(kTriggeredData.ePlayer)
	(loopCity, iter) = player.firstCity(false)
	bFound = false

	while(loopCity):

		if (loopCity.getPopulation() >= 5):
			if (loopCity.canConstruct(iBuilding, false, false, true)):
				bFound = true
				break
				
		(loopCity, iter) = player.nextCity(iter, false)

	return bFound


######## HOLY MOUNTAIN ###########

def getHelpHolyMountain1(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	
	map = gc.getMap()
	iMinPoints = 2 * gc.getWorldInfo(map.getWorldSize()).getDefaultPlayers()
	
	iBuilding = -1
	iReligion = gc.getPlayer(kTriggeredData.ePlayer).getStateReligion()
	
	if (-1 != iReligion):
		for i in range(gc.getNumBuildingInfos()):
			if (gc.getBuildingInfo(i).getSpecialBuildingType() == CvUtil.findInfoTypeNum(gc.getSpecialBuildingInfo, gc.getNumSpecialBuildingInfos(), 'SPECIALBUILDING_CATHEDRAL')):
				if (gc.getBuildingInfo(i).getReligionType() == iReligion):
					iBuilding = i
					break


		szHelp = localText.getText("TXT_KEY_EVENT_HOLY_MOUNTAIN_HELP", ( gc.getBuildingInfo(iBuilding).getTextKey(), gc.getBuildingInfo(iBuilding).getTextKey(), iMinPoints))

	return szHelp

def canTriggerHolyMountain(argsList):
	kTriggeredData = argsList[0]
	map = gc.getMap()
	
	if gc.getGame().isOption(GameOptionTypes.GAMEOPTION_ONE_CITY_CHALLENGE) and gc.getPlayer(kTriggeredData.ePlayer).isHuman():
		return false

	plot = gc.getMap().plot(kTriggeredData.iPlotX, kTriggeredData.iPlotY)
	if (plot.getOwner() == -1):
		return true
	
	return false

def expireHolyMountain1(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]

	plot = gc.getMap().plot(kTriggeredData.iPlotX, kTriggeredData.iPlotY)
	if (plot == None):
		return true
	
	if (plot.getOwner() != kTriggeredData.ePlayer and plot.getOwner() != -1):
		return true
		
	return false

def canTriggerHolyMountainDone(argsList):

	kTriggeredData = argsList[0]
	trigger = gc.getEventTriggerInfo(kTriggeredData.eTrigger)
	player = gc.getPlayer(kTriggeredData.ePlayer)
	
	kOrigTriggeredData = player.getEventOccured(trigger.getPrereqEvent(0))
	
	if (kOrigTriggeredData == None):
		return false
		
	plot = gc.getMap().plot(kOrigTriggeredData.iPlotX, kOrigTriggeredData.iPlotY)
	if (plot == None):
		return false
	
	if (plot.getOwner() != kTriggeredData.ePlayer):
		return false
	
	return true

def canTriggerHolyMountainRevealed(argsList):

	kTriggeredData = argsList[0]
	trigger = gc.getEventTriggerInfo(kTriggeredData.eTrigger)
	player = gc.getPlayer(kTriggeredData.ePlayer)
	
	kOrigTriggeredData = player.getEventOccured(trigger.getPrereqEvent(0))
	
	if (kOrigTriggeredData == None):
		return false

	iNumPoints = 0		
	
	for i in range(gc.getNumBuildingInfos()):
		if (gc.getBuildingInfo(i).getReligionType() == kOrigTriggeredData.eReligion):
			if (gc.getBuildingInfo(i).getSpecialBuildingType() == CvUtil.findInfoTypeNum(gc.getSpecialBuildingInfo,gc.getNumSpecialBuildingInfos(),'SPECIALBUILDING_CATHEDRAL')):
				iNumPoints += 4 * player.countNumBuildings(i)
			elif (gc.getBuildingInfo(i).getSpecialBuildingType() == CvUtil.findInfoTypeNum(gc.getSpecialBuildingInfo,gc.getNumSpecialBuildingInfos(),'SPECIALBUILDING_TEMPLE')):
				iNumPoints += player.countNumBuildings(i)
			elif (gc.getBuildingInfo(i).getSpecialBuildingType() == CvUtil.findInfoTypeNum(gc.getSpecialBuildingInfo,gc.getNumSpecialBuildingInfos(),'SPECIALBUILDING_MONASTERY')):
				iNumPoints += player.countNumBuildings(i)
				
	if (iNumPoints < 2 * gc.getWorldInfo(gc.getMap().getWorldSize()).getDefaultPlayers()):
		return false

	plot = gc.getMap().plot(kOrigTriggeredData.iPlotX, kOrigTriggeredData.iPlotY)
	if (plot == None):
		return false
		
	plot.setRevealed(player.getTeam(), true, true, -1)

	kActualTriggeredDataObject = player.getEventTriggered(kTriggeredData.iId)
	kActualTriggeredDataObject.iPlotX = kOrigTriggeredData.iPlotX
	kActualTriggeredDataObject.iPlotY = kOrigTriggeredData.iPlotY
	
	return true

def doHolyMountainRevealed(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]

	if (kTriggeredData.ePlayer == gc.getGame().getActivePlayer()):
		CyCamera().JustLookAtPlot( CyMap().plot( kTriggeredData.iPlotX, kTriggeredData.iPlotY ) )

	return 1

######## MARATHON ###########

def canTriggerMarathon(argsList):	
	kTriggeredData = argsList[0]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	otherPlayer = gc.getPlayer(kTriggeredData.eOtherPlayer)
	team = gc.getTeam(player.getTeam())
	
	if (team.AI_getAtWarCounter(otherPlayer.getTeam()) == 1):
		(loopUnit, iter) = otherPlayer.firstUnit(false)
		while( loopUnit ):
			plot = loopUnit.plot()
			if (not plot.isNone()):
				if (plot.getOwner() == kTriggeredData.ePlayer):
					return true
			(loopUnit, iter) = otherPlayer.nextUnit(iter, false)

	return false

######## WEDDING FEUD ###########

def doWeddingFeud2(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	
	player = gc.getPlayer(kTriggeredData.ePlayer)
	(loopCity, iter) = player.firstCity(false)

	while(loopCity):
		if loopCity.isHasReligion(kTriggeredData.eReligion):
			loopCity.changeHappinessTimer(30)
		(loopCity, iter) = player.nextCity(iter, false)
		
	return 1

def getHelpWeddingFeud2(argsList):
	iEvent = argsList[0]
	event = gc.getEventInfo(iEvent)
	kTriggeredData = argsList[1]
	religion = gc.getReligionInfo(kTriggeredData.eReligion)

	szHelp = localText.getText("TXT_KEY_EVENT_WEDDING_FEUD_2_HELP", (gc.getDefineINT("TEMP_HAPPY"), 30, religion.getChar()))

	return szHelp

def canDoWeddingFeud3(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]

	player = gc.getPlayer(kTriggeredData.ePlayer)
	
	if player.getGold() - 10 * player.getNumCities() < 0:
		return false
				
	return true


def doWeddingFeud3(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	
	destPlayer = gc.getPlayer(kTriggeredData.eOtherPlayer)
	player = gc.getPlayer(kTriggeredData.ePlayer)
	
	for iLoopPlayer in range(gc.getMAX_CIV_PLAYERS()):
		loopPlayer = gc.getPlayer(iLoopPlayer)
		if loopPlayer.isAlive() and loopPlayer.getStateReligion() == player.getStateReligion():
			loopPlayer.AI_changeAttitudeExtra(kTriggeredData.ePlayer, 1)
			player.AI_changeAttitudeExtra(iLoopPlayer, 1)

	if gc.getTeam(destPlayer.getTeam()).canDeclareWar(player.getTeam()):			
		if destPlayer.isHuman():
			# this works only because it's a single-player only event
			popupInfo = CyPopupInfo()
			popupInfo.setButtonPopupType(ButtonPopupTypes.BUTTONPOPUP_PYTHON)
			popupInfo.setText(localText.getText("TXT_KEY_EVENT_WEDDING_FEUD_OTHER_3", (gc.getReligionInfo(kTriggeredData.eReligion).getAdjectiveKey(), player.getCivilizationShortDescriptionKey())))
			popupInfo.setData1(kTriggeredData.eOtherPlayer)
			popupInfo.setData2(kTriggeredData.ePlayer)
			popupInfo.setPythonModule("CvRandomEventInterface")
			popupInfo.setOnClickedPythonCallback("weddingFeud3Callback")
			popupInfo.addPythonButton(localText.getText("TXT_KEY_POPUP_YES", ()), "")
			popupInfo.addPythonButton(localText.getText("TXT_KEY_POPUP_NO", ()), "")
			popupInfo.addPopup(kTriggeredData.eOtherPlayer)
		else:
			gc.getTeam(destPlayer.getTeam()).declareWar(player.getTeam(), false, WarPlanTypes.WARPLAN_LIMITED)
			
	return 1


def weddingFeud3Callback(argsList):
	iButton = argsList[0]
	iData1 = argsList[1]
	iData2 = argsList[2]
	iData3 = argsList[3]
	szText = argsList[4]
	bOption1 = argsList[5]
	bOption2 = argsList[6]
	
	if iButton == 0:
		destPlayer = gc.getPlayer(iData1)
		player = gc.getPlayer(iData2)
		gc.getTeam(destPlayer.getTeam()).declareWar(player.getTeam(), false, WarPlanTypes.WARPLAN_LIMITED)
	
	return 0

def getHelpWeddingFeud3(argsList):
	iEvent = argsList[0]
	event = gc.getEventInfo(iEvent)
	kTriggeredData = argsList[1]
	religion = gc.getReligionInfo(kTriggeredData.eReligion)

	szHelp = localText.getText("TXT_KEY_EVENT_WEDDING_FEUD_3_HELP", (1, religion.getChar()))

	return szHelp

######## SPICY ###########

def canTriggerSpicy(argsList):

	kTriggeredData = argsList[0]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	
	iSpice = CvUtil.findInfoTypeNum(gc.getBonusInfo,gc.getNumBonusInfos(),'BONUS_SPICES')
	iHappyBonuses = 0
	bSpices = false
	for i in range(gc.getNumBonusInfos()):
		bonus = gc.getBonusInfo(i)
		iNum = player.getNumAvailableBonuses(i)
		if iNum > 0 :
			if bonus.getHappiness() > 0:
				iHappyBonuses += 1
				if iHappyBonuses > 4:
					return false
			if i == iSpice:
				return false

	plot = gc.getMap().plot(kTriggeredData.iPlotX, kTriggeredData.iPlotY)
	if not plot.canHaveBonus(iSpice, false):
		return false
	
	return true

def doSpicy2(argsList):
#	need this because plantations are notmally not allowed unless there are already spices
	iEvent = argsList[0]
	kTriggeredData = argsList[1]

	plot = gc.getMap().plot(kTriggeredData.iPlotX, kTriggeredData.iPlotY)
	
	if not plot.isNone():
		plot.setImprovementType(CvUtil.findInfoTypeNum(gc.getImprovementInfo,gc.getNumImprovementInfos(),'IMPROVEMENT_PLANTATION'))
	
	return 1

def getHelpSpicy2(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	
	iPlantation = CvUtil.findInfoTypeNum(gc.getImprovementInfo,gc.getNumImprovementInfos(),'IMPROVEMENT_PLANTATION')
	szHelp = localText.getText("TXT_KEY_EVENT_IMPROVEMENT_GROWTH", ( gc.getImprovementInfo(iPlantation).getTextKey(), ))

	return szHelp

######## BABY BOOM ###########

def canTriggerBabyBoom(argsList):
	kTriggeredData = argsList[0]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	team = gc.getTeam(player.getTeam())

	if team.getAtWarCount(true) > 0:
		return false

	for iLoopTeam in range(gc.getMAX_CIV_TEAMS()):
		if iLoopTeam != player.getTeam():
			if team.AI_getAtPeaceCounter(iLoopTeam) == 1:
				return true

	return false

######## BARD TALE ###########

def applyBardTale3(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]

	player = gc.getPlayer(kTriggeredData.ePlayer)
	
	player.changeGold(-10 * player.getNumCities())
	
def canApplyBardTale3(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]

	player = gc.getPlayer(kTriggeredData.ePlayer)
	
	if player.getGold() - 10 * player.getNumCities() < 0:
		return false
		
	return true
	

def getHelpBardTale3(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]

	player = gc.getPlayer(kTriggeredData.ePlayer)
	
	szHelp = localText.getText("TXT_KEY_EVENT_GOLD_LOST", (10 * player.getNumCities(), ))	

	return szHelp

######## LOOTERS ###########

def getHelpLooters3(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	otherPlayer = gc.getPlayer(kTriggeredData.eOtherPlayer)
	city = otherPlayer.getCity(kTriggeredData.iOtherPlayerCityId)

	szHelp = localText.getText("TXT_KEY_EVENT_LOOTERS_3_HELP", (1, 2, city.getNameKey()))

	return szHelp

def canApplyLooters3(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]

	otherPlayer = gc.getPlayer(kTriggeredData.eOtherPlayer)
	city = otherPlayer.getCity(kTriggeredData.iOtherPlayerCityId)

	iNumBuildings = 0	
	for iBuilding in range(gc.getNumBuildingInfos()):
		if (city.getNumRealBuilding(iBuilding) > 0 and gc.getBuildingInfo(iBuilding).getProductionCost() <= 100 and gc.getBuildingInfo(iBuilding).getProductionCost() > 0  and not isLimitedWonderClass(gc.getBuildingInfo(iBuilding).getBuildingClassType())):
			iNumBuildings += 1
		
	return (iNumBuildings > 0)
	

def applyLooters3(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]

	otherPlayer = gc.getPlayer(kTriggeredData.eOtherPlayer)
	city = otherPlayer.getCity(kTriggeredData.iOtherPlayerCityId)
	
	iNumBuildings = gc.getGame().getSorenRandNum(2, "Looters event number of buildings destroyed")
	iNumBuildingsDestroyed = 0

	listBuildings = []	
	for iBuilding in range(gc.getNumBuildingInfos()):
		if (city.getNumRealBuilding(iBuilding) > 0 and gc.getBuildingInfo(iBuilding).getProductionCost() <= 100 and gc.getBuildingInfo(iBuilding).getProductionCost() > 0  and not isLimitedWonderClass(gc.getBuildingInfo(iBuilding).getBuildingClassType())):
			listBuildings.append(iBuilding)

	for i in range(iNumBuildings+1):
		if len(listBuildings) > 0:
			iBuilding = listBuildings[gc.getGame().getSorenRandNum(len(listBuildings), "Looters event building destroyed")]
			szBuffer = localText.getText("TXT_KEY_EVENT_CITY_IMPROVEMENT_DESTROYED", (gc.getBuildingInfo(iBuilding).getTextKey(), ))
			CyInterface().addMessage(kTriggeredData.eOtherPlayer, false, gc.getEVENT_MESSAGE_TIME(), szBuffer, "AS2D_BOMBARDED", InterfaceMessageTypes.MESSAGE_TYPE_INFO, gc.getBuildingInfo(iBuilding).getButton(), gc.getInfoTypeForString("COLOR_RED"), city.getX(), city.getY(), true, true)
			city.setNumRealBuilding(iBuilding, 0)
			iNumBuildingsDestroyed += 1
			listBuildings.remove(iBuilding)
				
	if iNumBuildingsDestroyed > 0:
		szBuffer = localText.getText("TXT_KEY_EVENT_NUM_BUILDINGS_DESTROYED", (iNumBuildingsDestroyed, gc.getPlayer(kTriggeredData.eOtherPlayer).getCivilizationAdjectiveKey(), city.getNameKey()))
		CyInterface().addMessage(kTriggeredData.ePlayer, false, gc.getEVENT_MESSAGE_TIME(), szBuffer, "AS2D_BOMBARDED", InterfaceMessageTypes.MESSAGE_TYPE_INFO, None, gc.getInfoTypeForString("COLOR_WHITE"), -1, -1, true, true)

######## BROTHERS IN NEED ###########

def canTriggerBrothersInNeed(argsList):
	kTriggeredData = argsList[0]
	trigger = gc.getEventTriggerInfo(kTriggeredData.eTrigger)
	player = gc.getPlayer(kTriggeredData.ePlayer)
	otherPlayer = gc.getPlayer(kTriggeredData.eOtherPlayer)
	
	if not player.canTradeNetworkWith(kTriggeredData.eOtherPlayer):
		return false
	
	listResources = []
	#listResources.append(CvUtil.findInfoTypeNum(gc.getBonusInfo,gc.getNumBonusInfos(),'BONUS_COPPER')) # edead
	listResources.append(CvUtil.findInfoTypeNum(gc.getBonusInfo,gc.getNumBonusInfos(),'BONUS_IRON'))
	listResources.append(CvUtil.findInfoTypeNum(gc.getBonusInfo,gc.getNumBonusInfos(),'BONUS_HORSE'))
	#listResources.append(CvUtil.findInfoTypeNum(gc.getBonusInfo,gc.getNumBonusInfos(),'BONUS_IVORY')) # edead
	#listResources.append(CvUtil.findInfoTypeNum(gc.getBonusInfo,gc.getNumBonusInfos(),'BONUS_OIL')) # edead
	#listResources.append(CvUtil.findInfoTypeNum(gc.getBonusInfo,gc.getNumBonusInfos(),'BONUS_URANIUM')) # edead

	bFound = false
	for iResource in listResources: 
		if (player.getNumTradeableBonuses(iResource) > 1 and otherPlayer.getNumAvailableBonuses(iResource) <= 0):
			bFound = true
			break
		
	if not bFound:
		return false
		
	for iTeam in range(gc.getMAX_CIV_TEAMS()):
		if iTeam != player.getTeam() and iTeam != otherPlayer.getTeam() and gc.getTeam(iTeam).isAlive():
			if gc.getTeam(iTeam).isAtWar(otherPlayer.getTeam()) and not gc.getTeam(iTeam).isAtWar(player.getTeam()):
				return true
			
	return false
	
def canDoBrothersInNeed1(argsList):
	kTriggeredData = argsList[1]
	newArgs = (kTriggeredData, )
	
	return canTriggerBrothersInNeed(newArgs)
	
######## HURRICANE ###########

def canTriggerHurricaneCity(argsList):
	eTrigger = argsList[0]
	ePlayer = argsList[1]
	iCity = argsList[2]
	
	player = gc.getPlayer(ePlayer)
	city = player.getCity(iCity)
	
	if city.isNone():
		return false
		
	if not city.isCoastal(gc.getMIN_WATER_SIZE_FOR_OCEAN()):
		return false
		
	# if city.plot().getLatitude() <= 0:
		# return false
	
	if not city.plot().getRegionID() in [con.rPunt, con.rArabiaFelix, con.rLanka, con.rSumatra, con.rJava]:
		return false
		
	if city.getPopulation() < 2:
		return false
		
	return true

def canApplyHurricane1(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	
	player = gc.getPlayer(kTriggeredData.ePlayer)
	city = player.getCity(kTriggeredData.iCityId)
	
	listBuildings = []	
	for iBuilding in range(gc.getNumBuildingInfos()):
		if (city.getNumRealBuilding(iBuilding) > 0 and gc.getBuildingInfo(iBuilding).getProductionCost() > 0 and not isLimitedWonderClass(gc.getBuildingInfo(iBuilding).getBuildingClassType())):
			listBuildings.append(iBuilding)
			
	return (len(listBuildings) > 0)

def canApplyHurricane2(argsList):			
	return (not canApplyHurricane1(argsList))

		
def applyHurricane1(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	
	player = gc.getPlayer(kTriggeredData.ePlayer)
	city = player.getCity(kTriggeredData.iCityId)
	
	listCheapBuildings = []	
	listExpensiveBuildings = []	
	for iBuilding in range(gc.getNumBuildingInfos()):
		if (city.getNumRealBuilding(iBuilding) > 0 and gc.getBuildingInfo(iBuilding).getProductionCost() <= 100 and gc.getBuildingInfo(iBuilding).getProductionCost() > 0 and not isLimitedWonderClass(gc.getBuildingInfo(iBuilding).getBuildingClassType())):
			listCheapBuildings.append(iBuilding)
		if (city.getNumRealBuilding(iBuilding) > 0 and gc.getBuildingInfo(iBuilding).getProductionCost() > 100 and gc.getBuildingInfo(iBuilding).getProductionCost() > 0 and not isLimitedWonderClass(gc.getBuildingInfo(iBuilding).getBuildingClassType())):
			listExpensiveBuildings.append(iBuilding)

	if len(listCheapBuildings) > 0:
		iBuilding = listCheapBuildings[gc.getGame().getSorenRandNum(len(listCheapBuildings), "Hurricane event cheap building destroyed")]
		szBuffer = localText.getText("TXT_KEY_EVENT_CITY_IMPROVEMENT_DESTROYED", (gc.getBuildingInfo(iBuilding).getTextKey(), ))
		CyInterface().addMessage(kTriggeredData.ePlayer, false, gc.getEVENT_MESSAGE_TIME(), szBuffer, "AS2D_BOMBARDED", InterfaceMessageTypes.MESSAGE_TYPE_INFO, gc.getBuildingInfo(iBuilding).getButton(), gc.getInfoTypeForString("COLOR_RED"), city.getX(), city.getY(), true, true)
		city.setNumRealBuilding(iBuilding, 0)

	if len(listExpensiveBuildings) > 0:
		iBuilding = listExpensiveBuildings[gc.getGame().getSorenRandNum(len(listExpensiveBuildings), "Hurricane event expensive building destroyed")]
		szBuffer = localText.getText("TXT_KEY_EVENT_CITY_IMPROVEMENT_DESTROYED", (gc.getBuildingInfo(iBuilding).getTextKey(), ))
		CyInterface().addMessage(kTriggeredData.ePlayer, false, gc.getEVENT_MESSAGE_TIME(), szBuffer, "AS2D_BOMBARDED", InterfaceMessageTypes.MESSAGE_TYPE_INFO, gc.getBuildingInfo(iBuilding).getButton(), gc.getInfoTypeForString("COLOR_RED"), city.getX(), city.getY(), true, true)
		city.setNumRealBuilding(iBuilding, 0)

		
######## CYCLONE ###########

def canTriggerCycloneCity(argsList):
	eTrigger = argsList[0]
	ePlayer = argsList[1]
	iCity = argsList[2]
	
	player = gc.getPlayer(ePlayer)
	city = player.getCity(iCity)
	
	if city.isNone():
		return false
		
	if not city.isCoastal(gc.getMIN_WATER_SIZE_FOR_OCEAN()):
		return false
	
	if not city.plot().getRegionID() in [con.rPunt, con.rArabiaFelix, con.rLanka, con.rSumatra, con.rJava]:
		return false
	
	# if city.plot().getLatitude() >= 0:
		# return false
		
	return true

######## TSUNAMI ###########

def canTriggerTsunamiCity(argsList):
	eTrigger = argsList[0]
	ePlayer = argsList[1]
	iCity = argsList[2]
	
	player = gc.getPlayer(ePlayer)
	city = player.getCity(iCity)
	
	if city.isNone():
		return false
		
	if not city.isCoastal(gc.getMIN_WATER_SIZE_FOR_OCEAN()):
		return false
				
	return true

def canApplyTsunami1(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	
	player = gc.getPlayer(kTriggeredData.ePlayer)
	city = player.getCity(kTriggeredData.iCityId)
	
	return (city.getPopulation() < 6)

def canApplyTsunami2(argsList):			
	return (not canApplyTsunami1(argsList))

		
def applyTsunami1(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	
	player = gc.getPlayer(kTriggeredData.ePlayer)
	city = player.getCity(kTriggeredData.iCityId)
	
	city.kill()
	
def applyTsunami2(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	
	player = gc.getPlayer(kTriggeredData.ePlayer)
	city = player.getCity(kTriggeredData.iCityId)
	
	listBuildings = []	
	for iBuilding in range(gc.getNumBuildingInfos()):
		if (city.getNumRealBuilding(iBuilding) > 0 and gc.getBuildingInfo(iBuilding).getProductionCost() > 0  and not isLimitedWonderClass(gc.getBuildingInfo(iBuilding).getBuildingClassType())):
			listBuildings.append(iBuilding)

	for i in range(5):
		if len(listBuildings) > 0:
			iBuilding = listBuildings[gc.getGame().getSorenRandNum(len(listBuildings), "Tsunami event building destroyed")]
			szBuffer = localText.getText("TXT_KEY_EVENT_CITY_IMPROVEMENT_DESTROYED", (gc.getBuildingInfo(iBuilding).getTextKey(), ))
			CyInterface().addMessage(kTriggeredData.ePlayer, false, gc.getEVENT_MESSAGE_TIME(), szBuffer, "AS2D_BOMBARDED", InterfaceMessageTypes.MESSAGE_TYPE_INFO, gc.getBuildingInfo(iBuilding).getButton(), gc.getInfoTypeForString("COLOR_RED"), city.getX(), city.getY(), true, true)
			city.setNumRealBuilding(iBuilding, 0)
			listBuildings.remove(iBuilding)
					

def getHelpTsunami2(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	city = player.getCity(kTriggeredData.iCityId)

	szHelp = localText.getText("TXT_KEY_EVENT_TSUNAMI_2_HELP", (5, city.getNameKey()))

	return szHelp

		
######## MONSOON ###########

def canTriggerMonsoonCity(argsList):
	eTrigger = argsList[0]
	ePlayer = argsList[1]
	iCity = argsList[2]
	
	player = gc.getPlayer(ePlayer)
	city = player.getCity(iCity)
	
	if city.isNone():
		return false
		
	# if city.isCoastal(gc.getMIN_WATER_SIZE_FOR_OCEAN()):
		# return false
		
	if city.plot().getRegionID() in [con.rSindh, con.rAvanti, con.rPunjab, con.rMagadha, con.rKerala, con.rTamilNadu, con.rKalinka, con.rBangala, con.rLanka]:
		return true
				
	return false

######## VOLCANO ###########

def getHelpVolcano1(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]

	szHelp = localText.getText("TXT_KEY_EVENT_VOLCANO_1_HELP", ())

	return szHelp

def canApplyVolcano1(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	
	iNumImprovements = 0
	for iDX in range(-1, 2):
		for iDY in range(-1, 2):
			loopPlot = plotXY(kTriggeredData.iPlotX, kTriggeredData.iPlotY, iDX, iDY)
			if not loopPlot.isNone():
				if (iDX != 0 or iDY != 0):
					if loopPlot.getImprovementType() != -1:
						iNumImprovements += 1

	return (iNumImprovements > 0)

def applyVolcano1(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	
	listPlots = []
	for iDX in range(-1, 2):
		for iDY in range(-1, 2):
			loopPlot = plotXY(kTriggeredData.iPlotX, kTriggeredData.iPlotY, iDX, iDY)
			if not loopPlot.isNone():
				if (iDX != 0 or iDY != 0):
					if loopPlot.getImprovementType() != -1:
						listPlots.append(loopPlot)
					
	listRuins = []
	listRuins.append(CvUtil.findInfoTypeNum(gc.getImprovementInfo,gc.getNumImprovementInfos(),'IMPROVEMENT_COTTAGE'))
	listRuins.append(CvUtil.findInfoTypeNum(gc.getImprovementInfo,gc.getNumImprovementInfos(),'IMPROVEMENT_HAMLET'))
	listRuins.append(CvUtil.findInfoTypeNum(gc.getImprovementInfo,gc.getNumImprovementInfos(),'IMPROVEMENT_VILLAGE'))
	listRuins.append(CvUtil.findInfoTypeNum(gc.getImprovementInfo,gc.getNumImprovementInfos(),'IMPROVEMENT_TOWN'))
	
	iRuins = CvUtil.findInfoTypeNum(gc.getImprovementInfo,gc.getNumImprovementInfos(),'IMPROVEMENT_CITY_RUINS')

	for i in range(3):
		if len(listPlots) > 0:
			plot = listPlots[gc.getGame().getSorenRandNum(len(listPlots), "Volcano event improvement destroyed")]
			iImprovement = plot.getImprovementType()
			szBuffer = localText.getText("TXT_KEY_EVENT_CITY_IMPROVEMENT_DESTROYED", (gc.getImprovementInfo(iImprovement).getTextKey(), ))
			CyInterface().addMessage(kTriggeredData.ePlayer, false, gc.getEVENT_MESSAGE_TIME(), szBuffer, "AS2D_BOMBARDED", InterfaceMessageTypes.MESSAGE_TYPE_INFO, gc.getImprovementInfo(iImprovement).getButton(), gc.getInfoTypeForString("COLOR_RED"), plot.getX(), plot.getY(), true, true)
			if iImprovement in listRuins:
				plot.setImprovementType(iRuins)
			else:
				plot.setImprovementType(-1)
			listPlots.remove(plot)
			
			if i == 1 and gc.getGame().getSorenRandNum(100, "Volcano event num improvements destroyed") < 50:
				break

######## DUSTBOWL ###########

def canTriggerDustbowlCont(argsList):
	kTriggeredData = argsList[0]

	trigger = gc.getEventTriggerInfo(kTriggeredData.eTrigger)
	player = gc.getPlayer(kTriggeredData.ePlayer)
	
	kOrigTriggeredData = player.getEventOccured(trigger.getPrereqEvent(0))
	
	if (kOrigTriggeredData == None):
		return false

	iFarmType = CvUtil.findInfoTypeNum(gc.getImprovementInfo,gc.getNumImprovementInfos(),'IMPROVEMENT_FARM')
	iPlainsType = CvUtil.findInfoTypeNum(gc.getTerrainInfo,gc.getNumTerrainInfos(),'TERRAIN_PLAINS')
	
	map = gc.getMap()
	iBestValue = map.getGridWidth() + map.getGridHeight()
	bestPlot = None
	for i in range(map.numPlots()):
		plot = map.plotByIndex(i)
		if (plot.getOwner() == kTriggeredData.ePlayer and plot.getImprovementType() == iFarmType and plot.getTerrainType() == iPlainsType):
			iValue = plotDistance(kOrigTriggeredData.iPlotX, kOrigTriggeredData.iPlotY, plot.getX(), plot.getY())
			if iValue < iBestValue:
				iBestValue = iValue
				bestPlot = plot
				
	if bestPlot != None:
		kActualTriggeredDataObject = player.getEventTriggered(kTriggeredData.iId)
		kActualTriggeredDataObject.iPlotX = bestPlot.getX()
		kActualTriggeredDataObject.iPlotY = bestPlot.getY()
	else:
		player.resetEventOccured(trigger.getPrereqEvent(0))
		return false
		
	return true

def getHelpDustBowl2(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]

	szHelp = localText.getText("TXT_KEY_EVENT_DUSTBOWL_2_HELP", ())

	return szHelp

######## SALTPETER ###########

def getSaltpeterNumExtraPlots():
	map = gc.getMap()	
	if map.getWorldSize() <= 1:
		return 1
	elif map.getWorldSize() <= 3:
		return 2
	elif map.getWorldSize() <= 4:
		return 3
	else:
		return 4

def getHelpSaltpeter(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]

	szHelp = localText.getText("TXT_KEY_EVENT_SALTPETER_HELP", (getSaltpeterNumExtraPlots(), ))

	return szHelp

def canApplySaltpeter(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	
	map = gc.getMap()
	
	player = gc.getPlayer(kTriggeredData.ePlayer)

	plot = gc.getMap().plot(kTriggeredData.iPlotX, kTriggeredData.iPlotY)
	if (plot == None):
		return false
		
	iForest = CvUtil.findInfoTypeNum(gc.getFeatureInfo,gc.getNumFeatureInfos(),'FEATURE_FOREST')
	
	iNumPlots = 0
	for i in range(map.numPlots()):
		loopPlot = map.plotByIndex(i)
		if (loopPlot.getOwner() == kTriggeredData.ePlayer and loopPlot.getFeatureType() == iForest and loopPlot.isHills()):
			iDistance = plotDistance(kTriggeredData.iPlotX, kTriggeredData.iPlotY, loopPlot.getX(), loopPlot.getY())
			if iDistance > 0:
				iNumPlots += 1
	
	return (iNumPlots >= getSaltpeterNumExtraPlots())

def applySaltpeter(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]

	map = gc.getMap()
	
	player = gc.getPlayer(kTriggeredData.ePlayer)

	plot = gc.getMap().plot(kTriggeredData.iPlotX, kTriggeredData.iPlotY)
	if (plot == None):
		return
		
	iForest = CvUtil.findInfoTypeNum(gc.getFeatureInfo,gc.getNumFeatureInfos(),'FEATURE_FOREST')
	
	listPlots = []
	for i in range(map.numPlots()):
		loopPlot = map.plotByIndex(i)
		if (loopPlot.getOwner() == kTriggeredData.ePlayer and loopPlot.getFeatureType() == iForest and loopPlot.isHills()):
			iDistance = plotDistance(kTriggeredData.iPlotX, kTriggeredData.iPlotY, loopPlot.getX(), loopPlot.getY())
			if iDistance > 0:
				listPlots.append((iDistance, loopPlot))

	listPlots.sort()
	
	iCount = getSaltpeterNumExtraPlots()
	for loopPlot in listPlots:
		if iCount == 0:
			break
		iCount -= 1
		gc.getGame().setPlotExtraYield(loopPlot[1].getX(), loopPlot[1].getY(), YieldTypes.YIELD_COMMERCE, 1)
		CyInterface().addMessage(kTriggeredData.ePlayer, false, gc.getEVENT_MESSAGE_TIME(), localText.getText("TXT_KEY_EVENT_SALTPETER_DISCOVERED", ()), "", InterfaceMessageTypes.MESSAGE_TYPE_INFO, None, gc.getInfoTypeForString("COLOR_WHITE"), loopPlot[1].getX(), loopPlot[1].getY(), true, true)

######## CHAMPION ###########

def canTriggerChampion(argsList):	
	kTriggeredData = argsList[0]
	
	player = gc.getPlayer(kTriggeredData.ePlayer)
	team = gc.getTeam(player.getTeam())

	if team.getAtWarCount(true) > 0:
		return false
				
	return true
	
def canTriggerChampionUnit(argsList):
	eTrigger = argsList[0]
	ePlayer = argsList[1]
	iUnit = argsList[2]
	
	player = gc.getPlayer(ePlayer)
	unit = player.getUnit(iUnit)
	
	if unit.isNone():
		return false
		
	if unit.getDamage() > 0:
		return false
		
	if unit.getExperience() < 3:
		return false

	iLeadership = CvUtil.findInfoTypeNum(gc.getPromotionInfo,gc.getNumPromotionInfos(),'PROMOTION_LEADERSHIP')
	if unit.isHasPromotion(iLeadership):
		return false

	return true
	
def applyChampion(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]

	player = gc.getPlayer(kTriggeredData.ePlayer)
	unit = player.getUnit(kTriggeredData.iUnitId)
	
	iLeadership = CvUtil.findInfoTypeNum(gc.getPromotionInfo,gc.getNumPromotionInfos(),'PROMOTION_LEADERSHIP')
	
	unit.setHasPromotion(iLeadership, true)
	
def getHelpChampion(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	
	player = gc.getPlayer(kTriggeredData.ePlayer)
	unit = player.getUnit(kTriggeredData.iUnitId)
	
	iLeadership = CvUtil.findInfoTypeNum(gc.getPromotionInfo,gc.getNumPromotionInfos(),'PROMOTION_LEADERSHIP')

	szHelp = localText.getText("TXT_KEY_EVENT_CHAMPION_HELP", (unit.getNameKey(), gc.getPromotionInfo(iLeadership).getTextKey()))	

	return szHelp
	
######## GOLD RUSH ###########

def canTriggerGoldRush(argsList):	
	kTriggeredData = argsList[0]
	
	player = gc.getPlayer(kTriggeredData.ePlayer)
	
	iIndustrial = CvUtil.findInfoTypeNum(gc.getEraInfo,gc.getNumEraInfos(),'ERA_INDUSTRIAL')
	
	if player.getCurrentEra() != iIndustrial:
		return false
	
						
	return true
	
######## INFLUENZA ###########

def canTriggerInfluenza(argsList):	
	kTriggeredData = argsList[0]
	
	player = gc.getPlayer(kTriggeredData.ePlayer)
	team = gc.getTeam(player.getTeam())
	
	#iIndustrial = CvUtil.findInfoTypeNum(gc.getEraInfo,gc.getNumEraInfos(),'ERA_INDUSTRIAL')
	iIndustrial = CvUtil.findInfoTypeNum(gc.getEraInfo,gc.getNumEraInfos(),'ERA_LATE_MIDDLE_AGES')
	
	if player.getCurrentEra() <= iIndustrial:
		return false
	
	#iMedicine = CvUtil.findInfoTypeNum(gc.getTechInfo,gc.getNumTechInfos(),'TECH_MEDICINE') # edead
	
	#if team.isHasTech(iMedicine): # edead
	#	return false # edead
						
	return true
	
def applyInfluenza2(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
		
	player = gc.getPlayer(kTriggeredData.ePlayer)
	eventCity = player.getCity(kTriggeredData.iCityId)

	iNumCities = 2 + gc.getGame().getSorenRandNum(3, "Influenza event number of cities")

	listCities = []	
	(loopCity, iter) = player.firstCity(false)
	while(loopCity):
		if loopCity.getPopulation() > 2:
			iDistance = plotDistance(eventCity.getX(), eventCity.getY(), loopCity.getX(), loopCity.getY())
			if iDistance > 0:
				listCities.append((iDistance, loopCity))
		(loopCity, iter) = player.nextCity(iter, false)
		
	listCities.sort()
	
	if iNumCities > len(listCities): 
		iNumCities = len(listCities)
				
	for i in range(iNumCities):
		(iDist, loopCity) = listCities[i]
		loopCity.changePopulation(-2)
		szBuffer = localText.getText("TXT_KEY_EVENT_INFLUENZA_HIT_CITY", (loopCity.getNameKey(), ))
		CyInterface().addMessage(kTriggeredData.ePlayer, false, gc.getEVENT_MESSAGE_TIME(), szBuffer, "AS2D_PILLAGE", InterfaceMessageTypes.MESSAGE_TYPE_INFO, None, gc.getInfoTypeForString("COLOR_RED"), loopCity.getX(), loopCity.getY(), true, true)
				

def getHelpInfluenza2(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	
	szHelp = localText.getText("TXT_KEY_EVENT_INFLUENZA_HELP_2", (2, ))	

	return szHelp

######## WHALEOFATHING ###########

def canTriggerWhaleOfAThing(argsList):

	kTriggeredData = argsList[0]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	
	iWhale = CvUtil.findInfoTypeNum(gc.getBonusInfo,gc.getNumBonusInfos(),'BONUS_WHALE')
	iHappyBonuses = 0
	bWhale = false
	for i in range(gc.getNumBonusInfos()):
		bonus = gc.getBonusInfo(i)
		iNum = player.getNumAvailableBonuses(i)
		if iNum > 0 :
			if bonus.getHappiness() > 0:
				iHappyBonuses += 1
				if iHappyBonuses > 5:
					return false
			if i == iWhale:
				return false

	plot = gc.getMap().plot(kTriggeredData.iPlotX, kTriggeredData.iPlotY)
	if not plot.canHaveBonus(iWhale, false):
		return false
		
	return true


######## HIYOSILVER ###########

def canTriggerHiyoSilver(argsList):

	kTriggeredData = argsList[0]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	
	iSilver = CvUtil.findInfoTypeNum(gc.getBonusInfo,gc.getNumBonusInfos(),'BONUS_SILVER')
	iHappyBonuses = 0
	bSilver = false
	for i in range(gc.getNumBonusInfos()):
		bonus = gc.getBonusInfo(i)
		iNum = player.getNumAvailableBonuses(i)
		if iNum > 0 :
			if bonus.getHappiness() > 0:
				iHappyBonuses += 1
				if iHappyBonuses > 5:
					return false
			if i == iSilver:
				return false

	plot = gc.getMap().plot(kTriggeredData.iPlotX, kTriggeredData.iPlotY)
	if not plot.canHaveBonus(iSilver, false):
		return false
				
	return true

######## WININGMONKS ###########

def canTriggerWiningMonks(argsList):

	kTriggeredData = argsList[0]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	
	if player.getNumAvailableBonuses(CvUtil.findInfoTypeNum(gc.getBonusInfo,gc.getNumBonusInfos(),'BONUS_WINE')) > 0:
		return false
				
	return true


def doWiningMonks2(argsList):
#	Need this because wineries are not normally allowed unless there is already wine.
	iEvent = argsList[0]
	kTriggeredData = argsList[1]

	plot = gc.getMap().plot(kTriggeredData.iPlotX, kTriggeredData.iPlotY)
	
	if not plot.isNone():
		plot.setImprovementType(CvUtil.findInfoTypeNum(gc.getImprovementInfo,gc.getNumImprovementInfos(),'IMPROVEMENT_WINERY'))
	
	return 1

def getHelpWiningMonks2(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	
	iImp = CvUtil.findInfoTypeNum(gc.getImprovementInfo,gc.getNumImprovementInfos(),'IMPROVEMENT_WINERY')
	szHelp = localText.getText("TXT_KEY_EVENT_IMPROVEMENT_GROWTH", ( gc.getImprovementInfo(iImp).getTextKey(), ))

	return szHelp

######## EARTH DAY ###########

def getHelpEarthDay2(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	
	szHelp = localText.getText("TXT_KEY_EVENT_EARTHDAY_HELP_2", ())	

	return szHelp

def canApplyEarthDay2(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	
	player = gc.getPlayer(kTriggeredData.ePlayer)
	
	# edead: start
	# iCivic = CvUtil.findInfoTypeNum(gc.getCivicInfo,gc.getNumCivicInfos(),'CIVIC_ENVIRONMENTALISM')
	iCivic = con.iGuildsCivic
	# edead: end
	
	for iPlayer in range(gc.getMAX_CIV_PLAYERS()):			
		loopPlayer = gc.getPlayer(iPlayer)
		if loopPlayer.isAlive() and iPlayer != kTriggeredData.ePlayer and not loopPlayer.isHuman():
			loopTeam = gc.getTeam(loopPlayer.getTeam())
			if loopTeam.isHasMet(gc.getPlayer(kTriggeredData.ePlayer).getTeam()):
				tradeData = TradeData()
				tradeData.ItemType = TradeableItems.TRADE_CIVIC
				tradeData.iData = iCivic
				if loopPlayer.canTradeItem(kTriggeredData.ePlayer, tradeData, False):
					if (loopPlayer.getTradeDenial(kTriggeredData.ePlayer, tradeData) == DenialTypes.NO_DENIAL):
						return true
	return false
	
		
def applyEarthDay2(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	
	# edead: start
	# iCivic = CvUtil.findInfoTypeNum(gc.getCivicInfo,gc.getNumCivicInfos(),'CIVIC_ENVIRONMENTALISM')
	# iCivicOption = CvUtil.findInfoTypeNum(gc.getCivicOptionInfo,gc.getNumCivicOptionInfos(),'CIVICOPTION_ECONOMY')
	iCivic = con.iGuildsCivic
	iCivicOption = 3
	# edead: end
	
	
	listPlayers = []
	for iPlayer in range(gc.getMAX_CIV_PLAYERS()):			
		loopPlayer = gc.getPlayer(iPlayer)
		if loopPlayer.isAlive() and iPlayer != kTriggeredData.ePlayer and not loopPlayer.isHuman():
			loopTeam = gc.getTeam(loopPlayer.getTeam())
			if loopTeam.isHasMet(gc.getPlayer(kTriggeredData.ePlayer).getTeam()):
				tradeData = TradeData()
				tradeData.ItemType = TradeableItems.TRADE_CIVIC
				tradeData.iData = iCivic
				if loopPlayer.canTradeItem(kTriggeredData.ePlayer, tradeData, False):
					if (loopPlayer.getTradeDenial(kTriggeredData.ePlayer, tradeData) == DenialTypes.NO_DENIAL):
						listPlayers.append((-loopPlayer.AI_civicValue(iCivic), iPlayer))
						
	listPlayers.sort()	
	
	if len(listPlayers) > 3:
		listPlayers = listPlayers[:2]
	
	for (iValue, iPlayer) in listPlayers:
		gc.getPlayer(iPlayer).setCivics(iCivicOption, iCivic)

######## HEROIC_GESTURE ###########

def canTriggerHeroicGesture(argsList):
	kTriggeredData = argsList[0]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	destPlayer = gc.getPlayer(kTriggeredData.eOtherPlayer)

	if not gc.getTeam(destPlayer.getTeam()).canChangeWarPeace(player.getTeam()):
		return false
		
	if gc.getTeam(destPlayer.getTeam()).AI_getWarSuccess(player.getTeam()) <= 0:
		return false

	if gc.getTeam(player.getTeam()).AI_getWarSuccess(destPlayer.getTeam()) <= 0:
		return false
	
	return true

def doHeroicGesture2(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]

	destPlayer = gc.getPlayer(kTriggeredData.eOtherPlayer)
	player = gc.getPlayer(kTriggeredData.ePlayer)
	
	if destPlayer.isHuman():
		# this works only because it's a single-player only event
		popupInfo = CyPopupInfo()
		popupInfo.setButtonPopupType(ButtonPopupTypes.BUTTONPOPUP_PYTHON)
		popupInfo.setText(localText.getText("TXT_KEY_EVENT_HEROIC_GESTURE_OTHER_3", (player.getCivilizationAdjectiveKey(), )))
		popupInfo.setData1(kTriggeredData.eOtherPlayer)
		popupInfo.setData2(kTriggeredData.ePlayer)
		popupInfo.setPythonModule("CvRandomEventInterface")
		popupInfo.setOnClickedPythonCallback("heroicGesture2Callback")
		popupInfo.addPythonButton(localText.getText("TXT_KEY_POPUP_YES", ()), "")
		popupInfo.addPythonButton(localText.getText("TXT_KEY_POPUP_NO", ()), "")
		popupInfo.addPopup(kTriggeredData.eOtherPlayer)
	else:
		destPlayer.forcePeace(kTriggeredData.ePlayer)
		destPlayer.AI_changeAttitudeExtra(kTriggeredData.ePlayer, 1)
		player.AI_changeAttitudeExtra(kTriggeredData.eOtherPlayer, 1)

	return

def heroicGesture2Callback(argsList):
	iButton = argsList[0]
	iData1 = argsList[1]
	iData2 = argsList[2]
	iData3 = argsList[3]
	szText = argsList[4]
	bOption1 = argsList[5]
	bOption2 = argsList[6]
	
	if iButton == 0:
		destPlayer = gc.getPlayer(iData1)
		player = gc.getPlayer(iData2)
		destPlayer.forcePeace(iData2)
		destPlayer.AI_changeAttitudeExtra(iData2, 1)
		player.AI_changeAttitudeExtra(iData1, 1)		

	return 0
	
def getHelpHeroicGesture2(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	
	destPlayer = gc.getPlayer(kTriggeredData.eOtherPlayer)

	# Get help text
	szHelp = localText.getText("TXT_KEY_EVENT_ATTITUDE_GOOD", (1, destPlayer.getNameKey()));

	return szHelp

######## GREAT_MEDIATOR ###########

def canTriggerGreatMediator(argsList):
	kTriggeredData = argsList[0]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	destPlayer = gc.getPlayer(kTriggeredData.eOtherPlayer)
	
	# edead: start
	if kTriggeredData.ePlayer >= con.iNumPlayers or kTriggeredData.eOtherPlayer >= con.iNumPlayers:
		return false
	# edead: end
	
	if not gc.getTeam(player.getTeam()).canChangeWarPeace(destPlayer.getTeam()):
		return false
		
	if gc.getTeam(player.getTeam()).AI_getAtWarCounter(destPlayer.getTeam()) < 10:
		return false

	return true

def doGreatMediator2(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]

	destPlayer = gc.getPlayer(kTriggeredData.eOtherPlayer)
	player = gc.getPlayer(kTriggeredData.ePlayer)
	
	if destPlayer.isHuman():
		# this works only because it's a single-player only event
		popupInfo = CyPopupInfo()
		popupInfo.setButtonPopupType(ButtonPopupTypes.BUTTONPOPUP_PYTHON)
		popupInfo.setText(localText.getText("TXT_KEY_EVENT_GREAT_MEDIATOR_OTHER_3", (player.getCivilizationAdjectiveKey(), )))
		popupInfo.setData1(kTriggeredData.eOtherPlayer)
		popupInfo.setData2(kTriggeredData.ePlayer)
		popupInfo.setPythonModule("CvRandomEventInterface")
		popupInfo.setOnClickedPythonCallback("greatMediator2Callback")
		popupInfo.addPythonButton(localText.getText("TXT_KEY_POPUP_YES", ()), "")
		popupInfo.addPythonButton(localText.getText("TXT_KEY_POPUP_NO", ()), "")
		popupInfo.addPopup(kTriggeredData.eOtherPlayer)
	else:
		gc.getTeam(player.getTeam()).makePeace(destPlayer.getTeam())
		destPlayer.AI_changeAttitudeExtra(kTriggeredData.ePlayer, 1)
		player.AI_changeAttitudeExtra(kTriggeredData.eOtherPlayer, 1)

	return

def greatMediator2Callback(argsList):
	iButton = argsList[0]
	iData1 = argsList[1]
	iData2 = argsList[2]
	iData3 = argsList[3]
	szText = argsList[4]
	bOption1 = argsList[5]
	bOption2 = argsList[6]
	
	if iButton == 0:
		destPlayer = gc.getPlayer(iData1)
		player = gc.getPlayer(iData2)
		gc.getTeam(destPlayer.getTeam()).makePeace(player.getTeam())
		destPlayer.AI_changeAttitudeExtra(iData2, 1)
		player.AI_changeAttitudeExtra(iData1, 1)		

	return 0
	
def getHelpGreatMediator2(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	
	destPlayer = gc.getPlayer(kTriggeredData.eOtherPlayer)

	# Get help text
	szHelp = localText.getText("TXT_KEY_EVENT_ATTITUDE_GOOD", (1, destPlayer.getNameKey()));

	return szHelp

######## ANCIENT_TEXTS ###########

def doAncientTexts2(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]

	for iPlayer in range(gc.getMAX_CIV_PLAYERS()):			
		loopPlayer = gc.getPlayer(iPlayer)
		if loopPlayer.isAlive() and iPlayer != kTriggeredData.ePlayer:
			loopTeam = gc.getTeam(loopPlayer.getTeam())
			if loopTeam.isHasMet(gc.getPlayer(kTriggeredData.ePlayer).getTeam()):
				loopPlayer.AI_changeAttitudeExtra(kTriggeredData.ePlayer, 1)

	return

def getHelpAncientTexts2(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	
	szHelp = localText.getText("TXT_KEY_EVENT_SOLO_FLIGHT_HELP_1", (1, ))	

	return szHelp


######## IMPACT_CRATER ###########

def canTriggerImpactCrater(argsList):

	kTriggeredData = argsList[0]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	
	iUranium = CvUtil.findInfoTypeNum(gc.getBonusInfo,gc.getNumBonusInfos(),'BONUS_URANIUM')
	if player.getNumAvailableBonuses(iUranium) > 0:
		return false
	
	plot = gc.getMap().plot(kTriggeredData.iPlotX, kTriggeredData.iPlotY)
	if not plot.canHaveBonus(iUranium, false):
		return false
	
	return true

def doImpactCrater2(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]

	plot = gc.getMap().plot(kTriggeredData.iPlotX, kTriggeredData.iPlotY)
	
	if not plot.isNone():
		plot.setImprovementType(CvUtil.findInfoTypeNum(gc.getImprovementInfo,gc.getNumImprovementInfos(),'IMPROVEMENT_MINE'))
	
	return 1

def getHelpImpactCrater2(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	
	iMine = CvUtil.findInfoTypeNum(gc.getImprovementInfo,gc.getNumImprovementInfos(),'IMPROVEMENT_MINE')
	szHelp = localText.getText("TXT_KEY_EVENT_IMPROVEMENT_GROWTH", ( gc.getImprovementInfo(iMine).getTextKey(), ))

	return szHelp

######## SECURITY_TAX ###########

def canTriggerSecurityTax(argsList):

	kTriggeredData = argsList[0]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	
	iWalls = CvUtil.findInfoTypeNum(gc.getBuildingClassInfo, gc.getNumBuildingClassInfos(), 'BUILDINGCLASS_WALLS')
	if player.getNumCities() > player.getBuildingClassCount(iWalls):
		return false
	
	return true


######## LITERACY ###########

def canTriggerLiteracy(argsList):

	kTriggeredData = argsList[0]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	
	iLibrary = CvUtil.findInfoTypeNum(gc.getBuildingClassInfo, gc.getNumBuildingClassInfos(), 'BUILDINGCLASS_LIBRARY')
	if player.getNumCities() > player.getBuildingClassCount(iLibrary):
		return false
	
	return true

######## TEA ###########

def canTriggerTea(argsList):

	kTriggeredData = argsList[0]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	
	#if player.isCivic(CvUtil.findInfoTypeNum(gc.getCivicInfo,gc.getNumCivicInfos(),'CIVIC_MERCANTILISM')):
	#	return false

	bCanTrade = false		
	for iLoopPlayer in range(gc.getMAX_CIV_PLAYERS()):
		if player.canHaveTradeRoutesWith(iLoopPlayer):
			bCanTrade = true	
			break
			
	if not bCanTrade:
		return false
	
	return true

######## HORSE WHISPERING ###########

def canTriggerHorseWhispering(argsList):
	kTriggeredData = argsList[0]

	if gc.getGame().isOption(GameOptionTypes.GAMEOPTION_ONE_CITY_CHALLENGE) and gc.getPlayer(kTriggeredData.ePlayer).isHuman():
		return false
	
	return true

def getHelpHorseWhispering1(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	
	map = gc.getMap()
	
	#iNumStables = gc.getWorldInfo(map.getWorldSize()).getDefaultPlayers()
	iNumStables = gc.getWorldInfo(map.getWorldSize()).getDefaultPlayers()/2 # edead
	szHelp = localText.getText("TXT_KEY_EVENT_HORSE_WHISPERING_HELP", (iNumStables, ))

	return szHelp

def canTriggerHorseWhisperingDone(argsList):
	kTriggeredData = argsList[0]
	trigger = gc.getEventTriggerInfo(kTriggeredData.eTrigger)
	player = gc.getPlayer(kTriggeredData.ePlayer)
	
	iStable = CvUtil.findInfoTypeNum(gc.getBuildingClassInfo, gc.getNumBuildingClassInfos(), 'BUILDINGCLASS_STABLE')
	#if gc.getWorldInfo(gc.getMap().getWorldSize()).getDefaultPlayers() > player.getBuildingClassCount(iStable):
	if (gc.getWorldInfo(gc.getMap().getWorldSize()).getDefaultPlayers()/2) > player.getBuildingClassCount(iStable): # edead
		return false
	
	return true

def getHelpHorseWhisperingDone1(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer) # edead
	
	# edead: start mod-specific data
	iUnitClassType = CvUtil.findInfoTypeNum(gc.getUnitClassInfo, gc.getNumUnitClassInfos(), 'UNITCLASS_LANCER')
	iUnitType = gc.getCivilizationInfo(player.getCivilizationType()).getCivilizationUnits(iUnitClassType)
	# edead: end
	
	map = gc.getMap()
	
	#iNumUnits = gc.getWorldInfo(map.getWorldSize()).getDefaultPlayers()
	iNumUnits = gc.getWorldInfo(map.getWorldSize()).getDefaultPlayers()/2 # edead
	#szHelp = localText.getText("TXT_KEY_EVENT_HORSE_WHISPERING_DONE_HELP_1", (iNumUnits, ))
	szHelp = localText.getText("TXT_KEY_EVENT_HORSE_WHISPERING_DONE_HELP_1", (iNumUnits, gc.getUnitInfo(iUnitType).getDescription())) # edead
	

	return szHelp

def applyHorseWhisperingDone1(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)

	map = gc.getMap()
	plot = map.plot(kTriggeredData.iPlotX, kTriggeredData.iPlotY)
	#iNumUnits = gc.getWorldInfo(map.getWorldSize()).getDefaultPlayers()
	iNumUnits = gc.getWorldInfo(map.getWorldSize()).getDefaultPlayers()/2 # edead
	# edead: start mod-specific data
	#iUnitClassType = CvUtil.findInfoTypeNum(gc.getUnitClassInfo, gc.getNumUnitClassInfos(), 'UNITCLASS_HORSE_ARCHER')
	iUnitClassType = CvUtil.findInfoTypeNum(gc.getUnitClassInfo, gc.getNumUnitClassInfos(), 'UNITCLASS_LANCER')
	# edead: end
	iUnitType = gc.getCivilizationInfo(player.getCivilizationType()).getCivilizationUnits(iUnitClassType)
	
	if iUnitType != -1:
		for i in range(iNumUnits):
			player.initUnit(iUnitType, plot.getX(), plot.getY(), UnitAITypes.UNITAI_ATTACK, DirectionTypes.DIRECTION_SOUTH)

######## HARBORMASTER ###########

def getHelpHarbormaster1(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
		
	#iHarborsRequired = gc.getWorldInfo(gc.getMap().getWorldSize()).getDefaultPlayers()
	iHarborsRequired = gc.getWorldInfo(gc.getMap().getWorldSize()).getDefaultPlayers()/2 # edead
	iCaravelsRequired = iHarborsRequired / 2 + 1

	szHelp = localText.getText("TXT_KEY_EVENT_HARBORMASTER_HELP", (iHarborsRequired, iCaravelsRequired))

	return szHelp


def canTriggerHarbormaster(argsList):
	kTriggeredData = argsList[0]
	trigger = gc.getEventTriggerInfo(kTriggeredData.eTrigger)
	player = gc.getPlayer(kTriggeredData.ePlayer)

	# edead: start
	# if gc.getGame().isOption(GameOptionTypes.GAMEOPTION_ONE_CITY_CHALLENGE) and gc.getPlayer(kTriggeredData.ePlayer).isHuman():
		# return false

	# map = gc.getMap()

	# iNumWater = 0
	
	# for i in range(map.numPlots()):
		# plot = map.plotByIndex(i)
		
		# if plot.isWater():
			# iNumWater += 1
			
		# if 100 * iNumWater >= 40 * map.numPlots():
			# return true
		
	# return false
	return true
	# edead: end

def canTriggerHarbormasterDone(argsList):
	kTriggeredData = argsList[0]
	trigger = gc.getEventTriggerInfo(kTriggeredData.eTrigger)
	player = gc.getPlayer(kTriggeredData.ePlayer)
	
	iHarbor = CvUtil.findInfoTypeNum(gc.getBuildingClassInfo, gc.getNumBuildingClassInfos(), 'BUILDINGCLASS_HARBOR')
	#iHarborsRequired = gc.getWorldInfo(gc.getMap().getWorldSize()).getDefaultPlayers()
	iHarborsRequired = gc.getWorldInfo(gc.getMap().getWorldSize()).getDefaultPlayers()/2 # edead
	if iHarborsRequired > player.getBuildingClassCount(iHarbor):
		return false

	# edead: start
	#iCaravel = CvUtil.findInfoTypeNum(gc.getUnitClassInfo, gc.getNumUnitClassInfos(), 'UNITCLASS_CARAVEL')
	#iCaravelsRequired = iHarborsRequired / 2 + 1
	#if iCaravelsRequired > player.getUnitClassCount(iCaravel):
	#	return false
	iRoundship = CvUtil.findInfoTypeNum(gc.getUnitClassInfo, gc.getNumUnitClassInfos(), 'UNITCLASS_ROUNDSHIP')
	iBaghlah = CvUtil.findInfoTypeNum(gc.getUnitClassInfo, gc.getNumUnitClassInfos(), 'UNITCLASS_BAGHLAH')
	iShipsRequired = iHarborsRequired / 2 + 1
	if iShipsRequired > player.getUnitClassCount(iRoundship) + player.getUnitClassCount(iBaghlah):
		return false
	# edead: end
	
	return true
	
######## CLASSIC LITERATURE ###########

def canTriggerClassicLiterature(argsList):
	kTriggeredData = argsList[0]
	
	if gc.getGame().isOption(GameOptionTypes.GAMEOPTION_ONE_CITY_CHALLENGE) and gc.getPlayer(kTriggeredData.ePlayer).isHuman():
		return false

	return true

def getHelpClassicLiterature1(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
		
	iLibrariesRequired = gc.getWorldInfo(gc.getMap().getWorldSize()).getDefaultPlayers()

	szHelp = localText.getText("TXT_KEY_EVENT_CLASSIC_LITERATURE_HELP_1", (iLibrariesRequired, ))

	return szHelp


def canTriggerClassicLiteratureDone(argsList):
	kTriggeredData = argsList[0]
	trigger = gc.getEventTriggerInfo(kTriggeredData.eTrigger)
	player = gc.getPlayer(kTriggeredData.ePlayer)
	
	iLibrary = CvUtil.findInfoTypeNum(gc.getBuildingClassInfo, gc.getNumBuildingClassInfos(), 'BUILDINGCLASS_LIBRARY')
	iBuildingsRequired = gc.getWorldInfo(gc.getMap().getWorldSize()).getDefaultPlayers()
	if iBuildingsRequired > player.getBuildingClassCount(iLibrary):
		return false
	
	return true

def getHelpClassicLiteratureDone2(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	
	szHelp = localText.getText("TXT_KEY_EVENT_CLASSIC_LITERATURE_DONE_HELP_2", ( ))

	return szHelp

def canApplyClassicLiteratureDone2(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	
	iEraAncient = CvUtil.findInfoTypeNum(gc.getEraInfo, gc.getNumEraInfos(), 'ERA_ANCIENT')

	for iTech in range(gc.getNumTechInfos()):
		if gc.getTechInfo(iTech).getEra() == iEraAncient and player.canResearch(iTech, false):
			return true
			
	return false
		
def applyClassicLiteratureDone2(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)

	iEraAncient = CvUtil.findInfoTypeNum(gc.getEraInfo, gc.getNumEraInfos(), 'ERA_ANCIENT')

	listTechs = []
	for iTech in range(gc.getNumTechInfos()):
		if gc.getTechInfo(iTech).getEra() == iEraAncient and player.canResearch(iTech, false):
			listTechs.append(iTech)
			
	if len(listTechs) > 0:
		iTech = listTechs[gc.getGame().getSorenRandNum(len(listTechs), "Classic Literature Event Tech selection")]
		gc.getTeam(player.getTeam()).setHasTech(iTech, true, kTriggeredData.ePlayer, true, true)
		
def getHelpClassicLiteratureDone3(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)

	iSpecialist = CvUtil.findInfoTypeNum(gc.getSpecialistInfo, gc.getNumSpecialistInfos(), 'SPECIALIST_SCIENTIST', )
	iGreatLibrary = CvUtil.findInfoTypeNum(gc.getBuildingInfo, gc.getNumBuildingInfos(), 'BUILDING_GREAT_LIBRARY')

	szCityName = u""
	(loopCity, iter) = player.firstCity(false)
	while(loopCity):
		if (loopCity.isHasBuilding(iGreatLibrary)):
			szCityName = loopCity.getNameKey()
			break
				
		(loopCity, iter) = player.nextCity(iter, false)
	
	szHelp = localText.getText("TXT_KEY_EVENT_FREE_SPECIALIST", (1, gc.getSpecialistInfo(iSpecialist).getTextKey(), szCityName))

	return szHelp

def canApplyClassicLiteratureDone3(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	
	iGreatLibrary = CvUtil.findInfoTypeNum(gc.getBuildingInfo, gc.getNumBuildingInfos(), 'BUILDING_GREAT_LIBRARY')

	(loopCity, iter) = player.firstCity(false)
	while(loopCity):
		if (loopCity.isHasBuilding(iGreatLibrary)):
			return true
				
		(loopCity, iter) = player.nextCity(iter, false)
			
	return false
		
def applyClassicLiteratureDone3(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)

	iSpecialist = CvUtil.findInfoTypeNum(gc.getSpecialistInfo, gc.getNumSpecialistInfos(), 'SPECIALIST_SCIENTIST', )
	iGreatLibrary = CvUtil.findInfoTypeNum(gc.getBuildingInfo, gc.getNumBuildingInfos(), 'BUILDING_GREAT_LIBRARY')

	(loopCity, iter) = player.firstCity(false)
	while(loopCity):
		if (loopCity.isHasBuilding(iGreatLibrary)):
			loopCity.changeFreeSpecialistCount(iSpecialist, 1)
			return
				
		(loopCity, iter) = player.nextCity(iter, false)

######## MASTER BLACKSMITH ###########

def canTriggerMasterBlacksmith(argsList):
	kTriggeredData = argsList[0]
	
	if gc.getGame().isOption(GameOptionTypes.GAMEOPTION_ONE_CITY_CHALLENGE) and gc.getPlayer(kTriggeredData.ePlayer).isHuman():
		return false

	return true

def getHelpMasterBlacksmith1(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)
		
	#iRequired = gc.getWorldInfo(gc.getMap().getWorldSize()).getDefaultPlayers()
	iRequired = gc.getWorldInfo(gc.getMap().getWorldSize()).getDefaultPlayers()/2 # edead
	
	szHelp = localText.getText("TXT_KEY_EVENT_MASTER_BLACKSMITH_HELP_1", (iRequired, player.getCity(kTriggeredData.iCityId).getNameKey()))

	return szHelp

def expireMasterBlacksmith1(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	city = player.getCity(kTriggeredData.iCityId)	
	if city == None or city.getOwner() != kTriggeredData.ePlayer:
		return true
				
	return false

def canTriggerMasterBlacksmithDone(argsList):
	kTriggeredData = argsList[0]
	trigger = gc.getEventTriggerInfo(kTriggeredData.eTrigger)
	player = gc.getPlayer(kTriggeredData.ePlayer)
		
	iForge = CvUtil.findInfoTypeNum(gc.getBuildingClassInfo, gc.getNumBuildingClassInfos(), 'BUILDINGCLASS_FORGE')
	#iBuildingsRequired = gc.getWorldInfo(gc.getMap().getWorldSize()).getDefaultPlayers()
	iBuildingsRequired = gc.getWorldInfo(gc.getMap().getWorldSize()).getDefaultPlayers()/2 # edead
	if iBuildingsRequired > player.getBuildingClassCount(iForge):
		return false

	kOrigTriggeredData = player.getEventOccured(trigger.getPrereqEvent(0))

	city = player.getCity(kOrigTriggeredData.iCityId)	
	if city == None or city.getOwner() != kTriggeredData.ePlayer:
		return false

	kActualTriggeredDataObject = player.getEventTriggered(kTriggeredData.iId)
	kActualTriggeredDataObject.iCityId = kOrigTriggeredData.iCityId
		
	return true

def canApplyMasterBlacksmithDone1(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	
	iBonus = CvUtil.findInfoTypeNum(gc.getBonusInfo,gc.getNumBonusInfos(),'BONUS_COPPER')
	city = player.getCity(kTriggeredData.iCityId)
	
	if city == None:
		return false
	
	map = gc.getMap()
	iBestValue = map.getGridWidth() + map.getGridHeight()
	bestPlot = None
	for i in range(map.numPlots()):
		plot = map.plotByIndex(i)
		if (plot.getOwner() == kTriggeredData.ePlayer and plot.canHaveBonus(iBonus, false)):
			iValue = plotDistance(city.getX(), city.getY(), plot.getX(), plot.getY())
			if iValue < iBestValue:
				iBestValue = iValue
				bestPlot = plot
				
	if bestPlot == None:
		return false

	kActualTriggeredDataObject = player.getEventTriggered(kTriggeredData.iId)
	kActualTriggeredDataObject.iPlotX = bestPlot.getX()
	kActualTriggeredDataObject.iPlotY = bestPlot.getY()
		
	return true

def applyMasterBlacksmithDone1(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	
	plot = gc.getMap().plot(kTriggeredData.iPlotX, kTriggeredData.iPlotY)
	city = player.getCity(kTriggeredData.iCityId)
	
	iBonus = CvUtil.findInfoTypeNum(gc.getBonusInfo,gc.getNumBonusInfos(),'BONUS_COPPER')
	plot.setBonusType(iBonus)

	szBuffer = localText.getText("TXT_KEY_MISC_DISCOVERED_NEW_RESOURCE", (gc.getBonusInfo(iBonus).getTextKey(), city.getNameKey()))
	CyInterface().addMessage(kTriggeredData.ePlayer, false, gc.getEVENT_MESSAGE_TIME(), szBuffer, "AS2D_DISCOVERBONUS", InterfaceMessageTypes.MESSAGE_TYPE_MINOR_EVENT, gc.getBonusInfo(iBonus).getButton(), gc.getInfoTypeForString("COLOR_WHITE"), plot.getX(), plot.getY(), true, true)

def canApplyMasterBlacksmithDone3(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	
	if player.getStateReligion() == -1:		
		return false
		
	return true

######## THE BEST DEFENSE ###########

def canTriggerBestDefense(argsList):
	kTriggeredData = argsList[0]
	
	if gc.getGame().isOption(GameOptionTypes.GAMEOPTION_ONE_CITY_CHALLENGE) and gc.getPlayer(kTriggeredData.ePlayer).isHuman():
		return false

	return true

def getHelpBestDefense1(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)
		
	#iRequired = gc.getWorldInfo(gc.getMap().getWorldSize()).getDefaultPlayers()
	iRequired = gc.getWorldInfo(gc.getMap().getWorldSize()).getDefaultPlayers()/2 # edead
	
	szHelp = localText.getText("TXT_KEY_EVENT_BEST_DEFENSE_HELP_1", (iRequired, ))

	return szHelp

def canTriggerBestDefenseDone(argsList):
	kTriggeredData = argsList[0]
	trigger = gc.getEventTriggerInfo(kTriggeredData.eTrigger)
	player = gc.getPlayer(kTriggeredData.ePlayer)
		
	iCastle = CvUtil.findInfoTypeNum(gc.getBuildingClassInfo, gc.getNumBuildingClassInfos(), 'BUILDINGCLASS_CASTLE')
	#iBuildingsRequired = gc.getWorldInfo(gc.getMap().getWorldSize()).getDefaultPlayers()
	iBuildingsRequired = gc.getWorldInfo(gc.getMap().getWorldSize()).getDefaultPlayers()/2 # edead
	if iBuildingsRequired > player.getBuildingClassCount(iCastle):
		return false
		
	return true

def getHelpBestDefenseDone2(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	
	szHelp = localText.getText("TXT_KEY_EVENT_BEST_DEFENSE_DONE_HELP_2", (3, ))	

	return szHelp

def applyBestDefenseDone2(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	
	for iPlayer in range(gc.getMAX_CIV_PLAYERS()):			
		loopPlayer = gc.getPlayer(iPlayer)
		if loopPlayer.isAlive() and iPlayer != kTriggeredData.ePlayer:
			loopTeam = gc.getTeam(loopPlayer.getTeam())
			if loopTeam.isHasMet(gc.getPlayer(kTriggeredData.ePlayer).getTeam()):
				loopPlayer.AI_changeAttitudeExtra(kTriggeredData.ePlayer, 3)
						

def canApplyBestDefenseDone3(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	
	# edead: start
	# iGreatWall = CvUtil.findInfoTypeNum(gc.getBuildingInfo, gc.getNumBuildingInfos(), 'BUILDING_GREAT_WALL') 
	iQalehDokhtar = CvUtil.findInfoTypeNum(gc.getBuildingInfo, gc.getNumBuildingInfos(), 'BUILDING_QALEH_DOKHTAR')
	# edead: end

	(loopCity, iter) = player.firstCity(false)
	while(loopCity):
		# edead: start
		# if (loopCity.isHasBuilding(iGreatWall)): 
		if loopCity.isHasBuilding(iQalehDokhtar):
		# edead: end
			return true
				
		(loopCity, iter) = player.nextCity(iter, false)
			
	return false

######## NATIONAL SPORTS LEAGUE ###########

def canTriggerSportsLeague(argsList):
	kTriggeredData = argsList[0]
	
	if gc.getGame().isOption(GameOptionTypes.GAMEOPTION_ONE_CITY_CHALLENGE) and gc.getPlayer(kTriggeredData.ePlayer).isHuman():
		return false

	return true
def getHelpSportsLeague1(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)
		
	iRequired = gc.getWorldInfo(gc.getMap().getWorldSize()).getDefaultPlayers()
	iBuilding = CvUtil.findInfoTypeNum(gc.getBuildingInfo, gc.getNumBuildingInfos(), 'BUILDING_STATUE_OF_ZEUS')
	
	szHelp = localText.getText("TXT_KEY_EVENT_SPORTS_LEAGUE_HELP_1", (iRequired, gc.getBuildingInfo(iBuilding).getTextKey()))

	return szHelp

def canTriggerSportsLeagueDone(argsList):
	kTriggeredData = argsList[0]
	trigger = gc.getEventTriggerInfo(kTriggeredData.eTrigger)
	player = gc.getPlayer(kTriggeredData.ePlayer)
		
	iCastle = CvUtil.findInfoTypeNum(gc.getBuildingClassInfo, gc.getNumBuildingClassInfos(), 'BUILDINGCLASS_COLOSSEUM')
	iBuildingsRequired = gc.getWorldInfo(gc.getMap().getWorldSize()).getDefaultPlayers()
	if iBuildingsRequired > player.getBuildingClassCount(iCastle):
		return false
		
	return true

def canApplySportsLeagueDone3(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	
	iZeus = CvUtil.findInfoTypeNum(gc.getBuildingInfo, gc.getNumBuildingInfos(), 'BUILDING_STATUE_OF_ZEUS')

	(loopCity, iter) = player.firstCity(false)
	while(loopCity):
		if (loopCity.isHasBuilding(iZeus)):
			return true
				
		(loopCity, iter) = player.nextCity(iter, false)
			
	return false

######## CRUSADE ###########

def canTriggerCrusade(argsList):
	kTriggeredData = argsList[0]
	trigger = gc.getEventTriggerInfo(kTriggeredData.eTrigger)
	player = gc.getPlayer(kTriggeredData.ePlayer)
	otherPlayer = gc.getPlayer(kTriggeredData.eOtherPlayer)
	holyCity = gc.getGame().getHolyCity(kTriggeredData.eReligion)

	if gc.getGame().isOption(GameOptionTypes.GAMEOPTION_ONE_CITY_CHALLENGE) and gc.getPlayer(kTriggeredData.ePlayer).isHuman():
		return false

	if holyCity.getOwner() != kTriggeredData.eOtherPlayer:
		return false
		
	kActualTriggeredDataObject = player.getEventTriggered(kTriggeredData.iId)
	kActualTriggeredDataObject.iOtherPlayerCityId = holyCity.getID()	
			
	return true

def getHelpCrusade1(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)

	holyCity = gc.getGame().getHolyCity(kTriggeredData.eReligion)
	
	szHelp = localText.getText("TXT_KEY_EVENT_CRUSADE_HELP_1", (holyCity.getNameKey(), ))

	return szHelp

def expireCrusade1(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	otherPlayer = gc.getPlayer(kTriggeredData.eOtherPlayer)
	holyCity = gc.getGame().getHolyCity(kTriggeredData.eReligion)

	if holyCity.getOwner() == kTriggeredData.ePlayer:
		return false

	if player.getStateReligion() != kTriggeredData.eReligion:
		return true

	if holyCity.getOwner() != kTriggeredData.eOtherPlayer:
		return true

	if not gc.getTeam(player.getTeam()).isAtWar(otherPlayer.getTeam()):
		return true	
					
	return false

def canTriggerCrusadeDone(argsList):
	kTriggeredData = argsList[0]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	trigger = gc.getEventTriggerInfo(kTriggeredData.eTrigger)

	kOrigTriggeredData = player.getEventOccured(trigger.getPrereqEvent(0))
	holyCity = gc.getGame().getHolyCity(kOrigTriggeredData.eReligion)

	if holyCity.getOwner() != kTriggeredData.ePlayer:
		return false
					
	kActualTriggeredDataObject = player.getEventTriggered(kTriggeredData.iId)
	kActualTriggeredDataObject.iCityId = holyCity.getID()
	kActualTriggeredDataObject.eOtherPlayer = kOrigTriggeredData.eOtherPlayer
	kActualTriggeredDataObject.eReligion = kOrigTriggeredData.eReligion
	
	for iBuilding in range(gc.getNumBuildingInfos()):
		if gc.getBuildingInfo(iBuilding).getHolyCity() == kOrigTriggeredData.eReligion:
			kActualTriggeredDataObject.eBuilding = BuildingTypes(iBuilding)
			break	
			
	return true

def getHelpCrusadeDone1(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	
	holyCity = gc.getGame().getHolyCity(kTriggeredData.eReligion)
	szUnit = gc.getUnitInfo(holyCity.getConscriptUnit()).getTextKey()
	iNumUnits = gc.getWorldInfo(gc.getMap().getWorldSize()).getDefaultPlayers() / 2 + 1
	szHelp = localText.getText("TXT_KEY_EVENT_CRUSADE_DONE_HELP_1", (iNumUnits, szUnit, holyCity.getNameKey()))	

	return szHelp

def canApplyCrusadeDone1(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	
	holyCity = gc.getGame().getHolyCity(kTriggeredData.eReligion)
	if -1 == holyCity.getConscriptUnit():
		return false
	
	return true

def applyCrusadeDone1(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	
	holyCity = gc.getGame().getHolyCity(kTriggeredData.eReligion)						
	iUnitType = holyCity.getConscriptUnit()
	iNumUnits = gc.getWorldInfo(gc.getMap().getWorldSize()).getDefaultPlayers() / 2 + 1
	
	if iUnitType != -1:
		for i in range(iNumUnits):
			player.initUnit(iUnitType, holyCity.getX(), holyCity.getY(), UnitAITypes.UNITAI_CITY_DEFENSE, DirectionTypes.DIRECTION_SOUTH)

def getHelpCrusadeDone2(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	
	holyCity = gc.getGame().getHolyCity(kTriggeredData.eReligion)
	
	szHelp = localText.getText("TXT_KEY_EVENT_CRUSADE_DONE_HELP_2", (gc.getBuildingInfo(kTriggeredData.eBuilding).getTextKey(), holyCity.getNameKey()))	

	return szHelp

def canApplyCrusadeDone2(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	
	holyCity = gc.getGame().getHolyCity(kTriggeredData.eReligion)
	
	if -1 == kTriggeredData.eBuilding or holyCity.isHasBuilding(kTriggeredData.eBuilding):
		return false			
	
	return true

def applyCrusadeDone2(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	
	holyCity = gc.getGame().getHolyCity(kTriggeredData.eReligion)
	holyCity.setNumRealBuilding(kTriggeredData.eBuilding, 1)
						
	if (not gc.getGame().isNetworkMultiPlayer() and kTriggeredData.ePlayer == gc.getGame().getActivePlayer()):
		popupInfo = CyPopupInfo()
		popupInfo.setButtonPopupType(ButtonPopupTypes.BUTTONPOPUP_PYTHON_SCREEN)
		popupInfo.setData1(kTriggeredData.eBuilding)
		popupInfo.setData2(holyCity.getID())
		popupInfo.setData3(0)
		popupInfo.setText(u"showWonderMovie")
		popupInfo.addPopup(kTriggeredData.ePlayer)

def getHelpCrusadeDone3(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	
	iNumCities = gc.getWorldInfo(gc.getMap().getWorldSize()).getDefaultPlayers()
	holyCity = gc.getGame().getHolyCity(kTriggeredData.eReligion)
	
	szHelp = localText.getText("TXT_KEY_EVENT_CRUSADE_DONE_HELP_3", (gc.getReligionInfo(kTriggeredData.eReligion).getTextKey(), iNumCities))	

	return szHelp

def canApplyCrusadeDone3(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	
	iNumCities = gc.getWorldInfo(gc.getMap().getWorldSize()).getDefaultPlayers()

	if gc.getGame().getNumCities() == gc.getGame().countReligionLevels(kTriggeredData.eReligion):
		return false
		
	return true

def applyCrusadeDone3(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	holyCity = gc.getGame().getHolyCity(kTriggeredData.eReligion)

	listCities = []	
	for iPlayer in range(gc.getMAX_CIV_PLAYERS()):			
		loopPlayer = gc.getPlayer(iPlayer)
		if loopPlayer.isAlive():			
			(loopCity, iter) = loopPlayer.firstCity(false)

			while(loopCity):
				if (not loopCity.isHasReligion(kTriggeredData.eReligion)):
					iDistance = plotDistance(holyCity.getX(), holyCity.getY(), loopCity.getX(), loopCity.getY())
					listCities.append((iDistance, loopCity))
						
				(loopCity, iter) = loopPlayer.nextCity(iter, false)
	
	listCities.sort()
	
	iNumCities = min(gc.getWorldInfo(gc.getMap().getWorldSize()).getDefaultPlayers(), len(listCities))
	
	for i in range(iNumCities):
		iDistance, loopCity = listCities[i]
		loopCity.setHasReligion(kTriggeredData.eReligion, true, true, true)	

######## ESTEEMEED_PLAYWRIGHT ###########

def canTriggerEsteemedPlaywright(argsList):
	kTriggeredData = argsList[0]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	
	# If source civ is operating this Civic, disallow the event to trigger.
	#if player.isCivic(CvUtil.findInfoTypeNum(gc.getCivicInfo,gc.getNumCivicInfos(),'CIVIC_SLAVERY')):
	#	return false

	return true


######## SECRET_KNOWLEDGE ###########
	
def getHelpSecretKnowledge2(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)

	szHelp = localText.getText("TXT_KEY_EVENT_YIELD_CHANGE_BUILDING", (gc.getBuildingInfo(kTriggeredData.eBuilding).getTextKey(), u"+4[ICON_CULTURE]"))	

	return szHelp

def applySecretKnowledge2(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)

	city = player.getCity(kTriggeredData.iCityId)
	city.setBuildingCommerceChange(gc.getBuildingInfo(kTriggeredData.eBuilding).getBuildingClassType(), CommerceTypes.COMMERCE_CULTURE, 4)

######## HIGH_WARLORD ###########

def canTriggerHighWarlord(argsList):
	kTriggeredData = argsList[0]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	
	# If source civ is operating this Civic, disallow the event to trigger.
	# edead: start comment
	# if player.isCivic(CvUtil.findInfoTypeNum(gc.getCivicInfo,gc.getNumCivicInfos(),'CIVIC_PATRONAGE')):
		# return false
	# edead: end

	return true


######## EXPERIENCED_CAPTAIN ###########

def canTriggerExperiencedCaptain(argsList):
	kTriggeredData = argsList[0]
	
	player = gc.getPlayer(kTriggeredData.ePlayer)
	unit = player.getUnit(kTriggeredData.iUnitId)
	
	if unit.isNone():
		return false
		
	if unit.getExperience() < 7:
		return false

	return true

######## PARTISANS ###########

def getNumPartisanUnits(plot, iPlayer):
	for i in range(gc.getNumCultureLevelInfos()):
		iI = gc.getNumCultureLevelInfos() - i - 1
		if plot.getCulture(iPlayer) >= gc.getGame().getCultureThreshold(iI):
			return iI
	return 0

def getHelpPartisans1(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	capital = player.getCapitalCity()
	plot = gc.getMap().plot(kTriggeredData.iPlotX, kTriggeredData.iPlotY)
	
	if None != capital and not capital.isNone():
		iNumUnits = getNumPartisanUnits(plot, kTriggeredData.ePlayer)
		szUnit = gc.getUnitInfo(capital.getConscriptUnit()).getTextKey()
		
		szHelp = localText.getText("TXT_KEY_EVENT_PARTISANS_HELP_1", (iNumUnits, szUnit))	

	return szHelp

def canApplyPartisans1(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	plot = gc.getMap().plot(kTriggeredData.iPlotX, kTriggeredData.iPlotY)

	if getNumPartisanUnits(plot, kTriggeredData.ePlayer) <= 0:
		return false

	for i in range(3):
		for j in range(3):
			loopPlot = gc.getMap().plot(kTriggeredData.iPlotX + i - 1, kTriggeredData.iPlotY + j - 1)
			if None != loopPlot and not loopPlot.isNone():
				if not (loopPlot.isVisibleEnemyUnit(kTriggeredData.ePlayer) or loopPlot.isWater() or loopPlot.isImpassable() or loopPlot.isCity()):
					return true
	return false
	

def applyPartisans1(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)	
	capital = player.getCapitalCity()
	plot = gc.getMap().plot(kTriggeredData.iPlotX, kTriggeredData.iPlotY)
	
	if None != capital and not capital.isNone():
		iNumUnits = getNumPartisanUnits(plot, kTriggeredData.ePlayer)

		listPlots = []
		for i in range(3):
			for j in range(3):
				loopPlot = gc.getMap().plot(kTriggeredData.iPlotX + i - 1, kTriggeredData.iPlotY + j - 1)
				if None != loopPlot and not loopPlot.isNone() and (i != 1 or j != 1):
					if not (loopPlot.isVisibleEnemyUnit(kTriggeredData.ePlayer) or loopPlot.isWater() or loopPlot.isImpassable()):
						listPlots.append(loopPlot)
		
		if len(listPlots) > 0:
			for i in range(iNumUnits):
				iPlot = gc.getGame().getSorenRandNum(len(listPlots), "Partisan event placement")
				player.initUnit(capital.getConscriptUnit(), listPlots[iPlot].getX(), listPlots[iPlot].getY(), UnitAITypes.UNITAI_ATTACK, DirectionTypes.DIRECTION_SOUTH)

def getHelpPartisans2(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	capital = player.getCapitalCity()
	plot = gc.getMap().plot(kTriggeredData.iPlotX, kTriggeredData.iPlotY)
	
	if None != capital and not capital.isNone():
		iNumUnits = max(1, getNumPartisanUnits(plot, kTriggeredData.ePlayer) / 2)
		szUnit = gc.getUnitInfo(capital.getConscriptUnit()).getTextKey()
		
		szHelp = localText.getText("TXT_KEY_EVENT_PARTISANS_HELP_2", (iNumUnits, szUnit, capital.getNameKey()))	

	return szHelp

def canApplyPartisans2(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	plot = gc.getMap().plot(kTriggeredData.iPlotX, kTriggeredData.iPlotY)
	
	return (max(1, getNumPartisanUnits(plot, kTriggeredData.ePlayer) / 2) > 0)
	
def applyPartisans2(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)	
	capital = player.getCapitalCity()
	plot = gc.getMap().plot(kTriggeredData.iPlotX, kTriggeredData.iPlotY)

	if None != capital and not capital.isNone():
		iNumUnits = max(1, getNumPartisanUnits(plot, kTriggeredData.ePlayer) / 2)
		for i in range(iNumUnits):
			player.initUnit(capital.getConscriptUnit(), capital.getX(), capital.getY(), UnitAITypes.UNITAI_ATTACK, DirectionTypes.DIRECTION_SOUTH)

######## GREED ###########

def canTriggerGreed(argsList):
	kTriggeredData = argsList[0]
	trigger = gc.getEventTriggerInfo(kTriggeredData.eTrigger)
	player = gc.getPlayer(kTriggeredData.ePlayer)
	otherPlayer = gc.getPlayer(kTriggeredData.eOtherPlayer)
	
	if not gc.getTeam(player.getTeam()).canChangeWarPeace(otherPlayer.getTeam()):
		return false

	listBonuses = []
	# comment by edead
	# iOil = CvUtil.findInfoTypeNum(gc.getBonusInfo,gc.getNumBonusInfos(),'BONUS_OIL')
	# if 0 == player.getNumAvailableBonuses(iOil):
		# listBonuses.append(iOil)
	iIron = CvUtil.findInfoTypeNum(gc.getBonusInfo,gc.getNumBonusInfos(),'BONUS_IRON')
	if 0 == player.getNumAvailableBonuses(iIron):
		listBonuses.append(iIron)
	iHorse = CvUtil.findInfoTypeNum(gc.getBonusInfo,gc.getNumBonusInfos(),'BONUS_HORSE')
	if 0 == player.getNumAvailableBonuses(iHorse):
		listBonuses.append(iHorse)
	iCopper = CvUtil.findInfoTypeNum(gc.getBonusInfo,gc.getNumBonusInfos(),'BONUS_COPPER')
	if 0 == player.getNumAvailableBonuses(iCopper):
		listBonuses.append(iCopper)
	# edead: start
	iSulfur = CvUtil.findInfoTypeNum(gc.getBonusInfo,gc.getNumBonusInfos(),'BONUS_SULFUR')
	if 0 == player.getNumAvailableBonuses(iSulfur):
		listBonuses.append(iSulfur)
	# edead: end

	map = gc.getMap()
	bFound = false
	listPlots = []
	for iBonus in listBonuses:
		for i in range(map.numPlots()):
			loopPlot = map.plotByIndex(i)
			if loopPlot.getOwner() == kTriggeredData.eOtherPlayer and loopPlot.getBonusType(player.getTeam()) == iBonus and loopPlot.isRevealed(player.getTeam(), false) and not loopPlot.isWater():
				listPlots.append(loopPlot)
				bFound = true
		if bFound:
			break
			
	if not bFound:
		return false

	plot = listPlots[gc.getGame().getSorenRandNum(len(listPlots), "Greed event plot selection")]
	
	if -1 == getGreedUnit(player, plot):
		return false
	
	kActualTriggeredDataObject = player.getEventTriggered(kTriggeredData.iId)
	kActualTriggeredDataObject.iPlotX = plot.getX()
	kActualTriggeredDataObject.iPlotY = plot.getY()
				
	return true

def getHelpGreed1(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	otherPlayer = gc.getPlayer(kTriggeredData.eOtherPlayer)
	iBonus = gc.getMap().plot(kTriggeredData.iPlotX, kTriggeredData.iPlotY).getBonusType(player.getTeam())
	
	iTurns = gc.getGameSpeedInfo(gc.getGame().getGameSpeedType()).getGrowthPercent()
			
	szHelp = localText.getText("TXT_KEY_EVENT_GREED_HELP_1", (otherPlayer.getCivilizationShortDescriptionKey(), gc.getBonusInfo(iBonus).getTextKey(), iTurns))

	return szHelp

def expireGreed1(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	otherPlayer = gc.getPlayer(kTriggeredData.eOtherPlayer)
	plot = gc.getMap().plot(kTriggeredData.iPlotX, kTriggeredData.iPlotY)

	if plot.getOwner() == kTriggeredData.ePlayer or plot.getOwner() == -1:
		return false
	
	if gc.getGame().getGameTurn() >= kTriggeredData.iTurn + gc.getGameSpeedInfo(gc.getGame().getGameSpeedType()).getGrowthPercent():
		return true
	
	if plot.getOwner() != kTriggeredData.eOtherPlayer:
		return true
				
	return false

def canTriggerGreedDone(argsList):
	kTriggeredData = argsList[0]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	trigger = gc.getEventTriggerInfo(kTriggeredData.eTrigger)
	kOrigTriggeredData = player.getEventOccured(trigger.getPrereqEvent(0))
	plot = gc.getMap().plot(kOrigTriggeredData.iPlotX, kOrigTriggeredData.iPlotY)

	if plot.getOwner() != kOrigTriggeredData.ePlayer:
		return false
		
	if -1 == getGreedUnit(player, plot):
		return false

	kActualTriggeredDataObject = player.getEventTriggered(kTriggeredData.iId)
	kActualTriggeredDataObject.iPlotX = kOrigTriggeredData.iPlotX
	kActualTriggeredDataObject.iPlotY = kOrigTriggeredData.iPlotY
	kActualTriggeredDataObject.eOtherPlayer = kOrigTriggeredData.eOtherPlayer
	
	return true

def getGreedUnit(player, plot):
	iBonus = plot.getBonusType(player.getTeam())
	iBestValue = 0
	iBestUnit = -1
	for iUnitClass in range(gc.getNumUnitClassInfos()):
		iUnit = gc.getCivilizationInfo(player.getCivilizationType()).getCivilizationUnits(iUnitClass)
		# edead: skip limited units
		#if iUnit in [con.iTemplar, con.iHospitaller, con.iHospitallerSergeant, con.iItalianMaceman, con.iItalianCrossbowman]: 
			#continue
		# edead: end
		if -1 != iUnit and player.canTrain(iUnit, false, false) and (gc.getUnitInfo(iUnit).getDomainType() == DomainTypes.DOMAIN_LAND):
			iValue = 0
			if gc.getUnitInfo(iUnit).getPrereqAndBonus() == iBonus:
				iValue = player.AI_unitValue(iUnit, UnitAITypes.UNITAI_ATTACK, plot.area())
			else:
				for j in range(gc.getNUM_UNIT_PREREQ_OR_BONUSES()):
					if (gc.getUnitInfo(iUnit).getPrereqOrBonuses(j) == iBonus):
						iValue = player.AI_unitValue(iUnit, UnitAITypes.UNITAI_ATTACK, plot.area())
						break
			if iValue > iBestValue:
				iBestValue = iValue
				iBestUnit = iUnit
				
	return iBestUnit
	

def getHelpGreedDone1(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	plot = gc.getMap().plot(kTriggeredData.iPlotX, kTriggeredData.iPlotY)
	
	iNumUnits = gc.getWorldInfo(gc.getMap().getWorldSize()).getDefaultPlayers() / 2 + 1
	iUnitType = getGreedUnit(player, plot)
	
	if iUnitType != -1:	
		szHelp = localText.getText("TXT_KEY_EVENT_GREED_DONE_HELP_1", (iNumUnits, gc.getUnitInfo(iUnitType).getTextKey()))	

	return szHelp

def applyGreedDone1(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	plot = gc.getMap().plot(kTriggeredData.iPlotX, kTriggeredData.iPlotY)
		
	iUnitType = getGreedUnit(player, plot)
	iNumUnits = gc.getWorldInfo(gc.getMap().getWorldSize()).getDefaultPlayers() / 2 + 1
	
	if iUnitType != -1:
		for i in range(iNumUnits):
			player.initUnit(iUnitType, plot.getX(), plot.getY(), UnitAITypes.UNITAI_ATTACK, DirectionTypes.DIRECTION_SOUTH)


######## WAR CHARIOTS ###########

def canTriggerWarChariots(argsList):
	kTriggeredData = argsList[0]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	
	kActualTriggeredDataObject = player.getEventTriggered(kTriggeredData.iId)
	kActualTriggeredDataObject.eReligion = ReligionTypes(player.getStateReligion())
	
	return true

def getHelpWarChariots1(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
		
	iNumUnits = gc.getWorldInfo(gc.getMap().getWorldSize()).getDefaultPlayers() + 1
	szHelp = localText.getText("TXT_KEY_EVENT_WAR_CHARIOTS_HELP_1", (iNumUnits, ))

	return szHelp

def canTriggerWarChariotsDone(argsList):
	kTriggeredData = argsList[0]
	trigger = gc.getEventTriggerInfo(kTriggeredData.eTrigger)
	player = gc.getPlayer(kTriggeredData.ePlayer)
	
	iNumUnits = gc.getWorldInfo(gc.getMap().getWorldSize()).getDefaultPlayers() + 1
	iUnitClassType = CvUtil.findInfoTypeNum(gc.getUnitClassInfo, gc.getNumUnitClassInfos(), 'UNITCLASS_CHARIOT')
	if player.getUnitClassCount(iUnitClassType) < iNumUnits:
		return false
	
	kOrigTriggeredData = player.getEventOccured(trigger.getPrereqEvent(0))
	kActualTriggeredDataObject = player.getEventTriggered(kTriggeredData.iId)
	kActualTriggeredDataObject.eReligion = kOrigTriggeredData.eReligion
		
	return true

######## ELITE SWORDSMEN ###########

def getHelpEliteSwords1(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
		
	#iNumUnits = gc.getWorldInfo(gc.getMap().getWorldSize()).getDefaultPlayers() + 1
	iNumUnits = gc.getWorldInfo(gc.getMap().getWorldSize()).getDefaultPlayers() / 2 + 1 # edead
	szHelp = localText.getText("TXT_KEY_EVENT_ELITE_SWORDS_HELP_1", (iNumUnits, ))

	return szHelp

def canTriggerEliteSwordsDone(argsList):
	kTriggeredData = argsList[0]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	
	#iNumUnits = gc.getWorldInfo(gc.getMap().getWorldSize()).getDefaultPlayers() + 1
	iNumUnits = gc.getWorldInfo(gc.getMap().getWorldSize()).getDefaultPlayers() / 2 + 1 # edead
	iUnitClassType = CvUtil.findInfoTypeNum(gc.getUnitClassInfo, gc.getNumUnitClassInfos(), 'UNITCLASS_SWORDSMAN')
	if player.getUnitClassCount(iUnitClassType) < iNumUnits:
		return false
			
	return true


def canApplyEliteSwordsDone2(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	
	iCivic = CvUtil.findInfoTypeNum(gc.getCivicInfo,gc.getNumCivicInfos(),'CIVIC_MONARCHY')
	
	if not player.isCivic(iCivic):
		return false
	
	return true	

######## WARSHIPS ###########

def canTriggerWarships(argsList):
	kTriggeredData = argsList[0]
	
	map = gc.getMap()
	iNumWater = 0
	
	for i in range(map.numPlots()):
		plot = map.plotByIndex(i)
		
		if plot.isWater():
			iNumWater += 1
			
		if 100 * iNumWater >= 55 * map.numPlots():
			return true
			
	return false

def getHelpWarships1(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
		
	# edead: start
	#iNumUnits = gc.getWorldInfo(gc.getMap().getWorldSize()).getDefaultPlayers()
	iNumUnits = gc.getWorldInfo(gc.getMap().getWorldSize()).getDefaultPlayers() / 2
	# iBuilding = CvUtil.findInfoTypeNum(gc.getBuildingInfo, gc.getNumBuildingInfos(), 'BUILDING_GREAT_LIGHTHOUSE')
	iBuilding = CvUtil.findInfoTypeNum(gc.getBuildingInfo, gc.getNumBuildingInfos(), 'BUILDING_KIZIL_KULE')
	# edead: end
	szHelp = localText.getText("TXT_KEY_EVENT_WARSHIPS_HELP_1", (iNumUnits, gc.getBuildingInfo(iBuilding).getTextKey()))

	return szHelp

def canTriggerWarshipsDone(argsList):
	kTriggeredData = argsList[0]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	
	# edead: start
	#iNumUnits = gc.getWorldInfo(gc.getMap().getWorldSize()).getDefaultPlayers()
	iNumUnits = gc.getWorldInfo(gc.getMap().getWorldSize()).getDefaultPlayers() / 2
	# iUnitClassType = CvUtil.findInfoTypeNum(gc.getUnitClassInfo, gc.getNumUnitClassInfos(), 'UNITCLASS_TRIREME')
	iUnitClassType = CvUtil.findInfoTypeNum(gc.getUnitClassInfo, gc.getNumUnitClassInfos(), 'UNITCLASS_WAR_GALLEY')
	# edead: end

	if player.getUnitClassCount(iUnitClassType) < iNumUnits:
		return false
			
	return true


def canApplyWarshipsDone2(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	
	# edead: start
	# iBuilding = CvUtil.findInfoTypeNum(gc.getBuildingInfo, gc.getNumBuildingInfos(), 'BUILDING_GREAT_LIGHTHOUSE')
	iBuilding = CvUtil.findInfoTypeNum(gc.getBuildingInfo, gc.getNumBuildingInfos(), 'BUILDING_KIZIL_KULE')
	# edead: end
	if player.getBuildingClassCount(gc.getBuildingInfo(iBuilding).getBuildingClassType()) == 0:
		return false

	return true	

######## GUNS NOT BUTTER ###########

def getHelpGunsButter1(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
		
	#iNumUnits = gc.getWorldInfo(gc.getMap().getWorldSize()).getDefaultPlayers() + 1
	iNumUnits = gc.getWorldInfo(gc.getMap().getWorldSize()).getDefaultPlayers() / 2 + 1 # edead
	iBuilding = CvUtil.findInfoTypeNum(gc.getBuildingInfo, gc.getNumBuildingInfos(), 'BUILDING_TAJ_MAHAL')
	
	szHelp = localText.getText("TXT_KEY_EVENT_GUNS_BUTTER_HELP_1", (iNumUnits, gc.getBuildingInfo(iBuilding).getTextKey()))

	return szHelp

def canTriggerGunsButterDone(argsList):
	kTriggeredData = argsList[0]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	
	iNumUnits = gc.getWorldInfo(gc.getMap().getWorldSize()).getDefaultPlayers() + 1
	iUnitClassType = CvUtil.findInfoTypeNum(gc.getUnitClassInfo, gc.getNumUnitClassInfos(), 'UNITCLASS_MUSKETMAN')

	if player.getUnitClassCount(iUnitClassType) < iNumUnits:
		return false
			
	return true


def canApplyGunsButterDone2(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)
		
	iCivic = CvUtil.findInfoTypeNum(gc.getCivicInfo,gc.getNumCivicInfos(),'CIVIC_VASSALAGE')
	
	if not player.isCivic(iCivic):
		return false
	
	return true	

def canApplyGunsButterDone3(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)
		
	iBuilding = CvUtil.findInfoTypeNum(gc.getBuildingInfo, gc.getNumBuildingInfos(), 'BUILDING_TAJ_MAHAL')
	if player.getBuildingClassCount(gc.getBuildingInfo(iBuilding).getBuildingClassType()) == 0:
		return false

	return true	

######## NOBLE KNIGHTS ###########

def canTriggerNobleKnights(argsList):
	kTriggeredData = argsList[0]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	
	kActualTriggeredDataObject = player.getEventTriggered(kTriggeredData.iId)
	kActualTriggeredDataObject.eReligion = ReligionTypes(player.getStateReligion())
	
	return true

def getHelpNobleKnights1(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
		
	#iNumUnits = gc.getWorldInfo(gc.getMap().getWorldSize()).getDefaultPlayers() + 1
	iNumUnits = gc.getWorldInfo(gc.getMap().getWorldSize()).getDefaultPlayers() / 2 + 1 # edead
	# iBuilding = CvUtil.findInfoTypeNum(gc.getBuildingInfo, gc.getNumBuildingInfos(), 'BUILDING_ORACLE') 
	iBuilding = CvUtil.findInfoTypeNum(gc.getBuildingInfo, gc.getNumBuildingInfos(), 'BUILDING_GREAT_WALL') # edead
	
	szHelp = localText.getText("TXT_KEY_EVENT_NOBLE_KNIGHTS_HELP_1", (iNumUnits, gc.getBuildingInfo(iBuilding).getTextKey()))

	return szHelp

def canTriggerNobleKnightsDone(argsList):
	kTriggeredData = argsList[0]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	
	# edead: start
	#iNumUnits = gc.getWorldInfo(gc.getMap().getWorldSize()).getDefaultPlayers() + 1
	iNumUnits = gc.getWorldInfo(gc.getMap().getWorldSize()).getDefaultPlayers() / 2 + 1
	# iUnitClassType = CvUtil.findInfoTypeNum(gc.getUnitClassInfo, gc.getNumUnitClassInfos(), 'UNITCLASS_KNIGHT')
	iUnitClassType = CvUtil.findInfoTypeNum(gc.getUnitClassInfo, gc.getNumUnitClassInfos(), 'UNITCLASS_LANCER')
	iUnitClassType2 = CvUtil.findInfoTypeNum(gc.getUnitClassInfo, gc.getNumUnitClassInfos(), 'UNITCLASS_HEAVY_LANCER')

	# if player.getUnitClassCount(iUnitClassType) < iNumUnits:
	if player.getUnitClassCount(iUnitClassType) + player.getUnitClassCount(iUnitClassType2) < iNumUnits:
	# edead: end
		return false
			
	trigger = gc.getEventTriggerInfo(kTriggeredData.eTrigger)
	kOrigTriggeredData = player.getEventOccured(trigger.getPrereqEvent(0))
	kActualTriggeredDataObject = player.getEventTriggered(kTriggeredData.iId)
	kActualTriggeredDataObject.eReligion = kOrigTriggeredData.eReligion

	# iBuilding = CvUtil.findInfoTypeNum(gc.getBuildingInfo, gc.getNumBuildingInfos(), 'BUILDING_ORACLE') # edead
	iBuilding = CvUtil.findInfoTypeNum(gc.getBuildingInfo, gc.getNumBuildingInfos(), 'BUILDING_QALEH_DOKHTAR') # edead # srpt
	
	(loopCity, iter) = player.firstCity(false)
	while(loopCity):
		if (loopCity.isHasBuilding(iBuilding)):
			kActualTriggeredDataObject.iPlotX = loopCity.getX()
			kActualTriggeredDataObject.iPlotY = loopCity.getY()
			kActualTriggeredDataObject.iCityId = loopCity.getID()
			break
				
		(loopCity, iter) = player.nextCity(iter, false)

	return true

def canApplyNobleKnightsDone2(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)
		
	iCivic = CvUtil.findInfoTypeNum(gc.getCivicInfo,gc.getNumCivicInfos(),'CIVIC_ORGANIZED_RELIGION') # edead
	
	if not player.isCivic(iCivic):
		return false
	
	return true	

####### Immigrants ########

def canTriggerImmigrantCity(argsList):
	ePlayer = argsList[1]
	iCity = argsList[2]
	
	player = gc.getPlayer(ePlayer)
	city = player.getCity(iCity)

	if city.isNone():
		return false

	if ((city.happyLevel() - city.unhappyLevel(0) < 1) or (city.goodHealth() - city.badHealth(true) < 1)):
		return false

	if (city.getCommerceRateTimes100(CommerceTypes.COMMERCE_CULTURE) < 5500):
		return false

####### Controversial Philosopher ######

def canTriggerControversialPhilosopherCity(argsList):
	ePlayer = argsList[1]
	iCity = argsList[2]
	
	player = gc.getPlayer(ePlayer)
	city = player.getCity(iCity)
	
	if city.isNone():
		return false
	if (not city.isCapital()):
		return false
	if (city.getCommerceRateTimes100(CommerceTypes.COMMERCE_RESEARCH) < 3500):
		return false

	return true

####### Spy Discovered #######


def canDoSpyDiscovered3(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]

	player = gc.getPlayer(kTriggeredData.ePlayer)
	
	if player.getNumCities() < 4:
		return false
	
	if player.getCapitalCity().isNone():
		return false
				
	return true

def doSpyDiscovered3(argsList):
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)

	plot = player.getCapitalCity().plot()
	iNumUnits = player.getNumCities() / 4
	iUnitClassType = CvUtil.findInfoTypeNum(gc.getUnitClassInfo, gc.getNumUnitClassInfos(), 'UNITCLASS_TANK')
	iUnitType = gc.getCivilizationInfo(player.getCivilizationType()).getCivilizationUnits(iUnitClassType)
	
	if iUnitType != -1:
		for i in range(iNumUnits):
			player.initUnit(iUnitType, plot.getX(), plot.getY(), UnitAITypes.UNITAI_ATTACK, DirectionTypes.DIRECTION_SOUTH)

def getHelpSpyDiscovered3(argsList):
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	iNumUnits = player.getNumCities() / 4
	szHelp = localText.getText("TXT_KEY_EVENT_SPY_DISCOVERED_3_HELP", (iNumUnits, ))

	return szHelp

######## Preaching Researcher #######

def canTriggerPreachingResearcherCity(argsList):
	iCity = argsList[2]
	
	player = gc.getPlayer(argsList[1])
	city = player.getCity(iCity)

	if city.isHasBuilding(gc.getInfoTypeForString("BUILDING_UNIVERSITY")):
		return true
	return false

######## Greek Fire (edead) ########

def getHelpGreekFire1(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	
	iWarGalleysRequired = gc.getWorldInfo(gc.getMap().getWorldSize()).getDefaultPlayers() / 2
	
	szHelp = localText.getText("TXT_KEY_EVENT_GREEK_FIRE_HELP", (iWarGalleysRequired, ))
	
	return szHelp

def canTriggerGreekFire(argsList):
	kTriggeredData = argsList[0]

	if kTriggeredData.ePlayer != con.iRome:
		return false
	
	return true

def canTriggerGreekFireDone(argsList):
	kTriggeredData = argsList[0]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	
	iWarGalley = CvUtil.findInfoTypeNum(gc.getUnitClassInfo, gc.getNumUnitClassInfos(), 'UNITCLASS_WAR_GALLEY')
	
	nRequired = gc.getWorldInfo(gc.getMap().getWorldSize()).getDefaultPlayers() / 2
	if nRequired > player.getUnitClassCount(iWarGalley):
		return false
	
	return true

def canTriggerGreekFireDoneCity(argsList):
	eTrigger = argsList[0]
	ePlayer = argsList[1]
	iCity = argsList[2]
	
	player = gc.getPlayer(ePlayer)
	city = player.getCity(iCity)
	
	if (city.getX(), city.getY()) == con.tConstantinople:
		return true
	
	return false
	
def applyGreekFire1(argsList):
	kTriggeredData = argsList[1]
	
	iGreekFire = CvUtil.findInfoTypeNum(gc.getPromotionInfo, gc.getNumPromotionInfos(), 'PROMOTION_GREEK_FIRE')
	iWarGalley = CvUtil.findInfoTypeNum(gc.getUnitInfo, gc.getNumUnitInfos(), 'UNIT_WAR_GALLEY')
	
	unitList = PyPlayer(kTriggeredData.ePlayer).getUnitList()
	for unit in unitList:
		if unit.getUnitType() == iWarGalley:
			unit.setHasPromotion(iGreekFire, true)

######## EARTHQUAKE ###########

def getHelpEarthquake1(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]

	szHelp = localText.getText("TXT_KEY_EVENT_EARTHQUAKE_1_HELP", ())

	return szHelp

def canApplyEarthquake1(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	
	iNumImprovements = 0
	for iDX in range(-1, 2):
		for iDY in range(-1, 2):
			loopPlot = plotXY(kTriggeredData.iPlotX, kTriggeredData.iPlotY, iDX, iDY)
			if not loopPlot.isNone():
				if (iDX != 0 or iDY != 0):
					if loopPlot.getImprovementType() != -1:
						iNumImprovements += 1

	return (iNumImprovements > 0)

def applyEarthquake1(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	
	listPlots = []
	for iDX in range(-1, 2):
		for iDY in range(-1, 2):
			loopPlot = plotXY(kTriggeredData.iPlotX, kTriggeredData.iPlotY, iDX, iDY)
			if not loopPlot.isNone():
				if (iDX != 0 or iDY != 0):
					if loopPlot.getImprovementType() != -1:
						listPlots.append(loopPlot)
					
	listRuins = []
	listRuins.append(CvUtil.findInfoTypeNum(gc.getImprovementInfo,gc.getNumImprovementInfos(),'IMPROVEMENT_COTTAGE'))
	listRuins.append(CvUtil.findInfoTypeNum(gc.getImprovementInfo,gc.getNumImprovementInfos(),'IMPROVEMENT_HAMLET'))
	listRuins.append(CvUtil.findInfoTypeNum(gc.getImprovementInfo,gc.getNumImprovementInfos(),'IMPROVEMENT_VILLAGE'))
	listRuins.append(CvUtil.findInfoTypeNum(gc.getImprovementInfo,gc.getNumImprovementInfos(),'IMPROVEMENT_TOWN'))
	
	iRuins = CvUtil.findInfoTypeNum(gc.getImprovementInfo,gc.getNumImprovementInfos(),'IMPROVEMENT_CITY_RUINS')

	for i in range(3):
		if len(listPlots) > 0:
			plot = listPlots[gc.getGame().getSorenRandNum(len(listPlots), "Earthquake event improvement destroyed")]
			iImprovement = plot.getImprovementType()
			szBuffer = localText.getText("TXT_KEY_EVENT_CITY_IMPROVEMENT_DESTROYED", (gc.getImprovementInfo(iImprovement).getTextKey(), ))
			CyInterface().addMessage(kTriggeredData.ePlayer, false, gc.getEVENT_MESSAGE_TIME(), szBuffer, "AS2D_BOMBARDED", InterfaceMessageTypes.MESSAGE_TYPE_INFO, gc.getImprovementInfo(iImprovement).getButton(), gc.getInfoTypeForString("COLOR_RED"), plot.getX(), plot.getY(), true, true)
			if iImprovement in listRuins:
				plot.setImprovementType(iRuins)
			else:
				plot.setImprovementType(-1)
			listPlots.remove(plot)
			
			if i == 1 and gc.getGame().getSorenRandNum(100, "Earthquake event num improvements destroyed") < 50:
				break

####### Crusades (edead) ######

def canTriggerCrusadeCity(argsList):
	eTrigger = argsList[0]
	ePlayer = argsList[1]
	iCity = argsList[2]
	
	player = gc.getPlayer(ePlayer)
	city = player.getCity(iCity)
	
	# crusaders only
	#if ePlayer != con.iAxum and ePlayer != con.iKushans:
		#return false
	#if player.getStateReligion() != con.iCatholicism:
		#return false
	
	# no more than 10 crusades
	#if utils.getNumCrusades() >= 10:
		#return false
	
	# only proceed if the player has lost a city in core area
	#if not utils.isHasLostCity(ePlayer):
		#return false
	
	# minimum 15 turns delay between crusades
	#if utils.getLastCrusadeTurn(ePlayer) > gc.getGame().getGameTurn() - utils.getTurns(15):
		#return false
	
	return false

def applyCrusade1(argsList):
	kTriggeredData = argsList[1]
	
	player = gc.getPlayer(kTriggeredData.ePlayer)
	
	map = gc.getMap()
	plot = map.plot(kTriggeredData.iPlotX, kTriggeredData.iPlotY)
	
	unitSets = (
		(con.iLancer, con.iHorseman, con.iHorseman),
		(con.iLancer, con.iHeavySpearman, con.iMarksman),
		(con.iLancer, con.iMarksman, con.iMarksman),
		(con.iLancer, con.iSwordsman, con.iSpearman, con.iSpearman, con.iArcher),
		(con.iLancer, con.iSwordsman, con.iSpearman, con.iArcher, con.iArcher),
		(con.iHorseman, con.iSpearman, con.iArcher, con.iTrebuchet),
		(con.iHorseman, con.iSpearman, con.iArcher, con.iArcher, con.iArcher),
		(con.iSwordsman, con.iSwordsman, con.iMarksman, con.iTrebuchet),
		(con.iSwordsman, con.iSwordsman, con.iArcher, con.iArcher, con.iTrebuchet),
		(con.iHeavySwordsman, con.iMarksman, con.iTrebuchet),
	)
	
	for iUnitType in unitSets[gc.getGame().getSorenRandNum(len(unitSets), "Random set")]:
		player.initUnit(iUnitType, plot.getX(), plot.getY(), UnitAITypes.UNITAI_ATTACK, DirectionTypes.DIRECTION_SOUTH)
	
	utils.setNumCrusades(utils.getNumCrusades() + 1)
	utils.setHasLostCity(kTriggeredData.ePlayer, False)
	utils.setLastCrusadeTurn(kTriggeredData.ePlayer, gc.getGame().getGameTurn())

####### Aristocrats Concerned (edead) ######

def canTriggerAristocratsConcerned(argsList):
	
	kTriggeredData = argsList[0]
	
	if kTriggeredData.ePlayer >= con.iNumPlayers:
		return false
	
	if gc.getGame().getGameTurn() - con.tBirth[kTriggeredData.ePlayer] < 30:
		return false
	
	if gc.getPlayer(kTriggeredData.ePlayer).getGold() < 100:
		return false
	
	#if utils.getStability(kTriggeredData.ePlayer) < 10:  srpt needs to be updated to new system
		#return false
	
	return true

######## The Reconquest of Holy Land (edead) ########

def getHelpReconquestOfHolyLand1(argsList):
	szHelp = localText.getText("TXT_KEY_EVENT_RECONQUEST_OF_HOLY_LAND_HELP", ())
	return szHelp

def canTriggerReconquestOfHolyLand(argsList):
	kTriggeredData = argsList[0]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	
	if player.getStateReligion() != con.iIslam:
		return false
	
	if gc.getGame().getGameTurn() < getTurnForYear(con.tBirth[con.iJin]) + 2:
		return false
	
	if gc.getGame().getGameTurn() > getTurnForYear(1299):
		return false
	
	if gc.getPlayer(gc.getMap().plot(con.tJerusalem[0], con.tJerusalem[1]).getOwner()).getStateReligion() not in [con.iChristianity]:
		return false
	
	return true

def canTriggerReconquestOfHolyLandDone(argsList):
	kTriggeredData = argsList[0]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	
	if gc.getMap().plot(con.tJerusalem[0], con.tJerusalem[1]).getOwner() != kTriggeredData.ePlayer:
		return false
	
	return true

def doReconquestOfHolyLandDone(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	
	sd.changePiety(kTriggeredData.ePlayer, 10)
	CvMainInterface().updateGameDataStrings()
	
	return 1

def getHelpReconquestOfHolyLandDone1(argsList):
	szHelp = localText.getText("TXT_KEY_EVENT_RECONQUEST_OF_HOLY_LAND_DONE_HELP", (10, ))
	return szHelp

######## Kharijites (edead) ########

def canTriggerKharijitesCity(argsList):
	eTrigger = argsList[0]
	ePlayer = argsList[1]
	iCity = argsList[2]
	
	player = gc.getPlayer(ePlayer)
	city = player.getCity(iCity)
	
	if ePlayer != con.iArabs:
		return false
	
	if utils.getYear() > 1000:
		return false
	
	return true

####### Soil Degradation (edead) #######

def canTriggerSoilDegradation(argsList):
	kTriggeredData = argsList[0]
	
	if kTriggeredData.ePlayer >= con.iNumPlayers:
		return false
	
	if utils.getYear() < 1200:
		return false
	elif utils.getYear() < 1300:
		if gc.getMap().plot(con.tBaghdad[0],con.tBaghdad[1]).getOwner() == kTriggeredData.ePlayer:
			return true
		if gc.getMap().plot(con.tCtesiphon[0],con.tCtesiphon[1]).getOwner() == kTriggeredData.ePlayer:
			return true
		if gc.getMap().plot(con.tPersepolis[0],con.tPersepolis[1]).getOwner() == kTriggeredData.ePlayer:
			return true
	elif utils.getYear() < 1350:
			if gc.getMap().plot(6,11).getOwner() == kTriggeredData.ePlayer:
				return true
			if gc.getMap().plot(13,6).getOwner() == kTriggeredData.ePlayer:
				return true
			if gc.getMap().plot(79,21).getOwner() == kTriggeredData.ePlayer:
				return true
	elif utils.getYear() < 1400:
			if gc.getMap().plot(9,31).getOwner() == kTriggeredData.ePlayer:
				return true
			if gc.getMap().plot(9,27).getOwner() == kTriggeredData.ePlayer:
				return true
			if gc.getMap().plot(6,34).getOwner() == kTriggeredData.ePlayer:
				return true
			if gc.getMap().plot(68,63).getOwner() == kTriggeredData.ePlayer:
				return true
			if gc.getMap().plot(74,59).getOwner() == kTriggeredData.ePlayer:
				return true
	
	return false

####### Iconoclasm (edead) #######

def canTriggerIconoclasm(argsList):
	kTriggeredData = argsList[0]
	
	if kTriggeredData.ePlayer != con.iRome:
		return false
	
	if utils.getYear() > 1050:
		return false
	
	return true

def applyIconoclasm2(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	
	sd.changePiety(kTriggeredData.ePlayer, -5)
	CvMainInterface().updateGameDataStrings()

def getHelpIconoclasm2(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	
	szHelp = localText.getText("TXT_KEY_EVENT_HELP_ICONOCLASM_2", (5, ))

	return szHelp
	
####### Orban the Gunfounder (edead) #######

def canTriggerOrbanTheGunfounder(argsList):
	kTriggeredData = argsList[0]
	
	if kTriggeredData.ePlayer != con.iRome:
		return false
	
	if utils.getYear() < 1350:
		return false
	
	if not utils.isActive(con.iOttomans):
		return false
	
	return true

def canTriggerOrbanTheGunfounderCity(argsList):
	eTrigger = argsList[0]
	ePlayer = argsList[1]
	iCity = argsList[2]
	
	player = gc.getPlayer(ePlayer)
	city = player.getCity(iCity)
	
	if city.getX() == con.tConstantinople[0] and city.getY() == con.tConstantinople[1]:
		return true
	
	return false

def triggerOrbanTheGreedy(argsList):
	
	if gc.getMap().plot(1,65).isCity() and gc.getMap().plot(1,65).getOwner() == con.iOttomans:
		city = gc.getMap().plot(1,65).getPlotCity()
	elif gc.getMap().plot(5,59).isCity() and gc.getMap().plot(5,59).getOwner() == con.iOttomans:
		city = gc.getMap().plot(5,59).getPlotCity()
	elif gc.getMap().plot(2,60).isCity() and gc.getMap().plot(2,60).getOwner() == con.iOttomans:
		city = gc.getMap().plot(2,60).getPlotCity()
	elif gc.getMap().plot(1,60).isCity() and gc.getMap().plot(1,60).getOwner() == con.iOttomans:
		city = gc.getMap().plot(1,60).getPlotCity()
	elif gc.getMap().plot(2,56).isCity() and gc.getMap().plot(2,56).getOwner() == con.iOttomans:
		city = gc.getMap().plot(2,56).getPlotCity()
	else:
		city = None
	
	if city and gc.getPlayer(con.iOttomans).isAlive():
		gc.getPlayer(con.iOttomans).initTriggeredData(gc.getInfoTypeForString("EVENTTRIGGER_ORBAN_THE_GREEDY"), True, city.getID(), city.getX(), city.getY(), -1, -1, -1, -1, -1, -1, "")

####### Pilgrims (edead) ######

def canTriggerPilgrims(argsList):
	kTriggeredData = argsList[0]
	
	if kTriggeredData.ePlayer != con.iFranks:
		return false
	
	if not utils.isActive(con.iFranks):
		return false
	
	return true

def canTriggerPilgrimsCity(argsList):
	eTrigger = argsList[0]
	ePlayer = argsList[1]
	iCity = argsList[2]
	
	player = gc.getPlayer(ePlayer)
	city = player.getCity(iCity)
	
	if city.getOwner() == con.iAxum and city.isCoastal(20):
		return true
	
	return false

####### Knights of St. John (edead) ######

def canTriggerKnightsOfStJohnCity(argsList):
	ePlayer = argsList[1]
	
	if ePlayer == con.iFranks or ePlayer == con.iRome:
		return true
	
	return false

####### Middle Eastern Cuisine (edead) #######

def canTriggerAlmonds(argsList):
	kTriggeredData = argsList[0]

	if not kTriggeredData.ePlayer in [con.iRome, con.iParthia, con.iFranks]:
		return false

	plot = gc.getMap().plot(kTriggeredData.iPlotX, kTriggeredData.iPlotY)
	if plot.isCity() or plot.getBonusType(-1) >= 0:
		return false
		
	return true

def canTriggerApricots(argsList):
	kTriggeredData = argsList[0]

	if not kTriggeredData.ePlayer in [con.iRome, con.iParthia, con.iArmenia]:
		return false

	plot = gc.getMap().plot(kTriggeredData.iPlotX, kTriggeredData.iPlotY)
	if plot.isCity() or plot.getBonusType(-1) >= 0:
		return false
		
	return true

def canTriggerSesame(argsList):
	kTriggeredData = argsList[0]

	if not kTriggeredData.ePlayer in [con.iParthia, con.iSeleucids, con.iSaba, con.iEgypt, con.iAxum, con.iNubia, con.iSatavahana]:
		return false

	plot = gc.getMap().plot(kTriggeredData.iPlotX, kTriggeredData.iPlotY)
	if plot.isCity() or plot.getBonusType(-1) >= 0:
		return false
		
	return true

def canTriggerPistachios(argsList):
	kTriggeredData = argsList[0]

	if not kTriggeredData.ePlayer in [con.iParthia, con.iSeleucids, con.iSaba, con.iEgypt, con.iAxum, con.iNubia, con.iSatavahana]:
		return false

	plot = gc.getMap().plot(kTriggeredData.iPlotX, kTriggeredData.iPlotY)
	if plot.isCity() or plot.getBonusType(-1) >= 0:
		return false
		
	return true

####### Expulsion of Jews (edead) #######
	
def canTriggerExpulsionOfJewsCity(argsList):
	eTrigger = argsList[0]
	ePlayer = argsList[1]
	iCity = argsList[2]
	
	player = gc.getPlayer(ePlayer)
	city = player.getCity(iCity)
	
	if city.isNone():
		return false

	if city.getNumReligions() < 2:
		return false
		
	if city.getPopulation() < 2:
		return false
	
	return true

def doExpulsionOfJews2(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	
	city = gc.getMap().plot(kTriggeredData.iPlotX, kTriggeredData.iPlotY).getPlotCity()
	
	if city and not city.isNone():
		if city.isHasReligion(con.iJudaism):
			city.setHasReligion(con.iJudaism, False, True, True)
			return 1

	# move jews
	if gc.getGame().getGameTurn() <= getTurnForYear(1200):
		city = utils.getRandomCityByRegion(con.jewsEarlyRegions)
	else:
		city = utils.getRandomCityByRegion(con.jewsMiddleRegions)
	if city and not city.isNone() and not city.isHasReligion(con.iJudaism) and not city.getOwner() == kTriggeredData.ePlayer:
		city.setHasReligion(con.iJudaism, True, False, False)
		szText = CyTranslator().getText("TXT_KEY_MINOR_EVENT_JEWS", (city.getName(), ))
		CyInterface().addMessage(city.getOwner(), False, con.iDuration, szText, "AS2D_BUILD_JEWISH", InterfaceMessageTypes.MESSAGE_TYPE_MAJOR_EVENT, gc.getReligionInfo(con.iJudaism).getButton(), ColorTypes(con.iWhite), city.getX(), city.getY(), True, True)
			
	return 0

def canDoExpulsionOfJews3(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]

	player = gc.getPlayer(kTriggeredData.ePlayer)

	iNumJews = 0
	apCityList = PyPlayer(kTriggeredData.ePlayer).getCityList()
	for pCity in apCityList:
		city = pCity.GetCy()
		if city.isHasReligion(con.iJudaism):
			iNumJews += 1
	
	if iNumJews < 2:
		return false
				
	return true
	
def doExpulsionOfJews3(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	
	city = gc.getMap().plot(kTriggeredData.iPlotX, kTriggeredData.iPlotY).getPlotCity()
	
	if city and not city.isNone():
		if city.isHasReligion(con.iJudaism):
			city.setHasReligion(con.iJudaism, False, True, True)
			skipID = city.getID()
	
	apCityList = PyPlayer(city.getOwner()).getCityList()
	for pCity in apCityList:
		city = pCity.GetCy()
		if city.isHasReligion(con.iJudaism) and city.getID() != skipID:
			city.setHasReligion(con.iJudaism, False, True, False)
			if city.getPopulation() > 1:
				city.changePopulation(-1)
	
	# move jews
	#if gc.getGame().getGameTurn() <= getTurnForYear(1200):
	city = utils.getRandomCityByRegion(con.lNearJewishRegions)
	#else:
		#city = utils.getRandomCityByRegion(con.jewsMiddleRegions)
	if city and not city.isNone() and not city.isHasReligion(con.iJudaism) and not city.getOwner() == kTriggeredData.ePlayer:
		city.setHasReligion(con.iJudaism, True, False, False)
		szText = CyTranslator().getText("TXT_KEY_MINOR_EVENT_JEWS", (city.getName(), ))
		CyInterface().addMessage(city.getOwner(), False, con.iDuration, szText, "AS2D_BUILD_JEWISH", InterfaceMessageTypes.MESSAGE_TYPE_MAJOR_EVENT, gc.getReligionInfo(con.iJudaism).getButton(), ColorTypes(con.iWhite), city.getX(), city.getY(), True, True)
	
	return 1

####### Persian Rugs (edead) #######
	
def canTriggerPersianRugsCity(argsList):
	eTrigger = argsList[0]
	ePlayer = argsList[1]
	iCity = argsList[2]
	
	player = gc.getPlayer(ePlayer)
	city = player.getCity(iCity)
	
	if city.isNone():
		return false

	if city.plot().getRegionID() in [con.rPersia, con.rMedia, con.rParthia, con.rArachosia]:
		return true
	
	return false

####### Confectioners (edead) #######
	
def canTriggerConfectionersCity(argsList):
	eTrigger = argsList[0]
	ePlayer = argsList[1]
	iCity = argsList[2]
	
	player = gc.getPlayer(ePlayer)
	city = player.getCity(iCity)
	
	if city.isNone():
		return false

	if city.plot().getRegionID() in [con.rSyria, con.rMesopotamia]:
		return true
	
####### Camel Races (edead) #######
	
def canTriggerCamelRacesCity(argsList):
	eTrigger = argsList[0]
	ePlayer = argsList[1]
	iCity = argsList[2]
	
	player = gc.getPlayer(ePlayer)
	city = player.getCity(iCity)
	
	if city.isNone():
		return false

	if city.getOwner() not in [con.iEgypt, con.iAxum, con.iNubia, con.iSaba, con.iArabs]:
		return false
		
	if city.plot().getRegionID() not in [con.rArabia]:
		return false
	
	return true

####### Bickering Factions (edead) #######

def applyBickeringFactions1(argsList):
	kTriggeredData = argsList[1]
	sd.changePiety(kTriggeredData.ePlayer, 5)
	CvMainInterface().updateGameDataStrings()

def applyBickeringFactions2(argsList):
	kTriggeredData = argsList[1]
	iPlayer = kTriggeredData.ePlayer
	#sd.setStability(iPlayer, sd.getStability(iPlayer) + 2)
	#if iPlayer == utils.getHumanID():
		#utils.setParameter(iPlayer, con.iParCitiesE, True, 2)

def getHelpBickeringFactions1(argsList):
	szHelp = localText.getText("TXT_KEY_EVENT_HELP_BICKERING_FACTIONS_1", (5, ))
	return szHelp

def getHelpBickeringFactions2(argsList):
	szHelp = localText.getText("TXT_KEY_EVENT_HELP_BICKERING_FACTIONS_2", (2, ))
	return szHelp

####### Peasant Revolt (edead) #######

def applyPeasantRevolt1(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	plot = gc.getMap().plot(kTriggeredData.iPlotX, kTriggeredData.iPlotY)
	
	return
	
	'''if kTriggeredData.ePlayer in [con.iRome, con.iFranks, con.iArmenia]:
		if gc.getGame().getSorenRandNum(2, "Peasant revolt unit spawn") != 0:
			return
	
	listPlots = []
	for i in range(5):
		for j in range(5):
			loopPlot = gc.getMap().plot(kTriggeredData.iPlotX + i - 2, kTriggeredData.iPlotY + j - 2)
			if None != loopPlot and not loopPlot.isNone() and not loopPlot.isCity():
				if not (loopPlot.isVisibleEnemyUnit(kTriggeredData.ePlayer) or loopPlot.isWater() or loopPlot.isImpassable()):
					listPlots.append(loopPlot)
	
	if len(listPlots) > 0:
		iPlot = gc.getGame().getSorenRandNum(len(listPlots), "Partisan event placement")
		gc.getPlayer(con.iBarbarian).initUnit(con.iPeasant, listPlots[iPlot].getX(), listPlots[iPlot].getY(), UnitAITypes.UNITAI_PILLAGE, DirectionTypes.DIRECTION_SOUTH)'''
		
####### Massacre of the Latins & the Fourth Crusade (edead) #######

def canTriggerMassacreOfTheLatinsCity(argsList):
	eTrigger = argsList[0]
	ePlayer = argsList[1]
	iCity = argsList[2]
	
	return False
	
	'''player = gc.getPlayer(ePlayer)
	city = player.getCity(iCity)
	
	if city.isNone():
		return false

	if city.getOwner() != con.iRome:
		return false
		
	if utils.getYear() < 1120 or utils.getYear() > 1195:
		return false
	
	return true'''

def getHelpMassacreOfTheLatins1(argsList):
	return localText.getText("TXT_KEY_EVENT_HELP_MASSACRE_OF_THE_LATINS_1", ())
	
def getHelpMassacreOfTheLatins2(argsList):
	return localText.getText("TXT_KEY_EVENT_HELP_MASSACRE_OF_THE_LATINS_2", ())
	
def applyMassacreOfTheLatins1(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	
	sd.setVal('iLatinMassacreTurn', gc.getGame().getGameTurn())
	sd.setVal('iFourthCrusadeYear', 1192 + gc.getGame().getSorenRandNum(29, 'Fourth crusade date'))
	player = gc.getPlayer(kTriggeredData.ePlayer)
	(loopCity, iter) = player.firstCity(false)
	while(loopCity):
		if loopCity.isHasCorporation(con.iGenoans):
			loopCity.setHasCorporation(con.iGenoans, False, True, True)
		if loopCity.isHasCorporation(con.iVenetians):
			loopCity.setHasCorporation(con.iVenetians, False, True, True)
		(loopCity, iter) = player.nextCity(iter, false)

def applyMassacreOfTheLatins2(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	
	player = gc.getPlayer(kTriggeredData.ePlayer)
	(loopCity, iter) = player.firstCity(false)
	while(loopCity):
		iNumRevoltTurns = 0
		if loopCity.isCapital() or loopCity.isHasCorporation(con.iVenetians) or loopCity.isHasCorporation(con.iGenoans):
			iNumRevoltTurns += 1 + gc.getGame().getSorenRandNum(2, 'Revolt turns')
		if loopCity.isCoastal(20):
			iNumRevoltTurns += gc.getGame().getSorenRandNum(3, 'Revolt turns again')
		if loopCity.isCapital() or loopCity.isCoastal(20):
			loopCity.changeHurryAngerTimer(loopCity.flatHurryAngerLength())
			if loopCity.isHasCorporation(con.iGenoans):
				loopCity.setHasCorporation(con.iGenoans, False, True, True)
		loopCity.changeCultureUpdateTimer(iNumRevoltTurns)
		loopCity.changeOccupationTimer(iNumRevoltTurns)
		(loopCity, iter) = player.nextCity(iter, false)
	
def canTriggerFourthCrusade(argsList):
	kTriggeredData = argsList[0]

	if kTriggeredData.ePlayer != con.iRome:
		return false
	
	if not sd.getVal('iLatinMassacreTurn'):
		return false
	
	if gc.getMap().plot(con.tConstantinople[0], con.tConstantinople[1]).getOwner() != con.iRome:
		return false
	
	return true

def canTriggerFourthCrusadeCity(argsList):
	eTrigger = argsList[0]
	ePlayer = argsList[1]
	iCity = argsList[2]
	
	player = gc.getPlayer(ePlayer)
	city = player.getCity(iCity)
	
	if city.isNone():
		return false

	if city.getOwner() != con.iRome:
		return false
		
	if city.getX() != con.tConstantinople[0] or city.getY() != con.tConstantinople[1]:
		return false
	
	return true
	
def applyFourthCrusade1(argsList):
	kTriggeredData = argsList[0]
	
	# move out all units to make space for crusader spawn
	city = gc.getMap().plot(con.tConstantinople[0], con.tConstantinople[1]).getPlotCity()
	plot = gc.getMap().plot(con.tConstantinople[0] - 1, con.tConstantinople[1])
	if utils.getHumanID() == con.iRome:
		plot.cameraLookAt()
	
	for i in range(plot.getNumUnits()):
		unit = plot.getUnit(0)
		if unit.getOwner() == city.getOwner():
			unit.setXY(con.tConstantinople[0], con.tConstantinople[1], False, False, False)
		else:
			unit.setXY(con.tConstantinople[0] - 1, con.tConstantinople[1] + 1, False, False, False)
	plot = gc.getMap().plot(con.tConstantinople[0] - 1, con.tConstantinople[1] - 1)
	for i in range(plot.getNumUnits()):
		unit = plot.getUnit(0)
		if unit.getOwner() == city.getOwner():
			unit.setXY(con.tConstantinople[0], con.tConstantinople[1], False, False, False)
		else:
			unit.setXY(con.tConstantinople[0] - 2, con.tConstantinople[1], False, False, False)
	
	# declare war between indeps & byzantium
	if not gc.getTeam(gc.getPlayer(con.iIndependent).getTeam()).isAtWar(con.iRome):
		gc.getTeam(gc.getPlayer(con.iIndependent).getTeam()).declareWar(con.iRome, False, WarPlanTypes.WARPLAN_LIMITED)

	# spawn the crusaders
	iHandicap = gc.getGame().getHandicapType() - 1
	tPlot = (con.tConstantinople[0] - 1, con.tConstantinople[1])
	tSeaPlot = (con.tConstantinople[0] - 1, con.tConstantinople[1] - 1)
	utils.makeUnit(con.iWarGalley, con.iIndependent, tSeaPlot, 2 + iHandicap, UnitAITypes.NO_UNITAI, [con.iCombat1])
	utils.makeUnit(con.iTrebuchet, con.iIndependent, tPlot, 2 + iHandicap, UnitAITypes.NO_UNITAI, [con.iAccuracy, con.iCityRaider1])
	utils.makeUnit(con.iItalianMaceman, con.iIndependent, tPlot, 1, UnitAITypes.NO_UNITAI, [con.iCityRaider1])
	utils.makeUnit(con.iFootKnight, con.iIndependent, tPlot, 3 + iHandicap, UnitAITypes.NO_UNITAI, [con.iCityRaider1])
	utils.makeUnit(con.iItalianCrossbowman, con.iIndependent, tPlot, 1, UnitAITypes.NO_UNITAI, [con.iDrill1, con.iDrill2])
	pLeader = utils.makeUnit(con.iFootKnight, con.iIndependent, tPlot, 1, UnitAITypes.NO_UNITAI, [con.iCityRaider1, con.iCityRaider2])
	pLeader.setHasPromotion(con.iLeader, True)
	pLeader.setExperience(20, -1)
	pLeader.setLeaderUnitType(con.iGreatGeneral2)
	pLeader.setName('Boniface of Montferrat')
	
	# save turn info
	sd.setVal('iFourthCrusadeTurn', gc.getGame().getGameTurn())
	
	return true
	
### MANSA MUSA ###
	
def canTriggerMansaMusa(argsList):
	kTriggeredData = argsList[0]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	
	if kTriggeredData.ePlayer not in [con.iEgypt, con.iNubia, con.iAxum]:
		return false
	
	if gc.getGame().getGameTurnYear() < 1300:
		return false

	if gc.getGame().getGameTurnYear() > 1400:
		return false

	if kTriggeredData.ePlayer != gc.getMap().plot(con.tAlexandria[0], con.tAlexandria[1]).getOwner():
		return false
		
	return true

### AUTONOMY ###

# def canTriggerAutonomyCity(argsList):
	# eTrigger = argsList[0]
	# ePlayer = argsList[1]
	# iCity = argsList[2]
	
	# player = gc.getPlayer(ePlayer)
	# city = player.getCity(iCity)
	
	# if city.isNone():
		# return false
	
	# if city.isCapital():
		# return false
	
	# if city.plot().getRegionID() in utils.getCoreRegions(ePlayer):
		# return false
	
	# if city.plot().getRegionID() in utils.getNormalRegions(ePlayer):
		# return false
	
	# return true

### RELIGIOUS LAW ###
	
def canTriggerReligiousLaw(argsList):
	kTriggeredData = argsList[0]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	team = gc.getTeam(player.getTeam())
	
	if player.getStateReligion() not in [con.iIslam]:
		return false
	
	if not team.isHasTech(con.iEducation):
		return false
	
	if player.getCivics(1) == con.iReligiousLawCivic:
		return false
	
	return true

def applyReligiousLaw1(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	
	player.setCivics(1, con.iReligiousLawCivic)
	player.changeRevolutionTimer(gc.getDefineINT("MIN_REVOLUTION_TURNS"))

def getHelpReligiousLaw1(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	
	szHelp = localText.getText("TXT_KEY_EVENT_HELP_RELIGIOUS_LAW_1", ())

	return szHelp

def applyReligiousLaw2(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	
	sd.changePiety(kTriggeredData.ePlayer, -(10 + gc.getGame().getSorenRandNum(10, "Random piety loss")))
	CvMainInterface().updateGameDataStrings()

def getHelpReligiousLaw2(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	
	szHelp = localText.getText("TXT_KEY_EVENT_HELP_RELIGIOUS_LAW_2", ())

	return szHelp

### CASTE SYSTEM ###
	
def canTriggerCasteSystem(argsList):
	kTriggeredData = argsList[0]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	team = gc.getTeam(player.getTeam())
	
	if player.getStateReligion() != con.iHinduism:
		return false
	
	if not team.isHasTech(con.iCasteSystem):
		return false
	
	if player.getCivics(2) == con.iCasteSystemCivic:
		return false
	
	return true

def applyCasteSystem1(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	
	player.setCivics(2, con.iCasteSystemCivic)
	player.changeRevolutionTimer(gc.getDefineINT("MIN_REVOLUTION_TURNS"))

def getHelpCasteSystem1(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	
	szHelp = localText.getText("TXT_KEY_EVENT_HELP_CASTE_SYSTEM_1", ())

	return szHelp

def applyCasteSystem2(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	
	sd.changePiety(kTriggeredData.ePlayer, -(10 + gc.getGame().getSorenRandNum(10, "Random piety loss")))
	CvMainInterface().updateGameDataStrings()

def getHelpCasteSystem2(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	
	szHelp = localText.getText("TXT_KEY_EVENT_HELP_CASTE_SYSTEM_2", ())

	return szHelp

### HAJJ ###

def canTriggerHajj(argsList):
	kTriggeredData = argsList[0]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	
	if gc.getGame().getGameTurnYear() < 900:
		return false
	
	if player.getStateReligion() not in [con.iIslam]:
		return false
	
	if sd.getPiety(kTriggeredData.ePlayer) > 90:
		return false
	
	return true

def applyHajj1(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	
	sd.changePiety(kTriggeredData.ePlayer, 5)
	CvMainInterface().updateGameDataStrings()

def getHelpHajj1(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	
	szHelp = localText.getText("TXT_KEY_EVENT_HELP_HAJJ_1", (5,))

	return szHelp

def applyHajj2(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	
	sd.changePiety(kTriggeredData.ePlayer, (10 + gc.getGame().getSorenRandNum(10, "Random piety gain")))
	CvMainInterface().updateGameDataStrings()

def getHelpHajj2(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	
	szHelp = localText.getText("TXT_KEY_EVENT_HELP_HAJJ_2", (10, 20))

	return szHelp

def applyHajj3(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	
	sd.changePiety(kTriggeredData.ePlayer, -10)
	CvMainInterface().updateGameDataStrings()

def getHelpHajj3(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	
	szHelp = localText.getText("TXT_KEY_EVENT_HELP_HAJJ_3", (10,))

	return szHelp

### RELIGIOUS SUPPORTERS ###

def canTriggerReligiousSupporters(argsList):
	kTriggeredData = argsList[0]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	
	if gc.getGame().getGameTurnYear() < 900 or gc.getGame().getGameTurnYear() > 1250:
		return false
	
	if player.getStateReligion() not in [con.iIslam, con.iHinduism, con.iChristianity]:
		return false
	
	if sd.getPiety(kTriggeredData.ePlayer) < 60:
		return false
	
	return true

def applyReligiousSupporters1(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	
	iStateReligion = player.getStateReligion()
	unitList = []
	if iStateReligion == con.iIslam:
		unitList = [con.iSwordsman, con.iSpearman, con.iArcher]
	elif iStateReligion == con.iChristianity:
		unitList = [con.iSwordsman, con.iSpearman, con.iArcher]
	elif iStateReligion == con.iHinduism:
		unitList = [con.iSwordsman, con.iAxeman]
	plot = gc.getMap().plot(kTriggeredData.iPlotX, kTriggeredData.iPlotY)
	iNumUnits = 1 + gc.getGame().getSorenRandNum(max(1, (sd.getPiety(kTriggeredData.ePlayer) - 66) / 10), "Random number of units")
	for iLoopUnit in range(iNumUnits):
		iUnitType = unitList[gc.getGame().getSorenRandNum(len[unitList], "Random unit type")]
		player.initUnit(iUnitType, plot.getX(), plot.getY(), UnitAITypes.UNITAI_ATTACK, DirectionTypes.DIRECTION_SOUTH)