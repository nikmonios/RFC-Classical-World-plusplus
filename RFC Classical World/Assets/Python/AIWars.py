# Rhye's and Fall of Civilization - AI Wars

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

### Constants ###

iStartTurn = 10 # down from 20
iMinInterval = 3 # srpt down from 20
iMaxInterval = 12 # down from 40
iThreshold = 100
iMinValue = 20 # down from 30
iNumPlayers = con.iNumPlayers
iIndependent = con.iIndependent
iIndependent2 = con.iIndependent2
iIndependent3 = con.iIndependent3
iNumTotalPlayers = con.iBarbarian

  
class AIWars:


	def setup(self):
		#iTurn = utils.getTurns(iStartTurn + gc.getGame().getSorenRandNum(iMaxInterval-iMinInterval, 'random turn'))
		#sd.setNextTurnAIWar(iTurn)
		#print ("setNextTurnAIWar", iTurn)
		return

	def checkTurn(self, iGameTurn):
	
		iHuman = utils.getHumanID()
		
		
		#turn automatically peace on between independent cities and all the major civs
		if (iGameTurn % 20 == 5):
			utils.restorePeaceHuman(iIndependent3, False)
		if (iGameTurn % 20 == 10):
			utils.restorePeaceHuman(iIndependent2, False)
		if (iGameTurn % 20 == 20):
			utils.restorePeaceHuman(iIndependent, False)
		
		if (iGameTurn % 20 == 1 and iGameTurn > 40):
			utils.restorePeaceAI(iIndependent, False)
		if (iGameTurn % 20 == 6 and iGameTurn > 40):
			utils.restorePeaceAI(iIndependent2, False)
		if (iGameTurn % 20 == 11 and iGameTurn > 40):
			utils.restorePeaceAI(iIndependent3, False)
		
		#turn automatically war on between independent cities and some AI major civs
		if (iGameTurn % 20 == 2 and iGameTurn > 40): #1 turn after restorePeace()
			utils.minorWars(iIndependent)
		if (iGameTurn % 20 == 7 and iGameTurn > 40): #1 turn after restorePeace()
			utils.minorWars(iIndependent2)
		if (iGameTurn % 20 == 12 and iGameTurn > 40): #1 turn after restorePeace()
			utils.minorWars(iIndependent3)
			
		# just another AI war function
		if iGameTurn % 6 == 0 and iGameTurn > 0:
			print "AI War function"
			for iLoopPlayer in range(iNumPlayers):
				# alive, not human, not at war
				if iLoopPlayer != iHuman and gc.getPlayer(iLoopPlayer).isAlive():
					print ("iLoopPlayer", iLoopPlayer)
					if utils.getWarCount(iLoopPlayer) != 0:
						print "already at war"
					else:
						# has a target
						if sd.getWarTarget(iLoopPlayer, 0) != -1:
							print "has a target"
							# target is due
							if iGameTurn >= sd.getWarTarget(iLoopPlayer, 1):
								print "target is due"
								# reset if dead or vassal
								if not (gc.getPlayer(sd.getWarTarget(iLoopPlayer, 0)).isAlive()) or not utils.canDeclareWar(iLoopPlayer, sd.getWarTarget(iLoopPlayer, 0)):
									print "dead or vassal"
									sd.setWarTarget(iLoopPlayer, 0, -1)
								# else declare war
								elif sd.getWarTarget(iLoopPlayer, 2) == True:
									print ("declare total war, target=", sd.getWarTarget(iLoopPlayer, 0))
									gc.getTeam(gc.getPlayer(iLoopPlayer).getTeam()).declareWar(sd.getWarTarget(iLoopPlayer, 0), True, WarPlanTypes.WARPLAN_TOTAL)
									sd.setWarTarget(iLoopPlayer, 0, -1)
									break
								else:
									print ("declare limited war, target=", sd.getWarTarget(iLoopPlayer, 0))
									gc.getTeam(gc.getPlayer(iLoopPlayer).getTeam()).declareWar(sd.getWarTarget(iLoopPlayer, 0), True, WarPlanTypes.WARPLAN_LIMITED)
									sd.setWarTarget(iLoopPlayer, 0, -1)
									break
							# target not yet due
							else:
								print "target not yet due"
								continue
						# has no target
						else:
							print "no target, checking"
							self.checkAIWars(iLoopPlayer, iGameTurn)
			
						

	
		#for iLoopPlayer in range(iNumPlayers):
			#print ("WarTagets, iLoopPlayer", iLoopPlayer, "Target", sd.getWarTarget(iLoopPlayer, 0))
					
	def checkAIWars(self, iPlayer, iGameTurn):
	
		print ("checkAIWars, iPlayer", iPlayer, "iGameTurn", iGameTurn)
		
		#if gc.getGame().getSorenRandNum(100, 'random number') > 50:
			#return
	
		iCiv = sd.getCivilization(iPlayer)
		# foreigners in the core
		iNumForeignCities = 0
		iWarTargetPlayer = -1
		bForeigners = False
		for regionID in con.lCoreRegions[iCiv]:
			if not utils.checkRegionControl(iPlayer, regionID):
				bForeigners = True
				break
		if bForeigners == True:
			print "foreigners in core"
			for iLoopTargetPlayer in range(iNumTotalPlayers):
				iNumCities = 0
				apCityList = PyPlayer(iLoopTargetPlayer).getCityList()
				for pCity in apCityList:
					if pCity.GetCy().plot().getRegionID() in (con.lCoreRegions[iCiv]):
						iNumCities += 1
					if iNumCities > iNumForeignCities:
						iWarTargetPlayer = iLoopTargetPlayer
			if iWarTargetPlayer != -1:
				if utils.canDeclareWar(iPlayer, iWarTargetPlayer):
					sd.setLastAIWar(iPlayer, iGameTurn)
					print ("initWar, iPlayer", iPlayer, "iWarTargetPlayer", iWarTargetPlayer)
					self.initWar(iPlayer, iWarTargetPlayer, iGameTurn)
					return
		
		# passive civs will not declare unless their core is invaded
		if con.tAggression[iCiv] == 0:
			return
							
		# aggressive civs
		if con.tAggression[iCiv] == 2:
			print "Agressive"
		#if con.tAggression[iCiv] >= 0:
			# preferred targets in target regions
			bForeigners = False
			for regionID in con.lTargetRegions[iCiv]:
				if not utils.checkRegionControl(iPlayer, regionID):
					bForeigners = True
					break
			if bForeigners == True:
				print "target civ in target regions"
				iWarTargetPlayer = -1
				iNumForeignCities = 0
				for iLoopTargetPlayer in con.lWarTargets[iCiv]:
					print ("iLoopTargetPlayer", iLoopTargetPlayer)
					if gc.getPlayer(iPlayer).canContact(iLoopTargetPlayer) and gc.getPlayer(iPlayer).AI_getAttitude(iLoopTargetPlayer) <= con.iCautious:
						iNumCities = 0
						apCityList = PyPlayer(iLoopTargetPlayer).getCityList()
						for pCity in apCityList:
							if pCity.GetCy().plot().getRegionID() in (con.lTargetRegions[iCiv]):
								iNumCities += 1
						print("iNumCities", iNumCities)
						if iNumCities > iNumForeignCities and utils.canDeclareWar(iPlayer, iLoopTargetPlayer):
							print ("war target")
							iWarTargetPlayer = iLoopTargetPlayer
							iNumForeignCities = iNumCities
				if iWarTargetPlayer != -1:
					if utils.canDeclareWar(iPlayer, iWarTargetPlayer):
						sd.setLastAIWar(iPlayer, iGameTurn)
						print ("initWar, iPlayer", iPlayer, "iWarTargetPlayer", iWarTargetPlayer)
						self.initWar(iPlayer, iWarTargetPlayer, iGameTurn)
						return
								
			# other targets in target regions
			iNumForeignCities = 0
			iWarTargetPlayer = -1
			bForeigners = False
			for regionID in con.lTargetRegions[iCiv]:
				if not utils.checkRegionControl(iPlayer, regionID):
					bForeigners = True
					break
			if bForeigners == True:
				print "other civ in target regions"
				for iLoopTargetPlayer in range(iNumTotalPlayers):
					if gc.getPlayer(iPlayer).canContact(iLoopTargetPlayer) and gc.getPlayer(iPlayer).AI_getAttitude(iLoopTargetPlayer) <= con.iCautious:
						iNumCities = 0
						apCityList = PyPlayer(iLoopTargetPlayer).getCityList()
						for pCity in apCityList:
							if pCity.GetCy().plot().getRegionID() in (con.lTargetRegions[iCiv]):
								iNumCities += 1
							if iNumCities > iNumForeignCities:
								iWarTargetPlayer = iLoopTargetPlayer
				if iWarTargetPlayer != -1:
					if utils.canDeclareWar(iPlayer, iWarTargetPlayer):
						sd.setLastAIWar(iPlayer, iGameTurn)
						print ("initWar, iPlayer", iPlayer, "iWarTargetPlayer", iWarTargetPlayer)
						self.initWar(iPlayer, iWarTargetPlayer, iGameTurn)
						return
								
			# other targets in normal regions
			iNumForeignCities = 0
			iWarTargetPlayer = -1
			bForeigners = False
			for regionID in con.lNormalRegions[iCiv]:
				if not utils.checkRegionControl(iPlayer, regionID):
					bForeigners = True
					break
			if bForeigners == True:
				print "other civ in normal regions"
				for iLoopTargetPlayer in range(iNumTotalPlayers):
					if gc.getPlayer(iPlayer).canContact(iLoopTargetPlayer) and gc.getPlayer(iPlayer).AI_getAttitude(iLoopTargetPlayer) <= con.iCautious:
						iNumCities = 0
						apCityList = PyPlayer(iLoopTargetPlayer).getCityList()
						for pCity in apCityList:
							if pCity.GetCy().plot().getRegionID() in (con.lNormalRegions[iCiv]):
								iNumCities += 1
							if iNumCities > iNumForeignCities:
								iWarTargetPlayer = iLoopTargetPlayer
				if iWarTargetPlayer != -1:
					if utils.canDeclareWar(iPlayer, iWarTargetPlayer):
						sd.setLastAIWar(iPlayer, iGameTurn)
						print ("initWar, iPlayer", iPlayer, "iWarTargetPlayer", iWarTargetPlayer)
						self.initWar(iPlayer, iWarTargetPlayer, iGameTurn)
						return
								
		# normal civs
		else:
			# other targets in normal regions
			iNumForeignCities = 0
			iWarTargetPlayer = -1
			bForeigners = False
			for regionID in con.lNormalRegions[iCiv]:
				if not utils.checkRegionControl(iPlayer, regionID):
					bForeigners = True
					break
			if bForeigners == True:
				for iLoopTargetPlayer in range(iNumTotalPlayers):
					if gc.getPlayer(iPlayer).canContact(iLoopTargetPlayer) and gc.getPlayer(iPlayer).AI_getAttitude(iLoopTargetPlayer) <= con.iCautious:
						iNumCities = 0
						apCityList = PyPlayer(iLoopTargetPlayer).getCityList()
						for pCity in apCityList:
							if pCity.GetCy().plot().getRegionID() in (con.lNormalRegions[iCiv]):
								iNumCities += 1
							if iNumCities > iNumForeignCities:
								iWarTargetPlayer = iLoopTargetPlayer
				if iWarTargetPlayer != -1:
					if utils.canDeclareWar(iPlayer, iWarTargetPlayer):
						sd.setLastAIWar(iPlayer, iGameTurn)
						print ("initWar, iPlayer", iPlayer, "iWarTargetPlayer", iWarTargetPlayer)
						self.initWar(iPlayer, iWarTargetPlayer, iGameTurn)
						return

	def initWar(self, iPlayer, iTargetCiv, iGameTurn): 
	
	
		"""gc.getTeam(gc.getPlayer(iPlayer).getTeam()).AI_setWarPlan(iTargetCiv, WarPlanTypes.WARPLAN_PREPARING_TOTAL)
		sd.setWarTarget(iPlayer, 0, iTargetCiv)
		sd.setWarTarget(iPlayer, 1, iGameTurn + gc.getGame().getSorenRandNum(3, 'random number'))
		sd.setWarTarget(iPlayer, 2, True)
		print ("setWarTarget, iPlayer", iPlayer, "iTargetCiv", sd.getWarTarget(iPlayer, 0), "iGameTurn", sd.getWarTarget(iPlayer, 1))
		
		return"""
		
		# edead: instead of declaring war, start war preparations; declare immediately if indeps are involved
		if iTargetCiv < iNumPlayers:
			if iPlayer == con.iRome and iTargetCiv != utils.getHumanID() and iTargetCiv in [con.iCelts, con.iCarthage, con.iEgypt, con.iAntigonids, con.iMaccabees]:
				if sd.getRomanAIWar(iTargetCiv) == 0:
					gc.getTeam(gc.getPlayer(iPlayer).getTeam()).declareWar(iTargetCiv, True, -1)
					#print ("declareWar, iPlayer", iPlayer, "iTargetCiv", iTargetCiv)
				else:
					gc.getTeam(gc.getPlayer(iPlayer).getTeam()).AI_setWarPlan(iTargetCiv, WarPlanTypes.WARPLAN_PREPARING_TOTAL)
					sd.setWarTarget(iPlayer, 0, iTargetCiv)
					sd.setWarTarget(iPlayer, 1, iGameTurn + 20 + gc.getGame().getSorenRandNum(10, 'random number'))
					sd.setWarTarget(iPlayer, 2, True)
					#print ("setWarTarget, iPlayer", iPlayer, "iTargetCiv", sd.getWarTarget(iPlayer, 0), "iGameTurn", sd.getWarTarget(iPlayer, 1))
			elif iPlayer == con.iParthia and iTargetCiv != utils.getHumanID() and iTargetCiv in [con.iSeleucids]:
				gc.getTeam(gc.getPlayer(iPlayer).getTeam()).AI_setWarPlan(iTargetCiv, WarPlanTypes.WARPLAN_PREPARING_TOTAL)
				sd.setWarTarget(iPlayer, 0, iTargetCiv)
				sd.setWarTarget(iPlayer, 1, iGameTurn + 20 + gc.getGame().getSorenRandNum(10, 'random number'))
				sd.setWarTarget(iPlayer, 2, True)
				#print ("setWarTarget, iPlayer", iPlayer, "iTargetCiv", sd.getWarTarget(iPlayer, 0), "iGameTurn", sd.getWarTarget(iPlayer, 1))
			elif iPlayer == con.iSassanids and iTargetCiv != utils.getHumanID() and iTargetCiv in [con.iSeleucids, con.iParthia]:
				gc.getTeam(gc.getPlayer(iPlayer).getTeam()).AI_setWarPlan(iTargetCiv, WarPlanTypes.WARPLAN_PREPARING_TOTAL)
				sd.setWarTarget(iPlayer, 0, iTargetCiv)
				sd.setWarTarget(iPlayer, 1, iGameTurn + 20 + gc.getGame().getSorenRandNum(10, 'random number'))
				sd.setWarTarget(iPlayer, 2, True)
				#print ("setWarTarget, iPlayer", iPlayer, "iTargetCiv", sd.getWarTarget(iPlayer, 0), "iGameTurn", sd.getWarTarget(iPlayer, 1))
			elif iPlayer == con.iHan and iTargetCiv != utils.getHumanID() and iTargetCiv in [con.iQin, con.iVietnam]:
				gc.getTeam(gc.getPlayer(iPlayer).getTeam()).AI_setWarPlan(iTargetCiv, WarPlanTypes.WARPLAN_PREPARING_TOTAL)
				sd.setWarTarget(iPlayer, 0, iTargetCiv)
				sd.setWarTarget(iPlayer, 1, iGameTurn + 20 + gc.getGame().getSorenRandNum(10, 'random number'))
				sd.setWarTarget(iPlayer, 2, True)
				#print ("setWarTarget, iPlayer", iPlayer, "iTargetCiv", sd.getWarTarget(iPlayer, 0), "iGameTurn", sd.getWarTarget(iPlayer, 1))
			else:
				gc.getTeam(gc.getPlayer(iPlayer).getTeam()).AI_setWarPlan(iTargetCiv, WarPlanTypes.WARPLAN_PREPARING_LIMITED)
				sd.setWarTarget(iPlayer, 0, iTargetCiv)
				sd.setWarTarget(iPlayer, 1, iGameTurn + 20 + gc.getGame().getSorenRandNum(10, 'random number'))
				sd.setWarTarget(iPlayer, 2, False)
				#print ("setWarTarget, iPlayer", iPlayer, "iTargetCiv", sd.getWarTarget(iPlayer, 0), "iGameTurn", sd.getWarTarget(iPlayer, 1))
		else:
			gc.getTeam(gc.getPlayer(iPlayer).getTeam()).declareWar(iTargetCiv, True, -1)
			#print ("declareWar, iPlayer", iPlayer, "iTargetCiv", iTargetCiv)

		

