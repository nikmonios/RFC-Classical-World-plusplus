# UnitArtStyler by edead
# Works only with the related DLL changes (CvUnit::setArtDefineTag and CvUnitInfo::getArtDefineTag)
# Use to convert unit art of independent units based on the city art style, or province, or w/e

from CvPythonExtensions import *
import Consts as con

gc = CyGlobalContext()

# Unit Art Styles for a particular city/plot Art Style
g_CityArtStyles = (
"UNIT_ARTSTYLE_EUROPEAN", 			# 0 = ARTSTYLE_EUROPEAN
"UNIT_ARTSTYLE_ARABIAN", 			# 1 = ARTSTYLE_ARABIAN
"UNIT_ARTSTYLE_PERSIAN", 			# 2 = ARTSTYLE_MIDDLE_EAST
"UNIT_ARTSTYLE_MEDITERRANEAN",		# 3 = ARTSTYLE_MEDITERRANEAN
"UNIT_ARTSTYLE_INDIA",				# 4 = ARTSTYLE_INDIAN
"UNIT_ARTSTYLE_EGYPT",				# 5 = ARTSTYLE_EGYPT
"UNIT_ARTSTYLE_EAST_ASIAN",			# 6 = ARTSTYLE_ASIA
"UNIT_ARTSTYLE_EAST_ASIAN",			# 7 = ARTSTYLE_JAPAN
"UNIT_ARTSTYLE_INDIA",				# 8 = ARTSTYLE_SOUTH_EAST_ASIA
"UNIT_ARTSTYLE_AFRICAN",			# 9 = ARTSTYLE_AFRICA
)

# Unit Art Styles for a particular region (province)
g_RegionArtStyles = {
	con.rCaledonia 			: "UNIT_ARTSTYLE_EUROPEAN", 
	con.rHibernia 			: "UNIT_ARTSTYLE_EUROPEAN", 
	con.rBritannia 			: "UNIT_ARTSTYLE_EUROPEAN", 
	con.rScania 			: "UNIT_ARTSTYLE_EUROPEAN", 
	con.rAquitania 			: "UNIT_ARTSTYLE_EUROPEAN", 
	con.rGaul 				: "UNIT_ARTSTYLE_EUROPEAN", 
	con.rSeptimania 		: "UNIT_ARTSTYLE_MEDITERRANEAN", 
	con.rIberia 			: "UNIT_ARTSTYLE_EUROPEAN", 
	con.rGermania 			: "UNIT_ARTSTYLE_EUROPEAN", 
	con.rNItaly 			: "UNIT_ARTSTYLE_MEDITERRANEAN", 
	con.rSicily 			: "UNIT_ARTSTYLE_MEDITERRANEAN", 
	con.rGreece 			: "UNIT_ARTSTYLE_MEDITERRANEAN", 
	con.rIllyricum 			: "UNIT_ARTSTYLE_MEDITERRANEAN", 
	con.rThrace 			: "UNIT_ARTSTYLE_MEDITERRANEAN", 
	con.rMacedonia 			: "UNIT_ARTSTYLE_MEDITERRANEAN", 
	con.rDacia 				: "UNIT_ARTSTYLE_EUROPEAN", 
	con.rSlavia 			: "UNIT_ARTSTYLE_EUROPEAN", 
	con.rMoesia 			: "UNIT_ARTSTYLE_EUROPEAN", 
	con.rAsia 				: "UNIT_ARTSTYLE_MEDITERRANEAN", 
	con.rPontus 			: "UNIT_ARTSTYLE_MEDITERRANEAN", 
	con.rCappadocia 		: "UNIT_ARTSTYLE_MEDITERRANEAN", 
	con.rArmenia 			: "UNIT_ARTSTYLE_PERSIAN", 
	con.rSyria 				: "UNIT_ARTSTYLE_MEDITERRANEAN", 
	con.rMesopotamia 		: "UNIT_ARTSTYLE_PERSIAN", 
	con.rArabia 			: "UNIT_ARTSTYLE_ARABIAN", 
	con.rArabiaFelix 		: "UNIT_ARTSTYLE_ARABIAN", 
	con.rJudea 				: "UNIT_ARTSTYLE_PERSIAN", 
	con.rEgypt 				: "UNIT_ARTSTYLE_EGYPT", 
	con.rLibya 				: "UNIT_ARTSTYLE_EGYPT", 
	con.rNumidia 			: "UNIT_ARTSTYLE_MEDITERRANEAN", 
	con.rAfrica 			: "UNIT_ARTSTYLE_MEDITERRANEAN", 
	con.rMauretania 		: "UNIT_ARTSTYLE_MEDITERRANEAN", 
	con.rNubia 				: "UNIT_ARTSTYLE_AFRICAN", 
	con.rAxum 				: "UNIT_ARTSTYLE_AFRICAN", 
	con.rPunt 				: "UNIT_ARTSTYLE_AFRICAN", 
	con.rSahara 			: "UNIT_ARTSTYLE_AFRICAN", 
	con.rAethiopia 			: "UNIT_ARTSTYLE_AFRICAN", 
	con.rGuinea 			: "UNIT_ARTSTYLE_AFRICAN", 
	con.rMedia 				: "UNIT_ARTSTYLE_PERSIAN", 
	con.rPersia 			: "UNIT_ARTSTYLE_PERSIAN", 
	con.rParthia 			: "UNIT_ARTSTYLE_PERSIAN", 
	con.rArachosia 			: "UNIT_ARTSTYLE_PERSIAN", 
	con.rSogdiana 			: "UNIT_ARTSTYLE_PERSIAN", 
	con.rSindh 				: "UNIT_ARTSTYLE_INDIA", 
	con.rGandhara 			: "UNIT_ARTSTYLE_INDIA", 
	con.rPunjab 			: "UNIT_ARTSTYLE_INDIA", 
	con.rThar 				: "UNIT_ARTSTYLE_INDIA", 
	con.rSaurashtra 		: "UNIT_ARTSTYLE_DECCAN", 
	con.rMagadha 			: "UNIT_ARTSTYLE_MAURYANS", 
	con.rBangala 			: "UNIT_ARTSTYLE_INDIA", 
	con.rKalinka 			: "UNIT_ARTSTYLE_TAMIL", 
	con.rKerala 			: "UNIT_ARTSTYLE_TAMIL", 
	con.rTamilNadu 			: "UNIT_ARTSTYLE_TAMIL", 
	con.rAvanti 			: "UNIT_ARTSTYLE_DECCAN", 
	con.rDeccan 			: "UNIT_ARTSTYLE_DECCAN", 
	con.rLanka 				: "UNIT_ARTSTYLE_TAMIL", 
	con.rAndhra 			: "UNIT_ARTSTYLE_DECCAN", 
	con.rTibet 				: "UNIT_ARTSTYLE_EAST_ASIAN", 
	con.rTarim 				: "UNIT_ARTSTYLE_EAST_ASIAN", 
	con.rQinghai 			: "UNIT_ARTSTYLE_EAST_ASIAN", 
	con.rNanzhao 			: "UNIT_ARTSTYLE_SOUTHEAST_ASIAN", 
	con.rBirma 				: "UNIT_ARTSTYLE_TAMIL", 
	con.rFunan 				: "UNIT_ARTSTYLE_SOUTHEAST_ASIAN", 
	con.rAnnam 				: "UNIT_ARTSTYLE_SOUTHEAST_ASIAN", 
	con.rMalaya 			: "UNIT_ARTSTYLE_SOUTHEAST_ASIAN", 
	con.rSumatra 			: "UNIT_ARTSTYLE_SOUTHEAST_ASIAN", 
	con.rJava 				: "UNIT_ARTSTYLE_SOUTHEAST_ASIAN", 
	con.rBorneo 			: "UNIT_ARTSTYLE_SOUTHEAST_ASIAN", 
	con.rPhilipines 		: "UNIT_ARTSTYLE_SOUTHEAST_ASIAN", 
	con.rChampa 			: "UNIT_ARTSTYLE_SOUTHEAST_ASIAN", 
	con.rChu 				: "UNIT_ARTSTYLE_EAST_ASIAN", 
	con.rQi 				: "UNIT_ARTSTYLE_EAST_ASIAN", 
	con.rYan 				: "UNIT_ARTSTYLE_EAST_ASIAN", 
	con.rZhao 				: "UNIT_ARTSTYLE_EAST_ASIAN", 
	con.rWei 				: "UNIT_ARTSTYLE_EAST_ASIAN", 
	con.rQin 				: "UNIT_ARTSTYLE_EAST_ASIAN", 
	con.rHan 				: "UNIT_ARTSTYLE_EAST_ASIAN", 
	con.rNanYue 			: "UNIT_ARTSTYLE_EAST_ASIAN", 
	con.rAssam 				: "UNIT_ARTSTYLE_INDIA", 
	con.rNepal 				: "UNIT_ARTSTYLE_INDIA", 
	con.rPamir 				: "UNIT_ARTSTYLE_INDIA", 
	con.rFerghana 			: "UNIT_ARTSTYLE_PERSIAN", 
	con.rJin 				: "UNIT_ARTSTYLE_EAST_ASIAN", 
	con.rGoguryeo 			: "UNIT_ARTSTYLE_EAST_ASIAN", 
	con.rYamato 			: "UNIT_ARTSTYLE_EAST_ASIAN", 
	con.rEmishi 			: "UNIT_ARTSTYLE_EAST_ASIAN", 
	con.rHokkaido 			: "UNIT_ARTSTYLE_EAST_ASIAN", 
	con.rScythianSteppe 	: "UNIT_ARTSTYLE_PERSIAN", 
	con.rSarmatianSteppe 	: "UNIT_ARTSTYLE_PERSIAN", 
	con.rMongolianSteppe 	: "UNIT_ARTSTYLE_EAST_ASIAN", 
	con.rSiberia 			: "UNIT_ARTSTYLE_EUROPEAN", 
	con.rCaucasus 			: "UNIT_ARTSTYLE_PERSIAN", 
	con.rIslands 			: "UNIT_ARTSTYLE_INDIA", 
	con.rAustralia 			: "UNIT_ARTSTYLE_INDIA", 
	con.rTaiwan 			: "UNIT_ARTSTYLE_EAST_ASIAN", 
	con.rAtlanticOcean 		: "UNIT_ARTSTYLE_INDIA", 
	con.rNorthSea 			: "UNIT_ARTSTYLE_INDIA", 
	con.rBalticSea 			: "UNIT_ARTSTYLE_INDIA", 
	con.rMediterraneanSea 	: "UNIT_ARTSTYLE_INDIA", 
	con.rBlackSea 			: "UNIT_ARTSTYLE_INDIA", 
	con.rCaspianSea 		: "UNIT_ARTSTYLE_INDIA", 
	con.rAralSea 			: "UNIT_ARTSTYLE_INDIA", 
	con.rRedSea 			: "UNIT_ARTSTYLE_INDIA", 
	con.rPersianGulf 		: "UNIT_ARTSTYLE_INDIA", 
	con.rIndianOcean 		: "UNIT_ARTSTYLE_INDIA", 
	con.rSouthChinaSea 		: "UNIT_ARTSTYLE_EAST_ASIAN", 
	con.rYellowSea 			: "UNIT_ARTSTYLE_EAST_ASIAN", 
	con.rSeaOfJapan 		: "UNIT_ARTSTYLE_EAST_ASIAN", 
	con.rPacificOcean 		: "UNIT_ARTSTYLE_EAST_ASIAN", 
	con.rBactria 			: "UNIT_ARTSTYLE_PERSIAN", 
	con.rMargiana 			: "UNIT_ARTSTYLE_PERSIAN", 
	con.rCrimea 			: "UNIT_ARTSTYLE_MEDITERRANEAN", 
	con.rShu 				: "UNIT_ARTSTYLE_EAST_ASIAN", 
	con.rBa 				: "UNIT_ARTSTYLE_EAST_ASIAN", 
	con.rMinYue 			: "UNIT_ARTSTYLE_EAST_ASIAN", 
	con.rGansu 				: "UNIT_ARTSTYLE_EAST_ASIAN", 
	con.rMakan 				: "UNIT_ARTSTYLE_ARABIAN", 
	con.rBuyeo 				: "UNIT_ARTSTYLE_EAST_ASIAN", 
	con.rBaetica 			: "UNIT_ARTSTYLE_MEDITERRANEAN", 
	con.rLusitania 			: "UNIT_ARTSTYLE_MEDITERRANEAN", 
	con.rSItaly 			: "UNIT_ARTSTYLE_MEDITERRANEAN", 
	con.rSulawesi 			: "UNIT_ARTSTYLE_SOUTHEAST_ASIAN", 
	con.rPapua 				: "UNIT_ARTSTYLE_SOUTHEAST_ASIAN", 
	con.rWu 				: "UNIT_ARTSTYLE_EAST_ASIAN", 
	con.rMaldives 			: "UNIT_ARTSTYLE_INDIA", 
	con.rCyprus 			: "UNIT_ARTSTYLE_MEDITERRANEAN", 
	con.rCrete 				: "UNIT_ARTSTYLE_MEDITERRANEAN", 
	con.rRhodes 			: "UNIT_ARTSTYLE_MEDITERRANEAN", 
	con.rSardinia 			: "UNIT_ARTSTYLE_MEDITERRANEAN", 
	con.rCorsica 			: "UNIT_ARTSTYLE_MEDITERRANEAN", 
	con.rMallorca 			: "UNIT_ARTSTYLE_MEDITERRANEAN",
	con.rMalta 				: "UNIT_ARTSTYLE_MEDITERRANEAN"
}

# Conditional Unit Art Styles for a particular region : (iDate, tReligions, eArtStyle)
g_ConditionalArtStyles = {
	con.rMesopotamia			: (con.tBirth[con.iArabs], (con.iIslam), "UNIT_ARTSTYLE_ARABIAN"),
}


def checkUnitArt(unit):
	"""Checks unit and either updates or resets the ArtDefineTag."""
	if unit:
		if gc.getPlayer(unit.getOwner()).isMinorCiv():
			updateUnitArt(unit)
		else:
			resetUnitArt(unit)

			
def setUnitArt(unit, eUnitArtStyle):
	"""Sets the ArtDefineTag of unit based on eArtStyle (not UnitArtStyle!)."""
	if unit and eUnitArtStyle >= 0:
		unit.setArtDefineTag(gc.getUnitInfo(unit.getUnitType()).getArtDefineTag(0, eUnitArtStyle))


def updateUnitArt(unit):
	"""Updates the ArtDefineTag of unit based on the ArtStyle of its plot or region (province)."""
	if unit:
		plot = unit.plot()
		if plot:
			# base art style from plot art
			eUnitArtStyle = -1
			if plot.getRegionID() in g_RegionArtStyles:
				#print "plot in province"
				eUnitArtStyle = gc.getInfoTypeForString(g_RegionArtStyles[plot.getRegionID()])
				#print "eUnitArtStyle=", eUnitArtStyle
			# art style change based on date and religions present in city
			'''if plot.getRegionID() in g_ConditionalArtStyles:
				if gc.getGame().getGameTurnYear() >= g_ConditionalArtStyles[plot.getRegionID()][0]:
					bFound = True
					if plot.isCity():
						city = plot.getPlotCity()
						bFound = False
						for iReligion in g_ConditionalArtStyles[plot.getRegionID()][1]:
							if city.isHasReligion(iReligion):
								bFound = True
								break
					if bFound:
						eUnitArtStyle = gc.getInfoTypeForString(g_ConditionalArtStyles[plot.getRegionID()][2])''' # srpt
			setUnitArt(unit, eUnitArtStyle)


def updateUnitArtAtPlot(plot):
	"""Updates the ArtDefineTag of all units at a given plot."""
	if plot:
		for i in range(plot.getNumUnits()):
			updateUnitArt(plot.getUnit(i))


def resetUnitArt(unit):
	"""Resets the ArtDefineTag, bringing back the default civ-based UnitArtStyle."""
	if unit:
		unit.setArtDefineTag("")
