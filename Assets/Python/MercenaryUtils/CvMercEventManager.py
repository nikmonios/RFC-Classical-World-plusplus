#
# Mercenaries Mod
# CvMercEventManager
# 

from CvPythonExtensions import *
import CvUtil

import CvEventManager
import sys
import PyHelpers
import CvMainInterface
import CvMercenaryManager
import MercenaryUtils
import CvScreenEnums 
#import CvConfigParser # edead
import Popup as PyPopup
import Consts as con # edead

gc = CyGlobalContext()

objMercenaryUtils = MercenaryUtils.MercenaryUtils()

PyPlayer = PyHelpers.PyPlayer
PyGame = PyHelpers.PyGame()
PyInfo = PyHelpers.PyInfo

# Set g_bGameTurnMercenaryCreation to true if mercenary creation should happen during the 
# onBeginGameTurn method, false if it should happen during the onBeginPlayerTurn method
# Default value is true
g_bGameTurnMercenaryCreation = true

# Set g_bDisplayMercenaryManagerOnBeginPlayerTurn to true if the "Mercenary Manager" 
# screen should be displayed at the beginning of every player turn. 
# Default value is false
g_bDisplayMercenaryManagerOnBeginPlayerTurn = false

# This value also controls the "Mercenary Manager" button and when it should be displayed.
# Default value is "ERA_ANCIENT"
g_iStartingEra = gc.getInfoTypeForString("ERA_ANCIENT")

# Change this to false if mercenaries should be removed from the global mercenary pool 
# at the beginning of the game turn. When set to true a number of mercenaries will 
# wander away from the global mercenary pool. This is another variable used to control 
# the load time for the "Mercenary Manager" screen.
# Default valus is true
g_bWanderlustMercenaries = true

# Change this to increase the max number of mercenaries that may wander away from the
# global mercenary pool.
# Default valus is 3
g_iWanderlustMercenariesMaximum = 7 #Rhye

# Default valus is 0 
g_iWanderlustMercenariesMinimum = 2 #Rhye

# Change this to false to supress the mercenary messages.
# Default value is true
g_bDisplayMercenaryMessages = true

# Set to true to print out debug messages in the logs
g_bDebug = false

# Default value is 1 
g_iUpdatePeriod = 4 #Rhye 5

# Default value is 1 
g_iAIThinkPeriod = 5 #Rhye (5 in Warlords, 4 in vanilla) 6

# globals
###################################################
class CvMercEventManager:

	mercenaryManager = None
	
	def __init__(self, eventManager):
	
		self.EventKeyDown=6
		self.eventManager = eventManager

		# initialize base class
		eventManager.addEventHandler("BeginGameTurn", self.onBeginGameTurn)
		eventManager.addEventHandler("BeginPlayerTurn", self.onBeginPlayerTurn)
		eventManager.addEventHandler("kbdEvent",self.onKbdEvent)
		eventManager.addEventHandler("unitLost",self.onUnitLost)
		eventManager.addEventHandler("unitKilled",self.onUnitKilled)
		eventManager.addEventHandler("OnLoad",self.onLoadGame)
		eventManager.addEventHandler("GameStart",self.onGameStart)
		eventManager.addEventHandler("unitPromoted",self.onUnitPromoted)
		

		self.mercenaryManager = CvMercenaryManager.CvMercenaryManager(CvScreenEnums.MERCENARY_MANAGER)		

		global g_bGameTurnMercenaryCreation
		global g_bDisplayMercenaryManagerOnBeginPlayerTurn
		global g_iStartingEra
		global g_bWanderlustMercenaries
		global g_iWanderlustMercenariesMaximum
		global g_bDisplayMercenaryMessages 
		
##		# Load the Mercenaries Mod Config INI file containing all of the configuration information		
##		config = CvConfigParser.CvConfigParser("Mercenaries Mod Config.ini")
##		
##		# If we actually were able to open the "Mercenaries Mod Config.ini" file then read in the values.
##		# otherwise we'll keep the default values that were set at the top of this file.
##		if(config != None):
##			g_bGameTurnMercenaryCreation = config.getboolean("Mercenaries Mod", "Game Turn Mercenary Creation", true)
##			g_bDisplayMercenaryManagerOnBeginPlayerTurn = config.getboolean("Mercenaries Mod", "Display Mercenary Manager On Begin Player Turn", false)
##			g_iStartingEra = gc.getInfoTypeForString(config.get("Mercenaries Mod","Starting Era","ERA_ANCIENT"))
##			g_bWanderlustMercenaries = config.getboolean("Mercenaries Mod", "Wanderlust Mercenaries", true)
##			g_iWanderlustMercenariesMaximum = config.getint("Mercenaries Mod","Wanderlust Mercenaries Maximum", 5)
##			g_bDisplayMercenaryMessages = config.getboolean("Mercenaries Mod", "Display Mercenary Messages", true)

		objMercenaryUtils = MercenaryUtils.MercenaryUtils()

	
	# This method creates a new instance of the MercenaryUtils class to be used later
	def onLoadGame(self, argsList):

		if gc.getGame().getGameTurn() < getTurnForYear(con.tBirth[gc.getGame().getActivePlayer()]):
			return

		global objMercenaryUtils

		objMercenaryUtils = MercenaryUtils.MercenaryUtils()


	# This method create a new instance of the MercenaryUtils class to be used later
	def onGameStart(self, argsList):
	
		global objMercenaryUtils
		
		objMercenaryUtils = MercenaryUtils.MercenaryUtils()


	# This method will update the players gold, make some mercenaries wander away and add 
	# mercenaries to the global mercenary pool.
	def onBeginGameTurn(self, argsList):
		iGameTurn = argsList[0]
		# Get the list of active players in the game
		#playerList = PyGame.getCivPlayerList()
		
		# Go through each of the players and deduct their mercenary maintenance amount from their gold
		#playerList[i].setGold(playerList[i].getGold()+objMercenaryUtils.getPlayerMercenaryContractIncome(playerList[i].getID())) # edead
		# edead: gold moved to doGold in CvGameUtils.py
	
		iUpdatePeriod = g_iUpdatePeriod
		#if gc.getGame().getGameTurnYear() < 1080 or gc.getGame().getGameTurnYear() > 1220: iUpdatePeriod += 1 # edead: more mercs in 1080-1220
	
		# Have some mercenaries wander away from the global mercenary pool if 
		# g_bWanderlustMercenaries is set to true.	
		if(g_bWanderlustMercenaries):
			#Rhye - start (less frequent updates)
			#wanderingMercenaryCount = gc.getGame().getMapRand().get(g_iWanderlustMercenariesMaximum, "Random Num")
			#objMercenaryUtils.removeMercenariesFromPool(wanderingMercenaryCount)
			teamPlayer = gc.getTeam(gc.getActivePlayer().getTeam())
			#if (not teamPlayer.isHasTech(con.iNationalism)): #edead                    
			if (iGameTurn % iUpdatePeriod == (iUpdatePeriod-1)):
				wanderingMercenaryCount = gc.getGame().getMapRand().get(g_iWanderlustMercenariesMaximum, "Random Num") + g_iWanderlustMercenariesMinimum
				objMercenaryUtils.removeMercenariesFromPool(wanderingMercenaryCount)
			#Rhye - end
			
		# Add the mercenaries to the global mercenary pool if the g_bGameTurnMercenaryCreation 
		# is set to true
		if(g_bGameTurnMercenaryCreation):
			#Rhye - start (less frequent updates)
			#objMercenaryUtils.addMercenariesToPool()                  
			if (iGameTurn % iUpdatePeriod == (iUpdatePeriod-1)):
				objMercenaryUtils.addMercenariesToPool()
				# edead: alert the player when new mercenaries become available in their regional pool
				if iGameTurn >= getTurnForYear(con.tBirth[gc.getGame().getActivePlayer()]): # srpt no mercenary messages during autoplay or if player doesn't have Currency
					teamPlayer = gc.getTeam(gc.getActivePlayer().getTeam())
					if teamPlayer.isHasTech(con.iCurrency):
						if gc.getDefineINT("MERCENARY_POOL_ALERT_ENABLE") and objMercenaryUtils.getBestAvailableMercenary(500, gc.getGame().getActivePlayer()):
							CyInterface().addMessage(gc.getGame().getActivePlayer(), True, con.iDuration, CyTranslator().getText("TXT_KEY_MERCENARY_POOL_ALERT", ()), "", InterfaceMessageTypes.MESSAGE_TYPE_INFO, "", ColorTypes(con.iWhite), -1, -1, False, False)
				# edead: end
			#Rhye - end     
	
	
	# This method will add mercenaries to the global mercenary pool, display the mercenary manager screen
	# and provide the logic to make the computer players think.
	def onBeginPlayerTurn(self, argsList):		
		iGameTurn, iPlayer = argsList

		if gc.getGame().getGameTurn() < getTurnForYear(con.tBirth[gc.getGame().getActivePlayer()]):
			return

		player = gc.getPlayer(iPlayer)
		
		# Debug code - start
		if(g_bDebug):
			CvUtil.pyPrint(player.getName() + " Gold: " + str(player.getGold()) + " is human: " + str(player.isHuman()))
		# Debug code - end
		
		# Add the mercenaries to the global mercenary pool if the 
		# g_bGameTurnMercenaryCreation is set to false
		if(not g_bGameTurnMercenaryCreation):
			objMercenaryUtils.addMercenariesToPool()
		
		# if g_bDisplayMercenaryManagerOnBeginPlayerTurn is true the the player is human
		# then display the mercenary manager screen
		if(g_bDisplayMercenaryManagerOnBeginPlayerTurn and player.isHuman()):
			self.mercenaryManager.interfaceScreen()
		
		# if the player is not human then run the think method
		#Rhye - start
		#objMercenaryUtils.computerPlayerThink(iPlayer)                                        
		
		iAIThinkPeriod = g_iAIThinkPeriod
		#if gc.getGame().getGameTurnYear() < 1080 or gc.getGame().getGameTurnYear() > 1220: iAIThinkPeriod += 1 # edead: more mercs in 1080-1220
		
		if (player.isAlive() and iPlayer < con.iNumPlayers): # edead
			if (iPlayer % iAIThinkPeriod == iGameTurn % iAIThinkPeriod):
				#print ("AI thinking (Mercenaries)", iPlayer) #Rhye
				objMercenaryUtils.computerPlayerThink(iPlayer)                                                                
		#Rhye - end
		
		# Place any mercenaries that might be ready to be placed.
		objMercenaryUtils.placeMercenaries(iPlayer)
		
		
	def onEndPlayerTurn(self, argsList):
		'Called at the end of a players turn'
		iGameTurn, iPlayer = argsList
		
		player = gc.getPlayer(iPlayer)

		CyInterface().addImmediateMessage(player.getName(),"")
			
			
	# This method handles the key input and will bring up the mercenary manager screen if the 
	# player has at least one city and presses the 'M' key.
	def onKbdEvent(self, argsList):
		'keypress handler - return 1 if the event was consumed'
		# TO DO: REMOVE THE FOLLOWING LINE BEFORE RELEASE.
		#gc.getPlayer(0).setGold(20000)
		eventType,key,mx,my,px,py = argsList
			
		theKey=int(key)
		
		# edead: start fix & two shortcuts CTRL-M / ALT-M
		#if ( eventType == self.EventKeyDown and theKey == int(InputTypes.KB_M) and self.eventManager.bAlt and gc.getActivePlayer().getNumCities() > 0 and gc.getActivePlayer().getCurrentEra() >= g_iStartingEra):
		if eventType == self.EventKeyDown and theKey == int(InputTypes.KB_M):
			if self.eventManager.bAlt or self.eventManager.bCtrl:
				if gc.getActivePlayer().getNumCities() > 0 and gc.getActivePlayer().getCurrentEra() >= g_iStartingEra:
					self.mercenaryManager.interfaceScreen()
		# edead: end


	# This method will remove a mercenary unit from the game if it is killed
	def onUnitKilled(self, argsList):
		'Unit Killed'
		unit, iAttacker = argsList
		
		if gc.getGame().getGameTurn() < getTurnForYear(con.tBirth[gc.getGame().getActivePlayer()]):
			return
		
		mercenary = objMercenaryUtils.getMercenary(unit.getNameNoDesc())

		if(mercenary != None and g_bDisplayMercenaryMessages and mercenary.getBuilder() != -1 and unit.isDead()):
			strMessage = mercenary.getName() + " has died under " + gc.getPlayer(mercenary.getOwner()).getName() + "'s service."
			# Inform the player that the mercenary has died.
			CyInterface().addMessage(mercenary.getBuilder(), True, 20, strMessage, "", 0, "", ColorTypes(0), -1, -1, True, True) 

		objMercenaryUtils.removePlayerMercenary(unit)


	# This method will remove a mercenary unit from the game if it is lost
	def onUnitLost(self, argsList):
		'Unit Lost'
		unit = argsList[0]
		
		if gc.getGame().getGameTurn() < getTurnForYear(con.tBirth[gc.getGame().getActivePlayer()]):
			return
		
		# Debug code - start
		if(g_bDebug):
			CvUtil.pyPrint("lost: " + unit.getName())
		# Debug code - end
		
		# If the unit being lost is a mercenary, check to see if they have been
		# replaced by an upgraded version of themselves. If they are then save
		# the new upgraded version of themselves and return immediately.
		if(objMercenaryUtils.isMercenary(unit)):

			# Debug code - start
			if(g_bDebug):		
				CvUtil.pyPrint("mercenary unit lost: " + unit.getName())
			# Debug code - end
				
			# Get the active player ID
			iPlayer = gc.getGame().getActivePlayer()
			
			# Get the reference of the actual player
			pyPlayer = PyPlayer(iPlayer)

			# Get the list of units for the player
			unitList = pyPlayer.getUnitList()
				
			# Go through the list of units to see if an upgraded version of 
			# the unit has been added. If it exists then save it and return
			# immediately.
			for unit in unitList:

				if(unit.getUnitType() != argsList[0].getUnitType() and unit.getNameNoDesc() == argsList[0].getNameNoDesc()):

					# Debug code - start
					if(g_bDebug):		
						CvUtil.pyPrint("mercenary unit upgraded: " + unit.getName())
					# Debug code - end
					
					tmpMerc = objMercenaryUtils.createBlankMercenary()
					tmpMerc.loadUnitData(unit)
					tmpMerc.iBuilder = -1
					objMercenaryUtils.saveMercenary(tmpMerc)
					return
					
		mercenary = objMercenaryUtils.getMercenary(unit.getNameNoDesc())

		if(mercenary != None and g_bDisplayMercenaryMessages and mercenary.getBuilder() != -1 and unit.isDead()):
			strMessage = mercenary.getName() + " was lost under " + gc.getPlayer(mercenary.getOwner()).getName() + "'s service."
			# Inform the player that the mercenary has died.
			CyInterface().addMessage(mercenary.getBuilder(), True, 20, strMessage, "", 0, "", ColorTypes(0), -1, -1, True, True) 
		unit = argsList[0]
		
		# Debug code - start
		if(g_bDebug):		
			CvUtil.pyPrint("lost??: " + unit.getNameNoDesc())	
		# Debug code - end

		objMercenaryUtils.removePlayerMercenary(unit)
		

	# This method will redraw the main interface once a unit is promoted. This way the 
	# gold/turn information will be updated.		
	def onUnitPromoted(self, argsList):
		'Unit Promoted'
		pUnit, iPromotion = argsList
		
		if gc.getGame().getGameTurn() < getTurnForYear(con.tBirth[gc.getGame().getActivePlayer()]):
			return
		
		player = PyPlayer(pUnit.getOwner())

		if(objMercenaryUtils.isMercenary(pUnit)):
			CyInterface().setDirty(InterfaceDirtyBits.GameData_DIRTY_BIT, True)		
			
