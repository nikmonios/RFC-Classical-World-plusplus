# Religions

from CvPythonExtensions import *
import CvUtil
import Consts as con
from CvMainInterface import CvMainInterface
from PyHelpers import PyPlayer
from StoredData import sd
from RFCUtils import utils

# globals
gc = CyGlobalContext()
localText = CyTranslator()


class Religions:


#######################################
### Main methods (Event-Triggered) ###
#####################################


	def setup(self):
	
		return
		






	def eventApply7626(self, popupReturn):
		"""Persecution popup event."""
		iUnitX, iUnitY, iUnitID = sd.getPersecutionData()
		religionList = sd.getPersecutionReligions()
		utils.doPersecution(iUnitX, iUnitY, iUnitID, religionList[popupReturn.getButtonClicked()])



				
	def foundReligion(self, tPlot, iReligion):
		if (tPlot != False):
			plot = gc.getMap().plot( tPlot[0], tPlot[1] )                
			if (not plot.getPlotCity().isNone()):
				#if (gc.getPlayer(city.getOwner()).isHuman() == 0):
				#if (not gc.getGame().isReligionFounded(iReligion)):
				gc.getGame().setHolyCity(iReligion, plot.getPlotCity(), True)
				return True
			else:
				return False
				
		return False	


	def checkTurn(self, iGameTurn):
		
		# India
		if (iGameTurn % 20 == 0):
			if utils.getRandomPaganCityByRegion(con.lIndianRegions) != None:
				self.spreadReligion(utils.getRandomPaganCityByRegion(con.lIndianRegions), con.iHinduism)
			else:
				self.spreadReligion(utils.getRandomCityByRegion(con.lIndianRegions), con.iHinduism)
	
		if (iGameTurn % 30 == 1):
			if utils.getRandomPaganCityByRegion(con.lSouthIndianRegions) != None:
				self.spreadReligion(utils.getRandomPaganCityByRegion(con.lSouthIndianRegions), con.iJainism)
			else:
				self.spreadReligion(utils.getRandomCityByRegion(con.lSouthIndianRegions), con.iJainism)
			
		# Persia
		if (iGameTurn % 25 == 2):
			if utils.getRandomPaganCityByRegion(con.lPersianRegions) != None:
				self.spreadReligion(utils.getRandomPaganCityByRegion(con.lPersianRegions), con.iZoroastrianism)
			else:
				self.spreadReligion(utils.getRandomCityByRegion(con.lPersianRegions), con.iZoroastrianism)
			
		# China
		if (iGameTurn % 35 == 3):
			if utils.getRandomPaganCityByRegion(con.lGreaterChineseRegions) != None:
				self.spreadReligion(utils.getRandomPaganCityByRegion(con.lGreaterChineseRegions), con.iConfucianism)
			else:
				self.spreadReligion(utils.getRandomCityByRegion(con.lGreaterChineseRegions), con.iConfucianism)
			
		if (iGameTurn % 35 == 4):
			if utils.getRandomPaganCityByRegion(con.lChineseRegions) != None:
				self.spreadReligion(utils.getRandomPaganCityByRegion(con.lChineseRegions), con.iTaoism)
			else:
				self.spreadReligion(utils.getRandomCityByRegion(con.lChineseRegions), con.iTaoism)
		
		# Christianity
		if (not gc.getGame().isReligionFounded(con.iChristianity)):
			if (iGameTurn % 25 == 5):
				self.spreadReligion(utils.getRandomCityByRegion(con.lEasternMediterraneanRegions), con.iHellenism)
			
			if iGameTurn >= getTurnForYear(25):
				if gc.getGame().getSorenRandNum(100, 'chance') <= utils.getYear():
					self.foundReligion(con.tJerusalem, con.iChristianity)
			
					# 12 Apostles
					iOwner = gc.getMap().plot(con.tJerusalem[0], con.tJerusalem[1]).getOwner()
					utils.makeUnit(con.iApostle, iOwner, (con.tJerusalem[0], con.tJerusalem[1]), 1)
					if (gc.getMap().plot(con.tAlexandria[0], con.tAlexandria[1]).isCity()):
						iOwner = gc.getMap().plot(con.tAlexandria[0], con.tAlexandria[1]).getOwner()
						utils.makeUnit(con.iApostle, iOwner, (con.tAlexandria[0], con.tAlexandria[1]), 2)
					if (gc.getMap().plot(con.tAntioch[0], con.tAntioch[1]).isCity()):
						iOwner = gc.getMap().plot(con.tAntioch[0], con.tAntioch[1]).getOwner()
						utils.makeUnit(con.iApostle, iOwner, (con.tAntioch[0], con.tAntioch[1]), 1)
					if (gc.getMap().plot(con.tConstantinople[0], con.tConstantinople[1]).isCity()):
						iOwner = gc.getMap().plot(con.tConstantinople[0], con.tConstantinople[1]).getOwner()
						utils.makeUnit(con.iApostle, iOwner, (con.tConstantinople[0], con.tConstantinople[1]), 2)
					if (gc.getMap().plot(con.tRome[0], con.tRome[1]).isCity()):
						iOwner = gc.getMap().plot(con.tRome[0], con.tRome[1]).getOwner()
						utils.makeUnit(con.iApostle, iOwner, (con.tRome[0], con.tRome[1]), 3)
					if (gc.getMap().plot(con.tCarthage[0], con.tCarthage[1]).isCity()):
						iOwner = gc.getMap().plot(con.tCarthage[0], con.tCarthage[1]).getOwner()
						utils.makeUnit(con.iApostle, iOwner, (con.tCarthage[0], con.tCarthage[1]), 1)
					city = utils.getRandomCityByRegion([con.rMesopotamia, con.rPersia, con.rSyria])
					iOwner = gc.getMap().plot(city.getX(), city.getY()).getOwner()
					utils.makeUnit(con.iApostle, iOwner, (city.getX(), city.getY()), 1)
					city = utils.getRandomCityByRegion([con.rPersia, con.rArachosia, con.rSindh, con.rSogdiana, con.rTarim])
					iOwner = gc.getMap().plot(city.getX(), city.getY()).getOwner()
					utils.makeUnit(con.iApostle, iOwner, (city.getX(), city.getY()), 1)
		else:
			if (iGameTurn % 10 == 10):
				if utils.getRandomPaganCityByRegion(con.lEasternMediterraneanRegions) != None:
					self.spreadReligion(utils.getRandomPaganCityByRegion(con.lEasternMediterraneanRegions), con.iChristianity)
				else:
					self.spreadReligion(utils.getRandomCityByRegion(con.lEasternMediterraneanRegions), con.iChristianity)
				
			if (iGameTurn % 10 == 15):
				if utils.getRandomPaganCityByRegion(con.lWesternMediterraneanRegions) != None:
					self.spreadReligion(utils.getRandomPaganCityByRegion(con.lWesternMediterraneanRegions), con.iChristianity)
				else:
					self.spreadReligion(utils.getRandomCityByRegion(con.lWesternMediterraneanRegions), con.iChristianity)
				
			if (iGameTurn % 10 == 25):
				if utils.getRandomPaganCityByRegion(con.lEasternChristianRegions) != None:
					self.spreadReligion(utils.getRandomPaganCityByRegion(con.lEasternChristianRegions), con.iChristianity)
				else:
					self.spreadReligion(utils.getRandomCityByRegion(con.lEasternChristianRegions), con.iChristianity)
					
		# Manichaeism
		if (not gc.getGame().isReligionFounded(con.iManichaeism)):
			
			if iGameTurn >= getTurnForYear(276):
				if gc.getGame().getSorenRandNum(100, 'chance') <= utils.getYear() -250:
					self.foundReligion(con.tBabylon, con.iManichaeism)
		else:
			if (iGameTurn % 25 == 18):
				if utils.getRandomPaganCityByRegion(con.lEasternMediterraneanRegions) != None:
					self.spreadReligion(utils.getRandomPaganCityByRegion(con.lEasternMediterraneanRegions), con.iManichaeism)
				else:
					self.spreadReligion(utils.getRandomCityByRegion(con.lEasternMediterraneanRegions), con.iManichaeism)
			if (iGameTurn % 25 == 28):
				if utils.getRandomPaganCityByRegion(con.lPersianRegions) != None:
					self.spreadReligion(utils.getRandomPaganCityByRegion(con.lPersianRegions), con.iManichaeism)
				else:
					self.spreadReligion(utils.getRandomCityByRegion(con.lPersianRegions), con.iManichaeism)
			
		# Judaism
		if (iGameTurn % 20 == 17):
			if utils.getRandomPaganCityByRegion(con.lNearJewishRegions) != None:
				self.spreadReligion(utils.getRandomPaganCityByRegion(con.lNearJewishRegions), con.iJudaism)
			else:
				self.spreadReligion(utils.getRandomCityByRegion(con.lNearJewishRegions), con.iJudaism)
			
		if (iGameTurn % 35 == 27):
			if utils.getRandomPaganCityByRegion(con.lFartherJewishRegions) != None:
				self.spreadReligion(utils.getRandomPaganCityByRegion(con.lFartherJewishRegions), con.iJudaism)
			else:
				self.spreadReligion(utils.getRandomCityByRegion(con.lFartherJewishRegions), con.iJudaism)
		
		# Islam
		if iGameTurn > getTurnForYear(630):
			if (iGameTurn % 25 == 15):
				if utils.getRandomPaganCityByRegion(con.lEasternMediterraneanRegions) != None:
					self.spreadReligion(utils.getRandomPaganCityByRegion(con.lEasternMediterraneanRegions), con.iIslam)
				else:
					self.spreadReligion(utils.getRandomCityByRegion(con.lEasternMediterraneanRegions), con.iIslam)
				
			if (iGameTurn % 20 == 10):
				if utils.getRandomPaganCityByRegion(con.lPersianRegions) != None:
					self.spreadReligion(utils.getRandomPaganCityByRegion(con.lPersianRegions), con.iIslam)
				else:
					self.spreadReligion(utils.getRandomCityByRegion(con.lPersianRegions), con.iIslam)
				
			if (iGameTurn % 30 == 25):
				if utils.getRandomPaganCityByRegion(con.lCentralAsianRegions) != None:
					self.spreadReligion(utils.getRandomPaganCityByRegion(con.lCentralAsianRegions), con.iIslam)
				else:
					self.spreadReligion(utils.getRandomCityByRegion(con.lCentralAsianRegions), con.iIslam)
		
		# Central Asian & Chinese Buddhism
		if utils.getHumanID() != con.iTocharians:
			if (iGameTurn % 30 == 25):
				if utils.getRandomPaganCityByRegion(con.lCentralAsianRegions) != None:
					self.spreadReligion(utils.getRandomPaganCityByRegion(con.lCentralAsianRegions), con.iBuddhism)
				else:
					self.spreadReligion(utils.getRandomCityByRegion(con.lCentralAsianRegions), con.iBuddhism)
					
			if (iGameTurn > getTurnForYear(150)) and (iGameTurn % 30 == 25):
				if utils.getRandomPaganCityByRegion(con.lChineseRegions) != None:
					self.spreadReligion(utils.getRandomPaganCityByRegion(con.lChineseRegions), con.iBuddhism)
				else:
					self.spreadReligion(utils.getRandomCityByRegion(con.lChineseRegions), con.iBuddhism)
		
		
		# Southeast Asian Hinduism & Buddhism
		if utils.getHumanID() != con.iSatavahana:
			if (iGameTurn > getTurnForYear(-100)):
				if (iGameTurn % 30 == 25):
					if utils.getRandomPaganCityByRegion(con.lSouthEastAsianRegions) != None:
						self.spreadReligion(utils.getRandomPaganCityByRegion(con.lSouthEastAsianRegions), con.iBuddhism)
					else:
						self.spreadReligion(utils.getRandomCityByRegion(con.lSouthEastAsianRegions), con.iBuddhism)
				if (iGameTurn % 30 == 5):
					if utils.getRandomPaganCityByRegion(con.lSouthEastAsianRegions) != None:
						self.spreadReligion(utils.getRandomPaganCityByRegion(con.lSouthEastAsianRegions), con.iHinduism)
					else:
						self.spreadReligion(utils.getRandomCityByRegion(con.lSouthEastAsianRegions), con.iHinduism)
			
				
			
		
		iHuman = utils.getHumanID()
		# Tocharian Buddhism for AI
		if iHuman != con.iTocharians:
			if iGameTurn == getTurnForYear(100):
				self.spreadReligion(utils.getRandomCityByRegion([con.rTarim]), con.iBuddhism)
			if iGameTurn == getTurnForYear(150):
				self.spreadReligion(utils.getRandomCityByRegion([con.rTarim]), con.iBuddhism)
			if iGameTurn == getTurnForYear(200):
				self.spreadReligion(utils.getRandomCityByRegion([con.rTarim]), con.iBuddhism)
		
		
		

					
		# religious conversion of city populations
		if (iGameTurn % 15 == 0): #every 15 turns
			for iPlayer in range(con.iNumTotalPlayers): # indy & barb included
				if gc.getPlayer(iPlayer).isAlive():
					apCityList = PyPlayer(iPlayer).getCityList()
					for pyCity in apCityList:
						pCity = pyCity.GetCy()
						# Buddhists convert to Hinduism in India after 100BC
						if pCity.isHasReligion(con.iHinduism) and pCity.isHasReligion(con.iBuddhism) and iGameTurn > getTurnForYear(-100) and gc.getMap().plot(pCity.getX(), pCity.getY()).getRegionID() in [con.rSindh, con.rSaurashtra, con.rPunjab, con.rAvanti, con.rMagadha, con.rBangala, con.rDeccan, con.rKerala, con.rTamilNadu] and gc.getGame().getSorenRandNum(100, 'remove Buddhism') > 90:
							if not pCity.isHolyCityByType(con.iBuddhism):
								pCity.setHasReligion(con.iBuddhism, False, False, False)
						# Hellenic convert to Christianity
						if pCity.isHasReligion(con.iHellenism) and pCity.isHasReligion(con.iChristianity) and gc.getGame().getSorenRandNum(100, 'remove Hellenism') > 90:
							if not pCity.isHolyCityByType(con.iHellenism):
								pCity.setHasReligion(con.iHellenism, False, False, False)
						# Zoroastrians and Manicheans convert to Christianity or Islam
						if pCity.isHasReligion(con.iZoroastrianism) and pCity.isHasReligion(con.iChristianity) and gc.getGame().getSorenRandNum(100, 'remove Zoroastrianism') > 90:
							if not pCity.isHolyCityByType(con.iZoroastrianism):
								pCity.setHasReligion(con.iZoroastrianism, False, False, False)
						if pCity.isHasReligion(con.iZoroastrianism) and pCity.isHasReligion(con.iIslam) and gc.getGame().getSorenRandNum(100, 'remove Zoroastrianism') > 90:
							if not pCity.isHolyCityByType(con.iZoroastrianism):
								pCity.setHasReligion(con.iZoroastrianism, False, False, False)
		


	def spreadReligion(self, city, iReligion, textKey=False):
		
		if city is None or city.isNone():
			return -1
		
		# do not spread the religion if the city already has it, or the owner is using Persecution civic
		if city.isHasReligion(iReligion) or gc.getPlayer(city.getOwner()).getCivics(4) == con.iMilitancyCivic:
			return -1
			
		if iReligion == con.iChristianity:
			
			if city.isHasReligion(con.iHellenism) and not city.isHolyCityByType(con.iHellenism):
				rndNum = gc.getGame().getSorenRandNum(100, 'remove Hellenism')
				if rndNum <= 66:
					city.setHasReligion(con.iHellenism, False, False, False)
			
			if city.isHasReligion(con.iManichaeism) and not city.isHolyCityByType(con.iManichaeism):
				rndNum = gc.getGame().getSorenRandNum(100, 'remove Manichaeism')
				if rndNum <= 66:
					city.setHasReligion(con.iManichaeism, False, False, False)
			
		if iReligion == con.iIslam:
			
			if city.isHasReligion(con.iZoroastrianism) and not city.isHolyCityByType(con.iZoroastrianism):
				rndNum = gc.getGame().getSorenRandNum(100, 'remove Zoroastrianism')
				if rndNum <= 66:
					city.setHasReligion(con.iZoroastrianism, False, False, False)
			
			if city.isHasReligion(con.iManichaeism) and not city.isHolyCityByType(con.iManichaeism):
				rndNum = gc.getGame().getSorenRandNum(100, 'remove Manichaeism')
				if rndNum <= 66:
					city.setHasReligion(con.iManichaeism, False, False, False)
				
		
		# show the message about Jewish refugess if the religion is Judaism
		if iReligion == con.iJudaism:
			city.setHasReligion(iReligion, True, False, False)
			if not textKey:
				textKey = "TXT_KEY_MINOR_EVENT_JEWS"
			szText = localText.getText(textKey, (city.getName(), ))
			CyInterface().addMessage(city.getOwner(), False, con.iDuration, szText, "AS2D_BUILD_JEWISH", InterfaceMessageTypes.MESSAGE_TYPE_MAJOR_EVENT, gc.getReligionInfo(iReligion).getButton(), ColorTypes(con.iWhite), city.getX(), city.getY(), True, True)
		else:
			city.setHasReligion(iReligion, True, True, True)
		return True


	def removeReligion(self, city, iReligion):
		
		if city is None: return -1
		elif city.isNone(): return -1
		elif not city.isHasReligion(iReligion): return -1
		
		city.setHasReligion(iReligion, False, True, True)
		return True
		
		
	def onReligionSpread(self, iReligion, iOwner, city):
	
		if iReligion == con.iChristianity:
			
			if city.isHasReligion(con.iHellenism):
				rndNum = gc.getGame().getSorenRandNum(100, 'remove Hellenism')
				if rndNum <= 66:
					city.setHasReligion(con.iHellenism, False, False, False)
			
			if city.isHasReligion(con.iManichaeism):
				rndNum = gc.getGame().getSorenRandNum(100, 'remove Manichaeism')
				if rndNum <= 66:
					city.setHasReligion(con.iManichaeism, False, False, False)
			
		if iReligion == con.iIslam:
			
			if city.isHasReligion(con.iZoroastrianism):
				rndNum = gc.getGame().getSorenRandNum(100, 'remove Zoroastrianism')
				if rndNum <= 66:
					city.setHasReligion(con.iZoroastrianism, False, False, False)
			
			if city.isHasReligion(con.iManichaeism):
				rndNum = gc.getGame().getSorenRandNum(100, 'remove Manichaeism')
				if rndNum <= 66:
					city.setHasReligion(con.iManichaeism, False, False, False)
			
			if city.isHasReligion(con.iBuddhism):
				rndNum = gc.getGame().getSorenRandNum(100, 'remove Manichaeism')
				if rndNum <= 66:
					city.setHasReligion(con.iBuddhism, False, False, False)
			
			if city.isHasReligion(con.iHellenism):
				rndNum = gc.getGame().getSorenRandNum(100, 'remove Manichaeism')
				if rndNum <= 66:
					city.setHasReligion(con.iHellenism, False, False, False)


	def onPlayerChangeStateReligion(self, argsList):
		'Player changes his state religion'
		iPlayer, iNewReligion, iOldReligion = argsList
		
		# reset diplomatic penalty from persecution
		pPlayer = gc.getPlayer(iPlayer)
		for iLoopPlayer in range(con.iNumPlayers):
			if gc.getPlayer(iLoopPlayer).isAlive() and iLoopPlayer != iPlayer:
				pPlayer.AI_setAttitudeExtra(iLoopPlayer, 0)
		
		





	def onBuildingBuilt(self, iPlayer, iBuilding, city):
		
		return


	def onTechAcquired(self, iTech, iPlayer):
	
		return

	def onGreatPersonBorn(self, iPlayer):
		
		return


	def onChangeWar(self, argsList):
		bIsWar, iTeam, iRivalTeam = argsList
		
		if iTeam >= con.iNumPlayers or iRivalTeam >= con.iNumPlayers: return
		
		bSameReligion = False
		if gc.getPlayer(iTeam).getStateReligion() == gc.getPlayer(iRivalTeam).getStateReligion():
			bSameReligion = True
		

				
		## button refresh for spies conducting scret diplomacy ( this is only here because this module imports CvMainInterface)
		CvMainInterface().updateSelectionButtons()
				
				
	def onCityBuilt(self, city):
		
		
		# human Arabs holy city fix
		if city.getOwner() == con.iArabs == utils.getHumanID() and (gc.getPlayer(con.iArabs).getNumCities()) <= 1:
			
			gc.getGame().setHolyCity(con.iIslam, city, True)
		
		# Parsa Holy City fix
		#if city.getOwner() == con.iSassanids and (gc.getPlayer(con.iSassanids).getNumCities()) <= 1:
			#gc.getGame().setHolyCity(con.iZoroastrianism, city, True)
				
		# Pataliputra Holy City fix
		#if city.getOwner() == con.iGupta and (gc.getPlayer(con.iGupta).getNumCities()) <= 1:
			#gc.getGame().setHolyCity(con.iBuddhism, city, True)


	def onCityRazed(self, argsList):
		city, iPlayer = argsList
		
		if iPlayer >= con.iNumPlayers: return
		
		iStateReligion = gc.getPlayer(iPlayer).getStateReligion()
			
		
		# apply diplomatic penalty
		for iReligion in range(con.iNumReligions):
			if city.isHasReligion(iReligion):
				for iLoopPlayer in range(con.iNumPlayers):
					pLoopPlayer = gc.getPlayer(iLoopPlayer)
					if iLoopPlayer != iPlayer and pLoopPlayer.isAlive() and pLoopPlayer.getStateReligion() == iReligion:
						pLoopPlayer.AI_changeAttitudeExtra(iPlayer, -1)


	def onCityAcquired(self, argsList):
		iPreviousOwner, iNewOwner, city, bConquest, bTrade = argsList
		pNewOwner = gc.getPlayer(iNewOwner)
		iStateReligion = pNewOwner.getStateReligion()
		
		
		
		# Make sure stupid AI civs don't switch religions if they capture their first city
		if bConquest and pNewOwner.getNumCities() <= 1 and not pNewOwner.isHuman() and iStateReligion > 0:
			if not city.isHasReligion(iStateReligion):
				city.setHasReligion(iStateReligion, True, True, True)
		
		# UP: Arabs
		if iNewOwner == con.iArabs:
			if not city.isHasReligion(con.iIslam):
				city.setHasReligion(con.iIslam, True, True, True)
			if city.isHasReligion(con.iZoroastrianism):
				city.setHasReligion(con.iZoroastrianism, False, False, False)
			if city.isHasReligion(con.iHellenism):
				city.setHasReligion(con.iHellenism, False, False, False)
			if city.isHasReligion(con.iBuddhism):
				city.setHasReligion(con.iBuddhism, False, False, False)
			if city.isHasReligion(con.iManichaeism):
				city.setHasReligion(con.iManichaeism, False, False, False)


	def onCityAcquiredAndKept(self, argsList):
		'City Acquired and Kept'
		iOwner, city, bMassacre = argsList
		
		pOwner = gc.getPlayer(iOwner)
		iStateReligion = pOwner.getStateReligion()
		

		
		# UP: Arabs
		if iOwner == con.iArabs:
			if not city.isHasReligion(con.iIslam):
				city.setHasReligion(con.iIslam, True, True, True)
			if city.isHasReligion(con.iZoroastrianism):
				city.setHasReligion(con.iZoroastrianism, False, False, False)
			if city.isHasReligion(con.iHellenism):
				city.setHasReligion(con.iHellenism, False, False, False)
			if city.isHasReligion(con.iBuddhism):
				city.setHasReligion(con.iBuddhism, False, False, False)
			if city.isHasReligion(con.iManichaeism):
				city.setHasReligion(con.iManichaeism, False, False, False)
		
		
		
		# massacre the disbelievers
		if bMassacre and city.getReligionCount() > 0:
			
			# remove religions and count the loot
			iNumOldReligions = city.getReligionCount()
			iLootModifier = 2 * city.getPopulation() / city.getReligionCount() + 1
			iLoot = 0
			
			if iOwner == con.iBarbarian or pOwner.getStateReligion() == -1:
				return
			else:
				lReligions = con.tPersecutionOrder[pOwner.getStateReligion()]
				
			for iReligion in lReligions:
				if city.isHasReligion(iReligion) and iReligion != pOwner.getStateReligion() and not city.isHolyCityByType(iReligion):
					iTempLoot = 2
					iTempLoot += iLootModifier
					for iBuildingLoop in range(gc.getNumBuildingInfos()):
						if iBuildingLoop < con.iPlague:
							if city.getNumRealBuilding(iBuildingLoop):
								if gc.getBuildingInfo(iBuildingLoop).getPrereqReligion() == iReligion:
									city.setNumRealBuilding(iBuildingLoop, 0)
									iTempLoot += iLootModifier
					if iReligion == con.iJudaism:
						iTempLoot = iTempLoot*3/2
					iLoot += iTempLoot
					
					city.setHasReligion(iReligion, False, False, False)
					city.changeHurryAngerTimer(city.flatHurryAngerLength()/2)
					
					# apply diplomatic penalty
					for iLoopPlayer in range(con.iNumPlayers):
						pLoopPlayer = gc.getPlayer(iLoopPlayer)
						if pLoopPlayer.isAlive() and iLoopPlayer != iOwner:
							if pLoopPlayer.getStateReligion() == iReligion:
								pLoopPlayer.AI_changeAttitudeExtra(iOwner, -1)
					
					# Barbarians remove just 1 religion
					if iOwner == con.iBarbarian:
						break
			
			# proceed only if at least one religion was removed
			if city.getReligionCount() < iNumOldReligions:
				iPopulationMassacred = 0
				if city.getPopulation() > 1:
					iPopulationMassacred = city.getPopulation() * (iNumOldReligions - city.getReligionCount()) / iNumOldReligions
					iPopulationMassacred = min(iPopulationMassacred, city.getPopulation()/2)
					city.changePopulation(-iPopulationMassacred)
				
				iLoot = iLoot/2 + gc.getGame().getSorenRandNum(iLoot/2, 'random loot')
				pOwner.changeGold(iLoot)
				
				iHuman = utils.getHumanID()
				if iOwner == iHuman:
					CyInterface().addMessage(iHuman, False, con.iDuration, localText.getText("TXT_KEY_MESSAGE_MASSACRE", (city.getName(), iLoot)), "AS2D_COMBAT", InterfaceMessageTypes.MESSAGE_TYPE_INFO, None, ColorTypes(con.iGreen), -1, -1, False, False)
				elif city.isRevealed(iHuman, False):
					CyInterface().addMessage(iHuman, False, con.iDuration, localText.getText("TXT_KEY_MESSAGE_MASSACRE_OTHER", (pOwner.getCivilizationAdjectiveKey(), city.getName())), "AS2D_COMBAT", InterfaceMessageTypes.MESSAGE_TYPE_INFO, None, ColorTypes(con.iRed), -1, -1, False, False)
				
				return max(0, iPopulationMassacred)

	def onUnitSpreadReligionAttempt(self, argsList):
		'Unit tries to spread religion to a city'
		pUnit, iReligion, bSuccess = argsList
		

		if bSuccess:
			city = gc.getMap().plot(pUnit.getX(), pUnit.getY()).getPlotCity()
			iPlayer = pUnit.getOwner()
			if iPlayer >= con.iNumPlayers: return
			iStateReligion = -1
			if gc.getPlayer(iPlayer).getStateReligion() >= 0:
				iStateReligion = gc.getPlayer(iPlayer).getStateReligion()
				
			# Satavahana UP
			if iPlayer == con.iSatavahana and iReligion in [con.iHinduism, con.iBuddhism] and city.getOwner() != con.iSatavahana:
				apCityList = PyPlayer(iPlayer).getCityList()
				for pyCity in apCityList:
					pyCity.GetCy().changeCulture(con.iSatavahana, 20, True)
				
			if iReligion == con.iChristianity:
			
				
				if city.isHasReligion(con.iHellenism):
					rndNum = gc.getGame().getSorenRandNum(100, 'remove Hellenism')
					if rndNum <= 66:
						city.setHasReligion(con.iHellenism, False, False, False)
						for iBuildingLoop in range(gc.getNumBuildingInfos()):
							if iBuildingLoop < con.iPlague:
								if city.getNumRealBuilding(iBuildingLoop):
									if gc.getBuildingInfo(iBuildingLoop).getPrereqReligion() == con.iHellenism:
										city.setNumRealBuilding(iBuildingLoop, 0)
			
				if city.isHasReligion(con.iManichaeism):
					rndNum = gc.getGame().getSorenRandNum(100, 'remove Manichaeism')
					if rndNum <= 66:
						city.setHasReligion(con.iManichaeism, False, False, False)
						for iBuildingLoop in range(gc.getNumBuildingInfos()):
							if iBuildingLoop < con.iPlague:
								if city.getNumRealBuilding(iBuildingLoop):
									if gc.getBuildingInfo(iBuildingLoop).getPrereqReligion() == con.iManichaeism:
										city.setNumRealBuilding(iBuildingLoop, 0)
			
			if iReligion == con.iIslam:
			
				if city.isHasReligion(con.iZoroastrianism):
					rndNum = gc.getGame().getSorenRandNum(100, 'remove Zoroastrianism')
					if rndNum <= 66:
						city.setHasReligion(con.iZoroastrianism, False, False, False)
						for iBuildingLoop in range(gc.getNumBuildingInfos()):
							if iBuildingLoop < con.iPlague:
								if city.getNumRealBuilding(iBuildingLoop):
									if gc.getBuildingInfo(iBuildingLoop).getPrereqReligion() == con.iZoroastrianism:
										city.setNumRealBuilding(iBuildingLoop, 0)
			
				if city.isHasReligion(con.iManichaeism):
					rndNum = gc.getGame().getSorenRandNum(100, 'remove Manichaeism')
					if rndNum <= 66:
						city.setHasReligion(con.iManichaeism, False, False, False)
						for iBuildingLoop in range(gc.getNumBuildingInfos()):
							if iBuildingLoop < con.iPlague:
								if city.getNumRealBuilding(iBuildingLoop):
									if gc.getBuildingInfo(iBuildingLoop).getPrereqReligion() == con.iManichaeism:
										city.setNumRealBuilding(iBuildingLoop, 0)





	def onUnitBuilt(self, argsList):
		'Unit Completed'
		pCity, pUnit = argsList
		
		iPlayer = pCity.getOwner()
		if iPlayer >= con.iNumPlayers: return
		
		# blessed promotion for pious players
		iFavor = utils.getFavorLevel(iPlayer)
		if iFavor > 0:
			if con.tFavorLevelsBlessing[iFavor] > 0:
				if pUnit.getDomainType() == DomainTypes.DOMAIN_LAND:
					if pUnit.baseCombatStr() > 0:
						pUnit.setHasPromotion(con.iBlessed, True)


	def checkAIHolyWar(self, iPlayer):
		"""Determine whether it is a good idea to call for a holy war, and against whom.
		If a good target is found, call the war."""
		
		pPlayer = gc.getPlayer(iPlayer)
		targetList = utils.getHolyWarTargets(iPlayer)
		iBestWeight = -1
		iBestTarget = -1
		for tTarget in targetList:
			pTarget = gc.getPlayer(tTarget[0])
			iWeight = tTarget[2]
			iWeight = iWeight * pTarget.getPower() / pPlayer.getPower()
			civList = utils.getHolyWarParticipants(iPlayer, tTarget[0])
			iWeight *= len(civList)
			if iWeight > iBestWeight:
				iBestWeight = iWeight
				iBestTarget = tTarget[0]
		
		if gc.getGame().getSorenRandNum(100, 'Jihad!') < iBestWeight:
			sd.setVal('iLastHolyWarTurn', gc.getGame().getGameTurn())
			sd.setVal('iHolyWarTarget', iBestTarget)
			if utils.isActive(utils.getHumanID()):
				CyInterface().addMessage(utils.getHumanID(), False, con.iDuration, localText.getText("TXT_KEY_HOLY_WAR_CALLED", (pPlayer.getName(), gc.getPlayer(iBestTarget).getCivilizationDescription(0))), "AS2D_DECLAREWAR", InterfaceMessageTypes.MESSAGE_TYPE_MAJOR_EVENT, "", ColorTypes(con.iRed), -1, -1, False, False)
				
				
	def onReligionFounded(self, iReligion, iFounder):
		return
		

