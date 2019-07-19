# Dynamic Civs - edead

from CvPythonExtensions import *
import CvUtil
import PyHelpers
import Consts as con
from StoredData import sd
from RFCUtils import utils

# globals
gc = CyGlobalContext()
PyPlayer = PyHelpers.PyPlayer
PyInfo = PyHelpers.PyInfo
localText = CyTranslator()
iNumPlayers = con.iNumPlayers


class DynamicCivs:


	def __init__(self):
		
		self.defaultNames = {
			con.iAntigonids : "TXT_KEY_CIV_ANTIGONIDS_DESC_DEFAULT",
			con.iSeleucids : "TXT_KEY_CIV_SELEUCIDS_DESC_DEFAULT",
			con.iEgypt : "TXT_KEY_CIV_EGYPT_DESC_DEFAULT",
			con.iCarthage : "TXT_KEY_CIV_CARTHAGE_DESC_DEFAULT",
			con.iMauryans : "TXT_KEY_CIV_MAURYANS_DESC_DEFAULT",
			con.iKalinka : "TXT_KEY_CIV_KALINKA_DESC_DEFAULT",
			con.iQin : "TXT_KEY_CIV_QIN_DESC_DEFAULT",
			con.iGojoseon : "TXT_KEY_CIV_GOJOSEON_DESC_DEFAULT",
			con.iNubia : "TXT_KEY_CIV_NUBIA_DESC_DEFAULT",
			con.iSaba : "TXT_KEY_CIV_SABA_DESC_DEFAULT",
			con.iPandyans : "TXT_KEY_CIV_PANDYANS_DESC_DEFAULT",
			con.iTocharians : "TXT_KEY_CIV_TOCHARIANS_DESC_DEFAULT",
			con.iPontus : "TXT_KEY_CIV_PONTUS_DESC_DEFAULT",
			con.iCelts : "TXT_KEY_CIV_CELTS_DESC_DEFAULT",
			con.iRome : "TXT_KEY_CIV_ROME_DESC_DEFAULT",
			con.iVietnam : "TXT_KEY_CIV_VIETNAM_DESC_DEFAULT",
			con.iBactria : "TXT_KEY_CIV_BACTRIA_DESC_DEFAULT",
			con.iHan : "TXT_KEY_CIV_HAN_DESC_DEFAULT",
			con.iSatavahana : "TXT_KEY_CIV_SATAVAHANA_DESC_DEFAULT",
			con.iArmenia : "TXT_KEY_CIV_ARMENIA_DESC_DEFAULT",
			con.iMaccabees : "TXT_KEY_CIV_MACCABEES_DESC_DEFAULT",
			con.iParthia : "TXT_KEY_CIV_PARTHIA_DESC_DEFAULT",
			con.iDacia : "TXT_KEY_CIV_DACIA_DESC_DEFAULT",
			con.iGoguryeo: "TXT_KEY_CIV_GOGURYEO_DESC_DEFAULT",
			con.iAxum : "TXT_KEY_CIV_AXUM_DESC_DEFAULT",
			con.iKushans : "TXT_KEY_CIV_KUSHANS_DESC_DEFAULT",
			con.iFunan : "TXT_KEY_CIV_FUNAN_DESC_DEFAULT",
			con.iJin : "TXT_KEY_CIV_JIN_DESC_DEFAULT",
			con.iSassanids : "TXT_KEY_CIV_SASSANIDS_DESC_DEFAULT",
			con.iYamato : "TXT_KEY_CIV_YAMATO_DESC_DEFAULT",
			con.iByzantines : "TXT_KEY_CIV_BYZANTINES_DESC_DEFAULT",
			con.iGupta : "TXT_KEY_CIV_GUPTA_DESC_DEFAULT",
			con.iFranks : "TXT_KEY_CIV_FRANKS_DESC_DEFAULT",
			con.iChalukyans : "TXT_KEY_CIV_CHALUKYANS_DESC_DEFAULT",
			con.iGokturks : "TXT_KEY_CIV_GOKTURKS_DESC_DEFAULT",
			con.iSrivajaya : "TXT_KEY_CIV_SRIVAJAYA_DESC_DEFAULT",
			con.iKhazars : "TXT_KEY_CIV_KHAZARS_DESC_DEFAULT",
			con.iTibet : "TXT_KEY_CIV_TIBET_DESC_DEFAULT",
			con.iTang : "TXT_KEY_CIV_TANG_DESC_DEFAULT",
			con.iArabs : "TXT_KEY_CIV_ARABS_DESC_DEFAULT",
			con.iGhana : "TXT_KEY_CIV_GHANA_DESC_DEFAULT",
			con.iSungas : "TXT_KEY_CIV_SUNGAS_DESC_DEFAULT",
			con.iVisigoths : "TXT_KEY_CIV_VISIGOTHS_DESC_DEFAULT",
			con.iOstrogoths : "TXT_KEY_CIV_OSTROGOTHS_DESC_DEFAULT",
			con.iVandals : "TXT_KEY_CIV_VANDALS_DESC_DEFAULT",
			con.iLombards : "TXT_KEY_CIV_LOMBARDS_DESC_DEFAULT",
			con.iMakuria : "TXT_KEY_CIV_MAKURIA_DESC_DEFAULT",
			con.iHimyarites : "TXT_KEY_CIV_HIMYARITES_DESC_DEFAULT",
			#con.iChenla : "TXT_KEY_CIV_CHENLA_DESC_DEFAULT",
			con.iNanYue : "TXT_KEY_CIV_NANYUE_DESC_DEFAULT",
			con.iShu : "TXT_KEY_CIV_SHU_DESC_DEFAULT",
			con.iWu : "TXT_KEY_CIV_WU_DESC_DEFAULT",
			con.iScythians : "TXT_KEY_CIV_SCYTHIANS_DESC_DEFAULT",
			con.iHephthalites : "TXT_KEY_CIV_HEPHTHALITES_DESC_DEFAULT",
			con.iHuns : "TXT_KEY_CIV_HUNS_DESC_DEFAULT",
			con.iAvars : "TXT_KEY_CIV_AVARS_DESC_DEFAULT",
			con.iRouran : "TXT_KEY_CIV_ROURAN_DESC_DEFAULT",
			con.iVakatakas : "TXT_KEY_CIV_VAKATAKA_DESC_DEFAULT",
			con.iSong : "TXT_KEY_CIV_SONG_DESC_DEFAULT",
			con.iMagadha : "TXT_KEY_CIV_MAGADHA_DESC_DEFAULT",
			con.iRebelRome : "TXT_KEY_CIV_REBEL_ROME_DESC_DEFAULT",
			con.iNumidia : "TXT_KEY_CIV_NUMIDIA_DESC_DEFAULT",
			con.iMacedon : "TXT_KEY_CIV_MACEDON_DESC_DEFAULT",
			con.iPallavas : "TXT_KEY_CIV_PALLAVAS_DESC_DEFAULT",
			con.iKalabhras : "TXT_KEY_CIV_KALABHRAS_DESC_DEFAULT",
		}
		
		self.vassalNames = {
			con.iEgypt : "TXT_KEY_CIV_EGYPT_DESC_VASSAL",
			con.iNubia : "TXT_KEY_CIV_NUBIA_DESC_VASSAL",
			con.iCarthage : "TXT_KEY_CIV_CARTHAGE_DESC_VASSAL",
			con.iCelts : "TXT_KEY_CIV_CELTS_DESC_VASSAL",
			con.iSeleucids : "TXT_KEY_CIV_SELEUCIDS_DESC_VASSAL",
			con.iMauryans : "TXT_KEY_CIV_MAURYANS_DESC_VASSAL",
			con.iArmenia : "TXT_KEY_CIV_ARMENIA_DESC_VASSAL",
			con.iSaba: "TXT_KEY_CIV_SABA_DESC_VASSAL",
			con.iTocharians : "TXT_KEY_CIV_TOCHARIANS_DESC_VASSAL",
			con.iPandyans : "TXT_KEY_CIV_PANDYANS_DESC_VASSAL",
			con.iRome : "TXT_KEY_CIV_ROME_DESC_VASSAL",
			con.iHan : "TXT_KEY_CIV_HAN_DESC_VASSAL",
			con.iBactria : "TXT_KEY_CIV_BACTRIA_DESC_VASSAL",
			con.iParthia : "TXT_KEY_CIV_PARTHIA_DESC_VASSAL",
			con.iSatavahana : "TXT_KEY_CIV_SATAVAHANA_DESC_VASSAL",
			con.iDacia : "TXT_KEY_CIV_DACIA_DESC_VASSAL",
			con.iGoguryeo: "TXT_KEY_CIV_GOGURYEO_DESC_VASSAL",
			con.iKushans: "TXT_KEY_CIV_KUSHANS_DESC_VASSAL",
			con.iAxum: "TXT_KEY_CIV_AXUM_DESC_VASSAL",
			con.iFunan: "TXT_KEY_CIV_FUNAN_DESC_VASSAL",
			con.iSassanids: "TXT_KEY_CIV_SASSANIDS_DESC_VASSAL",
			con.iJin: "TXT_KEY_CIV_JIN_DESC_VASSAL",
			con.iGupta: "TXT_KEY_CIV_GUPTA_DESC_VASSAL",
			con.iFranks : "TXT_KEY_CIV_FRANKS_DESC_VASSAL",
			con.iChalukyans : "TXT_KEY_CIV_CHALUKYANS_DESC_VASSAL",
			con.iSrivajaya: "TXT_KEY_CIV_SRIVAJAYA_DESC_VASSAL",
			con.iTang: "TXT_KEY_CIV_TANG_DESC_VASSAL",
			con.iArabs: "TXT_KEY_CIV_ARABS_DESC_VASSAL",
			con.iGhana: "TXT_KEY_CIV_GHANA_DESC_VASSAL",
			con.iQin: "TXT_KEY_CIV_QIN_DESC_VASSAL",
			con.iByzantines: "TXT_KEY_CIV_BYZANTINES_DESC_VASSAL",
			con.iGokturks: "TXT_KEY_CIV_GOKTURKS_DESC_VASSAL",
			con.iKhazars: "TXT_KEY_CIV_KHAZARS_DESC_VASSAL",
			con.iTibet: "TXT_KEY_CIV_TIBET_DESC_VASSAL",
		}
		
		
		
		

		
		self.SpecialNames = {
			con.iQin : "TXT_KEY_CIV_SHU_DESC_DEFAULT",
			con.iHan : "TXT_KEY_CIV_WU_DESC_DEFAULT",
			con.iJin : "TXT_KEY_CIV_WEI_DESC_DEFAULT",
			con.iRome : "TXT_KEY_CIV_WESTERN_ROME",
			con.iByzantines : "TXT_KEY_CIV_EASTERN_ROME",
		}
		
		self.empireNames = {
			con.iAntigonids : "TXT_KEY_CIV_ANTIGONIDS_EMPIRE_DESC",
			con.iSeleucids : "TXT_KEY_CIV_SELEUCIDS_EMPIRE_DESC",
			con.iEgypt : "TXT_KEY_CIV_EGYPT_EMPIRE_DESC",
			con.iCarthage : "TXT_KEY_CIV_CARTHAGE_EMPIRE_DESC",
			con.iMauryans : "TXT_KEY_CIV_MAURYANS_EMPIRE_DESC",
			con.iKalinka : "TXT_KEY_CIV_KALINKA_EMPIRE_DESC",
			con.iQin : "TXT_KEY_CIV_QIN_EMPIRE_DESC",
			con.iGojoseon : "TXT_KEY_CIV_GOJOSEON_EMPIRE_DESC",
			con.iNubia : "TXT_KEY_CIV_NUBIA_EMPIRE_DESC",
			con.iSaba : "TXT_KEY_CIV_SABA_EMPIRE_DESC",
			con.iPandyans : "TXT_KEY_CIV_PANDYANS_EMPIRE_DESC",
			con.iTocharians : "TXT_KEY_CIV_TOCHARIANS_EMPIRE_DESC",
			con.iPontus : "TXT_KEY_CIV_PONTUS_EMPIRE_DESC",
			con.iCelts : "TXT_KEY_CIV_CELTS_EMPIRE_DESC",
			con.iRome : "TXT_KEY_CIV_ROME_EMPIRE_DESC",
			con.iVietnam : "TXT_KEY_CIV_VIETNAM_EMPIRE_DESC",
			con.iBactria : "TXT_KEY_CIV_BACTRIA_EMPIRE_DESC",
			con.iHan : "TXT_KEY_CIV_HAN_EMPIRE_DESC",
			con.iSatavahana : "TXT_KEY_CIV_SATAVAHANA_EMPIRE_DESC",
			con.iArmenia : "TXT_KEY_CIV_ARMENIA_EMPIRE_DESC",
			con.iMaccabees : "TXT_KEY_CIV_MACCABEES_EMPIRE_DESC",
			con.iParthia : "TXT_KEY_CIV_PARTHIA_EMPIRE_DESC",
			con.iDacia : "TXT_KEY_CIV_DACIA_EMPIRE_DESC",
			con.iGoguryeo : "TXT_KEY_CIV_GOGURYEO_EMPIRE_DESC",
			con.iAxum : "TXT_KEY_CIV_AXUM_EMPIRE_DESC",
			con.iKushans : "TXT_KEY_CIV_KUSHANS_EMPIRE_DESC",
			con.iSungas : "TXT_KEY_CIV_SUNGAS_EMPIRE_DESC",
			con.iChalukyans : "TXT_KEY_CIV_CHALUKYANS_EMPIRE_DESC",
			con.iSassanids : "TXT_KEY_CIV_SASSANIDS_EMPIRE_DESC",
			con.iFranks : "TXT_KEY_CIV_FRANKS_EMPIRE_DESC",
		}
		

	def setCivDesc(self, iCiv, sName, sShort="", sAdj=""):
		gc.getPlayer(iCiv).setCivName(localText.getText(sName, ()), localText.getText(sShort, ()), localText.getText(sAdj, ()))


	def setup(self):
	
		return
			
		for iCiv in range (con.iNumPlayers):
			self.setCivDesc(iCiv, self.defaultNames[sd.getCivilization(iCiv)])
			self.checkName(iCiv)


	def checkName(self, iPlayer):
	
		return
	
		#print "checkName"
		
		if iPlayer >= iNumPlayers: 
			return
		if not gc.getPlayer(iPlayer).isAlive: 
			return
	
		bVassal = utils.isAVassal(iPlayer)
		pPlayer = gc.getPlayer(iPlayer)
		iReligion = pPlayer.getStateReligion()
		capital = gc.getPlayer(iPlayer).getCapitalCity()
		iGameTurn = gc.getGame().getGameTurn()
		
		iCivilization = sd.getCivilization(iPlayer)
		
		# 3 kingdoms > respawn > capital > religion > empire > vassal
		
		if iPlayer == con.iJin:
			if gc.getPlayer(con.iQin).isAlive() and gc.getPlayer(con.iHan).isAlive():
				self.setCivDesc(iPlayer, self.SpecialNames[iPlayer])
				return
		if iPlayer in [con.iRome, con.iByzantines]: 
			if utils.getYear() >= con.tBirth[con.iByzantines] and gc.getPlayer(con.iByzantines).isAlive():
				self.setCivDesc(iPlayer, self.SpecialNames[iPlayer])
				self.setCivDesc(con.iByzantines, self.SpecialNames[con.iByzantines])
				return
		#if iPlayer == con.iByzantines and utils.isActive(con.iRome) and sd.getCivilization(con.iByzantines) == con.iByzantines:
				#self.setCivDesc(iPlayer, self.SpecialNames[iPlayer])
				#self.setCivDesc(con.iRome, self.SpecialNames[con.iRome])
				#return
		
		
		# by vassalage
		if bVassal and iCivilization in self.vassalNames:
			szName = self.vassalNames[iCivilization]
		else:
			szName = self.defaultNames[iCivilization]

		# by status (empires)
		if not bVassal:
			iCivic = pPlayer.getCivics(0)
			if iCivilization in self.empireNames:
				minCities = 5 
				if iCivic == con.iEmpireCivic or pPlayer.getNumCities() >= minCities:
					if pPlayer.getNumCities() >= (minCities):
						szName = self.empireNames[iCivilization]
			
		self.setCivDesc(iPlayer, szName)
		
	def onSetPlayerAlive(self, iPlayer):
		self.checkName(iPlayer)
		
	def onCivSpawn(self, iPlayer):
		self.checkName(iPlayer)
		if iPlayer == con.iByzantines and sd.getCivilization(con.iByzantines) == con.iByzantines:
			self.checkName(con.iRome)


	def onCivRespawn(self, iPlayer, iGameTurn):
	
		self.checkName(iPlayer)
		
		
			
				
	def onVassalState(self, argsList):
		iMaster, iVassal, bVassal = argsList
		self.checkName(iVassal)
	
	
	def onPlayerChangeStateReligion(self, argsList):
		iPlayer, iNewReligion, iOldReligion = argsList
		self.checkName(iPlayer)
		if iPlayer == con.iMauryans and iNewReligion == con.iHinduism and utils.checkRegionOwnedCity(con.iMauryans, con.rMagadha):
			sd.setCivilization(con.iMauryans, con.iSungas)
			self.setCivDesc(iPlayer, "TXT_KEY_CIV_SUNGA_DESC_DEFAULT", "TXT_KEY_CIV_SUNGA_SHORT_DESC", "TXT_KEY_CIV_SUNGA_ADJECTIVE")
			gc.getPlayer(iPlayer).setName(localText.getText("TXT_KEY_LEADER_PUSYAMITRA_SUNGA", ()))
			gc.getPlayer(iPlayer).setCivilizationType(con.iSungas)
			#gc.getPlayer(iPlayer).setLeader(con.iPusyamitra)
			CyInterface().addMessage(utils.getHumanID(), False, con.iDuration, CyTranslator().getText("TXT_KEY_SUNGA_REBELLION", ()), "", 0, "", ColorTypes(con.iRed), -1, -1, True, True)


	def onRevolution(self, iPlayer):
		self.checkName(iPlayer)
		

	def onCityAcquired(self, argsList):
		iPreviousOwner, iNewOwner, city, bConquest, bTrade = argsList
		
		if iPreviousOwner == con.iRome and iNewOwner == con.iByzantines:
			self.checkName(con.iRome)
		
		if city.getNumRealBuilding(con.iPalace):
			self.checkName(iPreviousOwner)
		
		if gc.getPlayer(iNewOwner).getNumCities() in [0, 1, 4, 6, 8, 12, 16]:
			self.checkName(iNewOwner)