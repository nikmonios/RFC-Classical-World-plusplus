# The Sword of Islam - Companies

from CvPythonExtensions import *
import CvUtil
import PyHelpers
import Consts as con
from StoredData import sd
from RFCUtils import utils
from operator import itemgetter

# globals
gc = CyGlobalContext()
localText = CyTranslator()
PyPlayer = PyHelpers.PyPlayer

iNumPlayers = con.iNumPlayers
iNumTotalPlayers = con.iNumTotalPlayers
iNumCompanies = con.iNumCompanies
iGrainMerchants = con.iGrainMerchants
iFishMerchants = con.iFishMerchants
iClothMerchants = con.iClothMerchants
iSpiceMerchants = con.iSpiceMerchants
iMasterArtisans = con.iMasterArtisans
iMasterTradesmen = con.iMasterTradesmen

tBabylon = (71,39)
tConstantinople = (53, 51)
tAlexandria = (53,35)
tTyre = (62,40)
tSyracuse = (35, 44)
tMassilia = (27, 54)
tSamarkand = (93, 54)
tKashgar = (106, 58)
tMadurai = (105, 17)
tRhodes = (51, 43)
tWuxi = (150, 46)
tPanyu = (142, 36)
tDunhuang = (120, 58)
tGoa = (100, 24)
tCarthage = (29, 40)
tCherson = (58, 55)

lPermanentGrainCities = [tConstantinople, tAlexandria, tSyracuse, tWuxi, tCarthage, tCherson]
lPermanentFishCities = [tSyracuse, tMassilia, tAlexandria, tMadurai, tRhodes, tWuxi, tPanyu, tGoa, tCarthage]
lPermanentClothCities = [tBabylon, tTyre, tSamarkand, tKashgar, tMadurai, tDunhuang]
lPermanentSpiceCities = [tTyre, tAlexandria, tBabylon, tMadurai, tRhodes, tGoa, tPanyu]

class Companies:


	def checkTurn(self, iGameTurn):
	
		return
	
		"""for iPlayer in range(iNumPlayers):
			pPlayer = gc.getPlayer(iPlayer)
			if pPlayer.getNumCities() > 4:
				if pPlayer.getCapitalCity().getPopulation() > 6:
					gc.getTeam(pPlayer.getTeam()).isHasTech(con.iBulkTrade):
						if pPlayer.getNumAvailableBonuses(con.iFish) > 1 or pPlayer.getNumAvailableBonuses(con.iCrab) > 1 or pPlayer.getNumAvailableBonuses(con.iClam) > 1:
							if pPlayer.getCapitalCity().isCoastal():
								pPlayer.getCapitalCity().setHasCorporation(con.iFishMerchants, True, True, True)
							else:
								apCityList = PyPlayer(iPlayer).getCityList()
								iLargestCoastalCityPop = 0
								for pCity in apCityList:
									city = pCity.GetCy()
									if city.isCoastal():
										if city.getPopulation() > iLargestCoastalCityPop:
											
		
		iCompany = iGameTurn % iNumCompanies
		
		iMaxCompanies = 0
		
		for iLoopCiv in range(iNumPlayers):
			if iCompany in [iSpiceMerchants, iClothMerchants] and gc.getTeam(gc.getPlayer(iLoopCiv).getTeam()).isHasTech(con.iLuxuryTrade): 
				iMaxCompanies += 4
			if iCompany in [iGrainMerchants, iFishMerchants] and gc.getTeam(gc.getPlayer(iLoopCiv).getTeam()).isHasTech(con.iBulkTrade): 
				iMaxCompanies += 4
			if iCompany in [iMasterArtisans, iMasterTradesmen] and gc.getTeam(gc.getPlayer(iLoopCiv).getTeam()).isHasTech(con.iManufacturedTrade): 
				iMaxCompanies += 4
		if iMaxCompanies == 0: 
			return
		
		
		#iMaxCompanies = 10
		
		# loop through all cities, check the company value for each and add the good ones to a list of tuples (city, value)
		cityValueList = []
		for iPlayer in range(iNumPlayers):
			apCityList = PyPlayer(iPlayer).getCityList()
			for pCity in apCityList:
				city = pCity.GetCy()
				iValue = self.getCityValue(city, iCompany)
				if iValue > 0: 
					cityValueList.append((city, iValue * 10 + gc.getGame().getSorenRandNum(10, 'random bonus')))
				elif city.isHasCorporation(iCompany): # quick check to remove companies
					city.setHasCorporation(iCompany, False, True, True)
		
		# sort cities from highest to lowest value
		cityValueList.sort(key=itemgetter(1), reverse=True)
		
		# count the number of companies
		iCompanyCount = 0
		for iLoopPlayer in range(iNumPlayers):
			if utils.isActive(iLoopPlayer):
				iCompanyCount += gc.getPlayer(iLoopPlayer).countCorporations(iCompany)
		
		# debugText = 'ID: %d, ' %(iCompany)
		# spread the company
		for i in range(len(cityValueList)):
			city = cityValueList[i][0]
			if city.isHasCorporation(iCompany):
				# debugText += '%s:%d(skip), ' %(city.getName(), cityValueList[i][1])
				continue
			if iCompanyCount >= iMaxCompanies and i >= iMaxCompanies: # don't spread to weak cities if the limit was reached
				# debugText += 'limit reached'
				break
			city.setHasCorporation(iCompany, True, True, True)
			# debugText += '%s(OK!), ' %(city.getName())
			break
		# utils.echo(debugText)
		
		# if the limit was exceeded, remove company from the worst city
		if iCompanyCount > iMaxCompanies:
			for i in range(len(cityValueList)-1, 0, -1):
				city = cityValueList[i][0]
				if city.isHasCorporation(iCompany):
					city.setHasCorporation(iCompany, False, True, True)
					break"""


	def onPlayerChangeStateReligion(self, argsList):
		iPlayer, iNewReligion, iOldReligion = argsList
		
		return
		
		'''apCityList = PyPlayer(iPlayer).getCityList()
		for pCity in apCityList:
			city = pCity.GetCy()
			for iCompany in range(iNumCompanies):
				if city.isHasCorporation(iCompany):
					if self.getCityValue(city, iCompany) < 0:
						city.setHasCorporation(iCompany, False, True, True)'''
						
	def onCityBuilt(self, city):
	
		tCity = (city.getX(), city.getY())
		if tCity in lPermanentGrainCities:
			city.setHasCorporation(iGrainMerchants, True, True, True)
		if tCity in lPermanentFishCities:
			city.setHasCorporation(iFishMerchants, True, True, True)
		if tCity in lPermanentClothCities:
			city.setHasCorporation(iClothMerchants, True, True, True)
		if tCity in lPermanentSpiceCities:
			city.setHasCorporation(iSpiceMerchants, True, True, True)


	def onCityAcquired(self, argsList):
		iPreviousOwner, iNewOwner, city, bConquest, bTrade = argsList
		
		if iNewOwner == con.iByzantines and iPreviousOwner == con.iRome:
			return
		
		for iCompany in range(iNumCompanies):
			if city.isHasCorporation(iCompany):
				if self.getCityValue(city, iCompany) < 0:
					city.setHasCorporation(iCompany, False, True, True)


	def getCityValue(self, city, iCompany):
		
		if city is None: return -1
		elif city.isNone(): return -1
		
		iValue = 0
		
		owner = gc.getPlayer(city.getOwner())
		ownerTeam = gc.getTeam(owner.getTeam())
		
		if iCompany in [iGrainMerchants, iFishMerchants]:
			if not ownerTeam.isHasTech(con.iBulkTrade): return -1
		if iCompany in [iSpiceMerchants, iClothMerchants]:
			if not ownerTeam.isHasTech(con.iLuxuryTrade): return -1
		if iCompany == iMasterArtisans:
			if not ownerTeam.isHasTech(con.iMetalCasting): return -1
		if iCompany == iMasterTradesmen:
			if not ownerTeam.isHasTech(con.iEngineering): return -1
		
		# trade companies - coastal cities only
		if iCompany in [iGrainMerchants, iFishMerchants]:
			if not city.isCoastal(20):
				return -1
		
		
		# various bonuses
		if city.getNumRealBuilding(con.iPalace) > 0: iValue += 2
		if iCompany == iGrainMerchants:
			if city.getNumRealBuilding(con.iLighthouse) > 0: iValue += 1
			if city.getNumRealBuilding(con.iHarbor) > 0: iValue += 1
			if city.getNumRealBuilding(con.iMarket) > 0: iValue += 1
			if city.getNumRealBuilding(con.iRomanForum) > 0: iValue += 1
			if city.getNumRealBuilding(con.iAntigonidAgora) > 0: iValue += 1
			if city.getNumRealBuilding(con.iGranary) > 0: iValue += 2
			if city.getNumRealBuilding(con.iGrainMarket) > 0: iValue += 3
		if iCompany == iFishMerchants:
			if city.getNumRealBuilding(con.iLighthouse) > 0: iValue += 2
			if city.getNumRealBuilding(con.iHarbor) > 0: iValue += 2
			if city.getNumRealBuilding(con.iMarket) > 0: iValue += 1
			if city.getNumRealBuilding(con.iRomanForum) > 0: iValue += 1
			if city.getNumRealBuilding(con.iAntigonidAgora) > 0: iValue += 1
			if city.getNumRealBuilding(con.iFishMarket) > 0: iValue += 3
		if iCompany == iClothMerchants:
			if city.getNumRealBuilding(con.iFairground) > 0: iValue += 1
			if city.getNumRealBuilding(con.iMarket) > 0: iValue += 1
			if city.getNumRealBuilding(con.iRomanForum) > 0: iValue += 1
			if city.getNumRealBuilding(con.iAntigonidAgora) > 0: iValue += 1
			if city.getNumRealBuilding(con.iClothMarket) > 0: iValue += 3
		if iCompany == iSpiceMerchants:
			if city.getNumRealBuilding(con.iFairground) > 0: iValue += 1
			if city.getNumRealBuilding(con.iMarket) > 0: iValue += 1
			if city.getNumRealBuilding(con.iRomanForum) > 0: iValue += 1
			if city.getNumRealBuilding(con.iAntigonidAgora) > 0: iValue += 1
			if city.getNumRealBuilding(con.iSpiceMarket) > 0: iValue += 3
		if iCompany == iMasterArtisans:
			if city.getNumRealBuilding(con.iBlacksmith) > 0: iValue += 1
			if city.getNumRealBuilding(con.iRoyalMint) > 0: iValue += 1
			if city.getNumRealBuilding(con.iBactrianGoldsmith) > 0: iValue += 1
			if city.getNumRealBuilding(con.iArtisansQuarter) > 0: iValue += 3
		if iCompany == iMasterTradesmen:
			if city.getNumRealBuilding(con.iBlacksmith) > 0: iValue += 1
			if city.getNumRealBuilding(con.iWalls) > 0: iValue += 1
			if city.getNumRealBuilding(con.iCelticDun) > 0: iValue += 1
			if city.getNumRealBuilding(con.iMaccabeeKotel) > 0: iValue += 1
			if city.getNumRealBuilding(con.iCastle) > 0: iValue += 1
			if city.getNumRealBuilding(con.iTradesmensQuarter) > 0: iValue += 3
		
		# resources
		iTempValue = 0
		bFound = False
		for i in range(4):
			iBonus = gc.getCorporationInfo(iCompany).getPrereqBonus(i)
			if iBonus > -1:
				if city.getNumBonuses(iBonus) > 0: bFound = True
				iTempValue += city.getNumBonuses(iBonus)
		if not bFound: return -1
		iValue += iTempValue
		
		
		
		# threshold
		if iValue < 3: return -1
		
		# spread it out
		iValue -= owner.countCorporations(iCompany)
		
		return iValue