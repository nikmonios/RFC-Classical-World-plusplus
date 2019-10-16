# RFC Communications Redux - edead

from CvPythonExtensions import *
import CvUtil
import PyHelpers  
import Consts as con
from RFCUtils import utils
from StoredData import sd
from random import shuffle

# globals
gc = CyGlobalContext()
PyPlayer = PyHelpers.PyPlayer


class Communications:


	def checkTurn(self, iGameTurn):
		
		return
		
		"""if iGameTurn >= getTurnForYear(-250):
			civList = utils.getRandomCivList()
			iPlayer = civList[iGameTurn % con.iNumPlayers]
			print ("CommunicationscheckTurn, iPlayer=", iPlayer)
			if gc.getPlayer(iPlayer) != None:
				if gc.getPlayer(iPlayer).isAlive(): # and iGameTurn >= getTurnForYear(con.tBirth[iPlayer]) + utils.getTurns(15):
					self.decay(iPlayer)
			else:
				print "nonetype"""

				
	def decay(self, iPlayer):
		
		pPlayer = gc.getPlayer(iPlayer)
		pTeam = gc.getTeam(gc.getPlayer(iPlayer).getTeam())
		iGameTurn = gc.getGame().getGameTurn()
		cutList = []
		for i in range(con.iNumPlayers):
			if i != iPlayer and gc.getPlayer(i).isAlive() and pTeam.canContact(i) and pPlayer.getBorders(i) > 3:
				if iGameTurn >= getTurnForYear(con.tBirth[i]) + utils.getTurns(15):
					cutList.append(i)

		if not cutList:
			return
					
		shuffle(cutList)
		
		#first browse our cities - if other civs can see our borders
		for pyCity in PyPlayer(iPlayer).getCityList():
			city = pyCity.GetCy()
			for iOtherCiv in cutList:
				if city.plot().isVisible(iOtherCiv, False) and iOtherCiv in cutList:
					cutList.remove(iOtherCiv)
			for x in range(city.getX()-4, city.getX()+5):
				for y in range(city.getY()-4, city.getY()+5):
					plot = gc.getMap().plot(x, y)
					if plot.isVisible(iPlayer, False):
						for iOtherCiv in cutList:
							if plot.getOwner() == iOtherCiv and iOtherCiv in cutList:
								cutList.remove(iOtherCiv)
									
		#then browse their cities - if we can see their borders (view distance is asymmetrical)        
		for iOtherCiv in cutList:
			bNear = False
			for pyCity in PyPlayer(iOtherCiv).getCityList():
				city = pyCity.GetCy()
				for x in range(city.getX()-4, city.getX()+5):
					for y in range(city.getY()-4, city.getY()+5):
						plot = gc.getMap().plot(x, y)
						if plot.isVisible(iOtherCiv, False):
							if plot.getOwner() == iPlayer:
								bNear = True
								break
								break
			if not bNear:
				iChance = 50
				if pPlayer.getBorders(iOtherCiv) == 5:
					iChance = 100
				for iTech in [con.iLuxuryTrade, con.iBureaucracy, con.iNavigation, con.iCartography, con.iBulkTrade]:
					if pTeam.isHasTech(iTech):
						iChance -= 10
				otherPlayer = gc.getPlayer(iOtherCiv)
				
				if gc.getGame().getSorenRandNum(100, 'Cut contact') < iChance:
					pTeam.cutContact(iOtherCiv)
					#utils.echo("Cutting contact between %s and %s." %(pPlayer.getCivilizationShortDescription(0),otherPlayer.getCivilizationShortDescription(0)))
					#print ("Cutting contacts between", pPlayer.getCivilizationShortDescription(0), "and", otherPlayer.getCivilizationShortDescription(0))
					return
