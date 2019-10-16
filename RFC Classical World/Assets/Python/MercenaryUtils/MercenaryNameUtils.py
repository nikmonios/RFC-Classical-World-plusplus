#
# Mercenaries Mod
# By: The Lopez
# MercenaryNameUtils
# 

from CvPythonExtensions import *

import CvUtil
#import sys
#import PyHelpers
#import math
from StoredData import sd # edead
#import cPickle as pickle
import Consts as con #Rhye
#import CvTranslator #Rhye
from random import shuffle

################# SD-UTILITY-PACK ###################
# import SdToolKit
# sdEcho         = SdToolKit.sdEcho
# sdModInit      = SdToolKit.sdModInit
# sdModLoad      = SdToolKit.sdModLoad
# sdModSave      = SdToolKit.sdModSave
# sdEntityInit   = SdToolKit.sdEntityInit
# sdEntityExists = SdToolKit.sdEntityExists
# sdGetVal       = SdToolKit.sdGetVal
# sdSetVal       = SdToolKit.sdSetVal

gc = CyGlobalContext()	

#edead - start (realistic names lists)

lGenericNames = [ 
	"Persian",
	"Median",
	"Parthian",
]

lPersianNames = [ 
	"Persian",
	"Median",
	"Parthian",
	"Arachosian",
	"Sogdian",
	"Bactrian",
	"Gedrosian",
	"Armenian",
]

lEastAsianNames = [ 
	"Qin",
	"Chu",
	"Yan",
	"Zhao",
	"Goguryeo",
	"Han",
	"Wei",
	"Qi",
	"Yuezhi",
	"Nanyue",
	"Mintue",
	"Yayoi",
	"Annamese",
	"Mon",
	"Khmer",
]

lCaucasianNames = [ 
	"Alan",
	"Cappadocian",
	"Armenian",
	"Caucasian",
	"Albanian",
	"Iberian",
]

lEuropeanNames = [
	"Dacian",
	"Teuton",
	"Gaulish",
	"Belgian",
	"Iberian",
	"Italian",
	"Celtic",
	"Lusitanian",
	"Illyrian",
	"Sicilian",
	"Greek",
	"Thracian",
	"Macedonian",
]

lLateEuropeanNames = [ 
	"Frankish",
	"Gepid",
	"Gothic",
	"Alemanii",
	"Vandal",
	"Suevi",
	"Saxon",
	"Lombard",
	"Rugian",
	"Frisian",
	"Marcomanii",
]

lNorthAfricanNames = [ 
	"Mauretanian",
	"Numidian",
	"African",
	"Libyan",
	"Tripolitanian",
	"Cyrenaican",
]

lIndianNames = [ 
	"Gandharan",
	"Punjabi",
	"Sindhi",
	"Magadhan",
	"Saurashtran",
	"Kalingan",
	"Tamil",
	"Keralan",
	"Nepalese",
	"Deccan",
]

lRajputNames = [
	"Soomro",
	"Sammat",
	"Parmar",
	"Sisodian",
	"Chattari",
	"Bhari",
	"Tomara",
	"Dhangar",
	"Jat",
	"Bhati"
]

lAfricanNames = [
	"Nubian",
	"Kushite",
	"Egyptian",
	"Libyan",
	"Tigrayan",
	"Axumite",
	"Ethiopian",
]

lLateAfricanNames = [
	"Somali",
	"Sudanese",
	"Tigrayan",
	"Afari",
	"Beja",
	"Amhara",
	"Oromo",
]

lArabianNames = [ 
	"Arabian",
	"Nabatean",
	"Ghassanid",
	"Lahkmid",
	"Himyarite",
]

lKipchakNames = [ 
	"Kipchak",
	"Cuman",
	"Karakalpak",
]

lEarlyTurkicNames = [ 
	"Turkish", 
	"Turkoman", 
	"Kara-khanid", 
	"Khalaj", 
	"Turko-Persian", 
	"Karakalpak", 
	"Qashqai", 
	"Oghuz",
]

lAnatolianNames = [ 
	"Anatolian",
	"Chaldean",
	"Thracian",
	"Cappadocian",
	"Macedonian",
	"Moesian",
	"Galatian",
	"Bithynian",
	"Macedonian",
	"Cilician",
]

lGalleyNames = [ # galley, roundship
	"Syracusan",
	"Massilian",
	"Phoenician",
	"Greek",
	"Cretan",
	"Egyptian",
	"Massilian",
	"Tyrian",
	"Ionian",
]

lDhowNames = [ # dhow, baghlah
	"Keralan",
	"Tamil",
	"Sabean",
	"Egyptian",
	"Axumite",
	"Aceh",
]

lVarangianNames = [ # varangian guard
	"Scandinavian",
	"Danish",
	"Swedish",
	"Norwegian",
	"Anglo-Saxon",
	"Rus",
]

lBulgarianNames = [ # bulgarian raider
	"Thracian",
	"Moesian",
	"Dobrujan",
	"Stranjan",
]

lGreekCityNames = [ # hoplites
	"Athenian",
	"Spartan",
	"Corinthian",
	"Theban",
	"Salonican",
	"Macedonian",
	"Ionian",
	"Ephesian",
]

lAthenianCityNames = [ # hoplites
	"Athenian",
]

lCorinthianCityNames = [ # hoplites
	"Corinthian",
]

lSpartanCityNames = [ # hoplites\
	"Spartan",
]

lArabNames = [ # lancer, heavy spearman
	"Iraqi",
	"Syrian",
	"Kurdish",
	"Ayyarun",
	"Fityan",
	"Muhajir",
]

lEasternCamelNames = [
	"Sindhi",
	"Punjabi",
	"Arachosian",
	"Bactrian",
	"Sogdian",
]

lHorsemanNames = [
	"Median",
	"Parthian",
	"Arabian",
	"Persian",
	"Elamite",
	"Syrian",
	"Anatolian",
	"Sindhi",
	"Iberian",
	"Circassian",
	"Crimean",
]

lHorseArcherNames = [
	"Median",
	"Parthian",
	"Persian",
	"Scythian",
	"Alan",
	"Sogdian",
	"Sarmatian",
]

lJavelinNames = [
	"Libyan",
	"Armenian",
	"Circassian",
	"Arachosian",
	"Persian",
	"Anatolian",
	"Median",
	"Iberian",
	"Celtic",
]

lWesternSteppesNames = [
	"Scythian",
	"Sarmatian",
	"Median",
	"Parthian",
	"Alan",
]

lCentralSteppesNames = [
	"Scythian",
	"Sarmatian",
	"Median",
	"Parthian",
	"Alan",
	"Kirghiz",
	"Yuezhi",
]

lEasternSteppesNames = [
	"Xiongnu",
	"Yuezhi",
	"Jouan-jouan",
]

lMediterraneanNames = [
	"Judean",
	"Egyptian",
	"Libyan",
	"African",
	"Mauretanian",
	"Iberian",
	"Lusitanian",
	"Gaulish",
	"Celtic",
	"Italian",
	"Illyrian",
	"Greek",
	"Thracian",
	"Dacian",
	"Anatolian",
	"Syrian",
	"Cretan",
	"Cypriot",
	"Sicilian",
	"Sardinian",
	"Corsican",
	"Ballaeric",
	"Lydian",
]

lMediterraneanShipNames = [
	"Phoenician",
	"Egyptian",
	"Libyan",
	"African",
	"Iberian",
	"Lusitanian",
	"Italian",
	"Illyrian",
	"Greek",
	"Cretan",
	"Cypriot",
	"Sicilian",
	"Sardinian",
	"Corsican",
	"Ballaeric",
]

lEmpty = [
	"",
]

namesDict = {
	con.iJavelinman					: lJavelinNames,
	con.iJavelinman_Persian			: lPersianNames,
	con.iJavelinman_Mediterranean	: lMediterraneanNames,
	con.iJavelinman_Indian			: lIndianNames,
	con.iJavelinman_East_Asian		: lEastAsianNames,
	con.iJavelinman_African			: lAfricanNames,
	con.iSpearman		 			: lJavelinNames,
	con.iHeavySpearman		 		: lJavelinNames,
	con.iArcher						: lJavelinNames,
	con.iMarksman					: lJavelinNames,
	con.iAxeman						: lJavelinNames,
	con.iSwordsman					: lJavelinNames,
	con.iHeavySwordsman				: lJavelinNames,
	con.iSkirmisher					: lJavelinNames,
	con.iHorseman					: lHorsemanNames,
	con.iHorseman_Scythian			: lWesternSteppesNames,
	con.iHorseman_Sarmatian			: lCentralSteppesNames,
	con.iHorseman_Xiongnu			: lEasternSteppesNames,
	con.iHorseArcher				: lHorseArcherNames,
	con.iHorseArcher_Scythian		: lWesternSteppesNames,
	con.iHorseArcher_Sarmatian		: lCentralSteppesNames,
	con.iHorseArcher_Xiongnu		: lEasternSteppesNames,
	con.iHeavyHorseArcher			: lJavelinNames,
	con.iLancer						: lJavelinNames,
	con.iHeavyLancer				: lJavelinNames,
	con.iCamelRider					: lArabianNames,
	con.iGalley						: lGalleyNames,
	con.iWarGalley					: lGalleyNames,
	con.iRoundship					: lGalleyNames,
	con.iDhow						: lDhowNames,
	con.iBaghlah					: lDhowNames,
	con.iWarElephant				: lIndianNames,
	con.iSwordsman_East_Asian		: lEastAsianNames, 
	con.iSpearman_East_Asian		: lEastAsianNames, 
	con.iAxeman_East_Asian			: lEastAsianNames, 
	con.iHeavySpearman_East_Asian	: lEastAsianNames, 
	con.iSwordsman_Indian			: lIndianNames, 
	con.iSpearman_Indian			: lIndianNames, 
	con.iAxeman_Indian				: lIndianNames, 
	con.iJavelinman_Indian			: lIndianNames, 
	con.iHeavySpearman_Greek		: lGreekCityNames, 
	con.iHeavySpearman_Athenian		: lAthenianCityNames, 
	con.iHeavySpearman_Corinthian	: lCorinthianCityNames, 
	con.iHeavySpearman_Spartan		: lSpartanCityNames, 
	con.iSpearman_African			: lAfricanNames, 
	con.iAxeman_Teutonic			: lLateEuropeanNames, 
	con.iSpearman_European			: lEuropeanNames, 
	con.iHeavySpearman_Indian		: lIndianNames, 
	con.iArcher_East_Asian			: lEastAsianNames, 
	con.iArcher_African				: lAfricanNames, 
	con.iArcher_European			: lEuropeanNames, 
	con.iArcher_Greek				: lGreekCityNames, 
	con.iArcher_Indian				: lIndianNames, 
	con.iMarksman_East_Asian		: lEastAsianNames, 
	con.iMarksman_Persian			: lPersianNames, 
	con.iMarksman_Indian			: lIndianNames, 
}

#edead - end

# Returns a random unique name not found in the global mercenary pool
def getRandomMercenaryName(iCiv, iUnitType, bContractOut): #Rhye

	mercenaryName = ""
	
	# return any name if the global mercenary pool does not exist
	# if(sdEntityExists("Mercenaries Mod","MercenaryData") == False):
		# return mercenaryFirstNames[gc.getGame().getMapRand().get(len(mercenaryEuropeanNames), "Random Name")] + " " + gc.getUnitInfo(iUnitType).getDescription()	
	# mercenaries = sdGetVal("Mercenaries Mod", "MercenaryData", "MercenaryNames")
	mercenaries = sd.getMercenaryData("MercenaryNames")

	if (bContractOut):
		firstName = gc.getPlayer(iCiv).getCivilizationAdjective(0)
	else:
		# edead - realistic names start
		lNames = namesDict.get(iUnitType, lGenericNames)
		lastName = gc.getUnitInfo(iUnitType).getDescription()
		shuffle(lNames)
		bFound = False
		for firstName in lNames:
			if firstName == "":
				mercenaryName = lastName
			else:
				mercenaryName = firstName + " " + lastName
			if not mercenaries.has_key(mercenaryName):
				bFound = True
				break
		
		if not bFound:
			while(mercenaries.has_key(mercenaryName)):
				mercenaryName = mercenaryName + " "
		
		#edead - end
				
	#iLanguage = CyGame().getCurrentLanguage()
	#if (iLanguage == 1 or iLanguage == 3 or iLanguage == 4): #fra, ita, esp
    #            mercenaryName = lastName + " " + firstName

	return mercenaryName
	
