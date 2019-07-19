## Sid Meier's Civilization 4
## Copyright Firaxis Games 2005
##
## Implementaion of miscellaneous game functions
# Mercenaries Mod
# By: The Lopez

import CvUtil
import CvGameUtils
import MercenaryUtils

from CvPythonExtensions import *

# globals
gc = CyGlobalContext()
objMercenaryUtils = MercenaryUtils.MercenaryUtils()

CONTRACT_OUT_UNIT = gc.getGame().getMapRand().get(500,"Action")+1000
FIRE_MERCENARY = CONTRACT_OUT_UNIT+1

class CvMercenaryModGameUtils(CvGameUtils.CvGameUtils):

	# This method is called when there is some type of action that wasn't handled.
	def cannotHandleAction(self,argsList):
		pPlot = argsList[0]
		iAction = argsList[1]
		bTestVisible = argsList[2]

		# Handle the contract out button pressed action
		if(iAction == CONTRACT_OUT_UNIT):
			objMercenaryUtils.contractOutUnit(CyInterface().getHeadSelectedUnit())

		# Handle the fire mercenary button pressed action
		if(iAction == FIRE_MERCENARY):
			objMercenaryUtils.fireMercenary(CyInterface().getHeadSelectedUnit().getNameNoDesc(),CyInterface().getHeadSelectedUnit().getOwner()) 

		return False


	# Resets the action button numbers
	def initActionButtonNumbers(self):
		global CONTRACT_OUT_UNIT
		global FIRE_MERCENARY
		
		CONTRACT_OUT_UNIT = gc.getGame().getMapRand().get(500,"Action")+1000
		FIRE_MERCENARY = CONTRACT_OUT_UNIT+1
