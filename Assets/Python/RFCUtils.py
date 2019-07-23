# Rhye's and Fall of Civilization - Utilities

from CvPythonExtensions import *
import CvUtil
import CvScreenEnums
import PyHelpers
import Popup
import Consts as con
import UnitArtStyler
import re
from StoredData import sd
from random import shuffle
from operator import itemgetter

# globals
gc = CyGlobalContext()
localText = CyTranslator()
ArtFileMgr = CyArtFileMgr()
PyPlayer = PyHelpers.PyPlayer

iNumPlayers = con.iNumPlayers
iNumMinorPlayers = con.iNumMinorPlayers
iNumTotalPlayers = con.iBarbarian
iMapHeight = con.iMapHeight
iMapWidth = con.iMapWidth
iNumReligions = con.iNumReligions

tCol = (
'255,255,255',
'200,200,200',
'150,150,150',
'128,128,128')

class RFCUtils:

	bStabilityOverlay = False

	#Rise and fall, stability
	def getLastTurnAlive( self, iCiv ):
		return sd.getLastTurnAlive(iCiv)

	def setLastTurnAlive( self, iCiv, iNewValue ):
		sd.setLastTurnAlive(iCiv, iNewValue)

	#Victory
	def getGoal( self, i, j ):
		return sd.getGoal(i, j)

	def setGoal( self, i, j, iNewValue ):
		sd.setGoal(i, j, iNewValue)

	#Flipping
	def getTempFlippingCity( self ):
		return sd.getTempFlippingCity()

	def setTempFlippingCity( self, tNewValue ):
		sd.setTempFlippingCity(tNewValue)

	#Plague
	def getPlagueCountdown( self, iCiv ):
		return sd.getPlagueCountdown(iCiv)

	def setPlagueCountdown( self, iCiv, iNewValue ):
		sd.setPlagueCountdown(iCiv, iNewValue)



	# edead: Dynamic Civ Names
	def getCivilization(self, iCiv):
		return sd.getCivilization(iCiv)

	def setCivilization(self, iCiv, iNewValue):
		sd.setCivilization(iCiv, iNewValue)

	# edead: Traits/UPs
	def getNumCrusades(self):
		return sd.getNumCrusades()

	def setNumCrusades(self, iNewValue):
		sd.setNumCrusades(iNewValue)

	def isHasLostCity(self, iCiv):
		return sd.isHasLostCity(iCiv)

	def setHasLostCity(self, iCiv, iNewValue):
		sd.setHasLostCity(iCiv, iNewValue)

	def getLastCrusadeTurn(self, iCiv):
		return sd.getLastCrusadeTurn(iCiv)

	def setLastCrusadeTurn(self, iCiv, iNewValue):
		sd.setLastCrusadeTurn(iCiv, iNewValue)

	def getSeed( self ):
		return sd.getSeed()
	
	def getRandomCivList( self ):
		return sd.getRandomCivList()

#######################################

	# Stability, RiseNFall, CvFinanceAdvisor
	def setParameter(self, iPlayer, iParameter, bPreviousAmount, iAmount):
		if (gc.getPlayer(iPlayer).isHuman()):
			if (bPreviousAmount):
				self.setStabilityParameters(iParameter, self.getStabilityParameters(iParameter) + iAmount)
			else:
				self.setStabilityParameters(iParameter, 0 + iAmount)


	def setStartingStabilityParameters(self, iCiv):
		
		iHandicap = gc.getGame().getHandicapType()
		
		for i in range(con.iNumStabilityParameters):
			self.setStabilityParameters(i, 0)
		
		if (iHandicap == 0):
			self.setStability(iCiv, 20)
			self.setParameter(iCiv, con.iParCitiesE, True, 4)
			self.setParameter(iCiv, con.iParCivicsE, True, 4)
			self.setParameter(iCiv, con.iParDiplomacyE, True, 4)
			self.setParameter(iCiv, con.iParEconomyE, True, 4)
			self.setParameter(iCiv, con.iParExpansionE, True, 4) 
		elif (iHandicap == 1):
			self.setStability(iCiv, 5)
			self.setParameter(iCiv, con.iParCitiesE, True, 1)
			self.setParameter(iCiv, con.iParCivicsE, True, 1)
			self.setParameter(iCiv, con.iParDiplomacyE, True, 1)
			self.setParameter(iCiv, con.iParEconomyE, True, 1)
			self.setParameter(iCiv, con.iParExpansionE, True, 1) 
		elif (iHandicap == 2):
			self.setStability(iCiv, -10)
			self.setParameter(iCiv, con.iParCitiesE, True, -2)
			self.setParameter(iCiv, con.iParCivicsE, True, -2)
			self.setParameter(iCiv, con.iParDiplomacyE, True, -2)
			self.setParameter(iCiv, con.iParEconomyE, True, -2)
			self.setParameter(iCiv, con.iParExpansionE, True, -2) 


	# CvFinanceAdvisor
	def getParCities(self):
		if (self.getStabilityParameters(con.iParCitiesE) > 7):
			return self.getStabilityParameters(con.iParCities3) + self.getStabilityParameters(con.iParCitiesE) - gc.getActivePlayer().getCurrentEra()
		elif (self.getStabilityParameters(con.iParCitiesE) < -7):
			return self.getStabilityParameters(con.iParCities3) + self.getStabilityParameters(con.iParCitiesE) + gc.getActivePlayer().getCurrentEra()
		else:
			return self.getStabilityParameters(con.iParCities3) + self.getStabilityParameters(con.iParCitiesE)


	def getParCivics(self):
		if (self.getStabilityParameters(con.iParCivicsE) > 7):
			return self.getStabilityParameters(con.iParCivics3) + self.getStabilityParameters(con.iParCivics1) + self.getStabilityParameters(con.iParCivicsE) - gc.getActivePlayer().getCurrentEra()
		elif (self.getStabilityParameters(con.iParCivicsE) < -7):
			return self.getStabilityParameters(con.iParCivics3) + self.getStabilityParameters(con.iParCivics1) + self.getStabilityParameters(con.iParCivicsE) + gc.getActivePlayer().getCurrentEra()
		else:
			return self.getStabilityParameters(con.iParCivics3) + self.getStabilityParameters(con.iParCivics1) + self.getStabilityParameters(con.iParCivicsE)


	def getParDiplomacy(self):
		if (self.getStabilityParameters(con.iParDiplomacyE) > 7):
			return self.getStabilityParameters(con.iParDiplomacy3) + self.getStabilityParameters(con.iParDiplomacyE) - gc.getActivePlayer().getCurrentEra()
		elif (self.getStabilityParameters(con.iParDiplomacyE) < -7):
			return self.getStabilityParameters(con.iParDiplomacy3) + self.getStabilityParameters(con.iParDiplomacyE) + gc.getActivePlayer().getCurrentEra()
		else:
			return self.getStabilityParameters(con.iParDiplomacy3) + self.getStabilityParameters(con.iParDiplomacyE)


	def getParEconomy(self):
		if (self.getStabilityParameters(con.iParEconomyE) > 7):
			return self.getStabilityParameters(con.iParEconomy3) + self.getStabilityParameters(con.iParEconomy1) + self.getStabilityParameters(con.iParEconomyE) - gc.getActivePlayer().getCurrentEra()
		elif (self.getStabilityParameters(con.iParEconomyE) < -7):
			return self.getStabilityParameters(con.iParEconomy3) + self.getStabilityParameters(con.iParEconomy1) + self.getStabilityParameters(con.iParEconomyE) + gc.getActivePlayer().getCurrentEra()
		else:
			return self.getStabilityParameters(con.iParEconomy3) + self.getStabilityParameters(con.iParEconomy1) + self.getStabilityParameters(con.iParEconomyE)


	def getParExpansion(self):
		if (self.getStabilityParameters(con.iParExpansionE) > 7):
			return self.getStabilityParameters(con.iParExpansion3) + self.getStabilityParameters(con.iParExpansion1) + self.getStabilityParameters(con.iParExpansionE) - gc.getActivePlayer().getCurrentEra()
		elif (self.getStabilityParameters(con.iParExpansionE) < -7):
			return self.getStabilityParameters(con.iParExpansion3) + self.getStabilityParameters(con.iParExpansion1) + self.getStabilityParameters(con.iParExpansionE) + gc.getActivePlayer().getCurrentEra()
		else:
			return self.getStabilityParameters(con.iParExpansion3) + self.getStabilityParameters(con.iParExpansion1) + self.getStabilityParameters(con.iParExpansionE)


	def getArrow(self, iParameter):
		if (iParameter == 0):
			if (self.getStability(self.getHumanID()) >= self.getLastRecordedStabilityStuff(iParameter) + 6):
				return 1
			elif (self.getStability(self.getHumanID()) <= self.getLastRecordedStabilityStuff(iParameter) - 6):
				return -1
			else:
				return 0
		else:
			if (iParameter == 1):
				iNewValue = self.getParCities()
			elif (iParameter == 2):
				iNewValue = self.getParCivics()
			elif (iParameter == 3):
				iNewValue = self.getParEconomy()
			elif (iParameter == 4):
				iNewValue = self.getParExpansion()
			elif (iParameter == 5):
				iNewValue = self.getParDiplomacy()
			if (iNewValue >= self.getLastRecordedStabilityStuff(iParameter) + 4):
				return 1
			elif (iNewValue <= self.getLastRecordedStabilityStuff(iParameter) - 4):
				return -1
			else:
				return 0


	#Victory
	def countAchievedGoals(self, iPlayer):
		iResult = 0
		for j in range(3):                        
			#iTemp = self.getGoal(iPlayer, j)
			#if (iTemp < 0):
			#        iTemp = 0
			#iResult += iTemp
			if (self.getGoal(iPlayer, j) == 1):
					iResult += 1
		return iResult

	def getGoalsColor(self, iPlayer): #by CyberChrist
		iCol = 0
		for j in range(3):
			if (self.getGoal(iPlayer, j) == 0):
				iCol += 1
		return tCol[iCol]


	def showPopup(self, popupID, title, message, labels):
		"""popupID has to be a registered ID in CvRhyesCatapultEventManager.__init__!"""
		
		popup = Popup.PyPopup(popupID, EventContextTypes.EVENTCONTEXT_ALL)
		popup.setHeaderString(title)
		popup.setBodyString(message)
		for i in labels:
			popup.addButton(i)
		popup.launch(False)


	def getYear(self):
		return gc.getGame().getGameTurnYear()


	def getTurns(self, turns):
			"""Returns the amount of turns modified adequately for the game's speed.
			Values are based on CIV4GameSpeedInfos.xml. Use this only for durations, intervals etc.; 
			for year->turn conversions, use the DLL function getTurnForYear(int year)."""
			iGameSpeed = gc.getGame().getGameSpeedType()
			if iGameSpeed == 1: return turns # normal
			elif iGameSpeed == 0: # epic
					if turns == 3: return 5 # getTurns(6) must be a multiple of getTurns(3) for turn divisors in Stability.py
					elif turns == 6: return 10
					else: return turns*3/2
			#elif iGameSpeed == 0: return turns*3 # marathon
			#elif iGameSpeed == 3: return turns*2/3 # quick
			return turns


	def isActive(self, iPlayer):
		"""Returns true if the player is spawned and alive."""
		
		if gc.getPlayer(iPlayer).getNumCities() < 1: 
			return False
		if not gc.getPlayer(iPlayer).isAlive: return False
		if self.getYear() < con.tBirth[iPlayer]: return False
		return True
		
	# Leoreth - finds an adjacent land plot without enemy units that's closest to the player's capital (for the Roman UP)
	def findNearestLandPlot(self, tPlot, iPlayer):
		x, y = tPlot
		plotList = []

		for i in range(x - 2, x + 3):        
			for j in range(y - 2, y + 3):	
				pCurrent = gc.getMap().plot( i, j )
				if (not pCurrent.isWater() and not pCurrent.isPeak() and pCurrent.getFeatureType() not in [con.iForest, con.iMarsh, con.iJungle, con.iDenseForest, con.iIce]):
					if ( not pCurrent.isUnit() ):
						plotList.append(pCurrent)
												
		if (len(plotList) > 0):
			rndNum = gc.getGame().getSorenRandNum(len(plotList), 'land plot')
			result = plotList[rndNum]
			if (result):                                                        
				return ((result.getX(), result.getY()))
		# if no plot is found, return that player's capital
		elif (len(plotList) == 0):
			return con.tCapitals[iPlayer]										


	# from SdToolkit
	def echo(self, echoString):
		printToScr = True
		printToLog = True
		message = "%s" %(echoString)
		if (printToScr):
			CyInterface().addImmediateMessage(message,"")
		if (printToLog):
			CvUtil.pyPrint(message)
		return 0

		
	def getCoreRegions(self, iCiv):
		result = []
		#if sd.getCivilization(iCiv) != iCiv:
			#result.extend(con.lRespawnRegions[iCiv])
		#else:
		result.extend(con.lCoreRegions[iCiv])
		return result
		
	def getTargetRegions(self, iCiv):
		result = []
		#if sd.getCivilization(iCiv) != iCiv:
			#result.extend(con.lTargetRegions[iCiv])
		#else:
		result.extend(con.lTargetRegions[iCiv])
		return result

		
	def getNormalRegions(self, iCiv):
		result = []
		#if sd.getCivilization(iCiv) != iCiv:
			#result.extend(con.lRespawnNormalRegions[iCiv])
		#else:
		result.extend(con.lNormalRegions[iCiv])
		return result
		
		
	def getBroaderRegions(self, iCiv):
		result = []
		#if sd.getCivilization(iCiv) != iCiv:
			#result.extend(con.lRespawnBroaderRegions[iCiv])
		#else: 
		result.extend(con.lBroaderRegions[iCiv])
		#if gc.getTeam(gc.getPlayer(iCiv).getTeam()).getProjectCount(con.iRaja) > 0 and gc.getPlayer(iCiv).getStateReligion() == con.iHinduism:
			#result.extend(con.lTitleRegions[con.iRaja])
			#self.uniq(result)
		return result
		
	def getSpecialRegions(self, iCiv):
		result = []
		#if sd.getCivilization(iCiv) != iCiv:
			#result.extend(con.lSpecialRegions[iCiv])
		#else:
		result.extend(con.lSpecialRegions[iCiv])
		return result

	
	# Temp function for compatibility with some RFC routines
	def getAreaPlotList(self, tTopLeft, tBottomRight):
		"""Converts the RFC-style rectangular area to a list of tuples."""
		
		plotList = []
		for x in range(tTopLeft[0], tBottomRight[0]+1):
			for y in range(tTopLeft[1], tBottomRight[1]+1):
				if x >= 0 and x < iMapWidth and y >= 0 and y < iMapHeight:
					plotList.append((x, y))
		
		return plotList

		
		
	def getRegionPlotList(self, lRegions, bBorder = False):
		"""Returns a list of all plots in listed regions, optionally with borders for visible coastline."""
		
		plotList = []
		for x in range(con.iMapWidth):
			for y in range(con.iMapHeight):
				if gc.getMap().plot(x, y).getRegionID() in lRegions:
					if not bBorder:
						plotList.append((x, y))
					else:
						for x2 in range(x-1, x+2):
							for y2 in range(y-1, y+2):
								if (x2, y2) not in plotList: plotList.append((x2, y2))
		
		return plotList


	def getCorePlotList(self, iCiv, bBorder = False):
		"""Returns a list of all plots in core regions."""

		return self.getRegionPlotList(self.getCoreRegions(iCiv), bBorder)


	def getNormalPlotList(self, iCiv, bBorder = False):
		"""Returns a list of all plots in core + normal regions."""
		
		return self.getRegionPlotList(self.getCoreRegions(iCiv) + self.getNormalRegions(iCiv), bBorder)


	def getBroaderPlotList(self, iCiv, bBorder = False):
		"""Returns a list of all plots in core + normal + broader regions."""
		
		return self.getRegionPlotList(self.getCoreRegions(iCiv) + self.getNormalRegions(iCiv) + self.getBroaderRegions(iCiv), bBorder)
		
	def getSpecialPlotList(self, iCiv, bBorder = False):
		"""Returns a list of all plots in special regions."""

		return self.getRegionPlotList(self.getSpecialRegions(iCiv), bBorder)


	def coverPlots(self, plotX, plotY, iCiv):
		"""Covers the plots revealed by RFC catapult and flipped units."""
		
		for x in range(plotX-1, plotX+2):
			for y in range(plotY-1, plotY+2):
				gc.getMap().plot(x, y).setRevealed(iCiv, False, True, -1);

				
	def revealPlots(self, iCiv, plotList):
		"""Reveals all plots on the list."""
		
		iTeam = gc.getPlayer(iCiv).getTeam()
		for i in range(len(plotList)):
			gc.getMap().plot(plotList[i][0], plotList[i][1]).setRevealed(iTeam, True, False, -1)

				
	def revealMap(self, iCiv):
		"""Reveals all plots."""
		
		iTeam = gc.getPlayer(iCiv).getTeam()
		for x in range(con.iMapWidth):
			for y in range(con.iMapHeight):
				gc.getMap().plot(x, y).setRevealed(iTeam, True, False, -1)

				
	def unrevealPlots(self, iCiv, plotList):
		"""Reveals all plots on the list."""
		
		for i in range(len(plotList)):
			gc.getMap().plot(plotList[i][0], plotList[i][1]).setRevealed(iCiv, False, True, -1)


	def revealCity(self, iCiv, tCoords):
		"""Reveals the specified city plot and its fat cross."""
		
		iTeam = gc.getPlayer(iCiv).getTeam()
		for x in range(tCoords[0]-2, tCoords[0]+3):
			for y in range(tCoords[1]-2, tCoords[1]+3):
				gc.getMap().plot(x, y).setRevealed(iTeam, True, False, -1)
				

	def getRegionStabilityLevel(self, iPlayer, iRegionID):
		"""Returns stability level for the given region."""
		
		iCiv = sd.getCivilization(iPlayer)
		
		if iRegionID in con.lCoreRegions[iCiv]:
			return 4 # core
		elif iRegionID in self.getNormalRegions(iCiv):
			for iLoopCiv in range(con.iNumPlayers):
				if iLoopCiv != iCiv and iRegionID in self.getCoreRegions(iLoopCiv):
					if gc.getGame().getGameTurn() >= getTurnForYear(con.tBirth[iLoopCiv]) and gc.getGame().getGameTurn() <= getTurnForYear(con.tFall[iLoopCiv]):
						return 2 # contested
			return 3 # border
		else:
			for iLoopCiv in range(con.iNumPlayers):
				if iLoopCiv != iCiv and iRegionID in self.getCoreRegions(iLoopCiv):
					if gc.getGame().getGameTurn() >= getTurnForYear(con.tBirth[iLoopCiv]) and gc.getGame().getGameTurn() <= getTurnForYear(con.tFall[iLoopCiv]):
						return 0 # foreign
			return 1 # none


	def getRandomMinorCiv(self):
		"""Returns a random minor civilization."""
		
		return con.iIndependent + gc.getGame().getSorenRandNum(iNumMinorPlayers, 'Random minor civilization')





# RFCUtils

	#AIWars
	def checkUnitsInEnemyTerritory(self, iCiv1, iCiv2): 
		unitList = PyPlayer(iCiv1).getUnitList()
		if(len(unitList)):
			for unit in unitList:
				iX = unit.getX()
				iY = unit.getY()
				if (gc.getMap().plot( iX, iY ).getOwner() == iCiv2):
					return True
			return False


	#AIWars
	def restorePeaceAI(self, iMinorCiv, bOpenBorders):
		teamMinor = gc.getTeam(gc.getPlayer(iMinorCiv).getTeam())
		for iActiveCiv in range( iNumPlayers ):
			if (gc.getPlayer(iActiveCiv).isAlive() and not gc.getPlayer(iActiveCiv).isHuman()):
				if (teamMinor.isAtWar(iActiveCiv)):
					bActiveUnitsInIndependentTerritory = self.checkUnitsInEnemyTerritory(iActiveCiv, iMinorCiv)
					bIndependentUnitsInActiveTerritory = self.checkUnitsInEnemyTerritory(iMinorCiv, iActiveCiv)
					if (not bActiveUnitsInIndependentTerritory and not bIndependentUnitsInActiveTerritory):
						teamMinor.makePeace(iActiveCiv)
						#print ("Minor peace", gc.getPlayer(iActiveCiv).getCivilizationAdjective(0))
						if (bOpenBorders):
							teamMinor.signOpenBorders(iActiveCiv)


	#AIWars
	def restorePeaceHuman(self, iMinorCiv, bOpenBorders): 
		teamMinor = gc.getTeam(gc.getPlayer(iMinorCiv).getTeam())
		for iActiveCiv in range( iNumPlayers ):
			if (gc.getPlayer(iActiveCiv).isHuman()):
				if (gc.getPlayer(iActiveCiv).isAlive()):
					if (teamMinor.isAtWar(iActiveCiv)):
						bActiveUnitsInIndependentTerritory = self.checkUnitsInEnemyTerritory(iActiveCiv, iMinorCiv)
						bIndependentUnitsInActiveTerritory = self.checkUnitsInEnemyTerritory(iMinorCiv, iActiveCiv)
						if (not bActiveUnitsInIndependentTerritory and not bIndependentUnitsInActiveTerritory):
							teamMinor.makePeace(iActiveCiv)
					return


	#AIWars
	def minorWars(self, iMinorCiv):
		teamMinor = gc.getTeam(gc.getPlayer(iMinorCiv).getTeam())
		apCityList = PyPlayer(iMinorCiv).getCityList()
		for pCity in apCityList:
			city = pCity.GetCy()
			x = city.getX()
			y = city.getY()
			for iActiveCiv in range( iNumPlayers ):
				if gc.getPlayer(iActiveCiv).isAlive() and not gc.getPlayer(iActiveCiv).isHuman():
					regionList = []
					regionList.extend(self.getCoreRegions(sd.getCivilization(iActiveCiv)))
					regionList.extend(self.getNormalRegions(sd.getCivilization(iActiveCiv)))
					#regionList.extend(self.getBroaderRegions(sd.getCivilization(iActiveCiv)))
					if gc.getMap().plot(x, y).getRegionID() in regionList:
						if (not teamMinor.isAtWar(iActiveCiv)):
							teamMinor.declareWar(iActiveCiv, False, WarPlanTypes.WARPLAN_LIMITED)
							#print ("Minor war", city.getName(), gc.getPlayer(iActiveCiv).getCivilizationAdjective(0))


	# RiseAndFall, Stability
	def calculateDistance(self, x1, y1, x2, y2):
		dx = abs(x2-x1)
		dy = abs(y2-y1)
		return max(dx, dy)


	# RiseAndFall
	def updateMinorTechs(self, iMinorCiv, iMajorCiv):
		"""Gives all techs of iMajorCiv to iMinorCiv."""
		
		for t in range(con.iNumTechs):
			if (gc.getTeam(gc.getPlayer(iMajorCiv).getTeam()).isHasTech(t)):
				gc.getTeam(gc.getPlayer(iMinorCiv).getTeam()).setHasTech(t, True, iMinorCiv, False, False)


	# RiseAndFall, Religions, Barbs
	#def makeUnit(self, iUnit, iPlayer, tCoords, iNum, eUnitAIType = UnitAITypes.NO_UNITAI, tPromotions = False, prefix = False, name = False): #by LOQ/edead
	def makeUnit(self, iUnit, iPlayer, tCoords, iNum, eDirectionType = DirectionTypes.DIRECTION_SOUTH, eUnitAIType = UnitAITypes.NO_UNITAI, tPromotions = False, prefix = False, name = False): #by LOQ/edead
		"""Makes iNum units for player iPlayer of the type iUnit at tCoords."""
		
		if iUnit == -1: return None # edead
		
		pUnit = None
		#print ("eDirectionType", eDirectionType)
		for i in range(iNum):
			#pUnit = gc.getPlayer(iPlayer).initUnit(iUnit, tCoords[0], tCoords[1], eUnitAIType, DirectionTypes.DIRECTION_SOUTH)
			pUnit = gc.getPlayer(iPlayer).initUnit(iUnit, tCoords[0], tCoords[1], eUnitAIType, eDirectionType)
			if pUnit:
				UnitArtStyler.checkUnitArt(pUnit) # update unit art
				if tPromotions:
					for j in tPromotions:
						pUnit.setHasPromotion(j, True)
				if prefix:
					pUnit.setName("%s %s" %(prefix, pUnit.getName()))
				if name:
					pUnit.setName("%s" %(name))
		return pUnit
		
	def makeUnitAI(self, iUnit, iPlayer, tCoords, iAI, iNum): #by LOQ, modified by Leoreth
                'Makes iNum units for player iPlayer of the type iUnit at tCoords.'
                for i in range(iNum):
                        player = gc.getPlayer(iPlayer)
                        player.initUnit(iUnit, tCoords[0], tCoords[1], iAI, DirectionTypes.DIRECTION_SOUTH)


	# RiseAndFall, Religions
	def getHumanID(self):
		return gc.getGame().getActivePlayer()


	# RiseAndFall
	def flipUnitsInCityBefore(self, tCityPlot, iNewOwner, iOldOwner):
		if iNewOwner == con.iByzantines and iOldOwner != con.iRome:
			return
		plotCity = gc.getMap().plot(tCityPlot[0], tCityPlot[1])
		city = plotCity.getPlotCity()
		iNumUnitsInAPlot = plotCity.getNumUnits()
		j = 0
		for i in range(iNumUnitsInAPlot):
			unit = plotCity.getUnit(j)
			unitType = unit.getUnitType()
			if (unit.getOwner() == iOldOwner):
				unit.kill(False, con.iBarbarian)
				if (iNewOwner < con.iNumPlayers or unitType > con.iSettler):
					self.makeUnit(self.getBaseUnit(unitType, iNewOwner), iNewOwner, [con.iFlipX, con.iFlipY], 1) # edead
			else:
				j += 1


	# RiseAndFall
	def flipUnitsInCityAfter(self, tCityPlot, iCiv):
		#moves new units back in their place
		#print ("tCityPlot After", tCityPlot)
		tempPlot = gc.getMap().plot(con.iFlipX, con.iFlipY)
		if (tempPlot.getNumUnits() != 0):
			iNumUnitsInAPlot = tempPlot.getNumUnits()
			for i in range(iNumUnitsInAPlot):
				unit = tempPlot.getUnit(0)
				unit.setXY(tCityPlot[0], tCityPlot[1], False, False, False)
				if iCiv >= iNumPlayers:
					#print "unit art"
					UnitArtStyler.updateUnitArt(unit)
		#cover plots revealed
		self.coverPlots(con.iFlipX, con.iFlipY, iCiv)


	# Leaving it as it is, since it's only used for the whole map
	def killUnitsInArea(self, tTopLeft, tBottomRight, iCiv):
		for x in range(tTopLeft[0], tBottomRight[0]+1):
			for y in range(tTopLeft[1], tBottomRight[1]+1):
				killPlot = gc.getMap().plot(x,y)
				iNumUnitsInAPlot = killPlot.getNumUnits()
				if (iNumUnitsInAPlot):
					for i in range(iNumUnitsInAPlot):
						unit = killPlot.getUnit(0)
						if (unit.getOwner() == iCiv):
							unit.kill(False, con.iBarbarian)


	# RiseAndFall
	def flipUnitsInArea(self, plotList, iNewOwner, iOldOwner, bSkipPlotCity, bKillSettlers, bSkipOwned=False):
				"""Deletes, recreates units in 0,67 and moves them to the previous tile.
				If there are units belonging to others in that plot and the new owner is barbarian, the units aren't recreated.
				Settlers aren't created.
				If bSkipPlotCity is True, units in a city won't flip. This is to avoid converting barbarian units that would capture a city before the flip delay"""
				#print "flipping units", iNewOwner
				for iLoop in range(len(plotList)):
					killPlot = gc.getMap().plot(plotList[iLoop][0], plotList[iLoop][1])
					if bSkipOwned and killPlot.getOwner() < iNumPlayers and killPlot.getOwner() != utils.getHumanID(): # edead
						continue
					elif iNewOwner == con.iByzantines and iOldOwner != con.iRome:
						continue
					iNumUnitsInAPlot = killPlot.getNumUnits()
					if (iNumUnitsInAPlot):
						bRevealedZero = False
						if (gc.getMap().plot(con.iFlipX, con.iFlipY).isRevealed(iNewOwner, False)):
							bRevealedZero = True
						#print ("killplot", plotList[iLoop][0], plotList[iLoop][1])
						if (bSkipPlotCity == True) and (killPlot.isCity()):
							#print (killPlot.isCity())
							#print 'do nothing'
							pass
						else:
							j = 0
							for i in range(iNumUnitsInAPlot):
								unit = killPlot.getUnit(j)
								#print ("killplot", plotList[iLoop][0], plotList[iLoop][1], unit.getUnitType(), unit.getOwner(), "j", j)
								if (unit.getOwner() == iOldOwner):
									unit.kill(False, con.iBarbarian)
									if (bKillSettlers):
										if ((unit.getUnitType() > con.iSettler)):
											self.makeUnit(self.getBaseUnit(unit.getUnitType(), iNewOwner), iNewOwner, [con.iFlipX, con.iFlipY], 1)
									else:
										if ((unit.getUnitType() >= con.iSettler)): #skip animals
											self.makeUnit(self.getBaseUnit(unit.getUnitType(), iNewOwner), iNewOwner, [con.iFlipX, con.iFlipY], 1)
								else:
										j += 1
							tempPlot = gc.getMap().plot(con.iFlipX, con.iFlipY)
							#moves new units back in their place
							if (tempPlot.getNumUnits() != 0):
								iNumUnitsInAPlot = tempPlot.getNumUnits()
								for i in range(iNumUnitsInAPlot):
									unit = tempPlot.getUnit(0)
									#print ("Moving unit from ", unit.getNameNoDesc(), con.iFlipX, con.iFlipY)
									#print ("Moving unit to ", plotList[iLoop][0], plotList[iLoop][1])
									unit.setXY(plotList[iLoop][0], plotList[iLoop][1], False, False, False)
									if iNewOwner >= iNumPlayers:
										UnitArtStyler.updateUnitArt(unit)
								iCiv = iNewOwner
								if (bRevealedZero == False):
									self.coverPlots(con.iFlipX, con.iFlipY, iCiv)
									
	# srpt
	def byzantineRomanUnitFlip(self):
		unitList = PyPlayer(con.iRome).getUnitList()
		for pUnit in unitList:
			if pUnit.getX() >= 43:
				iX = pUnit.getX()
				iY = pUnit.getY()
				pUnit.kill(False, con.iBarbarian)
				self.makeUnit(self.getBaseUnit(pUnit.getUnitType(), con.iByzantines), con.iByzantines, [con.iFlipX, con.iFlipY], 1)
				tempPlot = gc.getMap().plot(con.iFlipX, con.iFlipY)
				if (tempPlot.getNumUnits() != 0):
					unit = tempPlot.getUnit(0)
					unit.setXY(iX, iY, False, False, False)
					self.coverPlots(con.iFlipX, con.iFlipY, con.iByzantines)


	# RiseAndFall
	def flipCity(self, tCityPlot, bFlipType, bKillUnits, iNewOwner, iOldOwners):
		"""Changes owner of city specified by tCityPlot.
		bFlipType specifies if it's conquered or traded.
		If bKillUnits != 0 all the units in the city will be killed.
		iRetainCulture will determine the split of the current culture between old and new owner. -1 will skip
		iOldOwners is a list. Flip happens only if the old owner is in the list.
		An empty list will cause the flip to always happen."""
		pNewOwner = gc.getPlayer(iNewOwner)
		city = gc.getMap().plot(tCityPlot[0], tCityPlot[1]).getPlotCity()
		if (gc.getMap().plot(tCityPlot[0], tCityPlot[1]).isCity()):
			if not city.isNone():
				iOldOwner = city.getOwner()
				if (iOldOwner in iOldOwners or not iOldOwners):
					if (bKillUnits):
						killPlot = gc.getMap().plot( tCityPlot[0], tCityPlot[1] )
						for i in range(killPlot.getNumUnits()):
							unit = killPlot.getUnit(0)
							unit.kill(False, iNewOwner)
					
					if (bFlipType): #conquest
						if (city.getPopulation() == 2):
							city.setPopulation(3)
						if (city.getPopulation() == 1):
							city.setPopulation(2)
						pNewOwner.acquireCity(city, True, False)
					else: #trade
						pNewOwner.acquireCity(city, False, True)
					
					return True
		return False


	#Congresses, RiseAndFall
	def cultureManager(self, tCityPlot, iCulturePercent, iNewOwner, iOldOwner, bBarbarian2x2Decay, bBarbarian2x2Conversion, bAlwaysOwnPlots):
				"""Converts the culture of the city and of the surrounding plots to the new owner of a city.
				iCulturePercent determine the percentage that goes to the new owner.
				If old owner is barbarian, all the culture is converted"""
				
				pCity = gc.getMap().plot(tCityPlot[0], tCityPlot[1])
				city = pCity.getPlotCity()
				
				#city
				if (pCity.isCity()):
						iCurrentCityCulture = city.getCulture(iOldOwner)
						city.setCulture(iOldOwner, iCurrentCityCulture*(100-iCulturePercent)/100, False)
						if (iNewOwner != con.iBarbarian):
								city.setCulture(con.iBarbarian, 0, True)
						city.setCulture(iNewOwner, iCurrentCityCulture*iCulturePercent/100, False)
						if (city.getCulture(iNewOwner) <= 10):
								city.setCulture(iNewOwner, 20, False)
				
				#halve barbarian culture in a broader area
				if (bBarbarian2x2Decay or bBarbarian2x2Conversion):
					if (iNewOwner < iNumPlayers):
						for x in range(tCityPlot[0]-2, tCityPlot[0]+3):		# from x-2 to x+2
							for y in range(tCityPlot[1]-2, tCityPlot[1]+3):	# from y-2 to y+2
								iPlotBarbCulture = gc.getMap().plot(x, y).getCulture(con.iBarbarian)
								if (iPlotBarbCulture > 0):
									if (gc.getMap().plot(x, y).getPlotCity().isNone() or (x==tCityPlot[0] and y==tCityPlot[1])):
										if (bBarbarian2x2Decay):
											gc.getMap().plot(x, y).setCulture(con.iBarbarian, iPlotBarbCulture/4, True)
										if (bBarbarian2x2Conversion):
											gc.getMap().plot(x, y).setCulture(con.iBarbarian, 0, True)
											gc.getMap().plot(x, y).setCulture(iNewOwner, iPlotBarbCulture, True)
								# loop through minors - edead
								for offset in range(con.iNumMinorPlayers):
									iMinorCiv = con.iIndependent + offset
									iPlotIndependentCulture = gc.getMap().plot(x, y).getCulture(iMinorCiv)
									if (iPlotIndependentCulture > 0):
										if (gc.getMap().plot(x, y).getPlotCity().isNone() or (x==tCityPlot[0] and y==tCityPlot[1])):
											if (bBarbarian2x2Decay):
												gc.getMap().plot(x, y).setCulture(iMinorCiv, iPlotIndependentCulture/4, True)
											if (bBarbarian2x2Conversion):
												gc.getMap().plot(x, y).setCulture(iMinorCiv, 0, True)
												gc.getMap().plot(x, y).setCulture(iNewOwner, iPlotIndependentCulture, True)
				
				#plot
				for x in range(tCityPlot[0]-1, tCityPlot[0]+2):		# from x-1 to x+1
					for y in range(tCityPlot[1]-1, tCityPlot[1]+2):	# from y-1 to y+1
						pCurrent = gc.getMap().plot(x, y)
						
						iCurrentPlotCulture = pCurrent.getCulture(iOldOwner)
						
						if (pCurrent.isCity()):
							pCurrent.setCulture(iNewOwner, iCurrentPlotCulture*iCulturePercent/100, True)
							pCurrent.setCulture(iOldOwner, iCurrentPlotCulture*(100-iCulturePercent)/100, True)
						else:
							pCurrent.setCulture(iNewOwner, iCurrentPlotCulture*iCulturePercent/3/100, True)
							pCurrent.setCulture(iOldOwner, iCurrentPlotCulture*(100-iCulturePercent/3)/100, True)
						
						#cut other players culture
##						for iCiv in range(iNumPlayers):
##							if (iCiv != iNewOwner and iCiv != iOldOwner):
##								iPlotCulture = gc.getMap().plot(x, y).getCulture(iCiv)
##								if (iPlotCulture > 0):
##									gc.getMap().plot(x, y).setCulture(iCiv, iPlotCulture/3, True)
						
						if (not pCurrent.isCity()):
							if (bAlwaysOwnPlots):
								pCurrent.setOwner(iNewOwner)
							else:
								if (pCurrent.getCulture(iNewOwner)*4 > pCurrent.getCulture(iOldOwner)):
									pCurrent.setOwner(iNewOwner)



	# handler
	def spreadMajorCulture(self, iMajorCiv, iX, iY):
		for x in range(iX-4, iX+5):		# from x-4 to x+4
			for y in range(iY-4, iY+5):	# from y-4 to y+4
				pCurrent = gc.getMap().plot(x, y)
				if (pCurrent.isCity()):
					city = pCurrent.getPlotCity()
					if (city.getOwner() >= iNumPlayers):
						iMinor = city.getOwner()
						iDen = 25
						#if (gc.getPlayer(iMajorCiv).getSettlersMaps( 67-y, x ) >= 400):
						if gc.getMap().plot(iX, iY).getRegionID() in self.getCoreRegions(iMajorCiv):
							iDen = 10
						#elif (gc.getPlayer(iMajorCiv).getSettlersMaps( 67-y, x ) >= 150):
						elif gc.getMap().plot(iX, iY).getRegionID() in self.getNormalRegions(iMajorCiv):
							iDen = 15
						
						iMinorCityCulture = city.getCulture(iMinor)
						city.setCulture(iMajorCiv, iMinorCityCulture/iDen, True)
						
						iMinorPlotCulture = pCurrent.getCulture(iMinor)
						pCurrent.setCulture(iMajorCiv, iMinorPlotCulture/iDen, True)


	# RiseAndFall
	def convertPlotCulture(self, pCurrent, iCiv, iPercent, bOwner):
		
		if (pCurrent.isCity()):
			city = pCurrent.getPlotCity()
			iCivCulture = city.getCulture(iCiv)
			iLoopCivCulture = 0
			for iLoopCiv in range(iNumTotalPlayers):
				if (iLoopCiv != iCiv):
					iLoopCivCulture += city.getCulture(iLoopCiv)
					city.setCulture(iLoopCiv, city.getCulture(iLoopCiv)*(100-iPercent)/100, True)
			city.setCulture(iCiv, iCivCulture + iLoopCivCulture, True)  
		
		iCivCulture = pCurrent.getCulture(iCiv)
		iLoopCivCulture = 0
		for iLoopCiv in range(iNumTotalPlayers):
			if (iLoopCiv != iCiv):
				iLoopCivCulture += pCurrent.getCulture(iLoopCiv)
				pCurrent.setCulture(iLoopCiv, pCurrent.getCulture(iLoopCiv)*(100-iPercent)/100, True)
		pCurrent.setCulture(iCiv, iCivCulture + iLoopCivCulture, True)
		if (bOwner == True):
			pCurrent.setOwner(iCiv)


	# RiseAndFall
	def pushOutGarrisons(self, tCityPlot, iOldOwner):
		tDestination = (-1, -1)
		for x in range(tCityPlot[0]-2, tCityPlot[0]+3):
			for y in range(tCityPlot[1]-2, tCityPlot[1]+3):
				pDestination = gc.getMap().plot(x, y)
				if (pDestination.getOwner() == iOldOwner and (not pDestination.isWater()) and (not pDestination.isImpassable())):
					tDestination = (x, y)
					break
					break
		if (tDestination != (-1, -1)):
			plotCity = gc.getMap().plot(tCityPlot[0], tCityPlot[1])
			iNumUnitsInAPlot = plotCity.getNumUnits()
			j = 0
			for i in range(iNumUnitsInAPlot):
				unit = plotCity.getUnit(j)
				if (unit.getDomainType() == 2): #land unit
					unit.setXY(tDestination[0], tDestination[1], False, False, False)
				else:
					j = j + 1


	# RiseAndFall
	def relocateSeaGarrisons(self, tCityPlot, iOldOwner):
				tDestination = (-1, -1)
				cityList = PyPlayer(iOldOwner).getCityList()
				for pyCity in cityList:
						if (pyCity.GetCy().isCoastal(0)):
								tDestination = (pyCity.GetCy().getX(), pyCity.GetCy().getY())
				if (tDestination == (-1, -1)):
						for x in range(tCityPlot[0]-12, tCityPlot[0]+12):
								for y in range(tCityPlot[1]-12, tCityPlot[1]+12):
										pDestination = gc.getMap().plot(x, y)
										if (pDestination.isWater()):
												tDestination = (x, y)
												break
												break
				if (tDestination != (-1, -1)):
						plotCity = gc.getMap().plot(tCityPlot[0], tCityPlot[1])
						iNumUnitsInAPlot = plotCity.getNumUnits()
						j = 0
						for i in range(iNumUnitsInAPlot):
								unit = plotCity.getUnit(j)
								if (unit.getDomainType() == 0): #sea unit
										unit.setXY(tDestination[0], tDestination[1], False, False, False)
								else:
										j = j + 1


	# RiseAndFall
	def createGarrisons(self, tCityPlot, iNewOwner, iNumUnits):
		pTeam = gc.getTeam(gc.getPlayer(iNewOwner).getTeam())
		
		if pTeam.isHasTech(con.iGunpowder):
			iUnitType = con.iMusketman
		elif pTeam.isHasTech(con.iBlastFurnace):
			iUnitType = con.iPikeman
		elif pTeam.isHasTech(con.iMarksmanship):
			iUnitType = con.iMarksman
		elif pTeam.isHasTech(con.iSteelWorking):
			iUnitType = con.iHeavySpearman
		else:
			iUnitType = con.iArcher
		
		self.makeUnit(iUnitType, iNewOwner, [tCityPlot[0], tCityPlot[1]], iNumUnits)


	# RiseAndFall, Stability
	def killCiv(self, iCiv, iNewCiv):
		self.clearPlague(iCiv)
		for pyCity in PyPlayer(iCiv).getCityList():
			tCoords = (pyCity.GetCy().getX(), pyCity.GetCy().getY())
			self.cultureManager(tCoords, 50, iNewCiv, iCiv, False, False, False)
			self.flipCity(tCoords, 0, 0, iNewCiv, [iCiv]) #by trade because by conquest may raze the city
		
		self.flipUnitsInArea(self.getAreaPlotList([0,0], [con.iMapWidth, con.iMapHeight]), iNewCiv, iCiv, False, True)
		self.setLastTurnAlive(iCiv, gc.getGame().getGameTurn())
		self.resetUHV(iCiv)


	def killAndFragmentCiv(self, iCiv, bAssignOneCity):
		
		self.clearPlague(iCiv)
		iNumLoyalCities = 0
		iCounter = gc.getGame().getSorenRandNum(6, 'random start')
		iNumPlayerCities = len(PyPlayer(iCiv).getCityList()) #needs to be assigned cause it changes dynamically
		for pyCity in PyPlayer(iCiv).getCityList():
			#print("iCounter",iCounter)
			tCoords = (pyCity.GetCy().getX(), pyCity.GetCy().getY())
			pCurrent = gc.getMap().plot(tCoords[0], tCoords[1])
			#loyal cities for the human player
			#print(bAssignOneCity,iNumLoyalCities,1+(iNumPlayerCities-1)/6,pyCity.GetCy().isCapital(),iCounter%6 == 0)
			if (bAssignOneCity and iNumLoyalCities <= 1+(iNumPlayerCities-1)/6 and (pyCity.GetCy().isCapital() or iCounter%6 == 0)):
					iNumLoyalCities += 1
					if (iNumLoyalCities == 1):
						for offset in range(con.iNumMinorPlayers):
							gc.getTeam(gc.getPlayer(iCiv).getTeam()).declareWar(con.iIndependent + offset, False, -1) #too dangerous?
					iCounter += 1
					#print(pyCity.GetCy().getName(), "loyal")
					continue
			#assign to neighbours first
			bNeighbour = False
			iRndnum = gc.getGame().getSorenRandNum(iNumPlayers, 'starting count')
			
			# edead - minors fix + efficiency
			plotCulture = pCurrent.getCulture(iCiv) + pCurrent.getCulture(con.iBarbarian)
			for offset in range(iNumMinorPlayers):
				plotCulture += pCurrent.getCulture(con.iIndependent + offset)
			
			for j in range(iRndnum, iRndnum + iNumPlayers): #only major players
				iLoopCiv = j % iNumPlayers
				if (gc.getPlayer(iLoopCiv).isAlive() and iLoopCiv != iCiv and not gc.getPlayer(iLoopCiv).isHuman()):
					regionList = []
					regionList.extend(self.getCoreRegions(iLoopCiv))
					regionList.extend(self.getNormalRegions(iLoopCiv))
					regionList.extend(self.getBroaderRegions(iLoopCiv))
					if pCurrent.getCulture(iLoopCiv) > 0 and pCurrent.getRegionID() in regionList: # make sure to skip random culture in far away cities
						if (pCurrent.getCulture(iLoopCiv)*100 / (pCurrent.getCulture(iLoopCiv) + plotCulture) >= 5): #change in vanilla
							self.flipUnitsInCityBefore(tCoords, iLoopCiv, iCiv)
							self.setTempFlippingCity((tCoords[0],tCoords[1]))
							self.flipCity(tCoords, 0, 0, iLoopCiv, [iCiv])
							#self.flipUnitsInCityAfter(self.getTempFlippingCity(), iLoopCiv) # edead - buggy for some reason
							self.flipUnitsInCityAfter(tCoords, iLoopCiv) # edead
							self.flipUnitsInArea(self.getAreaPlotList([tCoords[0]-2,tCoords[1]-2], [tCoords[0]+2,tCoords[1]+2]), iLoopCiv, iCiv, False, True)
							bNeighbour = True
							break
			if (bNeighbour):
				iCounter += 1
				continue
			iNewCiv = self.getRandomMinorCiv()
			self.flipUnitsInCityBefore(tCoords, iNewCiv, iCiv)
			self.setTempFlippingCity(tCoords) # edead
			self.cultureManager(tCoords, 50, iNewCiv, iCiv, False, False, False)
			self.flipCity(tCoords, 0, 0, iNewCiv, [iCiv])
			self.flipUnitsInCityAfter(tCoords, iNewCiv) # edead
			iCounter += 1
			self.flipUnitsInArea(self.getAreaPlotList([tCoords[0]-1,tCoords[1]-1], [tCoords[0]+1,tCoords[1]+1]), iNewCiv, iCiv, False, True)
			
			# free vassals - edead
			for i in range(iNumPlayers):
				if i != iCiv:
					pTeam = gc.getTeam(i)
					if pTeam.isAlive() and pTeam.isVassal(iCiv):
						pTeam.setVassal(iCiv, False, False)
			
		if (bAssignOneCity == False):
			self.killUnitsInArea([0,0], [con.iMapWidth, con.iMapHeight], iCiv)
			self.resetUHV(iCiv)
		self.setLastTurnAlive(iCiv, gc.getGame().getGameTurn())
		for x in range (con.iMapWidth):
			for y in range (con.iMapHeight):
				gc.getMap().plot(x, y).setCulture(iCiv, 0, True)
				
		
				
		# update unit art styles of independents
		#for iLoopPlayer in range(con.iIndependent, con.iBarbarian):
			#unitList = PyPlayer(iLoopPlayer).getUnitList()
			#for pUnit in unitList:
				#UnitArtStyler.updateUnitArt(pUnit)
		
	def collapseToCore(self, iPlayer, iCiv):
		#print "collapseToCore"
		#if sd.getAlreadyCollapsed(iPlayer) == 1 and iPlayer != utils.getHumanID():
			#self.killAndFragmentCiv(iPlayer, False)
			#sd.setAlreadyCollapsed(iPlayer, 0)
		#else:
		#sd.setAlreadyCollapsed(iPlayer, 1)
		pTeam = gc.getTeam(gc.getPlayer(iPlayer).getTeam())
		if pTeam.isHasTech(con.iStabilityCollapsing):
			pTeam.setHasTech(con.iStabilityUnstable, True, iPlayer, False, False)
			pTeam.setHasTech(con.iStabilityCollapsing, False, iPlayer, False, False)
		elif pTeam.isHasTech(con.iStabilityUnstable):
			pTeam.setHasTech(con.iStabilityStable, True, iPlayer, False, False)
			pTeam.setHasTech(con.iStabilityUnstable, False, iPlayer, False, False)
		safeRegionList = []
		capitalRegionID = gc.getMap().plot(gc.getPlayer(iPlayer).getCapitalCity().getX(), gc.getPlayer(iPlayer).getCapitalCity().getY()).getRegionID()
		safeRegionList.extend(self.getCoreRegions(iCiv))
		safeRegionList.append(capitalRegionID)
		for pyCity in PyPlayer(iPlayer).getCityList():
			tCoords = (pyCity.GetCy().getX(), pyCity.GetCy().getY())
			pCurrent = gc.getMap().plot(tCoords[0], tCoords[1])
			if pCurrent.getRegionID() in safeRegionList or pyCity.GetCy().getNumRealBuilding(con.iPalace) > 0:
				city = pCurrent.getPlotCity()
				iRevoltTurns = gc.getGame().getSorenRandNum(3, 'Revolt turns')
				city.changeCultureUpdateTimer(iRevoltTurns);
				city.changeOccupationTimer(iRevoltTurns);
			else:
				iNewCiv = self.getRandomMinorCiv()
				self.flipUnitsInCityBefore(tCoords, iNewCiv, iPlayer)
				self.setTempFlippingCity(tCoords) # edead
				self.cultureManager(tCoords, 50, iNewCiv, iPlayer, False, False, False)
				self.flipCity(tCoords, 0, 0, iNewCiv, [iPlayer])
				self.flipUnitsInCityAfter(tCoords, iNewCiv) # edead
				self.flipUnitsInArea(self.getAreaPlotList([tCoords[0]-1,tCoords[1]-1], [tCoords[0]+1,tCoords[1]+1]), iNewCiv, iPlayer, False, True)
		
				
		# update unit art styles of independents
		#for iLoopPlayer in range(con.iIndependent, con.iBarbarian):
			#unitList = PyPlayer(iLoopPlayer).getUnitList()
			#for pUnit in unitList:
				#UnitArtStyler.updateUnitArt(pUnit)
				
	def secedeProvinces(self, iPlayer, iCiv, iNumSecessions):
		
		apCityList = PyPlayer(iPlayer).getCityList()
		controlledProvinceList = []
		occupiedProvinceList = []
		
		for pCity in apCityList:
			regionID = gc.getMap().plot(pCity.getX(), pCity.getY()).getRegionID
			if self.checkRegionControl(iPlayer, regionID) and regionID not in controlledProvinceList:
				controlledProvinceList.append(regionID)
			elif regionID not in occupiedProvinceList:
				occupiedProvinceList.append(regionID)
		


	# edead: only used for Barbs
	def squareSearch( self, tTopLeft, tBottomRight, function, argsList ): #by LOQ
		"""Searches all tile in the square from tTopLeft to tBottomRight and calls function for
		every tile, passing argsList. The function called must return a tuple: (1) a result, (2) if
		a plot should be painted and (3) if the search should continue.
		"""
		tPaintedList = []
		result = None
		for x in range(tTopLeft[0], tBottomRight[0]+1):
			for y in range(tTopLeft[1], tBottomRight[1]+1, -1): # edead: added -1, not sure why it didn't work before
				result, bPaintPlot, bContinueSearch = function((x, y), result, argsList)
				if bPaintPlot: # paint plot
					tPaintedList.append((x, y))
				if not bContinueSearch: # goal reached, so stop
					return result, tPaintedList
		return result, tPaintedList


	# edead: replaces squareSearch for RiseAndFall
	def plotListSearch(self, plotList, function, argsList):
		"""Searches all tiles in the plotList and calls function for every tile, passing argsList. 
		The function called must return a tuple: (1) a result, (2) if a plot should be painted and 
		(3) if the search should continue.
		"""
		tPaintedList = []
		result = None
		for i in range(len(plotList)):
			result, bPaintPlot, bContinueSearch = function((plotList[i][0], plotList[i][1]), result, argsList)
			if bPaintPlot: # paint plot
				tPaintedList.append((plotList[i][0], plotList[i][1]))
			if not bContinueSearch: # goal reached, so stop
				return result, tPaintedList
		return result, tPaintedList
		
	def fatCrossPlotList(self, iX, iY):
	
		x = iX
		y = iY
		plotList = [(x-2, y-1), (x-2, y), (x-2, y+1), (x-1, y-2), (x-1, y-1), (x-1, y), (x-1, y+1), (x-1, y+2), (x, y-2), (x, y-1), (x, y+1), (x, y+2), (x+1, y-2), (x+1, y-1), (x+1, y), (x+1, y+1), (x+1, y+2), (x+2, y-1), (x+2, y), (x+2, y+1)]
		return plotList
		
	def citySquarePlotList(self, iX, iY):
	
		x = iX
		y = iY
		plotList = [(x-1, y-1), (x-1, y), (x-1, y+1), (x, y-1), (x, y+1), (x+1, y-1), (x+1, y), (x+1, y+1)]
		return plotList

	# functions for plotListSearch & squareSearch


	# Barbs, RiseAndFall
	def outerInvasion( self, tCoords, result, argsList ):
		"""Checks validity of the plot at the current tCoords, returns plot if valid (which stops the search).
		Plot is valid if it's hill or flatlands, it isn't marsh or jungle, it isn't occupied by a unit or city and if it isn't a civ's territory"""
		bPaint = True
		bContinue = True
		pCurrent = gc.getMap().plot(tCoords[0], tCoords[1])
		if pCurrent.isHills() or pCurrent.isFlatlands():
			if pCurrent.getTerrainType() != con.iWetland:
				if not pCurrent.isCity() and not pCurrent.isUnit():
					#if (pCurrent.countTotalCulture() == 0 ):
					if pCurrent.calculateCulturalOwner() == -1: # edead: bugfix
						# this is a good plot, so paint it and continue search
						return (None, bPaint, bContinue)
		# not a good plot, so don't paint it but continue search
		return (None, not bPaint, bContinue)

	# Barbs
	def innerSeaSpawn( self, tCoords, result, argsList ):
		"""Checks validity of the plot at the current tCoords, returns plot if valid (which stops the search).
		Plot is valid if it's water and it isn't occupied by any unit. Unit check extended to adjacent plots"""
		bPaint = True
		bContinue = True
		pCurrent = gc.getMap().plot(tCoords[0], tCoords[1])
		if pCurrent.isWater() and not pCurrent.isLake(): # edead: no barbs in lakes!
			if not pCurrent.isCity() and not pCurrent.isUnit():
				bClean = True
				for x in range(tCoords[0] - 1, tCoords[0] + 2):		# from x-1 to x+1
					for y in range(tCoords[1] - 1, tCoords[1] + 2):	# from y-1 to y+1
						if gc.getMap().plot(x,y).isUnit():
							bClean = False
							break
				if bClean:   
					# this is a good plot, so paint it and continue search
					return (None, bPaint, bContinue)
		# not a good plot, so don't paint it but continue search
		return (None, not bPaint, bContinue)

	# Barbs
	def outerSeaSpawn( self, tCoords, result, argsList ):
		"""Checks validity of the plot at the current tCoords, returns plot if valid (which stops the search).
		Plot is valid if it's water and it isn't occupied by any unit and if it isn't a civ's territory. Unit check extended to adjacent plots"""
		bPaint = True
		bContinue = True
		pCurrent = gc.getMap().plot(tCoords[0], tCoords[1])
		if pCurrent.isWater() and not pCurrent.isLake(): # edead: no barbs in lakes!
			if not pCurrent.isCity() and not pCurrent.isUnit():
				if pCurrent.calculateCulturalOwner() == -1: # edead: bugfix
					bClean = True
					for x in range(tCoords[0] - 1, tCoords[0] + 2):		# from x-1 to x+1
						for y in range(tCoords[1] - 1, tCoords[1] + 2):	# from y-1 to y+1
							if gc.getMap().plot(x,y).isUnit():
								bClean = False
								break
					if bClean:
						# this is a good plot, so paint it and continue search
						return (None, bPaint, bContinue)
		# not a good plot, so don't paint it but continue search
		return (None, not bPaint, bContinue)

	# Barbs
	def outerSpawn( self, tCoords, result, argsList ):
		"""Checks validity of the plot at the current tCoords, returns plot if valid (which stops the search).
		Plot is valid if it's hill or flatlands, it isn't marsh or jungle, it isn't occupied by a unit or city and if it isn't a civ's territory.
		Unit check extended to adjacent plots"""
		bPaint = True
		bContinue = True
		pCurrent = gc.getMap().plot(tCoords[0], tCoords[1])
		if pCurrent.isHills() or pCurrent.isFlatlands():
			if pCurrent.getTerrainType() != con.iWetland:
				if not pCurrent.isCity() and not pCurrent.isUnit():
					bClean = True
					for x in range(tCoords[0] - 1, tCoords[0] + 2):		# from x-1 to x+1
						for y in range(tCoords[1] - 1, tCoords[1] + 2):	# from y-1 to y+1
							if gc.getMap().plot(x,y).isUnit():
								bClean = False
								break
					if bClean:
						if pCurrent.calculateCulturalOwner() == -1: # edead: bugfix
							# this is a good plot, so paint it and continue search
							return (None, bPaint, bContinue)
		# not a good plot, so don't paint it but continue search
		return (None, not bPaint, bContinue)

	# RiseAndFall
	def innerInvasion( self, tCoords, result, argsList ):
		"""Checks validity of the plot at the current tCoords, returns plot if valid (which stops the search).
		Plot is valid if it's hill or flatlands, it isn't marsh or jungle, it isn't occupied by a unit or city and if it isn't a civ's territory"""
		bPaint = True
		bContinue = True
		pCurrent = gc.getMap().plot(tCoords[0], tCoords[1])
		if pCurrent.isHills() or pCurrent.isFlatlands():
			if pCurrent.getTerrainType() != con.iWetland:
				if not pCurrent.isCity() and not pCurrent.isUnit():
					if pCurrent.getOwner() >= 0 and pCurrent.getOwner() < con.iNumPlayers: #if (pCurrent.getOwner() in argsList ):
						# this is a good plot, so paint it and continue search
						return (None, bPaint, bContinue)
		# not a good plot, so don't paint it but continue search
		return (None, not bPaint, bContinue)


	def innerSpawn( self, tCoords, result, argsList ):
		"""Checks validity of the plot at the current tCoords, returns plot if valid (which stops the search).
		Plot is valid if it's hill or flatlands, it isn't marsh or jungle, it isn't occupied by a unit or city and if it isn't a civ's territory"""
		bPaint = True
		bContinue = True
		pCurrent = gc.getMap().plot(tCoords[0], tCoords[1])
		if pCurrent.isHills() or pCurrent.isFlatlands():
			if pCurrent.getTerrainType() != con.iWetland:
				if not pCurrent.isCity() and not pCurrent.isUnit():
					bClean = True
					for x in range(tCoords[0] - 1, tCoords[0] + 2):		# from x-1 to x+1
						for y in range(tCoords[1] - 1, tCoords[1] + 2):	# from y-1 to y+1
							if gc.getMap().plot(x,y).isUnit():
								bClean = False
								break
					if bClean:
						if pCurrent.getOwner() in argsList:
							# this is a good plot, so paint it and continue search
							return (None, bPaint, bContinue)
		# not a good plot, so don't paint it but continue search
		return (None, not bPaint, bContinue)


	def goodPlots( self, tCoords, result, argsList ):
		"""Checks validity of the plot at the current tCoords, returns plot if valid (which stops the search).
		Plot is valid if it's hill or flatlands, it isn't desert, tundra, marsh or jungle; it isn't occupied by a unit or city and if it isn't a civ's territory.
		Unit check extended to adjacent plots.
		"""
		bPaint = True
		bContinue = True
		pCurrent = gc.getMap().plot(tCoords[0], tCoords[1])
		if pCurrent.isHills() or pCurrent.isFlatlands():
			if not pCurrent.isImpassable():
				if not pCurrent.isUnit():
					if pCurrent.getTerrainType() not in [con.iDesert, con.iSemidesert, con.iTundra, con.iWetland]:
						if pCurrent.calculateCulturalOwner() == -1: # edead: bugfix
							# this is a good plot, so paint it and continue search
							return (None, bPaint, bContinue)
		# not a good plot, so don't paint it but continue search
		return (None, not bPaint, bContinue)
		
	def horsePlots( self, tCoords, result, argsList ): # plot search for Gokturk UP
		"""Checks validity of the plot at the current tCoords, returns plot if valid (which stops the search).
		Plot is valid if it's flatlands, it isn't tundra, marsh, forest or jungle; and if it doesn't already have a bonus.
		Unit check extended to adjacent plots.
		"""
		bPaint = True
		bContinue = True
		pCurrent = gc.getMap().plot(tCoords[0], tCoords[1])
		if pCurrent.isFlatlands():
			if not pCurrent.isImpassable():
				if pCurrent.getTerrainType() not in [con.iTundra, con.iWetland]:
					if pCurrent.getFeatureType() not in [con.iMarsh, con.iJungle, con.iForest, con.iWoodland, con.iTropicalForest, con.iOasis, con.iDenseForest, con.iIce]:
						if pCurrent.getBonusType(-1) == -1:
							# this is a good plot, so paint it and continue search
							return (None, bPaint, bContinue)
		# not a good plot, so don't paint it but continue search
		return (None, not bPaint, bContinue)


	def ownedCityPlots( self, tCoords, result, argsList ):
		"""Checks validity of the plot at the current tCoords, returns plot if valid (which stops the search).
		Plot is valid if it contains a city belonging to the civ.
		"""
		bPaint = True
		bContinue = True
		pCurrent = gc.getMap().plot(tCoords[0], tCoords[1])
		if pCurrent.getOwner() == argsList:
			if pCurrent.isCity():
				# this is a good plot, so paint it and continue search
				return (None, bPaint, bContinue)
		# not a good plot, so don't paint it but continue search
		return (None, not bPaint, bContinue)


	def ownedCityPlotsAdjacentArea( self, tCoords, result, argsList ):
		"""Checks validity of the plot at the current tCoords, returns plot if valid (which stops the search).
		Plot is valid if it contains a city belonging to the civ"""
		bPaint = True
		bContinue = True
		pCurrent = gc.getMap().plot(tCoords[0], tCoords[1])
		#print(tCoords[0], tCoords[1], pCurrent.isCity(), pCurrent.getOwner() == argsList[0], pCurrent.isAdjacentToArea(gc.getMap().plot(argsList[1][0],argsList[1][1]).area()))
		if pCurrent.getOwner() == argsList[0] and pCurrent.isAdjacentToArea(gc.getMap().plot(argsList[1][0],argsList[1][1]).area()):
			if pCurrent.isCity():
				# this is a good plot, so paint it and continue search
				return (None, bPaint, bContinue)
		# not a good plot, so don't paint it but continue search
		return (None, not bPaint, bContinue)


	def foundedCityPlots( self, tCoords, result, argsList ):
		"""Checks validity of the plot at the current tCoords, returns plot if valid (which stops the search).
		Plot is valid if it contains a city belonging to the civ"""
		bPaint = True
		bContinue = True
		pCurrent = gc.getMap().plot(tCoords[0], tCoords[1])
		if pCurrent.isCity():
			if pCurrent.getPlotCity().getOriginalOwner() == argsList:
				# this is a good plot, so paint it and continue search
				return (None, bPaint, bContinue)
		# not a good plot, so don't paint it but continue search
		return (None, not bPaint, bContinue)


	def ownedPlots( self, tCoords, result, argsList ):
		"""Checks validity of the plot at the current tCoords, returns plot if valid (which stops the search).
		Plot is valid if it is in civ's territory."""
		bPaint = True
		bContinue = True
		pCurrent = gc.getMap().plot(tCoords[0], tCoords[1])
		if pCurrent.getOwner() == argsList:
			# this is a good plot, so paint it and continue search
			return (None, bPaint, bContinue)
		# not a good plot, so don't paint it but continue search
		return (None, not bPaint, bContinue)


	def goodOwnedPlots( self, tCoords, result, argsList ):
		"""Checks validity of the plot at the current tCoords, returns plot if valid (which stops the search).
		Plot is valid if it's hill or flatlands; it isn't marsh or jungle, it isn't occupied by a unit and if it is in civ's territory."""
		bPaint = True
		bContinue = True
		pCurrent = gc.getMap().plot(tCoords[0], tCoords[1])
		if pCurrent.isHills() or pCurrent.isFlatlands():
			if pCurrent.getFeatureType() not in [con.iMarsh, con.iJungle]:
				if not pCurrent.isCity() and not pCurrent.isUnit():
						if pCurrent.getOwner() == argsList:
							# this is a good plot, so paint it and continue search
							return (None, bPaint, bContinue)
		# not a good plot, so don't paint it but continue search
		return (None, not bPaint, bContinue)


	def resetUHV(self, iPlayer):
		if (iPlayer < iNumPlayers):
			if (self.getGoal(iPlayer, 0) == -1):
				self.setGoal(iPlayer, 0, 0)
			if (self.getGoal(iPlayer, 1) == -1):
				self.setGoal(iPlayer, 1, 0)
			if (self.getGoal(iPlayer, 2) == -1):
				self.setGoal(iPlayer, 2, 0)


	def clearPlague(self, iCiv):
		for pyCity in PyPlayer(iCiv).getCityList():
			if (pyCity.GetCy().getNumRealBuilding(con.iPlague) > 0):
				pyCity.GetCy().setNumRealBuilding(con.iPlague, 0)


	#AIWars, by CyberChrist

	def isNoVassal(self, iCiv):
		iMaster = 0
		for iMaster in range (iNumTotalPlayers):
			if gc.getTeam(gc.getPlayer(iCiv).getTeam()).isVassal(iMaster):
				if gc.getPlayer(iMaster).isAlive(): # edead: occasional CIV4 bug makes dead masters
					return False
		return True


	def isAVassal(self, iCiv):
		iMaster = 0
		for iMaster in range (iNumTotalPlayers):
			if gc.getTeam(gc.getPlayer(iCiv).getTeam()).isVassal(iMaster):
				if gc.getPlayer(iMaster).isAlive(): # edead: occasional CIV4 bug makes dead masters
					return True
		return False


	#Plague, Religions
	def getRandomCity(self, iPlayer):
		
		cityList = []
		apCityList = PyPlayer(iPlayer).getCityList()
		for pCity in apCityList:
			cityList.append(pCity.GetCy())
		if (len(cityList)):
			return cityList[gc.getGame().getSorenRandNum(len(cityList), 'random city')]
		else:
			return -1
			
			
	# RomanAIWars		
	def getRandomRomanTargetCity(self, iPlayer):
		
		cityList = []
		regionList = [con.rAfrica, con.rLibya, con.rEgypt, con.rJudea, con.rSyria, con.rAsia, con.rCappadocia, con.rGreece, con.rThrace]
		apCityList = PyPlayer(iPlayer).getCityList()
		for pCity in apCityList:
			city = pCity.GetCy()
			if city.isCoastal(0):
				x = pCity.getX()
				y = pCity.getY()
				if gc.getMap().plot(x, y).getRegionID() in regionList:
					cityList.append(pCity.GetCy())
		if (len(cityList)):
			return cityList[gc.getGame().getSorenRandNum(len(cityList), 'random city')]
		else:
			return -1
			
	def getRandomCarthageTargetCity(self, iPlayer):
		
		cityList = []
		regionList = [con.rIberia, con.rSeptimania, con.rNItaly, con.rSicily]
		apCityList = PyPlayer(iPlayer).getCityList()
		for pCity in apCityList:
			x = pCity.getX()
			y = pCity.getY()
			if gc.getMap().plot(x, y).getRegionID() in regionList:
				cityList.append(pCity.GetCy())
		if (len(cityList)):
			return cityList[gc.getGame().getSorenRandNum(len(cityList), 'random city')]
		else:
			return -1


	def getRandomCiv( self ):
		
		civList = []
		for i in range(con.iNumPlayers):
			if gc.getPlayer(i).isAlive() and self.getYear() >= con.tBirth[i]:
				civList.append(i)
				
		return civList[gc.getGame().getSorenRandNum(len(civList), 'random civ')]


	def isMortalUnit(self, unit):
		
		if unit.isHasPromotion(con.iLeader): #leader
			if not gc.getPlayer(unit.getOwner()).isHuman():
				return False
		iUnitType = unit.getUnitType()
		if iUnitType >= con.iWorkBoat:
			return False
		return True


	def secedeCity(self, city, bSilent=False):
		"""Makes a specific city declare independence."""
		
		if city.isWeLoveTheKingDay() or city.isCapital():
			return False
		
		iPlayer = city.getOwner()
		iNewCiv = self.getRandomMinorCiv()
		self.cultureManager((city.getX(),city.getY()), 50, iNewCiv, iPlayer, False, True, True)
		self.flipUnitsInCityBefore((city.getX(),city.getY()), iNewCiv, iPlayer)
		self.setTempFlippingCity((city.getX(),city.getY()))
		self.flipCity((city.getX(),city.getY()), 0, 0, iNewCiv, [iPlayer])   #by trade because by conquest may raze the city
		self.flipUnitsInCityAfter(self.getTempFlippingCity(), iNewCiv)
		city = gc.getMap().plot(city.getX(),city.getY()).getPlotCity()
		output = True
		if iPlayer == self.getHumanID() and not city is None:
			if bSilent:
				output = city.getName()
			else:
				CyInterface().addMessage(iPlayer, True, con.iDuration, localText.getText("TXT_KEY_STABILITY_SECESSION", (city.getName(), )), "AS2D_CITY_REVOLT", InterfaceMessageTypes.MESSAGE_TYPE_MINOR_EVENT, ArtFileMgr.getInterfaceArtInfo("INTERFACE_RESISTANCE").getPath(), ColorTypes(con.iRed), city.getX(), city.getY(), True, True)
		#print ("city seccession, civ:", iPlayer)
		return output


	def secedeRandomCity(self, iPlayer, iRevoltTurns = 0):
		"""Makes one semi-random city declare independence."""
		
		if gc.getPlayer(iPlayer).getNumCities() > 0: #this check is needed, otherwise game crashes
			return False
		
		cityList = []
		secondPass = []
		apCityList = PyPlayer(iPlayer).getCityList()
		shuffle(apCityList)
		capital = gc.getPlayer(iPlayer).getCapitalCity()
		
		for pCity in apCityList:
			city = pCity.GetCy()
			iRegion = gc.getMap().plot(city.getX(), city.getY()).getRegionID()
			
			# skip capitals and core cities
			if city.isWeLoveTheKingDay() or city.isCapital():
				continue
			if city.getX() == con.tCapitals[iPlayer][0] and city.getY() == con.tCapitals[iPlayer][1]:
				continue
			if sd.getCivilization(iPlayer) != iCiv and city.getX() == con.tRespawnCapitals[iPlayer][0] and city.getY() == con.tRespawnCapitals[iPlayer][1]:
				continue
			if iRegion in self.getCoreRegions(iPlayer): # spare the core cities instead of iDistance > 3
				continue
			
			# add up unrest points from various sources
			iTotalUnrest = city.angryPopulation(0)
			if city.healthRate(False, 0) < 0: iTotalUnrest += 1
			if city.getReligionBadHappiness() > 0: iTotalUnrest += 1 
			if city.getHurryAngerModifier() > 0: iTotalUnrest += 1
			if city.getNoMilitaryPercentAnger() > 0: iTotalUnrest += 1
			if city.getWarWearinessPercentAnger() > 0: iTotalUnrest += 1
			if city.isOccupation() or city.isDisorder(): iTotalUnrest += 1
			
			iDistance = self.calculateDistance(city.getX(), city.getY(), capital.getX(), capital.getY())
			
			# if really bad city is found, take it and break the loop, otherwise store them in first & second pass lists
			if iRegion not in self.getNormalRegions(iPlayer) and (iRegion in con.lUnrulyRegions or city.isOccupation() or city.isDisorder()):
				cityList = [city]
				break
			if iRegion not in self.getNormalRegions(iPlayer) and iRegion not in self.getBroaderRegions(iPlayer) and (iTotalUnrest > 0 or iDistance > 40):
				cityList = [city]
				break
			if iRegion not in self.getNormalRegions(iPlayer) and iTotalUnrest > 1:
				cityList = [city]
				break
			if iTotalUnrest > 3 or (iRegion in con.lUnrulyRegions and iTotalUnrest > 0):
				cityList = [city]
				break
			if iRegion in con.lUnrulyRegions:
				cityList.append(city)
			elif iRegion not in self.getNormalRegions(iPlayer) and iRegion not in self.getBroaderRegions(iPlayer):
				cityList.append(city)
			elif iRegion not in self.getNormalRegions(iPlayer) and iTotalUnrest > 0:
				cityList.append(city)
			elif iTotalUnrest > 1:
				cityList.append(city)
			elif iTotalUnrest > 0:
				secondPass.append(city)
			else:
				pCurrent = gc.getMap().plot(city.getX(), city.getY())
				for iLoop in range(iNumTotalPlayers+1):
					if iLoop != iPlayer:
						if pCurrent.getCulture(iLoop) > 0:
							secondPass.append(city)
							break
		
		if not cityList:
			cityList = secondPass
		
		if cityList:
			splittingCity = cityList[gc.getGame().getSorenRandNum(len(cityList), 'random city')]
			
			# Stationed garrison can turn the secession into a revolt (10% chance per normal unit, 20% per mercenary)
			if iRevoltTurns == 0:
				iNumUnitsInAPlot = splittingCity.plot().getNumUnits()
				iRevoltProtection = iNumUnitsInAPlot * 10
				if iNumUnitsInAPlot:
					for i in range(iNumUnitsInAPlot):
						iRevoltProtection += splittingCity.plot().getUnit(i).getRevoltProtection()
				iStability = self.getStability(iPlayer)
				if iStability < 0:
					iRevoltProtection = max(0, iRevoltProtection + iStability)
				if gc.getGame().getSorenRandNum(100, 'Revolt test') < iRevoltProtection:
					iRevoltTurns = gc.getGame().getSorenRandNum(4, 'Revolt turns')
			if iRevoltTurns > 0:
				splittingCity.changeCultureUpdateTimer(iRevoltTurns)
				splittingCity.changeOccupationTimer(iRevoltTurns)
				CyInterface().addMessage(iPlayer, False, con.iDuration, localText.getText("TXT_KEY_STABILITY_REVOLT", (splittingCity.getName(),)), "AS2D_CITY_REVOLT", InterfaceMessageTypes.MESSAGE_TYPE_MINOR_EVENT, ArtFileMgr.getInterfaceArtInfo("INTERFACE_RESISTANCE").getPath(), ColorTypes(con.iRed), splittingCity.getX(), splittingCity.getY(), True, True)
			else:
				return self.secedeCity(splittingCity)
			
		return False


	# edead
	def showPersecutionPopup(self):
		"""Asks the human player to select a religion to persecute."""
		
		popup = Popup.PyPopup(7626, EventContextTypes.EVENTCONTEXT_ALL)
		popup.setHeaderString("Religious Persecution")
		popup.setBodyString("Choose a religious minority to deal with...")
		religionList = sd.getPersecutionReligions()
		for iReligion in religionList:
			strIcon = gc.getReligionInfo(iReligion).getType()
			strIcon = "[%s]" %(strIcon.replace("RELIGION_", "ICON_"))
			strButtonText = "%s %s" %(localText.getText(strIcon, ()), gc.getReligionInfo(iReligion).getText())
			popup.addButton(strButtonText)
		popup.launch(False)


	def doPersecution(self, iX, iY, iUnitID, iReligion=None):
		"""Removes one religion from the city and handles the consequences."""
		
		pCity = gc.getMap().plot(iX, iY).getPlotCity()
		if pCity.isNone(): return False
		
		iOwner = pCity.getOwner()
		pPlayer = gc.getPlayer(iOwner)
		pUnit = pPlayer.getUnit(iUnitID)
		
		# chance to work: 
		iChance = 50
		if gc.getGame().getSorenRandNum(100, "purge chance") < iChance:
			
			iStateReligion = pPlayer.getStateReligion()
			
			# determine the target religion, if not supplied by the popup decision
			if not iReligion:
				for iReligion in con.tPersecutionOrder[iStateReligion]:
					if iReligion != iStateReligion and not pCity.isHolyCityByType(iReligion): # spare holy cities
						if pCity.isHasReligion(iReligion):
							break
			
			# remove a single non-state religion and its buildings from the city, count the loot
			iLootModifier = 2 * pCity.getPopulation() / pCity.getReligionCount() + 1
			iLoot = 2 + iLootModifier
			pCity.setHasReligion(iReligion, 0, 0, 0)
			for iBuildingLoop in range(gc.getNumBuildingInfos()):
				if iBuildingLoop < con.iPlague:
					if pCity.getNumRealBuilding(iBuildingLoop):
						if gc.getBuildingInfo(iBuildingLoop).getPrereqReligion() == iReligion:
							pCity.setNumRealBuilding(iBuildingLoop, 0)
							iLoot += iLootModifier
			if iReligion == con.iJudaism:
				iLoot = iLoot*3/2
			
			# kill / expel some population
			if pCity.getPopulation() > 3:
				pCity.changePopulation(-1)
			elif pCity.getPopulation() > 9:
				pCity.changePopulation(-2)
			elif pCity.getPopulation() > 14:
				pCity.changePopulation(-3)
			
			# distribute the loot
			iLoot = iLoot/2 + gc.getGame().getSorenRandNum(iLoot/2, 'random loot')
			pPlayer.changeGold(iLoot)
			
			# apply diplomatic penalty
			for iLoopPlayer in range(con.iNumPlayers):
				pLoopPlayer = gc.getPlayer(iLoopPlayer)
				if pLoopPlayer.isAlive() and iLoopPlayer != iOwner:
					if pLoopPlayer.getStateReligion() == iReligion:
						pLoopPlayer.AI_changeAttitudeExtra(iOwner, -1)
			
			CyInterface().addMessage(iOwner, False, con.iDuration, localText.getText("TXT_KEY_MESSAGE_INQUISITION", (pCity.getName(), gc.getReligionInfo(iReligion).getDescription(), iLoot)), "AS2D_PLAGUE", InterfaceMessageTypes.MESSAGE_TYPE_INFO, pUnit.getButton(), ColorTypes(con.iGreen), iX, iY, True, True)
		
		else: # fail
			CyInterface().addMessage(iOwner, False, con.iDuration, localText.getText("TXT_KEY_MESSAGE_INQUISITION_FAIL", (pCity.getName(), )), "AS2D_SABOTAGE", InterfaceMessageTypes.MESSAGE_TYPE_INFO, pUnit.getButton(), ColorTypes(con.iRed), iX, iY, True, True)
		
		# start a small revolt
		pCity.changeCultureUpdateTimer(1);
		pCity.changeOccupationTimer(1);
		
		# consume the inquisitor
		pUnit.kill(0, -1)
		
		# Unhappiness from persecution
		pCity.changeHurryAngerTimer(pCity.flatHurryAngerLength())
		
		return True


	# edead
	def doGreatSaintEffect(self, unit):
		"""Spreads state religion to up to 5 surrounding cities and consumes the unit."""
		
		iPlayer = unit.getOwner()
		pPlayer = gc.getPlayer(iPlayer)
		iReligion = pPlayer.getStateReligion()
		
		# loop through all cities and save city+distance tuples for those that don't have the religion
		cityValueList = []
		for iLoopPlayer in range(iNumTotalPlayers+1): # include barbarians
			apCityList = PyPlayer(iLoopPlayer).getCityList()
			for pCity in apCityList:
				city = pCity.GetCy()
				if city.isHasReligion(iReligion) or city.isNone():
					continue
				iDistance = self.calculateDistance(unit.getX(), unit.getY(), city.getX(), city.getY())
				cityValueList.append((city, iDistance))
		
		# sort cities from closest to farthest to the unit
		cityValueList.sort(key=itemgetter(1))
		
		# loop through the new city list and spread the religion 3-5 times
		iCount = 0
		for tCity in cityValueList:
			city = tCity[0]
			iDistance = tCity[1]
			#if gc.getPlayer(city.getOwner()).getCivics(4) != con.iPersecutionCivic:
			city.setHasReligion(iReligion, True, True, True)
			iCount += 1
			if iCount == 6 or (iCount == 5 and iDistance > 30) or (iCount == 4 and iDistance > 55) or (iCount == 3 and iDistance > 70):
				break
		
		# interface message
		if iCount > 0:
			szText = localText.getText("TXT_KEY_MINOR_EVENT_GREAT_SAINT_SUCCESS", (unit.getName(), iCount))
			CyInterface().addMessage(iPlayer, False, con.iDuration, szText, "AS2D_RELIGION_CONVERT", InterfaceMessageTypes.MESSAGE_TYPE_MINOR_EVENT, "", ColorTypes(con.iGreen), -1, -1, False, False)
		else:
			szText = localText.getText("TXT_KEY_MINOR_EVENT_GREAT_SAINT_FAILURE", (unit.getName(), ))
			CyInterface().addMessage(iPlayer, False, con.iDuration, szText, "AS2D_RELIGION_CONVERT", InterfaceMessageTypes.MESSAGE_TYPE_MINOR_EVENT, "", ColorTypes(con.iRed), -1, -1, False, False)
		
		# consume the Great Saint
		unit.kill(0, -1)



	
		
	# srpt Pilgrim
	def doPilgrimage(self, unit, iReligion):
	
		iPlayer = unit.getOwner()
		pPlayer = gc.getPlayer(iPlayer)
		pNewUnit = utils.makeUnit(con.iJewishMissionary + iReligion, iPlayer, (unit.getX(), unit.getY()), 1)
		pNewUnit.finishMoves()
		unit.kill(0, -1)
		

	# srpt silkworm stealing
	def doSilkworm(self, unit):
	
		sd.setSilkWorms(unit.getOwner(), 1)
		unit.setHasPromotion(con.iSilkworm, True)
		
	def doSilkwormCultivation(self, unit, iX, iY):
	
		gc.getMap().plot(iX,iY).setBonusType(con.iSilk)
		unit.setHasPromotion(con.iSilkworm, False)
		#if (unit.getOwner() == con.iByzantines):
			#sd.setGoal(con.iByzantines, 1, 1)


	# modified from CvExoticForeignAdvisor.py - edead
	def calculateRelations(self, nPlayer, nTarget):
		"""Returns the total value of diplomatic relations between nPlayer and nTarget."""
		
		if (nPlayer != nTarget and gc.getTeam(gc.getPlayer(nPlayer).getTeam()).isHasMet(gc.getPlayer(nTarget).getTeam())):
			nAttitude = 0
			szAttitude = CyGameTextMgr().getAttitudeString(nPlayer, nTarget)
			ltPlusAndMinuses = re.findall ("[-+][0-9]+\s?: ", szAttitude)
			for i in range (len (ltPlusAndMinuses)):
				nAttitude += int (ltPlusAndMinuses[i][:-2])
			return nAttitude
		else:
			return 0





	def findSeaPlots( self, tCoords, iRange, iCiv):
		"""Searches a sea plot that isn't occupied by a unit and isn't a civ's territory surrounding the starting coordinates."""
		
		seaPlotList = []
		for x in range(tCoords[0] - iRange, tCoords[0] + iRange+1):
			for y in range(tCoords[1] - iRange, tCoords[1] + iRange+1):	
				pCurrent = gc.getMap().plot( x, y )
				if ( pCurrent.isWater()):
					if ( not pCurrent.isUnit() ):
						#if (pCurrent.countTotalCulture() == 0 ):
						if (not (pCurrent.isOwned() and pCurrent.getOwner() != iCiv)):
							seaPlotList.append(pCurrent)
							# this is a good plot, so paint it and continue search
		if (len(seaPlotList) > 0):
			rndNum = gc.getGame().getSorenRandNum(len(seaPlotList), 'sea plot')
			result = seaPlotList[rndNum]
			if (result):
				return ((result.getX(), result.getY()))
		return (None)


	def checkRegionOwnedCity(self, iPlayer, regionID, bCoastal = False):
		"""Returns True if the region has a city owned by iPlayer."""
		
		plotList = self.getRegionPlotList([regionID])
		for tPlot in plotList:
				pCurrent = gc.getMap().plot(tPlot[0], tPlot[1])
				if pCurrent.isCity():
					if pCurrent.getPlotCity().getOwner() == iPlayer:
						if bCoastal:
							if pCurrent.getPlotCity().isCoastal(gc.getMIN_WATER_SIZE_FOR_OCEAN()):
								return True
						else:
							return True
		return False


	def checkRegionControl(self, iPlayer, regionID, bVassal = False):
		"""Returns True if the region has no cities other than iPlayer's.
		if bVassal is True, vassal cities are counted as iPlayer's."""
		
		bFound = False
		plotList = self.getRegionPlotList([regionID])
		for tPlot in plotList:
				pCurrent = gc.getMap().plot(tPlot[0], tPlot[1])
				if pCurrent.isCity():
					iOwner = pCurrent.getPlotCity().getOwner()
					if iOwner != iPlayer:
						if bVassal:
							if gc.getTeam(gc.getPlayer(iOwner).getTeam()).isVassal(iPlayer):
								bFound = True
							else:
								return False
						else:
							return False
					else:
						bFound = True
		if bFound:
			return True
		else:
			for tPlot in plotList:
				pCurrent = gc.getMap().plot(tPlot[0], tPlot[1])
				iOwner = pCurrent.getOwner()
				if iOwner != iPlayer:
					bFound = False
					break
				else:
					bFound = True
			if bFound:
				return True
			else:
				return False
				
	def checkRegionCultureCoverage(self, iPlayer, regionID, bVassal = False):
		"""Returns True if the region is completely covered by iPlayer's culture."""
		
		bFound = False
		plotList = self.getRegionPlotList([regionID])
		for tPlot in plotList:
			pCurrent = gc.getMap().plot(tPlot[0], tPlot[1])
			iOwner = pCurrent.getOwner()
			if iOwner != iPlayer:
				bFound = False
				break
			else:
				bFound = True
		if bFound:
			return True
		else:
			return False
				
	def checkRegionHasCity(self, regionID):
	
		plotList = self.getRegionPlotList([regionID])
		for tPlot in plotList:
				pCurrent = gc.getMap().plot(tPlot[0], tPlot[1])
				if pCurrent.isCity():
					return True
		return False

	def canCollapse(self, iPlayer):
	
		if iPlayer == con.con.iMauryans and sd.getCivilization(con.con.iMauryans) == con.iSungas and gc.getMap().plot(con.tPataliputra[0],con.tPataliputra[1]).getOwner() == con.con.iMauryans and utils.getHumanID() in [con.iTocharians, con.iVietnam, con.iPandyans, con.iGoguryeo]: # keep Buddhist Holy City/Shrine open for Pilgrims/Teachers
			return False
		
		if iPlayer == con.iRome and not (gc.getPlayer(con.iRome).isPlayable()) and gc.getGame().getGameTurn() <= getTurnForYear(340): # no collapse before Byzantine spawn in 220AD scenario
			return False
		
		# stops rare cases of civs collapsing instantly after resurrection
		if gc.getGame().getGameTurn() < sd.getLatestRebellionTurn(iPlayer) + self.getTurns(20):
			return False
		
		return True





	def getBaseUnit(self, iUnit, iNewOwner):
	
		iUnitClass = gc.getUnitInfo(iUnit).getUnitClassType()
		if iNewOwner >= con.iNumPlayers:
			return iUnit
		else:
			iBaseUnit = gc.getCivilizationInfo(sd.getCivilization(iNewOwner)).getCivilizationUnits(iUnitClass) # srpt flipped units convert to UUs where applicable

		
		
		if iBaseUnit == -1:
			return iUnit
		else:
			return iBaseUnit

			
	def getRandomCityByRegion(self, lRegions):
		"""Returns a city located in any of the listed regions."""
		
		cityList = []
		for iPlayer in range(iNumTotalPlayers):
			for pyCity in PyPlayer(iPlayer).getCityList():
				pCurrent = gc.getMap().plot(pyCity.getX(), pyCity.getY())
				if pCurrent.getRegionID() in lRegions:
					cityList.append(pyCity.GetCy())
		if len(cityList):
			iCity = gc.getGame().getSorenRandNum(len(cityList), 'random city')
			return cityList[iCity]
		return None
		
	def getRandomMinorCityByRegion(self, lRegions):
		"""Returns a city located in any of the listed regions."""
		cityList = []
		for iPlayer in range(iNumPlayers, iNumTotalPlayers):
			for pyCity in PyPlayer(iPlayer).getCityList():
				pCurrent = gc.getMap().plot(pyCity.getX(), pyCity.getY())
				if pCurrent.getRegionID() in lRegions:
					cityList.append(pyCity.GetCy())
		if len(cityList):
			iCity = gc.getGame().getSorenRandNum(len(cityList), 'random city')
			return cityList[iCity]
		return None

	
	# From RFCE
	def getRandomCityByReligion(self, iReligion):
		
		if (gc.getGame().isReligionFounded(iReligion)):
			cityList = []
			for iPlayer in range(iNumTotalPlayers):
				for pyCity in PyPlayer(iPlayer).getCityList():
					if pyCity.GetCy().isHasReligion(iReligion):
						cityList.append(pyCity.GetCy())
			iCity = gc.getGame().getSorenRandNum(len(cityList), 'random city')
			return cityList[iCity]
		return None
		
	def getRandomPaganCityByRegion(self, lRegions):
		"""Returns a city located in any of the listed regions."""
		
		cityList = []
		for iPlayer in range(iNumTotalPlayers):
			for pyCity in PyPlayer(iPlayer).getCityList():
				pCurrent = gc.getMap().plot(pyCity.getX(), pyCity.getY())
				if pCurrent.getRegionID() in lRegions:
					bPagan = True
					for iReligion in range(iNumReligions):
						if pyCity.GetCy().isHasReligion(iReligion):
							bPagan = False
					if bPagan == True:
						cityList.append(pyCity.GetCy())
		if len(cityList):
			iCity = gc.getGame().getSorenRandNum(len(cityList), 'random city')
			return cityList[iCity]
		return None
	
	
	def canBetray(self, iUnitType, iReligion):
	
		
		return True
	
	
	def toggleStabilityOverlay(self):
		
		engine = CyEngine()
		
		# clear the highlight
		engine.clearColoredPlots(PlotLandscapeLayers.PLOT_LANDSCAPE_LAYER_WORLD_BUILDER)
		
		if self.bStabilityOverlay:
			self.bStabilityOverlay = False
			CyGInterfaceScreen("MainInterface", CvScreenEnums.MAIN_INTERFACE).setState("StabilityOverlay", False)
			return
		
		self.bStabilityOverlay = True
		CyGInterfaceScreen("MainInterface", CvScreenEnums.MAIN_INTERFACE).setState("StabilityOverlay", True)
		
		# set up colors
		colors = []
		colors.append("COLOR_HIGHLIGHT_FOREIGN")
		colors.append("COLOR_HIGHLIGHT_OUTSIDE")
		colors.append("COLOR_HIGHLIGHT_CONTESTED")
		colors.append("COLOR_HIGHLIGHT_BORDER")
		colors.append("COLOR_HIGHLIGHT_CORE")
		
		iHuman = self.getHumanID()
		iHumanTeam = gc.getPlayer(iHuman).getTeam()
		
		# apply the highlight
		for x in range(con.iMapWidth):
			for y in range(con.iMapHeight):
				pCurrent = gc.getMap().plot(x,y)
				if gc.getGame().isDebugMode() or pCurrent.isRevealed(iHumanTeam, False):
					if pCurrent.isWater():
						szColor = "COLOR_GREY"
					else:
						szColor = colors[self.getRegionStabilityLevel(iHuman, pCurrent.getRegionID())]
					engine.addColoredPlotAlt(x, y, int(PlotStyles.PLOT_STYLE_BOX_FILL), int(PlotLandscapeLayers.PLOT_LANDSCAPE_LAYER_WORLD_BUILDER), szColor, .2)
	
	
	def getMaster(self, iCiv):
		team = gc.getTeam(gc.getPlayer(iCiv).getTeam())
		for iMaster in range(iNumTotalPlayers):
			if team.isVassal(iMaster):
				return iMaster
	
	
	def uniq(self, alist):
		set = {}
		return [set.setdefault(e,e) for e in alist if e not in set]
		
	def isRegionFree(self, RegionID):
		bFree = true
		for p in range (iNumPlayers):
			if self.checkRegionOwnedCity(p, RegionID):
				bFree = false
				break
		return bFree
		
	def getRegionName(self, regionID):
		'Returns the region name of a plot.'
		map = gc.getMap()
		for i in range(map.numPlots()):
			plot = map.plotByIndex(i)
			if plot.getRegionID() == regionID:
				return plot.getRegionName(False)
		return ""
		
	def clearCulture(self, iPlayer):
		for x in range(iMapWidth):
			for y in range(iMapHeight):
				gc.getMap().plot(x, y).setCulture(iPlayer, 0, false)
				
	def findPlayerReverseLookup(self, iCiv):
		for iLoop in range(iNumPlayers):
			if sd.getCivilization(iLoop) == iCiv:
				return iLoop
			
	def printmap(bPeaks=True):
		for y in range(con.iMapHeight-1, -1, -1):
			row = ''
			for x in range(con.iMapWidth):
				plot = gc.getMap().plot(x,y)
				if plot.isWater(): row += '0;'
				else:
					if bPeaks and plot.isPeak(): row += '2;'
					else: row += '1;'
			print(row)
		
		
	def printCityNameMap(self):
	
		tMap = [[0 for i in range(con.iMapHeight)] for j in range(con.iMapWidth)]
		### insert prepared list here: ###
		### How to prepare the sign info:
		#1. trim leading space
		#2. insert 8 spaces
		#3. space to TAB
		#4. replace "B" with "#B" and "E" with "#E"
		#5. replace "plot" with "i"
		#6. replace "caption" with "tMap[iX][iY]"
		
		for iH in range(con.iMapHeight-1, -1, -1):
			row = ''
			for iW in range(con.iMapWidth):
				row += str(tMap[iW][iH]) + ","
			print(row)
			
	def canDeclareWar(self, iCiv, iTarget):
		
		bWar = True
		
		if gc.getTeam(gc.getPlayer(iCiv).getTeam()).isAtWar(iTarget) : bWar = False
		if gc.getTeam(gc.getPlayer(iCiv).getTeam()).isVassal(iTarget) : bWar = False
		if gc.getTeam(gc.getPlayer(iTarget).getTeam()).isVassal(iCiv) : bWar = False
		if iCiv == con.iRome and iTarget == con.iByzantines: bWar = False
		if iCiv == con.iByzantines and iTarget ==con.iRome: bWar = False
		if not gc.getPlayer(iCiv).canContact(iTarget) and iTarget < iNumPlayers: bWar = False
		
		return bWar
		
	def getWarCount(self, iPlayer):
	
		print "getWarCount"
		print ("iPlayer", iPlayer)
	
		iCount =0
		for iLoopCiv in range(iNumPlayers):
			if iLoopCiv != iPlayer:
				if gc.getTeam(gc.getPlayer(iPlayer).getTeam()).isAtWar(iLoopCiv):
					print ("iLoopCiv", iLoopCiv)
					iCount += 1
		return iCount
		
	def findRemotestCity(self, iPlayer, bRevolt = False):
		'''finds the city furthest from the capital'''
		
		apCityList = PyPlayer(iPlayer).getCityList()
		capital = gc.getPlayer(iPlayer).getCapitalCity()
		iCapitalX = capital.getX()
		iCapitalY = capital.getY()
		iDistance = 0
		city = None
		for pLoopCity in apCityList:
			if not pLoopCity.isCapital():
				if abs(pLoopCity.getX() - iCapitalX) > iDistance or abs(pLoopCity.getY() - iCapitalY) > iDistance :
					if (bRevolt == False) or (pLoopCity.GetCy().getOccupationTimer() == 0):
						iDistance = max((pLoopCity.getX() - iCapitalX), (pLoopCity.getY() - iCapitalY))
						city = pLoopCity
		return city
		
	def findRemotestProvince(self, iPlayer):
	
		print ("findRemotestProvince", iPlayer)
	
		capital = gc.getPlayer(iPlayer).getCapitalCity()
		iCapitalX = capital.getX()
		iCapitalY = capital.getY()
		#print ("capital", iCapitalX, iCapitalY)
		iDistance = 0
		regionList = []
		remoteRegionID = None
		regionCityList = []
		
		apCityList = PyPlayer(iPlayer).getCityList()
		for pCity in apCityList:
			regionID = gc.getMap().plot(pCity.getX(), pCity.getY()).getRegionID()
			if regionID not in regionList and regionID not in lCoreRegions[sd.getCivilization(iPlayer)]:
				regionList.append(regionID)
	
		for regionID in regionList:
			iTempDistance = 0
			plotList = self.getRegionPlotList([regionID])
			for i in range(len(plotList)):
				pCurrent = gc.getMap().plot(plotList[i][0], plotList[i][1])
				if (pCurrent.isCity()) and (pCurrent.getPlotCity().getOwner() == iPlayer):
					regionCityList.append(pCurrent.getPlotCity())
				iNewDistance = abs((plotList[i][0]) - iCapitalX) > iDistance or abs((plotList[i][1]) - iCapitalY)
				if iNewDistance > iTempDistance:
					iTempDistance = iNewDistance

					
			if iTempDistance > iDistance:
				iTempDistance = iDistance
				remoteRegionID = regionID				
			else: 
				regionCityList = []
				
		return (remoteRegionID, regionCityList)
		
	def areDividedByRiver(self, tStartingPlot, tDestinationPlot):
	
		bCrossing = False
		eDirectionType = DirectionTypes.DIRECTION_NORTHEAST
		
		if (abs(tStartingPlot[0] - tDestinationPlot[0]) > 1) or (abs(tStartingPlot[1] - tDestinationPlot[1]) > 1):
			print "out of range"
			return
		elif tStartingPlot[1] < tDestinationPlot[1]: # dest is N of start
			if tStartingPlot[0] > tDestinationPlot[0]: # dest is NE of start
				eDirectionType = DirectionTypes.DIRECTION_NORTHEAST
				if gc.getMap().plot(tStartingPlot[0], tStartingPlot[1]).isRiverCrossing(DirectionTypes.DIRECTION_NORTHEAST):
					bCrossing = True
			elif tStartingPlot[0] < tDestinationPlot[0]: # dest is due N of start
				eDirectionType = DirectionTypes.DIRECTION_NORTH
				if gc.getMap().plot(tStartingPlot[0], tStartingPlot[1]).isRiverCrossing(DirectionTypes.DIRECTION_NORTH):
					bCrossing = True
			elif tStartingPlot[0] > tDestinationPlot[0]: # dest is NW of start
				eDirectionType = DirectionTypes.DIRECTION_NORTHWEST
				if gc.getMap().plot(tStartingPlot[0], tStartingPlot[1]).isRiverCrossing(DirectionTypes.DIRECTION_NORTHWEST):
					bCrossing = True
					
		elif tStartingPlot[1] == tDestinationPlot[1]: # dest level with start
			if tStartingPlot[0] > tDestinationPlot[0]: # dest is due E of start
				eDirectionType = DirectionTypes.DIRECTION_EAST
				if gc.getMap().plot(tStartingPlot[0], tStartingPlot[1]).isRiverCrossing(DirectionTypes.DIRECTION_EAST):
					bCrossing = True
			elif tStartingPlot[0] > tDestinationPlot[0]: # dest is due W of start
				eDirectionType = DirectionTypes.DIRECTION_WEST
				if gc.getMap().plot(tStartingPlot[0], tStartingPlot[1]).isRiverCrossing(DirectionTypes.DIRECTION_WEST):
					bCrossing = True
					
		elif tStartingPlot[1] > tDestinationPlot[1]: # dest is S of start
			if tStartingPlot[0] > tDestinationPlot[0]: # dest is SE of start
				eDirectionType = DirectionTypes.DIRECTION_SOUTHEAST
				if gc.getMap().plot(tStartingPlot[0], tStartingPlot[1]).isRiverCrossing(DirectionTypes.DIRECTION_SOUTHEAST):
					bCrossing = True
			elif tStartingPlot[0] == tDestinationPlot[0]: # dest is due S of start
				print "dest is due S of start"
				eDirectionType = DirectionTypes.DIRECTION_SOUTH
				if gc.getMap().plot(tStartingPlot[0], tStartingPlot[1]).isRiverCrossing(DirectionTypes.DIRECTION_SOUTH):
					bCrossing = True
			elif tStartingPlot[0] > tDestinationPlot[0]: # dest is SW of start
				eDirectionType = DirectionTypes.DIRECTION_SOUTHWEST
				if gc.getMap().plot(tStartingPlot[0], tStartingPlot[1]).isRiverCrossing(DirectionTypes.DIRECTION_SOUTHWEST):
					bCrossing = True
					
		return bCrossing , eDirectionType
		
	def getSpawnChance(self, iGameTurn, iSpawnYear):
	
		iYear = getTurnForYear(iGameTurn)
		if (iSpawnYear -30) < iYear > iSpawnYear:
			if gc.getGame().getSorenRandNum(30, 'random number') > abs(iSpawnYear - iYear):
				return True
		return False
		
	def stabilityCheck(self, iPlayer, iAdjustment = 0):
	
		print "stabilityCheck called"
		
		print ("iPlayer =", iPlayer)
	
		#CyInterface().addMessage(utils.getHumanID(), True, iDuration, CyTranslator().getText("STABILITY CHECK", ()) + " " + gc.getPlayer(iPlayer).getCivilizationDescription(0), "", 0, "", ColorTypes(iRed), -1, -1, True, True)
		if (iPlayer > iNumPlayers):
			return
		pPlayer = gc.getPlayer(iPlayer)
		pTeam = gc.getTeam(pPlayer.getTeam())
		apCityList = PyPlayer(iPlayer).getCityList()
		iCiv = sd.getCivilization(iPlayer)
		iGameTurn = gc.getGame().getGameTurn()
		iCivicGovernment = pPlayer.getCivics(0)
		iCivicLegal = pPlayer.getCivics(1)
		iCivicLabor = pPlayer.getCivics(2)
		iCivicReligion = pPlayer.getCivics(4)
		iHuman = utils.getHumanID()
		iStateReligion = pPlayer.getStateReligion()
		
		# calibrate the system here:
		#iAdjustment -= 1
		
		if utils.getYear() > con.tFall[iCiv]:
			iAdjustment -= 3
			
		if pPlayer.getNumCities <= 1:
			print "pass on 1 city or none"
			return
		
		if iPlayer == con.iRome and (con.tBirth[con.iByzantines] + 20) > utils.getYear() > (con.tBirth[con.iByzantines] - 20):
			print "pass on Byzantine birth"
			return
		
		
		
		if (iGameTurn < getTurnForYear(con.tBirth[iPlayer]) + 30):
			print "pass, too early"
			return
			
		if (pPlayer.getAnarchyTurns() > 0):
			print "pass, anarchy"
			return
			
		if (pPlayer.getGoldenAgeTurns()) > 0:
			print "pass, golden age"
			return
			
		if iGameTurn < getTurnForYear(con.tFall[iCiv]):
			if (sd.getLastRebellion(iPlayer)) > utils.getYear() - 30:
				print "pass, recent rebellion"
				return
		else:
			if (sd.getLastRebellion(iPlayer)) > utils.getYear() - 10:
				print "pass, recent rebellion"
				return
		

		sd.setLastRebellion(iPlayer, utils.getYear())

		
		## CIVICS ##
		
		# combinations of civics and state religions
		
		# Civics
		print "CIVICS"
		
		iCivicsRating = sd.getCivicsStability(iPlayer)
		
		print ("iCivicsRating=", iCivicsRating)
		
		

			
		## HAPPINESS AND HEALTH ##
		print "HEALTH & HAPPINESS"
		# balance of health and happiness per city, with extra penalty for angry citizens
		
		iNumCities = pPlayer.getNumCities()
		if iNumCities < 1: iNumCities =1
		
		iHappinessAndHealthRating = 0
		print ("total happy", pPlayer.calculateTotalCityHappiness(), "total unhappy", pPlayer.calculateTotalCityUnhappiness(), "cities", iNumCities)
		print ("total health", pPlayer.calculateTotalCityHealthiness(), "total unhealth", pPlayer.calculateTotalCityUnhealthiness(), "cities", iNumCities)
		iHappiness = ((pPlayer.calculateTotalCityHappiness()) - (pPlayer.calculateTotalCityUnhappiness())) / (iNumCities)
		iHealth = ((pPlayer.calculateTotalCityHealthiness()) - (pPlayer.calculateTotalCityUnhealthiness())) / (iNumCities)
		print ("iHappiness=", iHappiness, "iHealth=", iHealth)
		
		if iHappiness < 0: iHappinessAndHealthRating -= 1
		elif iHappiness > 3: iHappinessAndHealthRating += 1
		
		if iHealth < 0: iHappinessAndHealthRating -= 1
		elif iHealth > 3: iHappinessAndHealthRating += 1
		
		if iPlayer == iHuman: # I think this kills the AI unfairly
			for pLoopCity in apCityList:
				if (pLoopCity.GetCy().angryPopulation(0) > 0): 
					iHappinessAndHealthRating -= 1
					print "angry city"
					
		print ("iHappinessAndHealthRating", iHappinessAndHealthRating)
		
		## ECONOMY ##
		print "ECONOMY"
		# balance of income and costs
		
		iEconomyRating = 0
		
		iRate = (pPlayer.calculateGoldRate() + pPlayer.calculateBaseNetResearch()) - (pPlayer.calculateInflatedCosts())
		print ("gold=", pPlayer.calculateGoldRate(), "research=", pPlayer.calculateBaseNetResearch(), "costs=", pPlayer.calculateInflatedCosts(), "iRate", iRate)
		
		if iRate < -300: iEconomyRating -= 4
		elif iRate < -200: iEconomyRating -= 3
		elif iRate < -100: iEconomyRating -= 2
		elif iRate < -20: iEconomyRating -= 1
		elif iRate > +10: iEconomyRating += 1
		elif iRate > +30: iEconomyRating += 2
		
		
		iEconomy = pPlayer.calculateTotalYield(YieldTypes.YIELD_COMMERCE) - pPlayer.calculateInflatedCosts()
		iIndustry = pPlayer.calculateTotalYield(YieldTypes.YIELD_PRODUCTION)
		iAgriculture = pPlayer.calculateTotalYield(YieldTypes.YIELD_FOOD)
		
		iGrowth = iEconomy + iIndustry + iAgriculture
			
			
		if iGrowth * 2 < sd.getOldEconomyRating(iPlayer): 
			iEconomyRating -= 3 
			print "high economic decline"
		elif iGrowth * 4 < sd.getOldEconomyRating(iPlayer) * 3: 
			iEconomyRating -= 2 
			print "med economic decline"
		elif iGrowth < sd.getOldEconomyRating(iPlayer): 
			iEconomyRating -= 1
			print "some economic decline"
		
		sd.setOldEconomyRating(iPlayer, iGrowth)
		
		print ("iEconomyRating", iEconomyRating)
			

			
		## EMPIRE ##
		print "EMPIRE"
		# balance of core and empire populations, mitigated by courthouses and civics
		
		iEmpireRating = 0
		bExiled = True
		for regionID in utils.getCoreRegions(iCiv):
			if (utils.checkRegionOwnedCity(iPlayer, regionID)): 
				bExiled = False
			if not (utils.checkRegionControl(iPlayer, regionID)):
				iEmpireRating -= 3
				print "core province not controlled"
		if bExiled:
			print "Exiled"
			if utils.getYear() > con.tFall[iCiv] or pPlayer.getNumCities() <= 3:
				self.terminalCrisis(iPlayer, iCiv, pPlayer, pTeam)
			else:
				iEmpireRating -= 6
				
		iCorePop = 0
		iEmpirePop = 0
		for pLoopCity in apCityList:
			if not pLoopCity.isNone(): 
				if pLoopCity.GetCy().isCapital():
					iCorePop += pLoopCity.getPopulation() * 3
				else:
					regionID = gc.getMap().plot(pLoopCity.GetCy().getX(),pLoopCity.GetCy().getY()).getRegionID()
					if regionID in utils.getCoreRegions(iCiv) or regionID in utils.getSpecialRegions(iCiv): 
						iCorePop += pLoopCity.getPopulation() * 2
					else:
						iFactor = 1
						if not ((iCivicGovernment == con.iTheocracyCivic) and (pLoopCity.GetCy().isHasReligion(iStateReligion))):
							if iCivicGovernment != con.iEmpireCivic: iFactor += 1
						if not (iCivicLegal == con.iBureaucracyCivic):
							iFactor += 1
						if pLoopCity.GetCy().getX() != 13 and pLoopCity.GetCy().getY() != 44: # C++ exception here
							if not (pLoopCity.GetCy().getNumRealBuilding(con.iCourthouse)): 
								if not (pLoopCity.GetCy().getNumRealBuilding(con.iVisigothSynod)): 
									if not (pLoopCity.GetCy().getNumRealBuilding(con.iVietnamCommunalHouse)): 
										if not (pLoopCity.GetCy().getNumRealBuilding(con.iFrankDukeResidence)): 
											iFactor += 1
						if not regionID in utils.getNormalRegions(iCiv):
							iFactor += 1
						iEmpirePop += pLoopCity.getPopulation() * iFactor
			
		print ("iCorePop=", iCorePop, "iEmpirePop=", iEmpirePop)
		
		if iCorePop > iEmpirePop *2: iEmpireRating += 2
		elif iCorePop > iEmpirePop: iEmpireRating += 1
		elif iCorePop *5 < iEmpirePop: iEmpireRating -= 5
		elif iCorePop *4 < iEmpirePop: iEmpireRating -= 4
		elif iCorePop *3 < iEmpirePop: iEmpireRating -= 3
		elif iCorePop *2 < iEmpirePop: iEmpireRating -= 2
		elif iCorePop < iEmpirePop: iEmpireRating -= 1
				
		if (pPlayer.getNumCities()) * 2 < (sd.getNumCities(iPlayer)): 
			iEmpireRating -= 3
			print "high city losses"
		elif (pPlayer.getNumCities()) * 3 < (sd.getNumCities(iPlayer)) * 2: 
			iEmpireRating -= 2
			print "med city losses"
		elif pPlayer.getNumCities() < sd.getNumCities(iPlayer): 
			iEmpireRating -= 1
			print "some losses"
		
		print ("iEmpireRating=", iEmpireRating)
		
		## RELIGION ##
		print "RELIGION"
		iReligionRating = 0
		iNumForeignReligions = 0
		iNumNonbelievingCities = 0
		
		if (iCivicReligion == con.iDynasticCultCivic) or (iCivicReligion == con.iPaganismCivic): 
			for pLoopCity in apCityList:
				for iLoopReligion in range(iNumReligions):
					if pLoopCity.GetCy().isHasReligion(iLoopReligion):
						if iLoopReligion != con.iHinduism: 
							iNumForeignReligions += 1
						elif iLoopReligion == con.iHinduism and iCivicLabor != con.iCasteSystemCivic:
							iNumForeignReligions += 1
		elif iCivicReligion == con.iStateReligionCivic: 
			for pLoopCity in apCityList:
				if not pLoopCity.GetCy().isHasReligion(iStateReligion):
					iNumNonbelievingCities += 2
				for iLoopReligion in range(iNumReligions):
					if pLoopCity.GetCy().isHasReligion(iLoopReligion) and iLoopReligion != iStateReligion:
						iNumForeignReligions += 1
		elif (iCivicReligion == con.iMilitancyCivic) or (iCivicGovernment == con.iTheocracyCivic): 
			for pLoopCity in apCityList:
				if not pLoopCity.GetCy().isHasReligion(iStateReligion):
					iNumNonbelievingCities += 2
				for iLoopReligion in range(iNumReligions):
					if pLoopCity.GetCy().isHasReligion(iLoopReligion) and iLoopReligion != iStateReligion:
						iNumForeignReligions += 2
						
		print ("iNumForeignReligions", iNumForeignReligions, "iNumNonbelievingCities", iNumNonbelievingCities, "iNumCities", iNumCities)
						
		if iNumNonbelievingCities *2 > iNumCities: iReligionRating -= 2
		elif iNumNonbelievingCities *4 > iNumCities: iReligionRating -= 1
		
		if iNumForeignReligions > iNumCities *2: iReligionRating -= 2
		elif iNumForeignReligions > iNumCities: iReligionRating -= 1
		
		print ("iReligionRating=", iReligionRating)
		
		print "TOTALS"
		print ("Civics:", iCivicsRating, "Health & Happiness:", iHappinessAndHealthRating, "Economy:", iEconomyRating, "Empire:", iEmpireRating, "Religion:", iReligionRating)
		print ("Total:", iCivicsRating + iHappinessAndHealthRating + iEconomyRating + iEmpireRating + iReligionRating)
		#iAdjustment = 3
		print ("iAdjustment=", iAdjustment)
		
		iStability = iCivicsRating + iHappinessAndHealthRating + iEconomyRating + iEmpireRating + iReligionRating + iAdjustment
		if iPlayer == con.iByzantines: 
			if iPlayer == iHuman:
				iStability += 3 # Byzantine UP
			else:
				iStability += 6 # Byzantine UP
		#if iGameTurn > getTurnForYear(con.tFall[iCiv]): iStability -= 3
		
		### RESULTS ###
		print "RESULT"

		if pTeam.isHasTech(con.iStabilityCollapsing):
			if iStability < -3:
				if iGameTurn > getTurnForYear(con.tFall[iCiv]) and iPlayer != iHuman:
					print ("already collapsing, terminal crisis, iCiv=", iCiv)
					self.terminalCrisis(iPlayer, iCiv, pPlayer, pTeam)
					return
				else:
					print ("already collapsing, severe crisis, iCiv=", iCiv)
					#self.severeCrisis(iPlayer, iCiv, pPlayer, pTeam)
					self.majorCrisis(iPlayer, iCiv, pPlayer, pTeam, 6)
					return
			elif iStability < 3:
				print ("stability flat at collapsing, major crisis, iCiv=", iCiv)
				#self.moderateCrisis(iPlayer, iCiv, pPlayer, pTeam)
				self.majorCrisis(iPlayer, iCiv, pPlayer, pTeam, 3)
			elif iStability > 3:
				print ("upgrade from collapsing to unstable, iCiv=", iCiv)
				pTeam.setHasTech(con.iStabilityCollapsing, False, iPlayer, False, False)
				pTeam.setHasTech(con.iStabilityUnstable, True, iPlayer, False, False)
				return
				
		elif pTeam.isHasTech(con.iStabilityUnstable):
			if iStability < -6:
				if iGameTurn > getTurnForYear(con.tFall[iCiv]) and iPlayer != iHuman:
					print ("unstable and past fall, terminal crisis, iCiv=", iCiv)
					pTeam.setHasTech(con.iStabilityUnstable, False, iPlayer, False, False)
					pTeam.setHasTech(con.iStabilityCollapsing, True, iPlayer, False, False)
					#self.severeCrisis(iPlayer, iCiv, pPlayer, pTeam)
					self.terminalCrisis(iPlayer, iCiv, pPlayer, pTeam)
					return
				else:
					print ("downgrade from unstable to collapsing, major crisis, iCiv=", iCiv)
					pTeam.setHasTech(con.iStabilityUnstable, False, iPlayer, False, False)
					pTeam.setHasTech(con.iStabilityCollapsing, True, iPlayer, False, False)
					#self.moderateCrisis(iPlayer, iCiv, pPlayer, pTeam)
					self.majorCrisis(iPlayer, iCiv, pPlayer, pTeam, 3)
					return
			elif iStability <= 0:
				print ("stability flat at unstable, minor crisis, iCiv=", iCiv)
				self.minorCrisis(iPlayer, iCiv, pPlayer, pTeam)
				return
			else:
				print ("stability upgrade from unstable to stable, no crisis, iCiv=", iCiv)
				pTeam.setHasTech(con.iStabilityUnstable, False, iPlayer, False, False)
				pTeam.setHasTech(con.iStabilityStable, True, iPlayer, False, False)
				return
		else:
			#if iStability < -6:
				#print ("downgrade from stable to unstable, minor crisis, iCiv=", iCiv)
				#pTeam.setHasTech(iStabilityStable, False, iPlayer, False, False)
				#pTeam.setHasTech(iStabilityUnstable, True, iPlayer, False, False)
				#self.minorCrisis(iPlayer, iCiv, pPlayer, pTeam)
				#return
			if iStability < -3:
				print ("downgrade from stable to unstable, no crisis, iCiv=", iCiv)
				pTeam.setHasTech(con.iStabilityStable, False, iPlayer, False, False)
				pTeam.setHasTech(con.iStabilityUnstable, True, iPlayer, False, False)
				if iPlayer == iHuman:
					CyInterface().addMessage(iHuman, True, con.iDuration, CyTranslator().getText("Your civilization has become unstable!", ()), "", 0, "", ColorTypes(con.iRed), -1, -1, True, True)
					#CyInterface().addMessage(utils.getHumanID(), True, iDuration, CyTranslator().getText("Your civilization has become unstable!", "", 0, "", ColorTypes(iRed), -1, -1, True, True))
				return
			else: 
				print ("stability flat at stable, no crisis, iCiv=", iCiv)

					
			
		
	def minorCrisis(self, iPlayer, iCiv, pPlayer, pTeam): # brief anarchy, revolts in provinces
		self.secedeDistantCities(iPlayer, iCiv)
		sd.setLastRebellion(iPlayer, utils.getYear())
		iCrisis = gc.getGame().getSorenRandNum(3, 'number') + 1
		
		pPlayer.changeAnarchyTurns(iCrisis)
		
		while iCrisis >=1:
			if utils.findRemotestCity(iPlayer, True) != None:
				utils.findRemotestCity(iPlayer, True).GetCy().changeOccupationTimer(iCrisis + 1);
				iCrisis -= 1
			else:
				iCrisis = 0
			
		
		#apCityList = PyPlayer(iPlayer).getCityList()
		#gc.getPlayer(iPlayer).changeAnarchyTurns(iCrisis - 1)
		#for pLoopCity in apCityList:
			#if gc.getMap().plot(pLoopCity.getX(), pLoopCity.getY()).getRegionID() not in utils.getCoreRegions(iCiv):
				#if gc.getGame().getSorenRandNum(6, 'number') > iCrisis:
					#pLoopCity.GetCy().changeOccupationTimer(iCrisis + 1);
		#return
		
	def majorCrisis(self, iPlayer, iCiv, pPlayer, pTeam, iCrisis):
		self.secedeDistantCities(iPlayer, iCiv)
		sd.setLastRebellion(iPlayer, utils.getYear())
		
		if iPlayer == con.iMauryans and iCiv == con.iMauryans and utils.checkRegionOwnedCity(con.iMauryans, con.rMagadha) and con.iMauryans != utils.getHumanID() and utils.getYear() < con.tFall[con.iSungas]:
			self.sungaRevolution()
	
		iCrisis += gc.getGame().getSorenRandNum(3, 'number')
		if utils.getYear() > con.tFall[iCiv]:
			iCrisis += (utils.getYear() - con.tFall[iCiv]) / 50
		iSuccessions = iCrisis / 3
		iRevolts = iCrisis
		
		pPlayer.changeAnarchyTurns(iCrisis)
		
		while iSuccessions >= 1:
			if utils.findRemotestCity(iPlayer) != None:
				utils.secedeCity(utils.findRemotestCity(iPlayer).GetCy())
				iSuccessions -= 1
				iRevolts -= 1
			else:
				iSuccessions = 0
		else:
			while iRevolts >= 1:
				if utils.findRemotestCity(iPlayer, True) != None:
					utils.findRemotestCity(iPlayer, True).GetCy().changeOccupationTimer(iRevolts + 1);
					iRevolts -= 1
				else:
					iRevolts = 0
		
	def moderateCrisis(self, iPlayer, iCiv, pPlayer, pTeam): # longer anarchy, rebellions in provinces, Sungas, Roman civil wars
		self.secedeDistantCities(iPlayer, iCiv)
		#if iPlayer == iRome and not gc.getPlayer(iByzantines).isAlive() and utils.getHumanID() != iByzantines and sd.getRomanRebellions() < 2 and utils.getYear() < (tBirth[iByzantines] - 20):
			#sd.setRomanRebellions(sd.getRomanRebellions() + 1)
			#if iPlayer == utils.getHumanID():
				#rfccwaiw.startRomanCivilWarPopup(iRome)
			#else:
				#rfccwaiw.startRomanCivilWar()
				#return
		#elif iPlayer == iByzantines and sd.getCivilization(iByzantines) == iRebelRome:
			#rfccwaiw.endRomanCivilWar()
		if iPlayer == con.iMauryans and iCiv == con.iMauryans and utils.checkRegionOwnedCity(con.iMauryans, con. rMagadha) and con.iMauryans != utils.getHumanID() and utils.getYear() < con.tFall[con.iSungas]:
			self.sungaRevolution()
		elif iPlayer == con.iQin and gc.getPlayer(iHan).isAlive() and sd.getCivilization(con.iQin) == con.iQin and utils.getHumanID() != con.iQin and utils.getHumanID() != con.iHan:
			self.terminalCrisis(iPlayer, iCiv, pPlayer, pTeam)
			gc.getTeam(gc.getPlayer(iHan).getTeam()).setHasTech(con.iStabilityStable, True, iPlayer, False, False)
		else:
			iCrisis = gc.getGame().getSorenRandNum(3, 'number') + 3
			if utils.getYear() > con.tFall[iCiv]:
				iCrisis += (utils.getYear() - con.tFall[iCiv]) / 50
			iSuccessions = iCrisis / 3
			pPlayer.changeAnarchyTurns(iCrisis + 1)
			iRevolts = iCrisis
			#print ("iSuccessions ", iSuccessions)
			#print ("iRevolts ", iRevolts)
			apCityList = PyPlayer(iPlayer).getCityList()
			gc.getPlayer(iPlayer).changeAnarchyTurns(iCrisis)
			while (iSuccessions >= 1):
				if utils.findRemotestProvince(iPlayer) != (None, None):
					regionID, cityList = utils.findRemotestProvince(iPlayer)
					#print ("len(cityList)", len(cityList))
					if len(cityList) <= iSuccessions:
						#print "len(cityList) <= iSuccessions "
						for pCity in cityList:
							utils.secedeCity(pCity)
						iSuccessions -= len(cityList)
						iRevolts -= len(cityList)
						#print ("iSuccessions ", iSuccessions)
						#print ("iRevolts ", iRevolts)
						if utils.findRemotestProvince(iPlayer) != (None, None):
							regionID, cityList = utils.findRemotestProvince(iPlayer)
						else:
							iSuccessions = 0
					else:
						#print "else"
						for i in range(iSuccessions):
							utils.secedeCity((cityList[i]))
						iRevolts -= iSuccessions
						#print ("iSuccessions ", iSuccessions)
						#print ("iRevolts ", iRevolts)
						iSuccessions = 0
				else:
					iSuccessions = 0
			else:
				while (iRevolts >= 1):
					if utils.findRemotestProvince(iPlayer) != (None, None):
						regionID, cityList = utils.findRemotestProvince(iPlayer)
						if len(cityList) <= iRevolts:
							#print "len(cityList) <= iRevolts "
							for pCity in cityList:
								pCity.changeOccupationTimer(iRevolts);
							iSuccessions -= len(cityList)
							iRevolts -= len(cityList)
							#print ("iSuccessions ", iSuccessions)
							#print ("iRevolts ", iRevolts)
							if utils.findRemotestProvince(iPlayer) != (None, None):
								regionID, cityList = utils.findRemotestProvince(iPlayer)
							else:
								iSuccessions = 0
						else:
							#print "else"
							for i in range(iRevolts):
								(cityList[i]).changeOccupationTimer(iRevolts);
							iRevolts = 0
							#print ("iSuccessions ", iSuccessions)
							#print ("iRevolts ", iRevolts)
					else:
						iRevolts = 0

			if gc.getPlayer(utils.getHumanID()).canContact(iPlayer):
				CyInterface().addMessage(utils.getHumanID(), False, con.iDuration, localText.getText("TXT_KEY_STABILITY_CIVILWAR4", ()) + " " + gc.getPlayer(iPlayer).getCivilizationDescription(0) + " " + \
				localText.getText("TXT_KEY_STABILITY_CIVILWAR5", ()), "", 0, "", ColorTypes(con.iRed), -1, -1, True, True)
		return
	
	def severeCrisis(self, iPlayer, iCiv, pPlayer, pTeam): 
		#print ("severeCrisis, iPlayer=", iPlayer)
		self.secedeDistantCities(iPlayer, iCiv)
		#if iPlayer == iRome and utils.getYear() < (tBirth[iByzantines] -10) and utils.getHumanID() != iByzantines and sd.getRomanRebellions() < 2 and utils.getYear() < (tBirth[iByzantines] - 20):
			#sd.setRomanRebellions(sd.getRomanRebellions() + 1)
			#if iPlayer == utils.getHumanID():
				#rfccwaiw.startRomanCivilWarPopup(iRome)
			#else:
				#rfccwaiw.startRomanCivilWar()
		#elif iPlayer == iByzantines and sd.getCivilization(iByzantines) == iRebelRome:
			#rfccwaiw.endRomanCivilWar()
		if iPlayer == con.iMauryans and iCiv == con.iMauryans and utils.checkRegionOwnedCity(con.iMauryans, rMagadha) and con.iMauryans != utils.getHumanID() and utils.getYear() < con.tFall[iSungas]:
			self.sungaRevolution()
			return
		elif iPlayer == iQin and pHan.isAlive() and sd.getCivilization(iQin) == iQin and utils.getHumanID() != iQin and utils.getHumanID() != iHan:
			self.terminalCrisis(iQin, iQin, pQin, pTeam)
			gc.getTeam(pHan.getTeam()).setHasTech(iStabilityStable, True, iPlayer, False, False)
		else:
			#print "crisis"
			iCrisis = gc.getGame().getSorenRandNum(3, 'number') + 6
			if utils.getYear() > con.tFall[iCiv]:
				iCrisis += (utils.getYear() - con.tFall[iCiv]) / 50
			iSuccessions = iCrisis / 3
			iRevolts = iCrisis
			#print ("iSuccessions ", iSuccessions)
			#print ("iRevolts ", iRevolts)
			apCityList = PyPlayer(iPlayer).getCityList()
			gc.getPlayer(iPlayer).changeAnarchyTurns(iCrisis)
			while (iSuccessions >= 1):
				if utils.findRemotestProvince(iPlayer) != (None, None):
					regionID, cityList = utils.findRemotestProvince(iPlayer)
					#print ("len(cityList)", len(cityList))
					if len(cityList) <= iSuccessions:
						#print "len(cityList) <= iSuccessions "
						for pCity in cityList:
							utils.secedeCity(pCity)
						iSuccessions -= len(cityList)
						iRevolts -= len(cityList)
						#print ("iSuccessions ", iSuccessions)
						#print ("iRevolts ", iRevolts)
						if utils.findRemotestProvince(iPlayer) != (None, None):
							regionID, cityList = utils.findRemotestProvince(iPlayer)
						else:
							iSuccessions = 0
					else:
						#print "else"
						for i in range(iSuccessions):
							utils.secedeCity((cityList[i]))
						iRevolts -= iSuccessions
						#print ("iSuccessions ", iSuccessions)
						#print ("iRevolts ", iRevolts)
						iSuccessions = 0
				else: iSuccessions = 0
			else:
				while (iRevolts >= 1):
					if utils.findRemotestProvince(iPlayer) != (None, None):
						regionID, cityList = utils.findRemotestProvince(iPlayer)
						if len(cityList) <= iRevolts:
							#print "len(cityList) <= iRevolts "
							for pCity in cityList:
								pCity.changeOccupationTimer(iRevolts);
							iSuccessions -= len(cityList)
							iRevolts -= len(cityList)
							#print ("iSuccessions ", iSuccessions)
							#print ("iRevolts ", iRevolts)
							if utils.findRemotestProvince(iPlayer) != (None, None):
								regionID, cityList = utils.findRemotestProvince(iPlayer)
							else:
								iSuccessions = 0
						else:
							#print "else"
							for i in range(iRevolts):
								(cityList[i]).changeOccupationTimer(iRevolts);
							iRevolts = 0
							#print ("iSuccessions ", iSuccessions)
							#print ("iRevolts ", iRevolts)
					else:
						iRevolts = 0
			if gc.getPlayer(utils.getHumanID()).canContact(iPlayer):
				CyInterface().addMessage(utils.getHumanID(), False, con.iDuration, localText.getText("TXT_KEY_STABILITY_CIVILWAR4", ()) + " " + gc.getPlayer(iPlayer).getCivilizationDescription(0) + " " + \
				localText.getText("TXT_KEY_STABILITY_CIVILWAR5", ()), "", 0, "", ColorTypes(con.iRed), -1, -1, True, True)
		return
	
	def terminalCrisis(self, iPlayer, iCiv, pPlayer, pTeam): # collapse
	
		if iPlayer == con.iMauryans and iCiv == con.iMauryans and utils.checkRegionOwnedCity(con.iMauryans, con.rMagadha) and con.iMauryans != utils.getHumanID() and utils.getYear() < con.tFall[con.iSungas]:
			self.sungaRevolution()
			
		else:
			utils.killAndFragmentCiv(iPlayer, False)
			if gc.getPlayer(utils.getHumanID()).canContact(iPlayer):
				CyInterface().addMessage(utils.getHumanID(), False, con.iDuration, gc.getPlayer(iPlayer).getCivilizationDescription(0) + " " + \
				localText.getText("TXT_KEY_STABILITY_CIVILWAR3", ()), "", 0, "", ColorTypes(con.iRed), -1, -1, True, True)
		return
		
		
	def secedeDistantCities(self, iPlayer, iCiv):
		apCityList = PyPlayer(iPlayer).getCityList()
		for pLoopCity in apCityList:
			regionID = gc.getMap().plot(pLoopCity.getX(), pLoopCity.getY()).getRegionID()
			if regionID not in utils.getCoreRegions(iCiv) and regionID not in utils.getNormalRegions(iCiv) and regionID not in utils.getBroaderRegions(iCiv):
				utils.secedeCity(pLoopCity.GetCy())
				
	def empireStability(self, iCorePop, iEmpirePop):
	
		iEmpireRating = 0
		maxPosBonus = 2
		maxNegBonus = 5

		if iCorePop > iEmpirePop:
			iEmpireRating += min(iCorePop/iEmpirePop, maxPosBonus)
		elif iCorePop < iEmpirePop:
			iEmpireRating -= min(iEmpirePop/iCorePop, maxNegBonus)

		#print ("iEmpireRating=", iEmpireRating)
		return iEmpireRating
		
	def setCivicsStability(self, iPlayer):
	
		pPlayer = gc.getPlayer(iPlayer)
		
		iCivicGovernment = pPlayer.getCivics(0)
		iCivicLegal = pPlayer.getCivics(1)
		iCivicLabor = pPlayer.getCivics(2)
		iCivicEconomy = pPlayer.getCivics(3)
		iCivicReligion = pPlayer.getCivics(4)
		
		iStateReligion = pPlayer.getStateReligion()
		
		iCivicsRating = 0 
		
		if iCivicGovernment == con.iMonarchyCivic:
			if iCivicLegal == con.iBarbarismCivic: 
				iCivicsRating -= 1
				#print ("bad combo", "monarchy", "barbarism")
			if iCivicLegal in [con.iVassalageCivic, con.iReligiousLawCivic]: 
				iCivicsRating += 1
				#print ("good combo", "monarchy", "vassalage, or religious law")
			if iCivicLabor == con.iSerfdomCivic: 
				iCivicsRating += 1
				#print ("good combo", "monarchy", "serfdom")
			if iCivicLabor == con.iWageLaborCivic: 
				iCivicsRating -= 1
				#print ("bad combo", "monarchy", "wage labor")
			if iCivicEconomy == con.iPatronageCivic: 
				iCivicsRating += 1
				#print ("good combo", "monarchy", "patronage")
			if iCivicReligion in [con.iDynasticCultCivic, con.iStateReligionCivic]: 
				iCivicsRating += 1
				#print ("good combo", "monarchy", "dynastic cult or state religion")
			
		if iCivicGovernment == con.iOligarchyCivic:
			if iCivicLegal in [con.iBarbarismCivic, con.iTyrannyCivic]: 
				iCivicsRating -= 1
				#print ("bad combo", "oligrachy", "barbarism or tyranny")
			if iCivicLegal == con.iBureaucracyCivic: 
				iCivicsRating += 1
				#print ("good combo", "oligrachy", "bureaucracy")
			if iCivicLabor == con.iTribalismCivic: 
				iCivicsRating -= 1
				#print ("bad combo", "oligrachy", "tribalism")
			if iCivicReligion in [con.iDynasticCultCivic, con.iMilitancyCivic]: 
				iCivicsRating -= 1
				#print ("bad combo", "oligrachy", "dynastic cult or militancy")
			if iCivicEconomy in [con.iAgrarianismCivic, con.iPatronageCivic]: 
				iCivicsRating += 1
				#print ("good combo", "oligrachy", "agrarianism or patronage")
			
		if iCivicGovernment == con.iEmpireCivic:
			if iCivicLegal == con.iBureaucracyCivic: 
				iCivicsRating += 1
				#print ("good combo", "empire", "bureaucracy")
			if iCivicLegal in [con.iBarbarismCivic, con.iTyrannyCivic]: 
				iCivicsRating -= 1
				#print ("bad combo", "empire", "tyranny")
			if iCivicLabor == con.iTribalismCivic: 
				iCivicsRating -= 1
				#print ("bad combo", "empire", "tribalism")
			if iCivicEconomy == con.iDecentralizationCivic: 
				iCivicsRating -= 1
				#print ("bad combo", "empire", "decentralization")
			if iCivicEconomy == con.iAgrarianismCivic: 
				iCivicsRating += 1
				#print ("good combo", "empire", "agrarianism")
			
		if iCivicLegal == con.iBarbarismCivic:
			if iCivicLabor == con.iWageLaborCivic: 
				iCivicsRating -= 1
				#print ("bad combo", "barbarism", "wage labor")
			if iCivicEconomy == con.iTradeEconomyCivic: 
				iCivicsRating -= 1
				#print ("bad combo", "barbarism", "trade economy")
			
		if iCivicLegal == con.iTyrannyCivic:
			if iCivicLabor in [con.iCasteSystemCivic, con.iWageLaborCivic]: 
				iCivicsRating -= 1
				#print ("bad combo", "tyranny", "caste system or wage labor")
			if iCivicEconomy == con.iTradeEconomyCivic: 
				iCivicsRating -= 1
				#print ("bad combo", "tyranny", "trade economy")
			if iCivicReligion == con.iDynasticCultCivic: 
				iCivicsRating += 1
				#print ("good combo", "tyranny", "dynastic cult")
			if iCivicReligion in [con.iStateReligionCivic, con.iMilitancyCivic, con.iSyncretismCivic]: 
				iCivicsRating -= 1
				#print ("bad combo", "tyranny", "state religion, militancy or syncretism")
			
		if iCivicLegal == con.iVassalageCivic:
			if iCivicLabor in [con.iCasteSystemCivic, con.iSerfdomCivic]: 
				iCivicsRating += 1
				#print ("good combo", "vassalge", "caste system or serfdom")
			if iCivicLabor == con.iWageLaborCivic: 
				iCivicsRating -= 1
				#print ("bad combo", "vassalge", "wage labor")
			if iCivicEconomy == con.iTradeEconomyCivic: 
				iCivicsRating -= 1
				#print ("bad combo", "vassalge", "trade economy")
			if iCivicEconomy == con.iPatronageCivic: 
				iCivicsRating += 1
				#print ("good combo", "vassalge", "patronage")
			
		if iCivicLegal == con.iReligiousLawCivic:
			if iCivicLabor in [con.iCasteSystemCivic, con.iSerfdomCivic]: 
				iCivicsRating += 1
				#print ("good combo", "religious law", "caste system or serfdom")
			if iCivicLabor == con.iWageLaborCivic: 
				iCivicsRating -= 1
				#print ("bad combo", "religious law", "wage labor")
			if iCivicEconomy in [con.iTradeEconomyCivic, con.iMilitaryEconomyCivic]: 
				iCivicsRating -= 1
				#print ("bad combo", "religious law", "trade economy or military economy")
			if iCivicReligion in [con.iPaganismCivic, con.iDynasticCultCivic, con.iSyncretismCivic]: 
				iCivicsRating -= 1
				#print ("bad combo", "religious law", "paganism, dynastic cult or syncretism")
			
		if iCivicLegal == con.iBureaucracyCivic:
			if iCivicLabor in [con.iTribalismCivic, con.iCasteSystemCivic]: 
				iCivicsRating -= 1
				#print ("bad combo", "bureaucracy", "tribalism or caste system")
			if iCivicLabor == con.iSlaveryCivic: 
				iCivicsRating += 1
				#print ("good combo", "bureaucracy", "slavery")
			if iCivicEconomy == con.iDecentralizationCivic: 
				iCivicsRating -= 1
				#print ("bad combo", "bureaucracy", "decentralization")
			
		if iCivicLabor == con.iTribalismCivic:
			if iCivicEconomy == con.iDecentralizationCivic: 
				iCivicsRating += 1
				#print ("good combo", "tribalism", "decentralization")
			if iCivicEconomy in [con.iTradeEconomyCivic, con.iMilitaryEconomyCivic]: 
				iCivicsRating -= 1
				#print ("bad combo", "tribalism", "trade economy or military economy")
			if iCivicReligion == con.iDynasticCultCivic: 
				iCivicsRating -= 1
				#print ("bad combo", "tribalism", "dynastic cult")
			
		if iCivicLabor == con.iSlaveryCivic:
			if iCivicEconomy == con.iAgrarianismCivic: 
				iCivicsRating += 1
				#print ("good combo", "slavery", "agrarianism")
			
		if iCivicLabor == con.iCasteSystemCivic:
			if iCivicEconomy == con.iAgrarianismCivic: 
				iCivicsRating += 1
				#print ("good combo", "caste system", "agrarianism")
			if iCivicEconomy == con.iTradeEconomyCivic: 
				iCivicsRating -= 1
				#print ("bad combo", "caste system", "trade economy")
			if iCivicReligion in [con.iDynasticCultCivic, con.iSyncretismCivic]: 
				iCivicsRating -= 1
				#print ("bad combo", "caste system", "dynastic cult or syncretism")
			
		if iCivicLabor == con.iSerfdomCivic:
			if iCivicEconomy == con.iAgrarianismCivic: 
				iCivicsRating += 1
				#print ("good combo", "serfdom", "agrarianism")
			if iCivicEconomy == con.iTradeEconomyCivic: 
				iCivicsRating -= 1
				#print ("bad combo", "serfdom", "trade economy")
			if iCivicReligion == con.iStateReligionCivic: 
				iCivicsRating += 1
				#print ("good combo", "serfdom", "state religion")
			
		if iCivicLabor == con.iWageLaborCivic:
			if iCivicEconomy in [con.iDecentralizationCivic, con.iAgrarianismCivic]: 
				iCivicsRating -= 1
				#print ("bad combo", "wage labor", "decentralization or agrarianism")
			if iCivicEconomy == con.iTradeEconomyCivic: 
				iCivicsRating += 1
				#print ("good combo", "wage labor", "trade economy")
			if iCivicReligion == con.iMilitancyCivic: 
				iCivicsRating -= 1
				#print ("bad combo", "wage labor", "militancy")
			
		if iCivicEconomy == con.iTradeEconomyCivic:
			if iCivicReligion in [con.iDynasticCultCivic, con.iMilitancyCivic]: 
				iCivicsRating -= 1
				#print ("bad combo", "trade economy", "dynastic cult or militancy")
			
		# Civics + State Religion
			
		if iCivicLabor == con.iCasteSystemCivic and con.iStateReligion != con.iHinduism: 
			iCivicsRating -= 1
			#print "caste wo hindu"
		
		if iCivicLabor == con.iSlaveryCivic and iStateReligion == con.iChristianity: 
			iCivicsRating -= 1
			#print "christian slaves"
		
		sd.setCivicsStability(iPlayer, iCivicsRating)
		
	def setStartingEconomyRating(self, iPlayer):
	
		pPlayer = gc.getPlayer(iPlayer)
		
		iEconomy = pPlayer.calculateTotalYield(YieldTypes.YIELD_COMMERCE) - pPlayer.calculateInflatedCosts()
		iIndustry = pPlayer.calculateTotalYield(YieldTypes.YIELD_PRODUCTION)
		iAgriculture = pPlayer.calculateTotalYield(YieldTypes.YIELD_FOOD)
		
		iGrowth = iEconomy + iIndustry + iAgriculture
		
		sd.setOldEconomyRating(iPlayer, iGrowth)
		
	def sungaRevolution(self):
	
		pMauryans = gc.getPlayer(con.iMauryans)
		
		sd.setCivilization(con.iMauryans, con.iSungas)
		pMauryans.setCivilizationType(con.iSungas)
		pMauryans.setLeader(con.iPusyamitra)
		self.assignTechs(con.iMauryans, con.iSungas)
		self.setCivDesc(con.iMauryans, "Sunga Kingdom", "Sunga", "Sungas", "Pusyamitra")
		CyInterface().addMessage(self.getHumanID(), True, con.iDuration, CyTranslator().getText("TXT_KEY_INDEPENDENCE_TEXT_SUNGAS", ()), "", 0, "", ColorTypes(con.iRed), -1, -1, True, True)
		self.majorCrisis(con.iMauryans, con.iSungas, pMauryans, gc.getTeam(pMauryans.getTeam()), 1)
		
	def assignTechs(self, iPlayer, iCiv):
		"""Assigns techs to the specific civ based on the starting tech table."""
		pTeam = gc.getTeam(gc.getPlayer(iPlayer).getTeam())
		for iLoopTech in range(con.iNumTechs):
			pTeam.setHasTech(iLoopTech, False, iPlayer, False, False) # srpt clear old techs first
		for iLoopTech in range(len(con.lStartingTechs[iCiv])):
			pTeam.setHasTech(con.lStartingTechs[iCiv][iLoopTech], True, iPlayer, False, False)
			if iPlayer == utils.getHumanID():
				pTeam.setHasTech(con.iImperialismTech, False, iPlayer, False, False)
				
	def setCivDesc(self, iPlayer, sName, sShort="", sAdj="", sLeader=""):
		
		pPlayer = gc.getPlayer(iPlayer)
		pPlayer.setCivName(localText.getText(sName, ()), localText.getText(sShort, ()), localText.getText(sAdj, ()))
		pPlayer.setName(localText.getText(sLeader, ()))

# singleton for use by all modules

utils = RFCUtils()