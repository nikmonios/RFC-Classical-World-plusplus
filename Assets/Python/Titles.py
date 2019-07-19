# The Sword of Islam - Honorific Titles

from CvPythonExtensions import *
import CvUtil
import PyHelpers
import Consts as con
from StoredData import sd
from RFCUtils import utils

# globals
gc = CyGlobalContext()
PyPlayer = PyHelpers.PyPlayer

class Titles:


	def setup(self):
		return
		#self.checkPlayerTitle(con.iRomanEmperor, con.iEgypt)
		#self.checkPlayerTitle(con.iCaliph, con.iCarthage)


	def checkPlayerTitle(self, iTitle, iPlayer):
		"""Checks if the player is eligible for the given title."""
		
		if iPlayer >= con.iNumPlayers:
			return
		
		# Skip if title is already taken, unless previous owner is a vassal of iPlayer
		for iLoopPlayer in range(con.iNumPlayers):
			if gc.getTeam(gc.getPlayer(iLoopPlayer).getTeam()).getProjectCount(iTitle):
				if not gc.getTeam(gc.getPlayer(iLoopPlayer).getTeam()).isVassal(iPlayer):
					return
		
		iStateReligion = gc.getPlayer(iPlayer).getStateReligion()
		
		if iTitle == con.iRomanEmperor:
			if gc.getMap().plot(con.tRome[0],con.tRome[1]).getOwner() == iPlayer or gc.getMap().plot(con.tConstantinople[0],con.tConstantinople[1]).getOwner() == iPlayer:
				iNumCities = 0
				regionList = [con.rGreece, con.rAsia, con.rThrace, con.rSyria, con.rJudea, con.rEgypt, con.rLibya, con.rAfrica, con.rIberia, con.rSeptimania, con.rGaul]
				apCityList = PyPlayer(iPlayer).getCityList()
				for pCity in apCityList:
					if pCity.GetCy().plot().getRegionID() in regionList:
						iNumCities += 1
				if iNumCities >= 20:
					gc.getTeam(gc.getPlayer(iPlayer).getTeam()).changeProjectCount(iTitle, 1)

		elif iTitle == con.iCaliph:
			pBabylon = gc.getMap().plot(con.tBabylon[0], con.tBabylon[1]).getPlotCity()
			if not pBabylon is None and not pBabylon.isNone():
				if pBabylon.getOwner() == iPlayer and (iStateReligion == con.iIslam):
					gc.getTeam(gc.getPlayer(iPlayer).getTeam()).changeProjectCount(iTitle, 1)
					# Fatimid UHV3
					#if iPlayer == con.iHan:
						#if sd.getGoal(con.iHan, 2) == -1:
							#sd.setGoal(con.iHan, 2, 1)
							
		elif iTitle == con.iShahanshah:
			if iStateReligion != con.iZoroastrianism:
				return
			bControl = True
			for iRegion in con.lTitleRegions[con.iShahanshah]:
				if not utils.checkRegionControl(iPlayer, iRegion):
					bControl = False
					break
			if bControl:
				gc.getTeam(gc.getPlayer(iPlayer).getTeam()).changeProjectCount(iTitle, 1)
				gc.getPlayer(iPlayer).changeFreeCityCommerce(CommerceTypes.COMMERCE_CULTURE, 1)
				# Sassanid UHV
				if iPlayer == con.iSassanids:
					if sd.getGoal(con.iSassanids, 0) == -1:
						sd.setGoal(con.iSassanids, 0, 1)
				#elif iPlayer == con.iTang:
					#if sd.getGoal(con.iTang, 2) == -1:
						#sd.setGoal(con.iTang, 2, 1)
				#elif iPlayer == con.iArabs:
					#if sd.getGoal(con.iArabs, 0) == -1:
						#sd.setGoal(con.iArabs, 0, 1)

		elif iTitle == con.iRaja:
			if iStateReligion != con.iHinduism:
				return
			iNumRegions = 0
			for iRegion in con.lTitleRegions[con.iRaja]:
				if utils.checkRegionControl(iPlayer, iRegion):
					iNumRegions += 1
					if iNumRegions == 6:
						gc.getTeam(gc.getPlayer(iPlayer).getTeam()).changeProjectCount(iTitle, 1)
						break
					
		elif iTitle == con.iSharif:
			return
			

		elif iTitle == con.iProtector:
			return
			


	def onCityAcquired(self, argsList):
		iPreviousOwner, iNewOwner, city, bConquest, bTrade = argsList
		
		# Sharif of Mecca - lost immediately if Mecca is lost
		if (city.getX(), city.getY()) == con.tMecca:
			pTeam = gc.getTeam(gc.getPlayer(iPreviousOwner).getTeam())
			if pTeam.getProjectCount(con.iSharif):
				pTeam.changeProjectCount(con.iSharif, -1)
				self.checkPlayerTitle(con.iSharif, iNewOwner)
				return

		# Protector of Jerusalem - lost immediately if Jerusalem is lost
		if (city.getX(), city.getY()) == con.tJerusalem:
			pTeam = gc.getTeam(gc.getPlayer(iPreviousOwner).getTeam())
			if pTeam.getProjectCount(con.iProtector):
				pTeam.changeProjectCount(con.iProtector, -1)
				self.checkPlayerTitle(con.iProtector, iNewOwner)
				return
				
		for iTitle in range(con.iNumTitles):
			if city.plot().getRegionID() in con.lTitleRegions[iTitle]:
				self.checkPlayerTitle(iTitle, iNewOwner)


	def onCityBuilt(self, city):
		
		if (city.getX(), city.getY()) == con.tBabylon:
			self.checkPlayerTitle(con.iCaliph, city.getOwner())
		elif city.plot().getRegionID() in con.lTitleRegions[con.iShahanshah]:
			self.checkPlayerTitle(con.iShahanshah, city.getOwner())
		elif city.plot().getRegionID() in con.lTitleRegions[con.iRaja]:
			self.checkPlayerTitle(con.iRaja, city.getOwner())


	def onPlayerChangeStateReligion(self, argsList):
		iPlayer, iNewReligion, iOldReligion = argsList
		
		pPlayer = gc.getPlayer(iPlayer)
		pTeam = gc.getTeam(pPlayer.getTeam())
		iStateReligion = pPlayer.getStateReligion()
		
		for iTitle in range(con.iNumTitles):
			if pTeam.getProjectCount(iTitle):
				if (iTitle in [con.iCaliph, con.iSharif] and iStateReligion != con.iIslam and iStateReligion != con.iZoroastrianism) \
				or (iTitle == con.iProtector and iStateReligion != con.iChristianity and iStateReligion != iHellenism) \
				or (iTitle == con.iRaja and iStateReligion != con.iHinduism):
					pTeam.changeProjectCount(iTitle, -1)
					for iPlayer in range(con.iNumPlayers):
						self.checkPlayerTitle(iTitle, iPlayer)
			else:
				if (iTitle in [con.iCaliph] and iStateReligion in [con.iIslam]) \
				or (iTitle == con.iRaja and iStateReligion == con.iHinduism):
					self.checkPlayerTitle(iTitle, iPlayer)


	def onSetPlayerAlive(self, argsList):
		iPlayer, bNewValue = argsList
		
		# remove titles
		if bNewValue == False:
			for iTitle in range(con.iNumTitles):
				pTeam = gc.getTeam(gc.getPlayer(iPlayer).getTeam())
				if pTeam.getProjectCount(iTitle):
					pTeam.changeProjectCount(iTitle, -1)
					if iTitle == con.iShahanshah:
						gc.getPlayer(iPlayer).changeFreeCityCommerce(CommerceTypes.COMMERCE_CULTURE, -1)
					if iTitle == con.iCaliph:
						sd.setVal('iLastHolyWarTurn', sd.getVal('iLastHolyWarTurn') - 1) # cancels holy war call
					for iLoopPlayer in range(con.iNumPlayers):
						if iLoopPlayer != iPlayer:
							self.checkPlayerTitle(iTitle, iLoopPlayer)