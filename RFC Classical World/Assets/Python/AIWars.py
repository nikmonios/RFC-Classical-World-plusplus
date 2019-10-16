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
		if iGameTurn % 7 == 0 and iGameTurn > 0:
			print "AI War function"
			for iLoopPlayer in range(iNumPlayers):
				iCiv = sd.getCivilization(iLoopPlayer)
				# alive, not human, not at war, 10 turns after spawn
				if iLoopPlayer != iHuman and gc.getPlayer(iLoopPlayer).isAlive() and iGameTurn > con.tBirth[iCiv]:
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
		pPlayer = gc.getPlayer(iPlayer)
		tTeam = gc.getTeam(pPlayer.getTeam())
		iCiv = sd.getCivilization(iPlayer)
		iPower = pPlayer.getPower()
		#print ("iCiv=", iCiv)
		iWarTargetPlayer = -1
		
		# foreigners in the core
		lEnemyCities = []
		plotList = utils.getRegionPlotList(con.lCoreRegions[iCiv])
		for tPlot in plotList:
			pCurrent = gc.getMap().plot(tPlot[0], tPlot[1])
			if pCurrent.isCity():
				print ("city in core regions", pCurrent.getPlotCity().getName())
				if pCurrent.getPlotCity().getOwner() != iPlayer:
					print ("foreign city in core regions", pCurrent.getPlotCity().getName())
					lEnemyCities.append(pCurrent.getPlotCity())
					
		if len(lEnemyCities):
			print "foreigners in core"
			iEnemyDistance = 200
			capital = gc.getPlayer(iPlayer).getCapitalCity()
			iCapitalX = capital.getX()
			iCapitalY = capital.getY()
			for pLoopCity in lEnemyCities:
				if gc.getPlayer(iPlayer).canContact(pLoopCity.getOwner()):
					if abs(pLoopCity.getX() - iCapitalX) < iEnemyDistance or abs(pLoopCity.getY() - iCapitalY) < iEnemyDistance :
						iEnemyDistance = max((pLoopCity.getX() - iCapitalX), (pLoopCity.getY() - iCapitalY))
						iWarTargetPlayer = pLoopCity.getOwner()
						print ("iWarTargetPlayer=", iWarTargetPlayer)
						
			if iWarTargetPlayer != -1:
				if utils.canDeclareWar(iPlayer, iWarTargetPlayer):
					if utils.isAVassal(iWarTargetPlayer):
						iMaster = utils.getMaster(iWarTargetPlayer)
						iTotalRivalPower = gc.getPlayer(iMaster).getPower() + gc.getPlayer(iWarTargetPlayer).getPower()
						if iPower > iTotalRivalPower *2/3:
							if pPlayer.AI_getAttitude(iWarTargetPlayer) < con.iFriendly and pPlayer.AI_getAttitude(iMaster) < con.iFriendly:
								self.initWar(iPlayer, iWarTargetPlayer, iGameTurn)
								print ("initWar", iPlayer, iWarTargetPlayer)
								return
					else:
						if iPower > gc.getPlayer(iWarTargetPlayer).getPower() *2/3:
							if pPlayer.AI_getAttitude(iWarTargetPlayer) < con.iFriendly:
								self.initWar(iPlayer, iWarTargetPlayer, iGameTurn)
								print ("initWar", iPlayer, iWarTargetPlayer)
								return
					

		if iWarTargetPlayer == -1:

			# passive civs will not declare war unless their core is invaded
			if con.tAggression[iCiv] == 0:
				return

			# aggressive civs
			if con.tAggression[iCiv] == 2:
				print "Aggressive"
				#if con.tAggression[iCiv] >= 0:
				# preferred targets in target regions
				lEnemyCities = []
				plotList = utils.getRegionPlotList(con.lTargetRegions[iCiv])
				for tPlot in plotList:
					pCurrent = gc.getMap().plot(tPlot[0], tPlot[1])
					if pCurrent.isCity():
						print ("city in target regions", pCurrent.getPlotCity().getName())
						if pCurrent.getPlotCity().getOwner() in con.lWarTargets[iCiv]:
							lEnemyCities.append(pCurrent.getPlotCity())
							print ("target civ city in target regions", pCurrent.getPlotCity().getName())

				if len(lEnemyCities):
					print "war targets in target regions"
					iEnemyDistance = 200
					capital = gc.getPlayer(iPlayer).getCapitalCity()
					iCapitalX = capital.getX()
					iCapitalY = capital.getY()
					for pLoopCity in lEnemyCities:
						if gc.getPlayer(iPlayer).canContact(pLoopCity.getOwner()):
							if abs(pLoopCity.getX() - iCapitalX) < iEnemyDistance or abs(pLoopCity.getY() - iCapitalY) < iEnemyDistance :
								iEnemyDistance = max((pLoopCity.getX() - iCapitalX), (pLoopCity.getY() - iCapitalY))
								iWarTargetPlayer = pLoopCity.getOwner()
								print ("iWarTargetPlayer=", iWarTargetPlayer)
						
					if iWarTargetPlayer != -1:
						if utils.canDeclareWar(iPlayer, iWarTargetPlayer):
							if utils.isAVassal(iWarTargetPlayer):
								iMaster = utils.getMaster(iWarTargetPlayer)
								iTotalRivalPower = gc.getPlayer(iMaster).getPower() + gc.getPlayer(iWarTargetPlayer).getPower()
								if iPower > iTotalRivalPower *2/3:
									if pPlayer.AI_getAttitude(iWarTargetPlayer) < con.iFriendly and pPlayer.AI_getAttitude(iMaster) < con.iFriendly:
										self.initWar(iPlayer, iWarTargetPlayer, iGameTurn)
										print ("initWar", iPlayer, iWarTargetPlayer)
										return
							else:
								if iPower > gc.getPlayer(iWarTargetPlayer).getPower() *2/3:
									if pPlayer.AI_getAttitude(iWarTargetPlayer) < con.iFriendly:
										self.initWar(iPlayer, iWarTargetPlayer, iGameTurn)
										print ("initWar", iPlayer, iWarTargetPlayer)
										return
							
				if iWarTargetPlayer == -1:

					# other civs in target regions
					lEnemyCities = []
					plotList = utils.getRegionPlotList(con.lTargetRegions[iCiv])
					for tPlot in plotList:
						pCurrent = gc.getMap().plot(tPlot[0], tPlot[1])
						if pCurrent.isCity():
							print ("city in target regions", pCurrent.getPlotCity().getName())
							if pCurrent.getPlotCity().getOwner() != iPlayer:
								lEnemyCities.append(pCurrent.getPlotCity())
								print ("other civcity in target regions", pCurrent.getPlotCity().getName())

					if len(lEnemyCities):
						print "other civs in target regions"
						iEnemyDistance = 200
						capital = gc.getPlayer(iPlayer).getCapitalCity()
						iCapitalX = capital.getX()
						iCapitalY = capital.getY()
						for pLoopCity in lEnemyCities:
							if gc.getPlayer(iPlayer).canContact(pLoopCity.getOwner()):
								if abs(pLoopCity.getX() - iCapitalX) < iEnemyDistance or abs(pLoopCity.getY() - iCapitalY) < iEnemyDistance :
									iEnemyDistance = max((pLoopCity.getX() - iCapitalX), (pLoopCity.getY() - iCapitalY))
									iWarTargetPlayer = pLoopCity.getOwner()
									print ("iWarTargetPlayer=", iWarTargetPlayer)
						
						if iWarTargetPlayer != -1:
							if utils.canDeclareWar(iPlayer, iWarTargetPlayer):
								if utils.isAVassal(iWarTargetPlayer):
									iMaster = utils.getMaster(iWarTargetPlayer)
									iTotalRivalPower = gc.getPlayer(iMaster).getPower() + gc.getPlayer(iWarTargetPlayer).getPower()
									if iPower > iTotalRivalPower *2/3:
										if pPlayer.AI_getAttitude(iWarTargetPlayer) < con.iFriendly and pPlayer.AI_getAttitude(iMaster) < con.iFriendly:
											self.initWar(iPlayer, iWarTargetPlayer, iGameTurn)
											print ("initWar", iPlayer, iWarTargetPlayer)
											return
								else:
									if iPower > gc.getPlayer(iWarTargetPlayer).getPower() *2/3:
										if pPlayer.AI_getAttitude(iWarTargetPlayer) < con.iFriendly:
											self.initWar(iPlayer, iWarTargetPlayer, iGameTurn)
											print ("initWar", iPlayer, iWarTargetPlayer)
											return
								
					if iWarTargetPlayer == -1:
						# other civs in normal regions
						lEnemyCities = []
						plotList = utils.getRegionPlotList(con.lNormalRegions[iCiv])
						for tPlot in plotList:
							pCurrent = gc.getMap().plot(tPlot[0], tPlot[1])
							if pCurrent.isCity():
								print ("city in normal regions", pCurrent.getPlotCity().getName())
								if pCurrent.getPlotCity().getOwner() != iPlayer:
									lEnemyCities.append(pCurrent.getPlotCity())
									print ("foreign city in normal regions", pCurrent.getPlotCity().getName())

						if len(lEnemyCities):
							print "other civs in normal regions"
							iEnemyDistance = 200
							capital = gc.getPlayer(iPlayer).getCapitalCity()
							iCapitalX = capital.getX()
							iCapitalY = capital.getY()
							for pLoopCity in lEnemyCities:
								if gc.getPlayer(iPlayer).canContact(pLoopCity.getOwner()):
									if abs(pLoopCity.getX() - iCapitalX) < iEnemyDistance or abs(pLoopCity.getY() - iCapitalY) < iEnemyDistance :
										iEnemyDistance = max((pLoopCity.getX() - iCapitalX), (pLoopCity.getY() - iCapitalY))
										iWarTargetPlayer = pLoopCity.getOwner()
										print ("iWarTargetPlayer=", iWarTargetPlayer)
						
							if iWarTargetPlayer != -1:
								if utils.canDeclareWar(iPlayer, iWarTargetPlayer):
									if utils.isAVassal(iWarTargetPlayer):
										iMaster = utils.getMaster(iWarTargetPlayer)
										iTotalRivalPower = gc.getPlayer(iMaster).getPower() + gc.getPlayer(iWarTargetPlayer).getPower()
										if iPower > iTotalRivalPower:
											if pPlayer.AI_getAttitude(iWarTargetPlayer) < con.iPleased and pPlayer.AI_getAttitude(iMaster) < con.iPleased:
												self.initWar(iPlayer, iWarTargetPlayer, iGameTurn)
												print ("initWar", iPlayer, iWarTargetPlayer)
												return
									else:
										if iPower > gc.getPlayer(iWarTargetPlayer).getPower():
											if pPlayer.AI_getAttitude(iWarTargetPlayer) < con.iPleased:
												self.initWar(iPlayer, iWarTargetPlayer, iGameTurn)
												print ("initWar", iPlayer, iWarTargetPlayer)
												return
									
			# normal civs
			elif con.tAggression[iCiv] == 1:
				print "Normal"
				# other civs in normal regions
				lEnemyCities = []
				plotList = utils.getRegionPlotList(con.lNormalRegions[iCiv])
				for tPlot in plotList:
					pCurrent = gc.getMap().plot(tPlot[0], tPlot[1])
					if pCurrent.isCity():
						print ("city in normal regions", pCurrent.getPlotCity().getName())
						if pCurrent.getPlotCity().getOwner() != iPlayer:
							print ("foreign city in normal regions", pCurrent.getPlotCity().getName())
							lEnemyCities.append(pCurrent.getPlotCity())

				if len(lEnemyCities):
					print "other civs in normal regions"
					iEnemyDistance = 200
					capital = gc.getPlayer(iPlayer).getCapitalCity()
					iCapitalX = capital.getX()
					iCapitalY = capital.getY()
					for pLoopCity in lEnemyCities:
						if gc.getPlayer(iPlayer).canContact(pLoopCity.getOwner()):
							if abs(pLoopCity.getX() - iCapitalX) < iEnemyDistance or abs(pLoopCity.getY() - iCapitalY) < iEnemyDistance :
								iEnemyDistance = max((pLoopCity.getX() - iCapitalX), (pLoopCity.getY() - iCapitalY))
								iWarTargetPlayer = pLoopCity.getOwner()
								print ("iWarTargetPlayer=", iWarTargetPlayer)
						
						if iWarTargetPlayer != -1:
							if utils.canDeclareWar(iPlayer, iWarTargetPlayer):
								if utils.isAVassal(iWarTargetPlayer):
									iMaster = utils.getMaster(iWarTargetPlayer)
									iTotalRivalPower = gc.getPlayer(iMaster).getPower() + gc.getPlayer(iWarTargetPlayer).getPower()
									if iPower > iTotalRivalPower *3/2:
										if pPlayer.AI_getAttitude(iWarTargetPlayer) < con.iCautious and pPlayer.AI_getAttitude(iMaster) < con.iCautious:
											self.initWar(iPlayer, iWarTargetPlayer, iGameTurn)
											print ("initWar", iPlayer, iWarTargetPlayer)
											return
								else:
									if iPower > gc.getPlayer(iWarTargetPlayer).getPower() *3/2:
										if pPlayer.AI_getAttitude(iWarTargetPlayer) < con.iCautious:
											self.initWar(iPlayer, iWarTargetPlayer, iGameTurn)
											print ("initWar", iPlayer, iWarTargetPlayer)
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
			#elif iTargetCiv != utils.getHumanID() and iTargetCiv in con.lWarTargets[sd.getCivilization(iPlayer)]:
				#gc.getTeam(gc.getPlayer(iPlayer).getTeam()).AI_setWarPlan(iTargetCiv, WarPlanTypes.WARPLAN_PREPARING_TOTAL)
				#sd.setWarTarget(iPlayer, 0, iTargetCiv)
				#sd.setWarTarget(iPlayer, 1, iGameTurn + 20 + gc.getGame().getSorenRandNum(10, 'random number'))
				#sd.setWarTarget(iPlayer, 2, True)
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

		

