# Rhye's and Fall Redux - edead

from CvPythonExtensions import *
import CvUtil
import PyHelpers
import Popup
import DynamicCivs
from Consts import *
from StoredData import sd
from RFCUtils import utils
import UnitArtStyler
import RFCCWAIWars

###############
### Globals ###
###############

gc = CyGlobalContext()
localText = CyTranslator()
ArtFileMgr = CyArtFileMgr()
PyPlayer = PyHelpers.PyPlayer
DynamicCivs = DynamicCivs.DynamicCivs()
rfccwaiw = RFCCWAIWars.RFCCWAIWars()

iCheatersPeriod = 12
iBetrayalPeriod = 8
iRebellionDelay = 15

iHuman = utils.getHumanID()

iRand = gc.getGame().getSorenRandNum(5, 'random number')

#save a random number for barb dates 3-18
iRand1 = gc.getGame().getSorenRandNum(5, 'first number') +1
iRand2 = gc.getGame().getSorenRandNum(5, 'second number') +1
iRand3 = gc.getGame().getSorenRandNum(5, 'third number') +1
iRandBellCurve = iRand1 + iRand2 + iRand3

pIndependent = gc.getPlayer(iIndependent)
pIndependent2 = gc.getPlayer(iIndependent2)
pIndependent3 = gc.getPlayer(iIndependent3)
pNomad0 = gc.getPlayer(iNomad0)
pNomad1 = gc.getPlayer(iNomad1)
pNomad2 = gc.getPlayer(iNomad2)
pNomad3 = gc.getPlayer(iNomad3)
pBarbarian = gc.getPlayer(iBarbarian)
pSeleucids = gc.getPlayer(iSeleucids)
pEgypt = gc.getPlayer(iEgypt)
pDacia = gc.getPlayer(iDacia)
pCelts = gc.getPlayer(iCelts)
pCarthage = gc.getPlayer(iCarthage)
pHan = gc.getPlayer(iHan)
pMauryans = gc.getPlayer(iMauryans)
pQin = gc.getPlayer(iQin)
pMaccabees = gc.getPlayer(iMaccabees)
pParthia = gc.getPlayer(iParthia)
pQin = gc.getPlayer(iQin)
pHan = gc.getPlayer(iHan)
pJin = gc.getPlayer(iJin)
pRome = gc.getPlayer(iRome)
pByzantines = gc.getPlayer(iByzantines)
pAntigonids = gc.getPlayer(iAntigonids)
pKalinka = gc.getPlayer(iKalinka)
pPandyans = gc.getPlayer(iPandyans)
pSatavahana = gc.getPlayer(iSatavahana)
pSaba = gc.getPlayer(iSaba)
pFunan = gc.getPlayer(iFunan)
pNubia = gc.getPlayer(iNubia)
pVietnam = gc.getPlayer(iVietnam)

teamIndependent = gc.getTeam(pIndependent.getTeam())
teamIndependent2 = gc.getTeam(pIndependent2.getTeam())
teamIndependent3 = gc.getTeam(pIndependent3.getTeam())
teamBarbarian = gc.getTeam(pBarbarian.getTeam())

bCityRadius = 2


		
# set invasion years
iXiongnuSpawn = (-210 + iRand2)
iXianbeiSpawn = (90 + iRand3)
iNumidianSpawn = (-195 + iRand1)
iSakaInvasion = (-100 + iRand2)
iPallavaSpawn = (190 + iRand3)
iKalabhraSpawn = (195 + iRand1)
iVakatakaSpawn = (210 + iRand3)
iHephthaliteInvasion = (390 + iRand2)
iRouranInvasion = (415 + iRand1)
iLiuSongSpawn = (415 + iRand2)
iHunsInvasion = (425 + iRand2)
iAvarInvasion = (558 + iRand3)
iArabMesopotamiaInvasion = (640 + iRand1)
iArabEgyptInvasion = (650 + iRand2)
iArabAfricaInvasion = (660 + iRand3)
iMoorsInvasion = (705 + iRand1)

class RiseAndFall:


#################################################
### Secure storage & retrieval of script data ###
#################################################

	def getNewCiv( self ):
		return sd.getNewCiv()

	def setNewCiv( self, iNewValue ):
		sd.setNewCiv(iNewValue)

	def getNewCivFlip( self ):
		return sd.getNewCivFlip()

	def setNewCivFlip( self, iNewValue ):
		sd.setNewCivFlip(iNewValue)

	def getOldCivFlip( self ):
		return sd.getOldCivFlip()

	def setOldCivFlip( self, iNewValue ):
		sd.setOldCivFlip(iNewValue)

	def getSpawnWar( self ):
		return sd.getSpawnWar()

	def setSpawnWar( self, iNewValue ):
		sd.setSpawnWar(iNewValue)

	def getAlreadySwitched( self ):
		return sd.getAlreadySwitched()

	def setAlreadySwitched( self, bNewValue ):
		sd.setAlreadySwitched(bNewValue)

	def getNumCities( self, iCiv ):
		return sd.getNumCities(iCiv)

	def setNumCities( self, iCiv, iNewValue ):
		sd.setNumCities(iCiv, iNewValue)

	def getSpawnDelay( self, iCiv ):
		return sd.getSpawnDelay(iCiv)

	def setSpawnDelay( self, iCiv, iNewValue ):
		sd.setSpawnDelay(iCiv, iNewValue)

	def getFlipsDelay( self, iCiv ):
		return sd.getFlipsDelay(iCiv)

	def setFlipsDelay( self, iCiv, iNewValue ):
		sd.setFlipsDelay(iCiv, iNewValue)

	def getBetrayalTurns( self ):
		return sd.getBetrayalTurns()

	def setBetrayalTurns( self, iNewValue ):
		sd.setBetrayalTurns(iNewValue)

	def getLatestFlipTurn( self ):
		return sd.getLatestFlipTurn()

	def setLatestFlipTurn( self, iNewValue ):
		sd.setLatestFlipTurn

	def getLatestRebellionTurn( self, iCiv ):
		return sd.getLatestRebellionTurn

	def setLatestRebellionTurn( self, iCiv, iNewValue ):
		sd.setLatestRebellionTurn

	def getRebelCiv( self ):
		return sd.getRebelCiv()

	def setRebelCiv( self, iNewValue ):
		sd.setRebelCiv(iNewValue)

	def getExileData( self, i ):
		return sd.getExileData(i)

	def setExileData( self, i, iNewValue ):
		sd.setExileData(i, iNewValue)

	def getTempFlippingCity( self ):
		return sd.getTempFlippingCity()

	def setTempFlippingCity( self, tNewValue ):
		sd.setTempFlippingCity(tNewValue)

	def getCheatersCheck( self, i ):
		return sd.getCheatersCheck(i)

	def setCheatersCheck( self, i, iNewValue ):
		sd.setCheatersCheck(i, iNewValue)

	def getDeleteMode( self, i ):
		return sd.getDeleteMode(i)

	def setDeleteMode( self, i, iNewValue ):
		sd.setDeleteMode(i, iNewValue)

	def getCheatMode( self ):
		return sd.getCheatMode()

	def setCheatMode( self, bNewValue ):
		sd.setCheatMode(bNewValue)

	def setCounter(self, iCounterID, iNewValue):
		sd.setCounter(iCounterID, iNewValue)

	def getCounter( self, iCounterID ):
		return sd.getCounter(iCounterID)

	def setTempPlotList( self, lNewList ):
		sd.setTempPlotList(lNewList)

	def getTempPlotList( self ):
		return sd.getTempPlotList()

	def setStopSpawn(self, iCiv, iNewValue):
		sd.setStopSpawn(iCiv, iNewValue)

	def getStopSpawn( self, iCiv ):
		return sd.getStopSpawn(iCiv)

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


	def newCivPopup(self, iCiv):
		self.showPopup(7614, CyTranslator().getText("TXT_KEY_NEWCIV_TITLE", ()), CyTranslator().getText("TXT_KEY_NEWCIV_MESSAGE", (gc.getPlayer(iCiv).getCivilizationDescriptionKey(),)), (CyTranslator().getText("TXT_KEY_POPUP_YES", ()), CyTranslator().getText("TXT_KEY_POPUP_NO", ())))
		self.setNewCiv(iCiv)


	def eventApply7614(self, popupReturn):
		if popupReturn.getButtonClicked() == 0: # 1st button
			iOldHandicap = gc.getActivePlayer().getHandicapType()
			gc.getActivePlayer().setHandicapType(gc.getPlayer(sd.getNewCiv()).getHandicapType())
			gc.getGame().setActivePlayer(sd.getNewCiv(), False)
			gc.getPlayer(sd.getNewCiv()).setHandicapType(iOldHandicap)
			for iMaster in range(iNumPlayers):
				if (gc.getTeam(gc.getPlayer(sd.getNewCiv()).getTeam()).isVassal(iMaster)):
					gc.getTeam(gc.getPlayer(sd.getNewCiv()).getTeam()).setVassal(iMaster, False, False)
			sd.setAlreadySwitched(True)
			gc.getPlayer(sd.getNewCiv()).setPlayable(True)


	# edead: Rhye's function modified to use plot lists
	def flipPopup(self, iNewCiv, plotList):
	
		iHuman = gc.getGame().getActivePlayer()
		flipText = CyTranslator().getText("TXT_KEY_FLIPMESSAGE1", ())
		for i in range(len(plotList)):
			pCurrent = gc.getMap().plot(plotList[i][0], plotList[i][1])
			if (pCurrent.isCity()):
				if (pCurrent.getPlotCity().getOwner() == iHuman):
					if (not (plotList[i] == tCapitals[iHuman]) and not (self.getCheatMode() == True and pCurrent.getPlotCity().isCapital())):
						flipText += (pCurrent.getPlotCity().getName() + "\n")
		flipText += CyTranslator().getText("TXT_KEY_FLIPMESSAGE2", ())
		
		self.showPopup(7615, CyTranslator().getText("TXT_KEY_NEWCIV_TITLE", ()), flipText, (CyTranslator().getText("TXT_KEY_POPUP_YES", ()), CyTranslator().getText("TXT_KEY_POPUP_NO", ())))
		self.setNewCivFlip(iNewCiv)
		self.setOldCivFlip(iHuman)
		self.setTempPlotList(plotList)


	# edead: Rhye's function modified to use plot lists
	def eventApply7615(self, popupReturn):
	
		#iHuman = utils.getHumanID()
		plotList = self.getTempPlotList()
		iNewCivFlip = self.getNewCivFlip()
		
		humanCityList = []
		for i in range(len(plotList)):
			pCurrent = gc.getMap().plot(plotList[i][0], plotList[i][1])
			if (pCurrent.isCity()):
				city = pCurrent.getPlotCity()
				if (city.getOwner() == iHuman):
					if (not (plotList[i] == tCapitals[iHuman]) and not (self.getCheatMode() == True and pCurrent.getPlotCity().isCapital())):
						humanCityList.append(city)
		
		if popupReturn.getButtonClicked() == 0: # 1st button
			#print ("Flip agreed")
			CyInterface().addMessage(iHuman, True, iDuration, CyTranslator().getText("TXT_KEY_FLIP_AGREED", ()), "", 0, "", ColorTypes(iGreen), -1, -1, True, True)
			
			if (len(humanCityList)):
				for i in range(len(humanCityList)):
					city = humanCityList[i]
					#print ("flipping ", city.getName())
					utils.cultureManager((city.getX(), city.getY()), 100, iNewCivFlip, iHuman, False, False, False)
					utils.flipUnitsInCityBefore((city.getX(), city.getY()), iNewCivFlip, iHuman)
					self.setTempFlippingCity((city.getX(), city.getY()))
					utils.flipCity((city.getX(), city.getY()), 0, 0, iNewCivFlip, [iHuman])
					utils.flipUnitsInCityAfter(self.getTempFlippingCity(), iNewCivFlip)
					
					#iEra = gc.getPlayer(iNewCivFlip).getCurrentEra()
					#if (iEra >= 2): #medieval
					#		if (city.getPopulation() < iEra):
					#				city.setPopulation(iEra) #causes an unidentifiable C++ exception
					
					#humanCityList[i].setHasRealBuilding(iPlague, False) #buggy
				
			#same code as Betrayal - done just once to make sure human player doesn't hold a stack just outside of the cities
			for i in range(len(plotList)):
				betrayalPlot = gc.getMap().plot(plotList[i][0], plotList[i][1])
				iNumUnitsInAPlot = betrayalPlot.getNumUnits()
				if (iNumUnitsInAPlot):
					for iJ in range(iNumUnitsInAPlot):
						pUnit = betrayalPlot.getUnit(iJ)
						if (pUnit.getOwner() == iHuman):
							rndNum = gc.getGame().getSorenRandNum(100, 'betrayal')
							if (rndNum >= self.getBetrayalThreshold()):
								if (pUnit.getDomainType() == 2): #land unit
									iUnitType = pUnit.getUnitType()
									pUnit.kill(False, iNewCivFlip)
									utils.makeUnit(iUnitType, iNewCivFlip, (plotList[i][0], plotList[i][1]), 1)
									iJ = iJ - 1
			
			#edead: extra defenders for cases of flip+war
			if gc.getTeam(gc.getPlayer(iHuman).getTeam()).isAtWar(iNewCivFlip):
				apCityList = PyPlayer(iNewCivFlip).getCityList()
				for pCity in apCityList:
					iFreeUnits = 1
					if pCity.GetCy().plot().getNumUnits() < 2: 
						iFreeUnits = 2
					utils.createGarrisons((pCity.getX(), pCity.getY()), iNewCivFlip, iFreeUnits)
								
			if self.getCheatersCheck(0) == 0:
				self.setCheatersCheck(0, iCheatersPeriod)
				self.setCheatersCheck(1, self.getNewCivFlip())
				
		elif popupReturn.getButtonClicked() == 1: # 2nd button
			#print ("Flip disagreed")
			CyInterface().addMessage(iHuman, True, iDuration, CyTranslator().getText("TXT_KEY_FLIP_REFUSED", ()), "", 0, "", ColorTypes(iGreen), -1, -1, True, True)

			if (len(humanCityList)):
				for iI in range(len(humanCityList)):
					city = humanCityList[iI]
					#city.setCulture(self.getNewCivFlip(), city.countTotalCulture(), True)
					pCurrent = gc.getMap().plot(city.getX(), city.getY())
					oldCulture = pCurrent.getCulture(iHuman)
					pCurrent.setCulture(iNewCivFlip, oldCulture/2, True)
					pCurrent.setCulture(iHuman, oldCulture/2, True)
					iWar = self.getSpawnWar() + 1
					self.setSpawnWar(iWar)
					if self.getSpawnWar() == 1:
						#CyInterface().addImmediateMessage(CyTranslator().getText("TXT_KEY_FLIP_REFUSED", ()), "")
						gc.getTeam(gc.getPlayer(iNewCivFlip).getTeam()).declareWar(iHuman, False, -1) ##True??
						#print "war1"
						self.setBetrayalTurns(iBetrayalPeriod)
						self.initBetrayal()


	def rebellionPopup(self, iRebelCiv):
		self.showPopup(7622, CyTranslator().getText("TXT_KEY_REBELLION_TITLE", ()), \
			CyTranslator().getText("TXT_KEY_REBELLION_TEXT", (gc.getPlayer(iRebelCiv).getCivilizationAdjectiveKey(),)), \
			(CyTranslator().getText("TXT_KEY_POPUP_YES", ()), \
			CyTranslator().getText("TXT_KEY_POPUP_NO", ())))


	def eventApply7622(self, popupReturn):
		iRebelCiv = self.getRebelCiv()
		if( popupReturn.getButtonClicked() == 0 ): # 1st button
			gc.getTeam(gc.getPlayer(utils.getHumanID()).getTeam()).makePeace(iRebelCiv)
		elif( popupReturn.getButtonClicked() == 1 ): # 2nd button
			gc.getTeam(gc.getPlayer(utils.getHumanID()).getTeam()).declareWar(iRebelCiv, False, -1)
			
	def romanUHVChoicePopup(self):
		self.showPopup(7627, CyTranslator().getText("TXT_KEY_POPUP_ROMAN_UHV_CHOICE_TITLE", ()), CyTranslator().getText("TXT_KEY_POPUP_ROMAN_UHV_CHOICE_MESSAGE", ()), (CyTranslator().getText("TXT_KEY_POPUP_ROMAN_UHV_CHOICE_EMPIRE", ()), CyTranslator().getText("TXT_KEY_POPUP_ROMAN_UHV_CHOICE_REPUBLIC", ())))
		
	def eventApply7627(self, popupReturn): 
		if popupReturn.getButtonClicked() == 0: # 1st button
			gc.getTeam(gc.getPlayer(utils.getHumanID()).getTeam()).setHasTech(iRomanEmpire, True, utils.getHumanID(), False, False)
		if popupReturn.getButtonClicked() == 1: # 2nd button
			pRome.setCivics(0, iOligarchyCivic)
			return
			
	def threeKingdomsPopup(self):
		self.showPopup(7629, CyTranslator().getText("TXT_KEY_POPUP_3KINGDOMS_CHOICE_TITLE", ()), CyTranslator().getText("TXT_KEY_POPUP_3KINGDOMS_CHOICE_MESSAGE", ()), (CyTranslator().getText("TXT_KEY_POPUP_3KINGDOMS_CHOICE_WEI", ()), CyTranslator().getText("TXT_KEY_POPUP_3KINGDOMS_CHOICE_SHU", ()), CyTranslator().getText("TXT_KEY_POPUP_3KINGDOMS_CHOICE_WU", ())))
			
	def eventApply7629(self, popupReturn): # Three Kingdoms choice
		if popupReturn.getButtonClicked() == 0: # 1st button
			return
		if popupReturn.getButtonClicked() == 1: # 2nd button
			self.do3KingdomsShu()
		if popupReturn.getButtonClicked() == 2: # 2nd button
			self.do3KingdomsWu()
			
	def tamilKingdomsPopup(self):
		self.showPopup(7632, CyTranslator().getText("TXT_KEY_POPUP_TAMIL_CHOICE_TITLE", ()), CyTranslator().getText("TXT_KEY_POPUP_TAMIL_CHOICE_MESSAGE", ()), (CyTranslator().getText("TXT_KEY_POPUP_TAMIL_CHOICE_CHOLAS", ()), CyTranslator().getText("TXT_KEY_POPUP_TAMIL_CHOICE_PANDYANS", ()), CyTranslator().getText("TXT_KEY_POPUP_TAMIL_CHOICE_CHERAS", ())))
			
	def eventApply7632(self, popupReturn): # Tamil Kingdoms choice
		if popupReturn.getButtonClicked() == 0: # 1st button
			self.do3KingdomsChola()
		if popupReturn.getButtonClicked() == 1: # 2nd button
			self.do3KingdomsPandyan()
		if popupReturn.getButtonClicked() == 2: # 2nd button
			self.do3KingdomsChera()


		
#######################################
### Main methods (Event-Triggered) ###
#####################################


	def setup(self):
		
		
		sd.setHordeOf406Year(400 + iRand3)
		
		self.createEarlyStartingUnits()
		for iLoopPlayer in range(iNumPlayers):
			utils.setCivicsStability(iLoopPlayer)
			if gc.getPlayer(iLoopPlayer).getNumCities() >= 1:
				sd.setNumCities(iLoopPlayer, gc.getPlayer(iLoopPlayer).getNumCities())
		for iLoopCiv in [iIndependent, iIndependent2, iIndependent3]:
			gc.getPlayer(iLoopCiv).changeGold(500)
		## set Civilization types for each scenario
		
		if not (gc.getPlayer(iSassanids).isPlayable()): # 550AD
			# Hephthalites
			sd.setCivilization(iNomad2, iHephthalites)
			self.setCivDesc(iNomad2, "Hephthalite Kingdom", "Hephthalites", "Hephthalite", "Mihirakula")
			# Rouran
			sd.setCivilization(iNomad3, iRouran)
			self.setCivDesc(iNomad3, "Rouran Khaganate", "Rouran", "Rouran", "Yujiulu")
			# Jin to Wei
			self.setCivDesc(iJin, "Kingdom of Wei", "Wei", "Wei", "Daowu")
			# Han to Liu Song
			sd.setCivilization(iHan, iSong)
			self.setCivDesc(iHan, "Liu Song Empire", "Liu Song", "Liu Song", "Liu Bei")
			# Saba to Himyarites
			sd.setCivilization(iSaba, iHimyarites)
			self.setCivDesc(iSaba, "Himyarite Kingdom", "Himyar", "Himyarite", "Yusuf As'ar Yath'ar")
			# Kalinka to Pallavas
			sd.setCivilization(iKalinka, iPallavas)
			self.setCivDesc(iKalinka, "Pallava Kingdom", "Pallavas", "Pallava", "Simhavishnu")
			# Pandyans to Kalabhras
			sd.setCivilization(iPandyans, iKalabhras)
			self.setCivDesc(iPandyans, "Kalabhra Kingdom", "Kalabhras", "Kalabhra", "Tiraiyan")
			# Mauryans to Magadha
			sd.setCivilization(iMauryans, iMagadha)
			self.setCivDesc(iMauryans, "Kingdom of Magadha", "Magadha", "Magadhan", "Vasudeva")
			# Vietnamese to Champa
			sd.setCivilization(iVietnam, iChampa)
			self.setCivDesc(iVietnam, "Kingdom of Champa", "Champa", "Champan", "Khu Lien")
			
		elif not (gc.getPlayer(iDacia).isPlayable()): # 220AD
			# Han to Wu
			sd.setCivilization(iHan, iWu)
			self.setCivDesc(iHan, "Kingdom of Wu", "Wu", "Wu", "Sun Quan")
			pHan.AI_changeAttitudeExtra(iQin, -2)
			pHan.AI_changeAttitudeExtra(iJin, -2)
			# Qin to Shu
			sd.setCivilization(iQin, iShu)
			self.setCivDesc(iQin, "Kingdom of Shu", "Shu", "Shu", "Liu Bei")
			pQin.AI_changeAttitudeExtra(iHan, -2)
			pQin.AI_changeAttitudeExtra(iJin, -2)
			# AI Jin
			if not utils.getHumanID() == iJin:
				pJin.AI_changeAttitudeExtra(iQin, -2)
				pJin.AI_changeAttitudeExtra(iHan, -2)
			# Satavahana to Vakataka
			sd.setCivilization(iSatavahana, iVakatakas)
			pSatavahana.setName("Vindhyasakti")
			self.setCivDesc(iSatavahana, "Vakataka Kingdom", "Vakatakas", "Vakatakan", "Vindhyasakti")
			# Pandyans to Kalabhras
			sd.setCivilization(iPandyans, iKalabhras)
			self.setCivDesc(iPandyans, "Kalabhra Kingdom", "Kalabhras", "Kalabhran", "Tiraiyan")
			# Kalinka to Pallavas
			sd.setCivilization(iKalinka, iPallavas)
			self.setCivDesc(iKalinka, "Pallava Kingdom", "Pallavas", "Pallavan", "Simhavishnu")
			# Mauryans to Magadha
			sd.setCivilization(iMauryans, iMagadha)
			pMauryans.setLeader(iPusyamitra)
			pMauryans.setName("Vasudeva")
			self.setCivDesc(iMauryans, "Kingdom of Magadha", "Magadha", "Magadhan", "Vasudeva")
			# Saba to Himyarites
			sd.setCivilization(iSaba, iHimyarites)
			self.setCivDesc(iSaba, "Himyarite Kingdom", "Himyar", "Himyarites", "Yusuf As'ar Yath'ar")
			# Vietnamese to Champa
			sd.setCivilization(iVietnam, iMagadha)
			self.setCivDesc(iVietnam, "Kingdom of Champa", "Champa", "Champan", "Khu Lien")
			
			utils.revealPlots(iJin, utils.getRegionPlotList(lRevealRegions[iJin], True)) 
			
		elif not (gc.getPlayer(iSeleucids).isPlayable()): # 80BC
			# Mauryans to Sungas
			sd.setCivilization(iMauryans, iSungas)
			pMauryans.setLeader(iPusyamitra)
			self.setCivDesc(iMauryans, "Sunga Kingdom", "Sungas", "Sunga", "Pusyamitra")
			# Numidia to Mauretania
			self.setCivDesc(iNomad1, "Kingdom of Mauretania", "Mauretania", "Mauretanian", "Bochhus")
			
		else: # 320BC
			
			if utils.getHumanID() == iQin:
				self.foundCity(iIndependent, "Shouchun", 145, 47, [iTaoism], [])
			
			if not utils.getHumanID() == iAntigonids:
				pAntigonids.AI_changeAttitudeExtra(iEgypt, -2)
				pAntigonids.AI_changeAttitudeExtra(iSeleucids, -2)
			if not utils.getHumanID() == iEgypt:
				pEgypt.AI_changeAttitudeExtra(iAntigonids, -2)
				pEgypt.AI_changeAttitudeExtra(iSeleucids, -2)
			if not utils.getHumanID() == iSeleucids:
				pSeleucids.AI_changeAttitudeExtra(iEgypt, -2)
				pSeleucids.AI_changeAttitudeExtra(iAntigonids, -2)
		
		for iLoopCiv in range(iNumTotalPlayers):
			gc.getPlayer(iLoopCiv).changeGold(tStartingGold[iLoopCiv]) # edead: set starting gold
				
			#utils.revealPlots(iLoopCiv, utils.getRegionPlotList(lRevealRegions[iLoopCiv], True)) 
			
			#if iLoopCiv != utils.getHumanID():
				#utils.revealMap(iLoopCiv) 
				
			
		

			
		# update unit art styles of independents
		for iLoopPlayer in range(iIndependent, iBarbarian):
			unitList = PyPlayer(iLoopPlayer).getUnitList()
			for pUnit in unitList:
				UnitArtStyler.updateUnitArt(pUnit)
				
				
		# 3 Kingdoms
		if utils.getHumanID() == iJin and (gc.getPlayer(iSassanids).isPlayable()) and not (gc.getPlayer(iDacia).isPlayable()):
			self.threeKingdomsPopup()
				
				
		
				
		
			
		# look at starting plot for late civs
		#if iLoopCiv == utils.getHumanID():
			#gc.getMap().plot(tCapitals[iLoopCiv][0], tCapitals[iLoopCiv][1]).cameraLookAt()
			
		
			


	def checkTurn(self, iGameTurn):
	
		print ("RiseAndFall.checkTurn, year=", utils.getYear())
		
		if iGameTurn == getTurnForYear(-320):
			utils.stabilityCheck(iCarthage)
		
		iHuman = utils.getHumanID()
		# update unit art styles of independents
		#for iLoopPlayer in range(iIndependent, iBarbarian):
			#unitList = PyPlayer(iLoopPlayer).getUnitList()
			#for pUnit in unitList:
				#UnitArtStyler.updateUnitArt(pUnit)
		
		#if gc.getPlayer(iGameTurn % iNumPlayers).getNumCities() >= 1 and (sd.getLastRebellion(iGameTurn % iNumPlayers)) < utils.getYear() - 20:
			#print ("periodic Stability Check, iPlayer =", iGameTurn % iNumPlayers)
			#self.stabilityCheck(iGameTurn % iNumPlayers)
		

		
		if (iGameTurn % 20 == 1):
			for iLoopCiv in range(iNumPlayers):
				if gc.getTeam(gc.getPlayer(iLoopCiv).getTeam()).isHasTech(iOverextension):
					utils.secedeDistantCities(iLoopCiv, sd.getCivilization(iLoopCiv))
					gc.getTeam(gc.getPlayer(iLoopCiv).getTeam()).setHasTech(iOverextension, False, iLoopCiv, False, False)
					#if gc.getPlayer(iHuman).canContact(iLoopCiv):
						#CyInterface().addMessage(utils.getHumanID(), False, iDuration, localText.getText("TXT_KEY_SECEDE_DISTANT1", ()) + " " + gc.getPlayer(iLoopCiv).getCivilizationDescription(0) + " " + localText.getText("TXT_KEY_SECEDE_DISTANT2", ()), "", 0, "", ColorTypes(iRed), -1, -1, True, True)
					
		

			
		# non-playable civ spawns, invasions and other events
		

		
		
		if iGameTurn == getTurnForYear(-318):
			# help for AI Qin
			if iHuman != iQin:
				utils.makeUnit(iSpearman, iQin, tCapitals[iQin], 2)
				utils.makeUnit(iQinInfantry, iQin, tCapitals[iQin], 2)
				utils.makeUnit(iCatapult, iQin, tCapitals[iQin], 2)
				
			# help for AI Gojoseon
			if iHuman != iGojoseon:
				utils.makeUnit(iSpearman, iGojoseon, tCapitals[iGojoseon], 1)
				utils.makeUnit(iChosonHorseman, iGojoseon, tCapitals[iGojoseon], 1)
			if iHuman == iQin:
				utils.makeUnit(iSpearman, iGojoseon, tCapitals[iGojoseon], 1)
				utils.makeUnit(iChosonHorseman, iGojoseon, tCapitals[iGojoseon], 1)
				
			# help for AI Seleucids
			if iHuman != iSeleucids:
				utils.makeUnit(iHoplite, iSeleucids, tCapitals[iSeleucids], 1)
				utils.makeUnit(iWarElephant, iSeleucids, tCapitals[iSeleucids], 1)
				
			# help for AI Egypt
			if iHuman != iEgypt:
				utils.makeUnit(iGalatianInfantry, iEgypt, tCapitals[iEgypt], 1)
				
			# help for AI Antigonids
			if iHuman == iSeleucids:
				utils.makeUnit(iAntigonidPeltast, iAntigonids, tCapitals[iAntigonids], 2)
				
		# Nan Yue
		if (getTurnForYear(-210) < iGameTurn < getTurnForYear(-180)) and (iGameTurn %  9 == 0) and not pNomad3.isAlive():
			self.assignTechs(iNomad3, iNanYue)
			self.provinceAttack(iNomad3, iNanYue, [rNanYue, rMinYue])
			CyInterface().addMessage(iHuman, True, iDuration, CyTranslator().getText("TXT_KEY_INDEPENDENCE_TEXT_NANYUE", ()), "", 0, "", ColorTypes(iRed), -1, -1, True, True)
			for iEnemyCiv in lEnemyCivsOnSpawn[iNanYue]:
				if utils.isActive(iEnemyCiv):
					gc.getTeam(pNomad3.getTeam()).declareWar(iEnemyCiv, False, -1)
		
		# Xiongnu
		if iGameTurn == getTurnForYear(iXiongnuSpawn) - 20:
			utils.killAndFragmentCiv(iNomad0, False)
			utils.clearCulture(iNomad0)
			self.createSettlerAndGarrison(iNomad0, tCapitals[iXiongnu], iXiongnu)
		if iGameTurn == getTurnForYear(iXiongnuSpawn):
			sd.setCivilization(iNomad0, iXiongnu)
			pNomad0.setCivilizationType(iXiongnu)
			self.setCivDesc(iNomad0, "Xiongnu Khanate", "Xiongnu", "Xiongnu", "Modu Chanyu")
			self.assignTechs(iNomad0, iXiongnu)
			self.provinceAttack(iNomad0, iXiongnu, [rMongolianSteppe, rGansu, rZhao])
			CyInterface().addMessage(iHuman, True, iDuration, CyTranslator().getText("TXT_KEY_INDEPENDENCE_TEXT_XIONGNU", ()), "", 0, "", ColorTypes(iRed), -1, -1, True, True)
			for iEnemyCiv in lEnemyCivsOnSpawn[iXiongnu]:
				if utils.isActive(iEnemyCiv):
					gc.getTeam(pNomad0.getTeam()).declareWar(iEnemyCiv, False, -1)
		if iGameTurn == getTurnForYear(iXiongnuSpawn) + 10:
			self.provinceAttack(iNomad0, iXiongnu, [rMongolianSteppe, rTarim, rGansu, rYan, rZhao, rQin, rQinghai])
			
		# Sungas
		if getTurnForYear(-200) < iGameTurn < getTurnForYear(-100) and iGameTurn % 8 == 0 and not pMauryans.isAlive() and sd.getCivilization(iMauryans) == iMauryans:
			sd.setCivilization(iMauryans, iSungas)
			pMauryans.setCivilizationType(iSungas)
			pMauryans.setCivics(4, iPaganismCivic)
			pMauryans.setLeader(iPusyamitra)
			self.setCivDesc(iMauryans, "Sunga Kingdom", "Sunga", "Sungas", "Pusyamitra")
			self.assignTechs(iMauryans, iSungas)
			self.provinceAttack(iMauryans, iSungas, [rMagadha])
			CyInterface().addMessage(iHuman, True, iDuration, CyTranslator().getText("TXT_KEY_INDEPENDENCE_TEXT_SUNGAS", ()), "", 0, "", ColorTypes(iRed), -1, -1, True, True)
			for iEnemyCiv in lEnemyCivsOnSpawn[iSungas]:
				if utils.isActive(iEnemyCiv):
					gc.getTeam(pMauryans.getTeam()).declareWar(iEnemyCiv, False, -1)
			

		
		# Numidia
		if iGameTurn == getTurnForYear(iNumidianSpawn):
			self.assignTechs(iNomad1, iNumidia)
			self.provinceAttack(iNomad1, iNumidia, [rNumidia, rMauretania])
			CyInterface().addMessage(iHuman, True, iDuration, CyTranslator().getText("TXT_KEY_INDEPENDENCE_TEXT_NUMIDIA", ()), "", 0, "", ColorTypes(iRed), -1, -1, True, True)
			for iEnemyCiv in lEnemyCivsOnSpawn[iNumidia]:
				if utils.isActive(iEnemyCiv):
					gc.getTeam(pNomad1.getTeam()).declareWar(iEnemyCiv, False, -1)

		# Sakas
		if iGameTurn == getTurnForYear(iSakaInvasion) - 20:
			self.assignTechs(iNomad2, iScythians)
			self.provinceAttack(iNomad2, iScythians, [rArachosia, rSindh])
			CyInterface().addMessage(iHuman, True, iDuration, CyTranslator().getText("TXT_KEY_INDEPENDENCE_TEXT_SCYTHIANS", ()), "", 0, "", ColorTypes(iRed), -1, -1, True, True)
			for iEnemyCiv in lEnemyCivsOnSpawn[iScythians]:
				if utils.isActive(iEnemyCiv):
					gc.getTeam(pNomad2.getTeam()).declareWar(iEnemyCiv, False, -1)
		if iGameTurn == getTurnForYear(iSakaInvasion) + 3:
			self.provinceAttack(iNomad2, iScythians, [rArachosia, rSindh, rPunjab, rSaurashtra])
		
		# Xianbei
		if iGameTurn == getTurnForYear(iXianbeiSpawn) - 20:
			utils.killAndFragmentCiv(iNomad0, False)
			utils.clearCulture(iNomad0)
		if iGameTurn == getTurnForYear(iXianbeiSpawn):
			sd.setCivilization(iNomad0, iXianbei)
			pNomad0.setCivilizationType(iXianbei)
			self.setCivDesc(iNomad0, "Xianbei Khanate", "Xianbei", "Xianbei", "Tanshihuai")
			self.assignTechs(iNomad0, iXianbei)
			self.provinceAttack(iNomad0, iXianbei, [rMongolianSteppe, rTarim, rGansu])
			CyInterface().addMessage(iHuman, True, iDuration, CyTranslator().getText("TXT_KEY_INDEPENDENCE_TEXT_XIANBEI", ()), "", 0, "", ColorTypes(iRed), -1, -1, True, True)
			for iEnemyCiv in lEnemyCivsOnSpawn[iXianbei]:
				if utils.isActive(iEnemyCiv):
					gc.getTeam(pNomad0.getTeam()).declareWar(iEnemyCiv, False, -1)
		if iGameTurn == getTurnForYear(iXianbeiSpawn) + 10:
			self.provinceAttack(iNomad0, iXianbei, [rMongolianSteppe, rTarim, rGansu, rYan, rZhao, rQin, rQinghai])
		
		# Pallavas
		if iGameTurn == getTurnForYear(iPallavaSpawn) - 20:
			if iKalinka != iHuman and not gc.getTeam(pKalinka.getTeam()).isHasTech(iStabilityStable):
				utils.killAndFragmentCiv(iKalinka, False)
				utils.clearCulture(iKalinka)
				sd.setCivilization(iKalinka, iPallavas)
		if iGameTurn == getTurnForYear(iPallavaSpawn) and self.checkUnoccupied([rAndhra], True, True):
			if sd.getCivilization(iKalinka) == iPallavas:
				pKalinka.setCivilizationType(iPallavas)
				self.setCivDesc(iKalinka, "Pallava Kingdom", "Pallavas", "Pallava", "Simhavishnu")
				self.assignTechs(iKalinka, iPallavas)
				self.provinceAttack(iKalinka, iPallavas, [rAndhra, rKalinka])
				CyInterface().addMessage(iHuman, True, iDuration, CyTranslator().getText("TXT_KEY_INDEPENDENCE_TEXT_PALLAVAS", ()), "", 0, "", ColorTypes(iRed), -1, -1, True, True)
				for iEnemyCiv in lEnemyCivsOnSpawn[iPallavas]:
					if utils.isActive(iEnemyCiv):
						gc.getTeam(pKalinka.getTeam()).declareWar(iEnemyCiv, False, -1)
		
		# Kalabhras
		if iGameTurn == getTurnForYear(iKalabhraSpawn) - 20:
			if iPandyans != iHuman and  not gc.getTeam(pPandyans.getTeam()).isHasTech(iStabilityStable):
				utils.killAndFragmentCiv(iPandyans, False)
				utils.clearCulture(iPandyans)
				sd.setCivilization(iPandyans, iKalabhras)
		if iGameTurn == getTurnForYear(iKalabhraSpawn) and self.checkUnoccupied([rTamilNadu], True, True):
			if sd.getCivilization(iPandyans) == iKalabhras:
				pPandyans.setCivilizationType(iKalabhras)
				self.setCivDesc(iPandyans, "Kalabhra Kingdom", "Kalabhras", "Kalabhra", "Tiraiyan")
				self.assignTechs(iPandyans, iKalabhras)
				self.provinceAttack(iPandyans, iKalabhras, [rTamilNadu])
				CyInterface().addMessage(iHuman, True, iDuration, CyTranslator().getText("TXT_KEY_INDEPENDENCE_TEXT_KALABHRAS", ()), "", 0, "", ColorTypes(iRed), -1, -1, True, True)
				for iEnemyCiv in lEnemyCivsOnSpawn[iKalabhras]:
					if utils.isActive(iEnemyCiv):
						gc.getTeam(pPandyans.getTeam()).declareWar(iEnemyCiv, False, -1)
		
		# Champa
		if iGameTurn == getTurnForYear(190) - 20:
			if iVietnam != iHuman and  not gc.getTeam(pVietnam.getTeam()).isHasTech(iStabilityStable):
				utils.killAndFragmentCiv(iVietnam, False)
				utils.clearCulture(iVietnam)
				sd.setCivilization(iVietnam, iChampa)
		if iGameTurn == getTurnForYear(190):
			if sd.getCivilization(iVietnam) == iChampa:
				pVietnam.setCivilizationType(iChampa)
				self.setCivDesc(iVietnam, "Kingdom of Champa", "Champa", "Champan", "Khu Lien")
				self.assignTechs(iVietnam, iChampa)
				self.provinceAttack(iVietnam, iChampa, [rChampa])
				#CyInterface().addMessage(iHuman, True, iDuration, CyTranslator().getText("TXT_KEY_INDEPENDENCE_TEXT_CHAMPA", ()), "", 0, "", ColorTypes(iRed), -1, -1, True, True)
				for iEnemyCiv in lEnemyCivsOnSpawn[iChampa]:
					if utils.isActive(iEnemyCiv):
						gc.getTeam(pVietnam.getTeam()).declareWar(iEnemyCiv, False, -1)
		
		# Vakatakas
		if iGameTurn == getTurnForYear(iVakatakaSpawn) - 20:
			if iSatavahana != iHuman and  not gc.getTeam(pSatavahana.getTeam()).isHasTech(iStabilityStable):
				utils.killAndFragmentCiv(iSatavahana, False)
				utils.clearCulture(iSatavahana)
				sd.setCivilization(iSatavahana, iVakatakas)
		if iGameTurn == getTurnForYear(iVakatakaSpawn):
			if sd.getCivilization(iSatavahana) == iVakatakas:
				pSatavahana.setCivilizationType(iVakatakas)
				self.setCivDesc(iSatavahana, "Vakataka Kingdom", "Vakatakas", "Vakataka", "Vindhyasakti")
				self.assignTechs(iSatavahana, iVakatakas)
				self.provinceAttack(iSatavahana, iVakatakas, [rDeccan, rAvanti])
				CyInterface().addMessage(iHuman, True, iDuration, CyTranslator().getText("TXT_KEY_INDEPENDENCE_TEXT_VAKATAKAS", ()), "", 0, "", ColorTypes(iRed), -1, -1, True, True)
				for iEnemyCiv in lEnemyCivsOnSpawn[iVakatakas]:
					if utils.isActive(iEnemyCiv):
						gc.getTeam(pSatavahana.getTeam()).declareWar(iEnemyCiv, False, -1)
		
		# Liu Song
		if iGameTurn == getTurnForYear(iLiuSongSpawn) - 20:
			if iHan != iHuman and not gc.getTeam(pHan.getTeam()).isHasTech(iStabilityStable):
				utils.killAndFragmentCiv(iHan, False)
				utils.clearCulture(iHan)
				sd.setCivilization(iHan, iSong)
		if iGameTurn == getTurnForYear(iLiuSongSpawn):
			if sd.getCivilization(iHan) == iSong:
				pHan.setCivilizationType(iSong)
				self.setCivDesc(iHan, "Liu Song Empire", "Liu Song", "Liu Song", "Wen")
				self.assignTechs(iHan, iSong)
				sd.setFlipsDelay(iHan, 0)
				self.birthConditional(iHan, (148, 47), utils.getCorePlotList(iSong))
				CyInterface().addMessage(iHuman, True, iDuration, CyTranslator().getText("TXT_KEY_INDEPENDENCE_TEXT_SONG", ()), "", 0, "", ColorTypes(iRed), -1, -1, True, True)
				for iEnemyCiv in lEnemyCivsOnSpawn[iSong]:
					if utils.isActive(iEnemyCiv):
						gc.getTeam(pHan.getTeam()).declareWar(iEnemyCiv, False, -1)
		if iGameTurn == getTurnForYear(iLiuSongSpawn) + 1 and sd.getCivilization(iHan) == iSong:
			self.birthConditional(iHan, (148, 47), utils.getCorePlotList(iSong))
		if iGameTurn == getTurnForYear(iLiuSongSpawn) + 5:
			self.provinceAttack(iHan, iSong, [rMinYue, rNanYue])
		
		# Hephthalites
		if iGameTurn == getTurnForYear(iHephthaliteInvasion) - 20:
			utils.killAndFragmentCiv(iNomad2, False)
			utils.clearCulture(iNomad2)
		if iGameTurn == getTurnForYear(iHephthaliteInvasion):
			sd.setCivilization(iNomad2, iHephthalites)
			pNomad2.setCivilizationType(iHephthalites)
			self.setCivDesc(iNomad2, "Hephthalite Kingdom", "Hephthalites", "Hephthalite", "Mihirakula")
			self.assignTechs(iNomad2, iHephthalites)
			self.provinceAttack(iNomad2, iHephthalites, [rSogdiana, rMargiana, rBactria, rArachosia])
			CyInterface().addMessage(iHuman, True, iDuration, CyTranslator().getText("TXT_KEY_INDEPENDENCE_TEXT_HEPHTHALITES", ()), "", 0, "", ColorTypes(iRed), -1, -1, True, True)
			for iEnemyCiv in lEnemyCivsOnSpawn[iHephthalites]:
				if utils.isActive(iEnemyCiv):
					gc.getTeam(pNomad2.getTeam()).declareWar(iEnemyCiv, False, -1)
		if iGameTurn == getTurnForYear(iHephthaliteInvasion) + 10:
			self.provinceAttack(iNomad2, iHephthalites, [rGandhara, rPunjab, rSindh])
			
		# Rouran
		if iGameTurn == getTurnForYear(iRouranInvasion) - 20:
			if pNomad3.isAlive():
				utils.killAndFragmentCiv(iNomad3, False)
			utils.clearCulture(iNomad3)
		if iGameTurn == getTurnForYear(iRouranInvasion):
			sd.setCivilization(iNomad3, iRouran)
			pNomad3.setCivilizationType(iRouran)
			pNomad3.setLeader(iRouranLeader)
			self.setCivDesc(iNomad3, "Rouran Khaganate", "Rouran", "Rouran", "Yujiulu")
			self.assignTechs(iNomad3, iRouran)
			self.provinceAttack(iNomad3, iRouran, [rTarim, rGansu, rMongolianSteppe])
			CyInterface().addMessage(iHuman, True, iDuration, CyTranslator().getText("TXT_KEY_INDEPENDENCE_TEXT_ROURAN", ()), "", 0, "", ColorTypes(iRed), -1, -1, True, True)
			for iEnemyCiv in lEnemyCivsOnSpawn[iRouran]:
				if utils.isActive(iEnemyCiv):
					gc.getTeam(pNomad3.getTeam()).declareWar(iEnemyCiv, False, -1)
		if iGameTurn == getTurnForYear(iRouranInvasion) + 5:
			self.provinceAttack(iNomad3, iRouran, [rQin, rZhao])
		
		# Huns
		if iGameTurn == getTurnForYear(iHunsInvasion) - 20:
			if pNomad0.isAlive():
				utils.killAndFragmentCiv(iNomad0, False)
			utils.clearCulture(iNomad0)
		if iGameTurn == getTurnForYear(iHunsInvasion):
			sd.setCivilization(iNomad0, iHuns)
			pNomad0.setCivilizationType(iHuns)
			pNomad0.setLeader(iRouranLeader)
			self.setCivDesc(iNomad0, "Hun Empire", "Huns", "Hun", "Atilla")
			self.assignTechs(iNomad0, iHuns)
			self.provinceAttack(iNomad0, iHuns, [rDacia, rScythianSteppe, rCrimea, rCaucasus])
			CyInterface().addMessage(iHuman, True, iDuration, CyTranslator().getText("TXT_KEY_INVASION_HUNS_SCYTHIA", ()), "", 0, "", ColorTypes(iRed), -1, -1, True, True)
			for iEnemyCiv in lEnemyCivsOnSpawn[iHuns]:
				if utils.isActive(iEnemyCiv):
					gc.getTeam(pNomad0.getTeam()).declareWar(iEnemyCiv, False, -1)
		if iGameTurn == getTurnForYear(iHunsInvasion) + 15:
			self.provinceAttack(iNomad0, iHuns, [rIllyricum])
			self.provinceAttack(iNomad0, iHuns, [rThrace, rNItaly], True)
		
		# Avars
		if iGameTurn == getTurnForYear(iAvarInvasion) - 3:
			if pNomad2.isAlive():
				utils.killAndFragmentCiv(iNomad2, False)
				utils.clearCulture(iNomad2)
		if iGameTurn == getTurnForYear(iAvarInvasion):
			sd.setCivilization(iNomad2, iAvars)
			pNomad2.setCivilizationType(iAvars)
			pNomad2.setLeader(iRouranLeader)
			self.setCivDesc(iNomad2, "Avar Khaganate", "Avars", "Avar", "Bayan")
			self.assignTechs(iNomad2, iAvars)
			self.provinceAttack(iNomad2, iAvars, [rDacia, rIllyricum])
			CyInterface().addMessage(iHuman, True, iDuration, CyTranslator().getText("TXT_KEY_INDEPENDENCE_TEXT_AVARS", ()), "", 0, "", ColorTypes(iRed), -1, -1, True, True)
			for iEnemyCiv in lEnemyCivsOnSpawn[iAvars]:
				if utils.isActive(iEnemyCiv):
					gc.getTeam(pNomad2.getTeam()).declareWar(iEnemyCiv, False, -1)
		if iGameTurn == getTurnForYear(iAvarInvasion) + 5:
			self.provinceAttack(iNomad2, iAvars, [rThrace], True)
			
			
		# Saxons
		if getTurnForYear(410) <= iGameTurn <= getTurnForYear(418):
			if not pCelts.isAlive():
				sd.setCivilization(iCelts, iSaxons)
				pCelts.setCivilizationType(iSaxons)
				self.setCivDesc(iCelts, "Saxon Kingdom", "Saxons", "Saxon", "TXT_KEY_LEADER_SAXON")
				pCelts.setFlag("Art/Interface/TeamColor/FlagDECAL_Blank.dds")
				utils.clearCulture(iCelts)
				self.barbarianBirth(iCelts, iSaxons)
				for iEnemyCiv in lEnemyCivsOnSpawn[iSaxons]:
					if utils.isActive(iEnemyCiv):
						gc.getTeam(pCelts.getTeam()).declareWar(iEnemyCiv, False, -1)
				
		# Chenla
		if iGameTurn > getTurnForYear(525) and not pFunan.isAlive():
			utils.clearCulture(iFunan)
			#sd.setCivilization(iFunan, iChenla)
			self.setCivDesc(iFunan, "Kingdom of Chenla", "Chenla", "Chenla", "Mahendravarman")
			self.assignTechs(iFunan, iFunan)
			self.provinceAttack(iFunan, iFunan, [rFunan])
			#for iEnemyCiv in lEnemyCivsOnSpawn[iChenla]:
				#if utils.isActive(iEnemyCiv):
					#gc.getTeam(pPlayer.getTeam()).declareWar(iEnemyCiv, False, -1)
				
		# Makuria
		if iGameTurn > getTurnForYear(600) and not pNubia.isAlive():
			utils.clearCulture(iNubia)
			sd.setCivilization(iNubia, iMakuria)
			self.setCivDesc(iNubia, "Kingdom of Makuria", "Makuria", "Makuria", "Merkurios")
			pNubia.setCivilizationType(iMakuria)
			self.assignTechs(iNubia, iMakuria)
			self.provinceAttack(iNubia, iMakuria, [rNubia])
			#for iEnemyCiv in lEnemyCivsOnSpawn[iMakuria]:
				#if utils.isActive(iEnemyCiv):
					#gc.getTeam(pPlayer.getTeam()).declareWar(iEnemyCiv, False, -1)
			
		# Harsha
		if iGameTurn == getTurnForYear(606) and not pMauryans.isAlive():
			sd.setCivilization(iMauryans, iHarsha)
			pMauryans.setCivilizationType(iHarsha)
			pMauryans.setCivics(4, iStateReligionCivic)
			pMauryans.setLastStateReligion(iBuddhism)
			pMauryans.setLeader(iPusyamitra)
			self.setCivDesc(iMauryans, "Empire of Harshavardhana", "Pushyabhuti", "Pushyabhutis", "Harshavardhana")
			self.assignTechs(iMauryans, iHarsha)
			pMauryans.setCivics(0, iMonarchyCivic)
			pMauryans.setCivics(1, iVassalageCivic)
			pMauryans.setCivics(2, iCasteSystemCivic)
			pMauryans.setCivics(3, iPatronageCivic)
			pMauryans.setCivics(4, iStateReligionCivic)
			sd.setFlipsDelay(iMauryans, 0)
			self.birthConditional(iMauryans, (107, 38), utils.getCorePlotList(iHarsha))
			CyInterface().addMessage(iHuman, True, iDuration, CyTranslator().getText("TXT_KEY_INDEPENDENCE_TEXT_HARSHA", ()), "", 0, "", ColorTypes(iRed), -1, -1, True, True)
			for iEnemyCiv in lEnemyCivsOnSpawn[iHarsha]:
				if utils.isActive(iEnemyCiv):
					gc.getTeam(pMauryans.getTeam()).declareWar(iEnemyCiv, False, -1)
			if utils.getHumanID() not in [iChalukyans, iTibet, iTang, iArabs]:
				self.newCivPopup(iMauryans)
		if iGameTurn == getTurnForYear(607) and sd.getCivilization(iMauryans) == iHarsha:
			self.birthConditional(iMauryans, (107, 38), utils.getCorePlotList(iHarsha))
		if iGameTurn == (606) + 5:
			if utils.getHumanID() != iMauryans:
				self.provinceAttack(iMauryans, iHarsha, [rMagadha, rAvanti, rSindh])
			
		# Arab conquerors
		if iGameTurn == getTurnForYear(iArabMesopotamiaInvasion) and iArabs != iHuman and not (utils.checkRegionControl(iArabs, rMesopotamia)):
			self.provinceAttack(iArabs, iArabs, [rMesopotamia])
		if iGameTurn == getTurnForYear(iArabEgyptInvasion) and iArabs != iHuman and not (utils.checkRegionControl(iArabs, rEgypt)):
			self.provinceAttack(iArabs, iArabs, [rEgypt])
		if iGameTurn == (getTurnForYear(iArabEgyptInvasion) + 3) and iArabs != iHuman and not (utils.checkRegionControl(iArabs, rLibya)):
			self.provinceAttack(iArabs, iArabs, [rLibya])
		if iGameTurn == getTurnForYear(iArabAfricaInvasion) and iArabs != iHuman and not (utils.checkRegionControl(iArabs, rAfrica)):
			self.provinceAttack(iArabs, iArabs, [rAfrica])
		if iGameTurn == (getTurnForYear(iArabAfricaInvasion) + 3) and iArabs != iHuman and not (utils.checkRegionControl(iArabs, rNumidia)):
			self.provinceAttack(iArabs, iArabs, [rNumidia])
		
		
		
		if iGameTurn == getTurnForYear(iMoorsInvasion) - 10 and iHuman != iArabs:
			utils.killAndFragmentCiv(iNomad1, False)
			utils.clearCulture(iNomad1)
		if iGameTurn == getTurnForYear(iMoorsInvasion + 1) and iHuman != iArabs:
			sd.setCivilization(iNomad1, iMoors)
			pNomad1.setCivilizationType(iMoors)
			self.setCivDesc(iNomad1, "Moorish Emirate", "Moors", "Moor", "Tariq ibn Ziyad")
			pNomad1.setLeader(iTariq)
			pNomad1.setFlag("Art/Interface/TeamColor/FlagDECAL_Blank.dds")
			self.assignTechs(iNomad1, iMoors)
			gc.getTeam(gc.getPlayer(iNomad1).getTeam()).setVassal(iArabs, True, False)
			self.provinceAttack(iNomad1, iMoors, [rMauretania, rBaetica, rNumidia])
			CyInterface().addMessage(iHuman, True, iDuration, CyTranslator().getText("TXT_KEY_INDEPENDENCE_TEXT_MOORS", ()), "", 0, "", ColorTypes(iRed), -1, -1, True, True)
			
		# respawns
		if iGameTurn > 30 and iGameTurn % 30 == 0:
			for iPlayer in [iAntigonids, iMauryans, iKalinka, iGojoseon, iNubia, iSaba, iPandyans, iRome, iVietnam, iTocharians, iArmenia, iMaccabees, iParthia, iGoguryeo, iAxum, iFunan, iSassanids, iYamato]:
				if iGameTurn > getTurnForYear(tBirth[iPlayer] + 50) and not gc.getPlayer(iPlayer).isAlive():
					if self.checkCoreUnoccupied(iPlayer):
						if gc.getGame().getSorenRandNum(100, 'random number') < tResurrectionProb[iPlayer]:
							if iPlayer == iAntigonids:
								if iGameTurn > getTurnForYear(-100):
									continue
								if iHuman not in [iCarthage, iRome, iEgypt, iSeleucids, iPontus]:
									continue
							if iPlayer == iGojoseon and iGameTurn > getTurnForYear(tBirth[iGoguryeo]) - 100:
								continue
							if iPlayer == iParthia and iGameTurn > getTurnForYear(tBirth[iSassanids]) - 100:
								continue
							#if iPlayer == iFunan and iGameTurn > 350:
								#continue
							if iPlayer == iMauryans:
								self.setCivDesc(iMauryans, "Kingdom of Magadha", "Magadha", "Magadhan", "Vasudeva")
							self.provinceAttack(iPlayer, sd.getCivilization(iPlayer), lCoreRegions[iPlayer])
			
		
			

							
		# special respawn at Pataliputra for Buddhist pilgrims should the Holy City happen to be indy or barb
		'''if (iGameTurn % 20 == 0) and iGameTurn < getTurnForYear(250): #every 20 turns until near Gupta spawn
			if iHuman in [iTocharians, iVietnam, iPandyans, iGoguryeo] and not utils.isActive(iMauryans) and sd.getCivilization(iMauryans) == iSungas and gc.getMap().plot(tPataliputra[0],tPataliputra[1]).getOwner() > iNumPlayers:
				if iGameTurn > getTurnForYear(-70):
					sd.setCivilization(iMauryans, iMagadha)
				utils.cultureManager((tPataliputra[0],tPataliputra[1]), 100, iMauryans, gc.getMap().plot(tPataliputra[0],tPataliputra[1]).getOwner(), False, False, False)
				utils.flipUnitsInCityBefore((tPataliputra[0],tPataliputra[1]), iMauryans, gc.getMap().plot(tPataliputra[0],tPataliputra[1]).getOwner())
				self.setTempFlippingCity((tPataliputra[0],tPataliputra[1]))
				utils.flipCity((tPataliputra[0],tPataliputra[1]), 0, 0, iMauryans, [gc.getMap().plot(tPataliputra[0],tPataliputra[1]).getOwner()])
				utils.flipUnitsInCityAfter(self.getTempFlippingCity(), iMauryans)
				if gc.getMap().plot(tVaranasi[0],tVaranasi[1]).getOwner() > iNumPlayers:
					utils.cultureManager((tVaranasi[0],tVaranasi[1]), 100, iMauryans, gc.getMap().plot(tVaranasi[0],tVaranasi[1]).getOwner(), False, False, False)
					utils.flipUnitsInCityBefore((tVaranasi[0],tVaranasi[1]), iMauryans, gc.getMap().plot(tVaranasi[0],tVaranasi[1]).getOwner())
					self.setTempFlippingCity((tVaranasi[0],tVaranasi[1]))
					utils.flipCity((tVaranasi[0],tVaranasi[1]), 0, 0, iMauryans, [gc.getMap().plot(tVaranasi[0],tVaranasi[1]).getOwner()])
					utils.flipUnitsInCityAfter(self.getTempFlippingCity(), iMauryans)
				for iCiv in range (iNumPlayers):
					gc.getTeam(gc.getPlayer(iMauryans).getTeam()).makePeace(iCiv)'''
		
	
		
	
		#Trigger betrayal mode
		if (self.getBetrayalTurns() > 0):
			self.initBetrayal()
			
		
			
			

				
		# help for AI Jin in 220AD start
		if iGameTurn == getTurnForYear(222) and not (gc.getPlayer(iDacia).isPlayable()):
			if iHuman != iJin:
				utils.makeUnit(iHeavySpearman, iJin, tCapitals[iJin], 2)
				utils.makeUnit(iMarksman, iJin, tCapitals[iJin], 2)
		
		if (self.getCheatersCheck(0) > 0):
			teamPlayer = gc.getTeam(gc.getPlayer(iHuman).getTeam())
			if (teamPlayer.isAtWar(self.getCheatersCheck(1))):
				#print ("No cheaters!")
				self.initMinorBetrayal(self.getCheatersCheck(1))
				self.setCheatersCheck(0, 0)
				self.setCheatersCheck(1, -1)
			else:
				self.setCheatersCheck(0, self.getCheatersCheck(0)-1)
		
		if (iGameTurn % utils.getTurns(20) == 0):
			for i in range(iIndependent, iIndependent3):
				if gc.getPlayer(i).isAlive():
					utils.updateMinorTechs(i, iBarbarian)
		
		
		# conditional spawn - destroy old civs if possible
		iHuman = utils.getHumanID()
		for iCiv in [iKushans, iGoguryeo, iJin, iTang, iSassanids]:
			if iGameTurn == getTurnForYear(tBirth[iCiv]) - utils.getTurns(10):
				iCivToDie = None
				if iCiv == iHuman:
					if iCiv == iKushans:
						iCivToDie = iBactria
					elif iCiv == iGoguryeo:
						iCivToDie = iGojoseon
					elif iCiv == iJin:
						iCivToDie = iHan
					elif iCiv == iSassanids:
						iCivToDie = iParthia
					elif iCiv == iTang:
						iCivToDie = iJin
				else:
					if iCiv == iKushans:
						if iBactria != iHuman:
							if gc.getTeam(gc.getPlayer(iBactria).getTeam()).isHasTech(iStabilityUnstable) or gc.getTeam(gc.getPlayer(iBactria).getTeam()).isHasTech(iStabilityCollapsing):
								iCivToDie = iBactria
					elif iCiv == iGoguryeo:
						if iGojoseon != iHuman:
							if gc.getTeam(gc.getPlayer(iGojoseon).getTeam()).isHasTech(iStabilityUnstable) or gc.getTeam(gc.getPlayer(iGojoseon).getTeam()).isHasTech(iStabilityCollapsing):
								iCivToDie = iGojoseon
					elif iCiv == iJin:
						if iBactria != iHuman:
							if gc.getTeam(gc.getPlayer(iHan).getTeam()).isHasTech(iStabilityUnstable) or gc.getTeam(gc.getPlayer(iHan).getTeam()).isHasTech(iStabilityCollapsing):
								iCivToDie = iHan
					elif iCiv == iSassanids:
						if iParthia != iHuman:
							if gc.getTeam(gc.getPlayer(iParthia).getTeam()).isHasTech(iStabilityUnstable) or gc.getTeam(gc.getPlayer(iParthia).getTeam()).isHasTech(iStabilityCollapsing):
								iCivToDie = iParthia
					elif iCiv == iTang:
						if iJin != iHuman:
							if gc.getTeam(gc.getPlayer(iJin).getTeam()).isHasTech(iStabilityUnstable) or gc.getTeam(gc.getPlayer(iJin).getTeam()).isHasTech(iStabilityCollapsing):
								#print "iCivToDie = iJin"
								iCivToDie = iJin
				if iCivToDie:
					if gc.getPlayer(iHuman).canContact(iCivToDie):
						CyInterface().addMessage(iHuman, False, iDuration, gc.getPlayer(iCivToDie).getCivilizationDescription(0) + " " + \
							CyTranslator().getText("TXT_KEY_STABILITY_CIVILWAR", ()), "", 0, "", ColorTypes(iRed), -1, -1, True, True)
					utils.killAndFragmentCiv(iCivToDie, False)

		# loop through civs and check birth dates - edead
		for iLoopCiv in range(iNumMajPlayers):
			if tBirth[iLoopCiv] > -321 and iGameTurn >= getTurnForYear(tBirth[iLoopCiv]) - 2 and iGameTurn <= getTurnForYear(tBirth[iLoopCiv]) + 6:
				# no Byzantine birth if Rome is human and stable
				if iLoopCiv == iByzantines and iHuman == iRome and gc.getTeam(gc.getPlayer(iRome).getTeam()).setHasTech(iStabilityStable, True, iRome, False, False):
					return
				# altered Kushan birth if Bactria is human
				if iLoopCiv == iKushans and utils.getHumanID() == iBactria:
					self.birthInvasion(iKushans, tSamarqand, utils.getSpecialPlotList(iKushans))
				if iLoopCiv == iByzantines:
					self.initByzantineBirth(iGameTurn, tBirth[iLoopCiv], iLoopCiv)
				else:
					#print ("initBirth called", "iLoopCiv=", iLoopCiv, "tBirth[iLoopCiv]=", tBirth[iLoopCiv])
					self.initBirth(iGameTurn, tBirth[iLoopCiv], iLoopCiv)
					#if iLoopCiv == iByzantines:
						#DynamicCivs.checkName(iRome)
					
		# Byzantine setup
		if (iGameTurn == getTurnForYear(tBirth[iByzantines]) - 5):
			#print "Byzantine setup"
			if iRome == utils.getHumanID() and gc.getTeam(gc.getPlayer(iRome).getTeam()).isHasTech(iStabilityStable):
				sd.setStopSpawn(iByzantines, 1)
				return
			# get rid of far eastern Roman conquests
			utils.secedeDistantCities(iRome, iRome)
			# end eastern Roman wars
			for iCiv in range(iNumPlayers):
				if iCiv in [iArmenia, iPontus, iParthia, iSassanids, iMaccabees, iEgypt, iNubia, iAxum, iSeleucids, iAntigonids, iSaba]:
					gc.getTeam(gc.getPlayer(iRome).getTeam()).makePeace(iCiv)
			
			if iGameTurn == getTurnForYear(tBirth[iByzantines]):
				rfccwaiw.endRomanCivilWar()
				sd.setCivilization(iByzantines, iByzantines)
				gc.getPlayer(iByzantines).setLeader(iJustinian)
				sd.setCivilization(iRome, iWesternRome)
				#sd.setFlipsDelay(iByzantines, 0)
			
		# 3 kingdoms setup
		if (iGameTurn == getTurnForYear(tBirth[iJin]) - 5) and iHuman != iHan:
			self.threeKingdomsSetup()
		
		
		# fragment utility
		if iGameTurn >= getTurnForYear(100) and iGameTurn % utils.getTurns(25) == 6:
			self.fragmentIndependents()
		
		
			
		

		
		# capitals
		self.checkCapitals(iGameTurn)

	# from RFCEurope
	def fragmentIndependents(self): 
		
		for iTest1 in range( iIndependent, iIndependent3):
			for iTest2 in range( iIndependent, iIndependent3):
				if ( not (iTest1 == iTest2) ):
					pTest1 = gc.getPlayer( iTest1 )
					pTest2 = gc.getPlayer( iTest2 )
					if ( abs( pTest1.getNumCities() - pTest2.getNumCities() ) > 5 ):
						if ( pTest1.getNumCities() > pTest2.getNumCities() ):
							iBig = iTest1
							pBig = pTest1
							iSmall = iTest2
							pSmall = pTest2
						else:
							iBig = iTest2
							pBig = pTest2
							iSmall = iTest1
							pSmall = pTest1
						apCityList = PyPlayer(iBig).getCityList()
						iDivideCounter = 0
						iCounter = 0
						for pCity in apCityList:
							iDivideCounter += 1
							if (iDivideCounter % 2 == 1):
								city = pCity.GetCy()
								pCurrent = gc.getMap().plot(city.getX(), city.getY())                                        
								utils.cultureManager((city.getX(),city.getY()), 50, iSmall, iBig, False, True, True)
								utils.flipUnitsInCityBefore((city.getX(),city.getY()), iSmall, iBig)                            
								self.setTempFlippingCity((city.getX(),city.getY()))
								utils.flipCity((city.getX(),city.getY()), 0, 0, iSmall, [iBig])   #by trade because by conquest may raze the city
								utils.flipUnitsInCityAfter(self.getTempFlippingCity(), iSmall)
								UnitArtStyler.updateUnitArtAtPlot(pCurrent)
								iCounter += 1
							if ( iCounter == 3 ):
								break





	def moveBackCapital(self, iCiv):
		apCityList = PyPlayer(iCiv).getCityList()
		if (gc.getMap().plot(tRespawnCapitals[iCiv][0], tRespawnCapitals[iCiv][1]).isCity()):
			oldCapital = gc.getMap().plot(tRespawnCapitals[iCiv][0], tRespawnCapitals[iCiv][1]).getPlotCity()
			if (oldCapital.getOwner() == iCiv):
				if oldCapital.getNumRealBuilding(iPalace) < 1:
					for pCity in apCityList:
						pCity.GetCy().setNumRealBuilding(iPalace, 0)
					oldCapital.setNumRealBuilding(iPalace, 1)
		else:
			iMaxValue = 0
			bestCity = None
			for pCity in apCityList:
				loopCity = pCity.GetCy()
				#loopCity.AI_cityValue() doesn't work as area AI types aren't updated yet
				loopValue = max(0,500-loopCity.getGameTurnFounded()) + loopCity.getPopulation()*10
				#print ("loopValue", loopCity.getName(), loopCity.AI_cityValue(), loopValue) #causes C++ exception
				if (loopValue > iMaxValue):
					iMaxValue = loopValue
					bestCity = loopCity
			if (bestCity != None):
				for pCity in apCityList:
					loopCity = pCity.GetCy()
					if (loopCity != bestCity):
						loopCity.setNumRealBuilding(iPalace, 0)
				bestCity.setNumRealBuilding(iPalace, 1)


	def convertBackCulture(self, iCiv, bMoved = False): # bMoved = True for civs that spawn in another area
		plotList = []
		if bMoved: 
			plotList.extend(utils.getRegionPlotList(lRespawnRegions[iCiv]))
			plotList.extend(utils.getRegionPlotList(lRespawnNormalRegions[iCiv]))
		newAreaIdx = len(plotList)
		plotList.extend(utils.getNormalPlotList(iCiv))
		plotList = utils.uniq(plotList)
		cityList = []
		#collect all the cities in the region
		for i in range(len(plotList)):
			pCurrent = gc.getMap().plot(plotList[i][0], plotList[i][1])
			if (pCurrent.isCity()):
				bOldArea = False
				if bMoved and i >= newAreaIdx:
					bOldArea = True
				for ix in range(pCurrent.getX()-1, pCurrent.getX()+2):		# from x-1 to x+1
					for iy in range(pCurrent.getY()-1, pCurrent.getY()+2):	# from y-1 to y+1
						pCityArea = gc.getMap().plot( ix, iy )
						if bMoved and bOldArea:
							iCivCulture = pCityArea.getCulture(iCiv) / 4
						else:
							iCivCulture = pCityArea.getCulture(iCiv)
						iLoopCivCulture = 0
						for iLoopCiv in range(iIndependent, iBarbarian + 1, 1): #barbarians too
							if bMoved and bOldArea:
								iLoopCivCulture += pCityArea.getCulture(iLoopCiv)/4
								pCityArea.setCulture(iLoopCiv, pCityArea.getCulture(iLoopCiv)*3/4, True)
							else:
								iLoopCivCulture += pCityArea.getCulture(iLoopCiv)
								pCityArea.setCulture(iLoopCiv, 0, True)
						pCityArea.setCulture(iCiv, iCivCulture + iLoopCivCulture, True)
				city = pCurrent.getPlotCity()
				if bMoved and bOldArea:
					iCivCulture = city.getCulture(iCiv) / 4
				else:
					iCivCulture = city.getCulture(iCiv)
				iLoopCivCulture = 0
				for iLoopCiv in range(iIndependent, iBarbarian + 1, 1): #barbarians too
					if bMoved and bOldArea:
						iLoopCivCulture += city.getCulture(iLoopCiv)/4
						city.setCulture(iLoopCiv, city.getCulture(iLoopCiv)*3/4, True)
					else:
						iLoopCivCulture += city.getCulture(iLoopCiv)  
						city.setCulture(iLoopCiv, 0, True)
				city.setCulture(iCiv, iCivCulture + iLoopCivCulture, True) 


	def initBirth(self, iCurrentTurn, iBirthYear, iPlayer):
		iHuman = utils.getHumanID()
		iBirthTurn = getTurnForYear(iBirthYear)
		iCiv = sd.getCivilization(iPlayer)
		#print ("initBirth, iCiv=", iCiv)
		#print("iBirthTurn:%d, iCurrentTurn:%d" %(iBirthTurn, iCurrentTurn))
		#print("getSpawnDelay:%d, getFlipsDelay:%d" %(self.getSpawnDelay(iCiv), self.getFlipsDelay(iCiv)))
		
		#DynamicCivs.onCivSpawn(iCiv)
		
		if self.getStopSpawn(iPlayer) > 0: return
		
		if iCurrentTurn == iBirthTurn and iHuman != iPlayer and utils.isActive(iHuman):
			self.showBirthMessage(iPlayer, iHuman)
		
		if (iCurrentTurn == iBirthTurn-1 + self.getSpawnDelay(iPlayer) + self.getFlipsDelay(iPlayer)):
				#print "1st call"
				tCapital = tCapitals[iCiv]
				if (self.getFlipsDelay(iPlayer) == 0): #city hasn't already been founded)
					
					#this may fix the -1 bug
					#if (iCiv == iHuman): # srpt Byz hack
					if (iPlayer == iHuman): 
						killPlot = gc.getMap().plot(tCapital[0], tCapital[1])
						iNumUnitsInAPlot = killPlot.getNumUnits()
						if (iNumUnitsInAPlot):
							for i in range(iNumUnitsInAPlot):
								unit = killPlot.getUnit(i)
								if (unit.getOwner() != iPlayer):
									unit.kill(False, iBarbarian)
					
					# conditional spawn - if applicable, will convert one city instead of spawning the settler
					if tNoSettler[iCiv] > 0 and gc.getMap().plot(tCapital[0], tCapital[1]).isCity():
						if iCiv in [iJin, iSassanids, iGupta, iTang]:
							#utils.makeUnit(iWorker, iCiv, (tCapital[0] + 1, tCapital[1] - 1), 1)
							self.birthConditional(iPlayer, tCapital, utils.getCorePlotList(iCiv))
							return
						if iCiv in [iKushans, iMaccabees, iVandals, iOstrogoths]:
							self.birthInvasion(iPlayer, tCapital, utils.getCorePlotList(iCiv))
							return
					#print "Continuing"
					bDeleteEverything = False
					pCapital = gc.getMap().plot(tCapital[0], tCapital[1])
					if (pCapital.isOwned()):
						if (iPlayer == iHuman or not gc.getPlayer(iHuman).isAlive()): 
							bDeleteEverything = True
							#print ("bDeleteEverything 1")
						else:
							bDeleteEverything = True
							for x in range(tCapital[0] - 2, tCapital[0] + 3):		# from x-1 to x+1
								for y in range(tCapital[1] - 2, tCapital[1] + 3):	# from y-1 to y+1
									pCurrent=gc.getMap().plot(x, y)
									if (pCurrent.isCity() and pCurrent.getPlotCity().getOwner() == iHuman):
										bDeleteEverything = False
										#print ("bDeleteEverything 2")
										break
					if iCiv in []:
						bDeleteEverything = False # military spawn, spare Kushans/Axum
					#print ("bDeleteEverything", bDeleteEverything)
					if (not gc.getMap().plot(tCapital[0], tCapital[1]).isOwned()):
						if iCiv in []: #dangerous starts
							self.setDeleteMode(0, iCiv)
						self.birthInFreeRegion(iCiv, tCapital, utils.getCorePlotList(iCiv))
					elif (bDeleteEverything):
						self.setDeleteMode(0, iPlayer)
						# edead: part 1 - cities
						for x in range(tCapital[0] - 2, tCapital[0] + 3):		# from x-2 to x+2
							for y in range(tCapital[1] - 2, tCapital[1] + 3):	# from y-2 to y+2
								#print ("deleting cities", x, y)
								pCurrent = gc.getMap().plot(x, y)
								if (pCurrent.isCity()):
									pCurrent.eraseAIDevelopment() #new function, similar to erase but won't delete rivers, resources and features()
						# edead: part 2 - units & culture
						for x in range(tCapital[0] - 1, tCapital[0] + 2):		# from x-1 to x+1
							for y in range(tCapital[1] - 1, tCapital[1] + 2):	# from y-1 to y+1
								#print ("deleting everything else", x, y)
								pCurrent = gc.getMap().plot(x, y)
								for iLoopPlayer in range(iBarbarian+1): #Barbarians as well
									if (iPlayer != iLoopPlayer):
										utils.flipUnitsInArea([(x,y)], iPlayer, iLoopPlayer, True, False)
								for iLoopPlayer in range(iBarbarian+1): #Barbarians as well
									if (iPlayer != iLoopPlayer):
										pCurrent.setCulture(iLoopPlayer, 0, True)
								pCurrent.setOwner(-1)
						plotList = utils.getCorePlotList(iCiv)
						for iLoopPlayer in range(iBarbarian+1): #Barbarians as well
							if (iPlayer != iLoopPlayer):
								utils.flipUnitsInArea(plotList, iPlayer, iLoopPlayer, True, False, True) # skip AI units within borders
						
						self.birthInFreeRegion(iPlayer, tCapital, utils.getCorePlotList(iCiv))
					else:
						self.birthInForeignBorders(iPlayer, utils.getCorePlotList(iCiv), utils.getBroaderPlotList(iCiv))
				else:
					#print ( "setBirthType again: flips" )
					
					self.birthInFreeRegion(iPlayer, tCapital, utils.getCorePlotList(iCiv))
		
		# war on spawn and reveal moved from here to after unit creation - edead
		
		if (iCurrentTurn == iBirthTurn + sd.getSpawnDelay(iPlayer)) and (gc.getPlayer(iPlayer).isAlive()) and (self.getAlreadySwitched() == False) and (iHuman + tDifference[iHuman] < iPlayer):
			self.newCivPopup(iPlayer)
			
			
	def initByzantineBirth(self, iCurrentTurn, iBirthYear, iCiv):
	
		#print ("initByzantineBirth, iCiv=", iCiv)
		iHuman = utils.getHumanID()
		iBirthTurn = getTurnForYear(iBirthYear)
		#print("iBirthTurn:%d, iCurrentTurn:%d" %(iBirthTurn, iCurrentTurn))
		#print("getSpawnDelay:%d, getFlipsDelay:%d" %(self.getSpawnDelay(iCiv), self.getFlipsDelay(iCiv)))
		
		DynamicCivs.onCivSpawn(iCiv)
		
		if self.getStopSpawn(iCiv) > 0: return
		
		# Byzantine identity fix
		sd.setCivilization(iByzantines, iByzantines)
		gc.getPlayer(iByzantines).setCivilizationType(iByzantines)
		gc.getPlayer(iByzantines).setLeader(iJustinian)
		if iRome != utils.getHumanID():
			gc.getTeam(pRome.getTeam()).setHasTech(iStateReligion, True, iRome, False, False)
			pRome.setCivics(4, iStateReligionCivic)
			pRome.setLastStateReligion(iChristianity)
		
		if iCurrentTurn == iBirthTurn and iHuman != iCiv and utils.isActive(iHuman):
			self.showBirthMessage(iCiv, iHuman)
		
		if (iCurrentTurn == iBirthTurn-1 + self.getSpawnDelay(iCiv) + self.getFlipsDelay(iCiv)):
				#print "1st call"
				tCapital = tCapitals[iCiv]
				if (self.getFlipsDelay(iCiv) == 0): #city hasn't already been founded)
					
					#this may fix the -1 bug
					killPlot = gc.getMap().plot(tCapital[0], tCapital[1])
					iNumUnitsInAPlot = killPlot.getNumUnits()
					if (iNumUnitsInAPlot):
						for i in range(iNumUnitsInAPlot):
							unit = killPlot.getUnit(i)
							if (unit.getOwner() != iCiv):
								unit.kill(False, iBarbarian)
					
					
					#print "Continuing"
					bDeleteEverything = False
					pCapital = gc.getMap().plot(tCapital[0], tCapital[1])
					if (pCapital.isOwned()):
						bDeleteEverything = True
					
					#print ("bDeleteEverything", bDeleteEverything)
					if (not gc.getMap().plot(tCapital[0], tCapital[1]).isOwned()):
						
						self.birthInFreeRegion(iCiv, tCapital, utils.getSpecialPlotList(iCiv))
					elif (bDeleteEverything):
						self.setDeleteMode(0, iCiv)
						# edead: part 1 - cities
						for x in range(tCapital[0] - 2, tCapital[0] + 3):		# from x-2 to x+2
							for y in range(tCapital[1] - 2, tCapital[1] + 3):	# from y-2 to y+2
								#print ("deleting cities", x, y)
								pCurrent = gc.getMap().plot(x, y)
								if (pCurrent.isCity()):
									pCurrent.eraseAIDevelopment() #new function, similar to erase but won't delete rivers, resources and features()
						# edead: part 2 - units & culture
						for x in range(tCapital[0] - 1, tCapital[0] + 2):		# from x-1 to x+1
							for y in range(tCapital[1] - 1, tCapital[1] + 2):	# from y-1 to y+1
								#print ("deleting everything else", x, y)
								pCurrent = gc.getMap().plot(x, y)
								for iLoopCiv in range(iBarbarian+1): #Barbarians as well
									if (iCiv != iLoopCiv):
										utils.flipUnitsInArea([(x,y)], iCiv, iLoopCiv, True, False)
								for iLoopCiv in range(iBarbarian+1): #Barbarians as well
									if (iCiv != iLoopCiv):
										pCurrent.setCulture(iLoopCiv, 0, True)
								pCurrent.setOwner(-1)
						plotList = utils.getCorePlotList(iCiv)
						for iLoopCiv in range(iBarbarian+1): #Barbarians as well
							if (iCiv != iLoopCiv):
								utils.flipUnitsInArea(plotList, iCiv, iLoopCiv, True, False, True) # skip AI units within borders
						#print ("Byzantine birth call 1, iCiv=", iCiv)
						self.byzantineBirthInFreeRegion(iCiv, tCapital, utils.getSpecialPlotList(iCiv))
				else:
					#print ( "setBirthType again: flips" )
					#print ("Byzantine birth call 2, iCiv=", iCiv)
					self.byzantineBirthInFreeRegion(iCiv, tCapital, utils.getSpecialPlotList(iCiv))
		
		# war on spawn and reveal moved from here to after unit creation - edead
		
		if (iCurrentTurn == iBirthTurn + sd.getSpawnDelay(iCiv)) and (gc.getPlayer(iCiv).isAlive()) and (self.getAlreadySwitched() == False) and (iHuman + tDifference[iHuman] < iCiv):
			self.newCivPopup(iCiv)

	def deleteMode(self, iCurrentPlayer):
		
		iCiv = self.getDeleteMode(0)
		#if tNoSettler[iCiv] > 0: return # skip
		
		#print ("deleteMode after", iCurrentPlayer)
		tCapital = tCapitals[iCiv]
		if (iCurrentPlayer == iCiv):
			for x in range(tCapital[0] - 2, tCapital[0] + 3):		# from x-2 to x+2
				for y in range(tCapital[1] - 2, tCapital[1] + 3):	# from y-2 to y+2
					pCurrent=gc.getMap().plot(x, y)
					pCurrent.setCulture(iCiv, 300, True)
			for x in range(tCapital[0] - 1, tCapital[0] + 2):		# from x-1 to x+1
				for y in range(tCapital[1] - 1, tCapital[1] + 2):	# from y-1 to y+1
					pCurrent=gc.getMap().plot(x, y)
					utils.convertPlotCulture(pCurrent, iCiv, 100, True)
					if (pCurrent.getCulture(iCiv) < 3000):
						pCurrent.setCulture(iCiv, 3000, True)
					pCurrent.setOwner(iCiv)
			self.setDeleteMode(0, -1)
			return
		
		#print ("iCurrentPlayer", iCurrentPlayer, "iCiv", iCiv)
		if (iCurrentPlayer != iCiv-1):
			return
		
		bNotOwned = True
		for x in range(tCapital[0] - 1, tCapital[0] + 2):		# from x-1 to x+1
			for y in range(tCapital[1] - 1, tCapital[1] + 2):	# from y-1 to y+1
				#print ("deleting again", x, y)
				pCurrent=gc.getMap().plot(x, y)
				if (pCurrent.isOwned()):
					bNotOwned = False
					for iLoopCiv in range(iBarbarian): #Barbarians as well
						if(iLoopCiv != iCiv):
							pCurrent.setCulture(iLoopCiv, 0, True)
						#else:
						#		if (pCurrent.getCulture(iCiv) < 4000):
						#				pCurrent.setCulture(iCiv, 4000, True)
					#pCurrent.setOwner(-1)
					pCurrent.setOwner(iCiv)
		
		#print ("bNotOwned loop executed OK")
		
		for x in range(tCapital[0] - 11, tCapital[0] + 12):		# must include the distance from Sogut to the Caspius
			for y in range(tCapital[1] - 11, tCapital[1] + 12):
				#print ("units", x, y, gc.getMap().plot(x, y).getNumUnits(), tCapital[0], tCapital[1])
				if (x != tCapital[0] or y != tCapital[1]):
					pCurrent=gc.getMap().plot(x, y)
					if (pCurrent.getNumUnits() > 0 and not pCurrent.isWater()):
						unit = pCurrent.getUnit(0)
						#print ("units2", x, y, gc.getMap().plot(x, y).getNumUnits(), unit.getOwner(), iCiv)
						if (unit.getOwner() == iCiv):
							#print ("moving starting units from", x, y, "to", (tCapital[0], tCapital[1]))
							for i in range(pCurrent.getNumUnits()):
								unit = pCurrent.getUnit(0)
								unit.setXY(tCapital[0], tCapital[1], False, False, False)
							#may intersect plot close to tCapital
##								for farX in range(x - 6, x + 7):
##									for farY in range(y - 6, y + 7):
##										pCurrentFar = gc.getMap().plot(farX, farY)
##										if (pCurrentFar.getNumUnits() == 0):
##											pCurrentFar.setRevealed(iCiv, False, True, -1);


	def birthConditional(self, iPlayer, tCapital, plotList):
		
		print("birthConditional, FlipsDelay=%d" %(self.getFlipsDelay(iPlayer)))
		print ("iPlayer", iPlayer)
		
		
		startingPlot = (tCapital[0], tCapital[1])
		iOwner = gc.getMap().plot(tCapital[0], tCapital[1]).getOwner()
		if self.getFlipsDelay(iPlayer) == 0:
			iFlipsDelay = self.getFlipsDelay(iPlayer) + 2
			if iFlipsDelay > 0:
				
				# pre-spawn a catapult to revive the player
				#gc.getPlayer(iPlayer).revive() # forces alive status
				print ("revived")
				pCatapult = utils.makeUnit(iCatapult, iPlayer, (iCatapultX, iCatapultY), 1)
				print ("catapult: ", pCatapult.getName())
				
				
				# flip capital instead of spawning starting units
				utils.flipCity(tCapital, False, True, iPlayer, ())
				utils.cultureManager(tCapital, 100, iPlayer, iOwner, True, False, False)
				self.convertSurroundingPlotCultureSquare(iPlayer, (tCapital[0]-1,tCapital[1]-1), (tCapital[0]+1,tCapital[1]+1))
				
				utils.cultureManager(startingPlot, 100, iPlayer, iOwner, True, False, False)
				utils.flipUnitsInCityBefore(startingPlot, iPlayer, iOwner)
				self.setTempFlippingCity(startingPlot) #necessary for the (688379128, 0) bug
				utils.flipCity(startingPlot, 0, 0, iPlayer, [iOwner])
				utils.flipUnitsInCityAfter(self.getTempFlippingCity(), iPlayer)
				
				print ("starting units in", tCapital[0], tCapital[1])
				print ("birthConditional: starting units in", tCapital[0], tCapital[1])
				self.createStartingUnits(iPlayer, tCapitals[sd.getCivilization(iPlayer)], sd.getCivilization(iPlayer))
				#utils.setPlagueCountdown(iPlayer, -utils.getTurns(iImmunity))
				#utils.clearPlague(iPlayer)
				print ("flipping remaining units")
				for i in range(iIndependent, iBarbarian+1):
					utils.flipUnitsInArea(utils.getAreaPlotList((tCapital[0]-2, tCapital[1]-2), (tCapital[0]+2, tCapital[1]+2)), iPlayer, i, True, True) #This is for AI only. During Human player spawn, that area is already cleaned
				self.setFlipsDelay(iPlayer, iFlipsDelay) #save
				
				# kill the catapult and cover the plots
				plotZero = gc.getMap().plot(iCatapultX, iCatapultY)
				if (plotZero.getNumUnits()):
					catapult = plotZero.getUnit(0)
					catapult.kill(False, iPlayer)
				utils.coverPlots(iCatapultX, iCatapultY, iPlayer) # edead
				print ("Plots covered")
				utils.coverPlots(tCapital[0], tCapital[1], iPlayer)# possible fix for city ruins bug
				utils.revealPlots(iPlayer, utils.getRegionPlotList(lRevealRegions[sd.getCivilization(iPlayer)], True)) # re-reveal the plot
		
		else: #starting units have already been placed, now the second part
			iNumAICitiesConverted, iNumHumanCitiesToConvert = self.convertSurroundingCities(iPlayer, plotList)
			self.convertSurroundingPlotCulture(iPlayer, plotList)
			
			# extra help for the post-barbarian invasion AI
			#if iPlayer != utils.getHumanID() and iPlayer in [iParthia, iDacia, iSrivajaya, iTang, iArabs]:
				#iNumAICitiesConverted += self.convertSurroundingCities(iPlayer, utils.getNormalPlotList(iPlayer), True) # barbs only
				
			# extra help for Rome and Parthia
			if iPlayer != utils.getHumanID() and iPlayer in [iRome, iParthia, iKushans, iJin, iTang, iGupta]:
				#print "conditional"
				iNumAICitiesConverted += self.convertSurroundingCities(iPlayer, utils.getSpecialPlotList(iPlayer), True) # barbs & indys only
			
			for i in range(iIndependent, iBarbarian+1):
				utils.flipUnitsInArea(plotList, iPlayer, i, False, True) #remaining barbs/indeps in the region now belong to the new civ   
			#print ("utils.flipUnitsInArea()")
			
			
			# kill the catapult & cover the plots
			plotZero = gc.getMap().plot(iCatapultX, iCatapultY)
			if (plotZero.getNumUnits()):
				catapult = plotZero.getUnit(0)
				catapult.kill(False, iPlayer)
			utils.coverPlots(iCatapultX, iCatapultY, iPlayer) # edead
			#print ("Plots covered")
			
			# create workers
			if gc.getPlayer(iPlayer).getNumCities() > 0:
				capital = gc.getPlayer(iPlayer).getCapitalCity()
				self.createStartingWorkers(iPlayer, (capital.getX(), capital.getY()))
			
			# convert human cities
			if iNumHumanCitiesToConvert > 0:
				self.flipPopup(iPlayer, plotList)
			
			# move AI capital
			#if tNoSettler[iPlayer] > 0:
			if not self.moveCapital(tCapital, iPlayer):
				self.moveCapital(tBackupCapitals[sd.getCiviization(iPlayer)], iPlayer)
			
			# extra units in flipped cities
			self.createPostFlipUnits(iPlayer)
			
			# extra settlers
			self.createPostFlipSettlers(iPlayer, tCapital)


	def birthInvasion(self, iPlayer, tCapital, plotList):#, iPlayer = -1):
	
		print ("birthInvasion, iPlayer=", iPlayer, "iCiv=", sd.getCivilization(iPlayer))
		print("birthInvasion, FlipsDelay=%d" %(self.getFlipsDelay(iPlayer)))
		#if iPlayer == -1:
			#iPlayer = iCiv
			
		bMaccabeanRomanWar = False
		
		if self.getFlipsDelay(iPlayer) == 0:
			print ("1st part of birthInvasion, iPlayer=", iPlayer)
			iFlipsDelay = self.getFlipsDelay(iPlayer) + 2
			print ("iFlipsDelay=", iFlipsDelay)
			if iFlipsDelay > 0:
				
				# declare war on the capital's owner
				print ("tCapital=", tCapital[0], tCapital[1])
				if gc.getMap().plot(tCapital[0], tCapital[1]).isCity():
					print "capital is city"
					iCapitalOwner = gc.getMap().plot(tCapital[0],tCapital[1]).getOwner()
					print ("iCapitalOwner=", iCapitalOwner)
					if sd.getCivilization(iPlayer) == iMaccabees and iCapitalOwner == iRome:
						bMaccabeanRomanWar = True
					if not gc.getTeam(gc.getPlayer(iPlayer).getTeam()).isAtWar(gc.getPlayer(iCapitalOwner).getTeam()):
						print ("declare war, iPlayer=", iPlayer, "iCapitalOwner=", iCapitalOwner)
						gc.getTeam(gc.getPlayer(iPlayer).getTeam()).declareWar(gc.getPlayer(iCapitalOwner).getTeam(), True, -1)
				
					# traitors open the gates...
					city = gc.getMap().plot(tCapital[0],tCapital[1]).getPlotCity()
					if city:
						city.changeCultureUpdateTimer(3);
						city.changeOccupationTimer(3);
						CyInterface().addMessage(city.getOwner(), False, iDuration, localText.getText("TXT_KEY_TRAITOR_REVOLT", (city.getName(),)), "AS2D_CITY_REVOLT", InterfaceMessageTypes.MESSAGE_TYPE_MINOR_EVENT, ArtFileMgr.getInterfaceArtInfo("INTERFACE_RESISTANCE").getPath(), ColorTypes(iRed), city.getX(), city.getY(), True, True);
					
					# find a spot for the siege
					for tPlot in ((city.getX(), city.getY()+1), (city.getX(), city.getY()-1), (city.getX()+1, city.getY()), (city.getX()-1, city.getY()), (city.getX()+1, city.getY()+1), (city.getX()-1, city.getY()-1), (city.getX()+1, city.getY()-1), (city.getX()-1, city.getY()+1)):
						pPlot = gc.getMap().plot(tPlot[0], tPlot[1])
						if pPlot.getOwner() < 0 or gc.getTeam(gc.getPlayer(iPlayer).getTeam()).isAtWar(gc.getPlayer(pPlot.getOwner()).getTeam()):
							if (not pPlot.isWater() and not pPlot.isPeak() and pPlot.getFeatureType() not in [iForest, iMarsh, iJungle, iDenseForest, iIce]):
								if not utils.areDividedByRiver(tPlot, [city.getX(), city.getY()]):
									break
									
					
					startingPlot = gc.getMap().plot(tPlot[0], tPlot[1])
					
					# clear the spot
					iNumUnitsInAPlot = startingPlot.getNumUnits()
					if iNumUnitsInAPlot:
						for i in range(iNumUnitsInAPlot):
							unit = startingPlot.getUnit(0)
							if unit.getOwner() != iPlayer:
								unit.kill(False, iBarbarian)
					
					print ("birthInvasion: starting units in", tPlot[0], tPlot[1])
					self.createStartingUnits(iPlayer, (tPlot[0], tPlot[1]), sd.getCivilization(iPlayer))
					if bMaccabeanRomanWar:
						self.createAdditionalMaccabeanUnits(iPlayer, tCapitals[iPlayer])
					utils.setPlagueCountdown(iPlayer, -utils.getTurns(iImmunity))
					utils.clearPlague(iPlayer)
					for i in range(iIndependent, iBarbarian+1):
						utils.flipUnitsInArea(utils.getAreaPlotList((tCapital[0]-2, tCapital[1]-2), (tCapital[0]+2, tCapital[1]+2)), iPlayer, i, True, True) #This is for AI only. During Human player spawn, that area is already cleaned
					self.setFlipsDelay(iPlayer, iFlipsDelay) #save
				else:
					self.createSettlerAndGarrison(iPlayer, tCapital, sd.getCivilization(iPlayer))
		
		else: #starting units have already been placed, now the second part
			print ("2nd part of birthInvasion, iPlayer=", iPlayer)
			iNumAICitiesConverted, iNumHumanCitiesToConvert = self.convertSurroundingCities(iPlayer, plotList)
			
			# extra help for the post-barbarian invasion AI
			#if iCiv != iHuman and iCiv in []:
				#iNumExtraCities, dummy = self.convertSurroundingCities(iCiv, utils.getNormalPlotList(iCiv), True) # barbs only
				#iNumAICitiesConverted += iNumExtraCities
			
			self.convertSurroundingPlotCulture(iPlayer, plotList)
			for i in range(iIndependent, iBarbarian+1):
				utils.flipUnitsInArea(plotList, iPlayer, i, False, True) #remaining barbs/indeps in the region now belong to the new civ   
			print ("utils.flipUnitsInArea()")
			
			# kill the catapult & cover the plots
			plotZero = gc.getMap().plot(iCatapultX, iCatapultY)
			if (plotZero.getNumUnits()):
				catapult = plotZero.getUnit(0)
				catapult.kill(False, iPlayer)
			utils.coverPlots(iCatapultX, iCatapultY, iPlayer) # edead
			print ("Plots covered")
			
			# create workers
			if gc.getPlayer(iPlayer).getNumCities() > 0:
				capital = gc.getPlayer(iPlayer).getCapitalCity()
				self.createStartingWorkers(iPlayer, (capital.getX(), capital.getY()))
			
			# convert human cities
			if iNumHumanCitiesToConvert > 0:
				self.flipPopup(iCiv, plotList)
			
			# move AI capital
			#if tNoSettler[iCiv] > 0:
			if not self.moveCapital(tCapital, iPlayer):
				self.moveCapital(tBackupCapitals[sd.getCivilization(iPlayer)], iPlayer)
			
			# extra units in flipped cities
			self.createPostFlipUnits(iPlayer)
			
			# extra settlers
			#self.createPostFlipSettlers(iCiv, tCapital)


	def birthInFreeRegion(self, iPlayer, tCapital, plotList):
		
		print("birthInFreeRegion, FlipsDelay=%d" %(self.getFlipsDelay(iPlayer)))
		
		startingPlot = gc.getMap().plot(tCapital[0], tCapital[1])
		if self.getFlipsDelay(iPlayer) == 0:
			iFlipsDelay = self.getFlipsDelay(iPlayer) + 2
			if iFlipsDelay > 0:
				self.createStartingUnits(iPlayer, tCapitals[sd.getCivilization(iPlayer)], sd.getCivilization(iPlayer))
				utils.setPlagueCountdown(iPlayer, -utils.getTurns(iImmunity))
				utils.clearPlague(iPlayer)
				for i in range(iIndependent, iBarbarian+1):
					utils.flipUnitsInArea(utils.getAreaPlotList((tCapital[0]-2, tCapital[1]-2), (tCapital[0]+2, tCapital[1]+2)), iPlayer, i, True, True) #This is for AI only. During Human player spawn, that area is already cleaned
				self.setFlipsDelay(iPlayer, iFlipsDelay) #save
		
		else: #starting units have already been placed, now the second part
			print ("2nd part of birth, iPlayer=", iPlayer)
			if iPlayer not in [iYamato, iPandyans] or iPlayer != utils.getHumanID():
				iNumAICitiesConverted, iNumHumanCitiesToConvert = self.convertSurroundingCities(iPlayer, plotList)
			else:
				iNumAICitiesConverted, iNumHumanCitiesToConvert = 0, 0
			
			# extra help for Rome
			if iPlayer != utils.getHumanID() and iPlayer == iRome:
				self.convertSurroundingCities(iPlayer, utils.getSpecialPlotList(iPlayer), True) # barbs & indys only
			
			if iPlayer not in [iYamato, iPandyans] or iPlayer != utils.getHumanID():
				self.convertSurroundingPlotCulture(iPlayer, plotList)
				for i in range(iIndependent, iBarbarian+1):
					utils.flipUnitsInArea(plotList, iPlayer, i, False, True) #remaining barbs/indeps in the region now belong to the new civ   
			
			
			
			# kill the catapult & cover the plots
			plotZero = gc.getMap().plot(iCatapultX, iCatapultY)
			if (plotZero.getNumUnits()):
				catapult = plotZero.getUnit(0)
				catapult.kill(False, iPlayer)
			utils.coverPlots(iCatapultX, iCatapultY, iPlayer) # edead
			print ("Plots covered")
			
			# create workers
			if gc.getPlayer(iPlayer).getNumCities() > 0:
				capital = gc.getPlayer(iPlayer).getCapitalCity()
				self.createStartingWorkers(iPlayer, (capital.getX(), capital.getY()))
			
			# convert human cities
			if iNumHumanCitiesToConvert > 0:
				self.flipPopup(iPlayer, plotList)
			
			# move AI capital
			#if tNoSettler[iPlayer] > 0:
			if not self.moveCapital(tCapital, iPlayer):
				self.moveCapital(tBackupCapitals[iPlayer], iPlayer)
			
			# extra units in flipped cities
			self.createPostFlipUnits(iPlayer)
			
			# extra settlers
			self.createPostFlipSettlers(iPlayer, tCapital)
			
			
	def byzantineBirthInFreeRegion(self, iPlayer, tCapital, plotList):
		
		print("byzantineBirthInFreeRegion, FlipsDelay=%d" %(self.getFlipsDelay(iPlayer)))
		
		startingPlot = gc.getMap().plot(tCapital[0], tCapital[1])
		if self.getFlipsDelay(iPlayer) == 0:
			iFlipsDelay = self.getFlipsDelay(iPlayer) + 2
			if iFlipsDelay > 0:
				self.createStartingUnits(iPlayer, tCapitals[sd.getCivilization(iPlayer)], sd.getCivilization(iPlayer))
				utils.setPlagueCountdown(iPlayer, -utils.getTurns(iImmunity))
				utils.clearPlague(iPlayer)
				for i in range(iIndependent, iBarbarian+1):
					utils.flipUnitsInArea(utils.getAreaPlotList((tCapital[0]-2, tCapital[1]-2), (tCapital[0]+2, tCapital[1]+2)), iPlayer, i, True, True) #This is for AI only. During Human player spawn, that area is already cleaned
				self.setFlipsDelay(iPlayer, iFlipsDelay) #save
		
		else: #starting units have already been placed, now the second part
			print ("2nd part of birth, iPlayer=", iPlayer)
			self.byzantineConvertRomanCities()
			
			self.convertSurroundingPlotCulture(iPlayer, plotList)
			for i in range(iIndependent, iBarbarian+1):
				utils.flipUnitsInArea(plotList, iPlayer, i, False, True) #remaining barbs/indeps in the region now belong to the new civ  
			utils.byzantineRomanUnitFlip()
			if iRome != utils.getHumanID():
				# stabilize Western Rome
				gc.getTeam(gc.getPlayer(iRome).getTeam()).setHasTech(iStabilityStable, True, iRome, False, False)
				# cut contacts with the east, make peace and set vassalge to Byzantium
				for iPlayer in [iArmenia, iPontus, iParthia, iSassanids, iMaccabees, iEgypt, iNubia, iAxum, iSeleucids, iAntigonids, iKushans, iSaba]:
					if gc.getTeam(gc.getPlayer(iRome).getTeam()).isAtWar(iPlayer):
						gc.getTeam(gc.getPlayer(iRome).getTeam()).makePeace(iPlayer)
						gc.getPlayer(iRome).AI_changeAttitudeExtra(iPlayer, 2)
						gc.getTeam(iRome).cutContact(iPlayer)
				for iPlayer in [iArmenia, iPontus, iParthia, iSassanids, iMaccabees, iEgypt, iNubia, iAxum, iSeleucids, iAntigonids, iKushans, iSaba]:
					if (gc.getTeam(gc.getPlayer(iPlayer).getTeam()).isVassal(iRome)):
						gc.getTeam(gc.getPlayer(iPlayer).getTeam()).setVassal(iRome, False, False)
						gc.getTeam(gc.getPlayer(iPlayer).getTeam()).setVassal(iByzantines, True, False)
					else:
						gc.getTeam(iRome).cutContact(iPlayer)
			
			
			# kill the catapult & cover the plots
			plotZero = gc.getMap().plot(iCatapultX, iCatapultY)
			if (plotZero.getNumUnits()):
				catapult = plotZero.getUnit(0)
				catapult.kill(False, iPlayer)
			utils.coverPlots(iCatapultX, iCatapultY, iPlayer) # edead
			print ("Plots covered")
			
			# create workers
			if gc.getPlayer(iPlayer).getNumCities() > 0:
				capital = gc.getPlayer(iPlayer).getCapitalCity()
				if iPlayer != iByzantines:
					self.createStartingWorkers(iPlayer, (capital.getX(), capital.getY()))
			
			# convert human cities
			#if iNumHumanCitiesToConvert > 0:
				#self.flipPopup(iPlayer, plotList)
			
			# move AI capital
			#if tNoSettler[iPlayer] > 0:
			if not self.moveCapital(tCapital, iPlayer):
				self.moveCapital(tBackupCapitals[iPlayer], iPlayer)
			
			# extra units in flipped cities
			self.createPostFlipUnits(iPlayer)
			
			# extra settlers
			self.createPostFlipSettlers(iPlayer, tCapital)


	def birthInForeignBorders(self, iPlayer, lCorePlots, lBroaderPlots):
		print "2nd part of birthInForeignBorders"
		
		iNumAICitiesConverted, iNumHumanCitiesToConvert = self.convertSurroundingCities(iPlayer, lCorePlots)
		self.convertSurroundingPlotCulture(iPlayer, lCorePlots)
		
		# extra help for the post-barbarian invasion AI
		if iPlayer != iHuman and iPlayer in [iParthia, iDacia, iSrivajaya, iTang, iArabs]:
			iNumExtraCities, dummy = self.convertSurroundingCities(iPlayer, utils.getNormalPlotList(iPlayer), True) # barbs only
			iNumAICitiesConverted += iNumExtraCities

		#now starting units must be placed
		if (iNumAICitiesConverted > 0):
			#utils.debugTextPopup( 'iConverted OK for placing units' )
			dummy1, plotList = utils.plotListSearch( lCorePlots, utils.ownedCityPlots, iPlayer )
			rndNum = gc.getGame().getSorenRandNum(len(plotList), 'searching any city just flipped')
			print ("rndNum for starting units", rndNum)
			if (len(plotList)):
				result = plotList[rndNum]
				if (result):
					self.createStartingUnits(iPlayer, result, sd.getCivilization(iPlayer))
					utils.setPlagueCountdown(iPlayer, -utils.getTurns(iImmunity))
					utils.clearPlague(iPlayer)
					#gc.getPlayer(iPlayer).changeAnarchyTurns(1)
			for i in range(iIndependent, iBarbarian+1):
				utils.flipUnitsInArea(lCorePlots, iPlayer, i, False, False) #remaining barbs in the region now belong to the new civ 
			
			# move AI capital
			#if tNoSettler[iPlayer] > 0:
			if not self.moveCapital(tCapitals[sd.getCivilization(iPlayer)], iPlayer):
				self.moveCapital(tBackupCapitals[sd.getCivilization(iPlayer)], iPlayer)
		
		else:   #search another place
			dummy, plotList = utils.plotListSearch( lCorePlots, utils.goodPlots, [] )
			rndNum = gc.getGame().getSorenRandNum(len(plotList), 'searching another free plot')
			if (len(plotList)):
				result = plotList[rndNum]
				if (result):
					self.createStartingUnits(iPlayer, result, sd.getCivilization(iPlayer))
					utils.setPlagueCountdown(iPlayer, -utils.getTurns(iImmunity))
					utils.clearPlague(iPlayer)
			else:
				dummy1, plotList = utils.plotListSearch( lBroaderPlots, utils.goodPlots, [] )
				rndNum = gc.getGame().getSorenRandNum(len(plotList), 'searching other good plots in a broader region')
				if (len(plotList)):
					result = plotList[rndNum]
					if (result):
						self.createStartingUnits(iPlayer, result, sd.getCivilization(iPlayer))
						self.createStartingWorkers(iPlayer, result)
						utils.setPlagueCountdown(iPlayer, -utils.getTurns(iImmunity))
						utils.clearPlague(iPlayer)
			for i in range(iIndependent, iBarbarian+1):
				utils.flipUnitsInArea(lCorePlots, iPlayer, i, True, True) #remaining barbs in the region now belong to the new civ 
		
		if (iNumHumanCitiesToConvert > 0):
			self.flipPopup(iPlayer, lCorePlots)
		
		# extra units in flipped cities
		self.createPostFlipUnits(iPlayer)


	def convertSurroundingCities(self, iCiv, plotList, fBarbOnly = False):
			print "convertSurroundingCities"
			iConvertedCitiesCount = 0
			iNumHumanCities = 0
			cityList = []
			self.setSpawnWar(0)
			
			#collect all the cities in the spawn region
			for i in range(len(plotList)):
				pCurrent = gc.getMap().plot(plotList[i][0], plotList[i][1])
				if pCurrent.isCity():
					if pCurrent.getPlotCity().getOwner() != iCiv:
						if not fBarbOnly or pCurrent.getPlotCity().getOwner() >= iNumPlayers:
							if iCiv == iByzantines and pCurrent.getPlotCity().getOwner() != iRome: #special case: Byzantines flip only Roman cities
								pass
							else:
								cityList.append(pCurrent.getPlotCity())

			#print ("Birth", iCiv)
			#print (cityList)

			#for each city
			if len(cityList):
				for i in range(len(cityList)):
					loopCity = cityList[i]
					loopX = loopCity.getX()
					loopY = loopCity.getY()
					print ("cityList", loopCity.getName(), (loopX, loopY))
					#iHuman = utils.getHumanID()
					iOwner = loopCity.getOwner()
					iCultureChange = 0 #if 0, no flip; if > 0, flip will occur with the value as variable for utils.CultureManager()
							
					#case 1: barbarian/independent city
					if (iOwner >= iNumPlayers):
						#print ("indy city", loopX, loopY)
						#utils.debugTextPopup( 'BARB' )
						iCultureChange = 100
					#case 2: human city
					#elif (iOwner == iHuman and not loopCity.isCapital()): #exploitable
					elif (iOwner == iHuman and not (loopX == tCapitals[iHuman] and loopY == tCapitals[iHuman]) and not gc.getPlayer(iHuman).getNumCities() <= 1 and not (self.getCheatMode() == True and loopCity.isCapital())):
						# Byzantines flip human Roman cities as normal
						#if iOwner != iRome or iCiv != iByzantines:
						if (iNumHumanCities == 0):
							iNumHumanCities += 1
							#iConvertedCitiesCount += 1
							#self.flipPopup(iCiv, plotList)
					#case 3: other
					else:  #if (not loopCity.isCapital()):   #utils.debugTextPopup( 'OTHER' )
						if (iConvertedCitiesCount < 7) or (iCiv == iByzantines) and (iOwner == iRome): #there won't be more than 5 flips in the area, special case for Byzantium flipping Roman cities
							#utils.debugTextPopup( 'iConvertedCities OK' )
							iCultureChange = 50
							if (gc.getGame().getGameTurn() <= getTurnForYear(tBirth[iCiv]) + 5): #if we're during a birth
								rndNum = gc.getGame().getSorenRandNum(100, 'odds')
								if (rndNum >= tAIStopBirthThreshold[iOwner]):
									#print (iOwner, "stops birth", iCiv, "rndNum:", rndNum, "threshold:", tAIStopBirthThreshold[iOwner])
									if (not gc.getTeam(gc.getPlayer(iOwner).getTeam()).isAtWar(iCiv)):
										if not (iCiv == iByzantines and iOwner == iRome):
											gc.getTeam(gc.getPlayer(iOwner).getTeam()).declareWar(iCiv, False, -1)
											if (gc.getPlayer(iCiv).getNumCities() > 0): #this check is needed, otherwise game crashes
												#print ("capital:", gc.getPlayer(iCiv).getCapitalCity().getX(), gc.getPlayer(iCiv).getCapitalCity().getY())
												if (gc.getPlayer(iCiv).getCapitalCity().getX() != -1 and gc.getPlayer(iCiv).getCapitalCity().getY() != -1):
													self.createAdditionalUnits(iCiv, (gc.getPlayer(iCiv).getCapitalCity().getX(), gc.getPlayer(iCiv).getCapitalCity().getY()))
													if iCiv == iMaccabees and iOwner == iRome:
														self.createAdditionalMaccabeanUnits(iCiv, (gc.getPlayer(iCiv).getCapitalCity().getX(), gc.getPlayer(iCiv).getCapitalCity().getY()))
												else:
													self.createAdditionalUnits(iCiv, tCapitals[iCiv])
													if iCiv == iMaccabees and iOwner == iRome:
														self.createAdditionalMaccabeanUnits(iCiv, tCapitals[iCiv])
							
					if (iCultureChange > 0):
						#print ("flipping ", cityList[i].getName())
						utils.cultureManager((loopX, loopY), iCultureChange, iCiv, iOwner, True, False, False)
						#gc.getMap().plot(cityList[i].getX(),cityList[i].getY()).setImprovementType(-1)
								
						utils.flipUnitsInCityBefore((loopX, loopY), iCiv, iOwner)
						self.setTempFlippingCity((loopX, loopY)) #necessary for the (688379128, 0) bug
						utils.flipCity((loopX, loopY), 0, 0, iCiv, [iOwner])
						#print ("flipping city at:", loopX, loopY)
						#print ("cityList[i].getXY", cityList[i].getX(), cityList[i].getY()) 
						utils.flipUnitsInCityAfter(self.getTempFlippingCity(), iCiv)
								
						iConvertedCitiesCount += 1
						#print ("iConvertedCitiesCount", iConvertedCitiesCount)

			if (iConvertedCitiesCount > 0):
				if (gc.getPlayer(iCiv).isHuman()):
					CyInterface().addMessage(iCiv, True, iDuration, CyTranslator().getText("TXT_KEY_FLIP_TO_US", ()), "", 0, "", ColorTypes(iGreen), -1, -1, True, True)
			
			# hit neighbours stability
			self.hitNeighboursStability(iCiv)
			
			#print( "converted cities", iConvertedCitiesCount)
			return (iConvertedCitiesCount, iNumHumanCities)
						
	def byzantineConvertRomanCities(self):
			#print "convertSurroundingCities"
			iConvertedCitiesCount = 0
			iNumHumanCities = 0
			cityList = []
			self.setSpawnWar(0)
			
			#collect all the cities in the spawn region
			for pCity in PyPlayer(iRome).getCityList():
					if pCity.getX() >= 43:
						cityList.append(pCity)

			#print ("Birth", iCiv)
			#print (cityList)

			#for each city
			if len(cityList):
				for i in range(len(cityList)):
					loopCity = cityList[i]
					loopX = loopCity.getX()
					loopY = loopCity.getY()
					#print ("cityList", loopCity.getName(), (loopX, loopY))
					#iHuman = utils.getHumanID()
					iOwner = loopCity.getOwner()
					iCultureChange = 0 #if 0, no flip; if > 0, flip will occur with the value as variable for utils.CultureManager()
					#print ("flipping ", cityList[i].getName())
					utils.cultureManager((loopX, loopY), 100, iByzantines, iOwner, True, False, False)
						#gc.getMap().plot(cityList[i].getX(),cityList[i].getY()).setImprovementType(-1)
								
					utils.flipUnitsInCityBefore((loopX, loopY), iByzantines, iOwner)
					self.setTempFlippingCity((loopX, loopY)) #necessary for the (688379128, 0) bug
					utils.flipCity((loopX, loopY), 0, 0, iByzantines, [iOwner])
					#print ("flipping city at:", loopX, loopY)
					#print ("cityList[i].getXY", cityList[i].getX(), cityList[i].getY()) 
					utils.flipUnitsInCityAfter(self.getTempFlippingCity(), iByzantines)



	def convertSurroundingPlotCulture(self, iCiv, plotList):
	
		for i in range(len(plotList)):
			pCurrent = gc.getMap().plot(plotList[i][0], plotList[i][1])
			if iCiv == iByzantines and pCurrent.getOwner () != iRome:
				pass
			elif not pCurrent.isCity():
				utils.convertPlotCulture(pCurrent, iCiv, 100, False)
				
	def convertSurroundingPlotCultureSquare(self, iCiv, tTopLeft, tBottomRight):
                
			for x in range(tTopLeft[0], tBottomRight[0]+1):
				for y in range(tTopLeft[1], tBottomRight[1]+1):
					pCurrent = gc.getMap().plot( x, y )
					if (not pCurrent.isCity()):
						utils.convertPlotCulture(pCurrent, iCiv, 100, False)


	def immuneMode(self, argsList): 
		
		pWinningUnit,pLosingUnit,pAttackingUnit = argsList
		iLosingPlayer = pLosingUnit.getOwner()
		iUnitType = pLosingUnit.getUnitType()
		if (iLosingPlayer < iNumPlayers):
			if (gc.getGame().getGameTurn() >= getTurnForYear(tBirth[iLosingPlayer]) and gc.getGame().getGameTurn() <= getTurnForYear(tBirth[iLosingPlayer])+2):
				if (pLosingUnit.getX() == tCapitals[iLosingPlayer][0] and pLosingUnit.getY() == tCapitals[iLosingPlayer][1]):
					#print("new civs are immune for now")
					if (gc.getGame().getSorenRandNum(100, 'immune roll') >= 50):
						utils.makeUnit(iUnitType, iLosingPlayer, (pLosingUnit.getX(), pLosingUnit.getY()), 1)


	def initMinorBetrayal(self, iCiv):
		
		iHuman = utils.getHumanID()
		dummy, plotList = utils.plotListSearch(utils.getCorePlotList(iCiv), utils.outerInvasion, [])
		rndNum = gc.getGame().getSorenRandNum(len(plotList), 'searching a free plot abroad human players borders')
		if len(plotList):
			result = plotList[rndNum]
			if result:
				self.createAdditionalUnits(iCiv, result)
				self.unitsBetrayal(iCiv, iHuman, utils.getCorePlotList(iCiv), result)


	def initBetrayal(self):
		
		iHuman = utils.getHumanID()
		turnsLeft = self.getBetrayalTurns()
		dummy, plotList = utils.plotListSearch( self.getTempPlotList(), utils.outerInvasion, [] )
		rndNum = gc.getGame().getSorenRandNum(len(plotList), 'searching a free plot abroad human players (or in general, the old civ if human player just swtiched) borders')
		if (not len(plotList)):
			dummy, plotList = utils.plotListSearch( self.getTempPlotList(), utils.innerSpawn, [self.getOldCivFlip(), self.getNewCivFlip()] )
			rndNum = gc.getGame().getSorenRandNum(len(plotList), 'searching a free plot within human or new civs border but distant from units')
		if (not len(plotList)):
			dummy, plotList = utils.plotListSearch( self.getTempPlotList(), utils.innerInvasion, [self.getOldCivFlip(), self.getNewCivFlip()] )
			rndNum = gc.getGame().getSorenRandNum(len(plotList), 'searching a free plot within human or new civs border')
		if (len(plotList)):
			result = plotList[rndNum]
			if (result):
				if (turnsLeft == iBetrayalPeriod):
					self.createAdditionalUnits(self.getNewCivFlip(), result)
				self.unitsBetrayal(self.getNewCivFlip(), self.getOldCivFlip(), self.getTempPlotList(), result)
		self.setBetrayalTurns(turnsLeft - 1)


	def unitsBetrayal(self, iNewOwner, iOldOwner, plotList, tPlot):
		
		#print ("iNewOwner", iNewOwner, "iOldOwner", iOldOwner, "tPlot", tPlot)
		if (gc.getPlayer(self.getOldCivFlip()).isHuman()):
			CyInterface().addMessage(self.getOldCivFlip(), False, iDuration, CyTranslator().getText("TXT_KEY_FLIP_BETRAYAL", ()), "", 0, "", ColorTypes(iGreen), -1, -1, True, True)
		elif (gc.getPlayer(self.getNewCivFlip()).isHuman()):
			CyInterface().addMessage(self.getNewCivFlip(), False, iDuration, CyTranslator().getText("TXT_KEY_FLIP_BETRAYAL_NEW", ()), "", 0, "", ColorTypes(iGreen), -1, -1, True, True)
		for i in range(len(plotList)):
			killPlot = gc.getMap().plot(plotList[i][0], plotList[i][1])
			iNumUnitsInAPlot = killPlot.getNumUnits()
			if (iNumUnitsInAPlot):
				iStateReligion = gc.getPlayer(iNewOwner).getStateReligion()
				for i in range(iNumUnitsInAPlot):
					unit = killPlot.getUnit(i)
					if (unit.getOwner() == iOldOwner):
						rndNum = gc.getGame().getSorenRandNum(100, 'betrayal')
						if (rndNum >= self.getBetrayalThreshold()):
							if (unit.getDomainType() == 2): #land unit
								iUnitType = unit.getUnitType()
								if utils.canBetray(iUnitType, iStateReligion):
									unit.kill(False, iNewOwner)
									utils.makeUnit(iUnitType, iNewOwner, tPlot, 1)
									i = i - 1


	def createAdditionalUnits( self, iCiv, tPlot ):
			
		if iCiv == iGojoseon:
			utils.makeUnit(iChosonHorseman, iCiv, tPlot, 3)
			#utils.makeUnit(iDeccanElephantRider, iCiv, tPlot, 1)
			
		if iCiv == iMauryans:
			utils.makeUnit(iAxeman, iCiv, tPlot, 2)
			utils.makeUnit(iDeccanElephantRider, iCiv, tPlot, 1)
			
		if iCiv == iQin:
			#utils.makeUnit(iArcher, iCiv, tPlot, 2)
			utils.makeUnit(iQinInfantry, iCiv, tPlot, 4)

		if iCiv == iTocharians:
			utils.makeUnit(iTarimBowman, iCiv, tPlot, 2)
			utils.makeUnit(iHorseman, iCiv, tPlot, 2)
			
		if iCiv == iArmenia:
			utils.makeUnit(iArcher, iCiv, tPlot, 2)
			utils.makeUnit(iAzatavrear, iCiv, tPlot, 3)
			
		if iCiv == iMaccabees:
			#utils.makeUnit(iArcher, iCiv, tPlot, 2)
			utils.makeUnit(iMaccabee, iCiv, tPlot, 3)
			
		if iCiv == iSeleucids:
			#utils.makeUnit(iArcher, iCiv, tPlot, 2)
			utils.makeUnit(iHoplite, iCiv, tPlot, 3)
			
		if iCiv == iHan:
			utils.makeUnit(iChokonu, iCiv, tPlot, 4)
			#utils.makeUnit(iSpearman, iCiv, tPlot, 4)
			
		if iCiv == iRome:
			utils.makeUnit(iLegionary, iCiv, tPlot, 4)
			
		if iCiv == iPandyans:
			#utils.makeUnit(iArcher, iCiv, tPlot, 2)
			utils.makeUnit(iAxeman, iCiv, tPlot, 3)
			
		if iCiv == iBactria:
			#utils.makeUnit(iArcher, iCiv, tPlot, 2)
			#utils.makeUnit(iSpearman, iCiv, tPlot, 2)
			utils.makeUnit(iHetairoi, iCiv, tPlot, 3)
			
		if iCiv == iParthia:
			utils.makeUnit(iShivatir, iCiv, tPlot, 4)
			if utils.getHumanID() != iParthia:
				utils.makeUnit(iShivatir, iCiv, tPlot, 4)
			
		if iCiv == iSatavahana:
			#utils.makeUnit(iArcher, iCiv, tPlot, 2)
			utils.makeUnit(iKshatriya, iCiv, tPlot, 4)
			
		if iCiv == iDacia:
			#utils.makeUnit(iArcher, iCiv, tPlot, 2)
			utils.makeUnit(iFalxman, iCiv, tPlot, 4)
			
		if iCiv == iGoguryeo:
			#utils.makeUnit(iArcher, iCiv, tPlot, 2)
			utils.makeUnit(iGoguryeoGaemamusa, iCiv, tPlot, 3)
			
		if iCiv == iKushans:
			utils.makeUnit(iHorseArcher_Kushan, iCiv, tPlot, 5)
			#utils.makeUnit(iArcher, iCiv, tPlot, 5)
			
		if iCiv == iAxum:
			utils.makeUnit(iHorseman, iCiv, tPlot, 2)
			utils.makeUnit(iAxumSarawit, iCiv, tPlot, 4)
			
		if iCiv == iSassanids:
			#utils.makeUnit(iArcher, iCiv, tPlot, 3)
			#utils.makeUnit(iSwordsman, iCiv, tPlot, 3)
			utils.makeUnit(iSassanidCataphract, iCiv, tPlot, 4)
			
		if iCiv == iYamato:
			#utils.makeUnit(iArcher, iCiv, tPlot, 2)
			utils.makeUnit(iHaniwa, iCiv, tPlot, 3)
		
		if iCiv == iJin:
			#utils.makeUnit(iArcher, iCiv, tPlot, 2)
			utils.makeUnit(iJinDaoInfantry, iCiv, tPlot, 4)
			
		if iCiv == iByzantines:
			#utils.makeUnit(iMarksman, iCiv, tPlot, 4)
			utils.makeUnit(iByzantineFeodorati, iCiv, tPlot, 4)
		
		if iCiv == iGupta:
			utils.makeUnit(iBambooArcher, iCiv, tPlot, 4)
		
		if iCiv == iFranks:
			#utils.makeUnit(iSpearman, iCiv, tPlot, 4)
			utils.makeUnit(iFrankThrowingAxeman, iCiv, tPlot, 4)
		
		if iCiv == iChalukyans:
			#utils.makeUnit(iArcher, iCiv, tPlot, 2)
			utils.makeUnit(iSwordsman, iCiv, tPlot, 2)
			
		if iCiv == iGokturks:
			#utils.makeUnit(iMarksman, iCiv, tPlot, 8)
			utils.makeUnit(iGokturkWarrior, iCiv, tPlot, 5)
		
		if iCiv == iSrivajaya:
			#utils.makeUnit(iArcher, iCiv, tPlot, 2)
			utils.makeUnit(iAxeman, iCiv, tPlot, 2)
			
		if iCiv == iKhazars:
			utils.makeUnit(iHeavyHorseArcher, iCiv, tPlot, 3)
			utils.makeUnit(iKhazarArsiyah, iCiv, tPlot, 4)
			
		if iCiv == iTibet:
			utils.makeUnit(iSwordsman, iCiv, tPlot, 6)
			utils.makeUnit(iSpearman, iCiv, tPlot, 6)
		
		if iCiv == iTang:
			#utils.makeUnit(iArcher, iCiv, tPlot, 2)
			utils.makeUnit(iTibetKhampa, iCiv, tPlot, 3)
		
		if iCiv == iArabs:
			#utils.makeUnit(iArcher, iCiv, tPlot, 2)
			utils.makeUnit(iArabiaGhazi, iCiv, tPlot, 6)
			
	def createAdditionalMaccabeanUnits( self, iCiv, tPlot ):
	
		utils.makeUnit(iArcher, iCiv, tPlot, 2)
		utils.makeUnit(iCatapult, iCiv, tPlot, 2)


	def createStartingUnits(self, iPlayer, tPlot, iCiv = -1):
		"""Creates starting units for initBirth."""
		
		print ("createStartingUnits, iPlayer", iPlayer, "iCiv", iCiv)
		
		if iCiv == -1:
			iCiv = iPlayer
		iHandicap = gc.getGame().getHandicapType()
		
		if iCiv == iNubia:
			utils.makeUnit(iSettler, iPlayer, tPlot, 1)
			utils.makeUnit(iNubiaLongbowman, iPlayer, tPlot, 2)
			utils.makeUnit(iSpearman, iPlayer, tPlot, 2)
			utils.makeUnit(iWorker, iPlayer, tPlot, 1) # not covered by createStartingWorkers due to birth date
				
		if iCiv == iCelts:
			utils.makeUnit(iSettler, iPlayer, tPlot, 1)
			utils.makeUnit(iGallicWarrior, iPlayer, tPlot, 4)
			utils.makeUnit(iChariot, iPlayer, tPlot, 2)
				
		if iCiv == iPontus:
			utils.makeUnit(iSettler, iPlayer, tPlot, 1)
			utils.makeUnit(iHellenicMissionary, iPlayer, tPlot, 1)
			utils.makeUnit(iPonticUazali, iPlayer, tPlot, 2)
			utils.makeUnit(iJavelinman, iPlayer, tPlot, 2)
			
		if iCiv == iTocharians:
			utils.makeUnit(iSettler, iPlayer, tPlot, 1)
			utils.makeUnit(iTarimBowman, iPlayer, tPlot, 2)
			if iPlayer != utils.getHumanID():
				utils.makeUnit(iTarimBowman, iPlayer, tPlot, 2)
			
		if iCiv == iArmenia:
			utils.makeUnit(iSettler, iPlayer, tPlot, 1)
			utils.makeUnit(iArcher, iPlayer, tPlot, 2)
			utils.makeUnit(iSpearman, iPlayer, tPlot, 2)
			utils.makeUnit(iAzatavrear, iPlayer, tPlot, 2)
			
		if iCiv == iSaba:
			utils.makeUnit(iSettler, iPlayer, tPlot, 2)
			utils.makeUnit(iSpearman, iPlayer, tPlot, 2)
			utils.makeUnit(iWorker, iPlayer, tPlot, 1) # not covered by createStartingWorkers due to birth date
			tSeaPlot = utils.findSeaPlots(tPlot, 1, iPlayer)
			if tSeaPlot:
				utils.makeUnit(iGalley, iPlayer, tSeaPlot, 1)
				utils.makeUnit(iWorkBoat, iPlayer, tSeaPlot, 1)
			
		if iCiv == iHan:
			utils.makeUnit(iSettler, iPlayer, tPlot, 2)
			utils.makeUnit(iChokonu, iPlayer, tPlot, 6)
			utils.makeUnit(iChariot, iPlayer, tPlot, 2)
			utils.makeUnit(iSpearman, iPlayer, tPlot, 4)
			utils.makeUnit(iConfucianMissionary, iPlayer, tPlot, 2)
			if iPlayer != utils.getHumanID():
				utils.makeUnit(iChokonu, iPlayer, tPlot, 2)
				utils.makeUnit(iChariot, iPlayer, tPlot, 2)
				utils.makeUnit(iSpearman, iPlayer, tPlot, 2)
				
			
		if iCiv == iRome:
			utils.makeUnit(iSettler, iPlayer, tPlot, 2)
			utils.makeUnit(iHellenicMissionary, iPlayer, tPlot, 2)
			utils.makeUnit(iLegionary, iPlayer, tPlot, 3)
			utils.makeUnit(iJavelinman, iPlayer, tPlot, 2)
			if iPlayer != utils.getHumanID():
				utils.makeUnit(iLegionary, iPlayer, tPlot, 4)
				utils.makeUnit(iSettler, iPlayer, tPlot, 2)
				utils.makeUnit(iJavelinman, iPlayer, tPlot, 2)
				utils.makeUnit(iWorker, iPlayer, tPlot, 2)
			tSeaPlot = utils.findSeaPlots(tPlot, 1, iPlayer)
			if tSeaPlot:
				utils.makeUnit(iGalley, iPlayer, tSeaPlot, 1)
				utils.makeUnit(iLegionary, iPlayer, tSeaPlot, 2)
				utils.makeUnit(iJavelinman, iPlayer, tSeaPlot, 2)
				utils.makeUnit(iWorkBoat, iPlayer, tSeaPlot, 1)
				if iPlayer != utils.getHumanID():
					utils.makeUnit(iGalley, iPlayer, tSeaPlot, 1)
					utils.makeUnit(iLegionary, iPlayer, tSeaPlot, 4)
			
		if iCiv == iVietnam:
			utils.makeUnit(iSettler, iPlayer, tPlot, 2)
			utils.makeUnit(iArcher, iPlayer, tPlot, 3)
			tSeaPlot = utils.findSeaPlots(tPlot, 1, iPlayer)
			if tSeaPlot:
				utils.makeUnit(iWorkBoat, iPlayer, tSeaPlot, 1)
			
		if iCiv == iPandyans:
			utils.makeUnit(iSettler, iPlayer, tPlot, 1)
			#utils.makeUnit(iPandyanVillavar, iPlayer, tPlot, 1)
			#utils.makeUnit(iHinduMissionary, iPlayer, tPlot, 1)
			#tSeaPlot = utils.findSeaPlots(tPlot, 1, iPlayer)
			#if tSeaPlot:
				#utils.makeUnit(iGalley, iPlayer, tSeaPlot, 1)
				#utils.makeUnit(iWorkBoat, iPlayer, tSeaPlot, 1)
			#if iPlayer != utils.getHumanID():
				#utils.makeUnit(iPandyanVillavar, iPlayer, tPlot, 1)
				#utils.makeUnit(iSpearman, iPlayer, tPlot, 1)
			
		if iCiv == iBactria:
			utils.makeUnit(iSettler, iPlayer, tPlot, 2)
			utils.makeUnit(iArcher, iPlayer, tPlot, 3)
			utils.makeUnit(iSpearman, iPlayer, tPlot, 2)
			utils.makeUnit(iHetairoi, iPlayer, tPlot, 2)
			utils.makeUnit(iHellenicMissionary, iPlayer, tPlot, 1)
			if iPlayer != utils.getHumanID():
				utils.makeUnit(iSpearman, iPlayer, tPlot, 1)
				utils.makeUnit(iHetairoi, iPlayer, tPlot, 1)
				utils.makeUnit(iArcher, iPlayer, tPlot, 1)
				
			
		if iCiv == iMaccabees:
			utils.makeUnit(iMaccabee, iPlayer, tPlot, 2)
			utils.makeUnit(iSpearman, iPlayer, tPlot, 2)
			utils.makeUnit(iArcher, iPlayer, tPlot, 2)
			
		if iCiv == iSatavahana:
			utils.makeUnit(iSettler, iPlayer, tPlot, 2)
			utils.makeUnit(iArcher, iPlayer, tPlot, 2)
			utils.makeUnit(iSpearman, iPlayer, tPlot, 2)
			utils.makeUnit(iKshatriya, iPlayer, tPlot, 3)
			utils.makeUnit(iHinduMissionary, iPlayer, tPlot, 2)
			if iPlayer != utils.getHumanID():
				utils.makeUnit(iSettler, iPlayer, tPlot, 1)
				utils.makeUnit(iHinduMissionary, iPlayer, tPlot, 1)
				utils.makeUnit(iArcher, iPlayer, tPlot, 1)
			
		if iCiv == iParthia:
			utils.makeUnit(iZoroastrianMissionary, iPlayer, tPlot, 1)
			utils.makeUnit(iSettler, iPlayer, tPlot, 3)
			utils.makeUnit(iArcher, iPlayer, tPlot, 8)
			utils.makeUnit(iShivatir, iPlayer, tPlot, 8)
			if iCiv != utils.getHumanID():
				utils.makeUnit(iShivatir, iPlayer, tPlot, 8)
			if iRome == utils.getHumanID():
				utils.makeUnit(iShivatir, iPlayer, tPlot, 2)
			
		if iCiv == iDacia:
			utils.makeUnit(iSettler, iPlayer, tPlot, 2)
			utils.makeUnit(iArcher, iPlayer, tPlot, 4)
			utils.makeUnit(iFalxman, iPlayer, tPlot, 2)
			if iCiv != utils.getHumanID():
				utils.makeUnit(iFalxman, iPlayer, tPlot, 2)
				utils.makeUnit(iArcher, iPlayer, tPlot, 2)
			if iRome == utils.getHumanID():
				utils.makeUnit(iFalxman, iPlayer, tPlot, 2)
			
		if iCiv == iGoguryeo:
			utils.makeUnit(iSettler, iPlayer, tPlot, 2)
			utils.makeUnit(iMarksman, iPlayer, tPlot, 2)
			utils.makeUnit(iHeavySpearman, iPlayer, tPlot, 2)
			if iHan == iHuman or iQin == iHuman:
				utils.makeUnit(iHeavySpearman, iPlayer, tPlot, 2)
			
		if iCiv == iKushans:
			utils.makeUnit(iSettler, iPlayer, tPlot, 2)
			utils.makeUnit(iArcher, iPlayer, tPlot, 7)
			utils.makeUnit(iHorseArcher_Kushan, iPlayer, tPlot, 7)
			if iCiv != utils.getHumanID():
				utils.makeUnit(iHorseArcher_Kushan, iPlayer, tPlot, 7)
				utils.makeUnit(iArcher, iPlayer, tPlot, 5)
				utils.makeUnit(iSettler, iPlayer, tPlot, 1)
			
		if iCiv == iAxum:
			utils.makeUnit(iSettler, iPlayer, tPlot, 2)
			utils.makeUnit(iArcher, iPlayer, tPlot, 2)
			utils.makeUnit(iAxumSarawit, iPlayer, tPlot, 2)
			utils.makeUnit(iHorseman, iPlayer, tPlot, 1)
			tSeaPlot = (65, 22)
			if tSeaPlot:
				utils.makeUnit(iGalley, iPlayer, tSeaPlot, 2)
				utils.makeUnit(iWarGalley, iPlayer, tSeaPlot, 1)
				utils.makeUnit(iWorkBoat, iPlayer, tSeaPlot, 2)
				
		if iCiv == iFunan:
			utils.makeUnit(iSettler, iPlayer, tPlot, 2)
			utils.makeUnit(iArcher, iPlayer, tPlot, 2)
			utils.makeUnit(iSpearman, iPlayer, tPlot, 2)
			utils.makeUnit(iFunanSurinSoldier, iPlayer, tPlot, 2)
			if iSatavahana != utils.getHumanID():
				utils.makeUnit(iHinduMissionary, iPlayer, tPlot, 1)
				utils.makeUnit(iBuddhistMissionary, iPlayer, tPlot, 1)
			
		if iCiv == iSassanids:
			utils.makeUnit(iSettler, iPlayer, tPlot, 1)
			utils.makeUnit(iMarksman, iPlayer, tPlot, 4)
			utils.makeUnit(iHeavySpearman, iPlayer, tPlot, 4)
			utils.makeUnit(iHorseArcher, iPlayer, tPlot, 5)
			utils.makeUnit(iSassanidCataphract, iPlayer, tPlot, 5)
			#utils.makeUnit(iCatapult, iPlayer, tPlot, 2)
			utils.makeUnit(iZoroastrianMissionary, iPlayer, tPlot, 2)
			if iCiv != utils.getHumanID():
				utils.makeUnit(iHorseArcher, iPlayer, tPlot, 2)
				utils.makeUnit(iSassanidCataphract, iPlayer, tPlot, 2)
				#utils.makeUnit(iCatapult, iPlayer, tPlot, 2)
			
		if iCiv == iYamato:
			utils.makeUnit(iSettler, iPlayer, tPlot, 2)
			utils.makeUnit(iMarksman, iPlayer, tPlot, 2)
			utils.makeUnit(iHaniwa, iPlayer, tPlot, 2)
			tSeaPlot = utils.findSeaPlots(tPlot, 1, iPlayer)
			if tSeaPlot:
				utils.makeUnit(iGalley, iPlayer, tSeaPlot, 2)
		
		if iCiv == iJin:
			utils.makeUnit(iSettler, iPlayer, tPlot, 2)
			utils.makeUnit(iMarksman, iPlayer, tPlot, 5)
			utils.makeUnit(iJinDaoInfantry, iPlayer, tPlot, 5)
		
		if iCiv == iByzantines:
			utils.makeUnit(iSettler, iPlayer, tPlot, 1)
			utils.makeUnit(iChristianMissionary, iPlayer, tPlot, 3)
			utils.makeUnit(iHeavySpearman, iPlayer, tPlot, 1)
			utils.makeUnit(iByzantineFeodorati, iPlayer, tPlot, 1)
			pByzantines.AI_changeAttitudeExtra(iRome, 3)
			pRome.AI_changeAttitudeExtra(iByzantines, 3)
			gc.getTeam(pByzantines.getTeam()).signOpenBorders(iRome)
			tSeaPlot = utils.findSeaPlots(tPlot, 1, iPlayer)
			if tSeaPlot:
				utils.makeUnit(iWarGalley, iPlayer, tSeaPlot, 3)
		
		if iCiv == iGupta:
			utils.makeUnit(iSettler, iPlayer, tPlot, 1)
			utils.makeUnit(iBambooArcher, iPlayer, tPlot, 5)
			utils.makeUnit(iHinduMissionary, iPlayer, tPlot, 1)
			#if iCiv != utils.getHumanID():
				#utils.makeUnit(iBambooArcher, iPlayer, tPlot, 5)
				#utils.makeUnit(iWarElephant, iPlayer, tPlot, 3)
		
		if iCiv == iVisigoths:
			utils.makeUnit(iSettler, iPlayer, tPlot, 1)
			utils.makeUnit(iSwordsman, iPlayer, tPlot, 2)
			utils.makeUnit(iVisigothComitatus, iPlayer, tPlot, 2)
			if self.isChristianitySplit():
				gc.getPlayer(iVisigoths).setLastStateReligion(iArianism)
				utils.makeUnit(iArianMissionary, iPlayer, tPlot, 2)
			else:
				gc.getPlayer(iVisigoths).setLastStateReligion(iChristianity)
				utils.makeUnit(iChristianMissionary, iPlayer, tPlot, 2)
		
		if iCiv == iVandals:
			utils.makeUnit(iSettler, iPlayer, tPlot, 1)
			utils.makeUnit(iSwordsman, iPlayer, tPlot, 2)
			utils.makeUnit(iVandalMountedWarrior, iPlayer, tPlot, 2)
			if self.isChristianitySplit():
				gc.getPlayer(iVandals).setLastStateReligion(iArianism)
				utils.makeUnit(iArianMissionary, iPlayer, tPlot, 2)
			else:
				gc.getPlayer(iVandals).setLastStateReligion(iChristianity)
				utils.makeUnit(iChristianMissionary, iPlayer, tPlot, 2)
			tSeaPlot = utils.findSeaPlots(tPlot, 1, iPlayer)
			if tSeaPlot:
				utils.makeUnit(iGalley, iPlayer, tSeaPlot, 2)
				utils.makeUnit(iWarGalley, iPlayer, tSeaPlot, 2)
		
		if iCiv == iOstrogoths:
			utils.makeUnit(iSettler, iPlayer, tPlot, 2)
			utils.makeUnit(iOstrogothSwordsman, iPlayer, tPlot, 4)
			utils.makeUnit(iLancer, iPlayer, tPlot, 2)
			if self.isChristianitySplit():
				gc.getPlayer(iOstrogoths).setLastStateReligion(iArianism)
				utils.makeUnit(iArianMissionary, iPlayer, tPlot, 2)
			else:
				gc.getPlayer(iOstrogoths).setLastStateReligion(iChristianity)
				utils.makeUnit(iChristianMissionary, iPlayer, tPlot, 2)
		
		if iCiv == iFranks:
			utils.makeUnit(iSettler, iPlayer, tPlot, 2)
			utils.makeUnit(iHeavySpearman, iPlayer, tPlot, 4)
			utils.makeUnit(iFrankThrowingAxeman, iPlayer, tPlot, 2)
			utils.makeUnit(iLancer, iPlayer, tPlot, 2)
			if self.isChristianitySplit():
				gc.getPlayer(iFranks).setLastStateReligion(iCatholicism)
				utils.makeUnit(iCatholicMissionary, iPlayer, tPlot, 2)
			else:
				gc.getPlayer(iFranks).setLastStateReligion(iChristianity)
				utils.makeUnit(iChristianMissionary, iPlayer, tPlot, 2)
		
		if iCiv == iChalukyans:
			utils.makeUnit(iSettler, iPlayer, tPlot, 1)
			utils.makeUnit(iMarksman, iPlayer, tPlot, 4)
			utils.makeUnit(iSwordsman, iPlayer, tPlot, 4)
			utils.makeUnit(iHinduMissionary, iPlayer, tPlot, 1)
		
		if iCiv == iLombards:
			utils.makeUnit(iSettler, iPlayer, tPlot, 2)
			if self.isChristianitySplit():
				gc.getPlayer(iLombards).setLastStateReligion(iArianism)
				utils.makeUnit(iArianMissionary, iPlayer, tPlot, 2)
			else:
				gc.getPlayer(iLombards).setLastStateReligion(iChristianity)
				utils.makeUnit(iChristianMissionary, iPlayer, tPlot, 2)
			utils.makeUnit(iLombardMilitia, iPlayer, tPlot, 4)
			utils.makeUnit(iLancer, iPlayer, tPlot, 2)
			
		if iCiv == iGokturks:
			t2ndPlot = (106, 63) # Almaliq
			utils.makeUnit(iSettler, iPlayer, tPlot, 3)
			utils.makeUnit(iMarksman, iPlayer, tPlot, 6)
			utils.makeUnit(iGokturkWarrior, iPlayer, tPlot, 8)
			if iCiv != utils.getHumanID():
				utils.makeUnit(iGokturkWarrior, iPlayer, tPlot, 6)
			utils.makeUnit(iSettler, iPlayer, t2ndPlot, 2)
			utils.makeUnit(iMarksman, iPlayer, t2ndPlot, 4)
			utils.makeUnit(iGokturkWarrior, iPlayer, t2ndPlot, 6)
		
		if iCiv == iSrivajaya:
			utils.makeUnit(iSettler, iPlayer, tPlot, 1)
			utils.makeUnit(iArcher, iPlayer, tPlot, 2)
			utils.makeUnit(iHinduMissionary, iPlayer, tPlot, 1)
			utils.makeUnit(iBuddhistMissionary, iPlayer, tPlot, 1)
			tSeaPlot = utils.findSeaPlots(tPlot, 1, iPlayer)
			if tSeaPlot:
				utils.makeUnit(iBalangay, iPlayer, tSeaPlot, 1)
				utils.makeUnit(iSettler, iPlayer, tSeaPlot, 1)
				utils.makeUnit(iArcher, iPlayer, tSeaPlot, 1)
				utils.makeUnit(iArcher, iPlayer, tSeaPlot, 1)
				utils.makeUnit(iWorkBoat, iPlayer, tSeaPlot, 3)
			
		if iCiv == iKhazars:
			utils.makeUnit(iSettler, iPlayer, tPlot, 3)
			utils.makeUnit(iMarksman, iPlayer, tPlot, 3)
			utils.makeUnit(iKhazarArsiyah, iPlayer, tPlot, 6)
			utils.makeUnit(iHeavyHorseArcher, iPlayer, tPlot, 4)
			if iCiv != utils.getHumanID():
				utils.makeUnit(iKhazarArsiyah, iPlayer, tPlot, 6)
				utils.makeUnit(iHeavyHorseArcher, iPlayer, tPlot, 4)
		
		if iCiv == iTibet:
			utils.makeUnit(iSettler, iPlayer, tPlot, 2)
			utils.makeUnit(iMarksman, iPlayer, tPlot, 3)
			utils.makeUnit(iTibetKhampa, iPlayer, tPlot, 2)
			utils.makeUnit(iBuddhistMissionary, iPlayer, tPlot, 2)
		
		if iCiv == iTang:
			utils.makeUnit(iSettler, iPlayer, tPlot, 1)
			utils.makeUnit(iMarksman, iPlayer, tPlot, 5)
			utils.makeUnit(iShenwuGuard, iPlayer, tPlot, 8)
			utils.makeUnit(iBuddhistMissionary, iPlayer, tPlot, 3)
		
		if iCiv == iArabs:
			utils.makeUnit(iSettler, iPlayer, tPlot, 1)
			utils.makeUnit(iMarksman, iPlayer, tPlot, 12)
			utils.makeUnit(iArabiaGhazi, iPlayer, tPlot, 12)
			utils.makeUnit(iGreatProphet, iPlayer, tPlot, 1)
		
		if iCiv == iGhana:
			utils.makeUnit(iSettler, iPlayer, tPlot, 1)
			utils.makeUnit(iArcher, iPlayer, tPlot, 1)
			utils.makeUnit(iHeavySpearman, iPlayer, tPlot, 1)
		
		if iCiv == iPallavas:
			utils.makeUnit(iMarksman, iPlayer, tPlot, 4)
			utils.makeUnit(iHeavySpearman, iPlayer, tPlot, 4)
		
		if iCiv == iWu:
			utils.makeUnit(iMarksman, iPlayer, tPlot, 4)
			utils.makeUnit(iHeavySpearman, iPlayer, tPlot, 4)
			utils.makeUnit(iCatapult, iPlayer, tPlot, 1)
		
		if iCiv == iShu:
			utils.makeUnit(iMarksman, iPlayer, tPlot, 4)
			utils.makeUnit(iHeavySpearman, iPlayer, tPlot, 4)
			utils.makeUnit(iCatapult, iPlayer, tPlot, 1)
		
		if iCiv == iHarsha:
			utils.makeUnit(iMarksman, iPlayer, tPlot, 4)
			utils.makeUnit(iSwordsman, iPlayer, tPlot, 3)
			utils.makeUnit(iArmoredElephant, iPlayer, tPlot, 1)
			utils.makeUnit(iBuddhistMissionary, iPlayer, tPlot, 2)
			
		# immobilize all units exceept 1 settler to prevent wandering before the flip
		if iPlayer != utils.getHumanID():
			bSettler = False
			plot = gc.getMap().plot(tPlot[0], tPlot[1])
			iNumUnitsInAPlot = plot.getNumUnits()
			if (iNumUnitsInAPlot):
				for i in range(iNumUnitsInAPlot):
					unit = plot.getUnit(i)
					if (unit.getOwner() == iCiv):
						if unit.getUnitType() == iSettler:
							if bSettler == False:
								bSettler = True
								continue
							else:
								unit.setImmobileTimer(2)
						else:
							unit.setImmobileTimer(2)
			
			
		# hit neighbours stability
		#self.hitNeighboursStability(iCiv)
		
			
	
		
		# init contacts
		pPlayer = gc.getPlayer(iPlayer)
		pTeam = gc.getTeam(pPlayer.getTeam())
		for i in range(len(lContactCivsOnSpawn[iCiv])):
			iCivToMeet = lContactCivsOnSpawn[iCiv][i]
			if gc.getTeam(gc.getPlayer(iCivToMeet).getTeam()).isAlive() and not pTeam.isHasMet(iCivToMeet):
				pTeam.meet(iCivToMeet, False)
		
		# edead: war on spawn I - declare war on civs from the list
		for iEnemyCiv in lEnemyCivsOnSpawn[iCiv]:
			if utils.isActive(iEnemyCiv):
				if iCiv == iHan and iCiv != utils.getHumanID() and iEnemyCiv != utils.getHumanID() and iEnemyCiv in [iQin]:
					gc.getTeam(pPlayer.getTeam()).declareWar(iEnemyCiv, False, WarPlanTypes.WARPLAN_TOTAL)
				if iCiv == iParthia and iCiv != utils.getHumanID() and iEnemyCiv != utils.getHumanID() and iEnemyCiv in [iSeleucids]:
					gc.getTeam(pPlayer.getTeam()).declareWar(iEnemyCiv, False, WarPlanTypes.WARPLAN_TOTAL)
				if iCiv == iArabs and iCiv != utils.getHumanID() and iEnemyCiv != utils.getHumanID() and iEnemyCiv in [iSassanids]:
					gc.getTeam(pPlayer.getTeam()).declareWar(iEnemyCiv, False, WarPlanTypes.WARPLAN_TOTAL)
				else:
					gc.getTeam(pPlayer.getTeam()).declareWar(iEnemyCiv, False, -1)
		
		# edead: reveal some map
		plotList = []
		for x in range(iMapWidth):
			for y in range(iMapHeight):
				plotList.append((x, y))
		print ("reveal map, iPlayer", iPlayer, "iCiv", iCiv)
		utils.unrevealPlots(iPlayer, plotList)
		utils.revealPlots(iPlayer, utils.getRegionPlotList(lRevealRegions[iCiv], True)) 
		
		
		

		
		self.assignTechs(iPlayer, iCiv)
		#if iPlayer == utils.getHumanID():
			#for iLoopCiv in range (iNumPlayers):
				#if gc.getPlayer(iLoopCiv).isAlive():
					#DynamicCivs.checkName(iLoopCiv)
					
		if utils.getHumanID() == iRome and iPlayer == iRome:
			self.romanUHVChoicePopup() 
			
		if iPlayer == iPandyans:
			if utils.getHumanID() == iPandyans:
				self.tamilKingdomsPopup()
			else:
				iRand = gc.getGame().getSorenRandNum(100, 'random number')
				if iRand < 50:
					self.do3KingdomsChola()
				else:
					self.do3KingdomsPandyan()
			
			

			
			
	def createCityAttackUnits(self, iPlayer, tPlot, iDefender, iCiv = -1, iBonus = 0, eDirectionType = DirectionTypes.DIRECTION_SOUTH):
	
		
		self.assignTechs(iPlayer, iCiv)
			
			
		if iCiv == iAntigonids:
			utils.makeUnit(iSpearman, iPlayer, tPlot, 2, eDirectionType)
			utils.makeUnit(iHeavySpearman, iPlayer, tPlot, 1 + iBonus, eDirectionType, UnitAITypes.UNITAI_ATTACK_CITY_LEMMING)
			utils.makeUnit(iCatapult, iPlayer, tPlot, 1 + iBonus, eDirectionType, UnitAITypes.UNITAI_ATTACK_CITY_LEMMING)
		
		if iCiv == iSungas:
			utils.makeUnit(iArcher, iPlayer, tPlot, 1, eDirectionType)
			utils.makeUnit(iSpearman, iPlayer, tPlot, 1, eDirectionType)
			utils.makeUnit(iAxeman, iPlayer, tPlot, 1 + iBonus, eDirectionType, UnitAITypes.UNITAI_ATTACK_CITY_LEMMING)
			utils.makeUnit(iWarElephant, iPlayer, tPlot, 1 + iBonus, eDirectionType, UnitAITypes.UNITAI_ATTACK_CITY_LEMMING)
		
		if iCiv == iHarsha:
			utils.makeUnit(iMarksman, iPlayer, tPlot, 1, eDirectionType)
			utils.makeUnit(iHeavySpearman, iPlayer, tPlot, 1, eDirectionType)
			utils.makeUnit(iSwordsman, iPlayer, tPlot, 1 + iBonus, eDirectionType, UnitAITypes.UNITAI_ATTACK_CITY_LEMMING)
			utils.makeUnit(iArmoredElephant, iPlayer, tPlot, iBonus, eDirectionType, UnitAITypes.UNITAI_ATTACK_CITY_LEMMING)
		
		if iCiv == iRome:
			utils.makeUnit(iLegionary, iPlayer, tPlot, 2 + iBonus, eDirectionType, UnitAITypes.UNITAI_ATTACK_CITY_LEMMING)
			utils.makeUnit(iCatapult, iPlayer, tPlot, 1 + iBonus, eDirectionType, UnitAITypes.UNITAI_ATTACK_CITY_LEMMING)
			utils.makeUnit(iLegionary, iPlayer, tPlot, 1 + iBonus, eDirectionType)
		
		if iCiv == iVietnam:
			utils.makeUnit(iAuLacCrossbowman, iPlayer, tPlot, 2 + iBonus, eDirectionType, UnitAITypes.UNITAI_ATTACK_CITY_LEMMING)
			utils.makeUnit(iCatapult, iPlayer, tPlot, 1 + iBonus, eDirectionType, UnitAITypes.UNITAI_ATTACK_CITY_LEMMING)
			utils.makeUnit(iSpearman, iPlayer, tPlot, 1, eDirectionType)
		
		if iCiv == iYamato:
			utils.makeUnit(iHaniwa, iPlayer, tPlot, 2 + iBonus, eDirectionType, UnitAITypes.UNITAI_ATTACK_CITY_LEMMING)
			utils.makeUnit(iCatapult, iPlayer, tPlot, 1 + iBonus, eDirectionType, UnitAITypes.UNITAI_ATTACK_CITY_LEMMING)
			utils.makeUnit(iSpearman, iPlayer, tPlot, 1, eDirectionType)
		
		if iCiv == iArmenia:
			utils.makeUnit(iAzatavrear, iPlayer, tPlot, 2 + iBonus, eDirectionType, UnitAITypes.UNITAI_ATTACK_CITY_LEMMING)
			utils.makeUnit(iSpearman, iPlayer, tPlot, 2, eDirectionType, UnitAITypes.UNITAI_ATTACK_CITY_LEMMING)
			utils.makeUnit(iArcher, iPlayer, tPlot, 2, eDirectionType)
		
		if iCiv == iGoguryeo:
			utils.makeUnit(iGoguryeoGaemamusa, iPlayer, tPlot, 2 + iBonus, eDirectionType, UnitAITypes.UNITAI_ATTACK_CITY_LEMMING)
			utils.makeUnit(iSpearman, iPlayer, tPlot, 2, eDirectionType, UnitAITypes.UNITAI_ATTACK_CITY_LEMMING)
			utils.makeUnit(iArcher, iPlayer, tPlot, 2, eDirectionType)
		
		if iCiv == iParthia:
			utils.makeUnit(iShivatir, iPlayer, tPlot, 2 + iBonus, eDirectionType, UnitAITypes.UNITAI_ATTACK_CITY_LEMMING)
			utils.makeUnit(iSpearman, iPlayer, tPlot, 2, eDirectionType, UnitAITypes.UNITAI_ATTACK_CITY_LEMMING)
			utils.makeUnit(iArcher, iPlayer, tPlot, 2, eDirectionType)
		
		if iCiv == iSassanids:
			utils.makeUnit(iSassanidCataphract, iPlayer, tPlot, 2 + iBonus, eDirectionType, UnitAITypes.UNITAI_ATTACK_CITY_LEMMING)
			utils.makeUnit(iHeavySpearman, iPlayer, tPlot, 2, eDirectionType, UnitAITypes.UNITAI_ATTACK_CITY_LEMMING)
			utils.makeUnit(iMarksman, iPlayer, tPlot, 2, eDirectionType, UnitAITypes.UNITAI_ATTACK_CITY_LEMMING)
		
		if iCiv == iNanYue:
			utils.makeUnit(iArcher, iPlayer, tPlot, 1, eDirectionType)
			utils.makeUnit(iSpearman, iPlayer, tPlot, 1, eDirectionType)
			utils.makeUnit(iAxeman, iPlayer, tPlot, 2 + iBonus, eDirectionType, UnitAITypes.UNITAI_ATTACK_CITY_LEMMING)
			utils.makeUnit(iCatapult, iPlayer, tPlot, 1 + iBonus, eDirectionType, UnitAITypes.UNITAI_ATTACK_CITY_LEMMING)
		
		if iCiv in [iFunan, iMauryans, iKalinka, iPandyans, iNubia, iSaba, iAxum]:
			utils.makeUnit(iArcher, iPlayer, tPlot, 2, eDirectionType)
			utils.makeUnit(iSpearman, iPlayer, tPlot, 2, eDirectionType, UnitAITypes.UNITAI_ATTACK_CITY_LEMMING)
			utils.makeUnit(iAxeman, iPlayer, tPlot, 1 + iBonus, eDirectionType, UnitAITypes.UNITAI_ATTACK_CITY_LEMMING)
			utils.makeUnit(iCatapult, iPlayer, tPlot, 1 + iBonus, eDirectionType, UnitAITypes.UNITAI_ATTACK_CITY_LEMMING)
		
		if iCiv in [iTocharians, iGojoseon]:
			utils.makeUnit(iArcher, iPlayer, tPlot, 2, eDirectionType)
			utils.makeUnit(iSpearman, iPlayer, tPlot, 2, eDirectionType, UnitAITypes.UNITAI_ATTACK_CITY_LEMMING)
			utils.makeUnit(iHorseman, iPlayer, tPlot, 2 + iBonus, eDirectionType, UnitAITypes.UNITAI_ATTACK_CITY_LEMMING)
			utils.makeUnit(iCatapult, iPlayer, tPlot, 1, eDirectionType, UnitAITypes.UNITAI_ATTACK_CITY_LEMMING)
		
		if iCiv == iNumidia:
			utils.makeUnit(iArcher, iPlayer, tPlot, 1, eDirectionType)
			utils.makeUnit(iSpearman, iPlayer, tPlot, 1, eDirectionType, UnitAITypes.UNITAI_ATTACK_CITY_LEMMING)
			utils.makeUnit(iHorseman, iPlayer, tPlot, 3 + iBonus, eDirectionType, UnitAITypes.UNITAI_ATTACK_CITY_LEMMING)
		
		if iCiv == iShu:
			utils.makeUnit(iArcher, iPlayer, tPlot, 2, eDirectionType)
			utils.makeUnit(iSpearman, iPlayer, tPlot, 2, eDirectionType, UnitAITypes.UNITAI_ATTACK_CITY_LEMMING)
			utils.makeUnit(iAxeman, iPlayer, tPlot, 2 + iBonus, eDirectionType, UnitAITypes.UNITAI_ATTACK_CITY_LEMMING)
			utils.makeUnit(iCatapult, iPlayer, tPlot, 1 + iBonus, eDirectionType, UnitAITypes.UNITAI_ATTACK_CITY_LEMMING)
		
		if iCiv == iWu:
			utils.makeUnit(iArcher, iPlayer, tPlot, 2, eDirectionType)
			utils.makeUnit(iSpearman, iPlayer, tPlot, 2, eDirectionType, UnitAITypes.UNITAI_ATTACK_CITY_LEMMING)
			utils.makeUnit(iAxeman, iPlayer, tPlot, 2 + iBonus, eDirectionType, UnitAITypes.UNITAI_ATTACK_CITY_LEMMING)
			utils.makeUnit(iCatapult, iPlayer, tPlot, 1 + iBonus, eDirectionType, UnitAITypes.UNITAI_ATTACK_CITY_LEMMING)
		
		if iCiv == iSong:
			utils.makeUnit(iMarksman, iPlayer, tPlot, 2, eDirectionType)
			utils.makeUnit(iHeavySpearman, iPlayer, tPlot, 3, eDirectionType, UnitAITypes.UNITAI_ATTACK_CITY_LEMMING)
			utils.makeUnit(iCatapult, iPlayer, tPlot, 1 + iBonus, eDirectionType, UnitAITypes.UNITAI_ATTACK_CITY_LEMMING)
		
		if iCiv == iScythians:
			utils.makeUnit(iHorseArcher, iPlayer, tPlot, 3 + iBonus, eDirectionType, UnitAITypes.UNITAI_ATTACK_CITY_LEMMING)
			utils.makeUnit(iArcher, iPlayer, tPlot, 1, eDirectionType)
			utils.makeUnit(iSpearman, iPlayer, tPlot, 1, eDirectionType, UnitAITypes.UNITAI_ATTACK_CITY_LEMMING)
		
		if iCiv == iXiongnu:
			utils.makeUnit(iHorseman, iPlayer, tPlot, 2 + iBonus, eDirectionType, UnitAITypes.UNITAI_ATTACK_CITY_LEMMING)
			utils.makeUnit(iArcher, iPlayer, tPlot, 1, eDirectionType)
			utils.makeUnit(iSpearman, iPlayer, tPlot, 1, eDirectionType)
		
		if iCiv == iXianbei:
			utils.makeUnit(iHorseArcher, iPlayer, tPlot, 4 + iBonus, eDirectionType, UnitAITypes.UNITAI_ATTACK_CITY_LEMMING)
			utils.makeUnit(iArcher, iPlayer, tPlot, 1, eDirectionType)
			utils.makeUnit(iSpearman, iPlayer, tPlot, 1, eDirectionType)
		
		if iCiv == iHephthalites:
			utils.makeUnit(iHeavyHorseArcher, iPlayer, tPlot, 4 + iBonus, eDirectionType, UnitAITypes.UNITAI_ATTACK_CITY_LEMMING)
			utils.makeUnit(iMarksman, iPlayer, tPlot, 2, eDirectionType)
		
		if iCiv == iHuns:
			utils.makeUnit(iHeavyHorseArcher, iPlayer, tPlot, 5 + iBonus, eDirectionType, UnitAITypes.UNITAI_ATTACK_CITY_LEMMING)
			utils.makeUnit(iMarksman, iPlayer, tPlot, 2, eDirectionType)
		
		if iCiv == iAvars:
			utils.makeUnit(iHeavyHorseArcher, iPlayer, tPlot, 4 + iBonus, eDirectionType, UnitAITypes.UNITAI_ATTACK_CITY_LEMMING)
			utils.makeUnit(iMarksman, iPlayer, tPlot, 3, eDirectionType)
			utils.makeUnit(iTrebuchet, iPlayer, tPlot, 2, eDirectionType, UnitAITypes.UNITAI_ATTACK_CITY_LEMMING)
		
		if iCiv == iPallavas:
			utils.makeUnit(iSwordsman, iPlayer, tPlot, 2 + iBonus, eDirectionType, UnitAITypes.UNITAI_ATTACK_CITY_LEMMING)
			utils.makeUnit(iHeavySpearman, iPlayer, tPlot, 1, eDirectionType, UnitAITypes.UNITAI_ATTACK_CITY_LEMMING)
			utils.makeUnit(iMarksman, iPlayer, tPlot, 1, eDirectionType)
			utils.makeUnit(iTrebuchet, iPlayer, tPlot, 1, eDirectionType, UnitAITypes.UNITAI_ATTACK_CITY_LEMMING)
		
		if iCiv == iKalabhras:
			utils.makeUnit(iSwordsman, iPlayer, tPlot, 2 + iBonus, eDirectionType, UnitAITypes.UNITAI_ATTACK_CITY_LEMMING)
			utils.makeUnit(iHeavySpearman, iPlayer, tPlot, 1, eDirectionType, UnitAITypes.UNITAI_ATTACK_CITY_LEMMING)
			utils.makeUnit(iMarksman, iPlayer, tPlot, 1, eDirectionType)
			utils.makeUnit(iTrebuchet, iPlayer, tPlot, 1, eDirectionType, UnitAITypes.UNITAI_ATTACK_CITY_LEMMING)
		
		if iCiv == iVakatakas:
			utils.makeUnit(iSwordsman, iPlayer, tPlot, 2 + iBonus, eDirectionType, UnitAITypes.UNITAI_ATTACK_CITY_LEMMING)
			utils.makeUnit(iHeavySpearman, iPlayer, tPlot, 1, eDirectionType, UnitAITypes.UNITAI_ATTACK_CITY_LEMMING)
			utils.makeUnit(iMarksman, iPlayer, tPlot, 1, eDirectionType)
			utils.makeUnit(iTrebuchet, iPlayer, tPlot, 1, eDirectionType, UnitAITypes.UNITAI_ATTACK_CITY_LEMMING)
		
		if iCiv == iRouran:
			utils.makeUnit(iHeavyHorseArcher, iPlayer, tPlot, 4 + iBonus, eDirectionType, UnitAITypes.UNITAI_ATTACK_CITY_LEMMING)
			utils.makeUnit(iMarksman, iPlayer, tPlot, 3, eDirectionType)
		
		if iCiv == iArabs:
			utils.makeUnit(iArabiaGhazi, iPlayer, tPlot, 3 + iBonus, eDirectionType, UnitAITypes.UNITAI_ATTACK_CITY_LEMMING)
			utils.makeUnit(iMarksman, iPlayer, tPlot, 2, eDirectionType)
			utils.makeUnit(iTrebuchet, iPlayer, tPlot, 1, eDirectionType, UnitAITypes.UNITAI_ATTACK_CITY_LEMMING)
		
		if iCiv == iMoors:
			utils.makeUnit(iLancer, iPlayer, tPlot, 6 + iBonus, eDirectionType, UnitAITypes.UNITAI_ATTACK_CITY_LEMMING)
			utils.makeUnit(iSwordsman, iPlayer, tPlot, 6 + iBonus, eDirectionType, UnitAITypes.UNITAI_ATTACK_CITY_LEMMING)
			utils.makeUnit(iMarksman, iPlayer, tPlot, 6, eDirectionType)
			utils.makeUnit(iTrebuchet, iPlayer, tPlot, 3, eDirectionType, UnitAITypes.UNITAI_ATTACK_CITY_LEMMING)
			
		# init contacts
		pPlayer = gc.getPlayer(iPlayer)
		pTeam = gc.getTeam(pPlayer.getTeam())
		for i in range(len(lContactCivsOnSpawn[iCiv])):
			iCivToMeet = lContactCivsOnSpawn[iCiv][i]
			if gc.getTeam(gc.getPlayer(iCivToMeet).getTeam()).isAlive() and not pTeam.isHasMet(iCivToMeet):
				pTeam.meet(iCivToMeet, True)
			
	def createSettlerAndGarrison(self, iPlayer, tPlot, iCiv = -1):
		
		if iCiv == -1:
			iCiv = iPlayer
			
		if iCiv in [iVisigoths, iOstrogoths, iVandals]:
			utils.makeUnit(iSettler, iPlayer, tPlot, 1)
			utils.makeUnit(iMarksman, iPlayer, tPlot, 1)
			utils.makeUnit(iHeavySpearman, iPlayer, tPlot, 1)
			
		if iCiv in [iScythians, iHephthalites, iHuns, iAvars, iRouran]:
			utils.makeUnit(iSettler, iPlayer, tPlot, 1)
			utils.makeUnit(iMarksman, iPlayer, tPlot, 2)
			
		if iCiv in [iNumidia, iNanYue]:
			utils.makeUnit(iSettler, iPlayer, tPlot, 1)
			utils.makeUnit(iArcher, iPlayer, tPlot, 2)
			utils.makeUnit(iSpearman, iPlayer, tPlot, 2)
			
			
		



	def createPostFlipUnits(self, iCiv):
		"""Creates extra units in flipped cities."""
		
		if iHuman in lEnemyCivsOnSpawn[iCiv]:
			apCityList = PyPlayer(iCiv).getCityList()
			for pCity in apCityList:
				utils.createGarrisons((pCity.getX(), pCity.getY()), iCiv, 1)


	def createStartingWorkers(self, iCiv, tPlot):
		"""Creates workers for the specified civ."""
		
		iNumWorkers = 2
		if iCiv == iNubia: iNumWorkers -= 1
		if iCiv in [iCelts, iVisigoths, iOstrogoths, iVandals, iFranks, iLombards, iByzantines, iJin, iTang, iSassanids, iGupta, iArabs]: iNumWorkers -= 2
		if iCiv == iRome: iNumWorkers += 1
		#if utils.getYear() > 100: iNumWorkers = 4
		#elif utils.getYear() > -150: iNumWorkers = 3
		utils.makeUnit(iWorker, iCiv, tPlot, iNumWorkers)


	def createEarlyStartingUnits(self):
		"""Creates a settler and a scout for early start civs and the human player."""
		#print "createEarlyStartingUnits"
		iHuman = utils.getHumanID()
		if tBirth[iHuman] != -321:
			utils.makeUnit(iCatapult, iHuman, (iCatapultX, iCatapultY), 1)
		# late start condition
		if (gc.getPlayer(iSeleucids).isPlayable()):
			for iCiv in range(iNumPlayers):
				if tBirth[iCiv] == -321:
					self.createStartingUnits(iCiv, tCapitals[iCiv], sd.getCivilization(iCiv))
				else:
					break
		


	def assignTechs(self, iPlayer, iCiv):
		"""Assigns techs to the specific civ based on the starting tech table."""
		pTeam = gc.getTeam(gc.getPlayer(iPlayer).getTeam())
		for iLoopTech in range(iNumTechs):
			pTeam.setHasTech(iLoopTech, False, iPlayer, False, False) # srpt clear old techs first
		for iLoopTech in range(len(lStartingTechs[iCiv])):
			pTeam.setHasTech(lStartingTechs[iCiv][iLoopTech], True, iPlayer, False, False)
			if iPlayer == utils.getHumanID():
				pTeam.setHasTech(iImperialismTech, False, iPlayer, False, False)
			



	def hitNeighboursStability( self, iPlayer ):
		
		if (len(lOlderNeighbours[sd.getCivilization(iPlayer)])):
			for iLoop in lOlderNeighbours[sd.getCivilization(iPlayer)]:
				#print ("hitNeighboursStability, iPlayer=", iPlayer, "Neighbor =", iLoop)
				utils.stabilityCheck(iLoop, -3)
				
	


	def moveCapital (self, tCoords, iPlayer, bHuman=False):
		"""Moves the AI's capital to the specified city."""
		
		if tCoords[0] == -1 or tCoords[1] == -1:
			return False
		
		pNewCapital = gc.getMap().plot(tCoords[0], tCoords[1]).getPlotCity()
		if pNewCapital and not pNewCapital.isNone(): 
			if pNewCapital.getNumRealBuilding(iPalace) > 0:
				return True
			if pNewCapital.getOwner() == iPlayer and (bHuman or pNewCapital.getOwner() != utils.getHumanID()):
				apCityList = PyPlayer(iPlayer).getCityList()
				for pyCity in apCityList:
					city = gc.getMap().plot(pyCity.getX(), pyCity.getY()).getPlotCity()
					if city.getNumRealBuilding(iPalace) > 0 and city.getX() != pNewCapital.getX() and city.getY() != pNewCapital.getY():
						city.setNumRealBuilding(iPalace, 0)
						break
				pNewCapital.setNumRealBuilding(iPalace, 1)
				return True
		return False


	def checkCapitals (self, iGameTurn):
		"""If applicable, moves the non-human player's capital to the historical location for free."""
		
		for iCiv in range(iNumPlayers):
			if tNewCapitals[iCiv][0] > -1:
				counter = self.getCounter(iCiv)
				if counter == 1:
					self.setCounter(iCiv, 0)
					self.moveCapital(tNewCapitals[iCiv], iCiv)
				elif counter > 1:
					self.setCounter(iCiv, counter - 1)


	def checkCapitalsOnCapture (self, pCity, iCiv):
		"""Sets the new capital counter when a new historical capital is captured by a non-human player."""
		
		if iCiv != iHuman and iCiv < iNumPlayers:
			if (pCity.getX(), pCity.getY()) == tNewCapitals[iCiv]:
				self.setCounter(iCiv, utils.getTurns(10+gc.getGame().getSorenRandNum(10, 'New Capital')))


	def getBetrayalThreshold(self):
		if gc.getGame().getHandicapType() == 0:
			return 85
		return 80


	def showBirthMessage(self, iCiv, iHuman):
		
		textKey = ""
		
		if iCiv == iArmenia and iHuman in [iEgypt, iCarthage, iRome, iSeleucids]:
			textKey = "TXT_KEY_CIV_BIRTH_ARMENIA"
		
		elif iCiv == iRome and iHuman in [iEgypt, iCarthage, iSeleucids, iCelts]:
			textKey = "TXT_KEY_CIV_BIRTH_ROME"
		
		elif iCiv == iHan and iHuman in [iVietnam, iTocharians]:
			textKey = "TXT_KEY_CIV_BIRTH_HAN1"
		
		elif iCiv == iHan and iHuman in [iQin]:
			textKey = "TXT_KEY_CIV_BIRTH_HAN2"
		
		elif iCiv == iBactria and iHuman in [iMauryans, iSeleucids, iTocharians, iArmenia]:
			textKey = "TXT_KEY_CIV_BIRTH_BACTRIA"
		
		elif iCiv == iParthia and iHuman in [iEgypt, iCarthage, iMauryans, iArmenia, iRome, iSatavahana, iBactria, iSaba]:
			textKey = "TXT_KEY_CIV_BIRTH_PARTHIA"
		
		elif iCiv == iSatavahana and iHuman in [iPandyans, iMauryans, iBactria, iSeleucids, iSaba]:
			textKey = "TXT_KEY_CIV_BIRTH_SATAVAHANA"
		
		elif iCiv == iDacia and iHuman in [iEgypt, iCarthage, iArmenia, iRome, iParthia]:
			textKey = "TXT_KEY_CIV_BIRTH_DACIA"
		
		elif iCiv == iGoguryeo and iHuman in [iHan, iQin]:
			textKey = "TXT_KEY_CIV_BIRTH_GOGURYEO"
		
		elif iCiv == iKushans and iHuman in [iBactria, iParthia, iArmenia, iMauryans, iSatavahana, iTocharians]:
			textKey = "TXT_KEY_CIV_BIRTH_KUSHANS"
		
		elif iCiv == iMaccabees and iHuman in [iEgypt, iSeleucids, iRome, iSaba, iArmenia, iNubia]:
			textKey = "TXT_KEY_CIV_BIRTH_MACCABEES"
		
		elif iCiv == iAxum and iHuman in [iEgypt, iNubia, iPandyans, iSaba]:
			textKey = "TXT_KEY_CIV_BIRTH_AXUM"
		
		elif iCiv == iFunan and iHuman in [iVietnam, iHan, iPandyans, iSatavahana]:
			textKey = "TXT_KEY_CIV_BIRTH_FUNAN"
		
		elif iCiv == iSassanids and iHuman in [iEgypt, iRome, iParthia, iSatavahana, iKushans, iArmenia]:
			textKey = "TXT_KEY_CIV_BIRTH_SASSANIDS"
		
		elif iCiv == iYamato and iHuman in [iHan, iGoguryeo, iJin]:
			textKey = "TXT_KEY_CIV_BIRTH_YAMATO"
		
		elif iCiv == iByzantines and iHuman in [iRome, iDacia, iArmenia, iEgypt, iNubia, iParthia, iSassanids, iCelts, iCarthage]:
			textKey = "TXT_KEY_CIV_BIRTH_BYZANTINES"
		
		elif iCiv == iGupta and iHuman in [iKushans, iSatavahana, iPandyans, iFunan, iSassanids, iParthia, iBactria]:
			textKey = "TXT_KEY_CIV_BIRTH_GUPTA"
		
		elif iCiv == iFranks and iHuman in [iRome, iCelts, iDacia, iByzantines]:
			textKey = "TXT_KEY_CIV_BIRTH_FRANKS"
		
		elif iCiv == iTang and iHuman in [iHan, iJin, iYamato, iGoguryeo, iVietnam]:
			textKey = "TXT_KEY_CIV_BIRTH_TANG"
		
		elif iCiv == iArabs and iHuman in [iRome, iEgypt, iNubia, iSaba, iSatavahana, iParthia, iSassanids, iArmenia]:
			textKey = "TXT_KEY_CIV_BIRTH_ARABS"
		
		if textKey:
			CyInterface().addMessage(iHuman, True, iDuration, CyTranslator().getText(textKey, ()), "AS2D_CIVIC_ADOPT", InterfaceMessageTypes.MESSAGE_TYPE_MAJOR_EVENT, gc.getCivilizationInfo(iCiv).getButton(), ColorTypes(iGreen), tCapitals[iCiv][0], tCapitals[iCiv][1], True, True)

	# free settlers for non-human civs in case central asia or north china is razed		
	def createPostFlipSettlers(self, iCiv, tPlot):

		if iCiv in [iBactria, iHan, iKushans, iJin, iParthia, iSassanids, iTang] and iCiv != utils.getHumanID():
			numCities = gc.getPlayer(iCiv).getNumCities()
			if numCities <= 1:
				utils.makeUnit(iSettler, iCiv, tPlot, 1)
				
	def threeKingdomsSetup(self):
		sd.setFlipsDelay(iShu, 0)
		sd.setFlipsDelay(iWu, 0)
		CyInterface().addMessage(utils.getHumanID(), True, iDuration, CyTranslator().getText("TXT_KEY_THREE_KINGDOMS_START", ()), "", 0, "", ColorTypes(iRed), -1, -1, True, True)
		utils.killAndFragmentCiv(iHan, False)
		utils.killAndFragmentCiv(iQin, False)
		for x in range(iMapWidth):
			for y in range(iMapHeight):
				gc.getMap().plot(x, y).setCulture(iHan, 0, false)
				gc.getMap().plot(x, y).setCulture(iQin, 0, false)
		gc.getPlayer(iHan).setCivilizationType(iWu)
		sd.setCivilization(iHan, iWu)
		self.setCivDesc(iHan, "Kingdom of Wu", "Wu", "Wu", "Sun Quan")
		gc.getPlayer(iQin).setCivilizationType(iShu)
		sd.setCivilization(iQin, iShu)
		self.setCivDesc(iQin, "Kingdom of Shu", "Shu", "Shu", "Liu Bei")
		WuPlotList = utils.getRegionPlotList([rWu, rChu])
		ShuPlotList = utils.getRegionPlotList([rShu, rBa])
		self.birthInvasion(iHan, tCapitals[iWu], WuPlotList)
		self.birthInvasion(iQin, tCapitals[iShu], ShuPlotList)
		

				
	def checkCoreUnoccupied(self, iCiv):
		for iLoopCiv in range (iNumPlayers):
			if gc.getPlayer(iLoopCiv).getNumCities() >= 1:
				for regionID in (lCoreRegions[iCiv]):
					if utils.checkRegionOwnedCity(iLoopCiv, regionID) and not (gc.getTeam(gc.getPlayer(iLoopCiv).getTeam()).isHasTech(iStabilityCollapsing)): ## srpt stability conversion
						return false
						break
		return true
		
	def checkUnoccupied(self, lRegions, bStable = False, bHuman = False):
		for iLoopCiv in range (iNumPlayers):
			if not bHuman or iLoopCiv == utils.getHumanID():
				if gc.getPlayer(iLoopCiv).getNumCities() >= 1:
					for regionID in (lRegions):
						if utils.checkRegionOwnedCity(iLoopCiv, regionID):
							if gc.getTeam(gc.getPlayer(iLoopCiv).getTeam()).isHasTech(iStabilityStable) or bStable == False:
								return false
		return true
		
	def checkRegionStableOwner(self, regionID):
		for iLoopCiv in range (iNumPlayers):
			if utils.checkRegionControl(iLoopCiv, regionID) and gc.getTeam(gc.getPlayer(iLoopCiv).getTeam()).isHasTech(iStabilityStable): ## srpt stability conversion
				return true
		return false
		
	def checkRegionStableHumanOwner(self, regionID):
		for iLoopCiv in range (iNumPlayers):
			if utils.checkRegionControl(iLoopCiv, regionID) and gc.getTeam(gc.getPlayer(iLoopCiv).getTeam()).isHasTech(iStabilityStable) and iLoopCiv == utils.getHumanID(): ## srpt stability conversion
				return true
		return false
		
	"""def checkHistoricalRespawns(self, iGameTurn):
		
		# srpt historical respawns
		iHuman = utils.getHumanID()
		
		# respawns in the same core
		for iPlayer in [iAntigonids, iMauryans, iKalinka, iPandyans, iSatavahana, iBactria, iVietnam, iTocharians]:
			if not gc.getPlayer(iPlayer).isAlive() and self.checkCoreUnoccupied(iPlayer):
				self.sameCoreRespawn(iPlayer)
				
		
		#Macedon: make text key for this!
		if iGameTurn <= getTurnForYear(-100) and not pAntigonids.isAlive() and sd.getCivilization(iAntigonids) == iAntigonids:
			if self.checkCoreUnoccupied(iAntigonids):
				sd.setCivilization(iAntigonids, iMacedon)
				pAntigonids.setCivilizationType(iMacedon)
				#DynamicCivs.checkName(iAntigonids)
				self.barbarianBirth(iAntigonids, iMacedon)
				CyInterface().addMessage(iHuman, True, iDuration, CyTranslator().getText("TXT_KEY_CIV_BIRTH_MACEDON", ()), "", 0, "", ColorTypes(iRed), -1, -1, True, True)
				#DynamicCivs.checkName(iAntigonids)
				return
		

			
		# 2nd Jewish revolt
		if getTurnForYear(60) <= iGameTurn <= getTurnForYear(80) and not pMaccabees.isAlive():
			if self.checkCoreUnoccupied(iMaccabees):
				self.birthInvasion(iMaccabees, tCapitals[iMaccabees], utils.getCorePlotList(iMaccabees))
				CyInterface().addMessage(iHuman, True, iDuration, CyTranslator().getText("TXT_KEY_CIV_BIRTH_MACCABEES", ()), "", 0, "", ColorTypes(iRed), -1, -1, True, True)
				return"""
				

			

			

				
		
			

			

		
					
						
						
	def barbarianBirth(self, iPlayer, iCiv):
	
		if not gc.getMap().plot(tCapitals[iCiv][0], tCapitals[iCiv][1]).isCity():
			self.createSettlerAndGarrison(iPlayer, (tCapitals[iCiv][0], tCapitals[iCiv][1]), iCiv)
	
		regionList = utils.getCoreRegions(iCiv)
		for pRegionID in regionList:
			cityList = []
			for iLoopPlayer in range(iNumTotalPlayers):
				for pyCity in PyPlayer(iLoopPlayer).getCityList():
					pCurrent = gc.getMap().plot(pyCity.getX(), pyCity.getY())
					if pCurrent.getRegionID() == pRegionID:
						cityList.append(pyCity.GetCy())
			
			if len(cityList):
				for loopCity in cityList:
					if iCiv != iMoors or loopCity.getOwner() != iArabs:
						self.cityAttack(iPlayer, iCiv, loopCity)
				
			else:
				self.createAuxBarbarianBirthUnits(pRegionID, iPlayer, iCiv)
			cityList = []
			
				
		self.assignTechs(iPlayer, iCiv)
			
			
	def minorBarbarianBirth(self, iPlayer, iCiv, iRadius):
	
		if (gc.getMap().plot(tCapitals[iCiv][0], tCapitals[iCiv][1]).isCity()):
			city = gc.getMap().plot(tCapitals[iCiv][0],tCapitals[iCiv][1]).getPlotCity()
			self.cityAttack(iPlayer, iCiv, city)
			return
		else:
			cityList = []
			for i in range (1, iRadius):
				for x in range (tCapitals[iCiv][0] -i, tCapitals[iCiv][0] + i + 1):
					for y in range (tCapitals[iCiv][1] -i, tCapitals[iCiv][1] + i + 1):
						if (gc.getMap().plot(x, y).isCity()):
							cityList.append(gc.getMap().plot(x,y).getPlotCity())
				if len(cityList):
					city = cityList[gc.getSorenRandNum(len(cityList))]
					self.cityAttack(iPlayer, iCiv, city)
					return
				else:
					self.createStartingUnits(iPlayer, (tCapitals[iCiv][0], tCapitals[iCiv][1]), iCiv)
					self.createSettlerAndGarrison(iPlayer, (tCapitals[iCiv][0], tCapitals[iCiv][1]), iCiv)
					
		self.assignTechs(iPlayer, iCiv)
		
	def provinceAttack(self, iPlayer, iCiv, lRegions, bHumanOnly = False):
	
		gc.getPlayer(iPlayer).changeGold(500)
		cityList = []
		if bHumanOnly:
			for pyCity in PyPlayer(utils.getHumanID()).getCityList():
				pCurrent = gc.getMap().plot(pyCity.getX(), pyCity.getY())
				if pCurrent.getRegionID() in lRegions:
					cityList.append(pyCity.GetCy())
		else:
			for iTargetPlayer in range(iNumTotalPlayers + 1):
				for pyCity in PyPlayer(iTargetPlayer).getCityList():
					pCurrent = gc.getMap().plot(pyCity.getX(), pyCity.getY())
					if pCurrent.getRegionID() in lRegions:
						cityList.append(pyCity.GetCy())
		if len(cityList):
			for i in range(len(cityList)):
				self.cityAttack(iPlayer, iCiv, cityList[i])
				
		else:
			for RegionID in lRegions:
				self.createAuxBarbarianBirthUnits(RegionID, iPlayer, iCiv)
			
			
	def cityAttack(self, iPlayer, iCiv, city):
		

		# declare war on the city's owner
		if not gc.getTeam(gc.getPlayer(iPlayer).getTeam()).isAtWar(gc.getPlayer(city.getOwner()).getTeam()):
			gc.getTeam(gc.getPlayer(iPlayer).getTeam()).declareWar(gc.getPlayer(city.getOwner()).getTeam(), True, -1)
				
		# traitors open the gates... (human player not affected)
		if not city.getOwner() == utils.getHumanID():
			city.changeCultureUpdateTimer(3);
			city.changeOccupationTimer(3);
				
		# find a spot for the siege
		eDirectionType = DirectionTypes.DIRECTION_SOUTH
		for tPlot in ((city.getX(), city.getY()+1), (city.getX(), city.getY()-1), (city.getX()+1, city.getY()), (city.getX()-1, city.getY()), (city.getX()+1, city.getY()+1), (city.getX()-1, city.getY()-1), (city.getX()+1, city.getY()-1), (city.getX()-1, city.getY()+1)):
			pPlot = gc.getMap().plot(tPlot[0], tPlot[1])
			if (not pPlot.isWater() and not pPlot.isPeak() and pPlot.getFeatureType() not in [iForest, iMarsh, iJungle, iDenseForest, iIce]):
				if pPlot.getOwner() < 0 or gc.getTeam(gc.getPlayer(iPlayer).getTeam()).isAtWar(gc.getPlayer(pPlot.getOwner()).getTeam()):
					#if not utils.areDividedByRiver(tPlot, [city.getX(), city.getY()]):
						#break
					bCrossing, eDirectionType = utils.areDividedByRiver(tPlot, [city.getX(), city.getY()])
					if not bCrossing:
						break
				
		startingPlot = gc.getMap().plot(tPlot[0], tPlot[1])
				
		# clear the spot
		iNumUnitsInAPlot = startingPlot.getNumUnits()
		if iNumUnitsInAPlot:
			for i in range(iNumUnitsInAPlot):
				unit = startingPlot.getUnit(0)
				if unit.getOwner() != iCiv:
					unit.kill(False, iBarbarian)
					
		# count defenders
		iBonus = 0
		iDefenders = 0
		for i in range(gc.getMap().plot(city.getX(), city.getY()).getNumUnits()):
			if iJavelinman <= (gc.getMap().plot(city.getX(), city.getY()).getUnit(i).getUnitType()) <= iTrebuchet:
				iDefenders += 1
		if city.getOwner() != utils.getHumanID() or gc.getGame().getHandicapType() == 2:
			iBonus += iDefenders / 2
		if city.getOwner == utils.getHumanID() and city.GetCy().isCapital() : 
			iBonus -= (2 - (2 - gc.getGame().getHandicapType())) # spare human capital on normal diffuculties
			
				
		#print ("birthInvasion: starting units in", tPlot[0], tPlot[1])
		#print ("createBarbarianBirthUnits, iPlayer=", iPlayer, "iCiv=", iCiv)
		self.createCityAttackUnits(iPlayer, (tPlot[0], tPlot[1]), city.getOwner(), iCiv, iBonus, eDirectionType)
		utils.setPlagueCountdown(iPlayer, -utils.getTurns(iImmunity))
		utils.clearPlague(iPlayer)
		
	def createAuxBarbarianBirthUnits(self, pRegionID, iPlayer, iCiv):
		kPlotList = utils.getRegionPlotList([pRegionID])
		jPlotList = []
		iValue = 0
		tPlot = (-1, -1)
		for i in range (len(kPlotList)): # first look based on Civ's settler map
			iTempValue = gc.getPlayer(iPlayer).getSettlersMaps(iMapHeight - 1 - kPlotList[i][1], kPlotList[i][0])
			#pCurrent = gc.getMap().plot(kPlotList[i][0], kPlotList[i][1])
			#iTempValue = pCurrent.getFoundValue(gc.getPlayer(iPlayer).getLeader())
			#print ("plot", kPlotList[i][0], kPlotList[i][1], "iTempValue", iTempValue)
			if iTempValue > 50 and iTempValue > iValue:
				iValue = iTempValue
				tPlot = (kPlotList[i][0], kPlotList[i][1])
		if tPlot == (-1, -1): # if not, pick a random plot
			for i in range (len(kPlotList)):
				pCurrent = gc.getMap().plot(kPlotList[i][0], kPlotList[i][1])
				if (not pCurrent.isWater() and not pCurrent.isPeak() and pCurrent.getFeatureType() not in [iForest, iMarsh, iJungle, iDenseForest, iIce]):
					if ( not pCurrent.isUnit() ):
						jPlotList.append(pCurrent)
			if (len(jPlotList)):
				i = gc.getGame().getSorenRandNum(len(jPlotList), 'plot')
				result = jPlotList[i]
				if (result):
					tPlot = ((result.getX(), result.getY()))
					
		if tPlot != (-1, -1):
			if iCiv == iNumidia:
				utils.makeUnit(iHorseman, iPlayer, tPlot, 4)
				utils.makeUnit(iArcher, iPlayer, tPlot, 4)
				utils.makeUnit(iSettler, iPlayer, tPlot, 2)
			if iCiv == iScythians:
				utils.makeUnit(iHorseArcher, iPlayer, tPlot, 4)
				utils.makeUnit(iArcher, iPlayer, tPlot, 4)
				utils.makeUnit(iSettler, iPlayer, tPlot, 2)
			if iCiv in [iHephthalites, iHuns, iRouran, iAvars]:
				utils.makeUnit(iHeavyHorseArcher, iPlayer, tPlot, 4)
				utils.makeUnit(iMarksman, iPlayer, tPlot, 4)
				utils.makeUnit(iSettler, iPlayer, tPlot, 2)
			if iCiv in [iVisigoths, iOstrogoths, iVandals]:
				utils.makeUnit(iSwordsman, iPlayer, tPlot, 4)
				utils.makeUnit(iHeavySpearman, iPlayer, tPlot, 4)
				utils.makeUnit(iSettler, iPlayer, tPlot, 2)
			
		
	def findPlayerReverseLookup(self, iCiv):
		for iLoop in range(iNumPlayers):
			if sd.getCivilization(iLoop) == iCiv:
				return iLoop
		
		

			
			

		
			
	def do3KingdomsShu(self):
	
		gc.getGame().setActivePlayer(iQin, False)
		sd.set3KingdomsMarker(1)
		
		return
		
		
	def do3KingdomsWu(self):
	
		gc.getGame().setActivePlayer(iHan, False)
		sd.set3KingdomsMarker(2)
		
		return
		
	def do3KingdomsChola(self):
	
		utils.killUnitsInArea((105, 17), (105, 17), iPandyans)
		#gc.getPlayer(iPandyans).setFlag("Art/Interface/TeamColor/FlagDECAL_chola.dds")
		self.createTamilStartingUnits((107, 20))
		self.foundCity(iIndependent, "Madurai", 105, 17, [iHinduism, iBuddhism], [iWalls, iMonument])
		self.foundCity(iIndependent2, "Karur", 104, 20, [iHinduism, iJainism], [iWalls, iMonument])
		self.setCivDesc(iPandyans, "Chola Kingdom", "Chola", "Cholan", "Karikala")
		sd.set3KingdomsMarker(3)
		utils.revealPlots(iPandyans, utils.getRegionPlotList(lRevealRegions[iPandyans], True))
		
		return
		
		
	def do3KingdomsPandyan(self):
		
		utils.killUnitsInArea((105, 17), (105, 17), iPandyans)
		self.foundCity(iIndependent, "Kaveripattinam", 107, 20, [iHinduism, iBuddhism], [iWalls, iMonument])
		self.foundCity(iIndependent2, "Karur", 104, 20, [iHinduism, iJainism], [iWalls, iMonument])
		self.setCivDesc(iPandyans, "Pandyan Kingdom", "Pandya", "Pandyan", "Nedunj")
		self.createTamilStartingUnits((105, 17))
		sd.set3KingdomsMarker(4)
		utils.revealPlots(iPandyans, utils.getRegionPlotList(lRevealRegions[iPandyans], True))
		
		return
		
		
	def do3KingdomsChera(self):
	
		#gc.getPlayer(iPandyans).setFlag("Art/Interface/TeamColor/FlagDECAL_chera.dds")
		self.createTamilStartingUnits((104, 20), False)
		utils.killUnitsInArea((105, 17), (105, 17), iPandyans)
		self.foundCity(iIndependent, "Kaveripattinam", 107, 20, [iHinduism, iJainism], [iWalls, iMonument])
		self.foundCity(iIndependent, "Madurai", 105, 17, [iHinduism, iBuddhism], [iWalls, iMonument])
		self.setCivDesc(iPandyans, "Chera Kingdom", "Chera", "Cheran", "Kuttuvan")
		sd.set3KingdomsMarker(5)
		utils.revealPlots(iPandyans, utils.getRegionPlotList(lRevealRegions[iPandyans], True))
		
		return
		
	def createTamilStartingUnits(self, tPlot, bShips = True):
	
		utils.makeUnit(iSettler, iPandyans, tPlot, 1)
		utils.makeUnit(iPandyanVillavar, iPandyans, tPlot, 1)
		utils.makeUnit(iHinduMissionary, iPandyans, tPlot, 1)
		utils.makeUnit(iWorker, iPandyans, tPlot, 2) # not covered by createStartingWorkers due to birth date
		tSeaPlot = utils.findSeaPlots(tPlot, 1, iPandyans)
		if bShips:
			if tSeaPlot:
				utils.makeUnit(iGalley, iPandyans, tSeaPlot, 1)
				utils.makeUnit(iWorkBoat, iPandyans, tSeaPlot, 1)
			if iPandyans != utils.getHumanID():
				utils.makeUnit(iPandyanVillavar, iPandyans, tPlot, 1)
				utils.makeUnit(iSpearman, iPandyans, tPlot, 1)
		
		
	def onCityAcquired(self, argsList):
		'City Acquired and Kept'
		iPreviousOwner, iNewOwner, city, bConquest, bTrade = argsList
		
		if bConquest and iNewOwner != utils.getHumanID() and iNewOwner < iNumPlayers:
			if gc.getMap().plot(city.getX(), city.getY()).getRegionID() not in utils.getCoreRegions(sd.getCivilization(iNewOwner)):
				if gc.getMap().plot(city.getX(), city.getY()).getRegionID() not in utils.getNormalRegions(sd.getCivilization(iNewOwner)):
					if gc.getMap().plot(city.getX(), city.getY()).getRegionID() not in utils.getBroaderRegions(sd.getCivilization(iNewOwner)):
						#print ("overextended. iCiv=", iNewOwner)
						gc.getTeam(gc.getPlayer(iNewOwner).getTeam()).setHasTech(iOverextension, True, iNewOwner, False, False)
						#if gc.getPlayer(utils.getHumanID()).canContact(iNewOwner):
							#CyInterface().addMessage(utils.getHumanID(), False, iDuration, localText.getText("TXT_KEY_OVEREXTENSION1", ()) + " " + gc.getPlayer(iNewOwner).getCivilizationAdjective(0) + " " + localText.getText("TXT_KEY_OVEREXTENSION2", ()), "", 0, "", ColorTypes(iRed), -1, -1, True, True)
					
		
	
		
	def setCivDesc(self, iPlayer, sName, sShort="", sAdj="", sLeader=""):
		
		pPlayer = gc.getPlayer(iPlayer)
		pPlayer.setCivName(localText.getText(sName, ()), localText.getText(sShort, ()), localText.getText(sAdj, ()))
		pPlayer.setName(localText.getText(sLeader, ()))
		
	
		
	def sungaRevolution(self):
	
		pMauryans = gc.getPlayer(iMauryans)
		
		sd.setCivilization(iMauryans, iSungas)
		pMauryans.setCivilizationType(iSungas)
		pMauryans.setLeader(iPusyamitra)
		self.assignTechs(iMauryans, iSungas)
		self.setCivDesc(iMauryans, "Sunga Kingdom", "Sunga", "Sungas", "Pusyamitra")
		CyInterface().addMessage(iHuman, True, iDuration, CyTranslator().getText("TXT_KEY_INDEPENDENCE_TEXT_SUNGAS", ()), "", 0, "", ColorTypes(iRed), -1, -1, True, True)
		self.majorCrisis(iMauryans, iSungas, pMauryans, gc.getTeam(pMauryans.getTeam()), 1)
		
	def foundCity(self, iCiv, sName, iX, iY, lReligions=[], lBuildings=[]):
	
		#if not self.checkRegion(iX, iY):
			#return None
		
		pCiv = gc.getPlayer(iCiv)
		pCiv.initCity(iX, iY)
		city = gc.getMap().plot(iX, iY).getPlotCity()
		
		if not city or city.isNone():
			return None
		
		city.setName(sName, False)
		
		if utils.getYear() < 240:
			pCiv.initUnit(iSpearman, iX, iY, UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
			pCiv.initUnit(iArcher, iX, iY, UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
		else:
			pCiv.initUnit(iHeavySpearman, iX, iY, UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
			pCiv.initUnit(iMarksman, iX, iY, UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
			
		UnitArtStyler.updateUnitArtAtPlot(city.plot())
		
		for iReligion in lReligions:
			city.setHasReligion(iReligion, True, False, False)
			
		for iBuilding in lBuildings:
			city.setNumRealBuilding(iBuilding, 1)
			
		UnitArtStyler.updateUnitArtAtPlot(city.plot())
		
		return city
		
	def isChristianitySplit(self):
	
		bSplit = False
		for iReligion in [iCatholicism, iArianism, iMonophysitism, iNestorianism]:
			if gc.getGame().isReligionFounded(iReligion):
				bSplit = True
				
		return bSplit

			