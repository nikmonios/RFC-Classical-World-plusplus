# Rhye's and Fall of Civilization - Barbarian units and cities

from CvPythonExtensions import *
import CvUtil
import UnitArtStyler
import Consts as con
from RFCUtils import utils
from StoredData import sd

# globals
gc = CyGlobalContext()
localText = CyTranslator()

### Constants ###

iIndependent = con.iIndependent
iIndependent2 = con.iIndependent2
iIndependent3 = con.iIndependent3
iBarbarian = con.iBarbarian
iScythians = con.iNomad2
iAvars = con.iNomad2
iHephthalites = con.iNomad2
iRouran = con.iNomad3
iHuns = con.iNomad1
iPandyans = con.iPandyans
iKalabhras = con.iKalabhras

pScythians = gc.getPlayer(con.iNomad2)
pAvars = gc.getPlayer(con.iNomad2)
pHephthalites = gc.getPlayer(con.iNomad2)
pRouran = gc.getPlayer(con.iNomad3)
pHuns = gc.getPlayer(con.iNomad1)

iHuman = utils.getHumanID()

# iCiv, Name, Year, X, Y, iReligion, Skip
tMinorCities = (
	(iIndependent,  "Artashat",			 -310,  71, 51, [], [], 0), 
	(iIndependent,  "Chersonesos",		 -300,  58, 56, [con.iHellenism], [], 0), 
	(iIndependent,  "Tamralipti",		 -300, 116, 34, [con.iHinduism], [], 0), 
	(iIndependent,  "Mediolanum",		 -300,  32, 57, [], [], 0), 
	(iIndependent3,  "Min Yue",		 	 -300, 148, 39, [con.iTaoism], [], 0),
	(iIndependent3,  "Lutetia",		 	 -295,  23, 63, [], [], 0),
	(iIndependent,  "Amaravati",		 -290, 109, 26, [con.iHinduism], [], 0), 
	(iIndependent3,  "Khotan",		 	 -285, 109, 54, [], [], 0), 
	(iIndependent2,  "Ji",		 	 	 -285, 143, 59, [], [], 0), 
	(iIndependent2,  "Trapezus",		 -270,  65, 51, [], [], 0), 
	(iIndependent3,  "Jinyang",		 	 -270, 139, 55, [], [], 0),
	(iIndependent,  "Dunhuang",	 		 -270, 120, 58, [], [], 0),  
	(iIndependent3,  "Kourion",		 	 -250,  58, 41, [], [], 0), 
	(iIndependent,  "Turpan",	 		 -215, 117, 63, [], [], 0), 
	(iIndependent,  "Cirta",	 		 -280,  24, 40, [], [], 0), 
	(iIndependent3,  "Albana",			 -190,  74, 54, [], [], 0), # before Armenian spawn
	(iIndependent3,  "Govapuri",	 	 -180, 100, 24, [con.iHinduism], [], 0), 
	(iIndependent3,  "Halin",			 -150, 124, 33, [], [], 0),
	(iIndependent3,  "Qiaohsi",		 	 -150, 148, 51, [], [], 0), 
	(iIndependent2,  "Charax",		 	 -130,  74, 36, [], [], 0),
	(iIndependent3,  "Qandahar",	 	 -100,  90, 41, [con.iZoroastrianism], [], 0), # before Saka invasion
	(iIndependent3,  "Dunhuang",	 	  -70, 120, 58, [], [], 0), 
	(iIndependent,  "Tamralipti",		  -70, 116, 34, [con.iHinduism], [], 0), 
	(iIndependent2,  "Khotan",			  -75, 109, 54, [], [], 0), 
	(iIndependent,  "Chersonesos",		  -50,  58, 56, [con.iHellenism], [], 0), 
	(iIndependent3,  "Dunhuang",	 	  -20, 120, 58, [con.iBuddhism], [], 0), 
	(iIndependent2,  "Adulis",		 	   10,  64, 22, [], [], 0),
	(iIndependent2,  "Merv",		 	   40,  87, 49, [con.iZoroastrianism, con.iJudaism], [], 0), # if razed before Kushan spawn
	(iIndependent,  "Samarqand",		   45,  93, 54, [con.iBuddhism], [], 0), 
	(iIndependent2,  "Prey Nokor",	 	   50, 135, 19, [], [], 0), # before Funan spawn
	(iIndependent3,  "Sundapura",		   50, 136,  2, [con.iHinduism], [], 0), 
	(iIndependent3,  "Indrapura",		   90, 138, 26, [], [], 0), 
	(iIndependent3,  "Pragjyotishpur",	  120, 120, 38, [con.iHinduism], [], 0), 
	(iIndependent3,  "Bakkah",			  150,  67, 27, [], [], 0), 
	(iIndependent3,  "Yathreb",			  200,  67, 31, [], [], 0), 
	#(iIndependent3,  "Iling",			  200, 138, 45, [con.iTaoism], [], 0), 
	(iIndependent3,  "Jianye",			  210, 148, 47, [con.iTaoism, con.iConfucianism], [], 0), # before 3 kingdoms
	(iIndependent3,  "Sundapura",		  225, 136,  2, [con.iHinduism], [], 0), 
	(iIndependent3,  "Khotan",		 	  225, 109, 54, [con.iBuddhism], [], 0), 
	(iIndependent3,  "Dunhuang",	 	  225, 120, 58, [con.iBuddhism], [], 0), 
	(iIndependent,  "Chersonesos",		  225,  58, 56, [con.iHellenism], [], 0), 
	#(iIndependent,  "Utou",		 		  221, 171, 57, [], [con.iWalls], 0),
	#(iIndependent2,  "Edo",		 		  221, 170, 53, [], [con.iWalls], 0),
	#(iIndependent3,  "Hiroshima",	 	  221, 161, 49, [], [con.iWalls], 0),
	(iIndependent,  "Utou",		 		  245, 171, 57, [], [con.iWalls], 0),
	(iIndependent2,  "Edo",		 		  245, 170, 54, [], [con.iWalls], 0),
	(iIndependent3,  "Dazaifu",	 		  245, 161, 49, [], [con.iWalls], 0),
	(iBarbarian,  "Erphesfurt",			  380,  35, 67, [], [], 0), 
	(iBarbarian,  "Ratisbon",			  385,  37, 63, [], [], 0), 
	(iIndependent3,  "Tanais",			  395,  65, 61, [], [], 0),
	(iBarbarian,  "Sarkel",				  395,  68, 65, [], [], 0),
	(iBarbarian,  "Stratisburgum",		  400,  30, 62, [], [], 0), 
	(iBarbarian,  "Mimigernaford",		  410,  31, 68, [], [], 0),  
	(iIndependent,  "Chersonesos",		  415,  58, 56, [], [], 0), # before Huns
	(iIndependent2,  "Sundapura",		  500, 136,  2, [con.iHinduism], [], 0), 
	(iIndependent2,  "Khotan",		 	  505, 109, 54, [con.iBuddhism], [], 0), 
	(iIndependent,  "Dunhuang",	 		  505, 120, 58, [con.iBuddhism], [], 0), 
	(iIndependent3,  "Sundapura",		  550, 136,  2, [con.iHinduism], [], 0), 
	(iIndependent3,  "Khotan",		 	  550, 109, 54, [con.iBuddhism], [], 0), # for 550AD map
	(iIndependent,  "Utou",		 		  550, 171, 57, [], [con.iWalls], 0),
	(iIndependent2,  "Edo",		 		  550, 170, 54, [], [con.iWalls], 0),
	(iIndependent3,  "Dazaifu",	 		  550, 161, 49, [], [con.iWalls], 0),
	(iBarbarian,  "Erphesfurt",			  550,  35, 67, [], [], 0), 
	(iBarbarian,  "Ratisbon",			  550,  37, 63, [], [], 0), 
	(iBarbarian,  "Stratisburgum",		  550,  30, 62, [], [], 0), 
	(iBarbarian,  "Mimigernaford",		  550,  31, 68, [], [], 0),  
	(iIndependent2,  "Dali",		 	  560, 127, 39, [con.iBuddhism], [], 0), # before Tibetan spawn 
	(iIndependent3,  "Yathreb",			  625,  67, 31, [], [], 0), # before Arab spawn
)

t320BCMinorCities = (
	(iIndependent, "Burdigala", 18, 57, [], [], []),
	(iIndependent2, "Masillia", 27, 54, [con.iHellenism], [], []),
	(iIndependent3, "Roma", 35, 52, [], [], []),
	(iIndependent, "Syracousai", 36, 43, [con.iHellenism], [], []),
	(iIndependent, "Epidamnos", 44, 50, [con.iHellenism], [], []),
	(iIndependent3, "Saguntum", 21, 49, [], [con.iWalls], []),
	(iIndependent2, "Cyrene", 43, 36, [con.iHellenism], [], []),
	(iIndependent3, "Pella", 46, 53, [con.iHellenism], [], []),
	(iIndependent, "Athinai", 47, 46, [con.iHellenism], [con.iParthenon], [con.iHellenism]),
	(iIndependent2, "Rhodos", 52, 44, [con.iHellenism], [con.iColossus], []),
	(iIndependent3, "Tungul", 54, 23, [], [], []),
	(iIndependent, "Byzantion", 54, 53, [con.iHellenism], [], []),
	(iIndependent3, "Chersonesos", 60, 59, [con.iHellenism], [], []),
	(iIndependent, "Albana", 72, 57, [], [], []),
	(iIndependent2, "Dwarka", 93, 30, [con.iHinduism], [], []),
	(iIndependent3, "Patalla", 93, 35, [con.iHinduism, con.iZoroastrianism], [], []),
	(iIndependent, "Samarqand", 93, 54, [con.iBuddhism], [], []),
	(iIndependent2, "Mulasthan", 98, 41, [con.iHinduism], [], []),
	(iIndependent3, "Bharuch", 100, 30, [con.iHinduism], [], []),
	(iIndependent, "Takshashila", 100, 46, [con.iBuddhism, con.iHinduism], [], []),
	(iIndependent2, "Vanchi Murthur", 101, 21, [con.iJainism, con.iHinduism], [], [con.iJainism]),
	(iIndependent3, "Anuradhapura", 107, 13, [con.iBuddhism], [], []),
	(iIndependent, "Jinyang", 137, 54, [], [], []),
	(iIndependent2, "Luoyang", 139, 50, [con.iConfucianism, con.iTaoism], [], []),
	(iIndependent3, "Changsha", 141, 41, [con.iTaoism], [], []),
	(iIndependent, "Panyu", 142, 36, [con.iTaoism], [], []),
	(iIndependent2, "Qufu", 144, 51, [con.iConfucianism, con.iTaoism], [], [con.iConfucianism, con.iTaoism]),
	(iIndependent3, "Jianye", 146, 45, [con.iConfucianism, con.iTaoism], [], []),
	(iIndependent, "Guzu", 151, 46, [con.iConfucianism], [], []),
	(iIndependent2, "Wangeomseong", 156, 58, [], [], []),
)

# These cities will receive extra defense if controlled by indeps/barbs: Start, End, X, Y
tMinorStates = (
	(-100, 100, 36, 43), # Syracuse
	(-290, 100, 100, 46), # Taxila
	(-290, 100, 93, 54), # Samarqand
)

# for random unit generation
earlySupport = [con.iSpearman, con.iArcher]
lateSupport = [con.iHeavySpearman, con.iMarksman]

class Barbs:

	def setup(self):
		
		#if gc.getPlayer(con.iSeleucids).isPlayable():
			#for i in range(len(t320BCMinorCities)):
				#self.foundCity(t320BCMinorCities[i][0], t320BCMinorCities[i][1], t320BCMinorCities[i][2], t320BCMinorCities[i][3], t320BCMinorCities[i][4], t320BCMinorCities[i][5], t320BCMinorCities[i][6])
		return


	def checkTurn(self, iGameTurn):
	
		#print "barbs checkTurn"
		
		iHuman = utils.getHumanID()
		iHandicap = gc.getGame().getHandicapType()
		iBonus = 0
		
		# Randomness
		iRand1 = gc.getGame().getSorenRandNum(2, 'Random spawn size for this turn') + 1
		iRand2 = gc.getGame().getSorenRandNum(2, 'Another one') + 1
		iRand3 = gc.getGame().getSorenRandNum(2, 'One more') + 1
		
		# Independent cities
		for i in range(len(tMinorCities)):
			if tMinorCities[i][7] == 0:
				iTurn = getTurnForYear(tMinorCities[i][2])
				if iGameTurn == iTurn or iGameTurn == iTurn + 5 or iGameTurn == iTurn + 10:
					if self.foundCity(tMinorCities[i][0], tMinorCities[i][1], tMinorCities[i][3], tMinorCities[i][4], tMinorCities[i][5], tMinorCities[i][6]):
						tMinorCities[i][7] == 1
		
		# Independent states - extra defense for minor cities
		if iGameTurn % 20 == 10 and iGameTurn >= getTurnForYear(-290):
			for tMinorCity in tMinorStates:
				if iGameTurn > getTurnForYear(tMinorCity[0]) and iGameTurn < getTurnForYear(tMinorCity[1]):
					plot = gc.getMap().plot(tMinorCity[2], tMinorCity[3])
					iOwner = plot.getOwner()
					if plot.isCity() and plot.getNumUnits() < 5 and iOwner >= con.iNumPlayers:
						if iGameTurn <= getTurnForYear(100):
							utils.makeUnit(self.getRandomUnit(earlySupport), iOwner, (tMinorCity[2], tMinorCity[3]), 1)
							gc.getMap().plot(tMinorCity[2], tMinorCity[3]).getPlotCity().setNumRealBuilding(con.iWalls, 1)
						else:
							utils.makeUnit(self.getRandomUnit(lateSupport), iOwner, (tMinorCity[2], tMinorCity[3]), 1)
							gc.getMap().plot(tMinorCity[2], tMinorCity[3]).getPlotCity().setNumRealBuilding(con.iWalls, 1)
							gc.getMap().plot(tMinorCity[2], tMinorCity[3]).getPlotCity().setNumRealBuilding(con.iCastle, 1)
							
							
							
		
			
		
		# Libyans
		#Cyrenaica
		if iGameTurn >= getTurnForYear(-300) and iGameTurn <= getTurnForYear(-150):
			if utils.checkRegionControl(iHuman, con.rEgypt) or utils.checkRegionControl(iHuman, con.rLibya) : iBonus += iHandicap
			self.spawnUnits(iBarbarian, (39,34),(55,30), self.getRandomUnit([con.iSkirmisher_Arab, con.iSpearman_African]), iBonus, iGameTurn, 11, 3, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Libyan")
			iBonus = 0
		#Libyan Desert
		if iGameTurn >= getTurnForYear(-300) and iGameTurn <= getTurnForYear(-150):
			if utils.checkRegionControl(iHuman, con.rEgypt) or utils.checkRegionControl(iHuman, con.rLibya) : iBonus += iHandicap
			self.spawnUnits(iBarbarian, (52,32),(58,24), self.getRandomUnit([con.iSkirmisher_Arab, con.iSpearman_African]), iBonus, iGameTurn, 11, 3, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Libyan")
			iBonus = 0
			
		#Cyrenaica
		if iGameTurn >= getTurnForYear(-150) and iGameTurn <= getTurnForYear(300):
			if utils.checkRegionControl(iHuman, con.rEgypt) or utils.checkRegionControl(iHuman, con.rLibya) : iBonus += iHandicap
			self.spawnUnits(iBarbarian, (39,34),(55,30), self.getRandomUnit([
			con.iSpearman_African, con.iSkirmisher_Arab, con.iHorseman_Scythian]), iBonus + iRand1, iGameTurn, 7, 4, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Libyan")
			iBonus = 0
		#Libyan Desert
		if iGameTurn >= getTurnForYear(-150) and iGameTurn <= getTurnForYear(300):
			if utils.checkRegionControl(iHuman, con.rEgypt) or utils.checkRegionControl(iHuman, con.rLibya) : iBonus += iHandicap
			self.spawnUnits(iBarbarian, (52,32),(58,24), self.getRandomUnit([
			con.iSpearman_African, con.iSkirmisher_Arab, con.iHorseman_Scythian]), iBonus + iRand1, iGameTurn, 7, 4, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Libyan")
			iBonus = 0
		
		#Cyrenaica
		if iGameTurn >= getTurnForYear(300) and iGameTurn <= getTurnForYear(500):
			if utils.checkRegionControl(iHuman, con.rEgypt) or utils.checkRegionControl(iHuman, con.rLibya) : iBonus += iHandicap
			self.spawnUnits(iBarbarian, (39,34),(55,30), self.getRandomUnit([con.iJavelinman_African, con.iHorseman]), iBonus + iRand1 +1, iGameTurn, 20, 4, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Libyan")
			iBonus = 0
		#Libyan Desert
		if iGameTurn >= getTurnForYear(300) and iGameTurn <= getTurnForYear(500):
			if utils.checkRegionControl(iHuman, con.rEgypt) or utils.checkRegionControl(iHuman, con.rLibya) : iBonus += iHandicap
			self.spawnUnits(iBarbarian, (52,32),(58,24), self.getRandomUnit([con.iJavelinman_African, con.iHorseman]), iBonus + iRand1 +1, iGameTurn, 20, 4, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Libyan")
			iBonus = 0
			
		#Cyrenaica
		if iGameTurn >= getTurnForYear(500) and iGameTurn <= getTurnForYear(800):
			if utils.checkRegionControl(iHuman, con.rEgypt) or utils.checkRegionControl(iHuman, con.rLibya) : iBonus += iHandicap
			self.spawnUnits(iBarbarian, (39,34),(55,30), self.getRandomUnit([con.iSkirmisher_Arab, con.iHorseman_Scythian]), iBonus + iRand1 +1, iGameTurn, 27, 4, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Libyan")
			iBonus = 0
		#Libyan Desert
		if iGameTurn >= getTurnForYear(500) and iGameTurn <= getTurnForYear(800):
			if utils.checkRegionControl(iHuman, con.rEgypt) or utils.checkRegionControl(iHuman, con.rLibya) : iBonus += iHandicap
			self.spawnUnits(iBarbarian, (52,32),(58,24), self.getRandomUnit([con.iSkirmisher_Arab, con.iHorseman_Scythian]), iBonus + iRand1 +1, iGameTurn, 27, 4, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Libyan")
			iBonus = 0
			
		
		# Ethiopians
		if iGameTurn >= getTurnForYear(-290) and iGameTurn <= getTurnForYear(100):
			if utils.checkRegionControl(iHuman, con.rNubia) or utils.checkRegionControl(iHuman, con.rAxum) : iBonus += iHandicap
			self.spawnUnits(iBarbarian, (57,25),(67,14), self.getRandomUnit([con.iSpearman_African]), iBonus + iRand1, iGameTurn, 11, 5, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Axumite")
			iBonus = 0
		
		# Darfur
		if iGameTurn >= getTurnForYear(-50) and iGameTurn <= getTurnForYear(150):
			if utils.checkRegionControl(iHuman, con.rNubia): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (46,23),(53,14), self.getRandomUnit([con.iSpearman_African, con.iSkirmisher_Arab]), iBonus + iRand1 +1, iGameTurn, 21, 5, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Darfur")
			iBonus = 0
		if iGameTurn >= getTurnForYear(150) and iGameTurn <= getTurnForYear(600):
			if utils.checkRegionControl(iHuman, con.rNubia): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (46,23),(53,14), self.getRandomUnit([con.iSpearman_African, con.iHorseman_Scythian]), iBonus + iRand1 +1, iGameTurn, 21, 5, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Darfur")
			iBonus = 0	
		
		# Numidians
		if iGameTurn >= getTurnForYear(-300) and iGameTurn <= getTurnForYear(-200):
			if utils.checkRegionControl(iHuman, con.rAfrica) or utils.checkRegionControl(iHuman, con.rNumidia) or utils.checkRegionControl(iHuman, con.rMauretania): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (11,41),(31,34), self.getRandomUnit([con.iSkirmisher_Arab]), iBonus + iRand1 +1, iGameTurn, 11, 5, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Numidian")
			iBonus = 0
		
		if iGameTurn >= getTurnForYear(-200) and iGameTurn <= getTurnForYear(300):
			if utils.checkRegionControl(iHuman, con.rAfrica) or utils.checkRegionControl(iHuman, con.rNumidia) or utils.checkRegionControl(iHuman, con.rMauretania): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (11,41),(31,34), self.getRandomUnit([con.iHorseman_Scythian]), iBonus + iRand1 +1, iGameTurn, 9, 7, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Numidian")
			iBonus = 0
			
		if iGameTurn >= getTurnForYear(300) and iGameTurn <= getTurnForYear(500):
			if utils.checkRegionControl(iHuman, con.rAfrica) or utils.checkRegionControl(iHuman, con.rNumidia) or utils.checkRegionControl(iHuman, con.rMauretania): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (11,41),(31,34), self.getRandomUnit([con.iHorseman_Scythian]), iBonus + iRand1 +1, iGameTurn, 27, 8, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Numidian")
			iBonus = 0
			
		
		# Berbers
		if iGameTurn >= getTurnForYear(300) and iGameTurn <= getTurnForYear(500):
			if utils.checkRegionControl(iHuman, con.rAfrica) or utils.checkRegionControl(iHuman, con.rNumidia) or utils.checkRegionControl(iHuman, con.rMauretania): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (11,41),(31,34), self.getRandomUnit([con.iCordobanBerber]), iBonus + iRand1, iGameTurn, 27, 8, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Berber")
			iBonus = 0
		
		# Scythians
		# Pontic
		if iGameTurn >= getTurnForYear(-300) and iGameTurn <= getTurnForYear(-200):
			if utils.checkRegionControl(iHuman, con.rThrace) or utils.checkRegionControl(iHuman, con.rGreece) or utils.checkRegionControl(iHuman, con.rCrimea): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (52,66),(62,60), self.getRandomUnit([con.iHorseman_Scythian]), iBonus + iRand1, iGameTurn, 15, 9, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Scythian")
			iBonus = 0
		# Caucasian
		if iGameTurn >= getTurnForYear(-300) and iGameTurn <= getTurnForYear(-200):
			self.spawnUnits(iBarbarian, (64,66),(76,62), self.getRandomUnit([con.iHorseman_Scythian]), iBonus + iRand1, iGameTurn, 15, 9, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Scythian")
			iBonus = 0
			
		# Pontic
		if iGameTurn >= getTurnForYear(-200) and iGameTurn <= getTurnForYear(-100):
			if utils.checkRegionControl(iHuman, con.rThrace) or utils.checkRegionControl(iHuman, con.rGreece) or utils.checkRegionControl(iHuman, con.rCrimea): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (52,66),(62,60), self.getRandomUnit([con.iHorseman_Scythian]), iBonus + iRand1 +1, iGameTurn, 12, 8, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Scythian")
			iBonus = 0
		# Caucasian
		if iGameTurn >= getTurnForYear(-200) and iGameTurn <= getTurnForYear(-100):
			if utils.checkRegionControl(iHuman, con.rCaucasus) or utils.checkRegionControl(iHuman, con.rArmenia): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (64,66),(76,62), self.getRandomUnit([con.iHorseman_Scythian]), iBonus + iRand1 +1, iGameTurn, 15, 8, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Scythian")
			iBonus = 0
		# Pontic
		if iGameTurn >= getTurnForYear(-100) and iGameTurn <= getTurnForYear(300):
			if utils.checkRegionControl(iHuman, con.rThrace) or utils.checkRegionControl(iHuman, con.rGreece) or utils.checkRegionControl(iHuman, con.rCrimea): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (52,66),(62,60), self.getRandomUnit([con.iHorseArcher_Scythian, con.iHorseman_Scythian]), iBonus + iRand2 +1, iGameTurn, 10, 1, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Scythian")
			iBonus = 0
		# Caucasian
		if iGameTurn >= getTurnForYear(-100) and iGameTurn <= getTurnForYear(300):
			if utils.checkRegionControl(iHuman, con.rCaucasus) or utils.checkRegionControl(iHuman, con.rArmenia): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (64,66),(76,62), self.getRandomUnit([con.iHorseArcher_Scythian, con.iHorseman_Scythian]), iBonus + iRand2 +1, iGameTurn, 15, 5, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Scythian")
			iBonus = 0
		# Pontic
		if iGameTurn >= getTurnForYear(-50) and iGameTurn <= getTurnForYear(300):
			if utils.checkRegionControl(iHuman, con.rThrace) or utils.checkRegionControl(iHuman, con.rGreece) or utils.checkRegionControl(iHuman, con.rCrimea): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (52,66),(62,60), self.getRandomUnit([con.iHorseArcher_Scythian, con.iHorseman_Scythian]), iBonus + iRand2 +1, iGameTurn, 30, 5, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Scythian")
			iBonus = 0
		# Caucasian
		if iGameTurn >= getTurnForYear(-50) and iGameTurn <= getTurnForYear(300):
			if utils.checkRegionControl(iHuman, con.rCaucasus) or utils.checkRegionControl(iHuman, con.rArmenia): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (64,66),(76,62), self.getRandomUnit([con.iHorseArcher_Scythian, con.iHorseman_Scythian]), iBonus + iRand2 +1, iGameTurn, 40, 5, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Scythian")
			iBonus = 0
			
		# Sarmatians
		if iGameTurn >= getTurnForYear(-300) and iGameTurn <= getTurnForYear(-200):
			if utils.checkRegionControl(iHuman, con.rSogdiana) or utils.checkRegionControl(iHuman, con.rMargiana) or utils.checkRegionControl(iHuman, con.rFerghana) or utils.checkRegionControl(iHuman, con.rBactria): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (80,63),(100,59), self.getRandomUnit([con.iHorseman_Scythian]), iBonus + iRand2, iGameTurn, 15, 1, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Sarmatian")
			iBonus = 0
			
		if iGameTurn >= getTurnForYear(-200) and iGameTurn <= getTurnForYear(-140):
			if utils.checkRegionControl(iHuman, con.rSogdiana) or utils.checkRegionControl(iHuman, con.rMargiana) or utils.checkRegionControl(iHuman, con.rFerghana) or utils.checkRegionControl(iHuman, con.rBactria): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (80,63),(100,59), self.getRandomUnit([con.iHorseman_Scythian]), iBonus + iRand2 +1, iGameTurn, 13, 5, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Sarmatian")
			iBonus = 0
			
		if iGameTurn >= getTurnForYear(-110) and iGameTurn <= getTurnForYear(300):
			if utils.checkRegionControl(iHuman, con.rSogdiana) or utils.checkRegionControl(iHuman, con.rMargiana) or utils.checkRegionControl(iHuman, con.rFerghana) or utils.checkRegionControl(iHuman, con.rBactria): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (80,63),(100,59), self.getRandomUnit([con.iHorseArcher_Scythian, con.iHorseman_Scythian]), iBonus + iRand2 +1, iGameTurn, 10, 1, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Sarmatian")
			iBonus = 0
			
		if iGameTurn >= getTurnForYear(100) and iGameTurn <= getTurnForYear(200):
			if utils.checkRegionControl(iHuman, con.rSogdiana) or utils.checkRegionControl(iHuman, con.rMargiana) or utils.checkRegionControl(iHuman, con.rFerghana) or utils.checkRegionControl(iHuman, con.rBactria): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (80,63),(100,59), self.getRandomUnit([con.iHorseArcher_Scythian, con.iHorseman_Scythian]), iBonus + iRand2 +1, iGameTurn, 8, 5, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Sarmatian")
			iBonus = 0
			
		if iGameTurn >= getTurnForYear(200) and iGameTurn <= getTurnForYear(275):
			if utils.checkRegionControl(iHuman, con.rSogdiana) or utils.checkRegionControl(iHuman, con.rMargiana) or utils.checkRegionControl(iHuman, con.rFerghana) or utils.checkRegionControl(iHuman, con.rBactria): iBonus += iHandicap
			if gc.getPlayer(con.iKushans).isAlive(): iBonus += 1
			self.spawnUnits(iBarbarian, (80,63),(100,59), self.getRandomUnit([con.iHorseArcher_Scythian]), iBonus + iRand2 +2, iGameTurn, 6, 5, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Sarmatian")
			iBonus = 0
			
		if iGameTurn >= getTurnForYear(275) and iGameTurn <= getTurnForYear(350):
			if utils.checkRegionControl(iHuman, con.rSogdiana) or utils.checkRegionControl(iHuman, con.rMargiana) or utils.checkRegionControl(iHuman, con.rFerghana) or utils.checkRegionControl(iHuman, con.rBactria): iBonus += iHandicap
			if gc.getPlayer(con.iKushans).isAlive(): iBonus += 1
			self.spawnUnits(iBarbarian, (80,63),(100,59), self.getRandomUnit([con.iHorseArcher_Scythian, con.iHorseArcher_Scythian, con.iHeavyHorseArcher]), iBonus + iRand2 +2, iGameTurn, 6, 5, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Sarmatian")
			iBonus = 0
			
		
		# Alans
		if iGameTurn >= getTurnForYear(-200) and iGameTurn <= getTurnForYear(-100):
			if utils.checkRegionControl(iHuman, con.rSogdiana) or utils.checkRegionControl(iHuman, con.rMargiana) or utils.checkRegionControl(iHuman, con.rFerghana) or utils.checkRegionControl(iHuman, con.rBactria): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (65,64),(72,60), self.getRandomUnit([con.iHorseman_Scythian]), iBonus + iRand2 +1, iGameTurn, 15, 1, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Alan")
			iBonus = 0
			
		if iGameTurn >= getTurnForYear(-100) and iGameTurn <= getTurnForYear(200):
			if utils.checkRegionControl(iHuman, con.rSogdiana) or utils.checkRegionControl(iHuman, con.rMargiana) or utils.checkRegionControl(iHuman, con.rFerghana) or utils.checkRegionControl(iHuman, con.rBactria): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (65,64),(72,60), self.getRandomUnit([con.iHorseArcher_Scythian, con.iHorseman_Scythian]), iBonus + iRand2 +1, iGameTurn, 12, 1, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Alan")
			iBonus = 0
		
		if iGameTurn >= getTurnForYear(200) and iGameTurn <= getTurnForYear(350):
			if utils.checkRegionControl(iHuman, con.rSogdiana) or utils.checkRegionControl(iHuman, con.rMargiana) or utils.checkRegionControl(iHuman, con.rFerghana) or utils.checkRegionControl(iHuman, con.rBactria): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (65,64),(72,60), self.getRandomUnit([con.iHorseArcher_Scythian, con.iHorseman_Scythian]), iBonus + iRand2 +1, iGameTurn, 8, 1, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Alan")
			iBonus = 0
		
		# early Yuezhi
		if iGameTurn >= getTurnForYear(-300) and iGameTurn <= getTurnForYear(-150):
			if utils.checkRegionControl(iHuman, con.rTarim) or utils.checkRegionControl(iHuman, con.rGansu) or utils.checkRegionControl(iHuman, con.rQin): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (113,68),(127,60), self.getRandomUnit([con.iHorseman_Xiongnu]), iBonus + iRand2, iGameTurn, 7, 1, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Yuezhi")
			iBonus = 0
		
		# Mongolians
		if iGameTurn >= getTurnForYear(-300) and iGameTurn <= getTurnForYear(-200):
			if utils.checkRegionControl(iHuman, con.rTarim) or utils.checkRegionControl(iHuman, con.rGansu) or utils.checkRegionControl(iHuman, con.rQin) or utils.checkRegionControl(iHuman, con.rZhao) or utils.checkRegionControl(iHuman, con.rYan) or utils.checkRegionControl(iHuman, con.rBuyeo): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (126,71),(149,64), self.getRandomUnit([con.iHorseman_Xiongnu]), iBonus + iRand2, iGameTurn, 7, 1, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Xiongnu")
			iBonus = 0
			
		if iGameTurn >= getTurnForYear(-200) and iGameTurn <= getTurnForYear(-100):
			if utils.checkRegionControl(iHuman, con.rTarim) or utils.checkRegionControl(iHuman, con.rGansu) or utils.checkRegionControl(iHuman, con.rQin) or utils.checkRegionControl(iHuman, con.rZhao) or utils.checkRegionControl(iHuman, con.rYan) or utils.checkRegionControl(iHuman, con.rBuyeo): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (126,71),(149,64), self.getRandomUnit([con.iHorseman_Xiongnu]), iBonus + iRand2 +1, iGameTurn, 15, 5, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Xiongnu")
			iBonus = 0
			
		if iGameTurn >= getTurnForYear(-100) and iGameTurn <= getTurnForYear(150):
			if utils.checkRegionControl(iHuman, con.rTarim) or utils.checkRegionControl(iHuman, con.rGansu) or utils.checkRegionControl(iHuman, con.rQin) or utils.checkRegionControl(iHuman, con.rZhao) or utils.checkRegionControl(iHuman, con.rYan) or utils.checkRegionControl(iHuman, con.rBuyeo): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (126,71),(149,64), self.getRandomUnit([con.iHorseArcher_Xiongnu, con.iHorseman_Xiongnu]), iBonus + iRand2 +1, iGameTurn, 15, 1, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Xiongnu")
			iBonus = 0
		
		# Xiongnu increase
		if iGameTurn >= getTurnForYear(150) and iGameTurn <= getTurnForYear(400):
			if utils.checkRegionControl(iHuman, con.rTarim) or utils.checkRegionControl(iHuman, con.rGansu) or utils.checkRegionControl(iHuman, con.rQin) or utils.checkRegionControl(iHuman, con.rZhao) or utils.checkRegionControl(iHuman, con.rYan) or utils.checkRegionControl(iHuman, con.rBuyeo): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (126,71),(149,64), self.getRandomUnit([con.iHorseArcher_Xiongnu, con.iHorseman_Xiongnu]), iBonus + iRand2 +1, iGameTurn, 9, 1, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Xiongnu")
			iBonus = 0
		
		# Rouran
		if iGameTurn >= getTurnForYear(400) and iGameTurn <= getTurnForYear(525):
			iCiv = iBarbarian
			if pRouran.isAlive(): iCiv = iRouran
			if utils.checkRegionControl(iHuman, con.rTarim) or utils.checkRegionControl(iHuman, con.rGansu) or utils.checkRegionControl(iHuman, con.rQin) or utils.checkRegionControl(iHuman, con.rZhao) or utils.checkRegionControl(iHuman, con.rYan) or utils.checkRegionControl(iHuman, con.rBuyeo): iBonus += iHandicap
			self.spawnUnits(iCiv, (126,71),(149,64), self.getRandomUnit([con.iHeavyHorseArcher]), iBonus + iRand2 +1, iGameTurn, 30, 1, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Rouran")
			iBonus = 0
			
		if iGameTurn >= getTurnForYear(450) and iGameTurn <= getTurnForYear(525):
			iCiv = iBarbarian
			if pRouran.isAlive(): iCiv = iRouran
			if utils.checkRegionControl(iHuman, con.rTarim) or utils.checkRegionControl(iHuman, con.rGansu) or utils.checkRegionControl(iHuman, con.rQin) or utils.checkRegionControl(iHuman, con.rZhao) or utils.checkRegionControl(iHuman, con.rYan) or utils.checkRegionControl(iHuman, con.rBuyeo): iBonus += iHandicap
			self.spawnUnits(iCiv, (126,71),(149,64), self.getRandomUnit([con.iHeavyHorseArcher]), iBonus + iRand2 +1, iGameTurn, 9, 2, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Rouran")
			iBonus = 0
			
		# Turks
		if iGameTurn >= getTurnForYear(450) and iGameTurn <= getTurnForYear(590):
			if utils.checkRegionControl(iHuman, con.rTarim) or utils.checkRegionControl(iHuman, con.rGansu) or utils.checkRegionControl(iHuman, con.rSogdiana) or utils.checkRegionControl(iHuman, con.rFerghana): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (97,70),(113,65), self.getRandomUnit([con.iHeavyHorseArcher]), iBonus + iRand2 +1, iGameTurn, 20, 1, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Turkish")
			iBonus = 0
			
		if iGameTurn >= getTurnForYear(450) and iGameTurn <= getTurnForYear(650):
			if utils.checkRegionControl(iHuman, con.rTarim) or utils.checkRegionControl(iHuman, con.rGansu) or utils.checkRegionControl(iHuman, con.rSogdiana) or utils.checkRegionControl(iHuman, con.rFerghana): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (97,70),(113,65), self.getRandomUnit([con.iHeavyHorseArcher]), iBonus + iRand2 +1, iGameTurn, 9, 2, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Turkish")
			iBonus = 0
			
		if iGameTurn >= getTurnForYear(500) and iGameTurn <= getTurnForYear(800):
			if utils.checkRegionControl(iHuman, con.rTarim) or utils.checkRegionControl(iHuman, con.rGansu) or utils.checkRegionControl(iHuman, con.rSogdiana) or utils.checkRegionControl(iHuman, con.rFerghana): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (97,70),(113,65), self.getRandomUnit([con.iHeavyHorseArcher]), iBonus + iRand2, iGameTurn, 30, 3, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Turkish")
			iBonus = 0
		
		# Manchuria
		if iGameTurn >= getTurnForYear(-280) and iGameTurn <= getTurnForYear(-150):
			if utils.checkRegionControl(iHuman, con.rBuyeo) or utils.checkRegionControl(iHuman, con.rYan): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (149,71),(161,67), self.getRandomUnit([con.iHorseman_Xiongnu]), iBonus + iRand2, iGameTurn, 17, 4, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Donghu")
			iBonus = 0
		
		if iGameTurn >= getTurnForYear(-140) and iGameTurn <= getTurnForYear(150):
			if utils.checkRegionControl(iHuman, con.rBuyeo) or utils.checkRegionControl(iHuman, con.rYan): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (149,71),(161,67), self.getRandomUnit([con.iHorseman_Xiongnu]), iBonus + iRand2 +1, iGameTurn, 9, 5, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Xianbei")
			iBonus = 0
		
		if iGameTurn >= getTurnForYear(150) and iGameTurn <= getTurnForYear(350):
			if utils.checkRegionControl(iHuman, con.rBuyeo) or utils.checkRegionControl(iHuman, con.rYan): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (149,71),(161,67), self.getRandomUnit([con.iHorseArcher_Xiongnu]), iBonus + iRand2 +1, iGameTurn, 7, 5, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Xianbei")
			iBonus = 0
		
		if iGameTurn >= getTurnForYear(350) and iGameTurn <= getTurnForYear(800):
			if utils.checkRegionControl(iHuman, con.rBuyeo) or utils.checkRegionControl(iHuman, con.rYan): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (149,71),(161,67), self.getRandomUnit([con.iHeavyHorseArcher]), iBonus + iRand2 +1, iGameTurn, 7, 5, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Xianbei")
			iBonus = 0
		
		# Kushans
		if iGameTurn >= getTurnForYear(-10) and iGameTurn <= getTurnForYear(45):
			if utils.checkRegionControl(iHuman, con.rSogdiana) or utils.checkRegionControl(iHuman, con.rMargiana) or utils.checkRegionControl(iHuman, con.rFerghana) or utils.checkRegionControl(iHuman, con.rBactria) or utils.checkRegionControl(iHuman, con.rArachosia): iBonus += iHandicap
			if utils.checkRegionControl(iHuman, con.rBuyeo) or utils.checkRegionControl(iHuman, con.rYan): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (84,55),(98,41), self.getRandomUnit([con.iHorseArcher_Kushan]), iBonus + iRand2 +1, iGameTurn, 9, 4, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Kushan")
			iBonus = 0
			
		# Maccabees
		if iGameTurn >= getTurnForYear(-180) and iGameTurn <= getTurnForYear(-160):
			if utils.checkRegionControl(iHuman, con.rJudea): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (60,43),(65,33), self.getRandomUnit([con.iMaccabee]), iBonus + iRand2 +1, iGameTurn, 4, 3, utils.innerInvasion, UnitAITypes.UNITAI_ATTACK, "Maccabean")
			iBonus = 0
		
		
	#### Europe ####
		
		# Helveti
		if iGameTurn >= getTurnForYear(-320) and iGameTurn <= getTurnForYear(-200):
			if utils.checkRegionControl(iHuman, con.rNItaly) or utils.checkRegionControl(iHuman, con.rSeptimania): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (28,62),(31,59), self.getRandomUnit([con.iAxeman_Goth, con.iSpearman]), iBonus + iRand2 +1, iGameTurn, 13, 2, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Helveti")
			iBonus = 0
		if iGameTurn >= getTurnForYear(-200) and iGameTurn <= getTurnForYear(1):
			if utils.checkRegionControl(iHuman, con.rNItaly) or utils.checkRegionControl(iHuman, con.rSeptimania): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (28,62),(31,59), self.getRandomUnit([con.iAxeman_Goth, con.iSpearman]), iBonus + iRand2 +1, iGameTurn, 7, 2, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Helveti")
			iBonus = 0
			
		# Belgae
		if iGameTurn >= getTurnForYear(-320) and iGameTurn <= getTurnForYear(-150):
			if utils.checkRegionControl(iHuman, con.rNItaly) or utils.checkRegionControl(iHuman, con.rSeptimania) or utils.checkRegionControl(iHuman, con.rGaul): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (23,71),(30,65), self.getRandomUnit([con.iAxeman_Goth, con.iSpearman]), iBonus + iRand2 +1, iGameTurn, 19, 4, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Belgae")
			iBonus = 0
		if iGameTurn >= getTurnForYear(-150) and iGameTurn <= getTurnForYear(1):
			if utils.checkRegionControl(iHuman, con.rNItaly) or utils.checkRegionControl(iHuman, con.rSeptimania) or utils.checkRegionControl(iHuman, con.rGaul): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (23,71),(30,65), self.getRandomUnit([con.iAxeman_Goth, con.iSpearman]), iBonus + iRand2 +1, iGameTurn, 11, 4, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Belgae")
			iBonus = 0
			
		# Frisii
		if iGameTurn >= getTurnForYear(-320) and iGameTurn <= getTurnForYear(1):
			if utils.checkRegionControl(iHuman, con.rGaul): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (27,73),(32,69), self.getRandomUnit([con.iAxeman_Teutonic, con.iSpearman]), iBonus + iRand2 +1, iGameTurn, 20, 8, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Frisii")
			iBonus = 0
		
		# Illyrians
		if iGameTurn >= getTurnForYear(-310) and iGameTurn <= getTurnForYear(-150):
			if utils.checkRegionControl(iHuman, con.rNItaly) or utils.checkRegionControl(iHuman, con.rIllyricum) or utils.checkRegionControl(iHuman, con.rGreece) or utils.checkRegionControl(iHuman, con.rThrace): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (38,61),(45,53), self.getRandomUnit([con.iAxeman_Goth, con.iSpearman]), iBonus + iRand2, iGameTurn, 20, 12, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Illyrian")
			iBonus = 0
		if iGameTurn >= getTurnForYear(-150) and iGameTurn <= getTurnForYear(-50):
			if utils.checkRegionControl(iHuman, con.rNItaly) or utils.checkRegionControl(iHuman, con.rIllyricum) or utils.checkRegionControl(iHuman, con.rGreece) or utils.checkRegionControl(iHuman, con.rThrace): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (38,61),(45,53), self.getRandomUnit([con.iAxeman_Goth, con.iSpearman]), iBonus + iRand2 +1, iGameTurn, 12, 12, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Illyrian")
			iBonus = 0
		
		# Getae
		if iGameTurn >= getTurnForYear(-300) and iGameTurn <= getTurnForYear(-200):
			if utils.checkRegionControl(iHuman, con.rNItaly) or utils.checkRegionControl(iHuman, con.rIllyricum) or utils.checkRegionControl(iHuman, con.rGreece) or utils.checkRegionControl(iHuman, con.rThrace): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (31,63),(41,61), self.getRandomUnit([con.iAxeman_Goth, con.iSpearman]), iBonus + iRand2 +1, iGameTurn, 17, 3, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Getae")
			iBonus = 0
		if iGameTurn >= getTurnForYear(-200) and iGameTurn <= getTurnForYear(-100):
			if utils.checkRegionControl(iHuman, con.rNItaly) or utils.checkRegionControl(iHuman, con.rIllyricum) or utils.checkRegionControl(iHuman, con.rGreece) or utils.checkRegionControl(iHuman, con.rThrace): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (31,63),(41,61), self.getRandomUnit([con.iAxeman_Goth, con.iSpearman]), iBonus + iRand2 +1, iGameTurn, 11, 3, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Getae")
			iBonus = 0
		
		# Quadi
		if iGameTurn >= getTurnForYear(-300) and iGameTurn <= getTurnForYear(-200):
			if utils.checkRegionControl(iHuman, con.rNItaly) or utils.checkRegionControl(iHuman, con.rIllyricum) or utils.checkRegionControl(iHuman, con.rGreece) or utils.checkRegionControl(iHuman, con.rThrace): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (31,63),(41,61), self.getRandomUnit([con.iAxeman_Goth, con.iSpearman]), iBonus + iRand2 +1, iGameTurn, 24, 9, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Quadi")
			iBonus = 0
		if iGameTurn >= getTurnForYear(-200) and iGameTurn <= getTurnForYear(-100):
			if utils.checkRegionControl(iHuman, con.rNItaly) or utils.checkRegionControl(iHuman, con.rIllyricum) or utils.checkRegionControl(iHuman, con.rGreece) or utils.checkRegionControl(iHuman, con.rThrace): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (31,63),(41,61), self.getRandomUnit([con.iAxeman_Goth, con.iSpearman]), iBonus + iRand2 +1, iGameTurn, 14, 9, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Quadi")
			iBonus = 0
		
		# Iazyges
		if iGameTurn >= getTurnForYear(-200) and iGameTurn <= getTurnForYear(250):
			if utils.checkRegionControl(iHuman, con.rIllyricum) or utils.checkRegionControl(iHuman, con.rGreece) or utils.checkRegionControl(iHuman, con.rThrace): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (51,64),(56,56), self.getRandomUnit([con.iHorseman]), iBonus + iRand2 +1, iGameTurn, 15, 1, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Iazyges")
			iBonus = 0
		
		# Roxolani
		if iGameTurn >= getTurnForYear(-150) and iGameTurn <= getTurnForYear(250):
			if utils.checkRegionControl(iHuman, con.rIllyricum) or utils.checkRegionControl(iHuman, con.rGreece) or utils.checkRegionControl(iHuman, con.rThrace): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (51,64),(56,56), self.getRandomUnit([con.iHorseman]), iBonus + iRand2 +1, iGameTurn, 12, 5, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Iazyges")
			iBonus = 0
		
		# Marcomanni
		if iGameTurn >= getTurnForYear(1) and iGameTurn <= getTurnForYear(250):
			if utils.checkRegionControl(iHuman, con.rNItaly) or utils.checkRegionControl(iHuman, con.rIllyricum) or utils.checkRegionControl(iHuman, con.rGreece) or utils.checkRegionControl(iHuman, con.rThrace): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (31,63),(41,61), self.getRandomUnit([con.iAxeman_Teutonic, con.iSpearman]), iBonus + iRand2 +1, iGameTurn, 11, 4, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Marcomanni")
			iBonus = 0
		if iGameTurn >= getTurnForYear(250) and iGameTurn <= getTurnForYear(400):
			if utils.checkRegionControl(iHuman, con.rNItaly) or utils.checkRegionControl(iHuman, con.rIllyricum) or utils.checkRegionControl(iHuman, con.rGreece) or utils.checkRegionControl(iHuman, con.rThrace): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (31,63),(41,61), self.getRandomUnit([con.iAxeman_Teutonic, con.iHeavySpearman, con.iHorseman]), iBonus + iRand2 +1, iGameTurn, 13, 3, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Marcomanni")
			iBonus = 0
		if iGameTurn >= getTurnForYear(400) and iGameTurn <= getTurnForYear(500):
			if utils.checkRegionControl(iHuman, con.rNItaly) or utils.checkRegionControl(iHuman, con.rIllyricum) or utils.checkRegionControl(iHuman, con.rGreece) or utils.checkRegionControl(iHuman, con.rThrace): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (31,63),(41,61), self.getRandomUnit([con.iAxeman_Teutonic, con.iHeavySpearman, con.iSwordsman]), iBonus + iRand2 +1, iGameTurn, 13, 3, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Marcomanni")
			iBonus = 0
		
		# Suevi
		if iGameTurn >= getTurnForYear(1) and iGameTurn <= getTurnForYear(200):
			if utils.checkRegionControl(iHuman, con.rNItaly) or utils.checkRegionControl(iHuman, con.rIllyricum) or utils.checkRegionControl(iHuman, con.rGreece) or utils.checkRegionControl(iHuman, con.rThrace) or utils.checkRegionControl(iHuman, con.rNItaly) or utils.checkRegionControl(iHuman, con.rGaul): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (31,63),(41,61), self.getRandomUnit([con.iAxeman_Teutonic, con.iSpearman]), iBonus + iRand2 +1, iGameTurn, 12, 2, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Suevi")
			iBonus = 0
		if iGameTurn >= getTurnForYear(200) and iGameTurn <= getTurnForYear(400):
			if utils.checkRegionControl(iHuman, con.rNItaly) or utils.checkRegionControl(iHuman, con.rIllyricum) or utils.checkRegionControl(iHuman, con.rGreece) or utils.checkRegionControl(iHuman, con.rThrace) or utils.checkRegionControl(iHuman, con.rNItaly) or utils.checkRegionControl(iHuman, con.rGaul): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (31,63),(41,61), self.getRandomUnit([con.iAxeman_Teutonic, con.iHeavySpearman, con.iHorseman]), iBonus + iRand2 +1, iGameTurn, 14, 1, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Suevi")
			iBonus = 0
		if iGameTurn >= getTurnForYear(400) and iGameTurn <= getTurnForYear(500):
			if utils.checkRegionControl(iHuman, con.rNItaly) or utils.checkRegionControl(iHuman, con.rIllyricum) or utils.checkRegionControl(iHuman, con.rGreece) or utils.checkRegionControl(iHuman, con.rThrace) or utils.checkRegionControl(iHuman, con.rNItaly) or utils.checkRegionControl(iHuman, con.rGaul): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (31,63),(41,61), self.getRandomUnit([con.iAxeman_Teutonic, con.iHeavySpearman, con.iSwordsman]), iBonus + iRand2 +1, iGameTurn, 11, 1, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Suevi")
			iBonus = 0
		
		
		# Iberians
		if iGameTurn >= getTurnForYear(-280) and iGameTurn <= getTurnForYear(100):
			if utils.checkRegionControl(iHuman, con.rIberia) or utils.checkRegionControl(iHuman, con.rBaetica) or utils.checkRegionControl(iHuman, con.rLusitania): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (10,54),(22,47), self.getRandomUnit([con.iJavelinman, con.iJavelinman, con.iJavelinman, con.iSpearman, con.iAxeman]), iBonus + iRand2, iGameTurn, 19, 9, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Iberian")
			iBonus = 0
		if iGameTurn >= getTurnForYear(100) and iGameTurn <= getTurnForYear(450):
			if utils.checkRegionControl(iHuman, con.rIberia) or utils.checkRegionControl(iHuman, con.rBaetica) or utils.checkRegionControl(iHuman, con.rLusitania): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (10,54),(22,47), self.getRandomUnit([con.iHorseman, con.iJavelinman, con.iHeavySpearman, con.iSpearman, con.iAxeman]), iBonus + iRand2, iGameTurn, 13, 8, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Iberian")
			iBonus = 0
		if iGameTurn >= getTurnForYear(450) and iGameTurn <= getTurnForYear(600):
			if utils.checkRegionControl(iHuman, con.rIberia) or utils.checkRegionControl(iHuman, con.rBaetica) or utils.checkRegionControl(iHuman, con.rLusitania): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (10,54),(22,47), self.getRandomUnit([con.iSwordsman, con.iJavelinman, con.iHeavySpearman, con.iSpearman, con.iAxeman, con.iHorseman]), iBonus + iRand2, iGameTurn, 13, 8, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Iberian")
			iBonus = 0
		
		# Lusitanians
		if iGameTurn >= getTurnForYear(-280) and iGameTurn <= getTurnForYear(450):
			if utils.checkRegionControl(iHuman, con.rIberia) or utils.checkRegionControl(iHuman, con.rBaetica) or utils.checkRegionControl(iHuman, con.rLusitania): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (10,52),(13,45), self.getRandomUnit([con.iJavelinman, con.iJavelinman, con.iJavelinman, con.iSpearman, con.iAxeman]), iBonus +1, iGameTurn, 23, 7, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Lusitanian")
			iBonus = 0
		if iGameTurn >= getTurnForYear(450) and iGameTurn <= getTurnForYear(600):
			if utils.checkRegionControl(iHuman, con.rIberia) or utils.checkRegionControl(iHuman, con.rBaetica) or utils.checkRegionControl(iHuman, con.rLusitania): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (10,52),(13,45), self.getRandomUnit([con.iSwordsman, con.iJavelinman, con.iHeavySpearman, con.iSpearman, con.iAxeman, con.iHorseman]), iBonus +1, iGameTurn, 13, 6, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Lusitanian")
			iBonus = 0
		
		# Allemanni
		if iGameTurn >= getTurnForYear(350) and iGameTurn <= getTurnForYear(600):
			if utils.checkRegionControl(iHuman, con.rNItaly) or utils.checkRegionControl(iHuman, con.rIllyricum) or utils.checkRegionControl(iHuman, con.rGreece) or utils.checkRegionControl(iHuman, con.rThrace) or utils.checkRegionControl(iHuman, con.rGaul): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (31,63),(41,61), self.getRandomUnit([con.iHeavySpearman, con.iSwordsman, con.iAxeman_Teutonic, con.iHorseman]), iBonus + iRand2 +1, iGameTurn, 15, 5, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Allemani")
			iBonus = 0
		if iGameTurn >= getTurnForYear(600) and iGameTurn <= getTurnForYear(700):
			if utils.checkRegionControl(iHuman, con.rNItaly) or utils.checkRegionControl(iHuman, con.rIllyricum) or utils.checkRegionControl(iHuman, con.rGreece) or utils.checkRegionControl(iHuman, con.rThrace) or utils.checkRegionControl(iHuman, con.rGaul): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (31,63),(41,61), self.getRandomUnit([con.iHeavySpearman, con.iSwordsman, con.iLancer]), iBonus + iRand2 +1, iGameTurn, 7, 5, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Allemani")
			iBonus = 0
		
		# early Goths
		if iGameTurn >= getTurnForYear(1) and iGameTurn <= getTurnForYear(180):
			if utils.checkRegionControl(iHuman, con.rIllyricum) or utils.checkRegionControl(iHuman, con.rGreece) or utils.checkRegionControl(iHuman, con.rThrace): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (50,66),(61,59), self.getRandomUnit([con.iAxeman_Teutonic, con.iSpearman]), iBonus + iRand2, iGameTurn, 10, 4, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Goth")
			iBonus = 0
		if iGameTurn >= getTurnForYear(1) and iGameTurn <= getTurnForYear(180):
			if utils.checkRegionControl(iHuman, con.rIllyricum) or utils.checkRegionControl(iHuman, con.rGreece) or utils.checkRegionControl(iHuman, con.rThrace): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (50,66),(61,59), self.getRandomUnit([con.iAxeman_Teutonic, con.iSpearman]), iBonus + iRand2, iGameTurn, 13, 2, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Goth")
			iBonus = 0
		
		# later Goths
		if iGameTurn >= getTurnForYear(180) and iGameTurn <= getTurnForYear(300):
			if utils.checkRegionControl(iHuman, con.rIllyricum) or utils.checkRegionControl(iHuman, con.rGreece) or utils.checkRegionControl(iHuman, con.rThrace) or utils.checkRegionControl(iHuman, con.rNItaly): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (42,61),(53,56), self.getRandomUnit([con.iHeavySpearman, con.iHorseman]), iBonus +1, iGameTurn, 9, 3, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Goth")
			iBonus = 0
		if iGameTurn >= getTurnForYear(180) and iGameTurn <= getTurnForYear(380):
			if utils.checkRegionControl(iHuman, con.rIllyricum) or utils.checkRegionControl(iHuman, con.rGreece) or utils.checkRegionControl(iHuman, con.rThrace) or utils.checkRegionControl(iHuman, con.rNItaly): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (42,61),(53,56), self.getRandomUnit([con.iHeavySpearman, con.iHorseman]), iBonus + iRand2, iGameTurn, 14, 2, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Goth")
			iBonus = 0
		if iGameTurn >= getTurnForYear(380) and iGameTurn <= getTurnForYear(450):
			if utils.checkRegionControl(iHuman, con.rIllyricum) or utils.checkRegionControl(iHuman, con.rGreece) or utils.checkRegionControl(iHuman, con.rThrace) or utils.checkRegionControl(iHuman, con.rNItaly): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (42,61),(53,56), self.getRandomUnit([con.iHeavySpearman, con.iSwordsman]), iBonus + iRand2 +1, iGameTurn, 7, 3, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Goth")
			iBonus = 0
		
		# Burgundians
		if iGameTurn >= getTurnForYear(350) and iGameTurn <= getTurnForYear(500):
			if utils.checkRegionControl(iHuman, con.rNItaly) or utils.checkRegionControl(iHuman, con.rGaul) or utils.checkRegionControl(iHuman, con.rSeptimania): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (31,63),(41,61), self.getRandomUnit([con.iSwordsman, con.iHeavySpearman]), iBonus + iRand2 +1, iGameTurn, 9, 1, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Burgundian")
			iBonus = 0
		if iGameTurn >= getTurnForYear(500) and iGameTurn <= getTurnForYear(600):
			if utils.checkRegionControl(iHuman, con.rNItaly) or utils.checkRegionControl(iHuman, con.rGaul) or utils.checkRegionControl(iHuman, con.rSeptimania): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (31,63),(41,61), self.getRandomUnit([con.iSwordsman, con.iHeavySpearman]), iBonus + iRand2 +1, iGameTurn, 9, 1, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Burgundian")
			iBonus = 0
		
		# Gepids
		if iGameTurn >= getTurnForYear(260) and iGameTurn <= getTurnForYear(500):
			if utils.checkRegionControl(iHuman, con.rNItaly) or utils.checkRegionControl(iHuman, con.rGaul) or utils.checkRegionControl(iHuman, con.rSeptimania): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (38,61),(45,53), self.getRandomUnit([con.iAxeman, con.iHeavySpearman]), iBonus + iRand2 +1, iGameTurn, 9, 2, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Gepid")
			iBonus = 0
		if iGameTurn >= getTurnForYear(500) and iGameTurn <= getTurnForYear(700):
			if utils.checkRegionControl(iHuman, con.rNItaly) or utils.checkRegionControl(iHuman, con.rGaul) or utils.checkRegionControl(iHuman, con.rSeptimania): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (38,61),(45,53), self.getRandomUnit([con.iSwordsman, con.iHeavySpearman]), iBonus + iRand2 +1, iGameTurn, 8, 2, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Gepid")
			iBonus = 0
		
		# Visigoths
		if iGameTurn >= getTurnForYear(410) and iGameTurn <= getTurnForYear(416):
			if utils.checkRegionControl(iHuman, con.rIberia) or utils.checkRegionControl(iHuman, con.rGaul) or utils.checkRegionControl(iHuman, con.rSeptimania): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (16,58),(28,52), self.getRandomUnit([con.iSwordsman, con.iHeavySpearman, con.iLancer]), iBonus + iRand2 +1, iGameTurn, 1, 0, utils.innerInvasion, UnitAITypes.UNITAI_ATTACK, "Visigoth")
			iBonus = 0
		if iGameTurn == getTurnForYear(418):
			if utils.checkRegionControl(iHuman, con.rIberia) or utils.checkRegionControl(iHuman, con.rGaul) or utils.checkRegionControl(iHuman, con.rSeptimania): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (16,58),(28,52), self.getRandomUnit([con.iSwordsman, con.iHeavySpearman, con.iLancer]), iBonus + iRand2 +1, iGameTurn, 1, 0, utils.innerInvasion, UnitAITypes.UNITAI_ATTACK, "Visigoth")
			iBonus = 0
			
		# Franks
		if iGameTurn >= getTurnForYear(420) and iGameTurn <= getTurnForYear(500):
			if utils.checkRegionControl(iHuman, con.rIberia) or utils.checkRegionControl(iHuman, con.rGaul) or utils.checkRegionControl(iHuman, con.rSeptimania) or utils.checkRegionControl(iHuman, con.rAquitania): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (24,72),(31,66), self.getRandomUnit([con.iSwordsman, con.iHeavySpearman, con.iLancer]), iBonus + iRand2 +1, iGameTurn, 8, 3, utils.innerInvasion, UnitAITypes.UNITAI_ATTACK, "Frankish")
			iBonus = 0
		
		# Ostrogoths
		if iGameTurn >= getTurnForYear(466) and iGameTurn <= getTurnForYear(476):
			if utils.checkRegionControl(iHuman, con.rNItaly) or utils.checkRegionControl(iHuman, con.rIllyricum) or utils.checkRegionControl(iHuman, con.rGreece) or utils.checkRegionControl(iHuman, con.rThrace): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (38,61),(45,53), self.getRandomUnit([con.iSwordsman, con.iHeavySpearman, con.iLancer]), iBonus + iRand2 +1, iGameTurn, 1, 0, utils.innerInvasion, UnitAITypes.UNITAI_ATTACK, "Ostrogoth")
			iBonus = 0
		if iGameTurn == getTurnForYear(478):
			if utils.checkRegionControl(iHuman, con.rNItaly) or utils.checkRegionControl(iHuman, con.rIllyricum) or utils.checkRegionControl(iHuman, con.rGreece) or utils.checkRegionControl(iHuman, con.rThrace): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (38,61),(45,53), self.getRandomUnit([con.iSwordsman, con.iHeavySpearman, con.iLancer]), iBonus + iRand2 +1, iGameTurn, 1, 0, utils.innerInvasion, UnitAITypes.UNITAI_ATTACK, "Ostrogoth")
			iBonus = 0
		# Horde of 406
		if iGameTurn == getTurnForYear(sd.getHordeOf406Year()) -2:
			if gc.getPlayer(con.iRome).isAlive():
				if gc.getPlayer(con.iRome).getNumCities() > 1: 
					self.invasionAlert("TXT_KEY_406_WARNING", [con.iRome, con.iByzantines, con.iDacia, con.iCelts])
		if iGameTurn == getTurnForYear(sd.getHordeOf406Year()):
			if gc.getPlayer(con.iRome).isAlive():
				if gc.getPlayer(con.iRome).getNumCities() > 1: 
					self.spawnUnits(iBarbarian, (27,63),(32,61), con.iHeavyHorseArcher, iBonus + iRand2 +3, iGameTurn, 1, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Alan")
					self.spawnUnits(iBarbarian, (27,63),(32,61), con.iLancer, iBonus + iRand2 +3, iGameTurn, 1, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Alan")
					self.spawnUnits(iBarbarian, (27,63),(32,61), con.iSwordsman, iBonus + iRand2 +3, iGameTurn, 1, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Vandal")
					self.spawnUnits(iBarbarian, (27,63),(32,61), con.iHeavySpearman, iBonus + iRand2 +3, iGameTurn, 1, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Vandal")
					self.spawnUnits(iBarbarian, (27,63),(32,61), con.iSwordsman, iBonus + iRand2 +1, iGameTurn, 1, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Marcomanni")
					self.spawnUnits(iBarbarian, (27,63),(32,61), con.iHeavySpearman, iBonus + iRand2 +3, iGameTurn, 1, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Marcomanni")
					self.spawnUnits(iBarbarian, (27,63),(32,61), con.iSwordsman, iBonus + iRand2 +3, iGameTurn, 1, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Suevi")
					self.spawnUnits(iBarbarian, (27,63),(32,61), con.iHeavySpearman, iBonus + iRand2 +3, iGameTurn, 1, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Suevi")
					iBonus = 0
			
		
	#### China ####
		
		# Chinese Bandits
		if iGameTurn >= getTurnForYear(-260) and iGameTurn <= getTurnForYear(850):
			if utils.checkRegionControl(iHuman, con.rQi) or utils.checkRegionControl(iHuman, con.rHan) or utils.checkRegionControl(iHuman, con.rWu) or utils.checkRegionControl(iHuman, con.rChu): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (128,46),(150,39), self.getRandomUnit([con.iSpearman_East_Asian, con.iSpearman_East_Asian, con.iArcher_East_Asian]), iBonus +1, iGameTurn, 12, 1, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Bandit")
			iBonus = 0
		
		# Qiang
		if iGameTurn >= getTurnForYear(-260) and iGameTurn <= getTurnForYear(300):
			if utils.checkRegionControl(iHuman, con.rQin) or utils.checkRegionControl(iHuman, con.rHan) or utils.checkRegionControl(iHuman, con.rShu) or utils.checkRegionControl(iHuman, con.rGansu): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (121,55),(129,48), self.getRandomUnit([con.iSpearman_East_Asian, con.iArcher_East_Asian, con.iAxeman_East_Asian, con.iHorseman_Xiongnu]), iBonus +1, iGameTurn, 12, 1, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Qiang")
			iBonus = 0
		
		if iGameTurn >= getTurnForYear(300) and iGameTurn <= getTurnForYear(850):
			if utils.checkRegionControl(iHuman, con.rQin) or utils.checkRegionControl(iHuman, con.rHan) or utils.checkRegionControl(iHuman, con.rShu) or utils.checkRegionControl(iHuman, con.rGansu): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (121,55),(129,48), self.getRandomUnit([con.iHeavySpearman_East_Asian, con.iMarksman_East_Asian, con.iSwordsman_East_Asian]), iBonus +1, iGameTurn, 12, 1, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Qiang")
			iBonus = 0
		
		# Bai
		if iGameTurn >= getTurnForYear(-260) and iGameTurn <= getTurnForYear(300):
			if utils.checkRegionControl(iHuman, con.rQin) or utils.checkRegionControl(iHuman, con.rHan) or utils.checkRegionControl(iHuman, con.rShu) or utils.checkRegionControl(iHuman, con.rBa): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (131,44),(136,39), self.getRandomUnit([con.iSpearman_East_Asian, con.iSpearman_East_Asian]), iBonus +1, iGameTurn, 12, 1, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Bai")
			iBonus = 0
		
		if iGameTurn >= getTurnForYear(300) and iGameTurn <= getTurnForYear(850):
			if utils.checkRegionControl(iHuman, con.rQin) or utils.checkRegionControl(iHuman, con.rHan) or utils.checkRegionControl(iHuman, con.rShu) or utils.checkRegionControl(iHuman, con.rBa): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (131,44),(136,39), self.getRandomUnit([con.iHeavySpearman_East_Asian, con.iMarksman_East_Asian, con.iSwordsman_East_Asian]), iBonus +1, iGameTurn, 12, 1, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Bai")
			iBonus = 0
		
		# Nan Yue
		if iGameTurn >= getTurnForYear(-250) and iGameTurn <= getTurnForYear(100):
			if utils.checkRegionControl(iHuman, con.rNanYue) or utils.checkRegionControl(iHuman, con.rWu) or utils.checkRegionControl(iHuman, con.rMinYue) or utils.checkRegionControl(iHuman, con.rChu): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (128,38),(149,35), self.getRandomUnit([con.iSpearman_East_Asian, con.iSpearman_East_Asian, con.iArcher_East_Asian, con.iAxeman_East_Asian]), iBonus +1, iGameTurn, 9, 1, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Yue")
			iBonus = 0
		if iGameTurn >= getTurnForYear(100) and iGameTurn <= getTurnForYear(400):
			if utils.checkRegionControl(iHuman, con.rNanYue) or utils.checkRegionControl(iHuman, con.rWu) or utils.checkRegionControl(iHuman, con.rMinYue) or utils.checkRegionControl(iHuman, con.rChu): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (128,38),(149,35), self.getRandomUnit([con.iSpearman_East_Asian, con.iSpearman_East_Asian, con.iArcher_East_Asian, con.iArcher_East_Asian, con.iAxeman_East_Asian]), iBonus +2, iGameTurn, 9, 1, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Yue")
			iBonus = 0
			
		# Yellow Turban Rebellion
		if iGameTurn >= getTurnForYear(180) and iGameTurn <= getTurnForYear(190):
			if gc.getPlayer(con.iHan).isAlive():
				self.spawnUnits(iBarbarian, (135,52),(147,49), self.getRandomUnit([con.iHeavySpearman_East_Asian, con.iSpearman_East_Asian, con.iArcher_East_Asian, con.iArcher_East_Asian, con.iAxeman_East_Asian]), iBonus +iRand1 +1, iGameTurn, 3, 1, utils.innerInvasion, UnitAITypes.UNITAI_ATTACK, "Yellow Turban Rebel")
				iBonus = 0
				self.spawnUnits(iBarbarian, (135,52),(147,49), self.getRandomUnit([con.iHeavySpearman_East_Asian, con.iSpearman_East_Asian, con.iArcher_East_Asian, con.iArcher_East_Asian, con.iAxeman_East_Asian]), iBonus +iRand1 +1, iGameTurn, 7, 1, utils.innerInvasion, UnitAITypes.UNITAI_ATTACK, "Yellow Turban Rebel")
				iBonus = 0
	
	#### Middle East ####
			
		# Parthians
		if iGameTurn >= getTurnForYear(-200) and iGameTurn <= getTurnForYear(-155):
			if utils.checkRegionControl(iHuman, con.rParthia) or utils.checkRegionControl(iHuman, con.rPersia) or utils.checkRegionControl(iHuman, con.rMargiana) or utils.checkRegionControl(iHuman, con.rMedia): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (79,50),(86,42), self.getRandomUnit([con.iHorseArcher]), iBonus +iRand1 +1, iGameTurn, 7, 8, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Parthian")
			iBonus = 0
		if iGameTurn >= getTurnForYear(-155) and iGameTurn <= getTurnForYear(-140):
			if utils.checkRegionControl(iHuman, con.rParthia) or utils.checkRegionControl(iHuman, con.rPersia) or utils.checkRegionControl(iHuman, con.rMargiana) or utils.checkRegionControl(iHuman, con.rMedia): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (79,50),(86,42), self.getRandomUnit([con.iHorseArcher]), iBonus +iRand1 +2, iGameTurn, 4, 8, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Parthian")
			iBonus = 0
			
		# Anatolians
		if iGameTurn >= getTurnForYear(-280) and iGameTurn <= getTurnForYear(-100):
			if utils.checkRegionControl(iHuman, con.rAsia) or utils.checkRegionControl(iHuman, con.rCappadocia) or utils.checkRegionControl(iHuman, con.rPontus) or utils.checkRegionControl(iHuman, con.rArmenia): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (51,52),(70,49), self.getRandomUnit([con.iAxeman, con.iSpearman, con.iSpearman, con.iArcher]), iBonus +1, iGameTurn, 9, 5, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Anatolian")
			iBonus = 0
		
		# Arabs
		if iGameTurn >= getTurnForYear(-300) and iGameTurn <= getTurnForYear(450):
			if utils.checkRegionControl(iHuman, con.rMesopotamia) or utils.checkRegionControl(iHuman, con.rArabiaFelix) or utils.checkRegionControl(iHuman, con.rSyria) or utils.checkRegionControl(iHuman, con.rArmenia) or utils.checkRegionControl(iHuman, con.rJudea): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (66,34),(76,24), self.getRandomUnit([con.iSkirmisher_Arab, con.iHorseman, con.iCamelRider]), iBonus +iRand1 +1, iGameTurn, 9, 6, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Nabatean")
			iBonus = 0
		
		if iGameTurn >= getTurnForYear(450) and iGameTurn <= getTurnForYear(550):
			if utils.checkRegionControl(iHuman, con.rMesopotamia) or utils.checkRegionControl(iHuman, con.rArabiaFelix) or utils.checkRegionControl(iHuman, con.rSyria) or utils.checkRegionControl(iHuman, con.rArmenia) or utils.checkRegionControl(iHuman, con.rJudea): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (66,34),(76,24), self.getRandomUnit([con.iHorseman, con.iArabiaGhazi, con.iCamelRider, con.iCamelArcher]), iBonus +iRand1 +2, iGameTurn, 7, 7, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Arab")
			iBonus = 0
		
		if iGameTurn >= getTurnForYear(550) and iGameTurn <= getTurnForYear(630):
			if utils.checkRegionControl(iHuman, con.rMesopotamia) or utils.checkRegionControl(iHuman, con.rArabiaFelix) or utils.checkRegionControl(iHuman, con.rSyria) or utils.checkRegionControl(iHuman, con.rArmenia) or utils.checkRegionControl(iHuman, con.rJudea): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (66,34),(76,24), self.getRandomUnit([con.iArabiaGhazi, con.iCamelRider, con.iCamelArcher]), iBonus +iRand1 +3, iGameTurn, 5, 7, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Arab")
			iBonus = 0
		
		
	#### India ####
		
		# Thar Desert raiders
		if iGameTurn >= getTurnForYear(-300) and iGameTurn <= getTurnForYear(800):
			if utils.checkRegionControl(iHuman, con.rSindh) or utils.checkRegionControl(iHuman, con.rPunjab) or utils.checkRegionControl(iHuman, con.rAvanti): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (95,38),(102,36), self.getRandomUnit([con.iArcher_Indian, con.iJavelinman_Indian]), iBonus +1, iGameTurn, 9, 3, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Thar Desert")
			iBonus = 0
			
		# Deccan raiders
		if iGameTurn >= getTurnForYear(-300) and iGameTurn <= getTurnForYear(300):
			if utils.checkRegionControl(iHuman, con.rDeccan) or utils.checkRegionControl(iHuman, con.rAndhra) or utils.checkRegionControl(iHuman, con.rTamilNadu) or utils.checkRegionControl(iHuman, con.rKalinka) or utils.checkRegionControl(iHuman, con.rAvanti) or utils.checkRegionControl(iHuman, con.rKerala): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (102,31),(109,22), self.getRandomUnit([con.iArcher_Indian, con.iSpearman_Indian, con.iAxeman_Indian]), iBonus +1, iGameTurn, 7, 4, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Deccan")
			iBonus = 0
		
		# Himalayan foothills
		if iGameTurn >= getTurnForYear(-300) and iGameTurn <= getTurnForYear(-100):
			if utils.checkRegionControl(iHuman, con.rMagadha) or utils.checkRegionControl(iHuman, con.rPunjab): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (108,42),(115,40), self.getRandomUnit([con.iArcher_Indian, con.iJavelinman_Indian]), iBonus +1, iGameTurn, 15, 5, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Himalayan Hill Tribe")
			iBonus = 0
		
		# Annamese Ambushers
		if iGameTurn >= getTurnForYear(-270) and iGameTurn <= getTurnForYear(100):
			if utils.checkRegionControl(iHuman, con.rMagadha) or utils.checkRegionControl(iHuman, con.rBangala) or utils.checkRegionControl(iHuman, con.rAnnam): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (122,41),(129,35), self.getRandomUnit([con.iAnnameseAmbusher]), iBonus +1, iGameTurn, 9, 1, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Annamese")
			iBonus = 0
			
		# Kalabhras
		if sd.getCivilization(iPandyans) != iKalabhras:
			if iGameTurn >= getTurnForYear(180) and iGameTurn <= getTurnForYear(500):
				if utils.checkRegionControl(iHuman, con.rTamilNadu) or utils.checkRegionControl(iHuman, con.rKerala) or utils.checkRegionControl(iHuman, con.rAndhra): iBonus += iHandicap
				self.spawnUnits(iBarbarian, (101,23),(107,19), self.getRandomUnit([con.iSwordsman_Indian, con.iSwordsman_Indian, con.iSpearman_Indian, con.iArcher_Indian]), iBonus +2, iGameTurn, 9, 1, utils.innerInvasion, UnitAITypes.UNITAI_ATTACK, "Kalabhra")
				iBonus = 0
				
			if iGameTurn >= getTurnForYear(180) and iGameTurn <= getTurnForYear(500):
				if utils.checkRegionControl(iHuman, con.rTamilNadu) or utils.checkRegionControl(iHuman, con.rKerala) or utils.checkRegionControl(iHuman, con.rAndhra): iBonus += iHandicap
				self.spawnUnits(iBarbarian, (101,23),(107,19), self.getRandomUnit([con.iSwordsman_Indian, con.iSpearman_Indian, con.iArcher_Indian]), iBonus +3, iGameTurn, 17, 1, utils.innerInvasion, UnitAITypes.UNITAI_ATTACK, "Kalabhra")
				iBonus = 0
				
	#### Southeast Asia ####
		if iGameTurn >= getTurnForYear(100) and iGameTurn <= getTurnForYear(850):
			if utils.checkRegionControl(iHuman, con.rMagadha) or utils.checkRegionControl(iHuman, con.rBangala) or utils.checkRegionControl(iHuman, con.rAnnam): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (127,32),(136,26), self.getRandomUnit([con.iSpearman_Southeast_Asian, con.iJavelinman_Southeast_Asian]), iBonus +1, iGameTurn, 9, 1, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Mon")
			iBonus = 0
		if iGameTurn >= getTurnForYear(100) and iGameTurn <= getTurnForYear(850):
			if utils.checkRegionControl(iHuman, con.rMagadha) or utils.checkRegionControl(iHuman, con.rBangala) or utils.checkRegionControl(iHuman, con.rAnnam): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (127,27),(138,22), self.getRandomUnit([con.iSpearman_Southeast_Asian, con.iJavelinman_Southeast_Asian]), iBonus +1, iGameTurn, 9, 4, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Khmer")
			iBonus = 0
		
	#### Pirates ####
		
		# Western Mediterranean pirates
		if iGameTurn > getTurnForYear(-250) and iGameTurn < getTurnForYear(100):
			self.spawnUnits(iBarbarian, (15,53),(41,34), con.iPirateGalley, iRand1, iGameTurn, 15, 1, utils.outerSeaSpawn, UnitAITypes.UNITAI_ATTACK_SEA, "Pirate")
			
		if iGameTurn > getTurnForYear(100) and iGameTurn < getTurnForYear(700):
			self.spawnUnits(iBarbarian, (15,53),(41,34), con.iWarGalley, iRand2, iGameTurn, 12, 3, utils.outerSeaSpawn, UnitAITypes.UNITAI_ATTACK_SEA, "Pirate")
		
		# Eastern Mediterranean pirates
		if iGameTurn > getTurnForYear(-300) and iGameTurn < getTurnForYear(100):
			self.spawnUnits(iBarbarian, (42,48),(62,35), con.iPirateGalley, iRand3, iGameTurn, 15, 5, utils.outerSeaSpawn, UnitAITypes.UNITAI_ATTACK_SEA, "Pirate")
			
		if iGameTurn > getTurnForYear(100) and iGameTurn < getTurnForYear(700):
			self.spawnUnits(iBarbarian, (42,48),(62,35), con.iWarGalley, iRand1, iGameTurn, 12, 7, utils.outerSeaSpawn, UnitAITypes.UNITAI_ATTACK_SEA, "Pirate")
			
		# Indian Ocean pirates
		if iGameTurn > getTurnForYear(-300) and iGameTurn < getTurnForYear(100):
			self.spawnUnits(iBarbarian, (78,21),(124,0), con.iPirateGalley, iRand2, iGameTurn, 11, 3, utils.outerSeaSpawn, UnitAITypes.UNITAI_ATTACK_SEA, "Pirate")
			
		if iGameTurn > getTurnForYear(100) and iGameTurn < getTurnForYear(700):
			self.spawnUnits(iBarbarian, (78,21),(124,0), con.iWarGalley, iRand3, iGameTurn, 11, 0, utils.outerSeaSpawn, UnitAITypes.UNITAI_ATTACK_SEA, "Pirate")
			
	
			
	#### Sakas & Kushans ####
	
		# Sakas invade NW India
		if iGameTurn == getTurnForYear(-100)-1:
			self.invasionAlert("TXT_KEY_INVASION_SAKAS", [con.iParthia, con.iBactria, con.iMauryans, con.iSatavahana])
		if iGameTurn == getTurnForYear(-100):
			if utils.checkRegionControl(iHuman, con.rArachosia) or utils.checkRegionControl(iHuman, con.rSindh) or utils.checkRegionControl(iHuman, con.rPunjab) or utils.checkRegionControl(iHuman, con.rGandhara): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (85,44),(102,35), con.iHorseArcher, iBonus +iRand1, iGameTurn, 1, 0, utils.innerInvasion, UnitAITypes.UNITAI_ATTACK, "Saka")
			iBonus = 0
		if iGameTurn > getTurnForYear(-100) and iGameTurn < getTurnForYear(-50):
			iCiv = iBarbarian
			if pScythians.isAlive(): iCiv = iScythians
			if utils.checkRegionControl(iHuman, con.rArachosia) or utils.checkRegionControl(iHuman, con.rSindh) or utils.checkRegionControl(iHuman, con.rPunjab) or utils.checkRegionControl(iHuman, con.rGandhara): iBonus += iHandicap
			self.spawnUnits(iCiv, (85,44),(102,35), con.iHorseArcher, iBonus +iRand1 +1, iGameTurn, 5, 3, utils.innerInvasion, UnitAITypes.UNITAI_ATTACK, "Saka")
			iBonus = 0
			self.spawnUnits(iCiv, (85,44),(102,35), con.iHorseArcher, iBonus +iRand1 +1, iGameTurn, 7, 1, utils.innerInvasion, UnitAITypes.UNITAI_ATTACK, "Saka")
			iBonus = 0
			
		# Kushans invade NW India
		if iGameTurn == getTurnForYear(10)-1:
			self.invasionAlert("TXT_KEY_INVASION_KUSHANS", [con.iParthia, con.iBactria, con.iMauryans, con.iSatavahana])
		if iGameTurn == getTurnForYear(10):
			if utils.checkRegionControl(iHuman, con.rArachosia) or utils.checkRegionControl(iHuman, con.rSindh) or utils.checkRegionControl(iHuman, con.rPunjab) or utils.checkRegionControl(iHuman, con.rGandhara) or utils.checkRegionControl(iHuman, con.rBactria) or utils.checkRegionControl(iHuman, con.rAvanti): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (81,57),(102,43), con.iHorseArcher_Kushan, iBonus +iRand1 +2, iGameTurn, 1, 0, utils.innerInvasion, UnitAITypes.UNITAI_ATTACK, "Kushan")
			iBonus = 0
			self.spawnUnits(iBarbarian, (81,57),(102,43), con.iHorseArcher_Kushan, iBonus +iRand1 +2, iGameTurn, 1, 0, utils.innerInvasion, UnitAITypes.UNITAI_ATTACK, "Kushan")
			iBonus = 0
		if iGameTurn > getTurnForYear(-10) and iGameTurn < getTurnForYear(40):
			if utils.checkRegionControl(iHuman, con.rArachosia) or utils.checkRegionControl(iHuman, con.rSindh) or utils.checkRegionControl(iHuman, con.rPunjab) or utils.checkRegionControl(iHuman, con.rGandhara) or utils.checkRegionControl(iHuman, con.rBactria) or utils.checkRegionControl(iHuman, con.rAvanti): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (81,57),(102,43), con.iHorseArcher_Kushan, iBonus +iRand1 +2, iGameTurn, 5, 3, utils.innerInvasion, UnitAITypes.UNITAI_ATTACK, "Kushan")
			iBonus = 0
			self.spawnUnits(iBarbarian, (81,57),(102,43), con.iHorseArcher_Kushan, iBonus +iRand1 +2, iGameTurn, 7, 1, utils.innerInvasion, UnitAITypes.UNITAI_ATTACK, "Kushan")
			iBonus = 0
		
		
		# other tribes attack the Kushans
		if iGameTurn > getTurnForYear(75) and iGameTurn < getTurnForYear(200):
			if utils.checkRegionControl(iHuman, con.rMargiana) or utils.checkRegionControl(iHuman, con.rParthia) or utils.checkRegionControl(iHuman, con.rSogdiana)or utils.checkRegionControl(iHuman, con.rBactria): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (80,63),(100,59), self.getRandomUnit([con.iHorseArcher_Scythian]), iBonus +iRand1, iGameTurn, 9, 2, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Yuezhi")
			iBonus = 0
		if iGameTurn > getTurnForYear(200) and iGameTurn < getTurnForYear(330):
			if utils.checkRegionControl(iHuman, con.rMargiana) or utils.checkRegionControl(iHuman, con.rParthia) or utils.checkRegionControl(iHuman, con.rSogdiana)or utils.checkRegionControl(iHuman, con.rBactria): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (80,63),(100,59), self.getRandomUnit([con.iHorseArcher_Scythian]), iBonus + iRand1 + 1, iGameTurn, 9, 2, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Yuezhi")
			iBonus = 0
			
		if iGameTurn >= getTurnForYear(-50) and iGameTurn <= getTurnForYear(45):
			if utils.checkRegionControl(iHuman, con.rArachosia) or utils.checkRegionControl(iHuman, con.rSindh) or utils.checkRegionControl(iHuman, con.rPunjab) or utils.checkRegionControl(iHuman, con.rGandhara) or utils.checkRegionControl(iHuman, con.rBactria) or utils.checkRegionControl(iHuman, con.rAvanti): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (81,57),(102,43), self.getRandomUnit([con.iHorseArcher_Scythian]), iBonus +iRand1 +2, iGameTurn, 14, 5, utils.innerInvasion, UnitAITypes.UNITAI_ATTACK, "Kushan")
			
		# Huns appear in Scythia & Sarmatia
		if iGameTurn == getTurnForYear(330)-1:
			self.invasionAlert("TXT_KEY_INVASION_HUNS1", [con.iParthia, con.iBactria, con.iRome, con.iSeleucids, con.iDacia, con.iCelts, con.iSassanids, con.iByzantines])
		# Sarmatia
		if iGameTurn == getTurnForYear(330):
			if utils.checkRegionControl(iHuman, con.rMargiana) or utils.checkRegionControl(iHuman, con.rParthia) or utils.checkRegionControl(iHuman, con.rSogdiana)or utils.checkRegionControl(iHuman, con.rBactria): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (80,63),(100,59), con.iHeavyHorseArcher, iBonus +iRand1 +1, iGameTurn, 1, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Hun")
			iBonus = 0
			self.spawnUnits(iBarbarian, (80,63),(100,59), con.iHeavyHorseArcher, iBonus +iRand1 +1, iGameTurn, 1, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Hun")
			iBonus = 0
		if iGameTurn > getTurnForYear(330) and iGameTurn < getTurnForYear(400):
			if utils.checkRegionControl(iHuman, con.rMargiana) or utils.checkRegionControl(iHuman, con.rParthia) or utils.checkRegionControl(iHuman, con.rSogdiana)or utils.checkRegionControl(iHuman, con.rBactria): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (80,63),(100,59), self.getRandomUnit([con.iHorseArcher_Scythian, con.iHeavyHorseArcher]), iBonus +iRand1, iGameTurn, 7, 2, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Hun")
			iBonus = 0
			self.spawnUnits(iBarbarian, (80,63),(100,59), self.getRandomUnit([con.iHorseArcher_Scythian, con.iHeavyHorseArcher]), iBonus +iRand1, iGameTurn, 5, 1, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Hun")
			iBonus = 0
		# Scythia
		if iGameTurn == getTurnForYear(330):
			if utils.checkRegionControl(iHuman, con.rCrimea) or utils.checkRegionControl(iHuman, con.rDacia) or utils.checkRegionControl(iHuman, con.rThrace) or utils.checkRegionControl(iHuman, con.rGreece) or utils.checkRegionControl(iHuman, con.rAsia) or utils.checkRegionControl(iHuman, con.rCaucasus) or utils.checkRegionControl(iHuman, con.rArmenia): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (52,66),(62,60), self.getRandomUnit([con.iHorseArcher_Scythian, con.iHeavyHorseArcher]), iBonus +iRand1, iGameTurn, 1, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Hun")
			iBonus = 0
			self.spawnUnits(iBarbarian, (52,66),(62,60), self.getRandomUnit([con.iHorseArcher_Scythian, con.iHeavyHorseArcher]), iBonus +iRand1, iGameTurn, 1, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Hun")
			iBonus = 0
		if iGameTurn > getTurnForYear(330) and iGameTurn < getTurnForYear(424):
			if utils.checkRegionControl(iHuman, con.rCrimea) or utils.checkRegionControl(iHuman, con.rDacia) or utils.checkRegionControl(iHuman, con.rThrace) or utils.checkRegionControl(iHuman, con.rGreece) or utils.checkRegionControl(iHuman, con.rAsia) or utils.checkRegionControl(iHuman, con.rCaucasus) or utils.checkRegionControl(iHuman, con.rArmenia): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (52,66),(62,60), self.getRandomUnit([con.iHorseArcher_Scythian, con.iHeavyHorseArcher]), iBonus +iRand1, iGameTurn, 7, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Hun")
			iBonus = 0
			self.spawnUnits(iBarbarian, (52,66),(62,60), self.getRandomUnit([con.iHorseArcher_Scythian, con.iHeavyHorseArcher]), iBonus +iRand1, iGameTurn, 5, 1, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Hun")
			iBonus = 0
		
			
		# Huns invade NW India
		if iGameTurn == getTurnForYear(350)-1:
			self.invasionAlert("TXT_KEY_INVASION_HUNS_IN_INDIA", [con.iParthia, con.iBactria, con.iMauryans, con.iSatavahana])
		if iGameTurn == getTurnForYear(350):
			if utils.checkRegionControl(iHuman, con.rArachosia) or utils.checkRegionControl(iHuman, con.rSindh) or utils.checkRegionControl(iHuman, con.rPunjab) or utils.checkRegionControl(iHuman, con.rGandhara) or utils.checkRegionControl(iHuman, con.rBactria) or utils.checkRegionControl(iHuman, con.rAvanti): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (85,44),(102,35), self.getRandomUnit([con.iHorseArcher_Scythian, con.iHeavyHorseArcher]), iBonus +iRand1 +2, iGameTurn, 1, 0, utils.innerInvasion, UnitAITypes.UNITAI_ATTACK, "Hun")
			iBonus = 0
			self.spawnUnits(iBarbarian, (85,44),(102,35), self.getRandomUnit([con.iHorseArcher_Scythian, con.iHeavyHorseArcher]), iBonus +iRand1 +2, iGameTurn, 1, 0, utils.innerInvasion, UnitAITypes.UNITAI_ATTACK, "Hun")
			iBonus = 0
		if iGameTurn > getTurnForYear(350) and iGameTurn < getTurnForYear(400):
			if utils.checkRegionControl(iHuman, con.rArachosia) or utils.checkRegionControl(iHuman, con.rSindh) or utils.checkRegionControl(iHuman, con.rPunjab) or utils.checkRegionControl(iHuman, con.rGandhara) or utils.checkRegionControl(iHuman, con.rBactria) or utils.checkRegionControl(iHuman, con.rAvanti): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (85,44),(102,35), self.getRandomUnit([con.iHorseArcher_Scythian, con.iHeavyHorseArcher]), iBonus +iRand1 +1, iGameTurn, 5, 3, utils.innerInvasion, UnitAITypes.UNITAI_ATTACK, "Hun")
			iBonus = 0
			self.spawnUnits(iBarbarian, (85,44),(102,35), self.getRandomUnit([con.iHorseArcher_Scythian, con.iHeavyHorseArcher]), iBonus +iRand1 +1, iGameTurn, 7, 1, utils.innerInvasion, UnitAITypes.UNITAI_ATTACK, "Hun")
			iBonus = 0
			
		
		# Huns invade the Balkans
		if iGameTurn == getTurnForYear(370):
			if utils.checkRegionControl(iHuman, con.rNItaly) or utils.checkRegionControl(iHuman, con.rIllyricum) or utils.checkRegionControl(iHuman, con.rGreece) or utils.checkRegionControl(iHuman, con.rDacia) or utils.checkRegionControl(iHuman, con.rThrace) or utils.checkRegionControl(iHuman, con.rAsia): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (38,61),(53,53), self.getRandomUnit([con.iHorseArcher_Scythian, con.iHeavyHorseArcher]), iBonus +iRand1 +2, iGameTurn, 1, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Hun")
			iBonus = 0
			if utils.checkRegionControl(iHuman, con.rNItaly) or utils.checkRegionControl(iHuman, con.rIllyricum) or utils.checkRegionControl(iHuman, con.rGreece) or utils.checkRegionControl(iHuman, con.rDacia) or utils.checkRegionControl(iHuman, con.rThrace) or utils.checkRegionControl(iHuman, con.rAsia): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (38,61),(53,53), self.getRandomUnit([con.iHorseArcher_Scythian, con.iHeavyHorseArcher]), iBonus +iRand1 +2, iGameTurn, 1, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Hun")
			iBonus = 0
			if utils.checkRegionControl(iHuman, con.rNItaly) or utils.checkRegionControl(iHuman, con.rIllyricum) or utils.checkRegionControl(iHuman, con.rGreece) or utils.checkRegionControl(iHuman, con.rDacia) or utils.checkRegionControl(iHuman, con.rThrace) or utils.checkRegionControl(iHuman, con.rAsia): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (38,61),(53,53), self.getRandomUnit([con.iHorseArcher_Scythian, con.iHeavyHorseArcher]), iBonus +iRand1 +2, iGameTurn, 1, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Hun")
			iBonus = 0
		if iGameTurn > getTurnForYear(370) and iGameTurn < getTurnForYear(450):
			iCiv = iBarbarian
			if pHuns.isAlive(): iCiv = iHuns
			if utils.checkRegionControl(iHuman, con.rNItaly) or utils.checkRegionControl(iHuman, con.rIllyricum) or utils.checkRegionControl(iHuman, con.rGreece) or utils.checkRegionControl(iHuman, con.rDacia) or utils.checkRegionControl(iHuman, con.rThrace) or utils.checkRegionControl(iHuman, con.rAsia): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (38,61),(53,53), self.getRandomUnit([con.iHorseArcher_Scythian, con.iHeavyHorseArcher]), iBonus +iRand1, iGameTurn, 7, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Hun")
			iBonus = 0
			if utils.checkRegionControl(iHuman, con.rNItaly) or utils.checkRegionControl(iHuman, con.rIllyricum) or utils.checkRegionControl(iHuman, con.rGreece) or utils.checkRegionControl(iHuman, con.rDacia) or utils.checkRegionControl(iHuman, con.rThrace) or utils.checkRegionControl(iHuman, con.rAsia): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (38,61),(53,53), self.getRandomUnit([con.iHorseArcher_Scythian, con.iHeavyHorseArcher]), iBonus +iRand1, iGameTurn, 6, 1, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Hun")
			iBonus = 0
			if utils.checkRegionControl(iHuman, con.rNItaly) or utils.checkRegionControl(iHuman, con.rIllyricum) or utils.checkRegionControl(iHuman, con.rGreece) or utils.checkRegionControl(iHuman, con.rDacia) or utils.checkRegionControl(iHuman, con.rThrace) or utils.checkRegionControl(iHuman, con.rAsia): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (38,61),(53,53), self.getRandomUnit([con.iHorseArcher_Scythian, con.iHeavyHorseArcher]), iBonus +iRand1, iGameTurn, 6, 1, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Hun")
			iBonus = 0
			
		# Huns invade Caucasia
		if iGameTurn == getTurnForYear(435):
			iCiv = iBarbarian
			if pHuns.isAlive(): iCiv = iHuns
			if utils.checkRegionControl(iHuman, con.rCrimea) or utils.checkRegionControl(iHuman, con.rDacia) or utils.checkRegionControl(iHuman, con.rThrace) or utils.checkRegionControl(iHuman, con.rGreece) or utils.checkRegionControl(iHuman, con.rAsia) or utils.checkRegionControl(iHuman, con.rCaucasus) or utils.checkRegionControl(iHuman, con.rArmenia): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (45,38),(51,35), con.iHeavyHorseArcher, iBonus +iRand1 +2, iGameTurn, 1, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Hun")
			iBonus = 0
			self.spawnUnits(iBarbarian, (45,38),(51,35), con.iHeavyHorseArcher, iBonus +iRand1 +3, iGameTurn, 1, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Hun")
			iBonus = 0
		if iGameTurn > getTurnForYear(435) and iGameTurn < getTurnForYear(440):
			iCiv = iBarbarian
			if pHuns.isAlive(): iCiv = iHuns
			self.spawnUnits(iBarbarian, (45,38),(51,35), con.iHeavyHorseArcher, iBonus +iRand1 +2, iGameTurn, 2, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Hun")
			iBonus = 0
			self.spawnUnits(iBarbarian, (45,38),(51,35), con.iHeavyHorseArcher, iBonus +iRand1 +3, iGameTurn, 2, 1, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Hun")
			iBonus = 0
		
		# Atilla
		if iGameTurn == getTurnForYear(447)-1:
			self.invasionAlert("TXT_KEY_INVASION_ATILLA", [con.iCelts, con.iRome, con.iDacia, con.iByzantines, con.iVisigoths])
		if iGameTurn == getTurnForYear(447):
			pUnit = self.spawnUnits(con.iNomad1, (38,61),(45,53), con.iHeavyHorseArcher, 1, iGameTurn, 1, 0, utils.outerInvasion)
			if pUnit:
				self.makeLeader(pUnit, "Atilla", con.iGreatGeneral5)
				pUnit.setHasPromotion(con.iCombat1, True)
				pUnit.setHasPromotion(con.iCombat2, True)
				pUnit.setHasPromotion(con.iFlanking1, True)
				pUnit.setHasPromotion(con.iFlanking2, True)
				pUnit.setHasPromotion(con.iFlanking3, True)
				pUnit.setHasPromotion(con.iFeintAttack, True)
				pUnit.setHasPromotion(con.iEncirclement, True)
			self.spawnUnits(con.iNomad1, (38,61),(45,53), con.iHeavyHorseArcher, self.getInvasionForce(3, con.iRome), iGameTurn, 1, 0, utils.outerInvasion) 
			self.spawnUnits(con.iNomad1, (38,61),(45,53), con.iHeavyHorseArcher, self.getInvasionForce(3, con.iRome), iGameTurn, 1, 0, utils.outerInvasion)
			self.spawnUnits(con.iNomad1, (38,61),(45,53), con.iHeavyHorseArcher, self.getInvasionForce(3, con.iRome), iGameTurn, 1, 0, utils.outerInvasion)
			iBonus = 0
		
		# Chionites in Sogdiana
		if iGameTurn == getTurnForYear(400):
			if utils.checkRegionControl(iHuman, con.rMargiana) or utils.checkRegionControl(iHuman, con.rParthia) or utils.checkRegionControl(iHuman, con.rSogdiana) or utils.checkRegionControl(iHuman, con.rBactria): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (87,63),(100,59), con.iHeavyHorseArcher, iBonus +iRand1 +1, iGameTurn, 11, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Chionite")
			iBonus = 0
			self.spawnUnits(iBarbarian, (87,63),(100,59), con.iHeavyHorseArcher, iBonus +iRand1 +2, iGameTurn, 13, 3, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Chionite")
			iBonus = 0
		if iGameTurn > getTurnForYear(400) and iGameTurn < getTurnForYear(450):
			if utils.checkRegionControl(iHuman, con.rMargiana) or utils.checkRegionControl(iHuman, con.rParthia) or utils.checkRegionControl(iHuman, con.rSogdiana) or utils.checkRegionControl(iHuman, con.rBactria): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (87,63),(100,59), con.iHeavyHorseArcher, iBonus +iRand1 +1, iGameTurn, 12, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Chionite")
			iBonus = 0
		
		# Hepthalites in Sogdiana this is now covered by the Hephthalite Nomad civ
		if iGameTurn == getTurnForYear(450):
			iCiv = iBarbarian
			if pHephthalites.isAlive(): iCiv = iHephthalites
			if utils.checkRegionControl(iHuman, con.rMargiana) or utils.checkRegionControl(iHuman, con.rParthia) or utils.checkRegionControl(iHuman, con.rSogdiana) or utils.checkRegionControl(iHuman, con.rBactria): iBonus += iHandicap
			self.spawnUnits(iCiv, (80,63),(100,59), con.iHeavyHorseArcher, iBonus +iRand1 +2, iGameTurn, 1, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Hepthalite")
			iBonus = 0
			self.spawnUnits(iCiv, (80,63),(100,59), con.iHeavyHorseArcher, iBonus +iRand1 +2, iGameTurn, 1, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Hepthalite")
			iBonus = 0
		if iGameTurn > getTurnForYear(450) and iGameTurn < getTurnForYear(500):
			iCiv = iBarbarian
			if pHephthalites.isAlive(): iCiv = iHephthalites
			if utils.checkRegionControl(iHuman, con.rMargiana) or utils.checkRegionControl(iHuman, con.rParthia) or utils.checkRegionControl(iHuman, con.rSogdiana) or utils.checkRegionControl(iHuman, con.rBactria): iBonus += iHandicap
			self.spawnUnits(iCiv, (80,63),(100,59), con.iHeavyHorseArcher, iBonus +iRand1 +2, iGameTurn, 2, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Hepthalite")
			iBonus = 0
			self.spawnUnits(iCiv, (80,63),(100,59), con.iHeavyHorseArcher, iBonus +iRand1 +2, iGameTurn, 2, 1, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Hepthalite")
			iBonus = 0
			
		# Huns invade India
		if iGameTurn == getTurnForYear(500):
			iCiv = iBarbarian
			if pHephthalites.isAlive(): iCiv = iHephthalites
			if utils.checkRegionControl(iHuman, con.rArachosia) or utils.checkRegionControl(iHuman, con.rSindh) or utils.checkRegionControl(iHuman, con.rPunjab) or utils.checkRegionControl(iHuman, con.rGandhara) or utils.checkRegionControl(iHuman, con.rBactria) or utils.checkRegionControl(iHuman, con.rAvanti): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (85,44),(102,35), con.iHeavyHorseArcher, iBonus +iRand1 +2, iGameTurn, 1, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Hun")
			iBonus = 0
			self.spawnUnits(iBarbarian, (85,44),(102,35), con.iHeavyHorseArcher, iBonus +iRand1 +2, iGameTurn, 1, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Hun")
			iBonus = 0
		if iGameTurn > getTurnForYear(500) and iGameTurn < getTurnForYear(550):
			iCiv = iBarbarian
			if pHephthalites.isAlive(): iCiv = iHephthalites
			if utils.checkRegionControl(iHuman, con.rArachosia) or utils.checkRegionControl(iHuman, con.rSindh) or utils.checkRegionControl(iHuman, con.rPunjab) or utils.checkRegionControl(iHuman, con.rGandhara) or utils.checkRegionControl(iHuman, con.rBactria) or utils.checkRegionControl(iHuman, con.rAvanti): iBonus += iHandicap
			self.spawnUnits(iBarbarian, (85,44),(102,35), con.iHeavyHorseArcher, iBonus +iRand1 +2, iGameTurn, 2, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Hun")
			iBonus = 0
			self.spawnUnits(iBarbarian, (85,44),(102,35), con.iHeavyHorseArcher, iBonus +iRand1 +2, iGameTurn, 2, 1, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "Hun")
			iBonus = 0

		# AI buildings to make Egyptian UHV harder
		if iGameTurn == getTurnForYear(-180):
			if utils.getHumanID() == con.iEgypt:
				gc.getMap().plot(con.tLuoyang[0], con.tLuoyang[1]).getPlotCity().setNumRealBuilding(con.iGranary, 1)
		if iGameTurn == getTurnForYear(-140):
			if utils.getHumanID() == con.iEgypt:
				gc.getMap().plot(con.tPataliputra[0], con.tPataliputra[1]).getPlotCity().setNumRealBuilding(con.iGranary, 1)
			
	def invasionAlert(self, textKey, playerList = []):
		
		iHuman = utils.getHumanID()
		if utils.isActive(iHuman):
			if not playerList or iHuman in playerList:
				szBuffer = localText.getText(textKey, ())
				CyInterface().addMessage(iHuman, False, con.iDuration, szBuffer, "AS2D_CIVIC_ADOPT", InterfaceMessageTypes.MESSAGE_TYPE_MAJOR_EVENT, None, gc.getInfoTypeForString("COLOR_RED"), -1, -1, False, False)


	def foundCity(self, iCiv, sName, iX, iY, lReligions=[], lBuildings=[]):
	
		if not self.checkRegion(iX, iY):
			return None
		
		pCiv = gc.getPlayer(iCiv)
		pCiv.initCity(iX, iY)
		city = gc.getMap().plot(iX, iY).getPlotCity()
		
		if not city or city.isNone():
			return None
		
		city.setName(sName, False)
		
		if utils.getYear() < 240:
			pCiv.initUnit(con.iSpearman, iX, iY, UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
			pCiv.initUnit(con.iArcher, iX, iY, UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
		else:
			pCiv.initUnit(con.iHeavySpearman, iX, iY, UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
			pCiv.initUnit(con.iMarksman, iX, iY, UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
			
		UnitArtStyler.updateUnitArtAtPlot(city.plot())
		
		for iReligion in lReligions:
			city.setHasReligion(iReligion, True, False, False)
			
		for iBuilding in lBuildings:
			city.setNumRealBuilding(iBuilding, 1)
			
		UnitArtStyler.updateUnitArtAtPlot(city.plot())
		
		return city


	# from Rhye's, simplified
	def checkRegion(self, plotX, plotY):
		
		cityPlot = gc.getMap().plot(plotX, plotY)
		iNumUnitsInAPlot = cityPlot.getNumUnits()
		
		#checks if the plot already belongs to someone
		if cityPlot.isOwned():
			if cityPlot.getOwner() != iBarbarian:
				#print ("owned fail", "x=", plotX, "y=", plotY)
				return False
		
		#checks if there's a unit on the plot
		if iNumUnitsInAPlot:
			for i in range(iNumUnitsInAPlot):
				unit = cityPlot.getUnit(i)
				iOwner = unit.getOwner()
				if iOwner != iBarbarian:
					#print ("unit fail", plotX, "y=", plotY)
					return False
		
		#checks the surroundings and allows only AI units
		for x in range(plotX-1, plotX+2):
			for y in range(plotY-1, plotY+2):
				currentPlot = gc.getMap().plot(x,y)
				if currentPlot.isCity():
					#print ("nearby city fail", plotX, "y=", plotY)
					return False
				iNumUnitsInAPlot = currentPlot.getNumUnits()
				if iNumUnitsInAPlot:
					for i in range(iNumUnitsInAPlot):
						unit = currentPlot.getUnit(i)
						iOwner = unit.getOwner()
						pOwner = gc.getPlayer(iOwner)
						if pOwner.isHuman():
							#print ("nearby human unit fail", plotX, "y=", plotY)
							return False
		
		return True


	def spawnUnits(self, iCiv, tTopLeft, tBottomRight, iUnitType, iNumUnits, iTurn, iPeriod, iRest, function, eUnitAIType = UnitAITypes.UNITAI_ATTACK, prefix = 0, promotionList = [], argsList = []):
		
		if iNumUnits <= 0: # edead
			return None
		pUnit = None # edead
		if (iTurn % utils.getTurns(iPeriod) == iRest):
			dummy, plotList = utils.squareSearch( tTopLeft, tBottomRight, function, [] )
			if (len(plotList)):
				rndNum = gc.getGame().getSorenRandNum(len(plotList), 'Spawn units')
				result = plotList[rndNum]
				if (result):
					pUnit = utils.makeUnit(iUnitType, iCiv, result, iNumUnits, DirectionTypes.DIRECTION_SOUTH, eUnitAIType, promotionList, prefix) # edead: pass the object
					#CyInterface().addMessage(iHuman, False, con.iDuration, prefix, "AS2D_CIVIC_ADOPT", InterfaceMessageTypes.MESSAGE_TYPE_MAJOR_EVENT, None, gc.getInfoTypeForString("COLOR_RED"), -1, -1, False, False)
					#print (prefix, iNumUnits)
					# if eUnitAIType == UnitAITypes.UNITAI_PILLAGE: # edead
						# pUnit.getGroup().setActivityType(ActivityTypes.ACTIVITY_SLEEP) # edead: fortify rebels
		return pUnit # edead: pass the object


	def getRandomUnit(self, unitList):
		
		return unitList[gc.getGame().getSorenRandNum(len(unitList), 'Random unit')]

		
	def isChristianRegion(self, regionID):
		
		bFound = False
		plotList = utils.getRegionPlotList([regionID])
		for tPlot in plotList:
				pCurrent = gc.getMap().plot(tPlot[0], tPlot[1])
				if pCurrent.isCity():
					iOwner = pCurrent.getPlotCity().getOwner()
					if iOwner not in [con.iEgypt, con.iBactria, con.iArmenia, con.iKushans, con.iAxum]:
						return False
					else:
						bFound = True
		return bFound

		
	def makeLeader(self, pUnit, szName, iLeaderType=con.iGreatGeneral):
		
		if pUnit:
			pUnit.setHasPromotion(con.iLeader, True)
			pUnit.setExperience(20, -1)
			pUnit.setLeaderUnitType(iLeaderType)
			pUnit.setName(szName)
	
	def getInvasionForce(self, iBaseNumUnits, iCiv):
	
		iHandicap = gc.getGame().getHandicapType()
		
		iNumUnits = iBaseNumUnits + gc.getGame().getSorenRandNum(3, 'Random invasion force')
		iNumCities = gc.getPlayer(iCiv).getNumCities()
		if iNumCities >= 20:
			iNumUnits += 3
		elif iNumCities >= 12:
			iNumUnits += 2
		elif iNumCities >= 5:
			iNumUnits += iHandicap
		return iNumUnits
		
		