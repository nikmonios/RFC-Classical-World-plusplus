# Dynamic resources - based on Rhye's and Fall of Civilizations
# rewritten by edead

from CvPythonExtensions import *
import CvUtil
import Consts as con
from StoredData import sd
from RFCUtils import utils

# globals
gc = CyGlobalContext()
localText = CyTranslator()


class Resources:


	def createResource(self, iX, iY, iBonus, textKey="TXT_KEY_MISC_DISCOVERED_NEW_RESOURCE"):
		"""Creates a bonus resource and alerts the plot owner"""
		
		if gc.getMap().plot(iX,iY).getBonusType(-1) == -1 or iBonus == -1: # only proceed if the bonus isn't already there or if we're removing the bonus
			if iBonus == -1:
				iBonus = gc.getMap().plot(iX,iY).getBonusType(-1) # for alert
				gc.getMap().plot(iX,iY).setBonusType(-1)
			else:
				gc.getMap().plot(iX,iY).setBonusType(iBonus)
				
			iOwner = gc.getMap().plot(iX,iY).getOwner()
			if iOwner >= 0 and textKey != -1: # only show alert to the tile owner
				city = gc.getMap().findCity(iX, iY, iOwner, TeamTypes.NO_TEAM, True, False, TeamTypes.NO_TEAM, DirectionTypes.NO_DIRECTION, CyCity())
				if not city.isNone() and iOwner >= 0:
					szText = localText.getText(textKey, (gc.getBonusInfo(iBonus).getTextKey(), city.getName(), gc.getPlayer(iOwner).getCivilizationAdjective(0)))
					CyInterface().addMessage(iOwner, False, con.iDuration, szText, "AS2D_DISCOVERBONUS", InterfaceMessageTypes.MESSAGE_TYPE_MINOR_EVENT, gc.getBonusInfo(iBonus).getButton(), ColorTypes(con.iWhite), iX, iY, True, True)


	def removeResource(self, iX, iY, textKey="TXT_KEY_MISC_EVENT_RESOURCE_EXHAUSTED"):
		"""Removes a bonus resource and alerts the plot owner"""
		
		self.createResource(iX, iY, -1, textKey)


	def checkTurn(self, iGameTurn):
	
		if iGameTurn == getTurnForYear(-320):
			if utils.getHumanID() != con.iRome:
				gc.getMap().plot(38, 59).setFeatureType(con.iForest, 0) # to make NE entrance to Italy easier to defend against barbs
				gc.getMap().plot(38, 59).setFeatureType(con.iDenseForest, 0) # to block out the Celts
		if iGameTurn == getTurnForYear(250):
			gc.getMap().plot(38, 59).setFeatureType(con.iForest, 0)
	
		if iGameTurn == getTurnForYear(-75 + (sd.getSeed() % 10)):
			self.removeResource(16, 37) # north african elephants
			
		if iGameTurn == getTurnForYear(100 + (sd.getSeed() % 10)):
			self.removeResource(82, 36) # persian elephants
			
		#if iGameTurn == getTurnForYear(-180 + (sd.getSeed() % 10)) and utils.getHumanID() == con.iHan:
			#gc.getMap().plot(148, 41).setImprovementType(14) # pasture near Min Yue
			#gc.getMap().plot(146, 39).setImprovementType(7) # mine near Min Yue
			#gc.getMap().plot(143, 37).setImprovementType(12) # orchard near Panyu - all to strengthen Nan Yue vs Han
		
		if iGameTurn >= getTurnForYear(-200) and iGameTurn <= getTurnForYear(-50) and utils.getHumanID() == con.iEgypt:
			gc.getMap().plot(113, 37).setImprovementType(4) # farm near Pataliputra
			gc.getMap().plot(116, 38).setImprovementType(14) # pasture near Pataliputra
			gc.getMap().plot(141, 51).setImprovementType(4) # farm near Luoyang
			gc.getMap().plot(141, 52).setImprovementType(4) # farm near Luoyang - all to make Egyptian UHV harder
		
		if iGameTurn >= getTurnForYear(-100) and iGameTurn <= getTurnForYear(50) and utils.getHumanID() == con.iRome and gc.getTeam(gc.getPlayer(con.iRome).getTeam()).isHasTech(con.iRomanEmpire):
			gc.getMap().plot(113, 37).setImprovementType(4) # farm near Pataliputra
			gc.getMap().plot(116, 38).setImprovementType(14) # pasture near Pataliputra
			gc.getMap().plot(141, 51).setImprovementType(4) # farm near Luoyang
			gc.getMap().plot(141, 52).setImprovementType(4) # farm near Luoyang - all to make Roman Empire UHV harder
			
		if iGameTurn == (getTurnForYear(530)):
			gc.getMap().plot(126, 40).setFeatureType(con.iTropicalForest, 0)
			gc.getMap().plot(127, 38).setImprovementType(14) # Dali
			
		if iGameTurn == (getTurnForYear(con.tBirth[con.iTibet]) -10):
			gc.getMap().plot(121, 43).setFeatureType(con.iWoodland, 0)
			gc.getMap().plot(122, 42).setFeatureType(con.iWoodland, 0)
			gc.getMap().plot(123, 40).setFeatureType(con.iTropicalForest, 0)
			gc.getMap().plot(124, 39).setPlotType(PlotTypes.PLOT_HILLS, True, True)# hill
			gc.getMap().plot(124, 36).setFeatureType(con.iTropicalForest, 0)
			gc.getMap().plot(125, 37).setFeatureType(con.iTropicalForest, 0)# access to & from Tibetan plateau
			
		if iGameTurn == (getTurnForYear(con.tBirth[con.iTibet]) -100):
			gc.getMap().plot(129, 42).setFeatureType(con.iWoodland, 0)
			gc.getMap().plot(130, 41).setFeatureType(con.iWoodland, 0) # prevent Qin cheesing the UHV by settling Nanzhao
			
		if iGameTurn == (getTurnForYear(con.tBirth[con.iGokturks]) -10):
			gc.getMap().plot(136, 71).setBonusType(con.iIron)
			
		#if iGameTurn == (getTurnForYear(380)):
			#gc.getMap().plot(67, 67).setBonusType(con.iFur)
			#gc.getMap().plot(70, 67).setBonusType(con.iTimber) # Sarkel
		
		


	def onTechAcquired(self, iTech):
		pass


	def onSetPlayerAlive(self, argsList):
		'Set Player Alive Event'
		iPlayer, bNewValue = argsList
		
		iHuman = utils.getHumanID()
		if iPlayer == iHuman: 
			return
		
		