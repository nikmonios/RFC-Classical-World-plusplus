# Rhye's and Fall of Civilization - Stored Data

# Moved all read/write functions here so that pickling is only done on load & preSave - edead

from CvPythonExtensions import *
import CvUtil
import cPickle as pickle
from Consts import iNumPlayers
from random import shuffle

# globals
gc = CyGlobalContext()


class StoredData:


	def __init__(self):
		self.setup()

	def setup(self):
		
		self.scriptDict = {
				#------------RiseAndFall
				'iSecretDiplomacyTargetCiv': -1,
				'i3KingdomsMarker': -1,
				'iNewCiv': -1,
				'iNewCivFlip': -1,
				'iOldCivFlip': -1,
				'iSpawnWar': 0, #if 1, add units and declare war. If >=2, do nothing
				'bAlreadySwitched': False,
				'lNumCities':			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
				'lRomanWars':			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
				'lLastTurnAlive':		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
				'lSpawnDelay':			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #active players
				'lCoreUnoccupied':		[-321,-321, -321,-321, -321, -321, -321, -321, -321, -321, -321, -321, -321, -321, -321, -321, -321, -321, -321, -321, -321, -321, -321, -321, -321, -321, -321, -321, -321, -321, -321, -321, -321, -321, -321, -321, -321, -321, -321, -321, -321, -321, -321, -321, -321, -321, -321, -321], #active players
				'lFlipsDelay':			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
				'lAlreadyCollapsed':	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
				'lLastRebellion':		[-320,-320, -320,-320, -320, -320, -320, -320, -320, -320, -320, -320, -320, -320, -320, -320, -320, -320, -320, -320, -320, -320, -320, -320, -320, -320, -320, -320, -320, -320, -320, -320, -320, -320, -320, -320, -320, -320, -320, -320, -320, -320, -320, -320, -320, -320, -320, -320, -320, -320], #48
				'iBetrayalTurns': 0,
				'lLatestRebellionTurn': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
				'iRebelCiv': 0,
				'lExileData': [-1, -1, -1, -1, -1],
				'tTempFlippingCity': -1,
				'lCheatersCheck': [0, -1],
				'iHordeOf406Year': -1,
				'iSungaCoup': -1,
				'iRomanRebellions': 0,
				# 'lBirthTurnModifier': 	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
				'lDeleteMode': [-1, -1, -1], #first is a bool, the other values are capital coordinates
				'bCheatMode': False,
				#------------AIWars
				'lWarTargets':[[-1, -1, -1],[-1, -1, -1],[-1, -1, -1],[-1, -1, -1],[-1, -1, -1],[-1, -1, -1],[-1, -1, -1],[-1, -1, -1],[-1, -1, -1],[-1, -1, -1],[-1, -1, -1],[-1, -1, -1],[-1, -1, -1],[-1, -1, -1],[-1, -1, -1],[-1, -1, -1],[-1, -1, -1],[-1, -1, -1],[-1, -1, -1],[-1, -1, -1],[-1, -1, -1],[-1, -1, -1],[-1, -1, -1],[-1, -1, -1],[-1, -1, -1],[-1, -1, -1],[-1, -1, -1],[-1, -1, -1],[-1, -1, -1],[-1, -1, -1],[-1, -1, -1],[-1, -1, -1],[-1, -1, -1],[-1, -1, -1],[-1, -1, -1],[-1, -1, -1],[-1, -1, -1],[-1, -1, -1],[-1, -1, -1],[-1, -1, -1],[-1, -1, -1],[-1, -1, -1],[-1, -1, -1],[-1, -1, -1],[-1, -1, -1],[-1, -1, -1],[-1, -1, -1],[-1, -1, -1],[-1, -1, -1],[-1, -1, -1]],
				'lLastAIWar': 	[-320,-320, -320,-320, -320, -320, -320, -320, -320, -320, -320, -320, -320, -320, -320, -320, -320, -320, -320, -320, -320, -320, -320, -320, -320, -320, -320, -320, -320, -320, -320, -320, -320, -320, -320, -320, -320, -320, -320, -320, -320, -320, -320, -320, -320, -320, -320, -320, -320, -320, -320],
				'iNextTurnAIWar': -1,
				'lRomanAIVictories': 0,
				'lRomanAIWars': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
				'bRomanCivilWar' : True,
				#------------Plague
				'lPlagueCountdown': 	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #total players + barbarians
				'lGenericPlagueDates': [-1, -1, -1, -1],
				#------------Victories
				'lGoals': [[-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1]],
				#------------Distant Conquest
				'lStabilitySetup': [[-1, -1],
					   [-1, -1],
					   [-1, -1],
					   [-1, -1],
					   [-1, -1],
					   [-1, -1],
					   [-1, -1],
					   [-1, -1],
					   [-1, -1],
					   [-1, -1],
					   [-1, -1],
					   [-1, -1],
					   [-1, -1],
					   [-1, -1],
					   [-1, -1],
					   [-1, -1],
					   [-1, -1],
					   [-1, -1],
					   [-1, -1],
					   [-1, -1],
					   [-1, -1],
					   [-1, -1],
					   [-1, -1],
					   [-1, -1],
					   [-1, -1],
					   [-1, -1],
					   [-1, -1],
					   [-1, -1],
					   [-1, -1],
					   [-1, -1],
					   [-1, -1],
					   [-1, -1],
					   [-1, -1],
					   [-1, -1],
					   [-1, -1],
					   [-1, -1],
					   [-1, -1],
					   [-1, -1],
					   [-1, -1],
					   [-1, -1],
					   [-1, -1],
					   [-1, -1],
					   [-1, -1],
					   [-1, -1],
					   [-1, -1],
					   [-1, -1],
					   [-1, -1],
					   [-1, -1],
					   [-1, -1],
					   [-1, -1],
					   [-1, -1],
					   [-1, -1],
					   [-1, -1],
					   [-1, -1]],
				'iNumParthianKills': 0,
				'iNumGojoseonKills': 0,
				'iGuptaGoldenAges': 0,
				'iNumTocharianConversions': 0,
				'iNumSatavahanaBuddhistConversions': 0,
				'iNumSatavahanaHinduConversions': 0,
				'iNumGenerals': 0,
				'iAxumTradeGold' : 0,
				'lRomanTechs': [-1, -1], 
				'lTangTechs': [-1, -1], 
				'lNubianTechs': [-1, -1], 
				'lYamatoTechs': [-1, -1], 
				'lFunanTechs': [-1, -1],  
				'lKalinkaGP': [0, 0], 
				'lWondersBuilt': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
				'l2OutOf3': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
				#------------Stability
				'lCivicsStability':	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
				'lOldEconomyRating':	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
				'lBaseStabilityLastTurn': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
				'lPartialBaseStability': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
				'lStability': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
				'lOwnedPlotsLastTurn': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
				'lOwnedCitiesLastTurn': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
				'lCombatResultTempModifier': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
				'lGNPold': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
				'lGNPnew': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
				'lStabilityParameters': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #2+3+2+3+3
				'lLastRecordedStabilityStuff': [0, 0, 0, 0, 0, 0], # total + 5 parameters
				'iCounter': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
				'plotList': [],
				'lCivilization': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55], # player to civ desc matchup
				'lStopSpawn': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
				#----------Traits/UPs
				'iNumCrusades': 0,
				'lHasLostCity': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
				'lLastCrusadeTurn': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
				'iLatestFlipTurn': 0,
				#----------Religions
				'lBasePiety': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
				'lPiety': [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1], # srpt + all 3 independents and nomads
				'lFirstConversion': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
				'iLastHolyWarTurn': -101,
				'iHolyWarTarget': -1,
				'lPersecutionData': [-1, -1, -1],
				'lPersecutionReligions': [],
				#----------Misc
				'iSeed': 0,
				'lRandomCivList': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55],
				#----------Mercenaries
				'iPirateX' : -1,
				'iPirateY' : -1,
				'iSeaBarbMercCount' : 0,
				'iBarbMercCount' : 0,
				'mercenaryData': {
					"AvailableMercenaries" : {},
					"HiredMercenaries" : {0:{}, 1:{}, 2:{}, 3:{}, 4:{}, 5:{}, 6:{}, 7:{}, 8:{}, 9:{}, 10:{}, 11:{}, 12:{}, 13:{}, 14:{}, 15:{}, 16:{}, 17:{}, 18:{}, 19:{}, 20:{}, 21:{}, 22:{}, 23:{}, 24:{}, 25:{}, 26:{}, 27:{}, 28:{}, 29:{}, 30:{}, 31:{}, 32:{}, 33:{}, 34:{}, 35:{}, 36:{}, 37:{}, 38:{}, 39:{}, 40:{}, 41:{}, 42:{}, 43:{}, 44:{}, 45:{}, 46:{}, 47:{}, 48:{}, 49:{}, 50:{}, 51:{}, 52:{}, 53:{}, 54:{}, 55:{}},
					"MercenaryGroups" : {},
					"MercenaryNames" : {},
					"UnplacedMercenaries" : {},
					},
				#-----------other stuff
				'lSilkWorms' : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			}
		
		self.setSeed()
		self.setRandomCivList()

	def load(self):
		'Loads and unpickles script data'
		self.scriptDict = pickle.loads(gc.getGame().getScriptData())

	def save(self):
		'Pickles and saves script data'
		gc.getGame().setScriptData(pickle.dumps(self.scriptDict))
		
	# AI wars
	
	def getWarTarget( self, i, j ):
		return self.scriptDict['lWarTargets'][i][j]

	def setWarTarget( self, i, j, iNewValue ):
		self.scriptDict['lWarTargets'][i][j] = iNewValue

	# Civic stability
	def getCivicsStability( self, iCiv ):
		return self.scriptDict['lCivicsStability'][iCiv]

	def setCivicsStability( self, iCiv, iNewValue ):
		self.scriptDict['lCivicsStability'][iCiv] = iNewValue

	# Economic stability
	def getOldEconomyRating( self, iCiv ):
		return self.scriptDict['lOldEconomyRating'][iCiv]

	def setOldEconomyRating( self, iCiv, iNewValue ):
		self.scriptDict['lOldEconomyRating'][iCiv] = iNewValue

	# from RiseAndFall.py

	def getSecretDiplomacyTargetCiv( self ):
		return self.scriptDict['iSecretDiplomacyTargetCiv']

	def setSecretDiplomacyTargetCiv( self, iNewValue ):
		self.scriptDict['iSecretDiplomacyTargetCiv'] = iNewValue

	def get3KingdomsMarker( self ):
		return self.scriptDict['i3KingdomsMarker']

	def set3KingdomsMarker( self, iNewValue ):
		self.scriptDict['i3KingdomsMarker'] = iNewValue

	def getNewCiv( self ):
		return self.scriptDict['iNewCiv']

	def setNewCiv( self, iNewValue ):
		self.scriptDict['iNewCiv'] = iNewValue

	def getNewCivFlip( self ):
		return self.scriptDict['iNewCivFlip']

	def setNewCivFlip( self, iNewValue ):
		self.scriptDict['iNewCivFlip'] = iNewValue

	def getOldCivFlip( self ):
		return self.scriptDict['iOldCivFlip']

	def setOldCivFlip( self, iNewValue ):
		self.scriptDict['iOldCivFlip'] = iNewValue

	def getSpawnWar( self ):
		return self.scriptDict['iSpawnWar']

	def setSpawnWar( self, iNewValue ):
		self.scriptDict['iSpawnWar'] = iNewValue

	def getAlreadySwitched( self ):
		return self.scriptDict['bAlreadySwitched']

	def setAlreadySwitched( self, bNewValue ):
		self.scriptDict['bAlreadySwitched'] = bNewValue

	def getNumCities( self, iCiv ):
		return self.scriptDict['lNumCities'][iCiv]

	def setNumCities( self, iCiv, iNewValue ):
		self.scriptDict['lNumCities'][iCiv] = iNewValue

	def getSpawnDelay( self, iCiv ):
		return self.scriptDict['lSpawnDelay'][iCiv]

	def setSpawnDelay( self, iCiv, iNewValue ):
		self.scriptDict['lSpawnDelay'][iCiv] = iNewValue

	def getCoreUnoccupied( self, iCiv ):
		return self.scriptDict['lCoreUnoccupied'][iCiv]

	def setCoreUnoccupied( self, iCiv, iNewValue ):
		self.scriptDict['lCoreUnoccupied'][iCiv] = iNewValue

	def getFlipsDelay( self, iCiv ):
		return self.scriptDict['lFlipsDelay'][iCiv]

	def setFlipsDelay( self, iCiv, iNewValue ):
		self.scriptDict['lFlipsDelay'][iCiv] = iNewValue

	def getAlreadyCollapsed( self, iCiv ):
		return self.scriptDict['lAlreadyCollapsed'][iCiv]

	def setAlreadyCollapsed( self, iCiv, iNewValue ):
		self.scriptDict['lAlreadyCollapsed'][iCiv] = iNewValue

	def getLastRebellion( self, iCiv ):
		return self.scriptDict['lLastRebellion'][iCiv]

	def setLastRebellion( self, iCiv, iNewValue ):
		self.scriptDict['lLastRebellion'][iCiv] = iNewValue

	def getBetrayalTurns( self ):
		return self.scriptDict['iBetrayalTurns']

	def setBetrayalTurns( self, iNewValue ):
		self.scriptDict['iBetrayalTurns'] = iNewValue

	def getLatestFlipTurn( self ):
		return self.scriptDict['iLatestFlipTurn']

	def setLatestFlipTurn( self, iNewValue ):
		self.scriptDict['iLatestFlipTurn'] = iNewValue

	def getLatestRebellionTurn( self, iCiv ):
		return self.scriptDict['lLatestRebellionTurn'][iCiv]

	def setLatestRebellionTurn( self, iCiv, iNewValue ):
		self.scriptDict['lLatestRebellionTurn'][iCiv] = iNewValue

	def getRebelCiv( self ):
		return self.scriptDict['iRebelCiv']

	def setRebelCiv( self, iNewValue ):
		self.scriptDict['iRebelCiv'] = iNewValue

	def getExileData( self, i ):
		return self.scriptDict['lExileData'][i]

	def setExileData( self, i, iNewValue ):
		self.scriptDict['lExileData'][i] = iNewValue

	def getTempFlippingCity( self ):
		return self.scriptDict['tempFlippingCity']

	def setTempFlippingCity( self, tNewValue ):
		self.scriptDict['tempFlippingCity'] = tNewValue

	def getCheatersCheck( self, i ):
		return self.scriptDict['lCheatersCheck'][i]

	def setCheatersCheck( self, i, iNewValue ):
		self.scriptDict['lCheatersCheck'][i] = iNewValue

	def getDeleteMode( self, i ):
		return self.scriptDict['lDeleteMode'][i]

	def setDeleteMode( self, i, iNewValue ):
		self.scriptDict['lDeleteMode'][i] = iNewValue

	def getCheatMode( self ):
		return self.scriptDict['bCheatMode']

	def setCheatMode( self, bNewValue ):
		self.scriptDict['bCheatMode'] = bNewValue

	def setCounter(self, iCounterID, iNewValue):
		self.scriptDict['iCounter'][iCounterID] = iNewValue

	def getCounter( self, iCounterID ):
		return self.scriptDict['iCounter'][iCounterID]

	def setTempPlotList( self, lNewList ):
		self.scriptDict['plotList'] = lNewList

	def getTempPlotList( self ):
		return self.scriptDict['plotList']

	def setStopSpawn(self, iCiv, iNewValue):
		self.scriptDict['lStopSpawn'][iCiv] = iNewValue

	def getStopSpawn( self, iCiv ):
		return self.scriptDict['lStopSpawn'][iCiv]

	def getHordeOf406Year( self ):
		return self.scriptDict['iHordeOf406Year']

	def setHordeOf406Year( self, iNewValue ):
		self.scriptDict['iHordeOf406Year'] = iNewValue

	def getSungaCoup( self ):
		return self.scriptDict['iSungaCoup']

	def setSungaCoup( self, iNewValue ):
		self.scriptDict['iSungaCoup'] = iNewValue

	def getRomanRebellions( self ):
		return self.scriptDict['iRomanRebellions']

	def setRomanRebellions( self, iNewValue ):
		self.scriptDict['iRomanRebellions'] = iNewValue

	# from Victory.py
	
	def getGoal( self, i, j ):
		return self.scriptDict['lGoals'][i][j]

	def setGoal( self, i, j, iNewValue ):
		self.scriptDict['lGoals'][i][j] = iNewValue

	def getAxumTradeGold( self ):
		return self.scriptDict['iAxumTradeGold']

	def setAxumTradeGold( self, iNewValue ):
		self.scriptDict['iAxumTradeGold'] = iNewValue

	def getWondersBuilt( self, iCiv ):
		return self.scriptDict['lWondersBuilt'][iCiv]

	def setWondersBuilt( self, iCiv, iNewValue ):
		self.scriptDict['lWondersBuilt'][iCiv] = iNewValue

	def getRomanTechs( self, i ):
		return self.scriptDict['lRomanTechs'][i]

	def setRomanTechs( self, i, iNewValue ):
		self.scriptDict['lRomanTechs'][i] = iNewValue

	def getTangTechs( self, i ):
		return self.scriptDict['lTangTechs'][i]

	def setTangTechs( self, i, iNewValue ):
		self.scriptDict['lTangTechs'][i] = iNewValue
		
	def getNubianTechs( self, i ):
		return self.scriptDict['lNubianTechs'][i]

	def setNubianTechs( self, i, iNewValue ):
		self.scriptDict['lNubianTechs'][i] = iNewValue
		
	def getYamatoTechs( self, i ):
		return self.scriptDict['lYamatoTechs'][i]

	def setYamatoTechs( self, i, iNewValue ):
		self.scriptDict['lYamatoTechs'][i] = iNewValue
		
	def getFunanTechs( self, i ):
		return self.scriptDict['lFunanTechs'][i]

	def setFunanTechs( self, i, iNewValue ):
		self.scriptDict['lFunanTechs'][i] = iNewValue
		
	def getKalinkaGP( self, i ):
		return self.scriptDict['lKalinkaGP'][i]

	def setKalinkaGP( self, i, iNewValue ):
		self.scriptDict['lKalinkaGP'][i] = iNewValue

	def getNumParthianKills( self ):
		return self.scriptDict['iNumParthianKills']

	def setNumParthianKills( self, iNewValue ):
		self.scriptDict['iNumParthianKills'] = iNewValue

	def getNumGojoseonKills( self ):
		return self.scriptDict['iNumGojoseonKills']

	def setNumGojoseonKills( self, iNewValue ):
		self.scriptDict['iNumGojoseonKills'] = iNewValue

	def getGuptaGoldenAges( self ):
		return self.scriptDict['iGuptaGoldenAges']

	def setGuptaGoldenAges( self, iNewValue ):
		self.scriptDict['iGuptaGoldenAges'] = iNewValue

	def getNumTocharianConversions( self ):
		return self.scriptDict['iNumTocharianConversions']

	def setNumTocharianConversions( self, iNewValue ):
		self.scriptDict['iNumTocharianConversions'] = iNewValue

	def getNumSatavahanaHinduConversions( self ):
		return self.scriptDict['iNumSatavahanaHinduConversions']

	def setNumSatavahanaHinduConversions( self, iNewValue ):
		self.scriptDict['iNumSatavahanaHinduConversions'] = iNewValue

	def getNumSatavahanaBuddhistConversions( self ):
		return self.scriptDict['iNumSatavahanaBuddhistConversions']

	def setNumSatavahanaBuddhistConversions( self, iNewValue ):
		self.scriptDict['iNumSatavahanaBuddhistConversions'] = iNewValue

	def getNumGenerals( self ):
		return self.scriptDict['iNumGenerals']

	def setNumGenerals( self, iNewValue ):
		self.scriptDict['iNumGenerals'] = iNewValue

	def get2OutOf3( self, iCiv ):
		return self.scriptDict['l2OutOf3'][iCiv]

	def set2OutOf3( self, iCiv, bNewValue ):
		self.scriptDict['l2OutOf3'][iCiv] = bNewValue
		
	# from RFCCWAIWars.py
	
	def getStabilitySetup( self, i, j ):
		return self.scriptDict['lStabilitySetup'][i][j]

	def setStabilitySetup( self, i, j, iNewValue ):
		self.scriptDict['lStabilitySetup'][i][j] = iNewValue
		
	def getRomanCivilWar( self ):
		return self.scriptDict['bRomanCivilWar']

	def setRomanCivilWar( self, bNewValue ):
		self.scriptDict['bRomanCivilWar'] = bNewValue

	# from RFCUtils.py

	def getLastTurnAlive( self, iCiv ):
		return self.scriptDict['lLastTurnAlive'][iCiv]

	def setLastTurnAlive( self, iCiv, iNewValue ):
		self.scriptDict['lLastTurnAlive'][iCiv] = iNewValue

	def getCivilization(self, iCiv):
		return self.scriptDict['lCivilization'][iCiv]

	def setCivilization(self, iCiv, iNewValue):
		self.scriptDict['lCivilization'][iCiv] = iNewValue

	def getNumCrusades(self):
		return self.scriptDict['iNumCrusades']

	def setNumCrusades(self, iNewValue):
		self.scriptDict['iNumCrusades'] = iNewValue

	def isHasLostCity(self, iCiv):
		return self.scriptDict['lHasLostCity'][iCiv]

	def setHasLostCity(self, iCiv, iNewValue):
		self.scriptDict['lHasLostCity'][iCiv] = iNewValue

	def getLastCrusadeTurn(self, iCiv):
		return self.scriptDict['lLastCrusadeTurn'][iCiv]

	def setLastCrusadeTurn(self, iCiv, iNewValue):
		self.scriptDict['lLastCrusadeTurn'][iCiv] = iNewValue

	# from Plague.py

	def getGenericPlagueDates( self, i ):
		return self.scriptDict['lGenericPlagueDates'][i]

	def setGenericPlagueDates( self, i, iNewValue ):
		self.scriptDict['lGenericPlagueDates'][i] = iNewValue

	def getPlagueCountdown( self, iCiv ):
		return self.scriptDict['lPlagueCountdown'][iCiv]

	def setPlagueCountdown( self, iCiv, iNewValue ):
		self.scriptDict['lPlagueCountdown'][iCiv] = iNewValue

	# from Religions.py

	def getBasePiety(self, iCiv):
		return self.scriptDict['lBasePiety'][iCiv]

	def setBasePiety(self, iCiv, iNewValue):
		self.scriptDict['lBasePiety'][iCiv] = max(0, min(100, iNewValue))

	def changePiety(self, iCiv, iChange):
		iNewValue = self.getPiety(iCiv) + iChange
		self.scriptDict['lPiety'][iCiv] = max(0, min(100, iNewValue))
		
	def getPiety(self, iCiv):
		if iCiv >= iNumPlayers: return -1
		return self.scriptDict['lPiety'][iCiv]

	def setPiety(self, iCiv, iNewValue):
		self.scriptDict['lPiety'][iCiv] = max(0, min(100, iNewValue))
		
	def getFirstConversion(self, iCiv):
		if iCiv >= iNumPlayers: return -1
		return self.scriptDict['lFirstConversion'][iCiv]

	def setFirstConversion(self, iCiv, iNewValue):
		self.scriptDict['lFirstConversion'][iCiv] = iNewValue

	def getPersecutionData(self):
		return self.scriptDict['lPersecutionData'][0], self.scriptDict['lPersecutionData'][1], self.scriptDict['lPersecutionData'][2]

	def setPersecutionData(self, iX, iY, iID):
		self.scriptDict['lPersecutionData'] = [iX, iY, iID]

	def getPersecutionReligions(self):
		return self.scriptDict['lPersecutionReligions']

	def setPersecutionReligions(self, val):
		self.scriptDict['lPersecutionReligions'] = val

	# from AIWars.py

	def getLastAIWar( self, iCiv ):
		return self.scriptDict['lLastAIWar'][iCiv]

	def setLastAIWar( self, iCiv, iNewValue ):
		self.scriptDict['lLastAIWar'][iCiv] = iNewValue

	def getNextTurnAIWar( self ):
		return self.scriptDict['iNextTurnAIWar']

	def setNextTurnAIWar( self, iNewValue ):
		self.scriptDict['iNextTurnAIWar'] = iNewValue
		
	# from RomanAIWars.py
	
	def increaseRomanAIVictories(self):
		sd.scriptDict['iRomanVictories'] += 1

	def resetRomanAIVictories(self):
		sd.scriptDict['iRomanVictories'] = 0

	def getRomanAIVictories(self):
		return sd.scriptDict['iRomanVictories']

	def getRomanAIWar(self, iPlayer):
		return sd.scriptDict['lRomanWars'][iPlayer]

	def setRomanAIWar(self, iPlayer, iValue):
		sd.scriptDict['lRomanWars'][iPlayer] = iValue

	# Mercenaries

	def getPirateX( self ):
		return self.scriptDict['iPirateX']

	def setPirateX( self, iNewValue ):
		self.scriptDict['iPirateX'] = iNewValue

	def getPirateY( self ):
		return self.scriptDict['iPirateY']

	def setPirateY( self, iNewValue ):
		self.scriptDict['iPirateY'] = iNewValue

	def getSeaBarbMercCount( self ):
		return self.scriptDict['iSeaBarbMercCount']

	def setSeaBarbMercCount( self, iNewValue ):
		self.scriptDict['iSeaBarbMercCount'] = iNewValue

	def getBarbMercCount( self ):
		return self.scriptDict['iBarbMercCount']

	def setBarbMercCount( self, iNewValue ):
		self.scriptDict['iBarbMercCount'] = iNewValue

	def getMercenaryData(self, key):
		return self.scriptDict['mercenaryData'][key]

	def setMercenaryData(self, key, value):
		self.scriptDict['mercenaryData'][key] = value
	
	# Misc
	
	def getSeed( self ):
		return self.scriptDict['iSeed']

	def setSeed( self ):
		self.scriptDict['iSeed'] = gc.getGame().getSorenRandNum(100, 'Seed for random delay')
	
	def getRandomCivList( self ):
		return self.scriptDict['lRandomCivList']

	def setRandomCivList( self ):
		shuffle(self.scriptDict['lRandomCivList'])
	
	# Generic
	
	def getVal( self, sVal ):
		if sVal in self.scriptDict:
			return self.scriptDict[sVal]
		
	def setVal( self, sVal, iNewValue ):
		self.scriptDict[sVal] = iNewValue

	def delVal( self, sVal ):
		del self.scriptDict[sVal]
		
	def getSilkWorms(self, iCiv):
		if iCiv >= iNumPlayers: return -1
		return self.scriptDict['lSilkWorms'][iCiv]

	def setSilkWorms(self, iCiv, iNewValue):
		self.scriptDict['lSilkWorms'][iCiv] = iNewValue

# All modules import the following single instance, not the class

sd = StoredData()