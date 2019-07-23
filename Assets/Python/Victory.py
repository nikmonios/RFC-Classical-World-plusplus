# Rhye's and Fall of Civilization - Historical Victory Goals


from CvPythonExtensions import *
import CvUtil
import PyHelpers   
import Popup
import Consts as con
from StoredData import sd
from RFCUtils import utils

# globals
gc = CyGlobalContext()
PyPlayer = PyHelpers.PyPlayer
localText = CyTranslator()

# initialise player variables
iHarsha = con.iHarsha
iAntigonids = con.iAntigonids
iSeleucids = con.iSeleucids
iEgypt = con.iEgypt
iNubia = con.iNubia
iCarthage = con.iCarthage
iCelts = con.iCelts
iMauryans = con.iMauryans
iTocharians = con.iTocharians
iArmenia = con.iArmenia
iSaba = con.iSaba
iHan = con.iHan
iRome = con.iRome
iPandyans = con.iPandyans
iBactria = con.iBactria
iParthia = con.iParthia
iSatavahana = con.iSatavahana
iDacia = con.iDacia
iGoguryeo = con.iGoguryeo
iKushans = con.iKushans
iAxum = con.iAxum
iFunan = con.iFunan
iSassanids = con.iSassanids
iYamato = con.iYamato
iJin = con.iJin
iGupta = con.iGupta
iVisigoths = con.iVisigoths
iVandals = con.iVandals
iOstrogoths = con.iOstrogoths
iFranks = con.iFranks
iChalukyans = con.iChalukyans
iLombards = con.iLombards
iSrivajaya = con.iSrivajaya
iTang = con.iTang
iArabs = con.iArabs
iGhana = con.iGhana
iQin = con.iQin
iByzantines = con.iByzantines
iGokturks = con.iGokturks
iKhazars = con.iKhazars
iTibet = con.iTibet
iMaccabees = con.iMaccabees
iVietnam = con.iVietnam
iKalinka = con.iKalinka
iGojoseon = con.iGojoseon
iPontus = con.iPontus
iNanYue = con.iNanYue
iIndependent = con.iIndependent
iIndependent2 = con.iIndependent2
iIndependent3 = con.iIndependent3

pAntigonids = gc.getPlayer(iAntigonids)
pSeleucids = gc.getPlayer(iSeleucids)
pEgypt = gc.getPlayer(iEgypt)
pNubia = gc.getPlayer(iNubia)
pCarthage = gc.getPlayer(iCarthage)
pCelts = gc.getPlayer(iCelts)
pMauryans = gc.getPlayer(iMauryans)
pKalinka = gc.getPlayer(iKalinka)
pGojoseon = gc.getPlayer(iGojoseon)
pPontus = gc.getPlayer(iPontus)
pArmenia = gc.getPlayer(iArmenia)
pSaba = gc.getPlayer(iSaba)
pTocharians = gc.getPlayer(iTocharians)
pHan = gc.getPlayer(iHan)
pRome = gc.getPlayer(iRome)
pPandyans = gc.getPlayer(iPandyans)
pBactria = gc.getPlayer(iBactria)
pParthia = gc.getPlayer(iParthia)
pSatavahana = gc.getPlayer(iSatavahana)
pDacia = gc.getPlayer(iDacia)
pGoguryeo = gc.getPlayer(iGoguryeo)
pKushans = gc.getPlayer(iKushans)
pAxum = gc.getPlayer(iAxum)
pFunan = gc.getPlayer(iFunan)
pSassanids = gc.getPlayer(iSassanids)
pYamato = gc.getPlayer(iYamato)
pJin = gc.getPlayer(iJin)
pGupta = gc.getPlayer(iGupta)
pFranks = gc.getPlayer(iFranks)
pVisigoths = gc.getPlayer(iVisigoths)
pVandals = gc.getPlayer(iVandals)
pOstrogoths = gc.getPlayer(iOstrogoths)
pChalukyans = gc.getPlayer(iChalukyans)
pLombards = gc.getPlayer(iLombards)
pSrivajaya = gc.getPlayer(iSrivajaya)
pTang = gc.getPlayer(iTang)
pArabs = gc.getPlayer(iArabs)
pGhana = gc.getPlayer(iGhana)
pQin = gc.getPlayer(iQin)
pByzantines = gc.getPlayer(iByzantines)
pGokturks = gc.getPlayer(iGokturks)
pKhazars = gc.getPlayer(iKhazars)
pTibet = gc.getPlayer(iTibet)
pMaccabees = gc.getPlayer(iMaccabees)
pVietnam = gc.getPlayer(iVietnam)

iNumPlayers = con.iNumPlayers
iBarbarian = con.iBarbarian
iNumTotalPlayers = con.iNumTotalPlayers
iHistoricalVictory = 8

class Victory:


	def checkPlayerTurn(self, iGameTurn, iPlayer):
		
		if not gc.getGame().isVictoryValid(iHistoricalVictory):
			return
			
		
		
		iHuman = utils.getHumanID()
		pPlayer = gc.getPlayer(iPlayer)
		
		if iPlayer != iHuman:
			return
		
		if iPlayer == iAntigonids:
			if pPlayer.isAlive():
				
				# Antigonid UHV1: be the first to discover Monarchy see onTechAcquired
				
				# Antigonid UHV2: build a palace in Pella by 250BC se onBuildingBuilt
				if iGameTurn == getTurnForYear(-250):
					if sd.getGoal(iAntigonids, 1) == -1:
						sd.setGoal(iAntigonids, 1, 0)
					
				# Antigonid UHV3: control 7 wonders by 70BC
				if sd.getGoal(iAntigonids, 2) == -1:
					if iGameTurn <= getTurnForYear(-70):
						iNumWonders = 0
						for iWonder in range (con.iPyramids, con.iShwedagonPaya):
							if self.getNumBuildings(iAntigonids, iWonder):
								iNumWonders += 1
						if iNumWonders >= 7:
							sd.setGoal(iAntigonids, 2, 1)
					else:
						sd.setGoal(iAntigonids, 2, 0)
				
		
		if iPlayer == iSeleucids:
			if pPlayer.isAlive():
				
				# Seleucid UHV1: Control or vassalize provinces by 180BC
				if sd.getGoal(iSeleucids, 0) == -1:
					if iGameTurn <= getTurnForYear(-180):
						bControl = True
						regionList = [con.rMacedonia, con.rEgypt, con.rJudea, con.rAsia, con.rGreece, con.rArachosia, con.rMargiana, con.rSyria, con.rMesopotamia, con.rMedia, con.rPersia, con.rThrace, con.rCappadocia, con.rBactria, con.rSogdiana]
						for regionID in regionList:
							if not utils.checkRegionControl(iSeleucids, regionID, True):
								bControl = False
						if bControl:
							sd.setGoal(iSeleucids, 0, 1)
					else:
						sd.setGoal(iSeleucids, 0, 0)
				
				# Seleucid UHV2: control at least 6 provinces and 12 cities in 75BC
				if sd.getGoal(iSeleucids, 1) == -1:
					if iGameTurn == getTurnForYear(-75):
						if pSeleucids.getNumCities() >= 12: 
							if self.getNumProvinces(iSeleucids) >= 6:
								sd.setGoal(iSeleucids, 1, 1)
						else:
							sd.setGoal(iSeleucids, 1, 0)
				
				# Seleucid UHV3: 3 great generals by 50BC see onGreatPersonBorn
				if iGameTurn == getTurnForYear(-50):
					if sd.getGoal(iSeleucids, 2) == -1:
						sd.setGoal(iSeleucids, 2, 0)
		
		elif iPlayer == iEgypt:
			if pPlayer.isAlive():
				
				# Egypt UHV: Build the Great Lighthouse and the Great Library by 180BC see onBuildingBuilt
				if iGameTurn == getTurnForYear(-180):
					if sd.getGoal(iEgypt, 0) == -1:
						sd.setGoal(iEgypt, 0, 0)
				
				# Egyptian UHV2: Make Alexandria the largest and most cutured city in 100BC
				if iGameTurn == getTurnForYear(-100):
					if self.isTopCityPopulation(iEgypt, con.tAlexandria) and self.isTopCityCulture(iEgypt, con.tAlexandria):
						sd.setGoal(iEgypt, 1, 1)
					else:
						sd.setGoal(iEgypt, 1, 0)
				
				# Egyptian UHV3: Control 7 ports by 150 BC
				if sd.getGoal(iEgypt, 2) == -1:
					if iGameTurn <= getTurnForYear(-150):
						PortList = []
						apCityList = PyPlayer(iEgypt).getCityList()
						for pCity in apCityList:
							if gc.getMap().plot(pCity.getX(), pCity.getY()).getRegionID() in [con.rGreece, con.rThrace, con.rAsia, con.rCrete, con.rRhodes, con.rCyprus, con.rCappadocia, con.rSyria, con.rJudea, con.rEgypt, con.rLibya]:
								if 32 < pCity.getY() < 54:
									if (pCity.getX(), pCity.getY()) not in [(58, 33), (58, 34), (60, 35), (60, 34), (60, 33), (61, 35), (61, 34), (61, 33), (62, 35), (63, 35)] and pCity.GetCy().isCoastal(gc.getMIN_WATER_SIZE_FOR_OCEAN()):
										PortList.append(pCity)
						if len (PortList) >= 7:
							sd.setGoal(iEgypt, 2, 1)
					else:
						sd.setGoal(iEgypt, 2, 0)
		
		elif iPlayer == iCarthage:
			if pPlayer.isAlive():
				
				# Carthaginian UHV1: Obtain 6 luxury resources by 150BC
				if sd.getGoal(iCarthage, 0) == -1:
					if iGameTurn <= getTurnForYear(-150):
						if self.getNumLuxuries(iCarthage) >= 6:
							sd.setGoal(iCarthage, 0, 1)
					else:
						sd.setGoal(iCarthage, 0, 0)
						
				# Carthaginian UHV2: Destroy the Romans by 100BC
				if sd.getGoal(iCarthage, 1) == -1:
					if iGameTurn >= getTurnForYear(-269) and iGameTurn <= getTurnForYear(-50):
						if not pRome.isAlive():
							sd.setGoal(iCarthage, 1, 1)
					elif iGameTurn >= getTurnForYear(-49):
						sd.setGoal(iCarthage, 1, 0)
				
				# Carthaginian UHV3: Control or trade for 9 luxury resources by 50AD
				if sd.getGoal(iCarthage, 2) == -1:
					if iGameTurn <= getTurnForYear(50):
						if self.getNumLuxuries(iCarthage) >= 9:
							sd.setGoal(iCarthage, 2, 1)
					else:
						sd.setGoal(iCarthage, 2, 0)
		
		elif iPlayer == iMauryans:
			if pPlayer.isAlive():
				
				if sd.getCivilization(iMauryans) == iMauryans:
					# Mauryan UHV1: Control Asoka's empire by 200BC
					if sd.getGoal(iMauryans, 0) == -1:
						if iGameTurn <= getTurnForYear(-200):
							bControl = True
							regionList = [con.rMagadha, con.rGandhara, con.rKalinka, con.rAvanti, con.rSindh, con.rArachosia, con.rPunjab, con.rDeccan, con.rKerala, con.rBangala, con.rSaurashtra, con.rAndhra, con.rBharat]
							for regionID in regionList:
								if not utils.checkRegionControl(iMauryans, regionID):
									bControl = False
							if bControl:
								sd.setGoal(iMauryans, 0, 1)
						else:
							sd.setGoal(iMauryans, 0, 0)
				
					# Mauryan UHV2: Build 10 Edicts by 200BC see onBuildingBuilt
					if iGameTurn == getTurnForYear(-200):
						if sd.getGoal(iMauryans, 1) == -1:
							sd.setGoal(iMauryans, 1, 0)
						
					# Mauryan UHV3: Spread Buddhism to every city in India by 150BC
					if sd.getGoal(iMauryans, 2) == -1:
						if iGameTurn <= getTurnForYear(-150):
							bSuccess = True
							for iLoopCiv in range(iNumTotalPlayers):
								apCityList = PyPlayer(iLoopCiv).getCityList()
								for pCity in apCityList:
									if gc.getMap().plot(pCity.getX(), pCity.getY()).getRegionID() in con.lIndianRegions:
										if not pCity.GetCy().isHasReligion(con.iBuddhism):
											bSuccess = False
											break
							if bSuccess:
								sd.setGoal(iMauryans, 2, 1)
						else:
							sd.setGoal(iMauryans, 2, 0)
							
				else:	
					# Harsha UHV1 control provinces
					if sd.getGoal(iMauryans, 0) == -1:
						if iGameTurn <= getTurnForYear(650):
							bControl = True
							regionList = [con.rMagadha, con.rGandhara, con.rSindh, con.rPunjab, con.rBangala, con.rSaurashtra, con.rBharat]
							for regionID in regionList:
								if not utils.checkRegionControl(iMauryans, regionID):
									bControl = False
							if bControl:
								sd.setGoal(iMauryans, 0, 1)
						else:
							sd.setGoal(iMauryans, 0, 0)
						
					# Harsha UHV2: great artist by 640AD see onGreatPersonBorn
					if sd.getGoal(iMauryans, 1) == -1:
						if iGameTurn >= getTurnForYear(640):
							sd.setGoal(iMauryans, 1, 0)
						
					# Harsha UHV3: Buddhist Cathedral by 640AD see onBuildingBuilt
					if sd.getGoal(iMauryans, 2) == -1:
						if iGameTurn >= getTurnForYear(640):
							sd.setGoal(iMauryans, 2, 0)
						
		elif iPlayer == iKalinka:
			if pPlayer.isAlive():
				
				# Kalinka UHV3: control at least 1 source of horses by 150BC
				if sd.getGoal(iKalinka, 0) == -1:
					if iGameTurn <= getTurnForYear(-150):
						if (pPlayer.getNumAvailableBonuses(con.iHorse)) >= 1:
							sd.setGoal(iKalinka, 0, 1)
					else:
						sd.setGoal(iKalinka, 0, 0)
						
				# Kalinka UHV2: 2 great prophets and 2 great generals by 100BC see onGreatPersonBorn
				if sd.getGoal(iKalinka, 1) == -1:
					if iGameTurn >= getTurnForYear(-100):
						sd.setGoal(iKalinka, 1, 0)
					
				# Kalinka UHV3: 7 Jain buildings by 50BC see onBuildingBuilt
				if sd.getGoal(iKalinka, 2) == -1: 
					if iGameTurn >= getTurnForYear(-50):
						sd.setGoal(iKalinka, 2, 0)
					
		elif iPlayer == iQin:
			if pPlayer.isAlive():
			
				if sd.get3KingdomsMarker() == 1:
				
					# Jin UHV1: control china in 300AD
					if iGameTurn == getTurnForYear(300):
						bControl = true
						regionList = [con.rHan, con.rChu, con.rQi, con.rQin, con.rMinYue, con.rNanYue, con.rShu, con.rBa, con.rWu, con.rChu, con.rYan, con.rZhao]
						for regionID in regionList:
							if not utils.checkRegionControl(iJin, regionID):
								bControl = False
						if bControl:
							sd.setGoal(iJin, 0, 1)
						else:
							sd.setGoal(iJin, 0, 0)
					
					# Jin UHV2: 6 luxuries in 350AD
					if sd.getGoal(iJin, 1) == -1:
						if iGameTurn <= getTurnForYear(350):
							if self.getNumLuxuries(iJin) >= 6:
								sd.setGoal(iJin, 1, 1)
						else:
							sd.setGoal(iJin, 1, 0)
					
					# Jin UHV3: Be the first to discover The Stirrup, see onTechAcquired
					
				else:
				
					# Qin UHV1: Build the Great Wall and the Terracotta Army by 215BC
					if sd.getGoal(iQin, 0) == -1:
						if iGameTurn >= getTurnForYear(-215):
							sd.setGoal(iQin, 0, 0)
					
					# Qin UHV2: control central and north China by 210BC
					if sd.getGoal(iQin, 1) == -1:
						if iGameTurn <= getTurnForYear(-210):
							bControl = True
							regionList = [con.rQin, con.rHan, con.rYan, con.rZhao, con.rChu, con.rNanYue, con.rQi, con.rWu, con.rShu]
							for regionID in regionList:
								if not utils.checkRegionControl(iQin, regionID):
									bControl = False
							if bControl:
								sd.setGoal(iQin, 1, 1)
						else:
							sd.setGoal(iQin, 1, 0)
					
					# Qin UHV3: control at least 9 provinces in 100BC
					if sd.getGoal(iQin, 2) == -1:
						if iGameTurn == getTurnForYear(-100):
							if self.getNumProvinces(iQin) >= 9:
								sd.setGoal(iQin, 2, 1)
							else:
								sd.setGoal(iQin, 2, 0)
							
		elif iPlayer == iGojoseon:
			if pPlayer.isAlive():
			
				# Gojoseon UHV1: kill 20 Chinese units and capture 3 Chinese cities by 100BC expire check only see onCombatResult and onCityAcquired
				if sd.getGoal(iGojoseon, 0) == -1:
					if iGameTurn >= getTurnForYear(-100):
						sd.setGoal(iGojoseon, 0, 0)
						
				# Gojoseon UHV2: be the first to discover Marksmanship see onTechAcquired
						
				# Gojoseon UHV3: never lose a city before 50BC see onCityAcquired
				if sd.getGoal(iGojoseon, 2) == -1:
					if iGameTurn == getTurnForYear(-50):
						sd.setGoal(iGojoseon, 2, 1)
		
		elif iPlayer == iNubia:
			if pPlayer.isAlive():
				
				# Nubian UHV1: Research Alphabet and Iron Working before 200BC, see onTechAcquired
				if sd.getGoal(iNubia, 0) == -1:
					if iGameTurn >= getTurnForYear(-200):
						sd.setGoal(iNubia, 0, 0)
				
				# Nubian UHV2: Be the most productive civ in 100BC
				if iGameTurn == getTurnForYear(-100):
					if self.isMostProductive(iNubia):
						sd.setGoal(iNubia, 1, 1)
					else:
						sd.setGoal(iNubia, 1, 0)
				
				# Nubian UHV3: at least 5 gold by 50BC
				if sd.getGoal(iNubia, 2) == -1:
					if iGameTurn <= getTurnForYear(-50):
						if (pPlayer.getNumAvailableBonuses(con.iGold) >= 5):
							sd.setGoal(iNubia, 2, 1)
					else:
						sd.setGoal(iNubia, 2, 0)
		
		elif iPlayer == iSaba:
			if pPlayer.isAlive():
				
				# Sabean UHV1: control at least 4 cities by 150BC
				if sd.getGoal(iSaba, 0) == -1:
					if iGameTurn <= getTurnForYear(-100):
						if pPlayer.getNumCities() >= 4:
							sd.setGoal(iSaba, 0, 1)
					else:
						sd.setGoal(iSaba, 0, 0)
				
				# Sabean UHV2: 3000 culture by 50AD
				if sd.getGoal(iSaba, 1) == -1:
					if iGameTurn <= getTurnForYear(50):
						if pPlayer.countTotalCulture() >= 3000 * (gc.getGame().getGameSpeedType() + 2) / 2:
							sd.setGoal(iSaba, 1, 1)
					else:
						sd.setGoal(iSaba, 1, 0)
				
				# Sabean UHV3: Incense Merchants
				if sd.getGoal(iSaba, 2) == -1:
					if iGameTurn >= getTurnForYear(100):
						sd.setGoal(iSaba, 2, 0)
						
						
		if iPlayer == iPontus:
			if pPlayer.isAlive():
				
				# Pontic UHV1: Control or vassalize provinces by 90BC
				if sd.getGoal(iPontus, 0) == -1:
					if iGameTurn <= getTurnForYear(-90):
						bControl = True
						regionList = [con.rPontus, con.rCappadocia, con.rAsia, con.rCrimea, con.rThrace]
						for regionID in regionList:
							if not utils.checkRegionControl(iPontus, regionID):
								bControl = False
						if bControl:
							sd.setGoal(iPontus, 0, 1)
					else:
						sd.setGoal(iPontus, 0, 0)
						
				# Pontic UHV2: capture 3 Roman cities or control 7 provinces including Greece by 30BC
				if sd.getGoal(iPontus, 1) == -1:
					if iGameTurn <= getTurnForYear(-30):
						if self.getNumProvinces(iPontus) >= 7 and utils.checkRegionControl(iPontus, con.rGreece):
							sd.setGoal(iPontus, 1, 1)
					else:
						sd.setGoal(iPontus, 1, 0)
							
				# Pontic UHV3: have friendly relations with 3 other civs by 100AD
				if sd.getGoal(iPontus, 2) == -1:
					if iGameTurn <= getTurnForYear(100):
						if self.countPlayersByMinAttitude(iPontus, 4) >= 3:
							sd.setGoal(iPontus, 2, 1)
					else:
						sd.setGoal(iPontus, 2, 0)
						
		
		elif iPlayer == iPandyans:
			if pPlayer.isAlive():
			
				if sd.get3KingdomsMarker() == 3:
					# Chola UHV1: control east coast of India by 150BC
					if sd.getGoal(iPandyans, 0) == -1:
						if iGameTurn <= getTurnForYear(-150):
							bControl = True
							regionList = [con.rLanka, con.rTamilNadu, con.rAndhra, con.rKalinka, con.rBangala]
							for regionID in regionList:
								if not utils.checkRegionControl(iPandyans, regionID):
									bControl = False
							if bControl:
								sd.setGoal(iPandyans, 0, 1)
						else:
							sd.setGoal(iPandyans, 0, 0)
							
					# Chola UHV2: build the heoic epic and the Grand Anicut by 150BC see onBuildingBuilt
					if sd.getGoal(iPandyans, 1) == -1:
						if iGameTurn == getTurnForYear(-150):
							sd.setGoal(iPandyans, 1, 0)
							
					# Chola UHV3: Have at least 2 vassals in 50BC
					if iGameTurn == getTurnForYear(-50):
						if self.getNumVassals(iPandyans) >= 1:
							sd.setGoal(iPandyans, 2, 1)
						else:
							sd.setGoal(iPandyans, 2, 0)
						
				elif sd.get3KingdomsMarker() == 4:
					
					# Pandyan UHV1: at least 1 silk and 1 gold and 1 silver by 50BC
					if sd.getGoal(iPandyans, 0) == -1:
						if iGameTurn <= getTurnForYear(-50):
							if ((pPlayer.getNumAvailableBonuses(con.iGold)) + (pPlayer.getNumAvailableBonuses(con.iSilk)) + (pPlayer.getNumAvailableBonuses(con.iIncense)) + (pPlayer.getNumAvailableBonuses(con.iSilver)) >= 2):
								sd.setGoal(iPandyans, 0, 1)
						else:
							sd.setGoal(iPandyans, 0, 0)
							
					# Pandyan UHV1: build 2 Cloth Markets and Spice Markets by 50AD see onBuildingBuilt
					if iGameTurn == getTurnForYear(50):
						if sd.getGoal(iPandyans, 1) == -1:
							sd.setGoal(iPandyans, 1, 0)
					
					# Pandyan UHV3: Be the first to discover Steel Working, see onTechAcquired
					
				elif sd.get3KingdomsMarker() == 5:
					
					# Chera UHV1:  9 Temples in Tamil Nadu by 50BC
					if sd.getGoal(iPandyans, 0) == -1:
						if iGameTurn <= getTurnForYear(-50):
							iNumTemples = 0
							apCityList = PyPlayer(iPandyans).getCityList()
							for pCity in apCityList:
								if gc.getMap().plot(pCity.getX(), pCity.getY()).getRegionID() == con.rTamilNadu:
									for iBuilding in range(con.iJewishTemple, con.iIslamicShrine):
										if pCity.GetCy().getNumRealBuilding(iBuilding):
											iNumTemples += 1
							if iNumTemples >= 9:
								sd.setGoal(iPandyans, 0, 1)
						else:
							sd.setGoal(iPandyans, 0, 0)
								
					# Chera UHV3: settle 2 great artists and 2 great saints in your cities by 50AD
					if sd.getGoal(iPandyans, 1) == -1:
						if iGameTurn <= getTurnForYear(50):
							iNumArtists = 0
							iNumSaints = 0
							apCityList = PyPlayer(iPandyans).getCityList()
							for pCity in apCityList:
								iNumArtists += pCity.GetCy().getFreeSpecialistCount(gc.getInfoTypeForString("SPECIALIST_GREAT_ARTIST"))
								iNumSaints += pCity.GetCy().getFreeSpecialistCount(gc.getInfoTypeForString("SPECIALIST_GREAT_PRIEST"))
							if iNumArtists >= 2 and iNumSaints >= 2:
								sd.setGoal(iPandyans, 1, 1)
						else:
							sd.setGoal(iPandyans, 1, 0)
							
					# Chera UHV2: Tamil culture better than the rest of India in 100AD
					if sd.getGoal(iPandyans, 2) == -1:
						if iGameTurn == getTurnForYear(100):
							iTamilCulture = 0
							iIndianCulture = 0
							for iLoopCiv in range(iNumTotalPlayers): 
								apCityList = PyPlayer(iLoopCiv).getCityList()
								for pCity in apCityList:
									if gc.getMap().plot(pCity.getX(), pCity.getY()).getRegionID() == con.rTamilNadu:
										iTamilCulture += pCity.getCulture()
									elif gc.getMap().plot(pCity.getX(), pCity.getY()).getRegionID() in con.lIndianRegions:
										iIndianCulture += pCity.getCulture()
							if iTamilCulture > iIndianCulture:
								sd.setGoal(iPandyans, 2, 1)
							else:
								sd.setGoal(iPandyans, 2, 0)
						
		
		elif iPlayer == iCelts:
			if pPlayer.isAlive():
				
				# Celtic UHV1: capture Rome before 150BC see onCityAcquired
				if sd.getGoal(iCelts, 0) == -1:
					if iGameTurn == getTurnForYear(-150):
						sd.setGoal(iCelts, 0, 0)
				
				# Celtic UHV2: colonize the Celtic world by 100BC
				if sd.getGoal(iCelts, 1) == -1:
					if iGameTurn <= getTurnForYear(-100):
						bControl = True
						regionList = [con.rGaul, con.rNItaly,con.rSeptimania, con.rAquitania, con.rIberia, con.rGermania, con.rIllyricum, con.rBritannia]
						for regionID in regionList:
							if not utils.checkRegionOwnedCity(iCelts, regionID):
								bControl = False
						if bControl:
							sd.setGoal(iCelts, 1, 1)
					else:
						sd.setGoal(iCelts, 1, 0)
				
				# Celtic UHV3: Best culture by 75BC
				if sd.getGoal(iCelts, 2) == -1:
					if iGameTurn <= getTurnForYear(-75):
						if self.isTopCulture(iCelts):
							sd.setGoal(iCelts, 2, 1)
					else:
						sd.setGoal(iCelts, 2, 0)
		
		elif iPlayer == iRome:
		
			if pRome.isAlive():
				if gc.getTeam(pRome.getTeam()).isHasTech(con.iRomanEmpire):
				
					# Roman Empire UHV1: Control provinces by 75BC
					if sd.getGoal(iRome, 0) == -1:
						if iGameTurn <= getTurnForYear(-75):
							bControl = True
							regionList = [con.rNItaly, con.rSItaly, con.rSicily, con.rIberia, con.rBaetica, con.rSeptimania, con.rAfrica, con.rGreece, con.rAsia, con.rSyria, con.rJudea, con.rEgypt, con.rLibya, con.rCappadocia]
							for regionID in regionList:
								if not utils.checkRegionControl(iRome, regionID):
									bControl = False
							if bControl:
								sd.setGoal(iRome, 0, 1)
						else:
							sd.setGoal(iRome, 0, 0)
						
					# Roman Empire UHV2: make Rome the largest city in the world in 50AD
					if sd.getGoal(iRome, 1) == -1:
						if iGameTurn == getTurnForYear(50):
							if self.isTopCityPopulation(iRome, con.tRome):
								sd.setGoal(iRome, 1, 1)
							else:
								sd.setGoal(iRome, 1, 0)
				
					# Roman Empire UHV3: Control provinces by 125AD
					if sd.getGoal(iRome, 2) == -1:
						if iGameTurn <= getTurnForYear(125):
							bControl = True
							regionList = [con.rNItaly, con.rSItaly, con.rSicily, con.rIberia, con.rLusitania, con.rBaetica, con.rSeptimania, con.rAquitania, con.rAfrica, con.rGreece, con.rAsia, con.rSyria, con.rJudea, con.rEgypt, con.rLibya, con.rGaul, con.rBritannia, con.rIllyricum, con.rThrace, con.rMesopotamia, con.rDacia, con.rMauretania, con.rCrimea, con.rArmenia, con.rCappadocia, con.rPontus, con.rNumidia]
							for regionID in regionList:
								if not utils.checkRegionControl(iRome, regionID):
									bControl = False
							if bControl:
								sd.setGoal(iRome, 2, 1)
						else:
							sd.setGoal(iRome, 2, 0)
					
				else:
				
					# Roman Republic UHV1: dominate the Mediterranean by 50BC
					if sd.getGoal(iRome, 0) == -1:
						if iGameTurn <= getTurnForYear(-75):
							iRomanMedProvinces = 0
							#iOtherMedProvinces = 0
							regionList = [con.rNItaly, con.rSItaly, con.rSicily, con.rIberia, con.rBaetica, con.rSeptimania, con.rAfrica, con.rGreece, con.rAsia, con.rSyria, con.rJudea, con.rEgypt, con.rLibya, con.rMauretania, con.rCyprus, con.rCrete, con.rSardinia, con.rCorsica, con.rThrace, con.rNumidia, con.rRhodes, con.rMallorca, con.rMacedonia, con.rIllyricum]
							for regionID in regionList:
								if utils.checkRegionControl(iRome, regionID):
									iRomanMedProvinces += 1
							#for iCiv in range (iNumTotalPlayers):
								#if iCiv != iRome:
									#for regionID in regionList:
										#if utils.checkRegionControl(iCiv, regionID):
											#iOtherMedProvinces += 1
							if iRomanMedProvinces >= 10 and utils.checkRegionControl(iRome, con.rSicily)and utils.checkRegionControl(iRome, con.rAfrica): #(iOtherMedProvinces * 2):
								sd.setGoal(iRome, 0, 1)
						else:
							sd.setGoal(iRome, 0, 0)
								
					# Roman Republic UHV2: be the first to discover Engineering and Jurisprudence see onTechAcquired
					
					# Roman Republic UHV3: settle five great people in Rome by 50AD
					if sd.getGoal(iRome, 2) == -1:
						if iGameTurn <= getTurnForYear(50):
							iCount = 0
							if pPlayer.getNumCities() > 0:
								capital = pPlayer.getCapitalCity()
								if self.countGreatPeople((capital.getX(), capital.getY())) >= 5:
									sd.setGoal(iRome, 2, 1)
						else:
							sd.setGoal(iRome, 2, 0)
							
				
		elif iPlayer == iVietnam:
			if pVietnam.isAlive():
			
				# Vietnam UHV1: control the most populous province by 50BC
				if sd.getGoal(iVietnam, 0) == -1:
					if iGameTurn <= getTurnForYear(-50):
						regionList = [con.rAnnam, con.rChampa, con.rNanYue]
						bControl = True
						for regionID in regionList:
							if not utils.checkRegionControl(iVietnam, regionID):
								bControl = False
						if bControl == True:
							sd.setGoal(iVietnam, 0, 1)
					else:
						sd.setGoal(iVietnam, 0, 0)
						
				# Vietnam UHV2: higher population and culture than the Han in 100AD
				if sd.getGoal(iVietnam, 1) == -1:
					if iGameTurn == getTurnForYear(50):
						if gc.getPlayer(iVietnam).getRealPopulation() > gc.getPlayer(iHan).getRealPopulation() and gc.getPlayer(iVietnam).countTotalCulture() > gc.getPlayer(iHan).countTotalCulture():
							sd.setGoal(iVietnam, 1, 1)
						else:
							sd.setGoal(iVietnam, 1, 0)
						
				# Vietnam UHV3: build 12 Buddhist buildings by 100AD see onCityAcquired
				if sd.getGoal(iVietnam, 2) == -1:
					if iGameTurn >= getTurnForYear(100):
						sd.setGoal(iVietnam, 2, 0)
		
		elif iPlayer == iTocharians:
			if pPlayer.isAlive():
				
				# Tocharian UHV1: Open borders x 5 by 100AD
				if sd.getGoal(iTocharians, 0) == -1:
					if iGameTurn <= getTurnForYear(100):
						if self.getNumOpenBorders(iTocharians) >= 5:
							sd.setGoal(iTocharians, 0, 1)
					else:
						sd.setGoal(iTocharians, 0, 0)
				
				# Tocharian UHV3: at least 1 silk and 1 incense by 100AD
				if sd.getGoal(iTocharians, 1) == -1:
					if iGameTurn <= getTurnForYear(100):
						if (pPlayer.getNumAvailableBonuses(con.iIncense) >= 1 and pPlayer.getNumAvailableBonuses(con.iSilk) >= 1):
							sd.setGoal(iTocharians, 1, 1)
					else:
						sd.setGoal(iTocharians, 1, 0)
				
				# Tocharian UHV3: Spread Buddhism to 5 Chinese or Korean cities by 200AD
				if sd.getGoal(iTocharians, 2) == -1:
					if iGameTurn == getTurnForYear(200):
						sd.setGoal(iTocharians, 2, 0)
						
				
							
		
		elif iPlayer == iBactria:
			if pBactria.isAlive():
				
				# Bactrian UHV1: Build a Palace in Taxila by 100BC
				if sd.getGoal(iBactria, 0) == -1:
					if iGameTurn >= getTurnForYear(-100):
						sd.setGoal(iBactria, 0, 0)
						
				# Bactrian UHV2: control 3 Indian provinces by 50BC
				if sd.getGoal(iBactria, 1) == -1:
					if iGameTurn <= getTurnForYear(-50):
						iNumProvinces = 0
						regionList = [con.rGandhara, con.rSindh, con.rPunjab, con.rAvanti, con.rMagadha, con.rDeccan, con.rKerala, con.rSaurashtra, con.rTamilNadu]
						for regionID in regionList:
							if utils.checkRegionControl(iBactria, regionID):
								iNumProvinces += 1
						if iNumProvinces >= 3:
							sd.setGoal(iBactria, 1, 1)
					else:
						sd.setGoal(iBactria, 1, 0)
				
				# Bactrian UHV3: 6,000 gold by 50AD
				if sd.getGoal(iBactria, 2) == -1:
					if iGameTurn <= getTurnForYear(50):
						iCities = 0
						iGreatPriest = gc.getInfoTypeForString("SPECIALIST_GREAT_PRIEST")
						iGreatScientist = gc.getInfoTypeForString("SPECIALIST_GREAT_SCIENTIST")
						apCityList = PyPlayer(iBactria).getCityList()
						for pCity in apCityList:
							if pCity.GetCy().isHasReligion(con.iBuddhism) and pCity.GetCy().isHasReligion(con.iHellenism):
								if (pCity.getFreeSpecialistCount(iGreatPriest) >= 1) or (pCity.getFreeSpecialistCount(iGreatScientist) >= 1):
									iCities += 1
						if iCities >= 3:
							sd.setGoal(iBactria, 2, 1)
					else:
						sd.setGoal(iBactria, 2, 0)
				
				
		
		elif iPlayer == iHan:
			if pHan.isAlive():
			
				if sd.get3KingdomsMarker() == 2:
				
					# Jin UHV1: control china in 300AD
					if iGameTurn == getTurnForYear(300):
						bControl = true
						regionList = [con.rHan, con.rChu, con.rQi, con.rQin, con.rMinYue, con.rNanYue, con.rShu, con.rBa, con.rWu, con.rChu, con.rYan, con.rZhao]
						for regionID in regionList:
							if not utils.checkRegionControl(iJin, regionID):
								bControl = False
						if bControl:
							sd.setGoal(iJin, 0, 1)
						else:
							sd.setGoal(iJin, 0, 0)
					
					# Jin UHV2: 6 luxuries in 350AD
					if sd.getGoal(iJin, 1) == -1:
						if iGameTurn <= getTurnForYear(350):
							if self.getNumLuxuries(iJin) >= 6:
								sd.setGoal(iJin, 1, 1)
						else:
							sd.setGoal(iJin, 1, 0)
					
					# Jin UHV3: Be the first to discover The Stirrup, see onTechAcquired
					
				else:
					
					# Han UHV1: Control provinces by 50BC
					if sd.getGoal(iHan, 0) == -1:
						if iGameTurn <= getTurnForYear(-50):
							bControl = True
							regionList = [con.rQin, con.rHan, con.rQi, con.rChu, con.rShu, con.rBa, con.rYan, con.rZhao, con.rGansu, con.rTarim, con.rNanYue, con.rMinYue]
							for regionID in regionList:
								if not utils.checkRegionControl(iHan, regionID):
									bControl = False
							if bControl:
								sd.setGoal(iHan, 0, 1)
						else:
							sd.setGoal(iHan, 0, 0)
							
							
					
					
					# Han UHV2: Be the first to discover Paper, see onTechAcquired
					if sd.getGoal(iHan, 1) == -1:
						if iGameTurn == getTurnForYear(100):
							sd.setGoal(iHan, 1, 0)
							
					# Han UHV3: double nearest rivals population in 150AD
					if sd.getGoal(iHan, 2) == -1:
						if iGameTurn == getTurnForYear(150):
							iPop = gc.getPlayer(iHan).getRealPopulation() / 2
							bHighest = True
							for iLoopCiv in range(iNumPlayers):
								if iLoopCiv != iHan:
									if iPop < gc.getPlayer(iLoopCiv).getRealPopulation():
										bHighest = False
										break
							if bHighest == True:
								sd.setGoal(iHan, 2, 1)
							else:
								sd.setGoal(iHan, 2, 0)
		
		elif iPlayer == iSatavahana:
			if pSatavahana.isAlive():
				
				# Satavahana UHV1: Control 2 Shrines by 50BC
				if sd.getGoal(iSatavahana, 0) == -1:
					if iGameTurn <= getTurnForYear(-50):
						iNumShrines = (self.getNumBuildings(iSatavahana, con.iJainShrine) + self.getNumBuildings(iSatavahana, con.iHinduShrine) + self.getNumBuildings(iSatavahana, con.iBuddhistShrine) + self.getNumBuildings(iSatavahana, con.iZoroastrianShrine) + self.getNumBuildings(iSatavahana, con.iJewishShrine) + self.getNumBuildings(iSatavahana, con.iTaoistShrine) + self.getNumBuildings(iSatavahana, con.iConfucianShrine) + self.getNumBuildings(iSatavahana, con.iChristianShrine) + self.getNumBuildings(iSatavahana, con.iManicheanShrine) + self.getNumBuildings(iSatavahana, con.iIslamicShrine) + self.getNumBuildings(iSatavahana, con.iHellenicShrine))
						if iNumShrines >= 2:
							sd.setGoal(iSatavahana, 0, 1)
					else:
						sd.setGoal(iSatavahana, 0, 0)
				
				# Satavahana UHV2: 15,000 culture by 1AD
				if sd.getGoal(iSatavahana, 1) == -1:
					if iGameTurn <= getTurnForYear(1):
						if pSatavahana.countTotalCulture() > 15000:
							sd.setGoal(iSatavahana, 1, 1)
					else:
						sd.setGoal(iSatavahana, 1, 0)
				
				# Satavahana UHV3: Spread Buddhism and Hinduism to 3 southeast asian cities by 50AD
				if sd.getGoal(iSatavahana, 2) == -1:
					if iGameTurn == getTurnForYear(50):
						sd.setGoal(iSatavahana, 2, 0)
		
		elif iPlayer == iArmenia:
			if pArmenia.isAlive():
				
				# Armenian UHV1: Tigranes empire
				if sd.getGoal(iArmenia, 0) == -1:
					if iGameTurn == getTurnForYear(-50):
						bControl = true
						regionList = [con.rArmenia, con.rCaucasus, con.rSyria, con.rCappadocia, con.rMedia]
						for regionID in regionList:
							if not utils.checkRegionControl(iArmenia, regionID):
								bControl = False
						if bControl:
							sd.setGoal(iArmenia, 0, 1)
						else:
							sd.setGoal(iArmenia, 0, 0)
			
				# Armenian UHV2: 1st Christian civ see onPlayerChangeStateReligion
				
				# Armenian UHV3: never lose a city before 100ad see onCityAcquired
				if iGameTurn == getTurnForYear(100):
					if sd.getGoal(iArmenia, 2) == -1:
						sd.setGoal(iArmenia, 2, 1)
						
		elif iPlayer == iMaccabees:
			if pMaccabees.isAlive():
				
				# Maccabees UHV1 capture 4 cities with Jewish populations before 50AD, and hold them in 50AD see onCityAcquired
				if iGameTurn == getTurnForYear(50):
					if sd.getWondersBuilt(iMaccabees) >= 4:
						sd.setGoal(iMaccabees, 0, 1)
					else:
						sd.setGoal(iMaccabees, 0, 0)
				# Maccabees UHV1: have open borders with all civs with Jewish populations in 50AD
				#if iGameTurn == getTurnForYear(50):
					#bSuccess = true
					#for iLoopCiv in range(iNumPlayers):
						#if iLoopCiv != iMaccabees:
							#if gc.getPlayer(iLoopCiv).isAlive():
								#cityList = PyPlayer(iLoopCiv).getCityList()
								#for pCity in cityList:
									#if pCity.GetCy().isHasReligion(con.iJudaism):
										#if not gc.getTeam(pMaccabees.getTeam()).isOpenBorders(iLoopCiv):
											#bSuccess = false
											#break
					#if bSuccess:
						#sd.setGoal(iMaccabees, 0, 1)
					#else:
						#sd.setGoal(iMaccabees, 0, 0)
						
				# Maccabees UHV2: build the Temple of Solomon by 75BC see onBuildingBuilt
				if iGameTurn == getTurnForYear(-75):
					if sd.getGoal(iMaccabees, 1) == -1:
						sd.setGoal(iMaccabees, 1, 0)
						
				# Maccabees UHV3: spread Judaism to 1/2 the world's civs and 1/3 of its cities
				if iGameTurn == getTurnForYear(100):
					if sd.getGoal(iMaccabees, 2) == -1:
						sd.setGoal(iMaccabees, 2, 0)
				
				
		
		elif iPlayer == iParthia:
			if pParthia.isAlive():
				
				# Parthian UHV2: 5% land by 50AD
				if sd.getGoal(iParthia, 0) == -1:
					if iGameTurn <= getTurnForYear(50):
						totalLand = gc.getMap().getLandPlots()
						ownedLand = pParthia.getTotalLand()
						if totalLand > 0:
							landPercent = (ownedLand * 100.0) / totalLand
						else:
							landPercent = 0.0
						if landPercent >= 4.995:
							sd.setGoal(iParthia, 0, 1)
					else:
						sd.setGoal(iParthia, 0, 0)
				
				# Parthian UHV2: Build a Palace and the National Epic in Ctesiphon by 50BC
				if iGameTurn == getTurnForYear(-50) + 1:
					if sd.getGoal(iParthia, 1) == -1:
						sd.setGoal(iParthia, 1, 0)
						
				# Parthian UHV3: Kill 20 Roman units see onCombatResult
		
		elif iPlayer == iDacia:
			if pDacia.isAlive():
				
				# Dacian UHV1: control Dacia, Thrace and Illyricum in 50AD
				if iGameTurn == getTurnForYear(50):
					bControl = true
					regionList = [con.rDacia, con.rThrace, con.rIllyricum]
					for regionID in regionList:
						if not utils.checkRegionOwnedCity(iDacia, regionID):
							bControl = False
					if bControl:
						sd.setGoal(iDacia, 0, 1)
					else:
						sd.setGoal(iDacia, 0, 0)
				
				# Dacian UHV2: 3,000 gold in 150AD
				if sd.getGoal(iDacia, 1) == -1:
					if iGameTurn <= getTurnForYear(150):
						if pDacia.getGold() >= 5000 * (gc.getGame().getGameSpeedType() + 2) / 2:
							sd.setGoal(iDacia, 1, 1)
					else:
						sd.setGoal(iDacia, 1, 0)
				
				# Dacian UHV3: Gain control of at least 6 provinces before 250AD
				if sd.getGoal(iDacia, 2) == -1:
					if iGameTurn <= getTurnForYear(250):
						if pDacia.getNumCities() >= 6: # efficiency
							if self.getNumProvinces(iDacia) >= 6:
								sd.setGoal(iDacia, 2, 1)
					else:
						sd.setGoal(iDacia, 2, 0)
		
		elif iPlayer == iGoguryeo:
			if pGoguryeo.isAlive():
				
				# Goguryeo UHV1: 1st Buddhist east asian civ see onPlayerChangeStateReligion 
				
				# Goguryeo UHV2: Gain control of at least 6 provinces before 400AD
				if sd.getGoal(iGoguryeo, 1) == -1:
					if iGameTurn <= getTurnForYear(300):
						if pGoguryeo.getNumCities() >= 6: # efficiency
							if self.getNumProvinces(iGoguryeo) >= 6:
								sd.setGoal(iGoguryeo, 1, 1)
					else:
						sd.setGoal(iGoguryeo, 1, 0)
				
				# Goguryeo UHV3: Best culture in 400
				if iGameTurn == getTurnForYear(400):
					if self.isTopCulture(iGoguryeo):
						sd.setGoal(iGoguryeo, 2, 1)
					else:
						sd.setGoal(iGoguryeo, 2, 0)
				
				
		
		elif iPlayer == iKushans:
			if pKushans.isAlive():
				
				# Kushan UHV1: Obtain 3 silk, incense or wine by 250
				#if sd.getGoal(iKushans, 0) == -1:
					#if iGameTurn <= getTurnForYear(250):
						#nBonuses = 0
						#nBonuses += pKushans.getNumAvailableBonuses(con.iSilk)
						#nBonuses += pKushans.getNumAvailableBonuses(con.iIncense)
						#nBonuses += pKushans.getNumAvailableBonuses(con.iWine)
						#if nBonuses >= 3:
							#sd.setGoal(iKushans, 0, 1)
					#else:
						#sd.setGoal(iKushans, 0, 0)
						
				# Kushan UHV1: build 5 Cloth Markets, Spice Markets or Artisan's Quarters in any combination by 200AD see onBuildingBuilt
				if iGameTurn == getTurnForYear(200):
					if sd.getGoal(iKushans, 0) == -1:
						sd.setGoal(iKushans, 0, 0)
				
				# Kushan UHV2: Best culture in 250
				if iGameTurn == getTurnForYear(250):
					if self.isTopCulture(iKushans):
						sd.setGoal(iKushans, 1, 1)
					else:
						sd.setGoal(iKushans, 1, 0)
						
				# Kushan UHV3: Largest empire in 300AD
				if (iGameTurn == getTurnForYear(300)):
					iKushanLand = pKushans.getTotalLand()
					bLargest = True
					for iCiv in range(0,iNumPlayers):
						if iCiv != iKushans:
							if (gc.getPlayer(iCiv).getTotalLand() > iKushanLand):
								bLargest = False

					if bLargest:
						sd.setGoal(iKushans, 2, 1)
					else:
						sd.setGoal(iKushans, 2, 0)
		
		elif iPlayer == iAxum:
			if pAxum.isAlive():
				
				# Axum UHV1: convert to a state religion by 200ad
				if iGameTurn == getTurnForYear(200):
					if sd.getGoal(iAxum, 0) == -1:
						sd.setGoal(iAxum, 0, 0)
						
				# Axum UHV2: be among the top 4 civs by score in 300AD
				if iGameTurn == getTurnForYear(300):
					for i in range(4):
						if gc.getGame().getRankTeam(i) == pAxum.getTeam():
							sd.setGoal(iAxum, 1, 1)
					if sd.getGoal(iAxum, 1) == -1:
						sd.setGoal(iAxum, 1, 0)
				
				# Axum UHV3: control provinces in 250AD
				#if iGameTurn == getTurnForYear(250):
					#bControl = true
					#regionList = [con.rAxum, con.rNubia, con.rArabiaFelix, con.rPunt]
					#for regionID in regionList:
						#if not utils.checkRegionOwnedCity(iAxum, regionID):
							#bControl = False
					#if bControl:
						#sd.setGoal(iAxum, 1, 1)
					#else:
						#sd.setGoal(iAxum, 1, 0)
				
				# Axum UHV3: acquire silk, pepper, cinnamon, incense, ivory, dye, cotton, salt, and wine before 300
				#if sd.getGoal(iAxum, 2) == -1:
					#if iGameTurn <= getTurnForYear(300):
						#bTrade = True
						#resourceList = [con.iSilk, con.iPepper, con.iCinnamon, con.iIncense, con.iIvory, con.iDye, con.iCotton, con.iSalt, con.iWine]
						#for i in range(len(resourceList)):
							#if not (pAxum.getNumAvailableBonuses(resourceList[i]) >=1):
								#bTrade = False
						#if bTrade:
							#sd.setGoal(iAxum, 2, 1)
					#else:
						#sd.setGoal(iAxum, 2, 0)
						
				# Axum UHV3: gold from trade
				if iGameTurn <= getTurnForYear(400):
					iTradeGold = 0
					
					# gold from city trade routes
					iTradeCommerce = 0
					cityList = PyPlayer(iAxum).getCityList()
					for pCity in cityList:
						city = pCity.GetCy()
						iTradeCommerce += city.getTradeYield(2)
					iTradeGold = iTradeCommerce * pAxum.getCommercePercent(0) / 100
					
					# gold from per turn gold trade
					for iCiv in range(con.iNumPlayers):
						iTradeGold += pAxum.getGoldPerTurnByPlayer(iCiv)
						
					sd.setAxumTradeGold(iTradeGold + sd.getAxumTradeGold())
					
					if self.getAxumTradeGold() >= 3000 * (gc.getGame().getGameSpeedType() + 2) / 2:
						sd.setGoal(iAxum, 2, 1)
						
					if iGameTurn >= getTurnForYear(400):
						if sd.getGoal(iAxum, 2) == -1:
							sd.setGoal(iAxum, 2, 0)
						
						
		
		elif iPlayer == iFunan:
			if pFunan.isAlive():
				
				# Funan UHV1: discover Crop Rotation and Monasticism by 300AD
				if iGameTurn == getTurnForYear(300):
					if sd.getGoal(iFunan, 0) == -1:
						sd.setGoal(iFunan, 0, 1)
					else:
						sd.setGoal(iFunan, 0, 0)
				
				# Funan UHV2: Build six Hindu or Buddhist buildings by 300AD see onBuildingBuilt
				if iGameTurn >= getTurnForYear(300):
					if sd.getGoal(iFunan, 1) == -1:
						sd.setGoal(iFunan, 1, 0)
						
				
				# Funan UHV3: cover your core province in your culture by 400AD
				if sd.getGoal(iFunan, 2) == -1:
					if iGameTurn <= getTurnForYear(400):
						if utils.checkRegionCultureCoverage(iFunan, con.rFunan):
							sd.setGoal(iFunan, 2, 1)
				else:
					sd.setGoal(iFunan, 2, 0)
						
				
				# Funan UHV3: 6,000 culture in 500AD
				#if iGameTurn == getTurnForYear(500):
					#if pFunan.countTotalCulture() >= 6000:
						#sd.setGoal(iFunan, 2, 1)
					#else:
						#sd.setGoal(iFunan, 2, 0)
		
		elif iPlayer == iSassanids:
			if pSassanids.isAlive():
				
				# Sassanid UHV1: Build 3 Zoroastrian Cathedrals by 600AD see onBuildingBuilt
				if iGameTurn == getTurnForYear(600):
					if sd.getGoal(iSassanids, 0) == -1:
						sd.setGoal(iSassanids, 0, 0)
				
				# Sassanid UHV2: control Darius' empire in 450AD
				if iGameTurn == getTurnForYear(450):
					bControl = true
					regionList = [con.rPersia, con.rMedia, con.rParthia, con.rArachosia, con.rMesopotamia, con.rSyria, con.rMargiana, con.rArmenia, con.rEgypt, con.rAsia, con.rJudea, con.rBactria, con.rSogdiana, con.rCappadocia, con.rPontus, con.rCaucasus, con.rGandhara]
					for regionID in regionList:
						if not utils.checkRegionOwnedCity(iSassanids, regionID):
							bControl = False
					if bControl:
						sd.setGoal(iSassanids, 1, 1)
					else:
						sd.setGoal(iSassanids, 1, 0)
				
				# Sassanid UHV3: Have a city with legendary culture
				if sd.getGoal(iSassanids, 2) == -1:
					if self.isHasLegendaryCity(iSassanids):
						sd.setGoal(iSassanids, 2, 1)
		
		elif iPlayer == iYamato:
			if pYamato.isAlive():
				
				# Yamato UHV1: control Yamato and Emishi in 300AD
				if iGameTurn == getTurnForYear(300):
					bControl = true
					regionList = [con.rYamato, con.rEmishi]
					for regionID in regionList:
						if not utils.checkRegionControl(iYamato, regionID):
							bControl = False
					if bControl:
						sd.setGoal(iYamato, 0, 1)
					else:
						sd.setGoal(iYamato, 0, 0)
				
				# Yamato UHV2: Gain control of at least 5 provinces before 450AD
				if sd.getGoal(iYamato, 1) == -1:
					if iGameTurn <= getTurnForYear(450):
						if pYamato.getNumCities() >= 5: # efficiency
							if self.getNumProvinces(iYamato) >= 5:
								sd.setGoal(iYamato, 1, 1)
					else:
						sd.setGoal(iYamato, 1, 0)
				
				# Yamato UHV3: discover Paper and Steel Working by 500AD
				if iGameTurn == getTurnForYear(500):
					if sd.getGoal(iYamato, 2) == -1:
						sd.setGoal(iYamato, 2, 0)
		
		elif iPlayer == iJin:
			if pJin.isAlive():
				
				# Jin UHV1: control china in 300AD
				if iGameTurn == getTurnForYear(300):
					bControl = true
					regionList = [con.rHan, con.rChu, con.rQi, con.rQin, con.rMinYue, con.rNanYue, con.rShu, con.rBa, con.rWu, con.rChu, con.rYan, con.rZhao]
					for regionID in regionList:
						if not utils.checkRegionControl(iJin, regionID):
							bControl = False
					if bControl:
						sd.setGoal(iJin, 0, 1)
					else:
						sd.setGoal(iJin, 0, 0)
				
				# Jin UHV2: 6 luxuries in 350AD
				if sd.getGoal(iJin, 1) == -1:
					if iGameTurn <= getTurnForYear(350):
						if self.getNumLuxuries(iJin) >= 6:
							sd.setGoal(iJin, 1, 1)
					else:
						sd.setGoal(iJin, 1, 0)
				
				# Jin UHV3: Be the first to discover The Stirrup, see onTechAcquired
		
		elif iPlayer == iGupta:
			if pGupta.isAlive():
				
				# Gupta UHV1: control provinces in 500AD
				if iGameTurn == getTurnForYear(500):
					bControl = true
					regionList = [con.rMagadha, con.rBangala, con.rAvanti, con.rKalinka, con.rDeccan, con.rKerala, con.rTamilNadu, con.rSaurashtra, con.rPunjab, con.rGandhara, con.rAndhra, con.rAndhra]
					for regionID in regionList:
						if not utils.checkRegionControl(iGupta, regionID, True):
							bControl = false
					if bControl:
						sd.setGoal(iGupta, 0, 1)
					else:
						sd.setGoal(iGupta, 0, 0)
				
				# Gupta UHV2: 3 golden ages by 510AD, expire check only, rest in onGoldenAge
				if iGameTurn == getTurnForYear(510):
					if sd.getGoal(iGupta, 1) == -1:
						sd.setGoal(iGupta, 1, 0)
				
				# Gupta UHV3: build Nalanda University and Dhamek Stupa see onBuildingBuilt
				
		elif iPlayer == iByzantines:
			if pByzantines.isAlive():
				
				# Byzantine UHV1: Justinian's empire by 540
				if sd.getGoal(iByzantines, 0) == -1:
					if iGameTurn <= getTurnForYear(540):
						bControl = True
						regionList = [con.rThrace, con.rGreece, con.rAsia, con.rSyria, con.rJudea, con.rEgypt, con.rLibya, con.rAfrica, con.rSicily, con.rSItaly, con.rCappadocia, con.rPontus, con.rNItaly, con.rIllyricum, con.rBaetica]
						for regionID in regionList:
							if not utils.checkRegionControl(iByzantines, regionID, True):
								bControl = False
								if not bControl:
									break
						if bControl:
							sd.setGoal(iByzantines, 0, 1)
					else:
						sd.setGoal(iByzantines, 0, 0)
						
						
				# Byzantine UHV2: no non-Catholic Chrisitian powers in 600AD
				if iGameTurn == getTurnForYear(600):
					iCatholic = 0
					for iLoopPlayer in range(iNumPlayers):
						pLoopPlayer = gc.getPlayer(iLoopPlayer)
						if pLoopPlayer.isAlive():
							if pLoopPlayer.getStateReligion() in [con.iArianism, con.iMonophysitism, con.iNestorianism]:
								sd.setGoal(iByzantines, 1, 0)
								return
							elif pLoopPlayer.getStateReligion() == con.iCatholicism:
								iCatholic += 1
					if iChristian >= 5:
						sd.setGoal(iByzantines, 1, 1)
					else:
						sd.setGoal(iByzantines, 1, 0)
						
				# Byzantine UHV3: Make Constaninople the largest and most cutured city in 700AD
				if iGameTurn == getTurnForYear(700):
					if self.isTopCityPopulation(iByzantines, con.tConstantinople) and self.isTopCityCulture(iByzantines, con.tConstantinople):
						sd.setGoal(iByzantines, 2, 1)
					else:
						sd.setGoal(iByzantines, 2, 0)
						
		elif iPlayer == iVisigoths:
			if pVisigoths.isAlive():
				
			
				# Visigoth UHV2 discover Jurisprudence by 650AD see onTechAcquired
				if iGameTurn == getTurnForYear(650) and sd.getGoal(iVisigoths, 1) == -1:
					sd.setGoal(iVisigoths, 0, 0)
			
				# Visigoth UHV2 control Spain, N Africa and Italy in 600AD
				if sd.getGoal(iVisigoths, 0) == -1:
					if iGameTurn <= getTurnForYear(600):
						bControl = True
						regionList = [con.rIberia, rBaetica, rLusitania, rSeptimania, rNItaly, rSItaly, rAfrica, rNumidia]
						for regionID in regionList:
							if not checkRegionControl(iVisigoths, regionID):
								bControl = False
							if bControl:
								sd.setGoal(iVisigoths, 1, 1)
					else:
						sd.setGoal(iVisigoths, 1, 0)
				
				# Visigoth UHV3 have at least 5,000 culture and be Stable in 650AD
				if iGameTurn == getTurnForYear(650):
					if pVisigoths.countTotalCulture > 5000 and gc.getTeam(pVisigoths.getTeam()).isHasTech(iStabilityStable):
						sd.setGoal(iVisigoths, 2, 1)
					else:
						sd.setGoal(iVisigoths, 2, 0)
							
		elif iPlayer == iVandals:
			if pVandals.isAlive():
				
				# Vandal UHV1: capture Rome before 455AD see onCityAcquired
				if sd.getGoal(iVandals, 0) == -1:
					if iGameTurn == getTurnForYear(455):
						sd.setGoal(iVandals, 0, 0)
			
				# Vandal UHV2 control 9 ports in 550AD
				if iGameTurn == getTurnForYear(550):
					PortList = []
					apCityList = PyPlayer(iVandals).getCityList()
					for pCity in apCityList:
						if pCity.GetCy().isCoastal(gc.getMIN_WATER_SIZE_FOR_OCEAN()):
							PortList.append(pCity)
					if len (PortList) >= 9:
						sd.setGoal(iVandals, 1, 1)
					else:
						sd.setGoal(iVandals, 1, 0)
			
				# Vandal UHV3 have 15,000 gold by 600AD
				if sd.getGoal(iVandals, 2) == -1:
					if iGameTurn <= getTurnForYear(600):
						if pVandals.getGold() >= 15000:
							sd.setGoal(iVandals, 2, 1)
					else:
						sd.setGoal(iVandals, 2, 0)
			
				return
				
		elif iPlayer == iOstrogoths:
			if pOstrogoths.isAlive():
			
				# Ostrogoth UHV1 build a palace and a royal mausoleum see onBuildingBuilt
				if iGameTurn == getTurnForYear(520) and sd.getGoal(iOstrogoths, 0) == -1:
					sd.setGoal(iOstrogoths, 0, 0)
			
				# Ostrogoth UHV3 control Dacia, Illyricum, Sicily and Italy in 600AD
				if sd.getGoal(iOstrogoths, 0) == -1:
					if iGameTurn == getTurnForYear(600):
						bControl = True
						regionList = [con.rDacia, rIllyricum, rNItaly, rSItaly, rSicily]
						for regionID in regionList:
							if not checkRegionControl(iOstrogoths, regionID):
								bControl = False
							if bControl:
								sd.setGoal(iOstrogoths, 1, 1)
							else:
								sd.setGoal(iOstrogoths, 1, 0)
			
				# Ostrogoth UHV2 have friendly relations with 3 christian civs without changing your state religion by 650AD
				if sd.getGoal(iOstrogoths, 2) == -1:
					if iGameTurn <= getTurnForYear(650):
						iNumFriends = 0
						for iLoopCiv in range(iNumPlayers):
							if gc.getPlayer(iLoopCiv).AI_getAttitude(iOstrogoths)  >= 4 and gc.getPlayer(iLoopCiv).getStateReligion() in [con.iChristianity, con.iArianism, con.iCatholicism, con.iMonophysitism, con.iNestorianism]:
								iNumFriends += 1
						if iNumFriends >= 4:
							sd.setGoal(iOstrogoths, 2, 1)
					else:
						sd.setGoal(iOstrogoths, 2, 0)
		
		elif iPlayer == iFranks:
			if pFranks.isAlive():
				
				# Frankish UHV1: Charlemagne's empire in 700AD
				if iGameTurn == getTurnForYear(700):
					bControl = true
					regionList = [con.rGaul, con.rAquitania, con.rSeptimania, con.rGermania, con.rNItaly]
					for regionID in regionList:
						if not utils.checkRegionControl(iFranks, regionID):
							bControl = false
					if bControl:
						sd.setGoal(iFranks, 0, 1)
					else:
						sd.setGoal(iFranks, 0, 0)
				
				# Frankish UHV2: build 7 Catholic Monasteries by and 1 Catholic Cathedral by 750AD
				if sd.getGoal(iFranks, 1) == -1:
					if iGameTurn <= getTurnForYear(750):
						iNumCathedrals = self.getNumBuildings(iFranks, con.iCatholicCathedral)
						iNumMonasteries = self.getNumBuildings(iFranks, con.iCatholicMonastery)
						if iNumCathedrals >= 1 and iNumMonasteries >= 7:
							sd.setGoal(iFranks, 1, 1)
					else:
						sd.setGoal(iFranks, 1, 0)
				
				# Frankish UHV3: do not allow Islam in Europe in 800AD
				if iGameTurn == getTurnForYear(800):
					bSuccess = self.isFreeOfIslam([con.rGaul, con.rAquitania, con.rSeptimania, con.rGermania, con.rNItaly, con.rSItaly, con.rIberia, con.rSicily, con.rIllyricum, con.rGreece, con.rBaetica, con.rLusitania])
					if bSuccess:
						sd.setGoal(iFranks, 2, 1)
					else:
						sd.setGoal(iFranks, 2, 0)
		
		elif iPlayer == iChalukyans:
			if pChalukyans.isAlive():
				
				# Chalukyan UHV1: Best culture in 700AD
				if iGameTurn == getTurnForYear(700):
					if self.isTopCulture(iChalukyans):
						sd.setGoal(iChalukyans, 0, 1)
					else:
						sd.setGoal(iChalukyans, 0, 0)
				
				# Chalukyan UHV2: build 3 cathedrals of Indian religons by 700AD
				if sd.getGoal(iChalukyans, 1) == -1:
					if iGameTurn <= getTurnForYear(700):
						iNumCathedrals = (self.getNumBuildings(iChalukyans, con.iHinduCathedral)) + (self.getNumBuildings(iChalukyans, con.iBuddhistCathedral)) +(self.getNumBuildings(iChalukyans, con.iJainCathedral))
						if iNumCathedrals >= 3:
							sd.setGoal(iChalukyans, 1, 1)
					else:
						sd.setGoal(iChalukyans, 1, 0)
				
				# Chalukyan UHV3: make Vatapi the most cultured city in the world in 800AD
				if iGameTurn == getTurnForYear(800):
					if self.isTopCityCulture(iChalukyans, con.tVatapi):
						sd.setGoal(iChalukyans, 2, 1)
					else:
						sd.setGoal(iChalukyans, 2, 0)
						
		elif iPlayer == iLombards:
			if pLombards.isAlive():
				
			
				# Lombard UHV3 settle a Great Prophet in Rome by 700AD
				if sd.getGoal(iLombards, 0) == -1:
					if iGameTurn <= getTurnForYear(700):
						plot = gc.getMap().plot(con.tRome[0], con.tRome[1])
						if plot.isCity():
							city = plot.getPlotCity()
							iGreatPriest = gc.getInfoTypeForString("SPECIALIST_GREAT_PRIEST")
							if city.getFreeSpecialistCount(iGreatPriest) >= 1:
								sd.setGoal(iLombards, 0, 1)
					else:
						sd.setGoal(iLombards, 0, 0)
			
				# Lombard UHV2 celebrate "we love the king day" in a city by 750AD
				if sd.getGoal(iLombards, 1) == -1:
					if iGameTurn <= getTurnForYear(750):
						cityList = PyPlayer(iLombards).getCityList()
						for pCity in cityList:
							if pCity.GetCy().isWeLoveTheKingDay():
								sd.setGoal(iLombards, 1, 1)
								break
					else:
						sd.setGoal(iLombards, 1, 0)
			
				# Lombard UHV1 build the National Epic by 790AD see onBuildingBuilt
				if iGameTurn >= getTurnForYear(790) and sd.getGoal(iLombards, 2) == -1:
					sd.setGoal(iLombards, 2, 0)
						
						
		elif iPlayer == iGokturks:
			if pGokturks.isAlive():
				
				# Gokturk UHV1: largest empire in 650
				if (iGameTurn == getTurnForYear(650)):
					iGokturksLand = pGokturks.getTotalLand()
					bLargest = True
					for iCiv in range(0,iNumPlayers):
						if (gc.getPlayer(iCiv).getTotalLand() > iGokturksLand):
							bLargest = False
					if bLargest:
						sd.setGoal(iGokturks, 0, 1)
					else:
						sd.setGoal(iGokturks, 0, 0)
			
				# Gokturk UHV2: 6% land by 750AD
				if sd.getGoal(iGokturks, 0) == -1:
					if iGameTurn <= getTurnForYear(750):
						totalLand = gc.getMap().getLandPlots()
						ownedLand = pGokturks.getTotalLand()
						if totalLand > 0:
							landPercent = (ownedLand * 100.0) / totalLand
						else:
							landPercent = 0.0
						if landPercent >= 5.995:
							sd.setGoal(iGokturks, 1, 1)
					else:
						sd.setGoal(iGokturks, 1, 0)
				
				# Gokturk UHV3: do not lose a city before 750AD see onCityAcquired
		
		elif iPlayer == iSrivajaya:
			if pSrivajaya.isAlive():
				
				# Srivajayan UHV1: control 7 cities in 700AD
				if iGameTurn == getTurnForYear(700):
					if pSrivajaya.getNumCities() >= 7:
						sd.setGoal(iSrivajaya, 0, 1)
					else:
						sd.setGoal(iSrivajaya, 0, 0)
				
				# Srivajayan UHV2: 11 luxuries by 840AD
				if sd.getGoal(iSrivajaya, 1) == -1:
					if iGameTurn <= getTurnForYear(840):
						if self.getNumLuxuries(iSrivajaya) >= 11:
							sd.setGoal(iSrivajaya, 1, 1)
					else:
						sd.setGoal(iSrivajaya, 1, 0)
					
				
				# Srivajayan UHV3: world'd highest population in 800
				if iGameTurn == getTurnForYear(800):
					if self.isHighestPopulation(iSrivajaya):
						sd.setGoal(iSrivajaya, 2, 1)
					else:
						sd.setGoal(iSrivajaya, 2, 0)
						
		elif iPlayer == iKhazars:
			if pKhazars.isAlive():
				
				# Khazar UHV1: Gain control of at least 7 provinces before 750AD
				if sd.getGoal(iKhazars, 0) == -1:
					if iGameTurn <= getTurnForYear(750):
						if pKhazars.getNumCities() >= 7: # efficiency
							if self.getNumProvinces(iKhazars) >= 7:
								sd.setGoal(iKhazars, 0, 1)
					else:
						sd.setGoal(iKhazars, 0, 0)
				
				# Khazar UHV2: Judaism in every city in 750AD
				if iGameTurn == getTurnForYear(750):
					cityList = PyPlayer(iKhazars).getCityList()
					bSuccess = True
					for pCity in cityList:
						if not pCity.GetCy().isHasReligion(con.iJudaism):
							bSuccess = False
					if bSuccess:
						sd.setGoal(iKhazars, 1, 1)
					else:
						sd.setGoal(iKhazars, 1, 0)
				
				# Khazar UHV3: open borders x 6 in 800AD
				if sd.getGoal(iKhazars, 2) == -1:
					if iGameTurn <= getTurnForYear(800):
						if self.getNumOpenBorders(iKhazars) >= 6:
							sd.setGoal(iKhazars, 2, 1)
					else:
						sd.setGoal(iKhazars, 2, 0)
						
		elif iPlayer == iTibet:
			if pTibet.isAlive():
				
				# Tibetan UHV1: Control or vassalize provinces in 750AD
				if iGameTurn == getTurnForYear(750):
					if sd.getGoal(iTibet, 0) == -1:
						bControl = True
						regionList = [con.rTibet, con.rNanzhao, con.rBirma, con.rTarim, con.rQinghai]
						for regionID in regionList:
							if not utils.checkRegionControl(iTibet, regionID, True):
								bControl = False
						if bControl:
							sd.setGoal(iTibet, 0, 1)
						else:
							sd.setGoal(iTibet, 0, 0)
				
				# Tibetan UHV2: Build at least 1 Buddhist wonder by 800AD see onBuildingBuilt
				if sd.getGoal(iTibet, 1) == -1:
					if iGameTurn >= getTurnForYear(800):
						sd.setGoal(iTibet, 1, 0)
						
				# Tibetan UHV3: Ensure that all east Asian civs are Buddhist in 800AD
				if iGameTurn == getTurnForYear(800):
					bSuccess = True
					for iLoopPlayer in [iGoguryeo, iYamato, iTang, iHan, iVietnam, iFunan, iQin]:
						if gc.getPlayer(iLoopPlayer).isAlive() and gc.getPlayer(iLoopPlayer).getStateReligion() != con.iBuddhism:
							bSuccess = False
							break
					if bSuccess:
						sd.setGoal(iTibet, 2, 1)
					else:
						sd.setGoal(iTibet, 2, 0)
		
		elif iPlayer == iTang:
			if pTang.isAlive():
				
				# Tang UHV1: Control provinces in 800
				if iGameTurn == getTurnForYear(800):
					bControl = True
					regionList = [con.rQin, con.rHan, con.rShu, con.rChu, con.rQi, con.rZhao, con.rYan, con.rBuyeo, con.rGoguryeo, con.rNanYue, con.rMinYue, con.rAnnam, con.rGansu, con.rTarim, con.rBa]
					for regionID in regionList:
						if not utils.checkRegionControl(iTang, regionID, True):
							bControl = False
					if bControl:
						sd.setGoal(iTang, 0, 1)
					else:
						sd.setGoal(iTang, 0, 0)
				
				# Tang UHV2: Have at least 2 vassals in 840AD
				if iGameTurn == getTurnForYear(840):
					if self.getNumVassals(iTang) >= 1:
						sd.setGoal(iTang, 1, 1)
					else:
						sd.setGoal(iTang, 1, 0)
						
				# Tang UHV3: first to discover Printing Press and Gunpowder see onTechAcquired
		
		elif iPlayer == iArabs:
			if pArabs.isAlive():
				
				# Arabs UHV3: Control provinces in 750
				if iGameTurn == getTurnForYear(750):
					bControl = True
					regionList = [con.rArabia, con.rJudea, con.rSyria, con.rMesopotamia, con.rMedia, con.rPersia, con.rEgypt, con.rLibya, con.rAfrica, con.rArachosia, con.rMargiana, con.rBactria, con.rNumidia, con.rMauretania, con.rSicily, con.rBaetica, con.rIberia]
					for regionID in regionList:
						if not utils.checkRegionControl(iArabs, regionID):
							bControl = False
					if bControl:
						sd.setGoal(iArabs, 0, 1)
					else:
						sd.setGoal(iArabs, 0, 0)
				
				# Arab UHV2: best tech in 800AD
				if sd.getGoal(iArabs, 1) == -1:
					if iGameTurn <= getTurnForYear(800):
						if self.isTopTech(iArabs):
							sd.setGoal(iArabs, 1, 1)
					else:
						sd.setGoal(iArabs, 1, 0)
				
				# Arab UHV3: Spread Islam to 30% by 850AD
				if sd.getGoal(iArabs, 2) == -1:
					if iGameTurn <= getTurnForYear(850):
						religionPercent = gc.getGame().calculateReligionPercent(con.iIslam)
						if religionPercent >= 30.0:
							sd.setGoal(iArabs, 2, 1)
					else:
						sd.setGoal(iArabs, 2, 0)
		
		#generic checks
		pPlayer = gc.getPlayer(iPlayer)
		if pPlayer.isAlive() and iPlayer < iNumPlayers -3:
			
			if sd.get2OutOf3(iPlayer) == False:
				if utils.countAchievedGoals(iPlayer) == 2:
					#intermediate bonus
					sd.set2OutOf3(iPlayer, True)
					if pPlayer.getNumCities() > 0: #this check is needed, otherwise game crashes
						pPlayer.changeGoldenAgeTurns(pPlayer.getGoldenAgeLength()) # edead
						iWarCounter = 0
						iRndnum = gc.getGame().getSorenRandNum(iNumPlayers, 'civs')
						iHandicap = gc.getGame().getHandicapType()
						for i in range(iRndnum, iNumPlayers + iRndnum):
							iCiv = i % iNumPlayers
							pCiv = gc.getPlayer(iCiv)
							if pCiv.isAlive() and pCiv.canContact(iPlayer):                                                                
								if pCiv.AI_getAttitude(iPlayer) <= 0:
									teamCiv = gc.getTeam(pCiv.getTeam())
									if not teamCiv.isAtWar(iPlayer) and not teamCiv.isDefensivePact(iPlayer) and not utils.isAVassal(iCiv):
										#teamCiv.declareWar(iPlayer, True, -1)
										teamCiv.AI_setWarPlan(iPlayer, WarPlanTypes.WARPLAN_PREPARING_TOTAL) # edead: prepare for total war
										iWarCounter += 1
										if iWarCounter == 1 + max(1, iHandicap):
											break
			
			if gc.getGame().getWinner() == -1:
				if sd.getGoal(iPlayer, 0) == 1 and sd.getGoal(iPlayer, 1) == 1 and sd.getGoal(iPlayer, 2) == 1:
					gc.getGame().setWinner(iPlayer, iHistoricalVictory)
					
	
	def onReligionSpread (self):
	
	
		if sd.getGoal(iMaccabees, 2) == -1:
			self.maccabeanCheck()
			
		'''if iMauryans == utils.getHumanID() and sd.getGoal(iMauryans, 2) == -1:
			cityList = []
			bSuccess = True
			for iPlayer in range(iNumTotalPlayers):
				for pyCity in PyPlayer(iPlayer).getCityList():
					pCurrent = gc.getMap().plot(pyCity.getX(), pyCity.getY())
					if pCurrent.getRegionID() in lIndianRegions:
						if not pyCity.GetCy().isHasReligion(con.iBuddhism):
							bSuccess = False
							break
			if bSuccess:
				sd.setGoal(iMauryans, 2, 1)'''
				
	def onCorporationSpread(self, iCorporation, iOwner, pSpreadCity):
	
		if iCorporation == con.iIncenseMerchants:
			iMediterraneanCities = 0
			iPersianCities = 0
			iIndianCities = 0
			iEasternCities = 0
			for iPlayer in range(iNumTotalPlayers):
				apCityList = PyPlayer(iPlayer).getCityList()
				for pCity in apCityList:
					if pCity.GetCy().isHasCorporation(con.iIncenseMerchants) and pCity.getOwner() != con.iSaba:
						pCurrent = gc.getMap().plot(pCity.getX(), pCity.getY())
						if pCurrent.getRegionID() == con.rSyria:
							if pCity.GetCy().isCoastal(gc.getMIN_WATER_SIZE_FOR_OCEAN()):
								iMediterraneanCities += 1
							else:
								iPersianCities += 1
						elif pCurrent.getRegionID() in con.lMediterraneanRegions:
							iMediterraneanCities += 1
						elif pCurrent.getRegionID() in con.lPersianRegions:
							iPersianCities += 1
						elif pCurrent.getRegionID() in con.lGreaterIndianRegions or pCurrent.getRegionID() in con.lCentralAsianRegions:
							iIndianCities += 1
						elif pCurrent.getRegionID() in con.lGreaterChineseRegions or pCurrent.getRegionID() in con.lSouthEastAsianRegions:
							iEasternCities += 1
							
			if iMediterraneanCities >= 5 and iPersianCities >= 5 and iIndianCities >= 5 and iEasternCities >= 5:
				sd.setGoal(iSaba, 2, 1)
	
	def maccabeanCheck (self):
		if pMaccabees.isAlive():
			iNumAliveCivs = 0
			iNumAliveCivsWithJudaism = 0
			for iLoopCiv in range(iNumPlayers):
				if gc.getPlayer(iLoopCiv).isAlive():
					iNumAliveCivs += 1
				cityList = PyPlayer(iLoopCiv).getCityList()
				for pCity in cityList:
					if pCity.GetCy().isHasReligion(con.iJudaism):
						iNumAliveCivsWithJudaism += 1
						break
			iNumTotalCities = 0
			iNumCitiesWithJudaism = 0
			for iLoopCiv in range(iNumTotalPlayers):
				iNumTotalCities += gc.getPlayer(iLoopCiv).getNumCities()
				cityList = PyPlayer(iLoopCiv).getCityList()
				for pCity in cityList:
					if pCity.GetCy().isHasReligion(con.iJudaism):
						iNumCitiesWithJudaism += 1
			if (iNumAliveCivsWithJudaism * 2 > iNumAliveCivs) and (iNumCitiesWithJudaism * 3 > iNumTotalCities):
				sd.setGoal(iMaccabees, 2, 1)
	
	def getTopPopulationRegion(self):
		"""Returns the ID of the most populous region (province)."""
		data = {}
		for iProvince in range(con.iNumRegions):
			data[iProvince] = 0
		for iLoopPlayer in range(con.iBarbarian + 1):
			apCityList = PyPlayer(iLoopPlayer).getCityList()
			for pCity in apCityList:
				data[pCity.GetCy().plot().getRegionID()] += pCity.getPopulation()
		key = -1
		for key, value in sorted(data.iteritems(), key=lambda (k,v): (v,k)):
			pass
		return key
	
	def onGoldenAge(self, iPlayer):
		
		if not gc.getGame().isVictoryValid(iHistoricalVictory):
			return
		
		# Gupta UHV
		if iPlayer == iGupta:
			sd.setGuptaGoldenAges(sd.getGuptaGoldenAges() + 1)
			if sd.getGuptaGoldenAges() == 3:
				sd.setGoal(iGupta, 1, 1)


	def onCityAcquired(self, argsList):
		iPreviousOwner, iNewOwner, city, bConquest, bTrade = argsList
		#print "onCityAcquired"
		if not gc.getGame().isVictoryValid(iHistoricalVictory):
			return
		
		iYear = utils.getYear()
		
		if sd.getGoal(iMaccabees, 2) == -1:
			self.maccabeanCheck()
							
		# Gojoseon UHV3: Never lose a city before 50BC
		if iPreviousOwner == iGojoseon:
			if pGojoseon.isAlive():
				if bConquest:
					if sd.getGoal(iGojoseon, 2) == -1:
						if iYear < -50:
							sd.setGoal(iGojoseon, 2, 0)
							
		# Armenian UHV3: Never lose a city before 100AD
		if iPreviousOwner == iArmenia:
			if pArmenia.isAlive():
				if bConquest:
					if sd.getGoal(iArmenia, 2) == -1:
						if iYear < 100:
							sd.setGoal(iArmenia, 2, 0)
							
		# Gokturk UHV3: Never lose a city before 750AD
		if iPreviousOwner == iGokturks:
			if pGokturks.isAlive():
				if bConquest:
					if sd.getGoal(iGokturks, 2) == -1:
						if iYear < 750:
							sd.setGoal(iGokturks, 2, 0)
							
		# Celtic UHV1: capture Rome before 150BC
		elif (city.getX(), city.getY()) == con.tRome:
			if iYear <= -150:
				if iNewOwner == iCelts:
					if sd.getGoal(iCelts, 0) == -1:
						sd.setGoal(iCelts, 0, 1)
							
		# Vandal UHV1: capture Rome before 455AD
		elif (city.getX(), city.getY()) == con.tRome:
			if iYear <= 455:
				if iNewOwner == iVandals:
					if sd.getGoal(iVandals, 0) == -1:
						sd.setGoal(iVandals, 0, 1)
						
		# Maccabean UHV#: capture 4 cities with Jewish populations before 50AD, and hold them in 50AD
		if iNewOwner == iMaccabees and city.isHasReligion(con.iJudaism):
			sd.setWondersBuilt(iMaccabees, sd.getWondersBuilt(iMaccabees) + 1)
		elif iPreviousOwner == iMaccabees and city.isHasReligion(con.iJudaism):
			if sd.getWondersBuilt(iMaccabees) != 0:
				sd.setWondersBuilt(iMaccabees, sd.getWondersBuilt(iMaccabees) -1)
				
		# Pontic UHV2 capture 4 Roman cities
		if iNewOwner == iPontus and iPreviousOwner in [iRome, iByzantines] and sd.getGoal(iPontus, 1) == -1:
			sd.setWondersBuilt(iPontus, sd.getWondersBuilt(iPontus) +1)
			if sd.getWondersBuilt(iPontus) >= 4:
				sd.setGoal(iPontus, 1, 1)
		
		# Gojoseon UHV2 capture 3 Chinese cities
		if iNewOwner == iGojoseon and sd.getGoal(iGojoseon, 0) == -1:
			if iPreviousOwner in [iQin, iHan, iNanYue]:
				sd.setWondersBuilt(iGojoseon, sd.getWondersBuilt(iGojoseon) +1)
				if sd.getWondersBuilt(iGojoseon) >= 3 and sd.getNumGojoseonKills() >= 20:
					sd.setGoal(iGojoseon, 0, 1)
			if con.iIndependent <= iPreviousOwner <= con.iIndependent3:
				regionList = [con.rYan, con.rZhao, con.rWei, con.rQin, con.rQi, con.rChu, con.rBa, con.rShu, con.rMinYue, con.rNanYue]
				if gc.getMap().plot(city.getX(), city.getY()).getRegionID() in regionList: 
					sd.setWondersBuilt(iGojoseon, sd.getWondersBuilt(iGojoseon) + 1)
					if sd.getWondersBuilt(iGojoseon) >= 3 and sd.getNumGojoseonKills() >= 20:
						sd.setGoal(iGojoseon, 0, 1)
						
		



	def onCityAcquiredAndKept(self, argsList):
		iOwner,pCity,bMassacre = argsList
		
		if not gc.getGame().isVictoryValid(iHistoricalVictory):
			return
		



	def onCityRazed(self, iPlayer):
		
		if sd.getGoal(iMaccabees, 2) == -1:
			self.maccabeanCheck()
		



	def onTechAcquired(self, iTech, iPlayer):
		
		if not gc.getGame().isVictoryValid(iHistoricalVictory):
			return
			
		if not iPlayer == utils.getHumanID():
			return
			
		# Visigoth UHV2: discover Jurisprudence by 600AD
		if iPlayer == iVisigoths:
			if iTech == con.iJurisprudence and sd.getGoal(iVisigoths, 1) == -1:
				sd.setGoal(iVisigoths, 0, 1)
					
		# Gojoseon UHV2: Be the first to discover Marksmanship
		if iPlayer == iGojoseon:
			if iTech == con.iMarksmanship and sd.getGoal(iGojoseon, 1) == -1:
				if iPlayer == iGojoseon:
					sd.setGoal(iGojoseon, 1, 1)
				else:
					sd.setGoal(iGojoseon, 1, 0)
			
		
					
		# Antigonid UHV1: Be the first to discover Monarchy
		if iPlayer == iAntigonids:
			if iTech == con.iMonarchy and sd.getGoal(iAntigonids, 0) == -1:
				if iPlayer == iAntigonids:
					sd.setGoal(iAntigonids, 0, 1)
				else:
					sd.setGoal(iAntigonids, 0, 0)
					
									
		# Pandyan UHV3: Be the first to discover Steel Working
		if iPlayer == iPandyans:
			if sd.getGoal(iPandyans, 2) == -1:
				if iTech == con.iSteelWorking:
					if iPlayer == iPandyans and sd.getGoal(iPandyans, 2) == -1: 
						sd.setGoal(iPandyans, 2, 1)
					else:
						sd.setGoal(iPandyans, 2, 0)
						
		# Qin/Jin UHV3: Be the first to discover the Stirrup
		if iPlayer == iQin and sd.get3KingdomsMarker() == 1:
			if sd.getGoal(iQin, 2) == -1 and iTech == con.iTheStirrup:
				if iPlayer == iQin:
					sd.setGoal(iQin, 2, 1)
				else:
					sd.setGoal(iQin, 2, 0)
					

		
		# Han UHV3: Be the first to discover Paper with Jin goal
		if iPlayer == iHan:
			if sd.get3KingdomsMarker() == 2:
				if sd.getGoal(iHan, 2) == -1 and iTech == con.iTheStirrup:
					if iPlayer == iHan:
						sd.setGoal(iHan, 2, 1)
					else:
						sd.setGoal(iHan, 2, 0)
			else:
				if iTech == con.iPaper and sd.getGoal(iHan, 1) == -1:
					if iPlayer == iHan:
						sd.setGoal(iHan, 1, 1)
					else:
						sd.setGoal(iHan, 1, 0)
									
									
		# Jin UHV3: Be the first to discover the Stirrup
		if iPlayer == iJin:
			if sd.getGoal(iJin, 2) == -1 and iTech == con.iTheStirrup:
				if iPlayer == iJin:
					sd.setGoal(iJin, 2, 1)
				else:
					sd.setGoal(iJin, 2, 0)
									
		# Roman Republc UHV2: Be the first to discover Engineering & Jurisprudence
		if not gc.getTeam(pRome.getTeam()).isHasTech(con.iRomanEmpire):
			if pRome.isAlive():
				if sd.getGoal(iRome, 1) == -1:
					if iTech == con.iEngineering:
						if iPlayer != iRome and sd.getRomanTechs(0) == -1: 
							sd.setGoal(iRome, 1, 0)
						else:
							sd.setRomanTechs(0, 1)
					elif iTech == con.iJurisprudence: 
						if iPlayer != iRome and sd.getRomanTechs(1) == -1: 
							sd.setGoal(iRome, 1, 0)
						else:
							sd.setRomanTechs(1, 1)
					if sd.getRomanTechs(0) ==	1 and sd.getRomanTechs(1) == 1:
						sd.setGoal(iRome, 1, 1)
						
		# Tang UHV3: Be the first to discover Printing Press & Gunpowder
		if pTang.isAlive():
			if sd.getGoal(iTang, 2) == -1:
				if iTech == con.iPrintingPress:
					if iPlayer != iTang and sd.getTangTechs(0) == -1: 
						sd.setGoal(iTang, 2, 0)
					else:
						sd.setTangTechs(0, 1)
				elif iTech == con.iAlchemy: 
					if iPlayer != iTang and sd.getTangTechs(1) == -1: 
						sd.setGoal(iTang, 2, 0)
					else:
						sd.setTangTechs(1, 1)
				if sd.getTangTechs(0) == 1 and sd.getTangTechs(1) == 1:
					sd.setGoal(iTang, 2, 1)
						
		# Nubian UHV1: Discover Iron Working & Alphabet by 150BC
		if iPlayer == iNubia:
			if pNubia.isAlive():
				if sd.getGoal(iNubia, 0) == -1:
					if iTech == con.iIronWorking:
						sd.setNubianTechs(0, 1)
					elif iTech == con.iAlphabet:
						sd.setNubianTechs(1, 1)
					if sd.getNubianTechs(0) == 1 and sd.getNubianTechs(1) == 1 :
						sd.setGoal(iNubia, 0, 1)
				
						
						
		# Yamato UHV1: discover Paper and Steel Working by 500AD				
		if iPlayer == iYamato:
			if pYamato.isAlive():
				if sd.getGoal(iYamato, 2) == -1:
					if iTech == con.iPaper:
						sd.setYamatoTechs(0, 1)
					elif iTech == con.iSteelWorking:
						sd.setYamatoTechs(1, 1)
					if sd.getYamatoTechs(0) == 1 and sd.getYamatoTechs(1) == 1 :
						sd.setGoal(iYamato, 2, 1)

		# Funan UHV1: discover Crop Rotation and Monasticism by 400AD				
		if iPlayer == iFunan:
			if pFunan.isAlive():
				if sd.getGoal(iFunan, 0) == -1:
					if iTech == con.iCropRotation:
						sd.setFunanTechs(0, 1)
					elif iTech == con.iMonasticism:
						sd.setFunanTechs(1, 1)
					if sd.getFunanTechs(0) == 1 and sd.getFunanTechs(1) == 1 :
						sd.setGoal(iFunan, 0, 1)

	def onBuildingBuilt(self, iPlayer, iBuilding, city):
		
		if not gc.getGame().isVictoryValid(iHistoricalVictory):
			return
		
		iGameTurn = gc.getGame().getGameTurn()
		
		# Pandyan UHV2: 2 cloth markets and 2 spice markets
		if iPlayer == iPandyans and sd.getGoal(iPandyans, 1) == -1:
			if sd.get3KingdomsMarker() == 4:
				if iBuilding in [con.iClothMarket, con.iSpiceMarket]:
					if self.getNumBuildings(iPandyans, con.iClothMarket) >= 2 and self.getNumBuildings(iPandyans, con.iSpiceMarket) >= 2:
						sd.setGoal(iPandyans, 1, 1)
		
		# Chola UHV2: national epic and Grand Anicut
		if iPlayer == iPandyans and sd.getGoal(iPandyans, 1) == -1:
			if sd.get3KingdomsMarker() == 3:
				#if iBuilding in [con.iNationalEpic, con.iGrandAnicut]:
				if iBuilding in [con.iNationalEpic, con.iKhajuraho]: # dummy wnder for now to avoid breaking saves
					sd.setWondersBuilt(iPandyans, sd.getWondersBuilt(iPandyans) + 1)
				if sd.getWondersBuilt(iPandyans) == 2:
					sd.setGoal(iPandyans, 1, 1)
		
		# Kushan UHV1: 5 trade buildings
		if iPlayer == iKushans and sd.getGoal(iKushans, 0) == -1:
			if iBuilding in [con.iClothMarket, con.iSpiceMarket, con.iArtisansQuarter]:
				sd.setWondersBuilt(iKushans, sd.getWondersBuilt(iKushans) + 1)
			if sd.getWondersBuilt(iKushans) == 5:
				sd.setGoal(iKushans, 0, 1)
		
		# Vietnamese UHV3: 12 Buddhist buildings
		if iPlayer == iVietnam and sd.getGoal(iVietnam, 2) == -1:
			if iBuilding in [con.iBuddhistTemple, con.iBuddhistMonastery, con.iBuddhistCathedral, con.iBuddhistShrine, con.iBuddhistReliquary, con.iDhamekStupa, con.iBamyanBuddha, con.iBorobudur, con.iShwedagonPaya]:
				sd.setWondersBuilt(iVietnam, sd.getWondersBuilt(iVietnam) + 1)
			if sd.getWondersBuilt(iVietnam) == 12:
				sd.setGoal(iVietnam, 2, 1)
		
		# Kalinkan UHV3: 7 Jain buildings
		if iPlayer == iKalinka and sd.getGoal(iKalinka, 2) == -1:
			if iBuilding in [con.iJainTemple, con.iJainMonastery, con.iJainCathedral, con.iJainShrine, con.iJainReliquary, con.iKalinkaJainLibrary]:
				sd.setWondersBuilt(iKalinka, sd.getWondersBuilt(iKalinka) + 1)
			if sd.getWondersBuilt(iKalinka) == 7:
				sd.setGoal(iKalinka, 2, 1)
		
		# Maccabees UHV2: build the Temple of Solomon by 75BC
		if iBuilding == con.iJewishShrine:
			if iPlayer == iMaccabees and pMaccabees.isAlive() and sd.getGoal(iMaccabees, 1) == -1:
				sd.setGoal(iMaccabees, 1, 1)
		
		# Egyptian UHV1: Build the Great Library and the Great Lighthouse by 180BC
		if iBuilding == con.iGreatLibrary or iBuilding == con.iGreatLighthouse:
			if iPlayer == iEgypt and pEgypt.isAlive() and sd.getGoal(iEgypt, 0) == -1:
				sd.setWondersBuilt(iEgypt, sd.getWondersBuilt(iEgypt) + 1)
				if sd.getWondersBuilt(iEgypt) == 2:
					sd.setGoal(iEgypt, 0, 1)
			else:
				sd.setGoal(iEgypt, 0, 0)
				
		# Sassanid UHV1: Build 3 Zoroastrian Cathedrals by 600AD
		if iBuilding == con.iZoroastrianCathedral:
			if iPlayer == iSassanids:
				if pSassanids.isAlive():
					if sd.getGoal(iSassanids, 0) == -1:
						sd.setWondersBuilt(iSassanids, sd.getWondersBuilt(iSassanids) + 1)
						if sd.getWondersBuilt(iSassanids) >= 3:
							sd.setGoal(iSassanids, 0, 1)

		# Mauryan UHV1: Build 10 Mauryan Edicts by 100BC
		if iBuilding == con.iMauryanEdict:
			if iPlayer == iMauryans and sd.getCivilization(iMauryans) == iMauryans:
				if pMauryans.isAlive():
					if sd.getGoal(iMauryans, 1) == -1:
						sd.setWondersBuilt(iMauryans, sd.getWondersBuilt(iMauryans) + 1)
						if sd.getWondersBuilt(iMauryans) >= 10:
							sd.setGoal(iMauryans, 1, 1)

		# Mauryan UHV1: Build 10 Mauryan Edicts by 100BC
		if iPlayer == iMauryans and sd.getCivilization(iMauryans) == iHarsha:
			if pMauryans.isAlive():
				if sd.getGoal(iMauryans, 2) == -1:
					if iBuilding == con.iBuddhistCathedral:
						sd.setGoal(iMauryans, 1, 1)
				
		# Qin UHV1: Build the Great Wall and the Terracotta Army by 215BC
		elif iBuilding == con.iGreatWall or iBuilding == con.iTerracottaArmy:
			if iPlayer == iQin and pQin.isAlive() and sd.getGoal(iQin, 0) == -1:
				sd.setWondersBuilt(iQin, sd.getWondersBuilt(iQin) + 1)
				if sd.getWondersBuilt(iQin) == 2:
					sd.setGoal(iQin, 0, 1)
			else:
				sd.setGoal(iQin, 0, 0)
		
		# Antigonid UHV2: Build a Palace in Pella by 250BC
		elif iPlayer == iAntigonids:
			if pAntigonids.isAlive():
				if sd.getGoal(iAntigonids, 1) == -1:
					if iGameTurn <= getTurnForYear(-250):
						if iBuilding == con.iPalace:
							if (city.getX(), city.getY()) == con.tPella:
								sd.setGoal(iAntigonids, 1, 1)
		
		# Bactrian UHV1: Build a Palace in Taxila by 100BC
		elif iPlayer == iBactria:
			if pBactria.isAlive():
				if sd.getGoal(iBactria, 0) == -1:
					if iGameTurn <= getTurnForYear(-100):
						if iBuilding == con.iPalace or iBuilding == con.iRoyalMint:
							if (city.getX(), city.getY()) == con.tTaxila:
								sd.setWondersBuilt(iBactria, sd.getWondersBuilt(iBactria) + 1)
								if sd.getWondersBuilt(iBactria) == 2:
									sd.setGoal(iBactria, 0, 1)
		
		# Parthian UHV1: Build a Palace and National Epic in Ctesiphon by 50BC
		elif iPlayer == iParthia:
			if pParthia.isAlive():
				if sd.getGoal(iParthia, 0) == -1:
					if iGameTurn <= getTurnForYear(-50):
						if iBuilding == con.iPalace or iBuilding == con.iNationalEpic:
							if (city.getX(), city.getY()) == con.tCtesiphon:
								sd.setWondersBuilt(iParthia, sd.getWondersBuilt(iParthia) + 1)
								if sd.getWondersBuilt(iParthia) == 2:
									sd.setGoal(iParthia, 1, 1)
		
		# Ostrogoth UHV1: Build a Palace and Royal Mausoleum in Rome by 50BC
		elif iPlayer == iOstrogoths:
			if pOstrogoths.isAlive():
				if sd.getGoal(iOstrogoths, 0) == -1:
					if iGameTurn <= getTurnForYear(520):
						if iBuilding == con.iPalace or iBuilding == con.iRoyalTomb:
							if (city.getX(), city.getY()) == con.tRome:
								sd.setWondersBuilt(iOstrogoths, sd.getWondersBuilt(iOstrogoths) + 1)
								if sd.getWondersBuilt(iOstrogoths) == 2:
									sd.setGoal(iOstrogoths, 1, 1)
								
		# Gupta UHV3: build Nalanda University and the Dhamek Stupa
		elif iPlayer == iGupta:
			if iBuilding == con.iNalandaUniversity or iBuilding == con.iDhamekStupa or iBuilding == con.iIronPillar:
				if pGupta.isAlive():
					if sd.getGoal(iGupta, 2) == -1:
						sd.setWondersBuilt(iGupta, sd.getWondersBuilt(iGupta) + 1)
						if sd.getWondersBuilt(iGupta) == 3:
							sd.setGoal(iGupta, 2, 1)
							
		# Funan UHV2 Build six Hindu or Buddhist buildings by 300AD
		elif iPlayer == iFunan:
			if sd.getGoal(iFunan, 1) == -1:
				if iBuilding in [con.iBuddhistTemple, con.iBuddhistCathedral, con.iBuddhistMonastery, con.iBuddhistReliquary, con.iBuddhistShrine, con.iBuddhistAcademy, con.iHinduTemple, con.iHinduCathedral, con.iHinduMonastery, con.iHinduReliquary, con.iHinduShrine, con.iHinduAcademy]:
					sd.setWondersBuilt(iFunan, sd.getWondersBuilt(iFunan) + 1)
				if sd.getWondersBuilt(iFunan) == 6:
					sd.setGoal(iFunan, 1, 1)
					
		# Lombard UHV3 build the National Epic by 790
		elif iPlayer == iLombards:
			if sd.getGoal(iLombards, 2) == -1:
				if iBuilding == con.iNationalEpic:
					sd.setGoal(iLombards, 2, 1)
					
		# Tibet UHV2 build 1 Buddhist wonder
		elif iPlayer == iTibet:
			if sd.getGoal(iTibet, 1) == -1:
				if iBuilding in [con.iNalandaUniversity, con.iDhamekStupa, con.iBamyanBuddha, con.iBorobudur, con.iShwedagonPaya]:
					sd.setGoal(iTibet, 1, 1)

				


	def onCombatResult(self, argsList):
		
		if not gc.getGame().isVictoryValid(iHistoricalVictory):
			return
		
		pWinningUnit,pLosingUnit,pAttackingUnit = argsList
		pWinningPlayer = gc.getPlayer(pWinningUnit.getOwner())
		pLosingPlayer = gc.getPlayer(pLosingUnit.getOwner())
		cLosingUnit = PyHelpers.PyInfo.UnitInfo(pLosingUnit.getUnitType())
		
		# Parthian UHV3: Kill 20 Roman units
		if pWinningPlayer.getID() == iParthia:
			if sd.getGoal(iParthia, 2) == -1:
				if pLosingPlayer.getID() in [iRome, iByzantines]:
					sd.setNumParthianKills(sd.getNumParthianKills() + 1)
					if sd.getNumParthianKills() == 20:
						sd.setGoal(iParthia, 2, 1)
						
		# Gojoseon UHV1: Kill 20 Chinese units
		if pWinningPlayer.getID() == iGojoseon:
			if sd.getGoal(iGojoseon, 0) == -1:
				if pLosingPlayer.getID() in [iQin, iHan, iNanYue]:
					sd.setNumGojoseonKills(sd.getNumGojoseonKills() + 1)
					if sd.getNumGojoseonKills() >= 20 and sd.getWondersBuilt(iGojoseon) >= 3:
						sd.setGoal(iGojoseon, 0, 1)
				elif pLosingPlayer.getID() in [iIndependent, iIndependent2, iIndependent3]:
					regionList = [con.rYan, con.rZhao, con.rWei, con.rQin, con.rQi, con.rChu, con.rBa, con.rShu, con.rMinYue, con.rNanYue]
					if gc.getMap().plot(pLosingUnit.getX(), pLosingUnit.getY()).getRegionID() in regionList: 
						sd.setNumGojoseonKills(sd.getNumGojoseonKills() + 1)
						if sd.getNumGojoseonKills() >= 20 and sd.getWondersBuilt(iGojoseon) >= 3:
							sd.setGoal(iGojoseon, 0, 1)


	def onUnitSpreadReligionAttempt(self, argsList):
		'Unit tries to spread religion to a city'
		pUnit, iReligion, bSuccess = argsList
		
		# Tocharian UHV3: Spread Buddhism to 5 Han or Goguryeo cities by 200AD
		if pUnit.getOwner() == iTocharians and bSuccess:
			if sd.getGoal(iTocharians, 2) == -1 and gc.getGame().getGameTurn() <= getTurnForYear(200):
				city = CyMap().plot(pUnit.getX(), pUnit.getY()).getPlotCity()
				if iReligion == con.iBuddhism: 
					if city.getOwner() == iHan or city.getOwner() == iGoguryeo or city.getOwner() == iQin:
						sd.setNumTocharianConversions(sd.getNumTocharianConversions() + 1)
						if sd.getNumTocharianConversions() == 5:
							sd.setGoal(iTocharians, 2, 1)
							
		# Satavahana UHV3: Spread Buddhism and Hinduism to 3 southeast asian cities by 50AD
		if pUnit.getOwner() == iSatavahana and bSuccess:
			if sd.getGoal(iSatavahana, 2) == -1 and gc.getGame().getGameTurn() <= getTurnForYear(50):
				x = pUnit.getX()
				y = pUnit.getY()
				regionList = [con.rFunan, con.rMalaya, con.rBirma, con.rSumatra, con.rJava, con.rBorneo, con.rAnnam, con.rChampa]
				if gc.getMap().plot(x, y).getRegionID() in regionList:
					if iReligion == con.iBuddhism:
						sd.setNumSatavahanaBuddhistConversions(sd.getNumSatavahanaBuddhistConversions() + 1)
					if iReligion == con.iHinduism:
						sd.setNumSatavahanaHinduConversions(sd.getNumSatavahanaHinduConversions() + 1)
				if sd.getNumSatavahanaBuddhistConversions() == 3 and sd.getNumSatavahanaHinduConversions() == 3:
					sd.setGoal(iSatavahana, 2, 1)


	def onGreatPersonBorn(self, argsList):
		pUnit, iPlayer, pCity = argsList
		
		iGameTurn = gc.getGame().getGameTurn()
		
		# Seleucid UHV3: Gain 3 Great Generals by 50BC
		if iPlayer == iSeleucids:
			if pUnit.getUnitType() >= con.iGreatGeneral and pUnit.getUnitType() <= con.iGreatGeneral5:
				if sd.getGoal(iSeleucids, 2) == -1:
					if gc.getGame().getGameTurn() <= getTurnForYear(-50):
						sd.setNumGenerals(sd.getNumGenerals() + 1)
						if sd.getNumGenerals() == 3:
							sd.setGoal(iSeleucids, 2, 1)
							
		# Kalinkan UHV2: 2 Great Generals and 2 Great Prophets
		if iPlayer == iKalinka and sd.getGoal(iKalinka, 1) == -1:
			if pUnit.getUnitType() >= con.iGreatGeneral and pUnit.getUnitType() <= con.iGreatGeneral5:
				sd.setKalinkaGP(0, sd.getKalinkaGP(0) + 1)
			elif pUnit.getUnitType() >= con.iGreatProphet and pUnit.getUnitType() <= con.iGreatProphet3:
				sd.setKalinkaGP(1, sd.getKalinkaGP(1) + 1)
			if sd.getKalinkaGP(0) == 2 and sd.getKalinkaGP(1) == 2:
				sd.setGoal(iKalinka, 1, 1)
		
		# Harsha UHV2 great artist
		if iPlayer == iMauryans and sd.getCivilization(iMauryans) == iMauryans and sd.getGoal(iMauryans, 1) == -1:
			if pUnit.getUnitType() == con.iGreatArtist or pUnit.getUnitType() == con.iGreatArtist2:
				sd.setGoal(iMauryans, 1, 1)


	def calculateTopCityCulture(self, x, y):
	
		iBestCityValue = 0
		pCurrent = gc.getMap().plot( x, y )
		if pCurrent.isCity():
			bestCity = pCurrent.getPlotCity()
			for iPlayerLoop in range(gc.getMAX_PLAYERS()):
				apCityList = PyPlayer(iPlayerLoop).getCityList()
				for pCity in apCityList:
					iTotalCityValue = pCity.GetCy().getCultureTimes100(pCity.getOwner())
					if iTotalCityValue > iBestCityValue:
						bestCity = pCity
						iBestCityValue = iTotalCityValue
			return bestCity
		return -1


	def calculateTopCityPopulation(self, x, y):
	
		iBestCityValue = 0
		pCurrent = gc.getMap().plot( x, y )
		if (pCurrent.isCity()):
			bestCity = pCurrent.getPlotCity()
			for iPlayerLoop in range(gc.getMAX_PLAYERS()):
				apCityList = PyPlayer(iPlayerLoop).getCityList()
				for pCity in apCityList:
					iTotalCityValue = pCity.getPopulation()
					if (iTotalCityValue > iBestCityValue and not pCity.isBarbarian()):
						bestCity = pCity
						iBestCityValue = iTotalCityValue
			return bestCity
		return -1


	def getNumOpenBorders(self, iPlayer):
		
		pTeam = gc.getTeam(gc.getPlayer(iPlayer).getTeam())
		iCount = 0
		for iLoopCiv in range(con.iNumPlayers):
			if iLoopCiv != iPlayer:
				if pTeam.isOpenBorders(iLoopCiv):
					iCount += 1
		return iCount


	def getNumBuildings(self, iPlayer, iBuilding):
		iCount = 0
		apCityList = PyPlayer(iPlayer).getCityList()
		for pCity in apCityList:
			if pCity.getNumBuilding(iBuilding): iCount += 1
		return iCount


	def getNumProvinces(self, iPlayer):
		iNumProvinces = 0
		regionList = []
		apCityList = PyPlayer(iPlayer).getCityList()
		for pCity in apCityList:
			regionID = gc.getMap().plot(pCity.getX(), pCity.getY()).getRegionID()
			if regionID not in regionList and utils.checkRegionControl(iPlayer, regionID):
				regionList.append(regionID)
				iNumProvinces += 1
		return iNumProvinces


	def isHighestGold(self, iPlayer):
		bHighest = True
		iGold = gc.getPlayer(iPlayer).getGold()
		for iLoopCiv in range(con.iNumPlayers):
			if iLoopCiv != iPlayer and gc.getPlayer(iLoopCiv).isAlive():
				if gc.getPlayer(iLoopCiv).getGold() > iGold:
					bHighest = False
					break
		return bHighest


	def isTopCityCulture(self, iPlayer, tCoords):
		bestCity = self.calculateTopCityCulture(tCoords[0], tCoords[1])
		if bestCity != -1:
			if bestCity.getOwner() == iPlayer and bestCity.getX() == tCoords[0] and bestCity.getY() == tCoords[1]:
				return True
		return False


	def isTopCityPopulation(self, iPlayer, tCoords):
		bestCity = self.calculateTopCityPopulation(tCoords[0], tCoords[1])
		if bestCity != -1:
			if bestCity.getOwner() == iPlayer and bestCity.getX() == tCoords[0] and bestCity.getY() == tCoords[1]:
				return True
		return False


	def getNumShrines(self, iPlayer):
		iNumShrines = 0
		apCityList = PyPlayer(iPlayer).getCityList()
		for pCity in apCityList:
			if pCity.getNumBuilding(con.iChristianShrine): iNumShrines += 1
			if pCity.getNumBuilding(con.iIslamicShrine): iNumShrines += 1
			if pCity.getNumBuilding(con.iHinduShrine): iNumShrines += 1
			if pCity.getNumBuilding(con.iBuddhistShrine): iNumShrines += 1
			if pCity.getNumBuilding(con.iJainShrine): iNumShrines += 1
			if pCity.getNumBuilding(con.iConfucianShrine): iNumShrines += 1
			if pCity.getNumBuilding(con.iTaoistShrine): iNumShrines += 1
			if pCity.getNumBuilding(con.iHellenicShrine): iNumShrines += 1
			if pCity.getNumBuilding(con.iManicheanShrine): iNumShrines += 1
			if pCity.getNumBuilding(con.iJewishShrine): iNumShrines += 1
			if pCity.getNumBuilding(con.iZoroastrianShrine): iNumShrines += 1
		return iNumShrines


	def isTopTech(self, iPlayer):
		iNumTotalTechs = gc.getNumTechInfos()
		bTopTech = True
		iNumTechs = 0
		for iTechLoop in range(iNumTotalTechs):
			if gc.getTeam(gc.getPlayer(iPlayer).getTeam()).isHasTech(iTechLoop):
				iNumTechs += 1
		for iPlayerLoop in range(con.iNumPlayers):
			if gc.getPlayer(iPlayerLoop).isAlive() and iPlayerLoop != iPlayer:
				iPlayerNumTechs = 0
				for iTechLoop in range(iNumTotalTechs):
					if gc.getTeam(gc.getPlayer(iPlayerLoop).getTeam()).isHasTech(iTechLoop):
						iPlayerNumTechs = iPlayerNumTechs + 1
				if iPlayerNumTechs >= iNumTechs:
					bTopTech = False
					break
		return bTopTech


	def isTopCulture(self, iPlayer):
		bTopCulture = True
		iCulture = gc.getPlayer(iPlayer).countTotalCulture()
		for iPlayerLoop in range(con.iNumPlayers):
			if gc.getPlayer(iPlayerLoop).isAlive() and iPlayerLoop != iPlayer:
				if gc.getPlayer(iPlayerLoop).countTotalCulture() > iCulture:
					bTopCulture = False
					break
		return bTopCulture


	def isHighestPopulation(self, iPlayer):
		iPop = gc.getPlayer(iPlayer).getRealPopulation()
		bHighest = True
		for iLoopCiv in range(con.iNumPlayers):
			if iPop < gc.getPlayer(iLoopCiv).getRealPopulation():
				bHighest = False
				break
		return bHighest


	def isMostProductive(self, iPlayer):
		iTopValue = 0
		iTopCiv = -1
		for iLoopPlayer in range(iNumPlayers):
			pLoopPlayer = gc.getPlayer(iLoopPlayer)
			if pLoopPlayer.getNumCities() > 0:
				iValue = pLoopPlayer.calculateTotalYield(YieldTypes.YIELD_PRODUCTION)
				if iValue > iTopValue:
					iTopValue = iValue
					iTopCiv = iLoopPlayer
		return (iTopCiv == iPlayer)


	def getNumVassals(self, iPlayer):
		iCounter = 0
		for iCiv in range(iNumPlayers):
			if iCiv != iPlayer:
				if gc.getPlayer(iCiv).isAlive():
					if gc.getTeam(gc.getPlayer(iCiv).getTeam()).isVassal(iPlayer):
						iCounter += 1
		return iCounter


	def getNumLuxuries(self, iPlayer):
		nLuxuries = 0
		pPlayer = gc.getPlayer(iPlayer)
		for iBonus in range(con.iNumResources):
			if gc.getBonusInfo(iBonus).getHappiness() > 0:
				if pPlayer.getNumAvailableBonuses(iBonus) > 0:
					nLuxuries += 1
		return nLuxuries


	def getRegionsOwnedCity(self, iPlayer, regionList, bCoastal=False):
		bFound = False
		for regionID in regionList:
			if utils.checkRegionOwnedCity(iPlayer, regionID, bCoastal):
				bFound = True
				break
		return bFound


	def isFreeOfIslam(self, regionList):
		bSuccess = True
		for regionID in regionList:
			plotList = utils.getRegionPlotList([regionID])
			for tPlot in plotList:
				pCurrent = gc.getMap().plot(tPlot[0], tPlot[1])
				if pCurrent.isCity():
					if pCurrent.getPlotCity().isHasReligion(con.iIslam):
						bSuccess = False
						break
		return bSuccess


	def isHasLegendaryCity(self, iPlayer):
		apCityList = PyPlayer(iPlayer).getCityList()
		for pCity in apCityList:
			if pCity.GetCy().countTotalCultureTimes100() >= 2500000:
				return True
		return False


	def isTopReligion(self, iReligion):
		religionPercent = gc.getGame().calculateReligionPercent(iReligion)
		bFirst = True
		for iLoop in range(con.iNumReligions):
			if iLoop != iReligion:
				if gc.getGame().calculateReligionPercent(iLoop) >= religionPercent:
					bFirst = False
					break
		return bFirst
		
	def onPlayerChangeStateReligion(self, argsList):
		iPlayer, iNewReligion, iOldReligion = argsList
		# Armenian UHV2:
		if (iPlayer != iArmenia) and (iNewReligion == con.iChristianity):
			if sd.getGoal(iArmenia, 1) == -1:
				sd.setGoal(iArmenia, 1, 0)
		elif (iPlayer == iArmenia) and (iNewReligion == con.iChristianity):
			if sd.getGoal(iArmenia, 1) == -1:
				sd.setGoal(iArmenia, 1, 1)
				
		# Goguryeo UHV1:
		if (iPlayer == iQin) or (iPlayer == iHan) or (iPlayer == iJin) or (iPlayer == iTang) or (iPlayer == iYamato) or (iPlayer == iVietnam):
			if (iNewReligion == con.iBuddhism):
				if sd.getGoal(iGoguryeo, 0) == -1:
					sd.setGoal(iGoguryeo, 0, 0)
		elif (iPlayer == iGoguryeo) and (iNewReligion == con.iBuddhism):
			if sd.getGoal(iGoguryeo, 0) == -1:
				sd.setGoal(iGoguryeo, 0, 1)
				
		# Axum UHV1:
		if iPlayer == iAxum:
			if sd.getGoal(iAxum, 0) == -1:
				sd.setGoal(iAxum, 0, 1)
				
		# Ostrogoth UHV3:
		if iPlayer == iOstrogoths:
			if iNewReligion != con.iArianism:
				sd.setGoal(iOstrogoths, 2, 0)
				


	def checkRegions(self, iPlayer, regionList, bVassal=False):
		for regionID in regionList:
			if not utils.checkRegionControl(iPlayer, regionID, bVassal):
				return False
		return True
		
	def countUniqueGreatPeople(self, tCoords):
		"""Returns the number of Great People settled at tCoords(x,y)."""
		iCount = 0
		plot = gc.getMap().plot(tCoords[0], tCoords[1])
		if plot.isCity():
			city = plot.getPlotCity()
			iGreatPriest = gc.getInfoTypeForString("SPECIALIST_GREAT_PRIEST")
			for i in range(iGreatPriest, iGreatPriest+7, 1):
				iCount += min(1, city.getFreeSpecialistCount(i))
		return iCount
		
	def countGreatPeople(self, tCoords):
		"""Returns the number of Great People settled at tCoords(x,y)."""
		iCount = 0
		plot = gc.getMap().plot(tCoords[0], tCoords[1])
		if plot.isCity():
			city = plot.getPlotCity()
			iGreatPriest = gc.getInfoTypeForString("SPECIALIST_GREAT_PRIEST")
			for i in range(iGreatPriest, iGreatPriest+7, 1):
				iCount += city.getFreeSpecialistCount(i)
		return iCount
		
	def getAxumTradeGold(self):
		return sd.scriptDict['iAxumTradeGold']


	def getIcon(self, bVal):
		if bVal:
			return u"%c" %(CyGame().getSymbolID(FontSymbols.POWER_CHAR) + 14)
		else:
			return u"%c" %(CyGame().getSymbolID(FontSymbols.POWER_CHAR) + 15)


	def getUHVHelp(self, iPlayer, iGoal):
		"Returns an array of help strings used by the Victory Screen table"
		
		pPlayer = gc.getPlayer(iPlayer)
		
		aHelp = [];
		
		# the info is outdated or irrelevant once the goal has been accomplished or failed
		if sd.getGoal(iPlayer, iGoal) == 1:
			aHelp.append(self.getIcon(True) + 'Goal accomplished!')
			return aHelp
		elif sd.getGoal(iPlayer, iGoal) == 0:
			aHelp.append(self.getIcon(False) + 'Goal failed!')
			return aHelp
			
		if iPlayer == iAntigonids:
			if iGoal == 0:
				aHelp.append(self.getIcon(sd.getGoal(iAntigonids, 0) == -1) + 'Monarchy not known to another civilization')
			elif iGoal == 1:
				aHelp.append(self.getIcon(sd.getGoal(iAntigonids, 1) == 1) + 'Palace built in Pella')
			elif iGoal ==2:
				iNumWonders = 0
				for iWonder in range (con.iPyramids, con.iShwedagonPaya):
					if self.getNumBuildings(iAntigonids, iWonder):
						iNumWonders += 1
				aHelp.append(self.getIcon(iNumWonders >= 7) + 'Wonders controlled: ' + str(iNumWonders) + ' / 7')
		
		if iPlayer == iSeleucids:
			if iGoal == 0:
				bMacedonia = utils.checkRegionControl(iSeleucids, con.rMacedonia, True)
				bEgypt = utils.checkRegionControl(iSeleucids, con.rEgypt, True)
				bMesopotamia = utils.checkRegionControl(iSeleucids, con.rMesopotamia, True)
				bMedia = utils.checkRegionControl(iSeleucids, con.rMedia, True)
				bJudea = utils.checkRegionControl(iSeleucids, con.rJudea, True)
				bSyria = utils.checkRegionControl(iSeleucids, con.rSyria, True)
				bAsia = utils.checkRegionControl(iSeleucids, con.rAsia, True)
				bCappadocia = utils.checkRegionControl(iSeleucids, con.rCappadocia, True)
				bGreece = utils.checkRegionControl(iSeleucids, con.rGreece, True)
				bThrace = utils.checkRegionControl(iSeleucids, con.rThrace, True)
				bPersia = utils.checkRegionControl(iSeleucids, con.rPersia, True)
				bArachosia = utils.checkRegionControl(iSeleucids, con.rArachosia, True)
				bMargiana = utils.checkRegionControl(iSeleucids, con.rMargiana, True)
				bBactria = utils.checkRegionControl(iSeleucids, con.rBactria, True)
				bSogdiana = utils.checkRegionControl(iSeleucids, con.rSogdiana, True)
				aHelp.append(self.getIcon(bMacedonia) + 'Macedon, ' + self.getIcon(bEgypt) + 'Egypt, ' + self.getIcon(bMesopotamia) + 'Mesopotamia, ' + self.getIcon(bMedia) + 'Media, ' + self.getIcon(bJudea) + 'Judea, ' + self.getIcon(bSyria) + 'Syria, ' + self.getIcon(bAsia) + 'Asia')
				aHelp.append(self.getIcon(bGreece) + 'Greece, ' + self.getIcon(bThrace) + 'Thrace, ' + self.getIcon(bPersia) + 'Persia, ' + self.getIcon(bArachosia) + 'Arachosia, ' + self.getIcon(bMargiana) + 'Margiana ' + self.getIcon(bCappadocia) + 'Cappadocia')
				aHelp.append(self.getIcon(bBactria) + 'Bactria, ' + self.getIcon(bSogdiana) + 'Sogdiana')
			elif iGoal == 1:
				iProvinceCount = self.getNumProvinces(iSeleucids)
				iCityCount = pSeleucids.getNumCities()
				aHelp.append(self.getIcon(iProvinceCount >= 6) + 'Provinces controlled: ' + str(iProvinceCount) + ' / 6, ' + self.getIcon(iCityCount >= 12) + 'Cities controlled: ' + str(iCityCount) + ' / 12')
			elif iGoal == 2:
				iCount = sd.getNumGenerals()
				aHelp.append(self.getIcon(iCount >= 3) + 'Great Generals created: ' + str(iCount) + ' / 3')
		
		elif iPlayer == iEgypt:
			if iGoal == 0:
				bLighthouse = self.getNumBuildings(iEgypt, con.iGreatLighthouse)
				bLibrary = self.getNumBuildings(iEgypt, con.iGreatLibrary)
				aHelp.append(self.getIcon(bLighthouse) + 'The Great Lighthouse, ' + self.getIcon(bLibrary) + 'The Great Library')
			elif iGoal == 1: 
				aHelp.append(self.getIcon(self.isTopCityPopulation(iEgypt, con.tAlexandria)) + 'Alexandria ranked first in Population, ' + self.getIcon(self.isTopCityCulture(iEgypt, con.tAlexandria)) + 'Alexandria ranked first in Culture')
			elif iGoal == 2:
				PortList = []
				apCityList = PyPlayer(iEgypt).getCityList()
				for pCity in apCityList:
					if gc.getMap().plot(pCity.getX(), pCity.getY()).getRegionID() in [con.rGreece, con.rThrace, con.rAsia, con.rCrete, con.rRhodes, con.rCyprus, con.rCappadocia, con.rSyria, con.rJudea, con.rEgypt, con.rLibya]:
						if 32 < pCity.getY() < 54:
							if (pCity.getX(), pCity.getY()) not in [(58, 33), (58, 34), (60, 35), (60, 34), (60, 33), (61, 35), (61, 34), (61, 33), (62, 35), (63, 35)] and pCity.GetCy().isCoastal(gc.getMIN_WATER_SIZE_FOR_OCEAN()):
								PortList.append(pCity)
				iNumPorts = len(PortList)
				aHelp.append(self.getIcon(iNumPorts >= 7) + 'Ports controlled: ' + str(iNumPorts) + ' / 7, ')
				
		
		elif iPlayer == iCarthage:
			if iGoal == 0: 
				iCount = self.getNumLuxuries(iCarthage)
				aHelp.append(self.getIcon(iCount >= 6) + 'Luxury resources: ' + str(iCount) + ' / 6')
			elif iGoal == 1:
				bComplete = False
				if sd.getGoal(iCarthage, 1) == 1: bComplete = True
				aHelp.append(self.getIcon(bComplete) + 'Romans destroyed')
			elif iGoal == 2: 
				iCount = self.getNumLuxuries(iCarthage)
				aHelp.append(self.getIcon(iCount >= 9) + 'Luxury resources: ' + str(iCount) + ' / 9')
		
		elif iPlayer == iMauryans:
			if sd.getCivilization(iMauryans) == iMauryans:
				if iGoal == 0:
					bMagadha = utils.checkRegionControl(iMauryans, con.rMagadha)
					bPunjab = utils.checkRegionControl(iMauryans, con.rPunjab)
					bBangala = utils.checkRegionControl(iMauryans, con.rBangala)
					bAvanti = utils.checkRegionControl(iMauryans, con.rAvanti)
					bDeccan = utils.checkRegionControl(iMauryans, con.rDeccan)
					bSindh = utils.checkRegionControl(iMauryans, con.rSindh)
					bKerala = utils.checkRegionControl(iMauryans, con.rKerala)
					bGandhara = utils.checkRegionControl(iMauryans, con.rGandhara)
					bArachosia = utils.checkRegionControl(iMauryans, con.rArachosia)
					bSaurashtra = utils.checkRegionControl(iMauryans, con.rSaurashtra)
					bKalinka = utils.checkRegionControl(iMauryans, con.rKalinka)
					bAndhra = utils.checkRegionControl(iMauryans, con.rAndhra)
					bBharat = utils.checkRegionControl(iMauryans, con.rBharat)
					aHelp.append(self.getIcon(bMagadha) + 'Magadha, ' + self.getIcon(bPunjab) + 'Punjab, ' + self.getIcon(bBangala) + 'Anga, ' + self.getIcon(bAvanti) + 'Avanti, ' + self.getIcon(bAvanti) + 'Kalinka, ' + self.getIcon(bDeccan) + 'Deccan')
					aHelp.append(self.getIcon(bSindh) + 'Sindh, ' + self.getIcon(bKerala) + 'Kerala, ' + self.getIcon(bGandhara) + 'Gandhara, ' + self.getIcon(bArachosia) + 'Arachosia' + self.getIcon(bSaurashtra) + 'Saurashtra, ' + self.getIcon(bAndhra) + 'Andhra')
					aHelp.append(self.getIcon(bBharat) + 'Bharat')
				elif iGoal == 1:
					iNumMauryanEdicts = sd.getWondersBuilt(iMauryans)
					aHelp.append(self.getIcon(iNumMauryanEdicts >= 10) + 'Mauryan Edicts: ' + str(iNumMauryanEdicts) + ' / 10')
				elif iGoal == 2:
					bSuccess = True
					for iLoopCiv in range(iNumTotalPlayers):
						apCityList = PyPlayer(iLoopCiv).getCityList()
						for pCity in apCityList:
							if gc.getMap().plot(pCity.getX(), pCity.getY()).getRegionID() in con.lIndianRegions:
								if not pCity.GetCy().isHasReligion(con.iBuddhism):
									bSuccess = False
									break
					aHelp.append(self.getIcon(bSuccess) + 'Buddhism in every Indian city')
					
			else:
				if iGoal == 0:
					bMagadha = utils.checkRegionControl(iMauryans, con.rMagadha)
					bPunjab = utils.checkRegionControl(iMauryans, con.rPunjab)
					bBangala = utils.checkRegionControl(iMauryans, con.rBangala)
					bSindh = utils.checkRegionControl(iMauryans, con.rSindh)
					bGandhara = utils.checkRegionControl(iMauryans, con.rGandhara)
					bSaurashtra = utils.checkRegionControl(iMauryans, con.rSaurashtra)
					bBharat = utils.checkRegionControl(iMauryans, con.rBharat)
					aHelp.append(self.getIcon(bMagadha) + 'Magadha, ' + self.getIcon(bPunjab) + 'Punjab, ' + self.getIcon(bBangala) + 'Anga, ' + self.getIcon(bSindh) + 'Sindh, ')
					aHelp.append(self.getIcon(bGandhara) + 'Gandhara, ' + self.getIcon(bSaurashtra) + 'Saurashtra, ' + self.getIcon(bBharat) + 'Bharat')
				elif iGoal == 1:
					aHelp.append(self.getIcon(sd.getGoal(iMauryans, 1) == 1) + 'Great Artist produced')
				elif iGoal == 2:
					aHelp.append(self.getIcon(sd.getGoal(iMauryans, 2) == 1) + 'Buddhist Cathedral built')
				
		elif iPlayer == iKalinka:
			if iGoal == 0: 
				bHorses = pKalinka.getNumAvailableBonuses(con.iHorse)
				aHelp.append(self.getIcon(bHorses) + 'Horses acquired')
			elif iGoal == 1:
				iGenerals = sd.getKalinkaGP(0)
				iProphets = sd.getKalinkaGP(1)
				aHelp.append(self.getIcon(iGenerals >= 2) + 'Great Generals: ' + str(iGenerals) + ' /2')
				aHelp.append(self.getIcon(iProphets >= 2) + 'Great Prophets: ' + str(iProphets) + ' /2')
			elif iGoal == 2:
				iCount = sd.getWondersBuilt(iKalinka)
				aHelp.append(self.getIcon(iCount >= 7) + 'Jain buildings built: ' + str(iCount) + ' /7')
				
		elif iPlayer == iQin:
			if iGoal == 0: 
				if sd.get3KingdomsMarker() == 1:
					bHan = utils.checkRegionControl(iQin, con.rHan)
					bWu = utils.checkRegionControl(iQin, con.rWu)
					bQi = utils.checkRegionControl(iQin, con.rQi) 
					bQin = utils.checkRegionControl(iQin, con.rQin) 
					bMinYue = utils.checkRegionControl(iQin, con.rMinYue) 
					bNanYue = utils.checkRegionControl(iQin, con.rNanYue) 
					bShu = utils.checkRegionControl(iQin, con.rShu) 
					bBa = utils.checkRegionControl(iQin, con.rBa)
					bChu = utils.checkRegionControl(iQin, con.rChu)
					bYan = utils.checkRegionControl(iQin, con.rYan)
					bZhao = utils.checkRegionControl(iQin, con.rZhao)
					aHelp.append(self.getIcon(bHan) + 'Han, ' + self.getIcon(bWu) + 'Wu, ' + self.getIcon(bQi) + 'Qi, ' + self.getIcon(bQin) + 'Qin' + self.getIcon(bChu) + 'Chu')
					aHelp.append(self.getIcon(bMinYue) + 'Min Yue, ' + self.getIcon(bNanYue) + 'Nanyue, ' + self.getIcon(bShu) + 'Shu, ' + self.getIcon(bBa) + 'Ba')
					aHelp.append(self.getIcon(bYan) + 'Yan, ' + self.getIcon(bZhao) + 'Zhao')
				else:
					bWall = self.getNumBuildings(iQin, con.iGreatWall)
					bArmy = self.getNumBuildings(iQin, con.iTerracottaArmy)
					aHelp.append(self.getIcon(bWall) + 'The Great Wall, ' + self.getIcon(bArmy) + 'The Terracotta Army')
			elif iGoal == 1:
				if sd.get3KingdomsMarker() == 1:
					iCount = self.getNumLuxuries(iQin)
					aHelp.append(self.getIcon(iCount >= 6) + 'Luxury resources: ' + str(iCount) + ' / 6')
				else:
					bQin = utils.checkRegionControl(iQin, con.rQin)
					bHan = utils.checkRegionControl(iQin, con.rHan)
					bYan = utils.checkRegionControl(iQin, con.rYan)
					bZhao = utils.checkRegionControl(iQin, con.rZhao)
					bChu = utils.checkRegionControl(iQin, con.rChu)
					bNanYue = utils.checkRegionControl(iQin, con.rNanYue)
					bWu = utils.checkRegionControl(iQin, con.rWu)
					bQi = utils.checkRegionControl(iQin, con.rQi)
					aHelp.append(self.getIcon(bQin) + 'Qin, ' + self.getIcon(bHan) + 'Han, ' + self.getIcon(bYan) + 'Yan, ' + self.getIcon(bZhao) + 'Zhao, ' + self.getIcon(bChu) + 'Chu')
					aHelp.append(self.getIcon(bNanYue) + 'Nan Yue, ' + self.getIcon(bQi) + 'Qi' + self.getIcon(bWu) + 'Wu')
			elif iGoal == 2:
				if sd.get3KingdomsMarker() == 1:
					aHelp.append(self.getIcon(sd.getGoal(iQin, 2) != 0) + 'Stirrup not yet discovered')
				else:
					iCount = self.getNumProvinces(iQin)
					aHelp.append(self.getIcon(iCount >= 9) + 'Provinces controlled: ' + str(iCount) + ' / 9')
				
		elif iPlayer == iGojoseon:
			if iGoal == 0:
				aHelp.append(self.getIcon(sd.getNumGojoseonKills() >= 20) + 'Chinese units killed: ' + str(sd.getNumGojoseonKills()) + ' / 20')
				aHelp.append(self.getIcon(sd.getWondersBuilt(iGojoseon) >= 3) + 'Chinese cities captured: ' + str(sd.getWondersBuilt(iGojoseon)) + ' / 3')
			elif iGoal == 1:
				aHelp.append(self.getIcon(sd.getGoal(iGojoseon, 1) == -1) + 'Marksmanship not known to another civilization')
			elif iGoal == 2:
				aHelp.append(self.getIcon(sd.getGoal(iGojoseon, 2) != 0) + 'No cities lost')
		
		elif iPlayer == iNubia:
			if iGoal == 0: 
				bIronWorking = gc.getTeam(pNubia.getTeam()).isHasTech(con.iIronWorking)
				bAlphabet = gc.getTeam(pNubia.getTeam()).isHasTech(con.iAlphabet)
				aHelp.append(self.getIcon(bIronWorking) + 'Iron Working, ' + self.getIcon(bAlphabet) + 'Alphabet')
			elif iGoal == 1:
				aHelp.append(self.getIcon(self.isMostProductive(iNubia)) + 'Highest production')
			elif iGoal == 2:
				iCount = pNubia.getNumAvailableBonuses(con.iGold)
				aHelp.append(self.getIcon(iCount >= 5) + 'Gold resources: ' + str(iCount) + ' / 5')
		
		elif iPlayer == iSaba:
			if iGoal == 0:
				iCount = pSaba.getNumCities()
				aHelp.append(self.getIcon(iCount >= 4) + 'Cities controlled: ' + str(iCount) + ' / 4')
			elif iGoal == 1:
				iCount = pSaba.countTotalCulture()
				aHelp.append(self.getIcon(iCount >= 3000 * (gc.getGame().getGameSpeedType() + 2) / 2) + 'Total Culture: ' + str(iCount) + ' / ' + str(3000 * (gc.getGame().getGameSpeedType() + 2) / 2))
			elif iGoal == 2:
				iMediterraneanCities = 0
				iPersianCities = 0
				iIndianCities = 0
				iEasternCities = 0
				for iPlayer in range(iNumTotalPlayers):
					apCityList = PyPlayer(iPlayer).getCityList()
					for pCity in apCityList:
						if pCity.GetCy().isHasCorporation(con.iIncenseMerchants) and pCity.getOwner() != con.iSaba:
							pCurrent = gc.getMap().plot(pCity.getX(), pCity.getY())
							if pCurrent.getRegionID() == con.rSyria:
								if pCity.GetCy().isCoastal(gc.getMIN_WATER_SIZE_FOR_OCEAN()):
									iMediterraneanCities += 1
								else:
									iPersianCities += 1
							elif pCurrent.getRegionID() in con.lMediterraneanRegions:
								iMediterraneanCities += 1
							elif pCurrent.getRegionID() in con.lPersianRegions:
								iPersianCities += 1
							elif pCurrent.getRegionID() in con.lGreaterIndianRegions or pCurrent.getRegionID() in con.lCentralAsianRegions:
								iIndianCities += 1
							elif pCurrent.getRegionID() in con.lGreaterChineseRegions or pCurrent.getRegionID() in con.lSouthEastAsianRegions:
								iEasternCities += 1
				aHelp.append(self.getIcon(iMediterraneanCities >= 5) + 'Mediterranean cities: ' + str(iMediterraneanCities) + ' /5  ' + self.getIcon(iPersianCities >= 5) + 'Persian cities: ' + str(iPersianCities) + ' /5')
				aHelp.append(self.getIcon(iIndianCities >= 5) + 'Indian and Central Asian cities: ' + str(iIndianCities) + ' /5  ' + self.getIcon(iEasternCities >= 5) + 'East and Southeast Asian cities: ' + str(iEasternCities) + ' /5')
		
		elif iPlayer == iPandyans:
			if sd.get3KingdomsMarker() == 3:
				if iGoal == 0:
					bTamilNadu = utils.checkRegionControl(iPandyans, con.rTamilNadu)
					bAndhra = utils.checkRegionControl(iPandyans, con.rAndhra)
					bKalinka = utils.checkRegionControl(iPandyans, con.rKalinka)
					bBangala = utils.checkRegionControl(iPandyans, con.rBangala)
					aHelp.append(self.getIcon(bTamilNadu) + 'Tamil Nadu, ' + self.getIcon(bAndhra) + 'Andhra, ' + self.getIcon(bKalinka) + 'Kalinka, ' + self.getIcon(bBangala) + 'Anga')
				elif iGoal == 1:
					bNationalEpic = self.getNumBuildings(iPandyans, con.iNationalEpic)
					bKhajuraho = self.getNumBuildings(iPandyans, con.iKhajuraho)
					aHelp.append(self.getIcon(bNationalEpic) + 'National Epic, ' + self.getIcon(bKhajuraho) + 'Khajuraho')
				elif iGoal == 2:
					iCount = self.getNumVassals(iPandyans)
					aHelp.append(self.getIcon(iCount >= 2) + 'Vassals: ' + str(iCount) + ' / 2')
					
			elif sd.get3KingdomsMarker() == 4:
				if iGoal == 0: 
					iLuxuries = ((pPandyans.getNumAvailableBonuses(con.iSilk)) + (pPandyans.getNumAvailableBonuses(con.iGold)) + (pPandyans.getNumAvailableBonuses(con.iIncense)) + (pPandyans.getNumAvailableBonuses(con.iSilver)))
					iGold = pPandyans.getNumAvailableBonuses(con.iGold)
					iIncense = pPandyans.getNumAvailableBonuses(con.iIncense)
					iSilver = pPandyans.getNumAvailableBonuses(con.iSilver)
					aHelp.append(self.getIcon(iLuxuries >= 2) + 'Foreign Luxuries: ' + str(iLuxuries) + ' / 2')
				elif iGoal == 1:
					iNumClothMarkets = (self.getNumBuildings(iPandyans, con.iClothMarket))
					iNumSpiceMarkets = (self.getNumBuildings(iPandyans, con.iSpiceMarket))
					aHelp.append(self.getIcon(iNumClothMarkets >= 2) + 'Cloth Markets: ' + str(iNumClothMarkets) + ' / 7  ' + self.getIcon(iNumSpiceMarkets >= 2) + 'Spice Markets: ' + str(iNumSpiceMarkets))
				elif iGoal == 2:
					aHelp.append(self.getIcon(sd.getGoal(iPandyans, 2) == -1) + 'Steel Working not known to another civilization')
					
			elif sd.get3KingdomsMarker() == 5:
				if iGoal == 0: 
					iNumTemples = 0
					apCityList = PyPlayer(iPandyans).getCityList()
					for pCity in apCityList:
						if gc.getMap().plot(pCity.getX(), pCity.getY()).getRegionID() == con.rTamilNadu:
							for iBuilding in range(con.iJewishTemple, con.iIslamicShrine):
								if pCity.GetCy().getNumRealBuilding(iBuilding):
									iNumTemples += 1
					aHelp.append(self.getIcon(iNumTemples >= 9) + 'Temples in Tamil Nadu: ' + str(iNumTemples) + ' / 9')
				elif iGoal == 1:
					iNumArtists = 0
					iNumSaints = 0
					apCityList = PyPlayer(iPandyans).getCityList()
					for pCity in apCityList:
						iNumArtists += pCity.GetCy().getFreeSpecialistCount(gc.getInfoTypeForString("SPECIALIST_GREAT_ARTIST"))
						iNumSaints += pCity.GetCy().getFreeSpecialistCount(gc.getInfoTypeForString("SPECIALIST_GREAT_PRIEST"))
					aHelp.append(self.getIcon(iNumArtists >= 2) + 'Great Artists settled: ' + str(iNumArtists) + ' / 2  ' + self.getIcon(iNumArtists >= 2) + '  Great Saints settled: ' + str(iNumSaints) + ' / 2')
				elif iGoal == 2:
					iTamilCulture = 0
					iIndianCulture = 0
					for iLoopCiv in range(iNumTotalPlayers): 
						apCityList = PyPlayer(iLoopCiv).getCityList()
						for pCity in apCityList:
							if gc.getMap().plot(pCity.getX(), pCity.getY()).getRegionID() == con.rTamilNadu:
								iTamilCulture += pCity.getCulture()
							elif gc.getMap().plot(pCity.getX(), pCity.getY()).getRegionID() in con.lIndianRegions:
								iIndianCulture += pCity.getCulture()
					aHelp.append(self.getIcon(iTamilCulture > iTamilCulture) + 'Tamil culture: ' + str(iTamilCulture) + '  Indian culture: ' + str(iIndianCulture))
		
		elif iPlayer == iCelts:
			if iGoal == 0:
				bComplete = False
				if sd.getGoal(iCelts, 0) == 1: bComplete = True
				aHelp.append(self.getIcon(bComplete) + 'Rome captured')
			elif iGoal == 1:
				bGaul = utils.checkRegionOwnedCity(iCelts, con.rGaul)
				bNItaly = utils.checkRegionOwnedCity(iCelts, con.rNItaly)
				bSeptimania = utils.checkRegionOwnedCity(iCelts, con.rSeptimania)
				bAquitania = utils.checkRegionOwnedCity(iCelts, con.rAquitania)
				bIberia = utils.checkRegionOwnedCity(iCelts, con.rIberia)
				bIllyricum = utils.checkRegionOwnedCity(iCelts, con.rIllyricum)
				bGermania = utils.checkRegionOwnedCity(iCelts, con.rGermania)
				bBritannia = utils.checkRegionOwnedCity(iCelts, con.rBritannia)
				aHelp.append(self.getIcon(bGaul) + 'Gaul, ' + self.getIcon(bNItaly) + 'Northern Italy, ' + self.getIcon(bSeptimania) + 'Narbonensis, ' + self.getIcon(bAquitania) + 'Aquitania')
				aHelp.append(self.getIcon(bIberia) + 'Iberia, ' + self.getIcon(bIllyricum) + 'Illyricum, ' + self.getIcon(bGermania) + 'Germania ' + self.getIcon(bBritannia) + 'Britannia')
			elif iGoal == 2: 
				aHelp.append(self.getIcon(self.isTopCulture(iCelts)) + 'Highest Culture')
				
		elif iPlayer == iPontus:
			if iGoal == 0:
				bPontus = utils.checkRegionControl(iPontus, con.rPontus)
				bCappadocia = utils.checkRegionControl(iPontus, con.rCappadocia)
				bCrimea = utils.checkRegionControl(iPontus, con.rCrimea)
				bThrace = utils.checkRegionControl(iPontus, con.rThrace)
				bAsia = utils.checkRegionControl(iPontus, con.rAsia)
				aHelp.append(self.getIcon(bPontus) + 'Pontus, ' + self.getIcon(bCappadocia) + 'Cappadocia, ' + self.getIcon(bCrimea) + 'Crimea, ' + self.getIcon(bThrace) + 'Thrace, ' + self.getIcon(bAsia) + 'Asia')
			elif iGoal == 1:
				iCount = sd.getWondersBuilt(iPontus)
				iProvinces = self.getNumProvinces(iPontus)
				bGreece = utils.checkRegionControl(iPontus, con.rGreece)
				aHelp.append(self.getIcon(iProvinces >= 7) + 'Provinces controlled: ' + str(iProvinces) + ' / 7')
				aHelp.append(self.getIcon(iCount >= 4) + 'Roman cities captured: ' + str(iCount) + ' / 4')
				aHelp.append(self.getIcon(bGreece) + 'Greece controlled')
			elif iGoal == 2: 
				iCount = self.countPlayersByMinAttitude(iPontus, 4)
				aHelp.append(self.getIcon(iCount >= 3) + 'Friendly civs: ' + str(iCount) + ' / 3')
		
		elif iPlayer == iRome:
			if gc.getTeam(pRome.getTeam()).isHasTech(con.iRomanEmpire):
				if iGoal == 0:
					bNItaly = utils.checkRegionControl(iRome, con.rNItaly)
					bSItaly = utils.checkRegionControl(iRome, con.rSItaly)
					bSicily = utils.checkRegionControl(iRome, con.rSicily)
					bIberia = utils.checkRegionControl(iRome, con.rIberia)
					bAfrica = utils.checkRegionControl(iRome, con.rAfrica)
					bSeptimania = utils.checkRegionControl(iRome, con.rSeptimania)
					bAsia = utils.checkRegionControl(iRome, con.rAsia)
					bGreece = utils.checkRegionControl(iRome, con.rGreece)
					bEgypt = utils.checkRegionControl(iRome, con.rEgypt)
					bLibya = utils.checkRegionControl(iRome, con.rLibya)
					bJudea = utils.checkRegionControl(iRome, con.rJudea)
					bSyria = utils.checkRegionControl(iRome, con.rSyria)
					bBaetica = utils.checkRegionControl(iRome, con.rBaetica)
					bCappadocia = utils.checkRegionControl(iRome, con.rCappadocia)
					aHelp.append(self.getIcon(bNItaly) + 'Northern Italy, ' + self.getIcon(bSItaly) + 'Southern Italy, ' + self.getIcon(bSicily) + 'Sicily, ' + self.getIcon(bIberia) + 'Iberia, ' + self.getIcon(bAfrica) + 'Africa, ' + self.getIcon(bSeptimania) + 'Southern Gaul, ' + self.getIcon(bAsia) + 'Asia')
					aHelp.append(self.getIcon(bGreece) + 'Greece, ' + self.getIcon(bEgypt) + 'Egypt, ' + self.getIcon(bLibya) + 'Libya, ' + self.getIcon(bJudea) + 'Judea ' + self.getIcon(bSyria) + 'Syria, ' + self.getIcon(bCappadocia) + 'Cappadocia ' + self.getIcon(bBaetica) + 'Baetica')
				elif iGoal == 1:
					aHelp.append(self.getIcon(self.isTopCityPopulation(iRome, con.tRome)) + 'Rome ranked first in Population')
				elif iGoal == 2:
					bNItaly = utils.checkRegionControl(iRome, con.rNItaly)
					bSItaly = utils.checkRegionControl(iRome, con.rSItaly)
					bSicily = utils.checkRegionControl(iRome, con.rSicily)
					bIberia = utils.checkRegionControl(iRome, con.rIberia)
					bAfrica = utils.checkRegionControl(iRome, con.rAfrica)
					bSeptimania = utils.checkRegionControl(iRome, con.rSeptimania)
					bAsia = utils.checkRegionControl(iRome, con.rAsia)
					bGreece = utils.checkRegionControl(iRome, con.rGreece)
					bAquitania = utils.checkRegionControl(iRome, con.rAquitania)
					bEgypt = utils.checkRegionControl(iRome, con.rEgypt)
					bLibya = utils.checkRegionControl(iRome, con.rLibya)
					bJudea = utils.checkRegionControl(iRome, con.rJudea)
					bSyria = utils.checkRegionControl(iRome, con.rSyria)
					bGaul = utils.checkRegionControl(iRome, con.rGaul)
					bBritannia = utils.checkRegionControl(iRome, con.rBritannia)
					bIllyricum = utils.checkRegionControl(iRome, con.rIllyricum)
					bThrace = utils.checkRegionControl(iRome, con.rThrace)
					bMesopotamia = utils.checkRegionControl(iRome, con.rMesopotamia)
					bMauretania = utils.checkRegionControl(iRome, con.rMauretania)
					bCrimea = utils.checkRegionControl(iRome, con.rCrimea)
					bArmenia = utils.checkRegionControl(iRome, con.rArmenia)
					bMesopotamia = utils.checkRegionControl(iRome, con.rMesopotamia)
					bBaetica = utils.checkRegionControl(iRome, con.rBaetica)
					bLusitania = utils.checkRegionControl(iRome, con.rLusitania)
					bDacia = utils.checkRegionControl(iRome, con.rDacia)
					bCappadocia = utils.checkRegionControl(iRome, con.rCappadocia)
					bPontus = utils.checkRegionControl(iRome, con.rPontus)
					bNumidia = utils.checkRegionControl(iRome, con.rNumidia)
					aHelp.append(self.getIcon(bNItaly) + 'Northern Italy, ' + self.getIcon(bSItaly) + 'Southern Italy, ' + self.getIcon(bSicily) + 'Sicily, ' + self.getIcon(bIberia) + 'Iberia, ' + self.getIcon(bAfrica) + 'Africa, ' + self.getIcon(bSeptimania) + 'Narbonensis' + self.getIcon(bNumidia) + 'Numidia')
					aHelp.append(self.getIcon(bGreece) + 'Greece, ' + self.getIcon(bAquitania) + 'Aquitania, ' + self.getIcon(bEgypt) + 'Egypt, ' + self.getIcon(bLibya) + 'Libya, ' + self.getIcon(bJudea) + 'Judea ' + self.getIcon(bSyria) + 'Syria, ' + self.getIcon(bCrimea) + 'Crimea') 
					aHelp.append(self.getIcon(bGaul) + 'Gaul, ' + self.getIcon(bBritannia) + 'Britannia, ' + self.getIcon(bIllyricum) + 'Illyricum, ' + self.getIcon(bThrace) + 'Thrace, ' + self.getIcon(bMesopotamia) + 'Mesopotamia, ' + self.getIcon(bMauretania) + 'Mauretania')
					aHelp.append(self.getIcon(bLusitania) + 'Lusitania, ' + self.getIcon(bBaetica) + 'Baetica, ' + self.getIcon(bAsia) + 'Asia, ' + self.getIcon(bArmenia) + 'Armenia, ' + self.getIcon(bDacia) + 'Dacia ' + self.getIcon(bCappadocia) + 'Cappadocia ' + self.getIcon(bPontus) + 'Pontus')
			else:
				if iGoal == 0:
					iRomanMedProvinces = 0
					bSicily = utils.checkRegionControl(iRome, con.rSicily)
					bAfrica = utils.checkRegionControl(iRome, con.rAfrica)
					regionList = [con.rNItaly, con.rSItaly, con.rSicily, con.rIberia, con.rBaetica, con.rSeptimania, con.rAfrica, con.rGreece, con.rAsia, con.rSyria, con.rJudea, con.rEgypt, con.rLibya, con.rMauretania, con.rCyprus, con.rCrete, con.rSardinia, con.rCorsica, con.rThrace, con.rNumidia, con.rRhodes, con.rMallorca, con.rMacedonia, con.rIllyricum]
					for regionID in regionList:
						if utils.checkRegionControl(iRome, regionID):
							iRomanMedProvinces += 1
					aHelp.append(self.getIcon(iRomanMedProvinces >= 10) + 'Mediterranean provinces controlled: ' + str(iRomanMedProvinces) + ' / 10' + self.getIcon(bSicily) + 'Sicily controlled ' + self.getIcon(bAfrica) + 'Africa controlled')
				if iGoal == 1: 
					bEngineering = gc.getTeam(pRome.getTeam()).isHasTech(con.iEngineering)
					bJurisprudence = gc.getTeam(pRome.getTeam()).isHasTech(con.iJurisprudence)
					aHelp.append(self.getIcon(bEngineering) + 'Engineering, ' + self.getIcon(bJurisprudence) + 'Jurisprudence')
				if iGoal == 2:
					iCount = 0
					if pPlayer.getNumCities() > 0:
						capital = pPlayer.getCapitalCity()
						iCount = self.countGreatPeople((capital.getX(), capital.getY()))
					aHelp.append(self.getIcon(iCount >= 5) + 'Great people settled: ' + str(iCount) + ' / 5')
				
		elif iPlayer == iVietnam:
			if iGoal== 0:
				bAnnam = utils.checkRegionControl(iVietnam, con.rAnnam)
				bChampa = utils.checkRegionControl(iVietnam, con.rChampa)
				bNanYue = utils.checkRegionControl(iVietnam, con.rNanYue)
				aHelp.append(self.getIcon(bAnnam) + 'Annam, ' + self.getIcon(bChampa) + 'Champa, ' + self.getIcon(bNanYue) + 'Nan Yue')
			elif iGoal == 1:
				bHigherPopulation = False
				if gc.getPlayer(iVietnam).getRealPopulation() > gc.getPlayer(iHan).getRealPopulation():
					bHigherPopulation = True
				bHigherCulture = False
				if gc.getPlayer(iVietnam).countTotalCulture() > gc.getPlayer(iHan).countTotalCulture():
					bHigherCulture = True
				aHelp.append(self.getIcon(bHigherPopulation) + 'Higher population than the Han' + self.getIcon(bHigherCulture) + 'Higher culture than the Han')
			elif iGoal == 2:
				iCount = sd.getWondersBuilt(iVietnam)
				aHelp.append(self.getIcon(iCount >= 12) + 'Buddhist buildings built: ' + str(iCount) + ' /12')
		
		elif iPlayer == iTocharians:
			if iGoal == 0: 
				iCount = self.getNumOpenBorders(iTocharians)
				aHelp.append(self.getIcon(iCount >= 5) + 'Open Borders agreements: ' + str(iCount) + ' / 5')
			elif iGoal == 1:
				bIncense = pTocharians.getNumAvailableBonuses(con.iIncense)
				bSilk = pTocharians.getNumAvailableBonuses(con.iSilk)
				aHelp.append(self.getIcon(bIncense) + 'Incense, ' + self.getIcon(bSilk) + 'Silk')
			elif iGoal == 2:
				aHelp.append(self.getIcon(sd.getNumTocharianConversions() >= 5) + 'Successful conversions: ' + str(sd.getNumTocharianConversions()) + ' / 5')
		
		elif iPlayer == iBactria:
			if iGoal == 0:
				bComplete = False
				if sd.getGoal(iBactria, 0) == 1: bComplete = True
				aHelp.append(self.getIcon(bComplete) + 'Palace and Royal Mint built in Taxila')
			elif iGoal == 1:
				iCount = 0
				regionList = [con.rGandhara, con.rSindh, con.rPunjab, con.rAvanti, con.rMagadha, con.rDeccan, con.rKerala, con.rSaurashtra, con.rTamilNadu]
				for regionID in regionList:
					if utils.checkRegionControl(iBactria, regionID):
						iCount += 1
				aHelp.append(self.getIcon(iCount >= 3) + 'Indian provinces controlled: ' + str(iCount) + ' / 3')
			elif iGoal == 2:
				iCities = 0
				iGreatPriest = gc.getInfoTypeForString("SPECIALIST_GREAT_PRIEST")
				iGreatScientist = gc.getInfoTypeForString("SPECIALIST_GREAT_SCIENTIST")
				apCityList = PyPlayer(iBactria).getCityList()
				for pCity in apCityList:
					if pCity.GetCy().isHasReligion(con.iBuddhism) and pCity.GetCy().isHasReligion(con.iHellenism):
						if (pCity.getFreeSpecialistCount(iGreatPriest) >= 1) or (pCity.getFreeSpecialistCount(iGreatScientist) >= 1):
							iCities += 1
				aHelp.append(self.getIcon(iCities >= 3) + 'Buddhist/Hellenic cities controlled, with great person settled: ' + str(iCities) + ' / 3')
		
		elif iPlayer == iHan:
			if iGoal == 0:
				if sd.get3KingdomsMarker() == 2:
					bHan = utils.checkRegionControl(iQin, con.rHan)
					bWu = utils.checkRegionControl(iQin, con.rWu)
					bQi = utils.checkRegionControl(iQin, con.rQi) 
					bQin = utils.checkRegionControl(iQin, con.rQin) 
					bMinYue = utils.checkRegionControl(iQin, con.rMinYue) 
					bNanYue = utils.checkRegionControl(iQin, con.rNanYue) 
					bShu = utils.checkRegionControl(iQin, con.rShu) 
					bBa = utils.checkRegionControl(iQin, con.rBa)
					bChu = utils.checkRegionControl(iQin, con.rChu)
					bYan = utils.checkRegionControl(iQin, con.rYan)
					bZhao = utils.checkRegionControl(iQin, con.rZhao)
					aHelp.append(self.getIcon(bHan) + 'Han, ' + self.getIcon(bWu) + 'Wu, ' + self.getIcon(bQi) + 'Qi, ' + self.getIcon(bQin) + 'Qin' + self.getIcon(bChu) + 'Chu')
					aHelp.append(self.getIcon(bMinYue) + 'Min Yue, ' + self.getIcon(bNanYue) + 'Nanyue, ' + self.getIcon(bShu) + 'Shu, ' + self.getIcon(bBa) + 'Ba')
					aHelp.append(self.getIcon(bYan) + 'Yan, ' + self.getIcon(bZhao) + 'Zhao')
				else:
					bQin = utils.checkRegionControl(iHan, con.rQin)
					bHan = utils.checkRegionControl(iHan, con.rHan)
					bChu = utils.checkRegionControl(iHan, con.rChu)
					bQi = utils.checkRegionControl(iHan, con.rQi)
					bShu = utils.checkRegionControl(iHan, con.rShu)
					bBa = utils.checkRegionControl(iHan, con.rBa)
					bYan = utils.checkRegionControl(iHan, con.rYan)
					bZhao = utils.checkRegionControl(iHan, con.rZhao)
					bGansu = utils.checkRegionControl(iHan, con.rGansu)
					bTarim = utils.checkRegionControl(iHan, con.rTarim)
					bNanYue = utils.checkRegionControl(iHan, con.rNanYue)
					bMinYue = utils.checkRegionControl(iHan, con.rMinYue)
					aHelp.append(self.getIcon(bQin) + 'Qin, ' + self.getIcon(bHan) + 'Han, ' + self.getIcon(bChu) + 'Chu, ' + self.getIcon(bQi) + 'Qi, ' + self.getIcon(bShu) + 'Shu, ' + self.getIcon(bBa) + 'Ba')
					aHelp.append(self.getIcon(bYan) + 'Yan, ' + self.getIcon(bZhao) + 'Zhao, ' + self.getIcon(bGansu) + 'Gansu, ' + self.getIcon(bTarim) + 'Tarim, ' + self.getIcon(bNanYue) + 'Nan Yue, ' + self.getIcon(bMinYue) + 'Min Yue')
			elif iGoal == 1:
				if sd.get3KingdomsMarker() == 2:
					iCount = self.getNumLuxuries(iHan)
					aHelp.append(self.getIcon(iCount >= 6) + 'Luxury resources: ' + str(iCount) + ' / 6')
				else:
					aHelp.append(self.getIcon(sd.getGoal(iHan, 1) == 1) + 'Paper discovered')
			elif iGoal == 2: 
				if sd.get3KingdomsMarker() == 2:
					aHelp.append(self.getIcon(sd.getGoal(iHan, 2) != 0) + 'Stirrup not yet discovered')
				else:
					iHanPop = gc.getPlayer(iHan).getRealPopulation() / 2
					bHighest = True
					for iLoopCiv in range(con.iNumPlayers):
						if iLoopCiv != iHan:
							if iHanPop < gc.getPlayer(iLoopCiv).getRealPopulation():
								bHighest = False
								iOtherPop = gc.getPlayer(iLoopCiv).getRealPopulation()
								break
					#aHelp.append(self.getIcon(bHighest) + 'Double the population of your nearest rival')
					aHelp.append('Your population: ' + str(iHanPop) + '  Nearest rival: ' + str(iOtherPop))
		
		elif iPlayer == iSatavahana:
			if iGoal == 0:
				iNumShrines = (self.getNumBuildings(iSatavahana, con.iJainShrine) + self.getNumBuildings(iSatavahana, con.iHinduShrine) + self.getNumBuildings(iSatavahana, con.iBuddhistShrine) + self.getNumBuildings(iSatavahana, con.iZoroastrianShrine) + self.getNumBuildings(iSatavahana, con.iJewishShrine) + self.getNumBuildings(iSatavahana, con.iTaoistShrine) + self.getNumBuildings(iSatavahana, con.iConfucianShrine) + self.getNumBuildings(iSatavahana, con.iChristianShrine) + self.getNumBuildings(iSatavahana, con.iManicheanShrine) + self.getNumBuildings(iSatavahana, con.iIslamicShrine) + self.getNumBuildings(iSatavahana, con.iHellenicShrine))
				aHelp.append(self.getIcon(iNumShrines >= 2) + 'Shrines: ' + str(iNumShrines) + ' / 2')
			elif iGoal == 1:
				iCount = pSatavahana.countTotalCulture()
				aHelp.append(self.getIcon(iCount >= 15000) + 'Total Culture: ' + str(iCount) + ' / 15,000')
			elif iGoal == 2:
				aHelp.append(self.getIcon(sd.getNumSatavahanaHinduConversions() >= 3) + 'Successful Hindu conversions: ' + str(sd.getNumSatavahanaHinduConversions()) + ' / 3')
				aHelp.append(self.getIcon(sd.getNumSatavahanaBuddhistConversions() >= 3) + 'Successful Buddhist conversions: ' + str(sd.getNumSatavahanaBuddhistConversions()) + ' / 3')
		
		elif iPlayer == iArmenia:
			if iGoal == 0:
				bArmenia = utils.checkRegionControl(iArmenia, con.rArmenia)
				bCaucasus = utils.checkRegionControl(iArmenia, con.rCaucasus)
				bSyria = utils.checkRegionControl(iArmenia, con.rSyria)
				bCappadocia = utils.checkRegionControl(iArmenia, con.rCappadocia)
				bMedia = utils.checkRegionControl(iArmenia, con.rMedia)
				aHelp.append(self.getIcon(bArmenia) + 'Armenia, ' + self.getIcon(bCaucasus) + 'Caucasus, ' + self.getIcon(bCappadocia) + 'Cappadocia, ' + self.getIcon(bSyria) + 'Syria ' + self.getIcon(bMedia) + 'Media')
			elif iGoal == 1: 
				bComplete = False
				if sd.getGoal(iArmenia, 0) == 1: bComplete = True
				aHelp.append(self.getIcon(bComplete) + 'First to convert to Christianity')
			elif iGoal == 2:
				aHelp.append(self.getIcon(sd.getGoal(iArmenia, 2) != 0) + 'No cities lost')
				
		elif iPlayer == iMaccabees:
			if iGoal == 0:
				aHelp.append(self.getIcon(sd.getWondersBuilt(iMaccabees) >= 4) + 'Jewish cities captured and held: ' + str(sd.getWondersBuilt(iMaccabees)) + ' / 4')
			elif iGoal == 1:
				aHelp.append(self.getIcon(sd.getGoal(iMaccabees, 1) == 1) + 'Temple of Solomon built')
			elif iGoal == 2:
				iNumAliveCivs = 0
				iNumAliveCivsWithJudaism = 0
				for iLoopCiv in range(iNumPlayers):
					if gc.getPlayer(iLoopCiv).isAlive():
						iNumAliveCivs += 1
					cityList = PyPlayer(iLoopCiv).getCityList()
					for pCity in cityList:
						if pCity.GetCy().isHasReligion(con.iJudaism):
							iNumAliveCivsWithJudaism += 1
							break
				iNumTotalCities = 0
				iNumCitiesWithJudaism = 0
				for iLoopCiv in range(iNumTotalPlayers):
					iNumTotalCities += gc.getPlayer(iLoopCiv).getNumCities()
					cityList = PyPlayer(iLoopCiv).getCityList()
					for pCity in cityList:
						if pCity.GetCy().isHasReligion(con.iJudaism):
							iNumCitiesWithJudaism += 1
				bSuccessCivs = false
				if iNumAliveCivsWithJudaism * 2 >= iNumAliveCivs:
					bSuccessCivs = true
				bSuccessCities = false
				if iNumCitiesWithJudaism * 3 >= iNumTotalCities:
					bSuccessCities = true
				aHelp.append(self.getIcon(bSuccessCivs) + 'Judaism spread to half of civilizations' + self.getIcon(bSuccessCities) + 'Judaism spread to one third of cities')
		
		elif iPlayer == iParthia:
			if iGoal == 0:
				totalLand = gc.getMap().getLandPlots()
				ownedLand = pParthia.getTotalLand()
				if totalLand > 0:
					landPercent = (ownedLand * 100.0) / totalLand
				else:
					landPercent = 0.0
				aHelp.append(self.getIcon(landPercent >= 4.995) + 'Land Area: ' + u"%.2f" % landPercent + '% / 5%')
			elif iGoal == 1:
				aHelp.append(self.getIcon(sd.getGoal(iParthia, 1) == 1) + 'Palace and National Epic built in Ctesiphon')
			elif iGoal == 2:
				aHelp.append(self.getIcon(sd.getNumParthianKills() >= 20) + 'Roman units killed: ' + str(sd.getNumParthianKills()) + ' / 20')
		
		elif iPlayer == iDacia:
			if iGoal == 0: 
				bDacia = utils.checkRegionControl(iDacia, con.rDacia)
				bThrace = utils.checkRegionControl(iDacia, con.rThrace)
				bIllyricum = utils.checkRegionControl(iDacia, con.rIllyricum)
				aHelp.append(self.getIcon(bDacia) + 'Dacia, ' + self.getIcon(bThrace) + 'Thrace, ' + self.getIcon(bIllyricum) + 'Illyricum')
			elif iGoal == 1:
				aHelp.append(self.getIcon(pDacia.getGold() >= 5000 * (gc.getGame().getGameSpeedType() + 2) / 2) + 'Gold: ' + str(pDacia.getGold()) + ' / ' + str(5000 * (gc.getGame().getGameSpeedType() + 2) / 2))
			elif iGoal == 2:
				iCount = self.getNumProvinces(iDacia)
				aHelp.append(self.getIcon(iCount >= 6) + 'Provinces controlled: ' + str(iCount) + ' / 6')
 		
		elif iPlayer == iGoguryeo:
			if iGoal == 0: 
				bComplete = False
				if sd.getGoal(iGoguryeo, 0) == 1: bComplete = True
				aHelp.append(self.getIcon(bComplete) + 'First East Asian civ to convert to Buddhism')
			elif iGoal == 1:
				iCount = self.getNumProvinces(iGoguryeo)
				aHelp.append(self.getIcon(iCount >= 6) + 'Provinces controlled: ' + str(iCount) + ' / 6')
			elif iGoal == 2:
				aHelp.append(self.getIcon(self.isTopCulture(iGoguryeo)) + 'Highest Culture')
		
		elif iPlayer == iKushans:
			if iGoal == 0:
				iCount = sd.getWondersBuilt(iKushans)
				aHelp.append(self.getIcon(iCount >= 5) + 'Trade buildings built: ' + str(iCount) + ' /5')
			elif iGoal == 1: 
				iKushanCulture = gc.getPlayer(iPlayer).countTotalCulture()
				iRivalCulture = 0
				for iPlayerLoop in range(con.iNumPlayers):
					if gc.getPlayer(iPlayerLoop).isAlive() and iPlayerLoop != iPlayer:
						if gc.getPlayer(iPlayerLoop).countTotalCulture() > iRivalCulture:
							iRivalCulture = gc.getPlayer(iPlayerLoop).countTotalCulture()
				aHelp.append(self.getIcon(self.isTopCulture(iKushans)) + 'Highest Culture')
				aHelp.append("Kushan culture: " + str(iKushanCulture) + " Highest rival culture: " + str(iRivalCulture))
			elif iGoal == 2:
				iKushanLand = pKushans.getTotalLand()
				iOtherLand = 0
				bLargest = True
				iLargestCiv = -1
				for iCiv in range(iNumPlayers):
					if iCiv != iKushans:
						if (gc.getPlayer(iCiv).getTotalLand() > iKushanLand):
							bLargest = False
							if (gc.getPlayer(iCiv).getTotalLand() > iOtherLand):
								iOtherLand = gc.getPlayer(iCiv).getTotalLand()
								iLargestCiv = iCiv
				if not bLargest:
					aHelp.append(self.getIcon(bLargest) + 'Largest empire: ' + PyPlayer(iLargestCiv).getCivilizationName())
				else:
					aHelp.append(self.getIcon(bLargest) + 'Largest empire')
		
		elif iPlayer == iAxum:
			if iGoal == 0: 
				bComplete = False
				if sd.getGoal(iAxum, 0) ==1: bComplete = True
				aHelp.append(self.getIcon(bComplete) + 'State Religion')
			elif iGoal == 1:
				iRank = 0
				for i in range (iNumPlayers):
					if gc.getGame().getRankTeam(i) == pAxum.getTeam():
						iRank = i + 1
						break
				if i == 1:
					aHelp.append('Rank by score: ' + str(iRank) + 'st')
				elif i == 2:
					aHelp.append('Rank by score: ' + str(iRank) + 'nd')
				else:
					aHelp.append('Rank by score: ' + str(iRank) + 'th')
			elif iGoal == 2:
				iGold = self.getAxumTradeGold()
				aHelp.append(self.getIcon(iGold >= 3000 * (gc.getGame().getGameSpeedType() + 2) / 2) + 'Gold from trade: ' + str(iGold) + ' / ' + str(3000 * (gc.getGame().getGameSpeedType() + 2) / 2))
		
		
		elif iPlayer == iFunan:
			if iGoal == 0: 
				bCropRotation = gc.getTeam(pFunan.getTeam()).isHasTech(con.iCropRotation)
				bMonasticism = gc.getTeam(pFunan.getTeam()).isHasTech(con.iMonasticism)
				aHelp.append(self.getIcon(bCropRotation) + 'Crop Rotation, ' + self.getIcon(bMonasticism) + 'Monasticism')
			elif iGoal == 1:
				iNumBuildings = sd.getWondersBuilt(iFunan)
				aHelp.append(self.getIcon(iNumBuildings >= 6) + 'Hindu or Buddhist buildings: ' + str(iNumBuildings) + ' / 6')
			elif iGoal == 2:
				aHelp.append(self.getIcon(sd.getGoal(iFunan, 2) == 1) + 'Funan province covered')
		
		elif iPlayer == iSassanids:
			if iGoal == 0:
				iNumBuildings = sd.getWondersBuilt(iSassanids)
				aHelp.append(self.getIcon(iNumBuildings >= 3) + 'Zoroastrian Cathedrals: ' + str(iNumBuildings) + ' / 3')
			elif iGoal == 1:
				bArmenia = utils.checkRegionControl(iSassanids, con.rArmenia)
				bPersia = utils.checkRegionControl(iSassanids, con.rPersia)
				bAsia = utils.checkRegionControl(iSassanids, con.rAsia)
				bSyria = utils.checkRegionControl(iSassanids, con.rSyria)
				bJudea = utils.checkRegionControl(iSassanids, con.rJudea)
				bMedia = utils.checkRegionControl(iSassanids, con.rMedia)
				bArachosia = utils.checkRegionControl(iSassanids, con.rArachosia)
				bMesopotamia = utils.checkRegionControl(iSassanids, con.rMesopotamia)
				bEgypt = utils.checkRegionControl(iSassanids, con.rEgypt)
				bParthia = utils.checkRegionControl(iSassanids, con.rParthia)
				bMargiana = utils.checkRegionControl(iSassanids, con.rMargiana)
				bBactria = utils.checkRegionControl(iSassanids, con.rBactria)
				bSogdiana = utils.checkRegionControl(iSassanids, con.rSogdiana)
				bCappadocia = utils.checkRegionControl(iSassanids, con.rCappadocia)
				bPontus = utils.checkRegionControl(iSassanids, con.rPontus)
				bGandhara = utils.checkRegionControl(iSassanids, con.rGandhara)
				bCaucasus = utils.checkRegionControl(iSassanids, con.rCaucasus)
				aHelp.append(self.getIcon(bArmenia) + 'Armenia, ' + self.getIcon(bPersia) + 'Persia, ' + self.getIcon(bAsia) + 'Asia, ' + self.getIcon(bSyria) + 'Syria, ' + self.getIcon(bJudea) + 'Judea, ' + self.getIcon(bCappadocia) + 'Cappadocia, ' + self.getIcon(bPontus) + 'Pontus, ' + self.getIcon(bMedia) + 'Media')
				aHelp.append(self.getIcon(bArachosia) + 'Arachosia, ' + self.getIcon(bMesopotamia) + 'Mesopotamia, ' + self.getIcon(bEgypt) + 'Egypt, ' + self.getIcon(bParthia) + 'Parthia, ' + self.getIcon(bMargiana) + 'Margiana, ' +self.getIcon(bBactria) + 'Bactria, ' + self.getIcon(bSogdiana) + 'Sogdiana')
				aHelp.append(self.getIcon(bGandhara) + 'Gandhara, ' + self.getIcon(bCaucasus) + 'Caucasus')
			elif iGoal == 2:
				aHelp.append(self.getIcon(self.isHasLegendaryCity(iSassanids)) + 'Cities with Legendary Culture: 0 / 1')
		
		elif iPlayer == iYamato:
			if iGoal == 0: 
				bYamato = utils.checkRegionControl(iYamato, con.rYamato)
				bEmishi = utils.checkRegionControl(iYamato, con.rEmishi)
				aHelp.append(self.getIcon(bYamato) + 'Yamato, ' + self.getIcon(bEmishi) + 'Emishi')
			elif iGoal == 1:
				iCount = self.getNumProvinces(iYamato)
				aHelp.append(self.getIcon(iCount >= 5) + 'Provinces controlled: ' + str(iCount) + ' / 5')
			elif iGoal == 2:
				bPaper = gc.getTeam(pYamato.getTeam()).isHasTech(con.iPaper)
				bSteelWorking = gc.getTeam(pYamato.getTeam()).isHasTech(con.iSteelWorking)
				aHelp.append(self.getIcon(bPaper) + 'Paper, ' + self.getIcon(bSteelWorking) + 'Steel Working')
		
		elif iPlayer == iJin:
			if iGoal == 0: 
				bHan = utils.checkRegionControl(iQin, con.rHan)
				bWu = utils.checkRegionControl(iQin, con.rWu)
				bQi = utils.checkRegionControl(iQin, con.rQi) 
				bQin = utils.checkRegionControl(iQin, con.rQin) 
				bMinYue = utils.checkRegionControl(iQin, con.rMinYue) 
				bNanYue = utils.checkRegionControl(iQin, con.rNanYue) 
				bShu = utils.checkRegionControl(iQin, con.rShu) 
				bBa = utils.checkRegionControl(iQin, con.rBa)
				bChu = utils.checkRegionControl(iQin, con.rChu)
				bYan = utils.checkRegionControl(iQin, con.rYan)
				bZhao = utils.checkRegionControl(iQin, con.rZhao)
				aHelp.append(self.getIcon(bHan) + 'Han, ' + self.getIcon(bWu) + 'Wu, ' + self.getIcon(bQi) + 'Qi, ' + self.getIcon(bQin) + 'Qin' + self.getIcon(bChu) + 'Chu')
				aHelp.append(self.getIcon(bMinYue) + 'Min Yue, ' + self.getIcon(bNanYue) + 'Nanyue, ' + self.getIcon(bShu) + 'Shu, ' + self.getIcon(bBa) + 'Ba')
				aHelp.append(self.getIcon(bYan) + 'Yan, ' + self.getIcon(bZhao) + 'Zhao')
			elif iGoal == 1:
				iCount = self.getNumLuxuries(iJin)
				aHelp.append(self.getIcon(iCount >= 6) + 'Luxury resources: ' + str(iCount) + ' / 6')
			elif iGoal == 2:
				aHelp.append(self.getIcon(sd.getGoal(iJin, 2) != 0) + 'Stirrup not yet discovered')
				
		elif iPlayer == iByzantines:
			if iGoal == 0: 
				bThrace = utils.checkRegionControl(iByzantines, con.rThrace, True)
				bGreece = utils.checkRegionControl(iByzantines, con.rGreece, True)
				bAsia = utils.checkRegionControl(iByzantines, con.rAsia, True)
				bSyria = utils.checkRegionControl(iByzantines, con.rSyria, True)
				bJudea = utils.checkRegionControl(iByzantines, con.rJudea, True)
				bEgypt = utils.checkRegionControl(iByzantines, con.rEgypt, True)
				bLibya = utils.checkRegionControl(iByzantines, con.rLibya, True)
				bAfrica = utils.checkRegionControl(iByzantines, con.rAfrica, True)
				bSicily = utils.checkRegionControl(iByzantines, con.rSicily, True)
				bSItaly = utils.checkRegionControl(iByzantines, con.rSItaly, True)
				bCappadocia = utils.checkRegionControl(iByzantines, con.rCappadocia, True)
				bPontus = utils.checkRegionControl(iByzantines, con.rPontus, True)
				bNItaly = utils.checkRegionControl(iByzantines, con.rNItaly, True)
				bIllyricum = utils.checkRegionControl(iByzantines, con.rIllyricum, True)
				bBaetica = utils.checkRegionControl(iByzantines, con.rBaetica, True)
				aHelp.append(self.getIcon(bThrace) + 'Thrace, ' + self.getIcon(bGreece) + 'Greece, ' + self.getIcon(bAsia) + 'Asia, ' + self.getIcon(bSyria) + 'Syria, ' + self.getIcon(bJudea) + 'Judea, ' + self.getIcon(bEgypt) + 'Egypt, ' + self.getIcon(bLibya) + 'Libya, ' + self.getIcon(bAfrica) + 'Africa')
				aHelp.append(self.getIcon(bSicily) + 'Sicily, ' + self.getIcon(bSItaly) + 'Southern Italy, ' + self.getIcon(bCappadocia) + 'Cappadocia, '+ self.getIcon(bPontus) + 'Pontus, ' + self.getIcon(bNItaly) + 'Northern Italy, ' + self.getIcon(bIllyricum) + 'Illyricum, '+ self.getIcon(bBaetica) + 'Baetica')
			elif iGoal == 1: 
				bNoHeresy = True
				iCatholic = 0
				for iLoopPlayer in range(iNumPlayers):
					pLoopPlayer = gc.getPlayer(iLoopPlayer)
					if pLoopPlayer.isAlive():
						if pLoopPlayer.getStateReligion() == con.iCatholicism:
							iCatholic += 1
						elif pLoopPlayer.getStateReligion() in [con.iArianism, con.iMonophysitism, con.iNestorianism]:
							bNoHeresy = False
				aHelp.append(self.getIcon(bNoHeresy) + 'No heretical civs          ' + 'Catholic civs: ' + str(iCatholic) + ' / 5' )
			elif iGoal == 2: 
				aHelp.append(self.getIcon(self.isTopCityPopulation(iByzantines, con.tConstantinople)) + 'Constantinople ranked first in Population, ' + self.getIcon(self.isTopCityCulture(iByzantines, con.tConstantinople)) + 'Constantinople ranked first in Culture')
		
		elif iPlayer == iGupta:
			if iGoal == 0: 
				iCount = sd.getGuptaGoldenAges()
				aHelp.append(self.getIcon(iCount >= 3) + 'Golden Ages: ' + str(iCount) + ' / 3')
			elif iGoal == 1:
				bMagadha = utils.checkRegionControl(iGupta, con.rMagadha, True)
				bBangala = utils.checkRegionControl(iGupta, con.rBangala, True)
				bDeccan = utils.checkRegionControl(iGupta, con.rDeccan, True)
				bKalinka = utils.checkRegionControl(iGupta, con.rKalinka, True)
				bAvanti = utils.checkRegionControl(iGupta, con.rAvanti, True)
				bKerala = utils.checkRegionControl(iGupta, con.rKerala, True)
				bTamilNadu = utils.checkRegionControl(iGupta, con.rTamilNadu, True)
				bPunjab = utils.checkRegionControl(iGupta, con.rPunjab, True)
				bSaurashtra = utils.checkRegionControl(iGupta, con.rSaurashtra, True)
				bGandhara = utils.checkRegionControl(iGupta, con.rGandhara, True)
				bAndhra = utils.checkRegionControl(iGupta, con.rAndhra, True)
				bSindh = utils.checkRegionControl(iGupta, con.rSindh, True)
				aHelp.append(self.getIcon(bMagadha) + 'Magadha, ' + self.getIcon(bBangala) + 'Anga, ' + self.getIcon(bDeccan) + 'Deccan, ' + self.getIcon(bKalinka) + 'Kalinka, ' + self.getIcon(bAvanti) + 'Avanti, ' + self.getIcon(bKerala) + 'Kerala') 
				aHelp.append(self.getIcon(bTamilNadu) + 'Tamil Nadu, ' + self.getIcon(bPunjab) + 'Punjab, ' + self.getIcon(bSaurashtra) + 'Saurashtra, ' + self.getIcon(bGandhara) + 'Gandhara, ' + self.getIcon(bSindh) + 'Sindh, ' + self.getIcon(bAndhra) + 'Andhra')
			elif iGoal == 2:
				bNalanda = self.getNumBuildings(iGupta, con.iNalandaUniversity)
				bStupa = self.getNumBuildings(iGupta, con.iDhamekStupa)
				bPillar = self.getNumBuildings(iGupta, con.iIronPillar)
				aHelp.append(self.getIcon(bNalanda) + 'Nalanda University, ' + self.getIcon(bStupa) + 'Dhamek Stupa, ' + self.getIcon(bPillar) + 'Iron Pillar')
		
		elif iPlayer == iVisigoths:
			if iGoal == 0:
				aHelp.append(self.getIcon(sd.getGoal(iVisigoths, 1) == 1) + 'Jurisprudence discovered')
			elif iGoal == 1:
				bIberia = utils.checkRegionControl(iVisigoths, con.rIberia)
				bLusitania = utils.checkRegionControl(iVisigoths, con.rLusitania)
				bBaetica = utils.checkRegionControl(iVisigoths, con.rBaetica)
				bSeptimania = utils.checkRegionControl(iVisigoths, con.rSeptimania)
				bNItaly = utils.checkRegionControl(iVisigoths, con.rNItaly)
				bSItaly = utils.checkRegionControl(iVisigoths, con.rSItaly)
				bAfrica = utils.checkRegionControl(iVisigoths, con.rAfrica)
				bNumidia = utils.checkRegionControl(iVisigoths, con.rNumidia)
				aHelp.append(self.getIcon(bIberia) + 'Iberia, ' + self.getIcon(bLusitania) + 'Lusitania, ' + self.getIcon(bBaetica) + 'Baetica, ' + self.getIcon(bSeptimania) + 'Narbonensis')
				aHelp.append(self.getIcon(bNItaly) + 'Northern Italy, ' + self.getIcon(bSItaly) + 'Southern Italy, ' + self.getIcon(bAfrica) + 'Africa, ' + self.getIcon(bNumidia) + 'Numidia')
			elif iGoal == 2:
				iCulture = pVisigoths.countTotalCulture()
				bStable = gc.getTeam(pVisigoths.getTeam()).isHasTech(con.iStabilityStable)
				aHelp.append(self.getIcon(iCulture >= 3000) + 'Culture: ' + str(iCulture) + ' / ' + '5000' + self.getIcon(bStable) + 'Stable')
				
		elif iPlayer == iVandals:
			if iGoal == 0:
				bComplete = False
				if sd.getGoal(iVandals, 0) == 1: bComplete = True
				aHelp.append(self.getIcon(bComplete) + 'Rome captured')
			elif iGoal == 1:
				PortList = []
				apCityList = PyPlayer(iVandals).getCityList()
				for pCity in apCityList:
					if pCity.GetCy().isCoastal(gc.getMIN_WATER_SIZE_FOR_OCEAN()):
						PortList.append(pCity)
				aHelp.append(self.getIcon(len (PortList) >= 9) + str(len (PortList)) + ' / ' + str(9))
			elif iGoal == 2:
				aHelp.append(self.getIcon(pVandals.getGold() >= 15000) + 'Gold: ' + str(pVandals.getGold()) + ' / ' + '15000')
				
		elif iPlayer == iOstrogoths:
			if iGoal == 0:
				bComplete = False
				if sd.getGoal(iOstrogoths, 0) == 1: bComplete = True
				aHelp.append(self.getIcon(bComplete) + 'Palace and Royal Mausoleum built in Rome')
			elif iGoal == 1:
				bDacia = utils.checkRegionControl(iOstrogoths, con.rDacia)
				bIllyricum = utils.checkRegionControl(iOstrogoths, con.rIllyricum)
				bNItaly = utils.checkRegionControl(iOstrogoths, con.rNItaly)
				bSItaly = utils.checkRegionControl(iOstrogoths, con.rSItaly)
				bSicily = utils.checkRegionControl(iOstrogoths, con.rSicily)
				aHelp.append(self.getIcon(bDacia) + 'Dacia, ' + self.getIcon(bIllyricum) + 'Illyricum, ' + self.getIcon(bNItaly) + 'Northern Italy, ' + self.getIcon(bSItaly) + 'Southern Italy, ' + self.getIcon(bSicily) + 'Sicily')
			elif iGoal ==2:
				iNumFriends = 0
				for iLoopCiv in range(iNumPlayers):
					if gc.getPlayer(iLoopCiv).AI_getAttitude(iOstrogoths)  >= 4 and gc.getPlayer(iLoopCiv).getStateReligion() in [con.iChristianity, con.iArianism, con.iCatholicism, con.iMonophysitism, con.iNestorianism]:
						iNumFriends += 1
				aHelp.append(self.getIcon(iNumFriends >= 3) + 'Friendly Christian civs: ' + str(iNumFriends) + ' / ' + str(3))
		
		elif iPlayer == iFranks:
			if iGoal == 0: 
				bSuccess = self.isFreeOfIslam([con.rGaul, con.rAquitania, con.rSeptimania, con.rGermania, con.rNItaly, con.rSItaly, con.rIberia, con.rSicily, con.rIllyricum, con.rGreece])
				aHelp.append(self.getIcon(bSuccess) + 'No Islam in Europe')
			elif iGoal == 1:
				bGaul = utils.checkRegionControl(iFranks, con.rGaul)
				bAquitania = utils.checkRegionControl(iFranks, con.rAquitania)
				bSeptimania = utils.checkRegionControl(iFranks, con.rSeptimania)
				bGermania = utils.checkRegionControl(iFranks, con.rGermania)
				bNItaly = utils.checkRegionControl(iFranks, con.rNItaly)
				aHelp.append(self.getIcon(bGaul) + 'Gaul, ' + self.getIcon(bAquitania) + 'Aquitania, ' + self.getIcon(bSeptimania) + 'Narbonensis, ' + self.getIcon(bGermania) + 'Germania, ' + self.getIcon(bNItaly) + 'Northern Italy')
			elif iGoal == 2:
				iNumCathedrals = self.getNumBuildings(iFranks, con.iChristianCathedral)
				iNumMonasteries = self.getNumBuildings(iFranks, con.iChristianMonastery)
				aHelp.append(self.getIcon(iNumCathedrals >= 1) + 'Cathedrals: ' + str(iNumCathedrals) + ' / 1, ' + self.getIcon(iNumMonasteries >= 5) + 'Monasteries: ' + str(iNumMonasteries) + ' / 7')
		
		elif iPlayer == iChalukyans:
			if iGoal == 0: 
				aHelp.append(self.getIcon(self.isTopCulture(iChalukyans)) + 'Highest Culture')
			elif iGoal == 1:
				iNumCathedrals = (self.getNumBuildings(iChalukyans, con.iHinduCathedral)) + (self.getNumBuildings(iChalukyans, con.iBuddhistCathedral)) +(self.getNumBuildings(iChalukyans, con.iJainCathedral))
				aHelp.append(self.getIcon(iNumCathedrals >= 3) + 'Cathedrals built: ' + str(iNumCathedrals) + ' / 3')
			elif iGoal == 2:
				aHelp.append(self.getIcon(self.isTopCityCulture(iChalukyans, con.tVatapi)) + 'Vatapi ranked first in culture')
				
		elif iPlayer == iLombards:
			if iGoal == 0:
				aHelp.append(self.getIcon(sd.getGoal(iLombards, 0) == 1) + 'Great Saint settled in Rome')
			elif iGoal == 1:
				aHelp.append(self.getIcon(sd.getGoal(iLombards, 1) == 1) + '"We Love the King Day" celebrated')
			elif iGoal == 2:
				aHelp.append(self.getIcon(sd.getGoal(iLombards, 2) == 1) + 'National Epic built')
				
		elif iPlayer == iGokturks:
			if iGoal == 0:
				iGokturkLand = pGokturks.getTotalLand()
				bLargest = True
				for iCiv in range(iNumPlayers):
					if (gc.getPlayer(iCiv).getTotalLand() > iGokturkLand):
						bLargest = False
				aHelp.append(self.getIcon(bLargest) + 'Largest empire')
			elif iGoal == 1:
				totalLand = gc.getMap().getLandPlots()
				ownedLand = pGokturks.getTotalLand()
				if totalLand > 0:
					landPercent = (ownedLand * 100.0) / totalLand
				else:
					landPercent = 0.0
				aHelp.append(self.getIcon(landPercent >= 5.995) + 'Land Area: ' + u"%.2f" % landPercent + '% / 7%')
			elif iGoal == 2:
				aHelp.append(self.getIcon(sd.getGoal(iGokturks, 2) != 0) + 'No cities lost')
				
		elif iPlayer == iSrivajaya:
			if iGoal == 0: 
				iCount = pSrivajaya.getNumCities()
				aHelp.append(self.getIcon(iCount >= 7) + 'Cities controlled: ' + str(iCount) + ' / 7')
			elif iGoal == 1:
				iCount = self.getNumLuxuries(iSrivajaya)
				aHelp.append(self.getIcon(iCount >= 11) + 'Luxuries acquired: ' + str(iCount) + ' / 11')
			elif iGoal == 2:
				bSuccess = self.isHighestPopulation(iSrivajaya)
				aHelp.append(self.getIcon(bSuccess) + 'Highest population')
				
		elif iPlayer == iKhazars:
			if iGoal == 0: 
				iCount = self.getNumProvinces(iKhazars)
				aHelp.append(self.getIcon(iCount >= 7) + 'Provinces controlled: ' + str(iCount) + ' / 7')
			elif iGoal == 1:
				bSuccess = True
				cityList = PyPlayer(iKhazars).getCityList()
				for pCity in cityList:
					if not pCity.GetCy().isHasReligion(con.iJudaism):
						bSuccess = False
				aHelp.append(self.getIcon(bSuccess) + 'Judaism in every city')
			elif iGoal == 2:
				iCount = self.getNumOpenBorders(iKhazars)
				aHelp.append(self.getIcon(iCount >= 6) + 'Open Borders agreements: ' + str(iCount) + ' / 6')
				
		elif iPlayer == iTibet:
			if iGoal == 0: 
				bTibet = utils.checkRegionControl(iTibet, con.rTibet)
				bNanzhao = utils.checkRegionControl(iTibet, con.rNanzhao)
				bBirma = utils.checkRegionControl(iTibet, con.rBirma)
				bTarim = utils.checkRegionControl(iTibet, con.rTarim)
				bQinghai = utils.checkRegionControl(iTibet, con.rQinghai)
				aHelp.append(self.getIcon(bTibet) + 'Tibet, ' + self.getIcon(bNanzhao) + 'Nanzhao, ' + self.getIcon(bBirma) + 'Birma,' + self.getIcon(bTarim) + 'Tarim, ' + self.getIcon(bQinghai) + 'Qinghai')
			elif iGoal == 1:
				aHelp.append(self.getIcon(sd.getGoal(iTibet, 1) == 1) + 'Buddhist wonder built')
			elif iGoal == 2:
				bSuccess = True
				for iLoopPlayer in [iGoguryeo, iYamato, iTang, iHan, iVietnam, iFunan, iQin]:
					if gc.getPlayer(iLoopPlayer).getStateReligion() != con.iBuddhism:
						bSuccess = False
						break
				aHelp.append(self.getIcon(bSuccess) + 'All East Asian civs Buddhist')
				
		elif iPlayer == iTang:
			if iGoal == 0: 
				bQin = utils.checkRegionControl(iTang, con.rQin, True)
				bHan = utils.checkRegionControl(iTang, con.rHan, True)
				bChu = utils.checkRegionControl(iTang, con.rChu, True)
				bZhao = utils.checkRegionControl(iTang, con.rZhao, True)
				bYan = utils.checkRegionControl(iTang, con.rYan, True)
				bQi = utils.checkRegionControl(iTang, con.rQi, True)
				bNanYue = utils.checkRegionControl(iTang, con.rNanYue, True)
				bTarim = utils.checkRegionControl(iTang, con.rTarim, True)
				bMinYue = utils.checkRegionControl(iTang, con.rMinYue, True)
				bShu = utils.checkRegionControl(iTang, con.rShu, True)
				bBa = utils.checkRegionControl(iTang, con.rBa, True)
				bGansu = utils.checkRegionControl(iTang, con.rGansu, True)
				bAnnam = utils.checkRegionControl(iTang, con.rAnnam, True)
				bGoguryeo = utils.checkRegionControl(iTang, con.rGoguryeo, True)
				bBuyeo = utils.checkRegionControl(iTang, con.rBuyeo, True)
				aHelp.append(self.getIcon(bQin) + 'Qin, ' + self.getIcon(bHan) + 'Han, ' + self.getIcon(bChu) + 'Chu, ' + self.getIcon(bZhao) + 'Zhao, ' + self.getIcon(bYan) + 'Yan, ' + self.getIcon(bQi) + 'Qi, ' + self.getIcon(bNanYue) + 'NanYue, ' + self.getIcon(bTarim) + 'Tarim')
				aHelp.append(self.getIcon(bMinYue) + 'Min Yue, ' + self.getIcon(bShu) + 'Shu, ' + self.getIcon(bBa) + 'Ba, ' + self.getIcon(bGansu) + 'Gansu, ' + self.getIcon(bAnnam) + 'Annam, ' + self.getIcon(bGoguryeo) + 'Goguryeo, ' + self.getIcon(bBuyeo) + 'Buyeo')
			elif iGoal == 1: 
				iCount = self.getNumVassals(iTang)
				aHelp.append(self.getIcon(iCount >= 2) + 'Vassals: ' + str(iCount) + ' / 2')
			elif iGoal == 2: 
				bPrintingPress = gc.getTeam(pTang.getTeam()).isHasTech(con.iPrintingPress)
				bAlchemy = gc.getTeam(pTang.getTeam()).isHasTech(con.iAlchemy)
				aHelp.append(self.getIcon(bPrintingPress) + 'Printing Press, ' + self.getIcon(bAlchemy) + 'Alchemy')
				
		elif iPlayer == iArabs:
			if iGoal == 0: 
				bArabia = utils.checkRegionControl(iArabs, con.rArabia)
				bJudea = utils.checkRegionControl(iArabs, con.rJudea)
				bSyria = utils.checkRegionControl(iArabs, con.rSyria)
				bMesopotamia = utils.checkRegionControl(iArabs, con.rMesopotamia)
				bMedia = utils.checkRegionControl(iArabs, con.rMedia)
				bPersia = utils.checkRegionControl(iArabs, con.rPersia)
				bEgypt = utils.checkRegionControl(iArabs, con.rEgypt)
				bLibya = utils.checkRegionControl(iArabs, con.rLibya)
				bAfrica = utils.checkRegionControl(iArabs, con.rAfrica)
				bArachosia = utils.checkRegionControl(iArabs, con.rArachosia)
				bMargiana = utils.checkRegionControl(iArabs, con.rMargiana)
				bBactria = utils.checkRegionControl(iArabs, con.rBactria)
				bNumidia = utils.checkRegionControl(iArabs, con.rNumidia)
				bMauretania = utils.checkRegionControl(iArabs, con.rMauretania)
				bBaetica = utils.checkRegionControl(iArabs, con.rBaetica)
				bIberia = utils.checkRegionControl(iArabs, con.rIberia)
				aHelp.append(self.getIcon(bArabia) + 'Arabia, ' + self.getIcon(bJudea) + 'Judea, ' + self.getIcon(bSyria) + 'Syria, ' + self.getIcon(bMesopotamia) + 'Mesopotamia, ' + self.getIcon(bMedia) + 'Media, ' + self.getIcon(bPersia) + 'Persia')
				aHelp.append(self.getIcon(bEgypt) + 'Egypt, ' + self.getIcon(bLibya) + 'Libya, ' + self.getIcon(bAfrica) + 'Africa, ' + self.getIcon(bArachosia) + 'Arachosia, ' + self.getIcon(bMargiana) + 'Margiana, ' + self.getIcon(bNumidia) + 'Numidia, ' + self.getIcon(bBactria) + 'Bactria')
				aHelp.append(self.getIcon(bMauretania) + 'Mauretania, ' + self.getIcon(bBaetica) + 'Baetica, ' + self.getIcon(bIberia) + 'Iberia')
			elif iGoal == 1:
				aHelp.append(self.getIcon(self.isTopTech(iArabs)) + 'Best Techs')
			elif iGoal == 2:
				fPercent = gc.getGame().calculateReligionPercent(con.iIslam)
				aHelp.append(self.getIcon(fPercent >= 30.0) + 'Islam spread to ' + str(fPercent) + '% / 30%')
				
		
		
		return aHelp
		
	def countPlayersByMinAttitude(self, iPlayer, iMinAttitude=4):
		"""Returns the number of players with attitude towards iPlayer being 
		greater or equal to iMinAttitude; The default of 4 is ATTITUDE_FRIENDLY."""
		iCount = 0
		for iLoopPlayer in range(con.iNumPlayers):
			if iLoopPlayer != iPlayer and gc.getPlayer(iLoopPlayer).isAlive():
				if gc.getPlayer(iLoopPlayer).AI_getAttitude(iPlayer) >= iMinAttitude:
					iCount += 1
		return iCount
		
	# from RFCA
	def isContinious(self, xstart, ystart, xtarget, ytarget, istep, iciv):
		plots = gc.getMap().plot(xstart, ystart)
		plott = gc.getMap().plot(xtarget, ytarget)
		if (plots.isCity() and plott.isCity()):
			if (plots.getPlotCity().getOwner() != iciv or plott.getPlotCity().getOwner() != iciv): #those spots should have cities and belong to you.
				return False
		else:
			return False
			
		return self.move (xstart, ystart, xstart, ystart, xtarget, ytarget, istep+1, iciv)
