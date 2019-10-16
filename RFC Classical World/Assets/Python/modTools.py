# Stability Checker
from CvPythonExtensions import *
from Consts import *
from RFCUtils import utils
import PyHelpers
from StoredData import sd
import UnitArtStyler

gc = CyGlobalContext()
localText = CyTranslator()
PyPlayer = PyHelpers.PyPlayer

def updateUnitArt():

	# update unit art styles of independents
	for iLoopPlayer in range(iIndependent, iBarbarian + 1):
		unitList = PyPlayer(iLoopPlayer).getUnitList()
		for pUnit in unitList:
			UnitArtStyler.updateUnitArt(pUnit)

def setCivDesc(iPlayer, sName, sShort="", sAdj="", sLeader=""):
	
	pPlayer = gc.getPlayer(iPlayer)
	pPlayer.setCivName(localText.getText(sName, ()), localText.getText(sShort, ()), localText.getText(sAdj, ()))
	pPlayer.setName(localText.getText(sLeader, ()))

def setTech(iPlayer, iTech):
	
	gc.getTeam(gc.getPlayer(iPlayer).getTeam()).setHasTech(iTech, True, iRome, False, False)

def switchPlayer(iPlayer):

	gc.getGame().setActivePlayer(iPlayer, False)
	
def setCivic(iPlayer, iCivicOption, iCivic):
	
	gc.getPlayer(iPlayer).setCivics(iCivicOption, iCivic)


def printStabilityData(iPlayer):

	pPlayer = gc.getPlayer(iPlayer)
	pTeam = gc.getTeam(pPlayer.getTeam())
	apCityList = PyPlayer(iPlayer).getCityList()
	iCiv = sd.getCivilization(iPlayer)
	print ("iCiv=", iCiv)
	iGameTurn = gc.getGame().getGameTurn()
	
	iCivicGovernment = pPlayer.getCivics(0)
	iCivicLegal = pPlayer.getCivics(1)
	iCivicLabor = pPlayer.getCivics(2)
	iCivicEconomy = pPlayer.getCivics(3)
	iCivicReligion = pPlayer.getCivics(4)
	
	iStateReligion = pPlayer.getStateReligion()
	
	iNumCities = pPlayer.getNumCities()
	if iNumCities < 1: iNumCities =1
	
	# CIVICS
	print "CIVICS"
	
	iCivicsRating = 2 # srpt civics is hurting too much
		
	if iCivicGovernment == iMonarchyCivic:
		if iCivicLegal == iBarbarismCivic: 
			iCivicsRating -= 1
			print ("bad combo", "monarchy", "barbarism")
		if iCivicLegal in [iVassalageCivic, iReligiousLawCivic]: 
			iCivicsRating += 1
			print ("good combo", "monarchy", "vassalage, or religious law")
		if iCivicLabor == iSerfdomCivic: 
			iCivicsRating += 1
			print ("good combo", "monarchy", "serfdom")
		if iCivicLabor == iWageLaborCivic: 
			iCivicsRating -= 1
			print ("bad combo", "monarchy", "wage labor")
		if iCivicEconomy == iPatronageCivic: 
			iCivicsRating += 1
			print ("good combo", "monarchy", "patronage")
		if iCivicReligion in [iDynasticCultCivic, iStateReligionCivic]: 
			iCivicsRating += 1
			print ("good combo", "monarchy", "dynastic cult or state religion")
		
	if iCivicGovernment == iOligarchyCivic:
		if iCivicLegal in [iBarbarismCivic, iTyrannyCivic]: 
			iCivicsRating -= 1
			print ("bad combo", "oligrachy", "barbarism or tyranny")
		if iCivicLegal == iBureaucracyCivic: 
			iCivicsRating += 1
			print ("good combo", "oligrachy", "bureaucracy")
		if iCivicLabor == iTribalismCivic: 
			iCivicsRating -= 1
			print ("bad combo", "oligrachy", "tribalism")
		if iCivicReligion in [iDynasticCultCivic, iMilitancyCivic]: 
			iCivicsRating -= 1
			print ("bad combo", "oligrachy", "dynastic cult or militancy")
		if iCivicEconomy in [iAgrarianismCivic, iPatronageCivic]: 
			iCivicsRating += 1
			print ("good combo", "oligrachy", "agrarianism or patronage")
		
	if iCivicGovernment == iEmpireCivic:
		if iCivicLegal == iBureaucracyCivic: 
			iCivicsRating += 1
			print ("good combo", "empire", "bureaucracy")
		if iCivicLegal in [iBarbarismCivic, iTyrannyCivic]: 
			iCivicsRating -= 1
			print ("bad combo", "empire", "tyranny")
		if iCivicLabor == iTribalismCivic: 
			iCivicsRating -= 1
			print ("bad combo", "empire", "tribalism")
		if iCivicEconomy == iDecentralizationCivic: 
			iCivicsRating -= 1
			print ("bad combo", "empire", "decentralization")
		if iCivicEconomy == iAgrarianismCivic: 
			iCivicsRating += 1
			print ("good combo", "empire", "agrarianism")
		
	if iCivicLegal == iBarbarismCivic:
		if iCivicLabor == iWageLaborCivic: 
			iCivicsRating -= 1
			print ("bad combo", "barbarism", "wage labor")
		if iCivicEconomy == iTradeEconomyCivic: 
			iCivicsRating -= 1
			print ("bad combo", "barbarism", "trade economy")
		
	if iCivicLegal == iTyrannyCivic:
		if iCivicLabor in [iCasteSystemCivic, iWageLaborCivic]: 
			iCivicsRating -= 1
			print ("bad combo", "tyranny", "caste system or wage labor")
		if iCivicEconomy == iTradeEconomyCivic: 
			iCivicsRating -= 1
			print ("bad combo", "tyranny", "trade economy")
		if iCivicReligion == iDynasticCultCivic: 
			iCivicsRating += 1
			print ("good combo", "tyranny", "dynastic cult")
		if iCivicReligion in [iStateReligionCivic, iMilitancyCivic, iSyncretismCivic]: 
			iCivicsRating -= 1
			print ("bad combo", "tyranny", "state religion, militancy or syncretism")
		
	if iCivicLegal == iVassalageCivic:
		if iCivicLabor in [iCasteSystemCivic, iSerfdomCivic]: 
			iCivicsRating += 1
			print ("good combo", "vassalge", "caste system or serfdom")
		if iCivicLabor == iWageLaborCivic: 
			iCivicsRating -= 1
			print ("bad combo", "vassalge", "wage labor")
		if iCivicEconomy == iTradeEconomyCivic: 
			iCivicsRating -= 1
			print ("bad combo", "vassalge", "trade economy")
		if iCivicEconomy == iPatronageCivic: 
			iCivicsRating += 1
			print ("good combo", "vassalge", "patronage")
		if iCivicReligion == iDynasticCultCivic: 
			iCivicsRating -= 1
			print ("bad combo", "vassalage", "dynastic cult")
		
	if iCivicLegal == iReligiousLawCivic:
		if iCivicLabor in [iCasteSystemCivic, iSerfdomCivic]: 
			iCivicsRating += 1
			print ("good combo", "religious law", "caste system or serfdom")
		if iCivicLabor == iWageLaborCivic: 
			iCivicsRating -= 1
			print ("bad combo", "religious law", "wage labor")
		if iCivicEconomy in [iTradeEconomyCivic, iMilitaryEconomyCivic]: 
			iCivicsRating -= 1
			print ("bad combo", "religious law", "trade economy or military economy")
		if iCivicReligion in [iPaganismCivic, iDynasticCultCivic, iSyncretismCivic]: 
			iCivicsRating -= 1
			print ("bad combo", "religious law", "paganism, dynastic cult or syncretism")
		
	if iCivicLegal == iBureaucracyCivic:
		if iCivicLabor in [iTribalismCivic, iCasteSystemCivic]: 
			iCivicsRating -= 1
			print ("bad combo", "bureaucracy", "tribalism or caste system")
		if iCivicLabor == iSlaveryCivic: 
			iCivicsRating += 1
			print ("good combo", "bureaucracy", "slavery")
		if iCivicEconomy == iDecentralizationCivic: 
			iCivicsRating -= 1
			print ("bad combo", "bureaucracy", "decentralization")
		
	if iCivicLabor == iTribalismCivic:
		if iCivicEconomy == iDecentralizationCivic: 
			iCivicsRating += 1
			print ("good combo", "tribalism", "decentralization")
		if iCivicEconomy in [iTradeEconomyCivic, iMilitaryEconomyCivic]: 
			iCivicsRating -= 1
			print ("bad combo", "tribalism", "trade economy or military economy")
		if iCivicReligion == iDynasticCultCivic: 
			iCivicsRating -= 1
			print ("bad combo", "tribalism", "dynastic cult")
		
	if iCivicLabor == iSlaveryCivic:
		if iCivicEconomy == iAgrarianismCivic: 
			iCivicsRating += 1
			print ("good combo", "slavery", "agrarianism")
		
	if iCivicLabor == iCasteSystemCivic:
		if iCivicEconomy == iAgrarianismCivic: 
			iCivicsRating += 1
			print ("good combo", "caste system", "agrarianism")
		if iCivicEconomy == iTradeEconomyCivic: 
			iCivicsRating -= 1
			print ("bad combo", "caste system", "trade economy")
		if iCivicReligion in [iDynasticCultCivic, iSyncretismCivic]: 
			iCivicsRating -= 1
			print ("bad combo", "caste system", "dynastic cult or syncretism")
		
	if iCivicLabor == iSerfdomCivic:
		if iCivicEconomy == iAgrarianismCivic: 
			iCivicsRating += 1
			print ("good combo", "serfdom", "agrarianism")
		if iCivicEconomy == iTradeEconomyCivic: 
			iCivicsRating -= 1
			print ("bad combo", "serfdom", "trade economy")
		if iCivicReligion == iStateReligionCivic: 
			iCivicsRating += 1
			print ("good combo", "serfdom", "state religion")
		
	if iCivicLabor == iWageLaborCivic:
		if iCivicEconomy in [iDecentralizationCivic, iAgrarianismCivic]: 
			iCivicsRating -= 1
			print ("bad combo", "wage labor", "decentralization or agrarianism")
		if iCivicEconomy == iTradeEconomyCivic: 
			iCivicsRating += 1
			print ("good combo", "wage labor", "trade economy")
		if iCivicReligion == iMilitancyCivic: 
			iCivicsRating -= 1
			print ("bad combo", "wage labor", "militancy")
		
	if iCivicEconomy == iTradeEconomyCivic:
		if iCivicReligion in [iDynasticCultCivic, iMilitancyCivic]: 
			iCivicsRating -= 1
			print ("bad combo", "trade economy", "dynastic cult or militancy")
		
	# Civics + State Religion
		
	if iCivicLabor == iCasteSystemCivic and iStateReligion != iHinduism: 
		iCivicsRating -= 1
		print "caste wo hindu"
	
	if iCivicLabor == iSlaveryCivic and iStateReligion == iChristianity: 
		iCivicsRating -= 1
		print "christian slaves"
		
	print ("Civics rating:", iCivicsRating)
	print ("stored civics rating", sd.getCivicsStability(iPlayer))
	
	## HAPPINESS AND HEALTH ##
	print "HEALTH & HAPPINESS"
	# balance of health and happiness per city, with extra penalty for angry citizens
	
	iHappinessAndHealthRating = 0
	print ("total happy", pPlayer.calculateTotalCityHappiness(), "total unhappy", pPlayer.calculateTotalCityUnhappiness(), "cities", iNumCities)
	print ("total health", pPlayer.calculateTotalCityHealthiness(), "total unhealth", pPlayer.calculateTotalCityUnhealthiness(), "cities", iNumCities)
	iHappiness = ((pPlayer.calculateTotalCityHappiness()) - (pPlayer.calculateTotalCityUnhappiness())) / (iNumCities)
	iHealth = ((pPlayer.calculateTotalCityHealthiness()) - (pPlayer.calculateTotalCityUnhealthiness())) / (iNumCities)
	print ("iHappiness=", iHappiness, "iHealth=", iHealth)
	
	if iHappiness < 0: iHappinessAndHealthRating -= 1
	elif iHappiness > 3: iHappinessAndHealthRating += 1
	
	if iHealth < 0: iHappinessAndHealthRating -= 1
	elif iHealth > 3: iHappinessAndHealthRating += 1
	
	if iPlayer == utils.getHumanID(): # I think this kills the AI unfairly
			for pLoopCity in apCityList:
				if (pLoopCity.GetCy().angryPopulation(0) > 0): 
					iHappinessAndHealthRating -= 1
					print "angry city"
			
	print ("Health & Happiness rating:", iHappinessAndHealthRating)
	
	## ECONOMY ##
	print "ECONOMY"
	# balance of income and costs
	
	iEconomyRating = 0
	
	#if pPlayer.getGold() < 300:
	iRate = (pPlayer.calculateGoldRate() + pPlayer.calculateBaseNetResearch()) - (pPlayer.calculateInflatedCosts())
	print ("gold=", pPlayer.calculateGoldRate(), "research=", pPlayer.calculateBaseNetResearch(), "costs=", pPlayer.calculateInflatedCosts(), "iRate", iRate)
	
	if iRate < -300: iEconomyRating -= 4
	elif iRate < -200: iEconomyRating -= 3
	elif iRate < -100: iEconomyRating -= 2
	elif iRate < -20: iEconomyRating -= 1
	elif iRate > +10: iEconomyRating += 1
	elif iRate > +30: iEconomyRating += 2
		
		
	iEconomy = pPlayer.calculateTotalYield(YieldTypes.YIELD_COMMERCE) - pPlayer.calculateInflatedCosts()
	iIndustry = pPlayer.calculateTotalYield(YieldTypes.YIELD_PRODUCTION)
	iAgriculture = pPlayer.calculateTotalYield(YieldTypes.YIELD_FOOD)
	
	iGrowth = iEconomy + iIndustry + iAgriculture
		
		
	if iGrowth * 2 < sd.getOldEconomyRating(iPlayer): 
		iEconomyRating -= 3 
		print "high economic decline"
	elif iGrowth * 4 < sd.getOldEconomyRating(iPlayer) * 3: 
		iEconomyRating -= 2 
		print "med economic decline"
	elif iGrowth < sd.getOldEconomyRating(iPlayer): 
		iEconomyRating -= 1
		print "some economic decline"
	
	sd.setOldEconomyRating(iPlayer, iGrowth)
	
	print ("Economy rating:", iEconomyRating)
	
	## EMPIRE ##
	print "EMPIRE"
	# balance of core and empire populations, mitigated by courthouses and civics
	
	iEmpireRating = 0
	bExiled = True
	for regionID in utils.getCoreRegions(iCiv):
			if (utils.checkRegionOwnedCity(iPlayer, regionID)): 
				bExiled = False
			if not (utils.checkRegionControl(iPlayer, regionID)):
				iEmpireRating -= 4
				print "core province not controlled"
	if bExiled:
		print "Exiled"
			
	iCorePop = 0
	iEmpirePop = 0
	for pLoopCity in apCityList:
		if pLoopCity.GetCy().isCapital():
			iCorePop += pLoopCity.getPopulation() * 3
		else:
			regionID = gc.getMap().plot(pLoopCity.GetCy().getX(),pLoopCity.GetCy().getY()).getRegionID()
			if regionID in utils.getCoreRegions(iCiv) or regionID in utils.getSpecialRegions(iCiv): 
				iCorePop += pLoopCity.getPopulation() * 2
			elif regionID in utils.getNormalRegions(iCiv):
				iFactor = 1
				if not ((iCivicGovernment == iTheocracyCivic) and (pLoopCity.GetCy().isHasReligion(iStateReligion))):
					if iCivicGovernment != iEmpireCivic: iFactor += 1
				if not (iCivicLegal == iBureaucracyCivic):
					iFactor += 1
				if not (pLoopCity.GetCy().getNumRealBuilding(iCourthouse)): 
					iFactor += 1
				iEmpirePop += pLoopCity.getPopulation() * iFactor
			else:
				iFactor = 2
				if not ((iCivicGovernment == iTheocracyCivic) and (pLoopCity.GetCy().isHasReligion(iStateReligion))):
					if iCivicGovernment != iEmpireCivic: iFactor += 1
				if not (iCivicLegal == iBureaucracyCivic):
					iFactor += 1
				if not (pLoopCity.GetCy().getNumRealBuilding(iCourthouse) > 0):
					iFactor += 1
				iEmpirePop += pLoopCity.getPopulation() * iFactor
				
	if (pPlayer.getNumCities()) * 2 < (sd.getNumCities(iPlayer)): 
		iEmpireRating -= 6
		print "high city losses"
	elif (pPlayer.getNumCities()) * 3 < (sd.getNumCities(iPlayer)) * 2: 
		iEmpireRating -= 3
		print "med city losses"
	elif pPlayer.getNumCities() < sd.getNumCities(iPlayer): 
		iEmpireRating -= 1
		print "some losses"
		
	print ("iCorePop=", iCorePop, "iEmpirePop=", iEmpirePop)
			

	if iCorePop > iEmpirePop *2: iEmpireRating += 2
	elif iCorePop > iEmpirePop: iEmpireRating += 1
	elif iCorePop *5 < iEmpirePop: iEmpireRating -= 5
	elif iCorePop *4 < iEmpirePop: iEmpireRating -= 4
	elif iCorePop *3 < iEmpirePop: iEmpireRating -= 3
	elif iCorePop *2 < iEmpirePop: iEmpireRating -= 2
	elif iCorePop < iEmpirePop: iEmpireRating -= 1
	
	print ("iEmpireRating=", iEmpireRating)
	
	
	## RELIGION ##
	print "RELIGION"
	iReligionRating = 0
	iNumForeignReligions = 0
	iNumNonbelievingCities = 0
	
	if (iCivicReligion == iDynasticCultCivic) or (iCivicReligion == iPaganismCivic): 
		for pLoopCity in apCityList:
			for iLoopReligion in range(iNumReligions):
				if pLoopCity.GetCy().isHasReligion(iLoopReligion):
					if iLoopReligion != iHinduism: 
						iNumForeignReligions += 1
					elif iLoopReligion == iHinduism and iCivicLabor != iCasteSystemCivic:
						iNumForeignReligions += 1
	elif iCivicReligion == iStateReligionCivic: 
		for pLoopCity in apCityList:
			if not pLoopCity.GetCy().isHasReligion(iStateReligion):
				iNumNonbelievingCities += 2
			for iLoopReligion in range(iNumReligions):
				if pLoopCity.GetCy().isHasReligion(iLoopReligion) and iLoopReligion != iStateReligion:
					iNumForeignReligions += 1
	elif (iCivicReligion == iMilitancyCivic) or (iCivicGovernment == iTheocracyCivic): 
		for pLoopCity in apCityList:
			if not pLoopCity.GetCy().isHasReligion(iStateReligion):
				iNumNonbelievingCities += 2
			for iLoopReligion in range(iNumReligions):
				if pLoopCity.GetCy().isHasReligion(iLoopReligion) and iLoopReligion != iStateReligion:
					iNumForeignReligions += 2
					
	print ("iNumForeignReligions", iNumForeignReligions, "iNumNonbelievingCities", iNumNonbelievingCities, "iNumCities", iNumCities)
					
	if iNumNonbelievingCities *2 > iNumCities: iReligionRating -= 2
	elif iNumNonbelievingCities *4 > iNumCities: iReligionRating -= 1
	
	if iNumForeignReligions > iNumCities *2: iReligionRating -= 2
	elif iNumForeignReligions > iNumCities: iReligionRating -= 1
	
	print ("iReligionRating=", iReligionRating)
	
	print "TOTALS"
	print ("Total:", iCivicsRating + iHappinessAndHealthRating + iEconomyRating + iEmpireRating + iReligionRating)
	
	
	def stabilityCheck(iPlayer, iAdjustment = 0):
	
		#print "stabilityCheck called"
	
		#CyInterface().addMessage(utils.getHumanID(), True, iDuration, CyTranslator().getText("STABILITY CHECK", ()) + " " + gc.getPlayer(iPlayer).getCivilizationDescription(0), "", 0, "", ColorTypes(iRed), -1, -1, True, True)
		if (iPlayer > iNumPlayers):
			return
		pPlayer = gc.getPlayer(iPlayer)
		pTeam = gc.getTeam(pPlayer.getTeam())
		apCityList = PyPlayer(iPlayer).getCityList()
		iCiv = sd.getCivilization(iPlayer)
		iGameTurn = gc.getGame().getGameTurn()
		iCivicGovernment = pPlayer.getCivics(0)
		iCivicLegal = pPlayer.getCivics(1)
		iCivicLabor = pPlayer.getCivics(2)
		iCivicReligion = pPlayer.getCivics(4)
		
		# calibrate the system here:
		#iAdjustment -= 1
		
		if utils.getYear() > tFall[iCiv]:
			iAdjustment -= 3
		
		if iPlayer == iRome and (tBirth[iByzantines] + 20) > utils.getYear() > (tBirth[iByzantines] - 20):
			#print "pass on Byzantine birth"
			return
		
		
		
		if (iGameTurn < getTurnForYear(tBirth[iPlayer]) + 50):
			#print "pass, too early"
			return
			
		if iPlayer == iRome and gc.getPlayer(iByzantines).isAlive() and sd.getCivilization(iByzantines) == iRebelRome:
			#print "pass for Rome during civil war"
			return
		
		'''if pTeam.isHasTech(iStabilityCollapsing):
			if iGameTurn > getTurnForYear(tFall[iCiv]):
				print ("quick terminal crisis, iCiv=", gc.getPlayer(iPlayer).getCivilizationShortDescription(0), "year=", utils.getYear())
				self.terminalCrisis(iPlayer, iCiv, pPlayer, pTeam)
				return
			else:
				print ("quick severe crisis, iCiv=", gc.getPlayer(iPlayer).getCivilizationShortDescription(0), "year=", utils.getYear())
				self.severeCrisis(iPlayer, iCiv, pPlayer, pTeam)
				return'''
		

		
		## CIVICS ##
		
		# combinations of civics and state religions
		
		# Civics
		#print "CIVICS"
		
		iCivicsRating = sd.getCivicsStability(iPlayer)
		
		

			
		## HAPPINESS AND HEALTH ##
		#print "HEALTH & HAPPINESS"
		# balance of health and happiness per city, with extra penalty for angry citizens
		
		iNumCities = pPlayer.getNumCities()
		if iNumCities < 1: iNumCities =1
		
		iHappinessAndHealthRating = 0
		#print ("total happy", pPlayer.calculateTotalCityHappiness(), "total unhappy", pPlayer.calculateTotalCityUnhappiness(), "cities", iNumCities)
		#print ("total health", pPlayer.calculateTotalCityHealthiness(), "total unhealth", pPlayer.calculateTotalCityUnhealthiness(), "cities", iNumCities)
		iHappiness = ((pPlayer.calculateTotalCityHappiness()) - (pPlayer.calculateTotalCityUnhappiness())) / (iNumCities)
		iHealth = ((pPlayer.calculateTotalCityHealthiness()) - (pPlayer.calculateTotalCityUnhealthiness())) / (iNumCities)
		#print ("iHappiness=", iHappiness, "iHealth=", iHealth)
		
		if iHappiness < 0: iHappinessAndHealthRating -= 1
		elif iHappiness > 3: iHappinessAndHealthRating += 1
		
		if iHealth < 0: iHappinessAndHealthRating -= 1
		elif iHealth > 3: iHappinessAndHealthRating += 1
		
		if iPlayer == utils.getHumanID(): # I think this kills the AI unfairly
			for pLoopCity in apCityList:
				if (pLoopCity.GetCy().angryPopulation(0) > 0): 
					iHappinessAndHealthRating -= 1
					#print "angry city"
		
		## ECONOMY ##
		#print "ECONOMY"
		# balance of income and costs
		
		iEconomyRating = 0
		
		iRate = (pPlayer.calculateGoldRate() + pPlayer.calculateBaseNetResearch()) - (pPlayer.calculateInflatedCosts())
		#print ("gold=", pPlayer.calculateGoldRate(), "research=", pPlayer.calculateBaseNetResearch(), "costs=", pPlayer.calculateInflatedCosts(), "iRate", iRate)
		
		if iRate < -300: iEconomyRating -= 4
		elif iRate < -200: iEconomyRating -= 3
		elif iRate < -100: iEconomyRating -= 2
		elif iRate < -20: iEconomyRating -= 1
		elif iRate > +10: iEconomyRating += 1
		elif iRate > +30: iEconomyRating += 2
			
		#else:
			#iEconomyRating += 2
			#print "pass on savings"
			
		## EMPIRE ##
		#print "EMPIRE"
		# balance of core and empire populations, mitigated by courthouses and civics
		
		iEmpireRating = 0
		bExiled = True
		for regionID in utils.getCoreRegions(iCiv):
			if (utils.checkRegionOwnedCity(iPlayer, regionID)): 
				bExiled = False
			if not (utils.checkRegionControl(iPlayer, regionID)):
				iEmpireRating -= 4
				#print "core province not controlled"
		if bExiled:
			#print "Exiled"
			self.terminalCrisis(iPlayer, iCiv, pPlayer, pTeam)
				
		iCorePop = 0
		iEmpirePop = 0
		for pLoopCity in apCityList:
			if not pLoopCity.isNone(): # possible fix for C++ exception 
				if pLoopCity.GetCy().isCapital():
					iCorePop += pLoopCity.getPopulation() * 3
				else:
					regionID = gc.getMap().plot(pLoopCity.GetCy().getX(),pLoopCity.GetCy().getY()).getRegionID()
					if regionID in utils.getCoreRegions(iCiv) or regionID in utils.getSpecialRegions(iCiv): 
						iCorePop += pLoopCity.getPopulation() * 2
					elif regionID in utils.getNormalRegions(iCiv):
						iFactor = 1
						if not ((iCivicGovernment == iTheocracyCivic) and (pLoopCity.GetCy().isHasReligion(iStateReligion))):
							if iCivicGovernment != iEmpireCivic: iFactor += 1
						if not (iCivicLegal == iBureaucracyCivic):
							iFactor += 1
						print "C++ exception, Normal Regions", ("iPlayer = ", iPlayer), ("Year = ", utils.getYear()), ("Location = ", "(",pLoopCity.GetCy().getX(),",",pLoopCity.GetCy().getY())
						if not (pLoopCity.GetCy().getNumRealBuilding(iCourthouse)): 
							print "Courthouse statement answered no"
							iFactor += 1
						else:
							print "Courthouse statement answered yes"
						iEmpirePop += pLoopCity.getPopulation() * iFactor
					else:
						iFactor = 2
						if not ((iCivicGovernment == iTheocracyCivic) and (pLoopCity.GetCy().isHasReligion(iStateReligion))):
							if iCivicGovernment != iEmpireCivic: iFactor += 1
						if not (iCivicLegal == iBureaucracyCivic):
							iFactor += 1
						print "C++ exception, Other Regions", ("iPlayer = ", iPlayer), ("Year = ", utils.getYear()), ("Location = ", "(",pLoopCity.GetCy().getX(),",",pLoopCity.GetCy().getY())
						if not (pLoopCity.GetCy().getNumRealBuilding(iCourthouse)): 
							print "Courthouse statement answered no"
							iFactor += 1
						else:
							print "Courthouse statement answered yes"
						iEmpirePop += pLoopCity.getPopulation() * iFactor
			
		#print ("iCorePop=", iCorePop, "iEmpirePop=", iEmpirePop)
				
		#if iCorePop > iEmpirePop *5: iEmpireRating += 5
		#elif iCorePop > iEmpirePop *4: iEmpireRating += 4
		#elif iCorePop > iEmpirePop *3: iEmpireRating += 3
		#iEmpireRating += self.empireStability(iCorePop, iEmpirePop)
		
		if iCorePop > iEmpirePop *2: iEmpireRating += 2
		elif iCorePop > iEmpirePop: iEmpireRating += 1
		elif iCorePop *5 < iEmpirePop: iEmpireRating -= 5
		elif iCorePop *4 < iEmpirePop: iEmpireRating -= 4
		elif iCorePop *3 < iEmpirePop: iEmpireRating -= 3
		elif iCorePop *2 < iEmpirePop: iEmpireRating -= 2
		elif iCorePop < iEmpirePop: iEmpireRating -= 1
		
		#if iCorePop < iEmpirePop:
			#iEmpireRating -= (((iEmpirePop * 10) / iCorePop) * ((iEmpirePop * 10) / iCorePop)) / 100
		
		#print ("iEmpireRating=", iEmpireRating)
		
		## RELIGION ##
		#print "RELIGION"
		iReligionRating = 0
		iNumForeignReligions = 0
		iNumNonbelievingCities = 0
		
		if (iCivicReligion == iDynasticCultCivic) or (iCivicReligion == iPaganismCivic): 
			for pLoopCity in apCityList:
				for iLoopReligion in range(iNumReligions):
					if pLoopCity.GetCy().isHasReligion(iLoopReligion):
						if iLoopReligion != iHinduism: 
							iNumForeignReligions += 1
						elif iLoopReligion == iHinduism and iCivicLabor != iCasteSystemCivic:
							iNumForeignReligions += 1
		elif iCivicReligion == iStateReligionCivic: 
			for pLoopCity in apCityList:
				if not pLoopCity.GetCy().isHasReligion(iStateReligion):
					iNumNonbelievingCities += 2
				for iLoopReligion in range(iNumReligions):
					if pLoopCity.GetCy().isHasReligion(iLoopReligion) and iLoopReligion != iStateReligion:
						iNumForeignReligions += 1
		elif (iCivicReligion == iMilitancyCivic) or (iCivicGovernment == iTheocracyCivic): 
			for pLoopCity in apCityList:
				if not pLoopCity.GetCy().isHasReligion(iStateReligion):
					iNumNonbelievingCities += 2
				for iLoopReligion in range(iNumReligions):
					if pLoopCity.GetCy().isHasReligion(iLoopReligion) and iLoopReligion != iStateReligion:
						iNumForeignReligions += 2
						
		#print ("iNumForeignReligions", iNumForeignReligions, "iNumNonbelievingCities", iNumNonbelievingCities, "iNumCities", iNumCities)
						
		if iNumNonbelievingCities *2 > iNumCities: iReligionRating -= 2
		elif iNumNonbelievingCities *4 > iNumCities: iReligionRating -= 1
		
		if iNumForeignReligions > iNumCities *2: iReligionRating -= 2
		elif iNumForeignReligions > iNumCities: iReligionRating -= 1
		
		#print ("iReligionRating=", iReligionRating)
		
		#print "TOTALS"
		#print ("Civics:", iCivicsRating, "Health & Happiness:", iHappinessAndHealthRating, "Economy:", iEconomyRating, "Empire:", iEmpireRating, "Religion:", iReligionRating)
		#print ("Total:", iCivicsRating + iHappinessAndHealthRating + iEconomyRating + iEmpireRating + iReligionRating)
		#iAdjustment = 3
		#print ("iAdjustment=", iAdjustment)
		
		iStability = iCivicsRating + iHappinessAndHealthRating + iEconomyRating + iEmpireRating + iReligionRating + iAdjustment
		if iPlayer == iByzantines: iStability += 3 # Byzantine UP
		if iGameTurn > getTurnForYear(tFall[iCiv]): iStability -= 3
		
		### RESULTS ###
		

		if pTeam.isHasTech(iStabilityCollapsing):
			if iStability < -3:
				if iGameTurn > getTurnForYear(tFall[iCiv]):
					#print "RESULT"
					#print ("already collapsing, terminal crisis, iCiv=", iCiv)
					self.terminalCrisis(iPlayer, iCiv, pPlayer, pTeam)
					return
				else:
					#print "RESULT"
					#print ("already collapsing, severe crisis, iCiv=", iCiv)
					self.severeCrisis(iPlayer, iCiv, pPlayer, pTeam)
					return
			elif iStability < 3:
				#print "RESULT"
				#print ("stability flat at collapsing, moderate crisis, iCiv=", iCiv)
				self.moderateCrisis(iPlayer, iCiv, pPlayer, pTeam)
			elif iStability > 3:
				#print "RESULT"
				#print ("upgrade from collapsing to unstable, iCiv=", iCiv)
				pTeam.setHasTech(iStabilityCollapsing, False, iPlayer, False, False)
				pTeam.setHasTech(iStabilityUnstable, True, iPlayer, False, False)
				return
				
		elif pTeam.isHasTech(iStabilityUnstable):
			if iStability < -6:
				if iGameTurn > getTurnForYear(tFall[iCiv]):
					#print "RESULT"
					#print ("downgrade from unstable to collapsing, severe crisis, iCiv=", iCiv)
					pTeam.setHasTech(iStabilityUnstable, False, iPlayer, False, False)
					pTeam.setHasTech(iStabilityCollapsing, True, iPlayer, False, False)
					self.severeCrisis(iPlayer, iCiv, pPlayer, pTeam)
					return
				else:
					#print "RESULT"
					#print ("downgrade from unstable to collapsing, moderate crisis, iCiv=", iCiv)
					pTeam.setHasTech(iStabilityUnstable, False, iPlayer, False, False)
					pTeam.setHasTech(iStabilityCollapsing, True, iPlayer, False, False)
					self.moderateCrisis(iPlayer, iCiv, pPlayer, pTeam)
					return
			elif iStability <= 0:
				#print "RESULT"
				#print ("stability flat at unstable, minor crisis, iCiv=", iCiv)
				self.minorCrisis(iPlayer, iCiv, pPlayer, pTeam)
				return
			else:
				#print "RESULT"
				#print ("stability upgrade from unstable to stable, no crisis, iCiv=", iCiv)
				pTeam.setHasTech(iStabilityUnstable, False, iPlayer, False, False)
				pTeam.setHasTech(iStabilityStable, True, iPlayer, False, False)
				return
		else:
			if iStability < -6:
				#print "RESULT"
				#print ("downgrade from stable to unstable, minor crisis, iCiv=", iCiv)
				pTeam.setHasTech(iStabilityStable, False, iPlayer, False, False)
				pTeam.setHasTech(iStabilityUnstable, True, iPlayer, False, False)
				self.minorCrisis(iPlayer, iCiv, pPlayer, pTeam)
				return
			elif iStability < -3:
				#print "RESULT"
				#print ("downgrade from stable to unstable, no crisis, iCiv=", iCiv)
				pTeam.setHasTech(iStabilityStable, False, iPlayer, False, False)
				pTeam.setHasTech(iStabilityUnstable, True, iPlayer, False, False)
				return
			#elif iStability >= 0: print ("stability flat at stable, no crisis, iCiv=", iCiv)