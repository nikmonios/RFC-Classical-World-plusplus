## Sid Meier's Civilization 4
## Copyright Firaxis Games 2005
from CvPythonExtensions import *
import PyHelpers
import CvUtil
import ScreenInput
import CvScreenEnums
from StoredData import sd # srpt

# < Mercenaries Start >
import MercenaryUtils
# < Mercenaries End   >

from RFCUtils import utils # edead
import Consts as con # srpt

# globals
gc = CyGlobalContext()
ArtFileMgr = CyArtFileMgr()
localText = CyTranslator()
PyPlayer = PyHelpers.PyPlayer

# < Mercenaries Start >
objMercenaryUtils = MercenaryUtils.MercenaryUtils()
# < Mercenaries End >

class CvFinanceAdvisor:

	def __init__(self):
		self.SCREEN_NAME = "FinanceAdvisor"
		self.DEBUG_DROPDOWN_ID =  "FinanceAdvisorDropdownWidget"
		self.WIDGET_ID = "FinanceAdvisorWidget"
		self.WIDGET_HEADER = "FinanceAdvisorWidgetHeader"
		self.EXIT_ID = "FinanceAdvisorExitWidget"
		self.BACKGROUND_ID = "FinanceAdvisorBackground"
		self.X_SCREEN = 500
		self.Y_SCREEN = 396
		self.W_SCREEN = 1024
		self.H_SCREEN = 768
		self.Y_TITLE = 12
		self.BORDER_WIDTH = 4
		self.PANE_HEIGHT = 340 #450 #Rhye
		self.PANE_WIDTH = 283
		self.X_SLIDERS = 50
		self.X_INCOME = 373
		self.X_EXPENSES = 696
		self.Y_TREASURY = 60 #90 #Rhye
		self.H_TREASURY = 60 #100 #Rhye
		self.Y_LOCATION = 130 #230 #Rhye
		self.Y_SPACING = 30
		self.TEXT_MARGIN = 15
		self.Z_BACKGROUND = -2.1
		self.Z_CONTROLS = self.Z_BACKGROUND - 0.2
		self.DZ = -0.2
		self.X_EXIT = 994
		self.Y_EXIT = 726
		self.Y_STABILITY = 480 #Rhye
		self.Y_PARAMETERS = 550 #Rhye
		self.H_PARAMETERS = 140 #Rhye
		self.PARAMETERS_WIDTH = 170 #Rhye
		self.X_PARAMETERS1 = self.X_SLIDERS #Rhye
		self.X_PARAMETERS2 = self.X_PARAMETERS1 + self.PARAMETERS_WIDTH + 20 #Rhye
		self.X_PARAMETERS3 = self.X_PARAMETERS2 + self.PARAMETERS_WIDTH + 20 #Rhye
		self.X_PARAMETERS4 = self.X_PARAMETERS3 + self.PARAMETERS_WIDTH + 20 #Rhye
		self.X_PARAMETERS5 = self.X_PARAMETERS4 + self.PARAMETERS_WIDTH + 20 #Rhye
		
		
		self.nWidgetCount = 0

	def getScreen(self):
		return CyGInterfaceScreen(self.SCREEN_NAME, CvScreenEnums.FINANCE_ADVISOR)

	def interfaceScreen (self):

		self.iActiveLeader = CyGame().getActivePlayer()

		player = gc.getPlayer(self.iActiveLeader)
	
		screen = self.getScreen()
		if screen.isActive():
			return
		screen.setRenderInterfaceOnly(True);
		screen.showScreen( PopupStates.POPUPSTATE_IMMEDIATE, False)
	
		# Set the background and exit button, and show the screen
		screen.setDimensions(screen.centerX(0), screen.centerY(0), self.W_SCREEN, self.H_SCREEN)

		screen.addDDSGFC(self.BACKGROUND_ID, ArtFileMgr.getInterfaceArtInfo("MAINMENU_SLIDESHOW_LOAD").getPath(), 0, 0, self.W_SCREEN, self.H_SCREEN, WidgetTypes.WIDGET_GENERAL, -1, -1 )
		screen.addPanel( "TechTopPanel", u"", u"", True, False, 0, 0, self.W_SCREEN, 55, PanelStyles.PANEL_STYLE_TOPBAR )
		screen.addPanel( "TechBottomPanel", u"", u"", True, False, 0, 713, self.W_SCREEN, 55, PanelStyles.PANEL_STYLE_BOTTOMBAR )

		screen.showWindowBackground(False)
		screen.setText(self.EXIT_ID, "Background", u"<font=4>" + localText.getText("TXT_KEY_PEDIA_SCREEN_EXIT", ()).upper() + "</font>", CvUtil.FONT_RIGHT_JUSTIFY, self.X_EXIT, self.Y_EXIT, self.Z_CONTROLS, FontTypes.TITLE_FONT, WidgetTypes.WIDGET_CLOSE_SCREEN, -1, -1 )

		# Header...
		screen.setLabel(self.WIDGET_HEADER, "Background", u"<font=4b>" + localText.getText("TXT_KEY_FINANCIAL_ADVISOR_TITLE", ()).upper() + u"</font>", CvUtil.FONT_CENTER_JUSTIFY, self.X_SCREEN, self.Y_TITLE, self.Z_CONTROLS, FontTypes.TITLE_FONT, WidgetTypes.WIDGET_GENERAL, -1, -1)
				
		if (CyGame().isDebugMode()):
			self.szDropdownName = self.DEBUG_DROPDOWN_ID
			screen.addDropDownBoxGFC(self.szDropdownName, 22, 12, 300, WidgetTypes.WIDGET_GENERAL, -1, -1, FontTypes.GAME_FONT)
			for j in range(gc.getMAX_PLAYERS()):
				if (gc.getPlayer(j).isAlive()):
					screen.addPullDownString(self.szDropdownName, gc.getPlayer(j).getName(), j, j, False )

		# draw the contents
		self.drawContents()

	def drawContents(self):
		
		self.deleteAllWidgets()

		# Create a new screen, called FinanceAdvisor, using the file FinanceAdvisor.py for input
		screen = self.getScreen()
	
		player = gc.getPlayer(self.iActiveLeader)

		ePlayer = self.iActiveLeader #Rhye
		#Rhye - start ## srpt stability conversion
		## srpt stability conversion replaced below
		#Rhye - end
		
		pTeam = gc.getTeam(gc.getPlayer(utils.getHumanID()).getTeam())
		
		if pTeam.isHasTech(con.iStabilityStable):
			szTempBuffer = localText.getText("TXT_KEY_STABILITY_STABLE", ())
		elif pTeam.isHasTech(con.iStabilityUnstable):
			szTempBuffer = localText.getText("TXT_KEY_STABILITY_UNSTABLE", ())
		elif pTeam.isHasTech(con.iStabilityCollapsing):
			szTempBuffer = localText.getText("TXT_KEY_STABILITY_COLLAPSING", ())
			
		## srpt stability conversion end
	
		numCities = player.getNumCities()	
					
		totalUnitCost = player.calculateUnitCost()
		totalUnitSupply = player.calculateUnitSupply()
		totalMaintenance = player.getTotalMaintenance()
		totalCivicUpkeep = player.getCivicUpkeep([], False)
		totalPreInflatedCosts = player.calculatePreInflatedCosts()
		totalInflatedCosts = player.calculateInflatedCosts()
		goldCommerce = player.getCommerceRate(CommerceTypes.COMMERCE_GOLD)
		if (not player.isCommerceFlexible(CommerceTypes.COMMERCE_RESEARCH)):
			goldCommerce += player.calculateBaseNetResearch()
		gold = player.getGold()
		goldFromCivs = player.getGoldPerTurn()
		
		# < Mercenaries Start >
		totalMercenaryMaintenanceCost = objMercenaryUtils.getPlayerMercenaryMaintenanceCost(self.iActiveLeader)
		# totalMercenaryContractIncome = objMercenaryUtils.getPlayerMercenaryContractIncome(self.iActiveLeader)
		# < Mercenaries End   >

		szTreasuryPanel = self.getNextWidgetName()
		screen.addPanel(szTreasuryPanel, u"", "", True, True, self.X_SLIDERS, self.Y_TREASURY, self.X_EXPENSES + self.PANE_WIDTH - self.X_SLIDERS, self.H_TREASURY, PanelStyles.PANEL_STYLE_MAIN )
		screen.setLabel(self.getNextWidgetName(), szTreasuryPanel, u"<font=4>" + localText.getText("TXT_KEY_FINANCIAL_ADVISOR_TREASURY", (gold, )).upper() + u"</font>", CvUtil.FONT_CENTER_JUSTIFY, (self.X_SLIDERS + self.PANE_WIDTH + self.X_EXPENSES)/2, self.Y_TREASURY + self.H_TREASURY/2 - self.Y_SPACING/2, self.Z_CONTROLS, FontTypes.TITLE_FONT, WidgetTypes.WIDGET_HELP_FINANCE_GOLD_RESERVE, -1, -1 )

		szCommercePanel = self.getNextWidgetName()
		screen.addPanel(szCommercePanel, u"", "", True, True, self.X_SLIDERS, self.Y_LOCATION, self.PANE_WIDTH, self.PANE_HEIGHT, PanelStyles.PANEL_STYLE_MAIN )
		screen.setLabel(self.getNextWidgetName(), "Background",  u"<font=3>" + localText.getText("TXT_KEY_CONCEPT_COMMERCE", ()).upper() + u"</font>", CvUtil.FONT_CENTER_JUSTIFY, self.X_SLIDERS + self.PANE_WIDTH/2, self.Y_LOCATION + self.TEXT_MARGIN, self.Z_CONTROLS + self.DZ, FontTypes.GAME_FONT, WidgetTypes.WIDGET_GENERAL, -1, -1 )
				
		szIncomePanel = self.getNextWidgetName()
		screen.addPanel(szIncomePanel, u"", "", True, True, self.X_INCOME, self.Y_LOCATION, self.PANE_WIDTH, self.PANE_HEIGHT, PanelStyles.PANEL_STYLE_MAIN )
		screen.setLabel(self.getNextWidgetName(), "Background",  u"<font=3>" + localText.getText("TXT_KEY_FINANCIAL_ADVISOR_INCOME_HEADER", ()).upper() + u"</font>", CvUtil.FONT_CENTER_JUSTIFY, self.X_INCOME + self.PANE_WIDTH/2, self.Y_LOCATION + self.TEXT_MARGIN, self.Z_CONTROLS + self.DZ, FontTypes.GAME_FONT, WidgetTypes.WIDGET_GENERAL, -1, -1 )
		
		szExpensePanel = self.getNextWidgetName()
		screen.addPanel(szExpensePanel, u"", "", True, True, self.X_EXPENSES, self.Y_LOCATION, self.PANE_WIDTH, self.PANE_HEIGHT, PanelStyles.PANEL_STYLE_MAIN )
		screen.setLabel(self.getNextWidgetName(), "Background",  u"<font=3>" + localText.getText("TXT_KEY_FINANCIAL_ADVISOR_EXPENSES_HEADER", ()).upper() + u"</font>", CvUtil.FONT_CENTER_JUSTIFY, self.X_EXPENSES + self.PANE_WIDTH/2, self.Y_LOCATION + self.TEXT_MARGIN, self.Z_CONTROLS + self.DZ, FontTypes.GAME_FONT, WidgetTypes.WIDGET_GENERAL, -1, -1 )

		#Rhye - start
		iHuman = utils.getHumanID()
		pPlayer = gc.getPlayer(iHuman)
		apCityList = PyPlayer(utils.getHumanID()).getCityList()
		iNumCities = pPlayer.getNumCities()
		if iNumCities < 1: iNumCities =1
		iCivicGovernment = pPlayer.getCivics(0)
		iCivicLegal = pPlayer.getCivics(1)
		iCivicLabor = pPlayer.getCivics(2)
		iCivicReligion = pPlayer.getCivics(4)
		iStateReligion = pPlayer.getStateReligion()
		
		szStabilityPanel = self.getNextWidgetName()
		screen.addPanel(szStabilityPanel, u"", "", True, True, self.X_SLIDERS, self.Y_STABILITY, self.X_EXPENSES + self.PANE_WIDTH - self.X_SLIDERS, self.H_TREASURY, PanelStyles.PANEL_STYLE_MAIN )
		screen.setLabel(self.getNextWidgetName(), szStabilityPanel, u"<font=4>" + localText.getText("TXT_KEY_STABILITY_ADVISOR_TITLE", ()).upper() + " " + szTempBuffer + u"</font>", CvUtil.FONT_CENTER_JUSTIFY, (self.X_SLIDERS + self.PANE_WIDTH + self.X_EXPENSES)/2, self.Y_STABILITY + self.H_TREASURY/2 - self.Y_SPACING/2, self.Z_CONTROLS, FontTypes.TITLE_FONT, WidgetTypes.WIDGET_GENERAL, -1, -1 )

		szParametersPanel1 = self.getNextWidgetName()
		screen.addPanel(szParametersPanel1, u"", "", True, True, self.X_PARAMETERS1, self.Y_PARAMETERS, self.PARAMETERS_WIDTH, self.H_PARAMETERS, PanelStyles.PANEL_STYLE_MAIN )
		screen.setLabel(self.getNextWidgetName(), "Background",  u"<font=3>" + localText.getText("TXT_KEY_STABILITY_CIVICS", ()) + u"</font>", CvUtil.FONT_CENTER_JUSTIFY, self.X_PARAMETERS1 + self.PARAMETERS_WIDTH/2, self.Y_PARAMETERS + self.TEXT_MARGIN, self.Z_CONTROLS + self.DZ, FontTypes.GAME_FONT, WidgetTypes.WIDGET_GENERAL, -1, -1 )
		
		## srpt stability data ##
		
		## Civics calculation
		iCivicsRating = sd.getCivicsStability(iHuman)
		
		self.printNumber(ePlayer, self.getNextWidgetName(), iCivicsRating, self.X_PARAMETERS1 + self.PARAMETERS_WIDTH/2, self.Y_PARAMETERS + self.TEXT_MARGIN + 60, self.Z_CONTROLS + self.DZ)
		
		szParametersPanel2 = self.getNextWidgetName()
		screen.addPanel(szParametersPanel2, u"", "", True, True, self.X_PARAMETERS2, self.Y_PARAMETERS, self.PARAMETERS_WIDTH, self.H_PARAMETERS, PanelStyles.PANEL_STYLE_MAIN )
		screen.setLabel(self.getNextWidgetName(), "Background",  u"<font=3>" + localText.getText("TXT_KEY_STABILITY_HH", ()) + u"</font>", CvUtil.FONT_CENTER_JUSTIFY, self.X_PARAMETERS2 + self.PARAMETERS_WIDTH/2, self.Y_PARAMETERS + self.TEXT_MARGIN, self.Z_CONTROLS + self.DZ, FontTypes.GAME_FONT, WidgetTypes.WIDGET_GENERAL, -1, -1 )
		
		## H & H calculation
		iHappinessAndHealthRating = 0
		iHappiness = ((pPlayer.calculateTotalCityHappiness()) - (pPlayer.calculateTotalCityUnhappiness())) / (iNumCities)
		iHealth = ((pPlayer.calculateTotalCityHealthiness()) - (pPlayer.calculateTotalCityUnhealthiness())) / (iNumCities)
		if iHappiness < 0: iHappinessAndHealthRating -= 1
		elif iHappiness > 3: iHappinessAndHealthRating += 1
		if iHealth < 0: iHappinessAndHealthRating -= 1
		elif iHealth > 3: iHappinessAndHealthRating += 1
		for pLoopCity in apCityList:
			if (pLoopCity.GetCy().angryPopulation(0) > 0): 
				iHappinessAndHealthRating -= 1
		self.printNumber(ePlayer, self.getNextWidgetName(), iHappinessAndHealthRating, self.X_PARAMETERS2 + self.PARAMETERS_WIDTH/2, self.Y_PARAMETERS + self.TEXT_MARGIN + 60, self.Z_CONTROLS + self.DZ)
		
		szParametersPanel3 = self.getNextWidgetName()
		screen.addPanel(szParametersPanel3, u"", "", True, True, self.X_PARAMETERS3, self.Y_PARAMETERS, self.PARAMETERS_WIDTH, self.H_PARAMETERS, PanelStyles.PANEL_STYLE_MAIN )
		screen.setLabel(self.getNextWidgetName(), "Background",  u"<font=3>" + localText.getText("TXT_KEY_STABILITY_ECONOMY", ()) + u"</font>", CvUtil.FONT_CENTER_JUSTIFY, self.X_PARAMETERS3 + self.PARAMETERS_WIDTH/2, self.Y_PARAMETERS + self.TEXT_MARGIN, self.Z_CONTROLS + self.DZ, FontTypes.GAME_FONT, WidgetTypes.WIDGET_GENERAL, -1, -1 )
		
		## Economy calculation
		iEconomyRating = 0
		#if pPlayer.getGold() < 300:
		iRate = (pPlayer.calculateGoldRate() + pPlayer.calculateBaseNetResearch()) - (pPlayer.calculateInflatedCosts())
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
			
			
		if iGrowth * 2 < sd.getOldEconomyRating(iHuman): 
			iEconomyRating -= 3 
			#print "high economic decline"
		elif iGrowth * 4 < sd.getOldEconomyRating(iHuman) * 3: 
			iEconomyRating -= 2 
			#print "med economic decline"
		elif iGrowth < sd.getOldEconomyRating(iHuman): 
			iEconomyRating -= 1
			#print "some economic decline"
			
		self.printNumber(ePlayer, self.getNextWidgetName(), iEconomyRating, self.X_PARAMETERS3 + self.PARAMETERS_WIDTH/2, self.Y_PARAMETERS + self.TEXT_MARGIN + 60, self.Z_CONTROLS + self.DZ)
		
		szParametersPanel4 = self.getNextWidgetName()
		screen.addPanel(szParametersPanel4, u"", "", True, True, self.X_PARAMETERS4, self.Y_PARAMETERS, self.PARAMETERS_WIDTH, self.H_PARAMETERS, PanelStyles.PANEL_STYLE_MAIN )
		screen.setLabel(self.getNextWidgetName(), "Background",  u"<font=3>" + localText.getText("TXT_KEY_STABILITY_EMPIRE", ()) + u"</font>", CvUtil.FONT_CENTER_JUSTIFY, self.X_PARAMETERS4 + self.PARAMETERS_WIDTH/2, self.Y_PARAMETERS + self.TEXT_MARGIN, self.Z_CONTROLS + self.DZ, FontTypes.GAME_FONT, WidgetTypes.WIDGET_GENERAL, -1, -1 )
		
		## Empire calculation
		iEmpireRating = 0
		for regionID in utils.getCoreRegions(iHuman):
			if not (utils.checkRegionControl(iHuman, regionID)): 
				iEmpireRating -= 3
		iCorePop = 0
		iEmpirePop = 0
		for pLoopCity in apCityList:
			if pLoopCity.GetCy().isCapital():
				iCorePop += pLoopCity.getPopulation() * 3
			else:
				regionID = gc.getMap().plot(pLoopCity.GetCy().getX(),pLoopCity.GetCy().getY()).getRegionID()
				if regionID in utils.getCoreRegions(iHuman) or regionID in utils.getSpecialRegions(iHuman): 
					iCorePop += pLoopCity.getPopulation() * 2
				elif regionID in utils.getNormalRegions(iHuman):
					iFactor = 1
					if not ((iCivicGovernment == con.iTheocracyCivic) and (pLoopCity.GetCy().isHasReligion(iStateReligion))):
						if iCivicGovernment != con.iEmpireCivic: iFactor += 1
					if not (iCivicLegal == con.iBureaucracyCivic):
						iFactor += 1
					if not (pLoopCity.GetCy().getNumRealBuilding(con.iCourthouse) > 0):
						iFactor += 1
					iEmpirePop += pLoopCity.getPopulation() * iFactor
				else:
					iFactor = 2
					if not ((iCivicGovernment == con.iTheocracyCivic) and (pLoopCity.GetCy().isHasReligion(iStateReligion))):
						if iCivicGovernment != con.iEmpireCivic: iFactor += 1
					if not (iCivicLegal == con.iBureaucracyCivic):
						iFactor += 1
					if not (pLoopCity.GetCy().getNumRealBuilding(con.iCourthouse) > 0):
						iFactor += 1
					iEmpirePop += pLoopCity.getPopulation() * iFactor
					
		if iCorePop > iEmpirePop *2: iEmpireRating += 2
		elif iCorePop > iEmpirePop: iEmpireRating += 1
		elif iCorePop *5 < iEmpirePop: iEmpireRating -= 5
		elif iCorePop *4 < iEmpirePop: iEmpireRating -= 4
		elif iCorePop *3 < iEmpirePop: iEmpireRating -= 3
		elif iCorePop *2 < iEmpirePop: iEmpireRating -= 2
		elif iCorePop < iEmpirePop: iEmpireRating -= 1
				
		if (pPlayer.getNumCities()) * 2 < (sd.getNumCities(iHuman)): 
			iEmpireRating -= 6
		elif (pPlayer.getNumCities()) * 3 < (sd.getNumCities(iHuman)) * 2: 
			iEmpireRating -= 3
		elif pPlayer.getNumCities() < sd.getNumCities(iHuman): 
			iEmpireRating -= 1
		
		self.printNumber(ePlayer, self.getNextWidgetName(), iEmpireRating, self.X_PARAMETERS4 + self.PARAMETERS_WIDTH/2, self.Y_PARAMETERS + self.TEXT_MARGIN + 60, self.Z_CONTROLS + self.DZ)
		
		szParametersPanel5 = self.getNextWidgetName()
		screen.addPanel(szParametersPanel5, u"", "", True, True, self.X_PARAMETERS5, self.Y_PARAMETERS, self.PARAMETERS_WIDTH, self.H_PARAMETERS, PanelStyles.PANEL_STYLE_MAIN )
		screen.setLabel(self.getNextWidgetName(), "Background",  u"<font=3>" + localText.getText("TXT_KEY_STABILITY_RELIGION", ()) + u"</font>", CvUtil.FONT_CENTER_JUSTIFY, self.X_PARAMETERS5 + self.PARAMETERS_WIDTH/2, self.Y_PARAMETERS + self.TEXT_MARGIN, self.Z_CONTROLS + self.DZ, FontTypes.GAME_FONT, WidgetTypes.WIDGET_GENERAL, -1, -1 )
		
		
		## Religion calculation
		iReligionRating = 0
		iNumForeignReligions = 0
		iNumNonbelievingCities = 0
		if (iCivicReligion == con.iDynasticCultCivic) or (iCivicReligion == con.iPaganismCivic): 
			for pLoopCity in apCityList:
				for iLoopReligion in range(con.iNumReligions):
					if pLoopCity.GetCy().isHasReligion(iLoopReligion):
						if iLoopReligion != con.iHinduism: 
							iNumForeignReligions += 1
						elif iLoopReligion == con.iHinduism and iCivicLabor != con.iCasteSystemCivic:
							iNumForeignReligions += 1
		elif iCivicReligion == con.iStateReligionCivic: 
			for pLoopCity in apCityList:
				if not pLoopCity.GetCy().isHasReligion(iStateReligion):
					iNumNonbelievingCities += 2
				for iLoopReligion in range(con.iNumReligions):
					if pLoopCity.GetCy().isHasReligion(iLoopReligion) and iLoopReligion != iStateReligion:
						iNumForeignReligions += 1
		elif (iCivicReligion == con.iMilitancyCivic) or (iCivicGovernment == con.iTheocracyCivic): 
			for pLoopCity in apCityList:
				if not pLoopCity.GetCy().isHasReligion(iStateReligion):
					iNumNonbelievingCities += 2
				for iLoopReligion in range(con.iNumReligions):
					if pLoopCity.GetCy().isHasReligion(iLoopReligion) and iLoopReligion != iStateReligion:
						iNumForeignReligions += 2
		
		#if sd.getPiety(iHuman) > 70: iReligionRating += 2
		#elif sd.getPiety(iHuman) > 40: iReligionRating += 1
		#elif sd.getPiety(iHuman) < 30: iReligionRating -= 1
		self.printNumber(ePlayer, self.getNextWidgetName(), iReligionRating, self.X_PARAMETERS5 + self.PARAMETERS_WIDTH/2, self.Y_PARAMETERS + self.TEXT_MARGIN + 60, self.Z_CONTROLS + self.DZ)

		 ## srpt stability conversion
		#Rhye - end		

		
		# Slider percentages
		yLocation  = self.Y_LOCATION
	
		yLocation += 0.5 * self.Y_SPACING
		for iI in range(CommerceTypes.NUM_COMMERCE_TYPES):
			eCommerce = (iI + 1) % CommerceTypes.NUM_COMMERCE_TYPES

			if (player.isCommerceFlexible(eCommerce)):
				yLocation += self.Y_SPACING
				screen.setButtonGFC(self.getNextWidgetName(), u"", "", self.X_SLIDERS + self.TEXT_MARGIN, int(yLocation) + self.TEXT_MARGIN, 20, 20, WidgetTypes.WIDGET_CHANGE_PERCENT, eCommerce, gc.getDefineINT("COMMERCE_PERCENT_CHANGE_INCREMENTS"), ButtonStyles.BUTTON_STYLE_CITY_PLUS )
				screen.setButtonGFC(self.getNextWidgetName(), u"", "", self.X_SLIDERS + self.TEXT_MARGIN + 24, int(yLocation) + self.TEXT_MARGIN, 20, 20, WidgetTypes.WIDGET_CHANGE_PERCENT, eCommerce, -gc.getDefineINT("COMMERCE_PERCENT_CHANGE_INCREMENTS"), ButtonStyles.BUTTON_STYLE_CITY_MINUS )

				szText = u"<font=3>" + gc.getCommerceInfo(eCommerce).getDescription() + u" (" + unicode(player.getCommercePercent(eCommerce)) + u"%)</font>"
				screen.setLabel(self.getNextWidgetName(), "Background",  szText, CvUtil.FONT_LEFT_JUSTIFY, self.X_SLIDERS + self.TEXT_MARGIN + 50, yLocation + self.TEXT_MARGIN, self.Z_CONTROLS + self.DZ, FontTypes.GAME_FONT, WidgetTypes.WIDGET_GENERAL, -1, -1 )
				szRate = u"<font=3>" + unicode(player.getCommerceRate(CommerceTypes(eCommerce))) + u"</font>"
				screen.setLabel(self.getNextWidgetName(), "Background", szRate, CvUtil.FONT_RIGHT_JUSTIFY, self.X_SLIDERS + self.PANE_WIDTH - self.TEXT_MARGIN, yLocation + self.TEXT_MARGIN, self.Z_CONTROLS + self.DZ, FontTypes.GAME_FONT, WidgetTypes.WIDGET_GENERAL, -1, -1)


		yLocation += self.Y_SPACING
		szText = u"<font=3>" + gc.getCommerceInfo(CommerceTypes.COMMERCE_GOLD).getDescription() + u" (" + unicode(player.getCommercePercent(CommerceTypes.COMMERCE_GOLD)) + u"%)</font>"
		screen.setLabel(self.getNextWidgetName(), "Background",  szText, CvUtil.FONT_LEFT_JUSTIFY, self.X_SLIDERS + self.TEXT_MARGIN + 50, yLocation + self.TEXT_MARGIN, self.Z_CONTROLS + self.DZ, FontTypes.GAME_FONT, WidgetTypes.WIDGET_GENERAL, -1, -1 )
		szCommerce = u"<font=3>" + unicode(goldCommerce) + u"</font>"
		screen.setLabel(self.getNextWidgetName(), "Background", szCommerce, CvUtil.FONT_RIGHT_JUSTIFY, self.X_SLIDERS + self.PANE_WIDTH - self.TEXT_MARGIN, yLocation + self.TEXT_MARGIN, self.Z_CONTROLS + self.DZ, FontTypes.GAME_FONT, WidgetTypes.WIDGET_GENERAL, -1, -1)

		# Income
		yLocation  = self.Y_LOCATION
		iIncome = 0

		yLocation += 1.5 * self.Y_SPACING
		screen.setLabel(self.getNextWidgetName(), "Background", u"<font=3>" + localText.getText("TXT_KEY_FINANCIAL_ADVISOR_TAXES", ()) + "</font>", CvUtil.FONT_LEFT_JUSTIFY, self.X_INCOME + self.TEXT_MARGIN, yLocation + self.TEXT_MARGIN, self.Z_CONTROLS + self.DZ, FontTypes.GAME_FONT, WidgetTypes.WIDGET_HELP_FINANCE_GROSS_INCOME, -1, -1 )
		screen.setLabel(self.getNextWidgetName(), "Background", u"<font=3>" + unicode(goldCommerce) + "</font>", CvUtil.FONT_RIGHT_JUSTIFY, self.X_INCOME + self.PANE_WIDTH - self.TEXT_MARGIN, yLocation + self.TEXT_MARGIN, self.Z_CONTROLS + self.DZ, FontTypes.GAME_FONT, WidgetTypes.WIDGET_HELP_FINANCE_GROSS_INCOME, -1, -1 )
		iIncome += goldCommerce

		# < Mercenaries Start >
		# yLocation += 1.5 * self.Y_SPACING
		# screen.setLabel(self.getNextWidgetName(), "Background", u"<font=3>" + localText.getText("TXT_KEY_FINANCIAL_ADVISOR_MERCENARY_CONTRACT_INCOME", ()) + "</font>", CvUtil.FONT_LEFT_JUSTIFY, self.X_INCOME + self.TEXT_MARGIN, yLocation + self.TEXT_MARGIN, self.Z_CONTROLS + self.DZ, FontTypes.GAME_FONT, WidgetTypes.WIDGET_GENERAL, -1, -1 )
		# screen.setLabel(self.getNextWidgetName(), "Background", u"<font=3>" + unicode(totalMercenaryContractIncome) + "</font>", CvUtil.FONT_RIGHT_JUSTIFY, self.X_INCOME + self.PANE_WIDTH - self.TEXT_MARGIN, yLocation + self.TEXT_MARGIN, self.Z_CONTROLS + self.DZ, FontTypes.GAME_FONT, WidgetTypes.WIDGET_GENERAL, -1, -1 )
		# iIncome += totalMercenaryContractIncome
		# < Mercenaries End   >

		if (goldFromCivs > 0):
			yLocation += self.Y_SPACING
			szText = unicode(goldFromCivs) + " : " + localText.getText("TXT_KEY_FINANCIAL_ADVISOR_PER_TURN", ())
			screen.setLabel(self.getNextWidgetName(), "Background", u"<font=3>" + localText.getText("TXT_KEY_FINANCIAL_ADVISOR_PER_TURN", ()) + "</font>", CvUtil.FONT_LEFT_JUSTIFY, self.X_INCOME + self.TEXT_MARGIN, yLocation + self.TEXT_MARGIN, self.Z_CONTROLS + self.DZ, FontTypes.GAME_FONT, WidgetTypes.WIDGET_HELP_FINANCE_FOREIGN_INCOME, self.iActiveLeader, 1)
			screen.setLabel(self.getNextWidgetName(), "Background", u"<font=3>" + unicode(goldFromCivs) + "</font>", CvUtil.FONT_RIGHT_JUSTIFY, self.X_INCOME + self.PANE_WIDTH - self.TEXT_MARGIN, yLocation + self.TEXT_MARGIN, self.Z_CONTROLS + self.DZ, FontTypes.GAME_FONT, WidgetTypes.WIDGET_HELP_FINANCE_FOREIGN_INCOME, self.iActiveLeader, 1)
			iIncome += goldFromCivs

		yLocation += 1.5 * self.Y_SPACING
		screen.setLabel(self.getNextWidgetName(), "Background", u"<font=3>" + localText.getText("TXT_KEY_FINANCIAL_ADVISOR_INCOME", ()) + "</font>", CvUtil.FONT_LEFT_JUSTIFY, self.X_INCOME + self.TEXT_MARGIN, yLocation + self.TEXT_MARGIN, self.Z_CONTROLS + self.DZ, FontTypes.GAME_FONT, WidgetTypes.WIDGET_GENERAL, -1, -1 )
		screen.setLabel(self.getNextWidgetName(), "Background", u"<font=3>" + unicode(iIncome) + "</font>", CvUtil.FONT_RIGHT_JUSTIFY, self.X_INCOME + self.PANE_WIDTH - self.TEXT_MARGIN, yLocation + self.TEXT_MARGIN, self.Z_CONTROLS + self.DZ, FontTypes.GAME_FONT, WidgetTypes.WIDGET_GENERAL, -1, -1 )
		iIncome += goldFromCivs


		# Expenses
		yLocation = self.Y_LOCATION
		iExpenses = 0

		yLocation += 1.5 * self.Y_SPACING
		screen.setLabel(self.getNextWidgetName(), "Background", u"<font=3>" + localText.getText("TXT_KEY_FINANCIAL_ADVISOR_UNITCOST", ()) + u"</font>", CvUtil.FONT_LEFT_JUSTIFY, self.X_EXPENSES + self.TEXT_MARGIN, yLocation + self.TEXT_MARGIN, self.Z_CONTROLS + self.DZ, FontTypes.GAME_FONT, WidgetTypes.WIDGET_HELP_FINANCE_UNIT_COST, self.iActiveLeader, 1)
		screen.setLabel(self.getNextWidgetName(), "Background", u"<font=3>" + unicode(totalUnitCost) + u"</font>", CvUtil.FONT_RIGHT_JUSTIFY, self.X_EXPENSES + self.PANE_WIDTH - self.TEXT_MARGIN, yLocation + self.TEXT_MARGIN, self.Z_CONTROLS + self.DZ, FontTypes.GAME_FONT, WidgetTypes.WIDGET_HELP_FINANCE_UNIT_COST, self.iActiveLeader, 1)
		iExpenses += totalUnitCost

		yLocation += self.Y_SPACING
		screen.setLabel(self.getNextWidgetName(), "Background", u"<font=3>" + localText.getText("TXT_KEY_FINANCIAL_ADVISOR_UNITSUPPLY", ()) + "</font>", CvUtil.FONT_LEFT_JUSTIFY, self.X_EXPENSES + self.TEXT_MARGIN, yLocation + self.TEXT_MARGIN, self.Z_CONTROLS + self.DZ, FontTypes.GAME_FONT, WidgetTypes.WIDGET_HELP_FINANCE_AWAY_SUPPLY, self.iActiveLeader, 1)
		screen.setLabel(self.getNextWidgetName(), "Background", u"<font=3>" + unicode(totalUnitSupply) + "</font>", CvUtil.FONT_RIGHT_JUSTIFY, self.X_EXPENSES + self.PANE_WIDTH - self.TEXT_MARGIN, yLocation + self.TEXT_MARGIN, self.Z_CONTROLS + self.DZ, FontTypes.GAME_FONT, WidgetTypes.WIDGET_HELP_FINANCE_AWAY_SUPPLY, self.iActiveLeader, 1)
		iExpenses += totalUnitSupply

		# < Mercenaries Start >
		yLocation += self.Y_SPACING
		screen.setLabel(self.getNextWidgetName(), "Background", u"<font=3>" + localText.getText("TXT_KEY_FINANCIAL_ADVISOR_MERCENARY_MAINTENANCE_COST", ()) + "</font>", CvUtil.FONT_LEFT_JUSTIFY, self.X_EXPENSES + self.TEXT_MARGIN, yLocation + self.TEXT_MARGIN, self.Z_CONTROLS + self.DZ, FontTypes.GAME_FONT, WidgetTypes.WIDGET_GENERAL, self.iActiveLeader, 1)
		screen.setLabel(self.getNextWidgetName(), "Background", u"<font=3>" + unicode(totalMercenaryMaintenanceCost) + "</font>", CvUtil.FONT_RIGHT_JUSTIFY, self.X_EXPENSES + self.PANE_WIDTH - self.TEXT_MARGIN, yLocation + self.TEXT_MARGIN, self.Z_CONTROLS + self.DZ, FontTypes.GAME_FONT, WidgetTypes.WIDGET_GENERAL, self.iActiveLeader, 1)
		iExpenses += totalMercenaryMaintenanceCost
		# < Mercenaries End   >

		yLocation += self.Y_SPACING
		screen.setLabel(self.getNextWidgetName(), "Background", u"<font=3>" + localText.getText("TXT_KEY_FINANCIAL_ADVISOR_MAINTENANCE", ()) + "</font>", CvUtil.FONT_LEFT_JUSTIFY, self.X_EXPENSES + self.TEXT_MARGIN, yLocation + self.TEXT_MARGIN, self.Z_CONTROLS + self.DZ, FontTypes.GAME_FONT, WidgetTypes.WIDGET_HELP_FINANCE_CITY_MAINT, self.iActiveLeader, 1)
		screen.setLabel(self.getNextWidgetName(), "Background", u"<font=3>" + unicode(totalMaintenance) + "</font>", CvUtil.FONT_RIGHT_JUSTIFY, self.X_EXPENSES + self.PANE_WIDTH - self.TEXT_MARGIN, yLocation + self.TEXT_MARGIN, self.Z_CONTROLS + self.DZ, FontTypes.GAME_FONT, WidgetTypes.WIDGET_HELP_FINANCE_CITY_MAINT, self.iActiveLeader, 1)
		iExpenses += totalMaintenance

		yLocation += self.Y_SPACING
		screen.setLabel(self.getNextWidgetName(), "Background", u"<font=3>" + localText.getText("TXT_KEY_FINANCIAL_ADVISOR_CIVICS", ()) + "</font>", CvUtil.FONT_LEFT_JUSTIFY, self.X_EXPENSES + self.TEXT_MARGIN, yLocation + self.TEXT_MARGIN, self.Z_CONTROLS + self.DZ, FontTypes.GAME_FONT, WidgetTypes.WIDGET_HELP_FINANCE_CIVIC_UPKEEP, self.iActiveLeader, 1)
		screen.setLabel(self.getNextWidgetName(), "Background", u"<font=3>" + unicode(totalCivicUpkeep) + "</font>", CvUtil.FONT_RIGHT_JUSTIFY, self.X_EXPENSES + self.PANE_WIDTH - self.TEXT_MARGIN, yLocation + self.TEXT_MARGIN, self.Z_CONTROLS + self.DZ, FontTypes.GAME_FONT, WidgetTypes.WIDGET_HELP_FINANCE_CIVIC_UPKEEP, self.iActiveLeader, 1)
		iExpenses += totalCivicUpkeep

		if (goldFromCivs < 0):
			yLocation += self.Y_SPACING
			screen.setLabel(self.getNextWidgetName(), "Background", u"<font=3>" + localText.getText("TXT_KEY_FINANCIAL_ADVISOR_COST_PER_TURN", ()) + "</font>", CvUtil.FONT_LEFT_JUSTIFY, self.X_EXPENSES + self.TEXT_MARGIN, yLocation + self.TEXT_MARGIN, self.Z_CONTROLS + self.DZ, FontTypes.GAME_FONT, WidgetTypes.WIDGET_HELP_FINANCE_FOREIGN_INCOME, self.iActiveLeader, 1)
			screen.setLabel(self.getNextWidgetName(), "Background", u"<font=3>" + unicode(-goldFromCivs) + "</font>", CvUtil.FONT_RIGHT_JUSTIFY, self.X_EXPENSES + self.PANE_WIDTH - self.TEXT_MARGIN, yLocation + self.TEXT_MARGIN, self.Z_CONTROLS + self.DZ, FontTypes.GAME_FONT, WidgetTypes.WIDGET_HELP_FINANCE_FOREIGN_INCOME, self.iActiveLeader, 1)
			iExpenses -= goldFromCivs

		yLocation += self.Y_SPACING
		iInflation = totalInflatedCosts - totalPreInflatedCosts
		screen.setLabel(self.getNextWidgetName(), "Background", u"<font=3>" + localText.getText("TXT_KEY_FINANCIAL_ADVISOR_INFLATION", ()) + "</font>", CvUtil.FONT_LEFT_JUSTIFY, self.X_EXPENSES + self.TEXT_MARGIN, yLocation + self.TEXT_MARGIN, self.Z_CONTROLS + self.DZ, FontTypes.GAME_FONT, WidgetTypes.WIDGET_HELP_FINANCE_INFLATED_COSTS, self.iActiveLeader, 1)
		screen.setLabel(self.getNextWidgetName(), "Background", u"<font=3>" + unicode(iInflation) + "</font>", CvUtil.FONT_RIGHT_JUSTIFY, self.X_EXPENSES + self.PANE_WIDTH - self.TEXT_MARGIN, yLocation + self.TEXT_MARGIN, self.Z_CONTROLS + self.DZ, FontTypes.GAME_FONT, WidgetTypes.WIDGET_HELP_FINANCE_INFLATED_COSTS, self.iActiveLeader, 1)
		iExpenses += iInflation

		yLocation += 1.5 * self.Y_SPACING
		screen.setLabel(self.getNextWidgetName(), "Background", u"<font=3>" + localText.getText("TXT_KEY_FINANCIAL_ADVISOR_EXPENSES", ()) + "</font>", CvUtil.FONT_LEFT_JUSTIFY, self.X_EXPENSES + self.TEXT_MARGIN, yLocation + self.TEXT_MARGIN, self.Z_CONTROLS + self.DZ, FontTypes.GAME_FONT, WidgetTypes.WIDGET_GENERAL, -1, -1 )
		screen.setLabel(self.getNextWidgetName(), "Background", u"<font=3>" + unicode(iExpenses) + "</font>", CvUtil.FONT_RIGHT_JUSTIFY, self.X_EXPENSES + self.PANE_WIDTH - self.TEXT_MARGIN, yLocation + self.TEXT_MARGIN, self.Z_CONTROLS + self.DZ, FontTypes.GAME_FONT, WidgetTypes.WIDGET_GENERAL, -1, -1 )

		return 0
		
	# returns a unique ID for a widget in this screen
	def getNextWidgetName(self):
		szName = self.WIDGET_ID + str(self.nWidgetCount)
		self.nWidgetCount += 1
		return szName

	def deleteAllWidgets(self):
		screen = self.getScreen()
		i = self.nWidgetCount - 1
		while (i >= 0):
			self.nWidgetCount = i
			screen.deleteWidget(self.getNextWidgetName())
			i -= 1

		self.nWidgetCount = 0
			
	# Will handle the input for this screen...
	def handleInput (self, inputClass):
		'Calls function mapped in FinanceAdvisorInputMap'
		if (inputClass.getNotifyCode() == NotifyCode.NOTIFY_LISTBOX_ITEM_SELECTED):
			screen = self.getScreen()
			iIndex = screen.getSelectedPullDownID(self.DEBUG_DROPDOWN_ID)
			self.iActiveLeader = screen.getPullDownData(self.DEBUG_DROPDOWN_ID, iIndex)
			self.drawContents()
		return 0

	def update(self, fDelta):
		if (CyInterface().isDirty(InterfaceDirtyBits.Financial_Screen_DIRTY_BIT) == True):
			CyInterface().setDirty(InterfaceDirtyBits.Financial_Screen_DIRTY_BIT, False)
			self.drawContents()
		return

	#Rhye - start
        def printStars(self, ePlayer, panel, n, x, y, z):
                totStars = ""
                for i in range(n):
                    totStars = totStars + unichr(CyGame().getSymbolID(FontSymbols.SILVER_STAR_CHAR))
                if (gc.getPlayer(ePlayer).isHuman()):
                        self.getScreen().setLabel(panel, "Background",  totStars, CvUtil.FONT_CENTER_JUSTIFY, x, y, z, FontTypes.GAME_FONT, WidgetTypes.WIDGET_GENERAL, -1, -1 )
	    
	"""def printNumber(self, ePlayer, panel, iParameter, x, y, z):
		if (gc.getPlayer(ePlayer).isHuman()):
			if (iParameter == 1):
                        	iNewValue = utils.getParCities()
                	elif (iParameter == 2):
                        	iNewValue = utils.getParCivics()
                	elif (iParameter == 3):
                        	iNewValue = utils.getParEconomy()
                	elif (iParameter == 4):
                        	iNewValue = utils.getParExpansion()
                	elif (iParameter == 5):
                        	iNewValue = utils.getParDiplomacy()
                        number = str(iNewValue)
                        if (iNewValue > 0):
                                number = '+' + number
                        self.getScreen().setLabel(panel, "Background",  "(" + number + ")", CvUtil.FONT_CENTER_JUSTIFY, x, y, z, FontTypes.GAME_FONT, WidgetTypes.WIDGET_GENERAL, -1, -1 )"""
	    
	def printArrow(self, ePlayer, panel, iParameter, x, y, z):
                if (gc.getPlayer(ePlayer).isHuman()):
                        self.getScreen().setLabel(panel, "Background",  unichr(CyGame().getSymbolID(FontSymbols.POWER_CHAR) + 8 + utils.getArrow(iParameter)), CvUtil.FONT_CENTER_JUSTIFY, x, y, z, FontTypes.GAME_FONT, WidgetTypes.WIDGET_GENERAL, -1, -1 )
	 

	 
	#Rhye - end
	
	# srpt replacement function
	def printNumber(self, ePlayer, panel, iNumber, x, y, z):
		number = str(iNumber)
		if (iNumber > 0):
			number = '+' + number
		self.getScreen().setLabel(panel, "Background",  "(" + number + ")", CvUtil.FONT_CENTER_JUSTIFY, x, y, z, FontTypes.GAME_FONT, WidgetTypes.WIDGET_GENERAL, -1, -1 )

        
