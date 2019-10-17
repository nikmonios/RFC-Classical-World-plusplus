# GENERAL

iStartYear = -320
iCalendar = 0

#for messages
iDuration = 20
iWhite = 0
iRed = 7
iGreen = 8
iBlue = 9
iLightBlue = 10
iYellow = 11
iDarkPink = 12
iLightRed = 20
iPurple = 25
iCyan = 44
iBrown = 55
iOrange = 78
iTan = 90
iLime = 139

# Map
iMapWidth = 176
iMapHeight = 84

# RiseAndFall (0,0) in RFC
iCatapultX = 70
iCatapultY = 82

# Unit flipping (0,67) in RFC
iFlipX = 72
iFlipY = 82

iSeaFlipX = 0
iSeaFlipY = 0

# Temp plot for creating mercenaries
iMercX = 74
iMercY = 82

# RFC Plague
iImmunity = 20

# directions
iNumDirections = 8
(iNorth, iNortheast, iEast, iSouthEast, iSouth, iSouthWest, iWest, iNorthWest) = range(iNumDirections)


l0Array =       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# CITY COORDS for religions, free capitals, name updates

tBabylon = (71,39)
tJerusalem = (62, 37)
tConstantinople = (53, 51)
tAlexandria = (53,35) 
tMecca = (67,27)
tMedina = (45,14) 
tPersepolis = (80,37) 
tVaranasi = (111,37) 
tTaxila = (100,46) 
tCtesiphon = (72,42)
tDamascus = (65,42)
tTyre = (62,41) 
tAntioch = (64,46) 
tRome = (35, 51) 
tPataliputra = (114,37)
tQufu = (145, 51)
tLuoyang = (140, 50)
tAthens = (47, 46)
tCarthage = (29, 40)
tVatapi = (103, 25)
tPella = (47, 50)

lAINoRaze = [tConstantinople, tJerusalem, tMecca, tPersepolis, tVaranasi, tAlexandria, tBabylon, tRome, tPataliputra, tLuoyang, tQufu, tTyre, tAthens]


tRomanNumerals = ( "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII", "XIII", "XIV", "XV", "XVI", "XVII", "XVIII", "XIX", "XX", "XXI", "XXII", "XXIII", "XXIV", 
"XXV", "XXVI", "XXVII", "XXVIII", "XXIX", "XXX", "XXXI", "XXXII", "XXXIII", "XXXIV", "XXXV", "XXXVI", "XXXVII", "XXXVIII", "XXXIX", "XXXX" )

# PLAYERS

iNumPlayers = 48
(iAntigonids, iSeleucids, iEgypt, iCarthage, iMauryans, iKalinka, iQin, iGojoseon, iNubia, iSaba, iPandyans, iPontus, iCelts, iRome, iVietnam, iTocharians, iBactria, 
iHan, iSatavahana, iArmenia, iMaccabees, iParthia, iDacia, iGoguryeo, iAxum, iKushans, iFunan, iJin, iSassanids, iYamato, iGupta, iByzantines, iVisigoths, iVandals, 
iOstrogoths, iFranks, iChalukyans, iLombards, iGokturks, iSrivajaya, iKhazars, iTibet, iTang, iArabs, iNomad0, iNomad1, iNomad2, iNomad3) = range(iNumPlayers)

iNumLeaders = 56
(iAntigonus, iSeleucus, iPtolemy, iHannibal, iAsoka, iKharavela, iQinShiHuang, iDangun, iArrakamani, iTubaAbu, iNedunj, iMithridates, iVercingetorix, iCaesar, 
iThucPhan, iSapadbizes, iDemetrius, iLeaderWu, iSatakarni, iTigranes, iSimonMaccabee, iArsaces, iDecebal, iGwanggaeto, iEzana, iKanishka, iLieuye, iSimaYan, iShapur, 
iJingu, iChandragupta, iJustinian, iAlaric, iGaiseric, iTheodoric, iCharlemagne, iPulakesi, iLiutprand, iBilge, iSarmatungga, iBulan, iSongstenGampo, iTaizong, 
iAbuBakr, iGhana, iSyphax, iSakaLeader, iZhaoTuo, iRouranLeader, iLiuBei, iSunQuan, iPusyamitra, iPompey, iTariq, iBarbarianLeader, iMinorLeader, ) = range(iNumLeaders)


iIndependent = iNumPlayers
iIndependent2 = iNumPlayers+1
iIndependent3 = iNumPlayers+2
iBarbarian = 51
iNumMajPlayers = 44
iNumMinorPlayers = 3
iNumTotalPlayers = 51

iNumCivilizations = 70
(iAntigonids, iSeleucids, iEgypt, iCarthage, iMauryans, iKalinka, iQin, iGojoseon, iNubia, iSaba, iPandyans, iPontus, iCelts, iRome, iVietnam, iTocharians, iBactria, 
iHan, iSatavahana, iArmenia, iMaccabees, iParthia, iDacia, iGoguryeo, iAxum, iKushans, iFunan, iJin, iSassanids, iYamato, iGupta, iByzantines, iVisigoths, iVandals, 
iOstrogoths, iFranks, iChalukyans, iLombards, iGokturks, iSrivajaya, iKhazars, iTibet, iTang, iArabs, iXiongnu, iNumidia, iScythians, iNanYue, iSungas, iMacedon, 
iMakuria, iHimyarites, iShu, iWu, iHephthalites, iXianbei, iHuns, iAvars, iRouran, iVakatakas, iSong, iMagadha, iRebelRome, iPallavas, iKalabhras, iSaxons, iWesternRome, 
iMoors, iChampa, iMinor) = range(iNumCivilizations)



# CIVILIZATION DATA for RiseAndFall

tCapitals = (
	(47,50), # 0 Pella, for Macedonian respawn
	(72,42), # 1 Seleucia
	(53,35), # 2 Alexandria
	(29, 40), # 3 Carthage
	(114,37), # 4 Pataliputra
	(112, 30), # 5 Singhapura
	(136, 50), # 6 Xian
	(153, 62), # 7 Liaodong
	(58, 21), # 8 Meroe
	(68, 21), # 9 Mariba
	(105, 17), # 10 Madurai
	(60, 52), # 11 Sinope
	(24, 60), # 12 Bibracte
	(35, 51), # 13 Rome
	(134, 34), # 14 Co Loa
	(106, 58), # 15 Kashgar
	(94, 50), # 16 Bactra
	(140, 50), # 17 Luoyang
	(103, 27), # 18 Pratishthana
	(71, 51), # 19 Artashat
	(62, 37), # 20 Jerusalem
	(82, 46), # 21 Hecatompylos
	(46, 59), # 22 Sarmizegetusa
	(156, 58), # 23 P'yongyang
	(62, 20), # 24 Axum
	(96, 47), # 25 Kapisa
	(135, 19), # 26 Khmer
	(140, 50), # 27 Luoyang
	(72, 42), # 28 Ctesiphon
	(166, 52), # 29 Yamato
	(114, 38), # 30 Pataliputra
	(53, 51), # 31 Constantinople
	(22, 55), # 32 Tolosa
	(29, 40), # 33 Carthage
	(32, 57), # 34 Mediolanum
	(28, 63), # 35 Metz
	(103, 25), # 36 Vatapi
	(32, 57), # 37 Mediolanum
	(135, 72), # 38 Karabalasagun
	(133,  6), # 39 Pelambang
	(73, 63), # 40 Atil
	(118, 44), # 41 Lhasa
	(139, 55), # 42 Taiyuan
	(67, 27), # 43 Mecca
	(135, 72), # Xiongnu
	(24, 40), # Numidians, Cirta
	(93, 35), # Sakas, Pattala
	(148, 39), # Min Yue
	(114, 38), # Pataliputra
	(47, 50), # Pella
	(58, 21), # Meroe
	(68, 21), # Mariba
	(131, 45), # Shu
	(148, 47), # Jianye
	(93, 54), # Hepthalites, Samarkand
	(135, 72), # Xianbei
	(40, 62), # Huns, Noricum
	(40, 62), # Avars, Noricum
	(106, 58), # Rouran, Kashgar
	(104, 27), # Vakataks, Pratishthana
	(146, 45), # Jianye
	(115, 38), # Pataliputra
	(35, 52), # Rome
	(109, 26), # Amaravati
	(105, 17), # Madurai
	(31, 68), # Saxons - Mimigernaford
	(35, 52), # Rome
	(35, 52), # Moors - Gadir for now
	(139, 21), # Champa
) 


# preferred capital if tCapital is not possible
tBackupCapitals = ( 
	(46,53), # 0 Pella, for Macedonian respawn
	(64, 46), # SEL Antioch
	(53,34), # 2 Alexandria
	(29, 40), # 3 Carthage
	(110,38), # 4 Varanasi
	(112, 30), # 5 Singhapura
	(139, 50), # 17 Luoyang
	(154, 63), # 7 Liaodong
	(58, 21), # 8 Meroe
	(68, 21), # 9 Mariba
	(105, 17), # 10 Madurai
	(61, 54), # 11 Sinope
	(23, 60), # 12 Bibracte
	(35, 52), # 13 Rome
	(134, 34), # 14 Co Loa
	(106, 58), # 15 Kashgar
	(94, 50), # 16 Bactra
	(146, 45), # Jianye
	(104, 27), # 18 Pratishthana
	(71, 52), # 19 Artashat
	(62, 37), # 20 Jerusalem
	(82, 46), # 21 Hecatompylos
	(45, 59), # 22 Sarmizegetusa
	(156, 58), # 23 P'yongyang
	(63, 20), # 24 Axum
	(95, 46), # 25 Kapisa
	(134, 24), # 26 Khmer
	(139, 50), # 27 Luoyang
	(72, 42), # 28 Ctesiphon
	(167, 52), # 29 Yamato
	(115, 38), # 30 Pataliputra
	(54,53), # 31 Constantinople
	(21, 55), # 32 Tolosa
	(29, 40), # 33 Carthage
	(32, 57), # 34 Mediolanum
	(28, 64), # 35 Metz
	(104, 25), # 36 Vatapi
	(32, 57), # 37 Mediolanum
	(134, 72), # 38 Karabalasagun
	(133,  6), # 39 Pelambang
	(73, 63), # 40 Atil
	(118, 44), # 41 Lhasa
	(139, 50), # 42 Luoyang
	(67, 27), # 43 Mecca
	(135, 72), # Xiongnu
	(24, 41), # Numidians, Cirta
	(93, 35), # Sakas, Pattala
	(148, 40), # Min Yue
	(115, 38), # Pataliputra
	(46, 53), # Pella
	(58, 21), # Meroe
	(68, 21), # Mariba
	(128, 45), # Shu
	(146, 45), # Jianye
	(93, 54), # Hepthalites, Samarkand
	(135, 72), # Xianbei
	(40, 62), # Huns, Noricum
	(40, 62), # Avars, Noricum
	(106, 58), # Rouran, Kashgar
	(104, 27), # Vakataks, Pratishthana
	(146, 45), # Jianye
	(115, 38), # Pataliputra
	(35, 52), # Rome
	(109, 26), # Amaravati
	(105, 17), # Madurai
	(31, 68), # Saxons - Mimigernaford
	(35, 52), # Rome
	(35, 52), # Moors - Gadir for now
	(-1, -1), # Champa
) 


# The AI will have its palace moved for free here
tNewCapitals = ( 
	(46,53), # 0 Pella, for Macedonian respawn
	(64, 46), # SEL Antioch
	(53,34), # 2 Alexandria
	(29, 40), # 3 Carthage
	(115, 38), # 4 Pataliputra
	(112, 30), # 5 Singhapura
	(134, 50), # 6 Xian
	(154, 63), # 7 Liaodong
	(58, 21), # 8 Meroe
	(68, 21), # 9 Mariba
	(105, 17), # 10 Madurai
	(61, 54), # 11 Sinope
	(23, 60), # 12 Bibracte
	(35, 52), # 13 Rome
	(134, 34), # 14 Co Loa
	(106, 58), # 15 Kashgar
	(100,46), # BAC - Taxila
	(139, 50), # 17 Luoyang
	(104, 27), # 18 Pratishthana
	(71, 52), # 19 Artashat
	(62, 37), # 20 Jerusalem
	(72, 42), # PAR - Ctesiphon
	(45, 59), # 22 Sarmizegetusa
	(156, 58), # 23 P'yongyang
	(63, 20), # 24 Axum
	(95, 46), # 25 Kapisa
	(134, 24), # 26 Khmer
	(139, 50), # 27 Luoyang
	(72, 42), # 28 Ctesiphon
	(167, 52), # 29 Yamato
	(115, 38), # 30 Pataliputra
	(54,53), # 31 Constantinople
	(21, 55), # 32 Tolosa
	(29, 40), # 33 Carthage
	(32, 57), # 34 Mediolanum
	(28, 64), # 35 Metz
	(104, 25), # 36 Vatapi
	(32, 57), # 37 Mediolanum
	(134, 72), # 38 Karabalasagun
	(133,  6), # 39 Pelambang
	(73, 63), # 40 Atil
	(118, 44), # 41 Lhasa
	(134, 50), # 6 Xian
	(65, 42), # ARA - Damascus
	(135, 72), # Xiongnu
	(24, 41), # Numidians, Cirta
	(93, 35), # Sakas, Pattala
	(148, 40), # Min Yue
	(115, 38), # Pataliputra
	(46, 53), # Pella
	(58, 21), # Meroe
	(68, 21), # Mariba
	(128, 45), # Shu
	(146, 45), # Jianye
	(93, 54), # Hepthalites, Samarkand
	(135, 72), # Xianbei
	(40, 62), # Huns, Noricum
	(40, 62), # Avars, Noricum
	(106, 58), # Rouran, Kashgar
	(104, 27), # Vakataks, Pratishthana
	(146, 45), # Jianye
	(115, 38), # Pataliputra
	(35, 52), # Rome
	(109, 26), # Amaravati
	(105, 17), # Madurai
	(31, 68), # Saxons - Mimigernaford
	(35, 52), # Rome
	(35, 52), # Moors - Gadir for now
	(-1, -1), # Champa
) # 

tBirth = (
	-321, #iAntigonids
	-321, #iSeleucids 
	-321, #iEgypt
	-321, #iCarthage 
	-321, #iMauryans 
	-321, #iKalinka 
	-321, #iQin
	-321, #iGojoseon 
	-315, #iNubia
	-305, #iSaba
	-300, #iPandyans
	-290, #iPontus
	-285, #iCelts
	-270, #iRome
	-260, #iVietnam
	-225, #iTocharians
	-220, #iBactria
	-210, #iHan
	-200, #iSatavahana
	-180, #iArmenia
	-160, #iMaccabees
	-140, #iParthia
	 -80, #iDacia
	 -30, #iGoguryeo
	  15, #iAxum
	  50, #iKushans
	 110, #iFunan
	 220, #iJin
	 225, #iSassanids
	 250, #iYamato
	 320, #iGupta
	 330, #iByzantines
	 420, #iVisigoths
	 430, #iVandals
	 475, #iOstrogoths
	 500, #iFranks
	 550, #iChalukyans
	 570, #iLombards
	 575, #iGokturks
	 600, #iSrivajaya
	 605, #iKhazars
	 610, #iTibet
	 620, #iTang
	 630, #iArabs
	-205, #iXiongnu
	-200, #Numidia
	 -90, #Scythians
	-180, #iNanYue
	-185, #iSungas
	-150, #iMacedon
	 600, #iMakuria
	 225, #iHimyarites
	 225, #iShu
	 225, #iWu
	 400, #iHephthalites
	  90, #iXianbei
	 425, #iHuns
	 560, #iAvars
	 410, #iRouran
	 225, #iVakataka
	 550, #iSong
	 100, #iMagadha
	-320, #iRebelRome
	 550, #iPallavas
	 250, #iKalabhras
	 490, #iSaxons
	 330, #iWestern Rome
	 710, #iMoors
	 190, #iChampa
	-320, #iMinor

)


#tPeakBegin = (
	  #-320, -320, -320, -320, -320, -320, -320, -320, -315,-305,-300,-295,-290,-280,-270, -260, -220, -210, -200,-180,-160, -140, -80, -30, 15, 50,150,220,225,250,320,330,500,550,590,600,605,610,620,630,710)
#	   ANT   SEL   EGY   CAR   MAU   KAL   QIN   GOJ   NUB  SAB  PAN  TOC  PON  CEL  ROM   VIE   BAC   HAN   SAT  ARM  MAC   PAR  DAC  GOG AXU KUS FUN JIN SAS YAM GUP BYZ FRA CHA GOK SRI KHA TIB TAN ARA GHA  NUM  SAK  NAN

#tPeakEnd = (
	  #-100, -100, -80, -100, -180, -100, -210, -100,-150,-305,-100,-100, -50,-150, 350, -260, -220,   50, -200,-180,-160,  150, -80, -30, 15, 50,150,220,225,250,500,600,500,550,590,600,605,610,620,630,710)
#	   ANT   SEL  EGY   CAR   MAU   KAL   QIN   GOJ  NUB  SAB  PAN  TOC  PON  CEL  ROM   VIE   BAC   HAN   SAT  ARM  MAC   PAR  DAC  GOG AXU KUS FUN JIN SAS YAM GUP BYZ FRA CHA GOK SRI KHA TIB TAN ARA GHA  NUM  SAK  NAN

tVictory = ( # for final score calculation
	1500,1500,1500,1250,1500,1500,1500,1500,1500,1500,1500,1500,1500,1500,1500,1500,1500,1500,1500,1500,1500,1500,1500,1500,1500,1500,1500,1500,1500,1500,1500,1500,1500,1500,1500,1500,1500,1500,1500,1500,1500,1500,1500,1500,1500)
#	 ANT  SEL  EGY  CAR  MAU  KAL  QIN  GOJ  NUB  SAB  PAN  TOC  PON  CEL  ROM  VIE  BAC  HAN  SAT  ARM  MAC  PAR  DAC  GOG  AXU  KUS  FUN  JIN  SAS  YAM  GUP  BYZ  FRA  CHA  GOK  SRI  KHA  TIB  TAN  ARA  GHA  NUM  SAK  NAN

tDifference = ( # for not allowing new civ popup if too close
	 13,  12,  11,  10,   9,   8,   7,   6,   5,   4,   4,   4,   3,   1,   1,   2,   2,   2,   1,   2,   1,  1,   0,   1,   1,   0,   0,   1,   0,   0,   1,   3,   3,   2,   1,   0,   0,   0,   0,   0,   0,  0,  0,  0,  0)
#	ANT  SEL  EGY  CAR  MAU  KAL  QIN  GOJ  NUB  SAB  PAN  PON  CEL  ROM  VIE  TOC  BAC  HAN  SAT  ARM  MAC  PAR  DAC  GOG AXU  KUS  FUN  JIN  SAS  YAM  GUP  BYZ  VIS  VAN  OST  FRA  CHA  LOM  GOK  SRI  KHA TIB TAN ARA GHA

tRespawnCutoff = (
    -200,   0,   0,   0, 100,   0,-180,   0,300, 100,   0,   0,   0, 420,   0,   0,   0, 185,   0,   0,  70, 426, 480,   0,   0,   0,   0,   1,   1,   1,   0,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0)
#	 ANT  SEL  EGY  CAR  MAU  KAL  QIN  GOJ NUB  SAB  PAN  TOC  PON  CEL  ROM  VIE  BAC  HAN  SAT  ARM  MAC  PAR  DAC  GOG  AXU  KUS  FUN  JIN  SAS  YAM  GUP  BYZ  FRA  CHA  GOK  SRI  KHA  TIB  TAN  ARA  GHA  NUM  SAK  NAN

#t2ndRespawn = (
       #0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0)
#	 ANT  SEL  EGY  CAR  MAU  KAL  QIN  GOJ  NUB  SAB  PAN  TOC  PON  CEL  ROM  VIE  BAC  HAN  SAT  ARM  MAC  PAR  DAC  GOG  AXU  KUS  FUN  JIN  SAS  YAM  GUP  BYZ  FRA  CHA  GOK  SRI  KHA  TIB  TAN  ARA  GHA    NUM  SAK  NAN

tFall = ( # a bit of determinism: no resurrection & stability penalty (if negative) beyond this point
	-150, #iAntigonids 0
	 -50, #iSeleucids 1
	  50, #iEgypt 2
	 -60, #iCarthage 3 
	-180, #iMauryans 4
	 100, #iKalinka 5
	-210, #iQin 6
	-100, #iGojoseon 7 
	 100, #iNubia 8
	 100, #iSaba 9
	 200, #iPandyans 10
	 100, #iPontus 11
	  50, #iCelts 12
	 460, #iRome 13
	 100, #iVietnam 14
	  50, #iTocharians 15
	 -50, #iBactria 16
	 150, #iHan 17
	 100, #iSatavahana 18
	 200, #iArmenia 19
	 -80, #iMaccabees 20
	 200, #iParthia 21
	 150, #iDacia 22
	1000, #iGoguryeo 23
	 300, #iAxum 24
	 350, #iKushans 25
	 300, #iFunan 26
	 350, #iJin 27
	 630, #iSassanids 28
	1000, #iYamato 29
	 550, #iGupta 30
	1000, #iByzantines 31
	 700, #iVisigoths 32
	 530, #iVandals 33
	 570, #iOstrogoths 34
	1000, #iFranks 35
	 800, #iChalukyans 36
	 800, #iLombards 37
	 800, #iGokturks 38
	 800, #iSrivajaya
	 800, #iKhazars
	1000, #iTibet
	 800, #iTang
	 800, #iArabs
	  50, #iXiongnu
	  50, #iNumidia
	 100, #iScythians
	 100, #iNanYue
	-100, #iSungas
	-100, #iMacedon
	1000, #iMakuria
	 600, #iHimyarites
	 600, #iShu
	 600, #iWu
	 550, #iHephthalites
	 300, #iXianbei
	 450, #iHuns
	 800, #iAvars
	 700, #iRouran
	 800, #iVakataka
	 800, #iSong
	 500, #iMagadha
	 250, #iRebelRome
	 800, #iPallavas
	 800, #iKalabhras
	 900, #iSaxons
	 800, #iWestern Rome
	 900, #iMoors
	 900  #iChampa
	#iMinor
)

tStabilityHandicap = ( 
 0, #iAntigonids
 0, #iSeleucids 
 0, #iEgypt
 0, #iCarthage 
 0, #iMauryans 
 0, #iKalinka 
 0, #iQin
 0, #iGojoseon 
 0, #iNubia
 0, #iSaba
 0, #iPandyans
 0, #iPontus
 0, #iCelts
 0, #iRome
 0, #iVietnam
 0, #iTocharians
 0, #iBactria
 0, #iHan
 0, #iSatavahana
 0, #iArmenia
 0, #iMaccabees
 0, #iParthia
 0, #iDacia
 0, #iGoguryeo
 0, #iAxum
 0, #iKushans
 0, #iFunan
 0, #iJin
 0, #iSassanids
 0, #iYamato
 0, #iGupta
 0, #iByzantines
 0, #iVisigoths
 0, #iVandals
 0, #iOstrogoths
 0, #iFranks
 0, #iChalukyans
 0, #iLombards
 0, #iGokturks
 0, #iSrivajaya
 0, #iKhazars
 0, #iTibet
 0, #iTang
 0, #iArabs
 0, #iXiongnu
 0, #iNumidia
 0, #iScythians
 0, #iNanYue
 0, #iSungas
 0, #iMacedon
 0, #iMakuria
 0, #iHimyarites
 0, #iShu
 0, #iWu
 0, #iHephthalites
 0, #iXianbei
 0, #iHuns
 0, #iAvars
 0, #iRouran
 0, #iVakataka
 0, #iSong
 0, #iMagadha
 0, #iRebelRome
 0, #iPallavas
 0, #iKalabhras
 0, #iSaxons
 0, #iWesternRome
 0, #iMoors
 0  #iChampa
#iMinor
)

#tFallRespawned = ( # slight changes for respawned civs
   #1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000)
#	ANT  SEL  EGY  CAR  MAU  KAL  QIN  GOJ  NUB  SAB  PAN  TOC  PON  CEL  ROM  VIE  BAC  HAN  SAT  ARM  MAC  PAR  DAC  GOG  AXU  KUS  FUN  JIN  SAS  YAM  GUP  BYZ  FRA  CHA  GOK  SRI  KHA  TIB  TAN  ARA  GHA  NUM  SAK  NAN

tNoSettler = (
	  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0,   0,   1,   0,   1,   1,   0,   1,   0,   0,   1,   1,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0)
#	ANT  SEL  EGY  CAR  MAU  KAL  QIN  GOJ  NUB  SAB  PAN  PON  CEL  ROM  VIE  TOC  BAC  HAN  SAT  ARM  MAC  PAR  DAC  GOG  AXU  KUS  FUN  JIN  SAS  YAM  GUP  BYZ  VIS  VAN  OST  FRA  CHA  LOM  GOK  SRI  KHA  TIB  TAN  ARA

tStartingGold = (
	 200, 300, 200, 200, 300, 100, 100, 100,  50,  50,  50,  50, 150, 300,  50, 100, 100, 300, 100, 100, 100, 300, 200, 100, 100, 200, 100, 200, 300, 100, 100, 200, 100, 100, 100, 100, 100, 100, 200, 100, 100, 100, 100, 500, 100, 100, 100, 100, 100, 100, 100)
#	 ANT  SEL  EGY  CAR  MAU  KAL  QIN  GOJ  NUB  SAB  PAN  PON  CEL  ROM  VIE  TOC  BAC  HAN  SAT  ARM  MAC  PAR  DAC  GOG  AXU  KUS  FUN  JIN  SAS  YAM  GUP  BYZ  VIS  VAN  OST  FRA  CHA  LOM  GOK  SRI  KHA  TIB  TAN  ARA  GHA  NUM  SAK  NAN  IN1  IN2  IN3

t80BCGold = (
	   0,   0,   0,   0,   0,   0,   0,   0,  50,  50,  50,  50, 150, 300, 300, 100, 100, 300, 100, 100, 100, 300, 200, 100, 100, 100, 100, 200, 300, 100, 100, 200, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 500, 100, 100, 100, 100, 100, 100, 100)
#	 ANT  SEL  EGY  CAR  MAU  KAL  QIN  GOJ  NUB  SAB  PAN  PON  CEL  ROM  VIE  TOC  BAC  HAN  SAT  ARM  MAC  PAR  DAC  GOG  AXU  KUS  FUN  JIN  SAS  YAM  GUP  BYZ  VIS  VAN  OST  FRA  CHA  LOM  GOK  SRI  KHA  TIB  TAN  ARA  GHA  NUM  SAK  NAN  IN1  IN2  IN3

t220ADGold = (
	   0,   0,   0,   0,   0,   0,   0,   0,  50,  50,  50,  50, 150, 900,  50, 100, 100, 300, 100, 100, 100, 300, 200, 100, 100, 100, 100, 200, 300, 100, 100, 200, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 500, 100, 100, 100, 100, 100, 100, 100)
#	 ANT  SEL  EGY  CAR  MAU  KAL  QIN  GOJ  NUB  SAB  PAN  PON  CEL  ROM  VIE  TOC  BAC  HAN  SAT  ARM  MAC  PAR  DAC  GOG  AXU  KUS  FUN  JIN  SAS  YAM  GUP  BYZ  VIS  VAN  OST  FRA  CHA  LOM  GOK  SRI  KHA  TIB  TAN  ARA  GHA  NUM  SAK  NAN  IN1  IN2  IN3

t550ADGold = (
	   0,   0,   0,   0,   0,   0,   0,   0,  50,  50,  50,  50, 150, 900,  50, 100, 100, 300, 100, 100, 100, 300, 200, 100, 100, 100, 100, 200, 300, 100, 100, 200, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 500, 100, 100, 100, 100, 100, 100, 100)
#	 ANT  SEL  EGY  CAR  MAU  KAL  QIN  GOJ  NUB  SAB  PAN  PON  CEL  ROM  VIE  TOC  BAC  HAN  SAT  ARM  MAC  PAR  DAC  GOG  AXU  KUS  FUN  JIN  SAS  YAM  GUP  BYZ  VIS  VAN  OST  FRA  CHA  LOM  GOK  SRI  KHA  TIB  TAN  ARA  GHA  NUM  SAK  NAN  IN1  IN2  IN3

tResurrectionProb = (
	 50,   0,   0,   0,  50,  50,   0,  50,  50,  50,  50,   0,   0,  50,  50,  50,   0,   0,   0,  50,  50,  50,   0,  50,  50,   0,  50,   0,  50,  50,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0)
#	ANT  SEL  EGY  CAR  MAU  KAL  QIN  GOJ  NUB  SAB  PAN  PON  CEL  ROM  VIE  TOC  BAC  HAN  SAT  ARM  MAC  PAR  DAC  GOG  AXU  KUS  FUN  JIN  SAS  YAM  GUP  BYZ  VIS  VAN  OST  FRA  CHA  LOM  GOK  SRI  KHA  TIB  TAN  ARA

tAIStopBirthThreshold = (
	 80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100)
#	ANT  SEL  EGY  CAR  MAU  KAL  QIN  GOJ  NUB  SAB  PAN  TOC  PON  CEL  ROM  VIE  BAC  HAN  SAT  ARM  MAC  PAR  DAC  GOG  AXU  KUS  FUN  JIN  SAS  YAM  GUP  BYZ  FRA  CHA  GOK  SRI  KHA  TIB  TAN  ARA  GHA  IN1  IN2  IN3  IN4  ---  ---  ---  ---  ---  BAR

tReligiousTolerance = ( # 80: zoroastrians, 60: jews, 50: muslims/christians/hindu+buddhism, 10: catholic/orthodox, islam
	 80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100)
#	ANT  SEL  EGY  CAR  MAU  KAL  QIN  GOJ  NUB  SAB  PAN  PON  CEL  ROM  VIE  TOC  BAC  HAN  SAT  ARM  MAC  PAR  DAC  GOG  AXU  KUS  FUN  JIN  SAS  YAM  GUP  BYZ  FRA  CHA  GOK  SRI  KHA  TIB  TAN  ARA  GHA  IN1  IN2  IN3  IN4  ---  ---  ---  ---  ---  BAR

tHire = ( # Mercenaries (more = higher chance)
	 50,  50,  50,  50,  50,  50,  50,  50,  50,  50,  50,  50,  50,  50,  50,  50,  50,  50,  50,  50,  50,  50,  50,  50,  50,  50,  50,  50,  50,  50,  50,  50,  50,  50,  50,  50,  50,  50,  50,  50,  50,  50,  50,  50,  50,  50,  50,  50)
#	ANT  SEL  EGY  CAR  MAU  KAL  QIN  GOJ  NUB  SAB  PAN  PON  CEL  ROM  VIE  TOC  BAC  HAN  SAT  ARM  MAC  PAR  DAC  GOG  AXU  KUS  FUN  JIN  SAS  YAM  GUP  BYZ  VIS  VAN  OST  FRA  CHA  LOM  GOK  SRI  KHA  TIB  TAN  ARA  GHA  NO1  NO2  NO3

tEmpire = ( # max number of cities before stability penalty
	 8,   12,   5,   6,   8,   5,  10,   3,   3,   3,   4,   4,   4,   6,  15,   4,   7,  10,   6,   4,   2,  10,   5,   8,   5,  10,   5,  10,  12,   6,   8,  10,   8,   7,  10,   8,   8,   7,  13,  14,   4)
#	ANT  SEL  EGY  CAR  MAU  KAL  QIN  GOJ  NUB  SAB  PAN  TOC  PON  CEL  ROM  VIE  BAC  HAN  SAT  ARM  MAC  PAR  DAC  GOG  AXU  KUS  FUN  JIN  SAS  YAM  GUP  BYZ  FRA  CHA  GOK  SRI  KHA  TIB  TAN  ARA  GHA

#tAggression = ( # 0 = passive, 1 = normal, 2 = agressive
#	 1,    2,   1,   1,   2,   2,   2,   1,   1,   0,   0,   0,   1,   2,   0,   0,   1,   1,   1,   1,   1,   1,   2,   1,   1,   1,   1,   0,   1,   2,   1,   1,   1,   2,   1,   1,   1,   2,   1,   2,   1,   1,   1,   2,   2,   1,   2,   2)
#	ANT  SEL  EGY  CAR  MAU  KAL  QIN  GOJ  NUB  SAB  PAN  PON  CEL  ROM  VIE  TOC  BAC  HAN  SAT  ARM  MAC  PAR  DAC  GOG  AXU  KUS  FUN  JIN  SAS  YAM  GUP  BYZ  VIS  VAN  OST  FRA  CHA  LOM  GOK  SRI  KHA  TIB  TAN  ARA  GHA  NUM  SAK  NAN

tAggression = ( # 0 = passive, 1 = normal, 2 = agressive
	1, #iAntigonids 0
	2, #iSeleucids 1
	1, #iEgypt 2
	1, #iCarthage 3 
	1, #iMauryans 4
	1, #iKalinka 5
	2, #iQin 6
	1, #iGojoseon 7 
	1, #iNubia 8
	0, #iSaba 9
	0, #iPandyans 10
	0, #iPontus 11
	1, #iCelts 12
	2, #iRome 13
	1, #iVietnam 14
	0, #iTocharians 15
	1, #iBactria 16
	1, #iHan 17
	1, #iSatavahana 18
	1, #iArmenia 19
	1, #iMaccabees 20
	2, #iParthia 21
	1, #iDacia 22
	1, #iGoguryeo 23
	1, #iAxum 24
	1, #iKushans 25
	0, #iFunan 26
	1, #iJin 27
	1, #iSassanids 28
	1, #iYamato 29
	1, #iGupta 30
	1, #iByzantines 31
	1, #iVisigoths 32
	2, #iVandals 33
	1, #iOstrogoths 34
	1, #iFranks 35
	1, #iChalukyans 36
	1, #iLombards 37
	2, #iGokturks 38
	1, #iSrivajaya
	1, #iKhazars
	1, #iTibet
	2, #iTang
	2, #iArabs
	2, #iXiongnu
	1, #iNumidia
	2, #iScythians
	1, #iNanYue
	1, #iSungas
	1, #iMacedon
	1, #iMakuria
	0, #iHimyarites
	2, #iShu
	2, #iWu
	2, #iHephthalites
	2, #iXianbei
	2, #iHuns
	2, #iAvars
	2, #iRouran
	1, #iVakataka
	1, #iSong
	1, #iMagadha
	2, #iRebelRome
	1, #iPallavas
	2, #iKalabhras
	2, #iSaxons
	1, #iWestern Rome
	1, #iMoors
	1  #iChampa
	#iMinor
)


tGoals = (
( # Normal
("TXT_KEY_UHV_ANT1", "TXT_KEY_UHV_ANT2", "TXT_KEY_UHV_ANT3"),
("TXT_KEY_UHV_SEL1", "TXT_KEY_UHV_SEL2", "TXT_KEY_UHV_SEL3"),
("TXT_KEY_UHV_EGY1", "TXT_KEY_UHV_EGY2", "TXT_KEY_UHV_EGY3"),
("TXT_KEY_UHV_CAR1", "TXT_KEY_UHV_CAR2", "TXT_KEY_UHV_CAR3"),
("TXT_KEY_UHV_MAU1", "TXT_KEY_UHV_MAU2", "TXT_KEY_UHV_MAU3"),
("TXT_KEY_UHV_KAL1", "TXT_KEY_UHV_KAL2", "TXT_KEY_UHV_KAL3"),
("TXT_KEY_UHV_QIN1", "TXT_KEY_UHV_QIN2", "TXT_KEY_UHV_QIN3"),
("TXT_KEY_UHV_GOJ1", "TXT_KEY_UHV_GOJ2", "TXT_KEY_UHV_GOJ3"),
("TXT_KEY_UHV_NUB1", "TXT_KEY_UHV_NUB2", "TXT_KEY_UHV_NUB3"),
("TXT_KEY_UHV_SAB1", "TXT_KEY_UHV_SAB2", "TXT_KEY_UHV_SAB3"),
("TXT_KEY_UHV_PAN1", "TXT_KEY_UHV_PAN2", "TXT_KEY_UHV_PAN3"),
("TXT_KEY_UHV_PON1", "TXT_KEY_UHV_PON2", "TXT_KEY_UHV_PON3"),
("TXT_KEY_UHV_CEL1", "TXT_KEY_UHV_CEL2", "TXT_KEY_UHV_CEL3"),
("TXT_KEY_UHV_ROM1", "TXT_KEY_UHV_ROM2", "TXT_KEY_UHV_ROM3"),
("TXT_KEY_UHV_VIE1", "TXT_KEY_UHV_VIE2", "TXT_KEY_UHV_VIE3"),
("TXT_KEY_UHV_TOC1", "TXT_KEY_UHV_TOC2", "TXT_KEY_UHV_TOC3"),
("TXT_KEY_UHV_BAC1", "TXT_KEY_UHV_BAC2", "TXT_KEY_UHV_BAC3"),
("TXT_KEY_UHV_HAN1", "TXT_KEY_UHV_HAN2", "TXT_KEY_UHV_HAN3"),
("TXT_KEY_UHV_SAT1", "TXT_KEY_UHV_SAT2", "TXT_KEY_UHV_SAT3"),
("TXT_KEY_UHV_ARM1", "TXT_KEY_UHV_ARM2", "TXT_KEY_UHV_ARM3"),
("TXT_KEY_UHV_MAC1", "TXT_KEY_UHV_MAC2", "TXT_KEY_UHV_MAC3"),
("TXT_KEY_UHV_PAR1", "TXT_KEY_UHV_PAR2", "TXT_KEY_UHV_PAR3"),
("TXT_KEY_UHV_DAC1", "TXT_KEY_UHV_DAC2", "TXT_KEY_UHV_DAC3"),
("TXT_KEY_UHV_GOG1", "TXT_KEY_UHV_GOG2", "TXT_KEY_UHV_GOG3"),
("TXT_KEY_UHV_AXU1", "TXT_KEY_UHV_AXU2", "TXT_KEY_UHV_AXU3"),
("TXT_KEY_UHV_KUS1", "TXT_KEY_UHV_KUS2", "TXT_KEY_UHV_KUS3"),
("TXT_KEY_UHV_FUN1", "TXT_KEY_UHV_FUN2", "TXT_KEY_UHV_FUN3"),
("TXT_KEY_UHV_JIN1", "TXT_KEY_UHV_JIN2", "TXT_KEY_UHV_JIN3"),
("TXT_KEY_UHV_SAS1", "TXT_KEY_UHV_SAS2", "TXT_KEY_UHV_SAS3"),
("TXT_KEY_UHV_YAM1", "TXT_KEY_UHV_YAM2", "TXT_KEY_UHV_YAM3"),
("TXT_KEY_UHV_GUP1", "TXT_KEY_UHV_GUP2", "TXT_KEY_UHV_GUP3"),
("TXT_KEY_UHV_BYZ1", "TXT_KEY_UHV_BYZ2", "TXT_KEY_UHV_BYZ3"),
("TXT_KEY_UHV_VIS1", "TXT_KEY_UHV_VIS2", "TXT_KEY_UHV_VIS3"),
("TXT_KEY_UHV_VAN1", "TXT_KEY_UHV_VAN2", "TXT_KEY_UHV_VAN3"),
("TXT_KEY_UHV_OST1", "TXT_KEY_UHV_OST2", "TXT_KEY_UHV_OST3"),
("TXT_KEY_UHV_FRA1", "TXT_KEY_UHV_FRA2", "TXT_KEY_UHV_FRA3"),
("TXT_KEY_UHV_CHA1", "TXT_KEY_UHV_CHA2", "TXT_KEY_UHV_CHA3"),
("TXT_KEY_UHV_LOM1", "TXT_KEY_UHV_LOM2", "TXT_KEY_UHV_LOM3"),
("TXT_KEY_UHV_GOK1", "TXT_KEY_UHV_GOK2", "TXT_KEY_UHV_GOK3"),
("TXT_KEY_UHV_SRI1", "TXT_KEY_UHV_SRI2", "TXT_KEY_UHV_SRI3"),
("TXT_KEY_UHV_KHA1", "TXT_KEY_UHV_KHA2", "TXT_KEY_UHV_KHA3"),
("TXT_KEY_UHV_TIB1", "TXT_KEY_UHV_TIB2", "TXT_KEY_UHV_TIB3"),
("TXT_KEY_UHV_TAN1", "TXT_KEY_UHV_TAN2", "TXT_KEY_UHV_TAN3"),
("TXT_KEY_UHV_ARA1", "TXT_KEY_UHV_ARA2", "TXT_KEY_UHV_ARA3"),
("TXT_KEY_UHV_GHA1", "TXT_KEY_UHV_GHA2", "TXT_KEY_UHV_GHA3"),),
( # Epic
("TXT_KEY_UHV_ANT1", "TXT_KEY_UHV_ANT2", "TXT_KEY_UHV_ANT3"),
("TXT_KEY_UHV_SEL1", "TXT_KEY_UHV_SEL2", "TXT_KEY_UHV_SEL3"),
("TXT_KEY_UHV_EGY1", "TXT_KEY_UHV_EGY2", "TXT_KEY_UHV_EGY3"),
("TXT_KEY_UHV_CAR1", "TXT_KEY_UHV_CAR2", "TXT_KEY_UHV_CAR3"),
("TXT_KEY_UHV_MAU1", "TXT_KEY_UHV_MAU2", "TXT_KEY_UHV_MAU3"),
("TXT_KEY_UHV_KAL1", "TXT_KEY_UHV_KAL2", "TXT_KEY_UHV_KAL3"),
("TXT_KEY_UHV_QIN1", "TXT_KEY_UHV_QIN2", "TXT_KEY_UHV_QIN3"),
("TXT_KEY_UHV_GOJ1", "TXT_KEY_UHV_GOJ2", "TXT_KEY_UHV_GOJ3"),
("TXT_KEY_UHV_NUB1", "TXT_KEY_UHV_NUB2", "TXT_KEY_UHV_NUB3"),
("TXT_KEY_UHV_SAB1", "TXT_KEY_UHV_SAB2_EPIC", "TXT_KEY_UHV_SAB3_EPIC"),
("TXT_KEY_UHV_PAN1", "TXT_KEY_UHV_PAN2", "TXT_KEY_UHV_PAN3"),
("TXT_KEY_UHV_PON1", "TXT_KEY_UHV_PON2", "TXT_KEY_UHV_PON3"),
("TXT_KEY_UHV_CEL1", "TXT_KEY_UHV_CEL2", "TXT_KEY_UHV_CEL3"),
("TXT_KEY_UHV_ROM1", "TXT_KEY_UHV_ROM2", "TXT_KEY_UHV_ROM3"),
("TXT_KEY_UHV_VIE1", "TXT_KEY_UHV_VIE2", "TXT_KEY_UHV_VIE3"),
("TXT_KEY_UHV_TOC1", "TXT_KEY_UHV_TOC2", "TXT_KEY_UHV_TOC3"),
("TXT_KEY_UHV_BAC1", "TXT_KEY_UHV_BAC2", "TXT_KEY_UHV_BAC3_EPIC"),
("TXT_KEY_UHV_HAN1", "TXT_KEY_UHV_HAN2", "TXT_KEY_UHV_HAN3"),
("TXT_KEY_UHV_SAT1", "TXT_KEY_UHV_SAT2_EPIC", "TXT_KEY_UHV_SAT3"),
("TXT_KEY_UHV_ARM1", "TXT_KEY_UHV_ARM2", "TXT_KEY_UHV_ARM3"),
("TXT_KEY_UHV_MAC1", "TXT_KEY_UHV_MAC2", "TXT_KEY_UHV_MAC3"),
("TXT_KEY_UHV_PAR1", "TXT_KEY_UHV_PAR2", "TXT_KEY_UHV_PAR3"),
("TXT_KEY_UHV_DAC1", "TXT_KEY_UHV_DAC2_EPIC", "TXT_KEY_UHV_DAC3"),
("TXT_KEY_UHV_GOG1", "TXT_KEY_UHV_GOG2", "TXT_KEY_UHV_GOG3"),
("TXT_KEY_UHV_AXU1", "TXT_KEY_UHV_AXU2", "TXT_KEY_UHV_AXU3_EPIC"),
("TXT_KEY_UHV_KUS1", "TXT_KEY_UHV_KUS2", "TXT_KEY_UHV_KUS3"),
("TXT_KEY_UHV_FUN1", "TXT_KEY_UHV_FUN2", "TXT_KEY_UHV_FUN3"),
("TXT_KEY_UHV_JIN1", "TXT_KEY_UHV_JIN2", "TXT_KEY_UHV_JIN3"),
("TXT_KEY_UHV_SAS1", "TXT_KEY_UHV_SAS2", "TXT_KEY_UHV_SAS3"),
("TXT_KEY_UHV_YAM1", "TXT_KEY_UHV_YAM2", "TXT_KEY_UHV_YAM3"),
("TXT_KEY_UHV_GUP1", "TXT_KEY_UHV_GUP2", "TXT_KEY_UHV_GUP3"),
("TXT_KEY_UHV_BYZ1", "TXT_KEY_UHV_BYZ2", "TXT_KEY_UHV_BYZ3"),
("TXT_KEY_UHV_VIS1", "TXT_KEY_UHV_VIS2", "TXT_KEY_UHV_VIS3_EPIC"),
("TXT_KEY_UHV_VAN1_EPIC", "TXT_KEY_UHV_VAN2", "TXT_KEY_UHV_VAN3_EPIC"),
("TXT_KEY_UHV_OST1", "TXT_KEY_UHV_OST2", "TXT_KEY_UHV_OST3"),
("TXT_KEY_UHV_FRA1", "TXT_KEY_UHV_FRA2", "TXT_KEY_UHV_FRA3"),
("TXT_KEY_UHV_CHA1", "TXT_KEY_UHV_CHA2", "TXT_KEY_UHV_CHA3"),
("TXT_KEY_UHV_LOM1", "TXT_KEY_UHV_LOM2", "TXT_KEY_UHV_LOM3"),
("TXT_KEY_UHV_GOK1", "TXT_KEY_UHV_GOK2", "TXT_KEY_UHV_GOK3"),
("TXT_KEY_UHV_SRI1", "TXT_KEY_UHV_SRI2", "TXT_KEY_UHV_SRI3"),
("TXT_KEY_UHV_KHA1", "TXT_KEY_UHV_KHA2", "TXT_KEY_UHV_KHA3"),
("TXT_KEY_UHV_TIB1", "TXT_KEY_UHV_TIB2", "TXT_KEY_UHV_TIB3"),
("TXT_KEY_UHV_TAN1", "TXT_KEY_UHV_TAN2", "TXT_KEY_UHV_TAN3"),
("TXT_KEY_UHV_ARA1", "TXT_KEY_UHV_ARA2", "TXT_KEY_UHV_ARA3"),
("TXT_KEY_UHV_GHA1_EPIC", "TXT_KEY_UHV_GHA2", "TXT_KEY_UHV_GHA3_EPIC"),
),
)


tRomanGoals = (
( # Epic
("TXT_KEY_UHV_ROM4", "TXT_KEY_UHV_ROM5", "TXT_KEY_UHV_ROM6"),
("TXT_KEY_UHV_ROM7", "TXT_KEY_UHV_ROM8", "TXT_KEY_UHV_ROM9"),
),
( # Normal
("TXT_KEY_UHV_ROM4", "TXT_KEY_UHV_ROM5", "TXT_KEY_UHV_ROM6"),
("TXT_KEY_UHV_ROM7", "TXT_KEY_UHV_ROM8", "TXT_KEY_UHV_ROM9"),
)
) 


lContactCivsOnSpawn = [
	[iEgypt], # Antigonids
	[], # Seleucids
	[iAntigonids, iCarthage], # Egypt
	[iEgypt], # Carthage
	[], # Mauryans
	[], # Kalinka
	[], # Qin
	[], # Gojoseon
	[], # Nubia
	[], # Saba
	[], # Pandyans
	[], # Pontus
	[], # Celts
	[iEgypt, iAntigonids, iCarthage, iSeleucids], # Rome
	[], # Vietnam
	[], # Tocharians
	[iSeleucids], # Bactria
	[], # Han
	[], # Satavahana
	[], # Armenia
	[], # Maccabees
	[], # Parthia
	[], # Dacia
	[iQin, iHan, iJin], # Goguryeo
	[], # Axum
	[], # Kushans
	[], # Funan
	[], # Jin
	[], # Sassanids
	[], # Yamato
	[], # Gupta
	[iRome, iArmenia, iAxum, iSaba], # Byzantines
	[iRome, iByzantines], # Visigoths
	[iRome, iByzantines], # Vandals
	[iRome, iByzantines], # Ostrogoths
	[iRome, iByzantines], # Franks
	[], # Chalukyans
	[], # Lombards
	[], # Gokturks
	[], # Srivajaya
	[], # Khazars
	[], # Tibet
	[], # Tang
	[], # Arabs
	[], # Xiongnu
	[], # Numidia
	[iParthia, iTocharians, iSatavahana, iBactria], # Scythians
	[iQin, iHan, iVietnam], # Nan Yue
	[], # Pataliputra
	[], # Pella
	[], # Meroe
	[], # Mariba
	[], # Madurai
	[], # Khmer
	[], # Shu
	[], # Jianye
	[], # Hepthalites
	[], # Xianbei
	[], # Huns
	[], # Avars
	[], # Rouran
	[], # Vakataka
	[], # Song
	[], # Magadha
	[], # Rebel Rome
	[], # Pallavas
	[], # Kalabhras
	[], # Saxons
	[], # Western Rome
	[iArabs], # Moors
	[], # Champa
]

#guaranteed war on spawn
lEnemyCivsOnSpawn = [
	[], # Antigonids
	[], # Seleucids
	[], # Egypt
	[], # Carthage
	[], # Mauryans
	[], # Kalinka
	[], # Qin
	[], # Gojoseon
	[], # Nubia
	[], # Saba
	[], # Pandyans
	[], # Pontus
	[], # Celts
	[], # Rome
	[], # Vietnam
	[], # Tocharians
	[], # Bactria
	[iQin], # Han
	[iMauryans], # Satavahana
	[], # Armenia
	[], # Maccabees
	[iSeleucids], # Parthia
	[iRome], # Dacia
	[], # Goguryeo
	[iSaba], # Axum
	[iBactria, iScythians], # Kushans
	[], # Funan
	[iHan, iQin], # Jin
	[iParthia, iSeleucids], # Sassanids
	[iGoguryeo], # Yamato
	[], # Gupta
	[], # Byzantines
	[], # Visigoths
	[], # Ostrogoths
	[iRome, iByzantines, iVisigoths], # Vandals
	[], # Franks
	[iGupta], # Chalukyans
	[iFranks, iVisigoths, iOstrogoths], # Lombards
	[], # Gokturks
	[], # Srivajaya
	[], # Khazars
	[], # Tibet
	[iHan, iJin, iQin], # Tang
	[iRome, iSassanids, iEgypt, iByzantines, iSaba], # Arabs
	[iQin, iHan], # Xiongnu
	[], # Numidia
	[iParthia, iTocharians, iSatavahana, iBactria], # Scythians
	[iQin, iHan, iVietnam], # Nan Yue
	[], # Sungas
	[], # Macedon
	[], # Makuria
	[], # Himyar
	[iJin, iHan], # Shu
	[iJin, iQin], # Wu
	[iSassanids, iTocharians, iGupta], # Hepthalites
	[iQin, iHan], # Xianbei
	[iRome, iByzantines], # Huns
	[], # Avars
	[], # Rouran
	[], # Vakataka
	[], # Song
	[], # Magadha
	[], # Rebel Rome
	[], # Pallavas
	[], # Kalabhras
	[iFranks], # Saxons
	[], # Western Rome
	[iVisigoths, iVandals, iRome], # Moors
	[], # Champa
]



#neighbours
lNeighbours = [
	[iEgypt, iSeleucids, iMaccabees, iRome, iDacia], # Antigonids
	[iEgypt, iParthia, iBactria, iSassanids, iArabs, iMaccabees], # Seleucids
	[iNubia, iSeleucids, iMaccabees], # Egypt
	[iRome], # Carthage
	[iSatavahana, iPandyans, iBactria, iKushans, iParthia, iSassanids, iGupta, iChalukyans], # Mauryans
	[], # Kalinka
	[iTocharians, iGoguryeo, iYamato, iFunan], # Qin
	[], # Gojoseon
	[iEgypt, iAxum, iSaba], # Nubia
	[iAxum, iArabs, iMaccabees], # Saba
	[iSatavahana, iMauryans, iGupta, iChalukyans], # Pandyans
	[], # Pontus
	[iRome], # Celts
	[iCelts, iCarthage], # Rome
	[iHan, iFunan, iTibet], # Vietnam
	[], # Tocharians
	[iSeleucids, iKushans, iMauryans, iParthia, iSassanids], # Bactria
	[iGoguryeo, iYamato, iFunan], # Han
	[iMauryans, iGupta, iChalukyans, iPandyans], # Satavahana
	[iSeleucids, iParthia, iSassanids], # Armenia
	[iEgypt, iSeleucids, iArmenia, iParthia], # Maccabees
	[iSeleucids, iArmenia, iSassanids, iBactria], # Parthia
	[iRome], # Dacia
	[iHan, iJin, iTang], # Goguryeo
	[iNubia, iSaba], # Axum
	[iSeleucids, iBactria, iSatavahana, iParthia, iSassanids, iMauryans], # Kushans
	[iHan, iJin, iTang], # Funan
	[iGoguryeo, iFunan], # Jin
	[iSeleucids, iParthia, iBactria, iArabs], # Sassanids
	[iGoguryeo], # Yamato
	[iSatavahana, iPandyans, iBactria, iKushans, iMauryans, iChalukyans], # Gupta
	[iCelts, iCarthage, iSassanids], # Byzantines
	[iRome, iOstrogoths, iVandals, iFranks], # Visigoths
	[iRome, iByzantines, iVisigoths], # Ostrogoths
	[iRome, iVisigoths, iByzantines], # Vandals
	[iRome, iCelts], # Franks
	[iSatavahana, iPandyans, iBactria, iKushans, iMauryans, iGupta], # Chalukyans
	[iFranks, iVisigoths, iOstrogoths], # Lombards
	[iJin, iGoguryeo, iTocharians], # Gokturks
	[], # Srivajaya
	[iByzantines, iArmenia, iRome], # Khazars
	[iGupta, iTang, iFunan], # Tibet
	[iGoguryeo, iFunan], # Tang
	[iSeleucids, iEgypt, iSassanids, iSaba], # Arabs
	[], # Xiongnu
	[], # Numidia
	[iParthia, iSatavahana, iBactria], # Scythians
	[iHan, iVietnam], # Nan Yue
	[], # Sungas
	[], # Macedon
	[], # Makuria
	[], # Himyar
	[iJin, iHan], # Shu
	[iJin, iQin], # Wu
	[iSassanids, iTocharians, iGupta], # Hepthalites
	[], # Xianbei
	[], # Huns
	[], # Avars
	[], # Rouran
	[], # Vakataka
	[], # Song
	[], # Magadha
	[], # Rebel Rome
	[], # Pallavas
	[], # Kalabhras
	[], # Saxons
	[], # Western Rome
	[], # Moors
	[], # Champa
]

# ai war targets in order of priority
lWarTargets = [
	[iSeleucids, iEgypt], # Antigonids
	[iEgypt, iAntigonids, iParthia, iMaccabees, iBactria], # Seleucids
	[iMaccabees, iSeleucids, iNubia], # Egypt
	[iRome], # Carthage
	[iSatavahana, iKalinka, iPandyans], # Mauryans
	[iMauryans, iPandyans, iSatavahana], # Kalinka
	[iNanYue, iGojoseon], # Qin
	[iHan, iQin], # Gojoseon
	[iAxum, iEgypt, iSaba], # Nubia
	[iAxum, iArabs, iMaccabees], # Saba
	[iSatavahana, iMauryans, iGupta, iChalukyans], # Pandyans
	[], # Pontus
	[iRome, iCarthage, iDacia], # Celts
	[iCarthage, iEgypt, iAntigonids, iCelts, iMaccabees, iSeleucids], # Rome
	[iHan, iFunan, iTibet, iQin, iShu, iNanYue, iWu, iJin], # Vietnam
	[iBactria, iKushans, iHephthalites], # Tocharians
	[iSeleucids, iKushans, iMauryans, iParthia, iSassanids, iScythians], # Bactria
	[iQin, iGoguryeo, iYamato, iFunan, iTocharians, iTibet], # Han
	[iMauryans, iGupta, iChalukyans, iPandyans, iScythians, iBactria], # Satavahana
	[iSeleucids, iParthia, iSassanids], # Armenia
	[iEgypt, iSeleucids, iArmenia, iParthia], # Maccabees
	[iSeleucids, iArmenia, iSassanids, iBactria], # Parthia
	[iRome], # Dacia
	[iHan, iJin, iTang], # Goguryeo
	[iNubia, iSaba], # Axum
	[iSeleucids, iBactria, iSatavahana, iParthia, iSassanids, iMauryans], # Kushans
	[iHan, iJin, iTang], # Funan
	[iGoguryeo, iFunan], # Jin
	[iSeleucids, iParthia, iBactria, iArabs, iByzantines], # Sassanids
	[iGoguryeo], # Yamato
	[iSatavahana, iPandyans, iBactria, iKushans, iMauryans, iChalukyans], # Gupta
	[iCelts, iCarthage, iSassanids], # Byzantines
	[iRome, iOstrogoths, iVandals, iFranks], # Visigoths
	[iRome, iByzantines, iVisigoths], # Ostrogoths
	[iRome, iVisigoths, iByzantines], # Vandals
	[iRome, iCelts], # Franks
	[iSatavahana, iPandyans, iBactria, iKushans, iMauryans, iGupta], # Chalukyans
	[iFranks, iVisigoths, iOstrogoths], # Lombards
	[iJin, iGoguryeo, iTocharians], # Gokturks
	[], # Srivajaya
	[iByzantines, iArmenia, iRome], # Khazars
	[iGupta, iTang, iFunan], # Tibet
	[iGoguryeo, iFunan], # Tang
	[iSeleucids, iEgypt, iSassanids, iSaba], # Arabs
	[iQin, iHan, iGojoseon], # Xiongnu
	[iCarthage, iRome], # Numidia
	[iSatavahana, iParthia, iBactria], # Scythians
	[iHan, iVietnam], # Nan Yue
	[], # Sungas
	[], # Macedon
	[], # Makuria
	[], # Himyar
	[iJin, iHan], # Shu
	[iJin, iQin], # Wu
	[iSassanids, iTocharians, iGupta], # Hepthalites
	[iQin, iHan, iGojoseon], # Xianbei
	[], # Huns
	[], # Avars
	[], # Rouran
	[], # Vakataka
	[], # Song
	[], # Magadha
	[iCelts, iCarthage, iSeleucids, iEgypt, iMaccabees, iNubia, iParthia, iSassanids, iFranks, iVisigoths, iOstrogoths], # Rebel Rome
	[], # Pallavas
	[], # Kalabhras
	[], # Saxons
	[], # Western Rome
	[], # Moors
	[], # Champa
]

#for stability check on spawn
lOlderNeighbours = [
	[], # Antigonids
	[], # Seleucids
	[], # Egypt
	[], # Carthage
	[], # Mauryans
	[], # Kalinka
	[], # Qin
	[], # Gojoseon
	[], # Nubia
	[], # Saba
	[], # Pandyans
	[iAntigonids], # Pontus
	[], # Celts
	[iCarthage], # Rome
	[], # Vietnam
	[], # Tocharians
	[iSeleucids], # Bactria
	[iQin, iGojoseon, iVietnam], # Han
	[iKalinka, iMauryans, iPandyans], # Satavahana
	[iAntigonids, iPontus], # Armenia
	[iSeleucids, iEgypt], # Maccabees
	[iSeleucids, iArmenia, iBactria], # Parthia
	[], # Dacia
	[iGojoseon], # Goguryeo
	[iNubia, iSaba, iEgypt], # Axum
	[iBactria, iParthia, iMauryans, iTocharians, iSatavahana], # Kushans
	[iVietnam], # Funan
	[iParthia, iParthia, iKushans, iEgypt], # Sassanids
	[iGoguryeo], # Yamato
	[iHan, iGojoseon, iGoguryeo], # Jin
	[iMauryans, iSatavahana, iPandyans, iKushans, iKalinka], # Gupta
	[iDacia], # Byzantines
	[iRome], # Visigoths
	[iRome], # Ostrogoths
	[iRome], # Vandals
	[iRome], # Franks
	[iGupta, iPandyans, iSatavahana, iKalinka], # Chalukyans
	[iFranks, iVisigoths, iOstrogoths], # Lombards
	[iJin, iTocharians, iKushans], # Gokturks
	[], # Srivajaya
	[iByzantines, iDacia, iSassanids], # Khazars
	[iGupta, iJin], # Tibet
	[iJin, iHan, iQin, iGoguryeo], # Tang
	[iSassanids, iByzantines, iEgypt, iEgypt, iSeleucids, iSeleucids], # Arabs
	[iQin, iHan, iGojoseon], # Xiongnu
	[], # Numidia
	[iParthia, iSatavahana, iBactria], # Scythians
	[], # Nan Yue
	[], # Sungas
	[], # Macedon
	[], # Makuria
	[], # Himyar
	[], # Shu
	[], # Wu
	[iSassanids, iTocharians, iGupta], # Hepthalites
	[iQin, iHan, iGojoseon], # Xianbei
	[], # Huns
	[], # Avars
	[], # Rouran
	[iSungas, iKushans], # Vakataka
	[], # Song
	[], # Magadha
	[], # Rebel Rome
	[], # Pallavas
	[], # Kalabhras
	[], # Saxons
	[], # Western Rome
	[], # Moors
	[], # Champa
]
# CIVICS

iNumCivics = 25
(iDespotismCivic, iMonarchyCivic, iOligarchyCivic, iEmpireCivic, iTheocracyCivic, # govt
iBarbarismCivic, iTyrannyCivic, iVassalageCivic, iReligiousLawCivic, iBureaucracyCivic, # legal
iTribalLevyCivic, iSlaveryCivic, iCasteSystemCivic, iSerfdomCivic, iWageLaborCivic, # labor
iDecentralizationCivic, iAgrarianismCivic, iTradeEconomyCivic, iPatronageCivic, iMilitaryEconomyCivic, # economy
iPaganismCivic, iDynasticCultCivic, iStateReligionCivic, iMilitancyCivic, iSyncretismCivic) = range(iNumCivics) # religion

# RELIGIONS

iNumReligions = 11
(iJudaism, iZoroastrianism, iHinduism, iBuddhism, iConfucianism, iHellenism, iTaoism, iJainism, iChristianity, iManichaeism, iIslam) = range(iNumReligions)

tPersecutionOrder = (
	(iTaoism, iConfucianism, iHinduism, iBuddhism, iJainism, iManichaeism, iHellenism, iZoroastrianism, iIslam, iChristianity),
	(iTaoism, iConfucianism, iJainism, iHellenism, iManichaeism, iHinduism, iBuddhism, iChristianity, iIslam, iJudaism),
	(iTaoism, iConfucianism, iHellenism, iChristianity, iIslam, iManichaeism, iJudaism, iZoroastrianism, iBuddhism, iJainism),
	(iTaoism, iConfucianism, iHellenism, iChristianity, iIslam, iManichaeism, iJudaism, iZoroastrianism, iBuddhism, iHinduism),
	(iChristianity, iHellenism, iHinduism, iZoroastrianism, iJainism, iManichaeism, iJudaism, iIslam, iBuddhism, iTaoism),
	(iTaoism, iConfucianism, iHinduism, iJainism, iIslam, iZoroastrianism, iManichaeism, iBuddhism, iJudaism, iChristianity),
	(iChristianity, iHellenism, iHinduism, iZoroastrianism, iJainism, iManichaeism, iJudaism, iIslam, iBuddhism, iConfucianism),
	(iTaoism, iConfucianism, iHellenism, iChristianity, iIslam, iManichaeism, iJudaism, iZoroastrianism, iBuddhism, iHinduism),
	(iTaoism, iConfucianism, iHinduism, iJainism, iIslam, iZoroastrianism, iManichaeism, iBuddhism, iJudaism, iHellenism),
	(iTaoism, iConfucianism, iHinduism, iJainism, iIslam, iZoroastrianism, iHellenism, iBuddhism, iJudaism, iChristianity),
	(iChristianity, iConfucianism, iHinduism, iJainism, iHellenism, iZoroastrianism, iManichaeism, iBuddhism, iJudaism, iTaoism),
)

iHolyWarPeriod = 100

# COMPANIES (CORPORATIONS)

iNumCompanies = 6
(iGrainMerchants, iFishMerchants, iClothMerchants, iSpiceMerchants, iMasterArtisans, iMasterTradesmen) = range(iNumCompanies)


# CIVICS

iNumCivics = 25
(iTribalFederationCivic, iMonarchyCivic, iOligarchyCivic, iEmpireCivic, iTheocracyCivic,
iTribalLawCivic, iTyrannyCivic, iVassalageCivic, iReligiousLawCivic, iBureacracyCivic,
iTribalismCivic, iSlaveryCivic, iCasteSystemCivic, iSerfdomCivic, iFreeLaborCivic,
iDecentralizationCivic, iAgrarianismCivic, iMarketEconomyCivic, iPatronageCivic, iMilitaryEconomyCivic,
iPaganismCivic, iDynasticCultCivic, iStateReligionCivic, iMilitancyCivic, iFreeReligionCivic) = range(iNumCivics)

# ERAS

iNumEras = 4
(iEra1, iEra2, iEra3, iEra4) = range(iNumEras)

# Attitudes

iNumAttitudes = 5
(iFurious, iAnnoyed, iCautious, iPleased, iFriendly) = range(iNumAttitudes)

# PROMOTIONS

iNumPromotions = 59
(iDiscipline, iSilkworm, iCombat1, iCombat2, iCombat3, iCombat4, iCombat5, iCover, iShock, iFormation, iSkirmish, iCharge, iAmphibious, iMarch, iBlitz, iCommando, 
iMedic1, iMedic2, iGuerilla1, iGuerilla2, iGuerilla3, iWoodsman1, iWoodsman2, iWoodsman3, iCityRaider1, iCityRaider2, iCityRaider3, iCityGarrison1, 
iCityGarrison2, iCityGarrison3, iDrill1, iDrill2, iDrill3, iDrill4, iBarrage1, iBarrage2, iBarrage3, iAccuracy, iFlanking1, iFlanking2, iFlanking3, 
iSentry, iMobility, iNavigation1, iNavigation2, iLeader, iLeadership, iTactics, iCombat6, iMorale, iMedic3, iFeintAttack, iEncirclement, iGreekFire, 
iDesertAdaptation, iBlessed, iRaider, iOceanfaring, iMercenary) = range(iNumPromotions)

# TERRAINS

iNumTerrains = 14
(iGrassland, iPlains, iSemidesert, iDesert, iWetland, iTundra, iIce, iSaltLake, iCoast, iSea, iOcean, iPeak, iHill, iWasteland) = range(iNumTerrains)

# TECHS

iNumTechs = 95
(iArchery, iSiegeEngines, iMarksmanship, iAgriculture, iHorticulture, iCropRotation, iCasteSystem, iCalendar, iAgrarianism, iThePlough, iAnimalHusbandry, iElephantTraining, iHorsemanship, 
iSelectiveBreeding, iCavalryTactics, iTheStirrup, iHorseArchery, iFishing, iSailing, iNavalWarfare, iSternRudder, iNavigation, iAstrolabe, iPottery, iConstruction, iMasonry, iBridgeBuilding, 
iEngineering, iFortification, iSanitation, iMachinery, iMedicine, iArchitecture, iPaper, iEducation, iPrintingPress, iBureaucracy, iLuxuryTrade, iMonarchy, iVassalage, iSerfdom, iCurrency, 
iCodeOfLaws, iStateReligion, iBulkTrade, iJurisprudence, iBanking, iManufacturedTrade, iWageLabor, iMining, iBronzeWorking, iInfantryTactics, iMilitaryDrill, iLogistics, iMetalCasting, 
iScaleArmor, iIronWorking, iSteelWorking, iChainmail, iBlastFurnace, iAlchemy, iGunpowder, iPriesthood, iAstronomy, iOrganisedReligion, iMonasticism, iTheology, iReligiousLaw, iMysticism, 
iSyncretism, iTheocracy, iWriting, iAlphabet, iMathematics, iCartography, iLiterature, iDrama, iPhilosophy, iAesthetics, iPatronage, 
iTibetanUP, iTocharianUP, iFunanUP, iSriVijayanUP, iFreeTradeTech, iImperialismTech, iStabilityStable, 
iStabilityUnstable, iStabilityCollapsing, iOverextension, iRomanEmpire, iPyramidsFunctionTech, iColossusFunctionTech, iTrajansColumnFunctionTech, iSuccessionTech) = range(iNumTechs) #4

lStabilityTechs = [iCasteSystem, iCalendar, iAgrarianism, iPaper, iMonarchy, iVassalage, iCurrency, iCodeOfLaws, iStateReligion, iBulkTrade, iJurisprudence, iBanking, iManufacturedTrade, 
iWageLabor, iPriesthood, iAstronomy, iOrganisedReligion, iMonasticism, iTheology, iReligiousLaw, iMysticism, iSyncretism, iTheocracy, iWriting, iAlphabet, iMathematics, iCartography, 
iLiterature, iDrama, iPhilosophy, iAesthetics, iPatronage, ]

# STARTING TECHS

lStartingTechs = [
	# 0 Antigonids 19
	[iStabilityStable, iFreeTradeTech, iAnimalHusbandry, iPottery, iMining, iPriesthood, iBronzeWorking, iMasonry, iFishing, iSailing, iAgriculture, iConstruction, iLuxuryTrade, iCurrency, 
	iIronWorking, iWriting, iAlphabet, iSiegeEngines, iInfantryTactics, iMilitaryDrill, iHorsemanship, ], 
	# 1 Seleucids 19
	[iStabilityStable, iFreeTradeTech, iAnimalHusbandry, iPottery, iMining, iPriesthood, iBronzeWorking, iMasonry, iFishing, iAgriculture, iConstruction, iLuxuryTrade, iCurrency, 
	iIronWorking, iWriting, iAlphabet, iInfantryTactics, iMilitaryDrill, iSiegeEngines, iElephantTraining, iHorsemanship, ], 
	# 2 Egypt 19
	[iPyramidsFunctionTech, iStabilityStable, iFreeTradeTech, iAnimalHusbandry, iPottery, iMining, iPriesthood, iBronzeWorking, iMasonry, iFishing, iAgriculture, iSailing, iConstruction, 
	iLuxuryTrade, iCurrency, iIronWorking, iAstronomy, iWriting, iAlphabet, iSiegeEngines, iInfantryTactics, iHorsemanship, ], 
	# 3 Carthage 18
	[iStabilityStable, iFreeTradeTech, iAnimalHusbandry, iPottery, iMining, iPriesthood, iBronzeWorking, iMasonry, iFishing, iAgriculture, iHorsemanship, iSailing, iConstruction, 
	iLuxuryTrade, iCurrency, iIronWorking, iWriting, iAlphabet, iSiegeEngines, iInfantryTactics, ], 
	# 4 Mauryans 19
	[iStabilityStable, iFreeTradeTech, iAnimalHusbandry, iPottery, iMining, iPriesthood, iBronzeWorking, iFishing, iArchery, iAgriculture, iConstruction, iLuxuryTrade, iIronWorking, 
	iAstronomy, iWriting, iAlphabet, iCasteSystem, iElephantTraining, iOrganisedReligion, iMasonry, iHorticulture, ], 
	# 5 Kalinka 18
	[iStabilityStable, iFreeTradeTech, iAnimalHusbandry, iPottery, iMining, iPriesthood, iBronzeWorking, iFishing, iArchery, iAgriculture, iConstruction, iLuxuryTrade, iIronWorking, 
	iAstronomy, iWriting, iAlphabet, iCasteSystem, iElephantTraining, iOrganisedReligion, iHorticulture, ], 
	# 6 Qin 18
	[iStabilityStable, iFreeTradeTech, iAnimalHusbandry, iPottery, iMining, iPriesthood, iBronzeWorking, iFishing, iArchery, iAgriculture, iLuxuryTrade, iCurrency, iIronWorking, 
	iAstronomy, iWriting, iInfantryTactics, iConstruction, iSiegeEngines, iFishing, ], 
	# 7 Gojoseon 15
	[iStabilityStable, iFreeTradeTech, iAnimalHusbandry, iPottery, iMining, iPriesthood, iBronzeWorking, iFishing, iArchery, iAgriculture, iSailing, iConstruction, iLuxuryTrade, 
	iIronWorking, iAstronomy, iWriting, iHorsemanship, ], 
	# 8 Nubia 12
	[iStabilityStable, iFreeTradeTech, iAnimalHusbandry, iPottery, iMining, iPriesthood, iBronzeWorking, iMasonry, iFishing, iArchery, iAgriculture, iConstruction, iLuxuryTrade, iWriting, ],
	# 9 Saba 12
	[iStabilityStable, iFreeTradeTech, iAnimalHusbandry, iPottery, iMining, iPriesthood, iBronzeWorking, iFishing, iSailing, iAgriculture, iConstruction, iLuxuryTrade, iWriting, iCurrency, ],
	# 10 Pandyans 18
	[iStabilityStable, iFreeTradeTech, iAnimalHusbandry, iPottery, iMining, iPriesthood, iBronzeWorking, iFishing, iArchery, iAgriculture, iConstruction, iLuxuryTrade, iIronWorking, 
	iAstronomy, iWriting, iAlphabet, iCasteSystem, iSailing, iHorticulture, iOrganisedReligion, ], 
	# 11 Pontus 16
	[iStabilityStable, iFreeTradeTech, iAnimalHusbandry, iPottery, iMining, iPriesthood, iBronzeWorking, iMasonry, iFishing, iSailing, iAgriculture, iConstruction, iLuxuryTrade, 
	iCurrency, iIronWorking, iWriting, iAlphabet, iInfantryTactics, ], 
	# 12 Celts 11
	[iStabilityStable, iFreeTradeTech, iAnimalHusbandry, iPottery, iMining, iPriesthood, iBronzeWorking, iFishing, iAgriculture, iConstruction, iLuxuryTrade, iIronWorking, iMetalCasting, ],
	# 13 Rome 20
	[iStabilityStable, iFreeTradeTech, iAnimalHusbandry, iPottery, iMining, iPriesthood, iBronzeWorking, iMasonry, iFishing, iAgriculture, iSailing, iConstruction, iLuxuryTrade, iCurrency, 
	iIronWorking, iWriting, iAlphabet, iMilitaryDrill, iSiegeEngines, iInfantryTactics, iAstronomy, iHorsemanship, ], 
	# 14 Vietnam 13
	[iStabilityStable, iFreeTradeTech, iAnimalHusbandry, iPottery, iMining, iPriesthood, iBronzeWorking, iFishing, iArchery, iAgriculture, iSailing, iConstruction, iLuxuryTrade, iIronWorking, 
	iWriting, ], 
	# 15 Tocharians 13
	[iStabilityStable, iFreeTradeTech, iAnimalHusbandry, iPottery, iMining, iPriesthood, iBronzeWorking, iFishing, iArchery, iAgriculture, iConstruction, iLuxuryTrade, iWriting, iAstronomy, 
	iHorsemanship, iTocharianUP, ],
	# 16 Bactria 18
	[iStabilityStable, iFreeTradeTech, iAnimalHusbandry, iPottery, iMining, iPriesthood, iBronzeWorking, iMasonry, iFishing, iArchery, iAgriculture, iConstruction, iLuxuryTrade, iCurrency, 
	iIronWorking, iWriting, iAlphabet, iHorsemanship, iSelectiveBreeding, iInfantryTactics, ], 
	# 17 Han 23
	[iStabilityStable, iFreeTradeTech, iAnimalHusbandry, iPottery, iMining, iPriesthood, iBronzeWorking, iMasonry, iFishing, iArchery, iAgriculture, iSailing, iCalendar, iSiegeEngines, 
	iConstruction, iLuxuryTrade, iCurrency, iIronWorking, iWriting, iHorticulture, iHorsemanship, iInfantryTactics, iCropRotation, iAlphabet, iAstronomy, ], 
	# 18 Satavahana 20
	[iStabilityStable, iFreeTradeTech, iAnimalHusbandry, iPottery, iMining, iPriesthood, iBronzeWorking, iFishing, iArchery, iAgriculture, iSailing, iConstruction, iLuxuryTrade, iIronWorking, 
	iOrganisedReligion, iWriting, iAlphabet, iCasteSystem, iHorticulture, iMasonry, iCalendar, iCurrency, ], 
	# 19 Armenia 18
	[iStabilityStable, iFreeTradeTech, iAnimalHusbandry, iPottery, iMining, iPriesthood, iBronzeWorking, iMasonry, iFishing, iArchery, iAgriculture, iHorsemanship, iConstruction, iLuxuryTrade, 
	iIronWorking, iWriting, iAlphabet, iCurrency, iMonarchy, iSelectiveBreeding, ],
	# 20 Maccabees 19
	[iStabilityStable, iFreeTradeTech, iAnimalHusbandry, iPottery, iMining, iPriesthood, iBronzeWorking, iMasonry, iFishing, iArchery, iAgriculture, iHorticulture, iConstruction, iLuxuryTrade, 
	iIronWorking, iWriting, iAlphabet, iCodeOfLaws, iOrganisedReligion, iStateReligion, iCurrency, ],
	# 21 Parthia 18
	[iStabilityStable, iFreeTradeTech, iAnimalHusbandry, iPottery, iMining, iPriesthood, iBronzeWorking, iMasonry, iArchery, iAgriculture, iHorsemanship, iHorseArchery, iConstruction, 
	iLuxuryTrade, iIronWorking, iCurrency, iWriting, iAlphabet, iSelectiveBreeding, iMonarchy, ],
	# 22 Dacia 14
	[iStabilityStable, iFreeTradeTech, iAnimalHusbandry, iPottery, iMining, iPriesthood, iBronzeWorking, iMasonry, iFishing, iArchery, iAgriculture, iConstruction, iLuxuryTrade, iMetalCasting, 
	iIronWorking, iWriting, ],
	# 23 Goguryeo 24
	[iStabilityStable, iFreeTradeTech, iAnimalHusbandry, iPottery, iMining, iPriesthood, iBronzeWorking, iMasonry, iFishing, iArchery, iCalendar, iAgriculture, iSailing, iConstruction, 
	iLuxuryTrade, iCurrency, iCodeOfLaws, iMetalCasting, iIronWorking, iWriting, iAlphabet, iHorsemanship, iInfantryTactics, iSiegeEngines, iMonarchy, iOrganisedReligion, ], 
	# 24 Axum 21
	[iStabilityStable, iFreeTradeTech, iAnimalHusbandry, iPottery, iMining, iPriesthood, iBronzeWorking, iMasonry, iFishing, iArchery, iAgriculture, iSailing, iNavalWarfare, iConstruction, 
	iLuxuryTrade, iCurrency, iIronWorking, iOrganisedReligion, iWriting, iAlphabet, iMonarchy, iHorsemanship, iHorticulture, ], 
	# 25 Kushans 19
	[iStabilityStable, iFreeTradeTech, iAnimalHusbandry, iPottery, iMining, iPriesthood, iBronzeWorking, iMasonry, iArchery, iAgriculture, iHorsemanship, iSelectiveBreeding, iHorseArchery, 
	iConstruction, iLuxuryTrade, iCurrency, iIronWorking, iOrganisedReligion, iWriting, iAlphabet, iMonarchy, ], 
	# 26 Funan 18
	[iStabilityStable, iFreeTradeTech, iAnimalHusbandry, iPottery, iMining, iPriesthood, iBronzeWorking, iMasonry, iFishing, iArchery, iAgriculture, iConstruction, iLuxuryTrade, 
	iMetalCasting, iIronWorking, iOrganisedReligion, iWriting, iAlphabet, iHorticulture, iSailing],
	# 27 Jin 35
	[iStabilityStable, iFreeTradeTech, iAnimalHusbandry, iPottery, iMining, iPriesthood, iBronzeWorking, iMasonry, iFishing, iArchery, iSiegeEngines, iAgriculture, iHorticulture, 
	iCropRotation, iCalendar, iHorsemanship, iSailing, iConstruction, iLuxuryTrade, iMonarchy, iCurrency, iMetalCasting, iIronWorking, iAstronomy, iOrganisedReligion, iWriting, iAlphabet, 
	iMathematics, iLiterature, iJurisprudence, iBureaucracy, iMarksmanship, iInfantryTactics, iSelectiveBreeding, iBridgeBuilding, iScaleArmor, iCodeOfLaws, ], 
	# 28 Sassanids 35
	[iStabilityStable, iFreeTradeTech, iAnimalHusbandry, iPottery, iMining, iPriesthood, iBronzeWorking, iMasonry, iFishing, iArchery, iSiegeEngines, iAgriculture, iHorticulture, iCalendar, 
	iHorsemanship, iSelectiveBreeding, iHorseArchery, iSailing, iConstruction, iLuxuryTrade, iMonarchy, iVassalage, iCurrency, iCodeOfLaws, iStateReligion, iIronWorking, iAstronomy, 
	iOrganisedReligion, iWriting, iAlphabet, iMathematics, iLiterature, iInfantryTactics, iMarksmanship, iCavalryTactics, 
	iMetalCasting, iScaleArmor, ], 
	# 29 Yamato 25
	[iStabilityStable, iFreeTradeTech, iAnimalHusbandry, iPottery, iMining, iPriesthood, iBronzeWorking, iMasonry, iFishing, iArchery, iAgriculture, iSailing, iConstruction, iLuxuryTrade, 
	iCurrency, iCodeOfLaws, iMetalCasting, iIronWorking, iAstronomy, iWriting, iHorticulture, iCalendar, iMonarchy, iMarksmanship, iMilitaryDrill, iSiegeEngines, iCropRotation, ], 
	# 30 Gupta 36
	[iStabilityStable, iFreeTradeTech, iAnimalHusbandry, iPottery, iMining, iPriesthood, iBronzeWorking, iMasonry, iFishing, iArchery, iMarksmanship, iAgriculture, iHorticulture, 
	iCropRotation, iCasteSystem, iCalendar, iHorsemanship, iSailing, iConstruction, iLuxuryTrade, iMonarchy, iVassalage, iCurrency, iCodeOfLaws, iStateReligion, iIronWorking, iAstronomy, 
	iOrganisedReligion, iMonasticism, iWriting, iAlphabet, iMathematics, iLiterature, iPhilosophy, iElephantTraining, iMetalCasting, iSelectiveBreeding, iScaleArmor, ], 
	# 31 Byzantines 42
	[iStabilityStable, iFreeTradeTech, iAnimalHusbandry, iPottery, iMining, iPriesthood, iBronzeWorking, iMasonry, iFishing, iArchery, iSiegeEngines, iAgriculture, 
	iHorticulture, iCalendar, iHorsemanship, iSailing, iConstruction, iTheology, iNavalWarfare, iLuxuryTrade, iMonarchy, iVassalage, iCurrency, iCodeOfLaws, iStateReligion, iIronWorking, 
	iAstronomy, iOrganisedReligion, iWriting, iAlphabet, iMathematics, iLiterature, iPhilosophy, iMilitaryDrill, iLogistics, iEngineering, iScaleArmor, iInfantryTactics, iBridgeBuilding, 
	iJurisprudence, iBureaucracy, iMetalCasting, iCropRotation, iBulkTrade], 
	# 36 Visigoths 31
	[iStabilityStable, iFreeTradeTech, iAnimalHusbandry, iPottery, iMining, iPriesthood, iBronzeWorking, iMasonry, iFishing, iArchery, iSiegeEngines, iAgriculture, iHorticulture, 
	iCropRotation, iCalendar, iHorsemanship, iSelectiveBreeding, iConstruction, iLuxuryTrade, iMonarchy, iVassalage, iCurrency, iStateReligion, iMetalCasting, iIronWorking, 
	iSteelWorking, iAstronomy, iOrganisedReligion, iWriting, iAlphabet, iCavalryTactics, iScaleArmor, iChainmail, ], 
	# 38 Vandals 33
	[iStabilityStable, iFreeTradeTech, iAnimalHusbandry, iPottery, iMining, iPriesthood, iBronzeWorking, iMasonry, iFishing, iSailing, iNavalWarfare, iArchery, iSiegeEngines, iAgriculture, 
	iHorticulture, iCropRotation, iCalendar, iHorsemanship, iSelectiveBreeding, iConstruction, iLuxuryTrade, iMonarchy, iVassalage, iCurrency, iStateReligion, iMetalCasting, 
	iIronWorking, iSteelWorking, iAstronomy, iOrganisedReligion, iWriting, iAlphabet, iCavalryTactics, iScaleArmor, iChainmail, ], 
	# 37 Ostrogoths 32
	[iStabilityStable, iFreeTradeTech, iAnimalHusbandry, iPottery, iMining, iPriesthood, iBronzeWorking, iMasonry, iFishing, iArchery, iSiegeEngines, iAgriculture, iHorticulture, 
	iCropRotation, iCalendar, iHorsemanship, iSelectiveBreeding, iTheStirrup, iConstruction, iLuxuryTrade, iMonarchy, iVassalage, iCurrency, iStateReligion, iMetalCasting, iIronWorking, 
	iSteelWorking, iAstronomy, iOrganisedReligion, iWriting, iAlphabet, iCavalryTactics, iScaleArmor, iChainmail, ], 
	# 32 Franks 34
	[iStabilityStable, iFreeTradeTech, iAnimalHusbandry, iPottery, iMining, iPriesthood, iBronzeWorking, iMasonry, iFishing, iArchery, iSiegeEngines, iAgriculture, iHorticulture, 
	iCropRotation, iCalendar, iHorsemanship, iSelectiveBreeding, iTheStirrup, iConstruction, iLuxuryTrade, iMonarchy, iVassalage, iSerfdom, iCurrency, iCodeOfLaws, iStateReligion, 
	iMetalCasting, iIronWorking, iSteelWorking, iAstronomy, iOrganisedReligion, iWriting, iAlphabet, iCavalryTactics, iScaleArmor, iChainmail, ], 
	# 36 Chalukyans 43
	[iStabilityStable, iFreeTradeTech, iAnimalHusbandry, iPottery, iMining, iPriesthood, iBronzeWorking, iMasonry, iFishing, iArchery, iSiegeEngines, iMarksmanship, iAgriculture, 
	iHorticulture, iCalendar, iHorsemanship, iCropRotation, iCasteSystem, iSailing, iNavalWarfare, iConstruction, iLuxuryTrade, iMonarchy, iVassalage, iCurrency, iCodeOfLaws, iStateReligion, 
	iMetalCasting, iIronWorking, iSteelWorking, iAstronomy, iOrganisedReligion, iMonasticism, iTheology, iWriting, iAlphabet, iMathematics, iLiterature, iPhilosophy, iElephantTraining, 
	iScaleArmor, iChainmail, iJurisprudence, iReligiousLaw, iPatronage], 
	# 34 Lombards 33
	[iStabilityStable, iFreeTradeTech, iAnimalHusbandry, iPottery, iMining, iPriesthood, iBronzeWorking, iMasonry, iFishing, iArchery, iSiegeEngines, iAgriculture, iHorticulture, 
	iCropRotation, iCalendar, iHorsemanship, iSelectiveBreeding, iTheStirrup, iConstruction, iLuxuryTrade, iMonarchy, iVassalage, iCurrency, iCodeOfLaws, iStateReligion, iMetalCasting, 
	iIronWorking, iSteelWorking, iAstronomy, iOrganisedReligion, iWriting, iAlphabet, iCavalryTactics, iScaleArmor, iChainmail, ], 
	# 35 Gokturks 29
	[iStabilityStable, iFreeTradeTech, iAnimalHusbandry, iPottery, iMining, iPriesthood, iBronzeWorking, iMasonry, iFishing, iArchery, iAgriculture, iHorsemanship, iSelectiveBreeding, 
	iHorseArchery, iConstruction, iLuxuryTrade, iCurrency, iCodeOfLaws, iMetalCasting, iIronWorking, iAstronomy, iOrganisedReligion, iWriting, iAlphabet, iTheStirrup, iMarksmanship, 
	iCavalryTactics, iCalendar, iHorticulture, iScaleArmor, iChainmail, ], 
	# 36 Srivajaya 27
	[iStabilityStable, iFreeTradeTech, iAnimalHusbandry, iPottery, iMining, iPriesthood, iBronzeWorking, iMasonry, iFishing, iArchery, iAgriculture, iSailing, iNavalWarfare, iSiegeEngines, 
	iConstruction, iLuxuryTrade, iCurrency, iCodeOfLaws, iMetalCasting, iIronWorking, iAstronomy, iWriting, iAlphabet, iHorticulture, iCropRotation, iCalendar, iOrganisedReligion, iMonarchy, 
	iSternRudder, iSriVijayanUP, ], 
	# 37 Khazars 31
	[iStabilityStable, iFreeTradeTech, iAnimalHusbandry, iPottery, iMining, iPriesthood, iBronzeWorking, iMasonry, iArchery, iAgriculture, iHorsemanship, iSelectiveBreeding, iHorseArchery, 
	iConstruction, iLuxuryTrade, iCurrency, iCodeOfLaws, iMetalCasting, iIronWorking, iAstronomy, iOrganisedReligion, iWriting, iAlphabet, iTheStirrup, iMarksmanship, iSerfdom, 
	iCavalryTactics, iCalendar, iHorticulture, iMonarchy, iCropRotation, iScaleArmor, iChainmail, ], 
	# Tibet 29
	[iStabilityStable, iFreeTradeTech, iAnimalHusbandry, iPottery, iMining, iPriesthood, iBronzeWorking, iMasonry, iFishing, iArchery, iAgriculture, iHorsemanship, iSelectiveBreeding, 
	iHorticulture, iCalendar, iConstruction, iLuxuryTrade, iCurrency, iCodeOfLaws, iIronWorking, iAstronomy, iOrganisedReligion, iWriting, iAlphabet, iStateReligion, iMonasticism, 
	iMarksmanship, iTheStirrup, iHorseArchery, iCavalryTactics, iScaleArmor, iTibetanUP, ], 
	# Tang 49
	[iStabilityStable, iFreeTradeTech, iAnimalHusbandry, iPottery, iMining, iPriesthood, iBronzeWorking, iMasonry, iFishing, iArchery, iSiegeEngines, iAgriculture, iHorticulture, 
	iCropRotation, iCalendar, iHorsemanship, iSelectiveBreeding, iSailing, iNavalWarfare, iConstruction, iEngineering, iLuxuryTrade, iMonarchy, iVassalage, iCurrency, iCodeOfLaws, 
	iMetalCasting, iIronWorking, iSteelWorking, iAstronomy, iOrganisedReligion, iMonasticism, iWriting, iAlphabet, iMathematics, iCartography, iLiterature, iPhilosophy, iCavalryTactics, 
	iTheStirrup, iBridgeBuilding, iMarksmanship, iInfantryTactics, iMilitaryDrill, iScaleArmor, iChainmail, iJurisprudence, iBureaucracy, iPaper, 
	iBulkTrade, iAgrarianism, ],  
	# Arabs 44
	[iStabilityStable, iFreeTradeTech, iAnimalHusbandry, iPottery, iMining, iPriesthood, iBronzeWorking, iMasonry, iFishing, iArchery, iSiegeEngines, iMarksmanship, iAgriculture, 
	iHorticulture, iCropRotation, iCalendar, iHorsemanship, iSelectiveBreeding, iTheStirrup, iSailing, iNavalWarfare, iConstruction, iEngineering, iLuxuryTrade, iMonarchy, iVassalage, 
	iCurrency, iCodeOfLaws, iStateReligion, iMetalCasting, iIronWorking, iSteelWorking, iAstronomy, iOrganisedReligion, iMonasticism, iTheology, iMysticism, iWriting, iAlphabet, 
	iMathematics, iTheocracy, iLiterature, iPhilosophy, iCavalryTactics, iBridgeBuilding, iScaleArmor, ], 
	# Xiongnu
	[iStabilityUnstable, iFreeTradeTech, iAnimalHusbandry, iPottery, iMining, iPriesthood, iBronzeWorking, iArchery, iHorsemanship, iHorseArchery, iLuxuryTrade, iIronWorking, iCurrency, 
	iSelectiveBreeding, iFishing, iConstruction, ],
	# Numidia
	[iStabilityStable, iFreeTradeTech, iAnimalHusbandry, iPottery, iMining, iPriesthood, iBronzeWorking, iArchery, iAgriculture, iHorsemanship, iLuxuryTrade, iIronWorking, iCurrency, ], 
	# Scythians
	[iStabilityUnstable, iFreeTradeTech, iAnimalHusbandry, iPottery, iMining, iPriesthood, iBronzeWorking, iArchery, iHorsemanship, iHorseArchery, iLuxuryTrade, iIronWorking, iCurrency, 
	iSelectiveBreeding, iFishing, iConstruction, ],
	# NanYue 15
	[iStabilityUnstable, iFreeTradeTech, iAnimalHusbandry, iPottery, iMining, iPriesthood, iBronzeWorking, iMasonry, iFishing, iArchery, iAgriculture, iSailing, iConstruction, iLuxuryTrade, 
	iCurrency, iIronWorking, iWriting, ], 
	# Sungas
	[iStabilityStable, iFreeTradeTech, iAnimalHusbandry, iPottery, iMining, iPriesthood, iBronzeWorking, iMasonry, iFishing, iArchery, iAgriculture, iSailing, iConstruction, iLuxuryTrade, 
	iCurrency, iIronWorking, iAstronomy, iOrganisedReligion, iWriting, iAlphabet, iCasteSystem, iElephantTraining, ], 
	# Macedon
	[iStabilityStable, iFreeTradeTech, iAnimalHusbandry, iPottery, iMining, iPriesthood, iBronzeWorking, iMasonry, iFishing, iSailing, iAgriculture, iConstruction, iLuxuryTrade, iCurrency, 
	iIronWorking, iWriting, iAlphabet, iAstronomy, iSiegeEngines, iInfantryTactics, iMilitaryDrill, ], 
	# Makuria
	[iStabilityStable, iFreeTradeTech, iAnimalHusbandry, iPottery, iMining, iPriesthood, iBronzeWorking, iMasonry, iFishing, iArchery, iAgriculture, iSailing, iNavalWarfare, iConstruction, 
	iLuxuryTrade, iCurrency, iCodeOfLaws, iMetalCasting, iIronWorking, iAstronomy, iOrganisedReligion, iWriting, iAlphabet,  iMarksmanship, ], 
	# Himyarites
	[iStabilityStable, iFreeTradeTech, iAnimalHusbandry, iPottery, iMining, iPriesthood, iBronzeWorking, iMasonry, iFishing, iArchery, iAgriculture, iSailing, iNavalWarfare, iConstruction, 
	iLuxuryTrade, iCurrency, iCodeOfLaws, iMetalCasting, iIronWorking, iAstronomy, iOrganisedReligion, iWriting, iAlphabet, ], 
	# Shu
	[iStabilityStable, iFreeTradeTech, iAnimalHusbandry, iPottery, iMining, iPriesthood, iBronzeWorking, iMasonry, iFishing, iArchery, iSiegeEngines, iAgriculture, iHorticulture, 
	iCropRotation, iCalendar, iHorsemanship, iConstruction, iLuxuryTrade, iMonarchy, iCurrency, iMetalCasting, iIronWorking, iAstronomy, iOrganisedReligion, iWriting, iAlphabet, 
	iMathematics, iLiterature, iJurisprudence, iMarksmanship, iInfantryTactics, iSelectiveBreeding, iBridgeBuilding, iScaleArmor, iCodeOfLaws, ], 
	# Wu
	[iStabilityStable, iFreeTradeTech, iAnimalHusbandry, iPottery, iMining, iPriesthood, iBronzeWorking, iMasonry, iFishing, iArchery, iSiegeEngines, iAgriculture, iHorticulture, 
	iCropRotation, iCalendar, iHorsemanship, iSailing, iConstruction, iLuxuryTrade, iMonarchy, iCurrency, iMetalCasting, iIronWorking, iAstronomy, iOrganisedReligion, iWriting, iAlphabet, 
	iMathematics, iLiterature, iJurisprudence, iMarksmanship, iInfantryTactics, iSelectiveBreeding, iBridgeBuilding, iScaleArmor, iCodeOfLaws, ], 
	# Hepthalites
	[iStabilityStable, iFreeTradeTech, iAnimalHusbandry, iPottery, iMining, iPriesthood, iBronzeWorking, iArchery, iHorsemanship, iHorseArchery, iLuxuryTrade, iIronWorking, iCurrency, 
	iSelectiveBreeding, iMarksmanship, iScaleArmor, iCavalryTactics, iTheStirrup, ],
	# Xianbei
	[iStabilityUnstable, iFreeTradeTech, iAnimalHusbandry, iPottery, iMining, iPriesthood, iBronzeWorking, iArchery, iHorsemanship, iHorseArchery, iLuxuryTrade, iIronWorking, iCurrency, 
	iSelectiveBreeding, iFishing, iConstruction, ],
	# Huns
	[iStabilityStable, iFreeTradeTech, iAnimalHusbandry, iPottery, iMining, iPriesthood, iBronzeWorking, iArchery, iAgriculture, iHorsemanship, iHorseArchery, iLuxuryTrade, iIronWorking, 
	iCurrency, iSelectiveBreeding, iMarksmanship, iTheStirrup, ], 
	# Avars
	[iStabilityStable, iFreeTradeTech, iAnimalHusbandry, iPottery, iMining, iPriesthood, iBronzeWorking, iArchery, iAgriculture, iHorsemanship, iHorseArchery, iLuxuryTrade, iIronWorking, 
	iCurrency, iSelectiveBreeding, iMarksmanship, iTheStirrup, ], 
	# Rouran
	[iStabilityStable, iFreeTradeTech, iAnimalHusbandry, iPottery, iMining, iPriesthood, iBronzeWorking, iArchery, iAgriculture, iHorsemanship, iHorseArchery, iLuxuryTrade, iIronWorking, 
	iCurrency, iSelectiveBreeding, iMarksmanship, iTheStirrup, ], 
	# Vakataka
	[iStabilityStable, iFreeTradeTech, iAnimalHusbandry, iPottery, iMining, iPriesthood, iBronzeWorking, iMasonry, iFishing, iArchery, iSiegeEngines, iMarksmanship, iAgriculture, 
	iHorticulture, iCropRotation, iCasteSystem, iCalendar, iHorsemanship, iSailing, iConstruction, iLuxuryTrade, iMonarchy, iVassalage, iCurrency, iCodeOfLaws, iIronWorking, 
	iAstronomy, iOrganisedReligion, iMonasticism, iWriting, iAlphabet, iMathematics, iLiterature, iPhilosophy, iElephantTraining, ], 
	# Song
	[iStabilityStable, iFreeTradeTech, iAnimalHusbandry, iPottery, iMining, iPriesthood, iBronzeWorking, iMasonry, iFishing, iArchery, iSiegeEngines, iMarksmanship, iAgriculture, 
	iHorticulture, iCropRotation, iCalendar, iHorsemanship, iSailing, iConstruction, iLuxuryTrade, iMonarchy, iVassalage, iCurrency, iCodeOfLaws, iStateReligion, iIronWorking, iAstronomy, 
	iOrganisedReligion, iMonasticism, iWriting, iAlphabet, iMathematics, iLiterature, iPhilosophy, ], 
	# Magadha
	[iStabilityStable, iFreeTradeTech, iAnimalHusbandry, iPottery, iMining, iPriesthood, iBronzeWorking, iMasonry, iFishing, iArchery, iAgriculture, iSailing, iConstruction, iLuxuryTrade, 
	iCurrency, iIronWorking, iAstronomy, iOrganisedReligion, iWriting, iAlphabet, iCasteSystem, ], 
	# Rebel Rome
	[iStabilityStable, iFreeTradeTech, iAnimalHusbandry, iPottery, iMining, iPriesthood, iBronzeWorking, iMasonry, iFishing, iAgriculture, iSailing, iConstruction, iLuxuryTrade, iCurrency, 
	iIronWorking, iAstronomy, iWriting, iAlphabet, iMilitaryDrill, iSiegeEngines, ], 
	# Pallavas
	[iStabilityStable, iFreeTradeTech, iAnimalHusbandry, iPottery, iMining, iPriesthood, iBronzeWorking, iMasonry, iFishing, iArchery, iMarksmanship, iAgriculture, 
	iHorticulture, iCalendar, iHorsemanship, iCropRotation, iCasteSystem, iElephantTraining, iSailing, iConstruction, iLuxuryTrade, iMonarchy, iCurrency, 
	iStateReligion, iMetalCasting, iIronWorking, iOrganisedReligion, iWriting, iAlphabet, ], 
	# Kalabhras
	[iStabilityStable, iFreeTradeTech, iAnimalHusbandry, iPottery, iMining, iPriesthood, iBronzeWorking, iMasonry, iFishing, iArchery, iMarksmanship, iAgriculture, 
	iHorticulture, iCalendar, iHorsemanship, iCropRotation, iCasteSystem, iElephantTraining, iSailing, iConstruction, iLuxuryTrade, iMonarchy, iCurrency, 
	iStateReligion, iMetalCasting, iIronWorking, iOrganisedReligion, iWriting, iAlphabet, ], 
	# 32 Saxons
	[iStabilityStable, iFreeTradeTech, iAnimalHusbandry, iPottery, iMining, iPriesthood, iBronzeWorking, iMasonry, iFishing, iArchery, iSiegeEngines, iAgriculture, iHorticulture, 
	iCropRotation, iCalendar, iHorsemanship, iSelectiveBreeding, iTheStirrup, iConstruction, iLuxuryTrade, iMonarchy, iVassalage, iSerfdom, iCurrency, iCodeOfLaws, iMetalCasting, 
	iIronWorking, iSteelWorking, iWriting, ], 
	# Western Rome
	[iStabilityStable, iFreeTradeTech, iAnimalHusbandry, iPottery, iMining, iPriesthood, iBronzeWorking, iMasonry, iFishing, iAgriculture, iSailing, iConstruction, iLuxuryTrade, 
	iCurrency, iIronWorking, iAstronomy, iWriting, iAlphabet, iMilitaryDrill, iSiegeEngines, ], 
	# Moors
	[iStabilityStable, iFreeTradeTech, iAnimalHusbandry, iPottery, iMining, iPriesthood, iBronzeWorking, iMasonry, iFishing, iArchery, iSiegeEngines, iMarksmanship, 
	iAgriculture, iHorticulture, iCropRotation, iCalendar, iHorsemanship, iSelectiveBreeding, iTheStirrup, iSailing, iNavalWarfare, iConstruction, iEngineering, iLuxuryTrade, iMonarchy, 
	iVassalage, iCurrency, iCodeOfLaws, iStateReligion, iMetalCasting, iIronWorking, iSteelWorking, iAstronomy, iOrganisedReligion, iMonasticism, iTheology, iMysticism, iWriting, iAlphabet, 
	iMathematics, iTheocracy, iLiterature, iPhilosophy, iCavalryTactics, iScaleArmor, ], 
	# 26 Champa 18
	[iStabilityStable, iFreeTradeTech, iAnimalHusbandry, iPottery, iMining, iPriesthood, iBronzeWorking, iMasonry, iFishing, iArchery, iAgriculture, iConstruction, iLuxuryTrade, 
	iMetalCasting, iIronWorking, iOrganisedReligion, iWriting, iAlphabet, iHorticulture, iSailing, iFunanUP, ],
	
 ]




# SPECIALISTS

iSettledSlave = 13

# FEATURES
iNumFeatures = 9
(iIce,
iJungle,
iTropicalForest,
iOasis,
iFloodPlains,
iForest,
iWoodland,
iDenseForest, 
iMarsh, ) = range (iNumFeatures)
 
 
 
 
# UNITS

iNumUnits = 167
(iSettler, 
iWorker, 
iSlave, 
iSpy, 
iAssassin,
iCaravan, 
iIncenseMerchant,
iInquisitor, 
iPilgrim, 
iJewishMissionary, 
iZoroastrianMissionary, 
iHinduMissionary, 
iBuddhistMissionary, 
iConfucianMissionary, 
iHellenicMissionary, 
iTaoistMissionary, 
iJainMissionary, 
iChristianMissionary, 
iManicheanMssionary, 
iIslamicMissionary, 
iApostle, 
iRelic, 
iJavelinman,
iJavelinman_Persian, 
iJavelinman_Mediterranean,
iJavelinman_East_Asian, 
iJavelinman_Indian, 
iJavelinman_African,
iAnnameseAmbusher, 
iAntigonidPeltast, # 1 unique javelinman
iJavelinman_Southeast_Asian, 
iArcher, 
iSlinger, 
iArcher_East_Asian, 
iArcher_African, 
iArcher_European, 
iArcher_Greek,
iArcher_Arab,
iArcher_Indian,
iNubiaLongbowman, 
iChokonu, 
iTarimBowman, 
iPandyanVillavar, # 4 unique archers
iMarksman, 
iMarksman_East_Asian, 
iMarksman_Persian, 
iMarksman_Indian, 
iMarksman_Arab,
iAuLacCrossbowman, 
iBambooArcher,
iAxeman, 
iAxeman_Goth, 
iAxeman_Teutonic, 
iAxeman_Indian,
iAxeman_East_Asian, 
iFalxman,
iGalatianInfantry,
iGallicWarrior, 
iKshatriya, 
iMaccabee, 
iFunanSurinSoldier, # 6 unique axemen
iSwordsman, 
iLombardMilitia, 
iByzantineFeodorati, 
iSwordsman_East_Asian, 
iSwordsman_Indian, 
iOstrogothSwordsman, 
iJinDaoInfantry,
iHaniwa,
iFrankThrowingAxeman, # 5 unique swordsmen
iHeavySwordsman, 
iHeavySwordsman_East_Asian, 
iHeavySwordsman_Indian, 
iGhanaSoninkeWarrior, 
iSpearman, 
iSpearman_East_Asian, 
iSpearman_African, 
iSpearman_European, 
iSpearman_Indian, 
iSpearmanGoth, 
iSpearman_Southeast_Asian, 
iAxumSarawit, 
iTibetMonk,
iPonticUazali, # 2 unique spearmen
iHeavySpearman, 
iHeavySpearman_Arab, 
iHeavySpearman_Indian,
iHeavySpearman_East_Asian, 
iHeavySpearman_Greek,
iHeavySpearman_Athenian,
iHeavySpearman_Corinthian,
iHeavySpearman_Spartan,
iMacedonianPhalanx, 
iLegionary, 
iHoplite, 
iQinInfantry, # 3 unique heavy spearmen
iPikeman, 
iShenwuGuard, 
iChariot, 
iKalinkaWarChariot, # 1 unique chariot
iSkirmisher, 
iSkirmisher_Arab, 
iHorseman, 
iHorseman_Scythian, 
iHorseman_Sarmatian, 
iHorseman_Xiongnu, 
iChosonHorseman, 
iAzatavrear, 
iHetairoi, 
iNumidianCavalry, # 4 unique horsemen
iHorseArcher, 
iHorseArcher_Scythian, 
iHorseArcher_Xiongnu, 
iHorseArcher_Indian,
iHorseArcher_Sarmatian,
iShivatir, 
iHorseArcher_Kushan, 
iCordobanBerber, 
iHeavyHorseArcher, 
iHeavyHorseArcher_Generic,
iTibetKhampa, 
iGokturkWarrior,
iLancer, 
iVandalMountedWarrior, 
iVisigothComitatus, 
iArabiaGhazi,
iGoguryeoGaemamusa, 
iLancer_Syrian, 
iLancer_Frankish, 
iSassanidCataphract, 
iHeavyLancer, 
iHeavyLancer_Frankish, 
iKhazarArsiyah,
iCamelRider, 
iBedouinCamelRider, 
iCamelArcher, 
iWarElephant,
iDeccanElephantRider,
iIntoxicatedElephant,
iArmoredElephant,
iCatapult, 
iTrebuchet, 
iWorkBoat, 
iGalley, 
iPirateGalley, 
iDhow, 
iWarGalley, 
iGreatGalley, 
iRoundship, 
iBaghlah,
iBalangay,
iGreatProphet, 
iGreatProphet2, 
iGreatProphet3, 
iGreatArist, 
iGreatArtist2,
iGreatScholar, 
iGreatScholar2, 
iGreatMerchant, 
iGreatMerchant2, 
iGreatEngineer, 
iGreatGeneral, 
iGreatGeneral2, 
iGreatGeneral3, 
iGreatGeneral4, 
iGreatGeneral5, 
iGreatSpy) = range(iNumUnits)

# mercenaries are only taken from this pool; duplicates = more common
lMercenaries = [ 
iJavelinman_Mediterranean,
iJavelinman_Indian, 
iJavelinman_African, 
iJavelinman_East_Asian, 
iAxeman_Teutonic, 
iAxeman_Indian,
iAxeman_East_Asian, 
iSwordsman,
iSwordsman_East_Asian,
iSwordsman_Indian, 
iHeavySwordsman,
iHeavySwordsman_East_Asian, 
iHeavySwordsman_Indian, 
iSpearman_East_Asian, 
iSpearman_African, 
iSpearman_European, 
iSpearman_Indian, 
iHeavySpearman_Indian, 
iHeavySpearman_East_Asian,
iSlinger, 
iArcher_East_Asian,
iArcher_African,
iArcher_European,
iArcher_Greek,
iArcher_Indian,
iMarksman_East_Asian, 
iMarksman_Persian, 
iMarksman_Indian, 
iHorseman,  
iHorseman_Scythian,  
iHorseman_Sarmatian,  
iHorseman_Xiongnu, 
iNumidianCavalry, 
iHorseArcher,  
iHorseArcher_Scythian,  
iHorseArcher_Sarmatian,   
iHorseArcher_Xiongnu, 
iWarElephant, 
iHeavySpearman_Greek,
iHeavySpearman_Athenian,
iHeavySpearman_Corinthian,
iHeavySpearman_Spartan,
iGalley, 
iDhow, 
iWarGalley, 
iRoundship ]

# RESOURCES

iNumResources = 55
(iHorse, iIron, iCopper, iSulfur, iMarble, iStone, iClam, iCrab, iCow, iDeer, iFish, iPig, iRice, iSheep, iWheat, iBarley, 
iDye, iFur, iGold, iIncense, iSilk, iSilver, iPepper, iSugar, iWine, iWhale, iHemp, iCotton, iHoney, iSalt, iOlives, 
iCitrus, iApples, iDates, iGems, iPearls, iIvory, iOpium, iCinnamon, iSorghum, iCharcoal, iCamel, iTimber, iTea, iHellenicWisdom, iJainWisdom, iHinduWisdom, 
iBuddhistWisdom, iTaoistWisdom, iConfucianWisdom, iZoroastrianWisdom, iJewishWisdom, iChristianWisdom, iManicheanWisdom, iIslamicWisdom) = range(iNumResources)

# IMPROVEMENTS

iTribalVillage = 3
iFarm = 4
iMine = 7
iWorkshop = 8
iWindmill = 9
iWatermill = 10
iPlantation = 11
iOrchard = 12
iQuarry = 13
iPasture = 14
iCottage = 19
iHamlet = 20
iVillage = 21
iTown = 22
iFort = 23
iWaterRoute = 25

# BUILDINGS

iNumBuildings = 186
(iPalace, iForbiddenPalace, #1
iInvasionProject, #2
iWalls, iCelticDun, iMaccabeeKotel, #5
iCastle, iDacianDava, #7
iBarracks, iStratopedon, iArmyCamp, #10
iArcheryRange, iNubianBowyer, #12
iStable, iParthianHorseBreeder, #14
iGranary, #15
iAqueduct, iFunanCanal, iPandyanKalyani, #18
iPublicBaths, #19
iHospital, iGuptaPharmacist, #21
iLighthouse, #22
iHarbor, iSriPort, iCarthageCothon, #25
iDrydock, iVandalShipyard, #27
iCourthouse, iVisigothSynod, iVietnamCommunalHouse, iFrankDukeResidence, #31
iBlacksmith, iSassanidMineralWorkshop, iQinBronzeworks, iPorcelainWorkshop, iBactrianGoldsmith, #36
iFoundry, #37
iMonument, iGojoseonDolmen, iPonticMithraticAltar, iAxumStele, iMauryanEdict, iGokturkOrkhonInscription, iArmeniaVank, iSatavahanaStatue, iEgyptianObelisk, #46
iAlchemistsLab, #47
iLibrary, iKalinkaJainLibrary, iKushanGandharaSchool, iChalukyanCaveTemple, #51
iObservatory, #52
iUniversity, iHanShufaStudio, iTibetGompa, # 55
iFairground, iTocharianSilkRoute, iSabaFunduq, #58
iRacingTrack, iHippodrome, iTangPavilion, iGhanaGriot, iJapanJinja, #63
iMarket, iRomanForum, iAntigonidAgora, iArabiaBazaar, #67
iBank, iKhazarYarmaq, #69
iTanner, #70
iTextileMill, iGoguryeoHanbokMaker, #72
iDungeon, #73
iJewishTemple, iJewishCathedral, iJewishMonastery, iJewishReliquary, iJewishShrine, #78
iZoroastrianTemple, iZoroastrianCathedral, iZoroastrianMonastery, iZoroastrianReliquary, iZoroastrianShrine, #83
iConfucianTemple, iConfucianCathedral, iConfucianMonastery, iConfucianReliquary, iConfucianShrine, #88
iHellenicTemple, iHellenicCathedral, iHellenicMonastery, iHellenicReliquary, iHellenicShrine, #93
iBuddhistTemple, iBuddhistCathedral, iBuddhistMonastery, iBuddhistReliquary, iBuddhistShrine, # 98
iHinduTemple, iHinduCathedral, iHinduMonastery, iHinduReliquary, iHinduShrine, #103
iTaoistTemple, iTaoistCathedral, iTaoistMonastery, iTaoistReliquary, iTaoistShrine, #108
iJainTemple, iJainCathedral, iJainMonastery, iJainReliquary, iJainShrine, #113
iChristianTemple, iChristianCathedral, iChristianMonastery, iChristianReliquary, iChristianShrine, #118
iManicheanTemple, iManicheanCathedral, iManicheanMonastery, iManicheanReliquary, iManicheanShrine, #123
iIslamicTemple, iIslamicCathedral, iIslamicMonastery, iIslamicReliquary, iIslamicShrine, #128
iHellenicAcademy, iJainAcademy, iHinduAcademy, iBuddhistAcademy, iTaoistAcademy, iConfucianAcademy, iZoroastrianAcademy, iJewishAcademy, iChristianAcademy, iManicheanAcademy, iIslamicAcademy, # 139
iPlague, #140
iGrainMarket, iFishMarket, iClothMarket, iSpiceMarket, iArtisansQuarter, iTradesmensQuarter, #146
iHeroicEpic, iNationalEpic, iMilitaryAcademy, iDenOfSpies, iRoyalTomb, iRoyalMint, iMedicalSchool, 
iKhajuraho, iPyramids, iTempleOfArtemis, iHangingGardens, iIshtarGate, iParthenon, iColossus, iGreatWall, iTerracottaArmy, iGreatLighthouse, iGreatLibrary, iTrajansColumn, #165
iColosseum, iArchimedesWorkshop, iUnitedNations, iSpiralMinaret, iHouseOfWisdom, iTombOfKhalid, iDhamekStupa, iNalandaUniversity, #173
iHagiaSophia, iBamyanBuddha, iDomeOfTheRock, iUmayyadMosque, iIronPillar, iQalehDokhtar, iGrandCanal, #180
iBorobudur, iTheodosianWalls, iShwedagonPaya, #183
iPyramidsFunctionBuilding, iColossusFunctionBuilding) = range(iNumBuildings)

# REGIONS for RFC RiseAndFall, RFC Stability, RFC AIWars, MEM Religions and MEM Regional Recruitment

iNumRegions = 134
(rNoRegion, rCaledonia, rHibernia, rBritannia, rScania, rAquitania, rGaul, rSeptimania, rIberia, rGermania, rNItaly, rSicily, rGreece, rIllyricum, rThrace, rDacia, rSlavia, rAsia, rArmenia, 
rSyria, rMesopotamia, rArabia, rArabiaFelix, rJudea, rEgypt, rLibya, rAfrica, rMauretania, rNubia, rAxum, rPunt, rSahara, rAethiopia, rGuinea, rMedia, rPersia, rParthia, rArachosia, rSogdiana, 
rSindh, rGandhara, rPunjab, rThar, rMagadha, rBangala, rKalinka, rKerala, rTamilNadu, rAvanti, rDeccan, rLanka, rTibet, rTarim, rBirma, rFunan, rAnnam, rMalaya, rSumatra, rJava, rBorneo, 
rPhilipines, rChu, rQi, rYan, rZhao, rWei, rQin, rHan, rNanYue, rNepal, rPamir, rFerghana, rJin, rGoguryeo, rYamato, rEmishi, rHokkaido, rScythianSteppe, rSarmatianSteppe, rMongolianSteppe, 
rSiberia, rCaucasus, rIslands, rAustralia, rTaiwan, rAtlanticOcean, rNorthSea, rBalticSea, rMediterraneanSea, rBlackSea, rCaspianSea, rAralSea, rRedSea, rPersianGulf, rIndianOcean, 
rSouthChinaSea, rYellowSea, rSeaOfJapan, rPacificOcean, rBactria, rMargiana, rCrimea, rSaurashtra, rShu, rBa, rMinYue, rGansu, rMakan, rBuyeo, rBaetica, rLusitania, rSItaly, rSulawesi, rPapua, 
rWu, rMaldives, rCyprus, rCrete, rRhodes, rSardinia, rCorsica, rMallorca, rPontus, rCappadocia, rAndhra, rNumidia, rMalta, rChampa, rNanzhao, rAssam, rQinghai, rMacedonia, rMoesia, rGedrosia) = range(iNumRegions)

lMediterraneanRegions = [rMacedonia, rBaetica, rIberia, rMallorca, rNumidia, rAfrica, rLibya, rEgypt, rJudea, rSyria, rCappadocia, rAsia, rCyprus, rRhodes, rThrace, rCrete, rGreece, rIllyricum, rNItaly, rSItaly, rSicily, rSeptimania, rCorsica, rSardinia]
lWesternMediterraneanRegions = [rBaetica, rIberia, rMallorca, rNumidia, rAfrica, rIllyricum, rNItaly, rSItaly, rSicily, rSeptimania, rCorsica, rSardinia]
lEasternMediterraneanRegions = [rMacedonia, rLibya, rEgypt, rJudea, rSyria, rCappadocia, rAsia, rCyprus, rRhodes, rThrace, rCrete, rGreece]
lPersianRegions = [rMesopotamia, rMedia, rPersia, rParthia, rArachosia, rMargiana, rBactria, rSogdiana]
lGreaterIndianRegions = [rTamilNadu, rKerala, rAndhra, rDeccan, rKalinka, rMagadha, rAvanti, rBangala, rNepal, rPunjab, rSaurashtra, rSindh, rGandhara, rArachosia, rBactria, rLanka, rBirma]
lIndianRegions = [rTamilNadu, rKerala, rAndhra, rDeccan, rKalinka, rMagadha, rAvanti, rBangala, rNepal, rPunjab, rSaurashtra, rSindh, rGandhara, rLanka]
lSouthIndianRegions = [rTamilNadu, rKerala, rAndhra, rDeccan, rKalinka, rLanka]
lCentralAsianRegions = [rMargiana, rBactria, rSogdiana, rFerghana, rTarim, rSarmatianSteppe]
lGreaterChineseRegions = [rTarim, rMongolianSteppe, rGansu, rQin, rZhao, rWei, rYan, rQi, rShu, rBa, rChu, rWu, rNanYue, rMinYue, rAnnam, rBuyeo, rGoguryeo]
lChineseRegions = [rGansu, rQin, rZhao, rWei, rYan, rQi, rShu, rBa, rChu, rWu, rNanYue, rMinYue]
lEastAfricanRegions = [rEgypt, rNubia, rAxum, rArabiaFelix]
lEasternChristianRegions = [rMesopotamia, rArmenia, rMedia, rPersia, rParthia, rArachosia, rMargiana, rSogdiana, rTarim]
lSouthEastAsianRegions = [rSumatra, rJava, rBorneo, rMalaya, rFunan, rAnnam]
lNearJewishRegions = [rJudea, rEgypt, rArabiaFelix, rAxum, rMesopotamia, rSyria, rArmenia, rCappadocia, rRhodes, rAsia, rPontus, rThrace, rGreece, rIllyricum, rCrete, rSItaly, rAfrica, rLibya, rSicily]
lFartherJewishRegions = [rPersia, rMedia, rParthia, rArachosia, rMargiana, rSogdiana, rKerala, rSaurashtra, rTamilNadu, rTarim]

# Region lists: replacement for RFC TL/BR stability areas and AI war maps

# Core (spawn) regions = RFC tCoreAreasTL/BR and AIWars +10
lCoreRegions = [
	[rAsia, rMacedonia], # Antigonids
	[rSyria, rMesopotamia], # Seleucids
	[rEgypt], # Egypt
	[rAfrica], # Carthage
	[rMagadha], # Mauryans
	[rKalinka], # Kalinka
	[rQin, rHan], # Qin
	[rBuyeo], # Gojoseon
	[rNubia], # Nubia
	[rArabiaFelix], # Saba
	[rTamilNadu], # Pandyans
	[rPontus], # Pontus
	[rGaul], # Celts
	[rNItaly, rSItaly], # Rome
	[rAnnam], # Vietnam
	[rTarim], # Tocharians
	[rBactria, rMargiana], # Bactria
	[rHan, rQi, rWu], # Han
	[rDeccan], # Satavahana
	[rArmenia], # Armenia
	[rJudea], # Maccabees
	[rParthia, rMedia, rPersia], # Parthia
	[rDacia], # Dacia
	[rGoguryeo, rJin], # Goguryeo
	[rAxum], # Axum
	[rArachosia, rSogdiana, rBactria, rGandhara], # Kushans
	[rFunan], # Funan
	[rHan, rQin, rZhao], # Jin
	[rPersia, rMedia, rMesopotamia], # Sassanids
	[rYamato], # Yamato
	[rMagadha], # Gupta
	[rThrace, rAsia, rGreece, rCappadocia, rPontus, rMacedonia], # Byzantines
	[rAquitania, rIberia], # Visigoths
	[rBaetica, rNumidia], # Vandals
	[rIllyricum, rNItaly], # Ostrogoths
	[rGaul], # Franks
	[rDeccan, rAvanti], # Chalukyans
	[rNItaly], # Lombards
	[rMongolianSteppe, rSarmatianSteppe], # Gokturks
	[rJava, rSumatra], # Srivajaya
	[rScythianSteppe], # Khazars
	[rTibet], # Tibet
	[rHan, rQin, rZhao], # Tang
	[rArabia, rArabiaFelix, rJudea, rSyria], # Arabs
	[rMongolianSteppe], # Xiongnu
	[rNumidia, rMauretania], # Numidia
	[rSindh, rSaurashtra, rGandhara, rPunjab], # Scythians
	[rNanYue, rMinYue], # Nan Yue
	[rMagadha], # Sungas
	[rGreece], # Macedon
	[rNubia], # Makuria
	[rArabiaFelix], # Himyarites
	[rShu, rBa], # Shu
	[rChu, rWu], # Wu
	[rSarmatianSteppe, rSogdiana, rFerghana], # Hepthalites
	[rMongolianSteppe], # Xianbei
	[rScythianSteppe, rDacia, rIllyricum, rGermania], # Huns
	[rIllyricum, rDacia, rScythianSteppe], # Avars
	[rMongolianSteppe, rTarim, rGansu], # Rouran
	[rDeccan], # Vakataka
	[rChu, rWu], # Song
	[rMagadha], # Magadha
	[rNItaly, rSItaly], # Rebel Rome
	[rAndhra], # Pallavas
	[rTamilNadu], # Kalabhras
	[rGermania], # Saxons
	[rNItaly, rSItaly], # Western Rome
	[rBaetica, rMauretania, rNumidia], # Moors
	[rChampa], # Champa
]

# Normal regions = RFC tNormalAreasTL/BR and AIWars +5
lNormalRegions = [
	[rThrace, rSyria, rPontus, rCappadocia, rRhodes, rCrete, rCyprus, rGreece], # Antigonids
	[rAsia, rGreece, rJudea, rEgypt, rMedia, rArmenia, rPersia, rArachosia, rCyprus, rCrete, rRhodes, rPontus, rCappadocia, rParthia, rMargiana, rMacedonia, rGedrosia], # Seleucids
	[rNubia, rJudea, rLibya, rCyprus, rCrete, rRhodes, rSyria, rCappadocia], # Egypt
	[rBaetica, rSicily, rMauretania, rSardinia, rCorsica, rMallorca, rLibya, rNumidia, rIberia, rLusitania, rMalta], # Carthage
	[rGandhara, rSindh, rAvanti, rKalinka, rArachosia, rBangala, rAndhra, rPunjab, rGedrosia], # Mauryans
	[rDeccan, rAvanti, rTamilNadu, rAndhra], # Kalinka
	[rZhao, rShu, rBa, rYan, rChu, rQi, rMinYue, rNanYue, rWu], # Qin
	[rGoguryeo, rYan, rJin], # Gojoseon
	[rAxum, rEgypt], # Nubia
	[rMakan, rArabia], # Saba
	[rKerala, rLanka, rAndhra], # Pandyans
	[rAsia, rThrace, rCappadocia, rCaucasus, rCrimea], # Pontus
	[rIberia, rNItaly, rIllyricum, rAquitania, rSeptimania], # Celts
	[rGreece, rMacedonia, rAsia, rSyria, rJudea, rEgypt, rLibya, rAfrica, rBaetica, rIllyricum, rIberia, rLusitania, rSicily, rCyprus, rCrete, rRhodes, rSardinia, rCorsica, rMallorca, rThrace, rCappadocia, rNumidia, rSeptimania, rPontus, rAquitania, rGaul, rMalta], # Rome
	[rNanYue, rFunan, rChampa], # Vietnam
	[rFerghana, rGansu, rSogdiana], # Tocharians
	[rGandhara, rArachosia, rPunjab, rSindh, rSogdiana, rFerghana, rGedrosia], # Bactria
	[rZhao, rYan, rNanYue, rAnnam, rShu, rBa, rMinYue, rGansu, rQin, rChu, rTarim, rGoguryeo, rBuyeo], # Han
	[rKerala, rSaurashtra, rAndhra, rMagadha, rAvanti], # Satavahana
	[rCaucasus, rSyria, rCappadocia], # Armenia
	[rSyria, rArabia, ], # Maccabees
	[rMesopotamia, rArmenia, rSyria, rMargiana, rSindh, rArachosia, rBactria, rGedrosia], # Parthia
	[rThrace, rIllyricum, rMoesia, rMacedonia], # Dacia
	[rBuyeo, rJin, rYan], # Goguryeo
	[rNubia, rPunt, rArabiaFelix], # Axum
	[rSindh, rPunjab, rMagadha, rMargiana, rParthia, rSaurashtra, rFerghana, rGedrosia], # Kushans
	[rBirma, rAnnam, rChampa], # Funan
	[rYan, rQi, rChu, rWu, rBa, rNanYue], # Jin
	[rParthia, rArmenia, rSyria, rJudea, rEgypt, rSogdiana, rAsia, rArmenia, rMargiana, rBactria, rArachosia, rGedrosia], # Sassanids
	[rEmishi], # Yamato
	[rPunjab, rDeccan, rKalinka, rAvanti, rAndhra, rBangala], # Gupta
	[rSyria, rMoesia, rJudea, rEgypt, rLibya, rCyprus, rCrete, rRhodes, rSardinia, rCorsica, rMallorca, rIllyricum], # Byzantines
	[rLusitania, rBaetica, rGaul, rSeptimania, rMallorca], # Visigoths
	[rMauretania, rSicily, rAfrica, rMallorca, rSardinia], # Vandals
	[rSeptimania, rSItaly, rGreece, rThrace, rDacia, rMoesia, rMacedonia], # Ostrogoths
	[rSeptimania, rGermania, rNItaly, rSardinia, rCorsica, rMallorca, rAquitania], # Franks
	[rAvanti, rKerala, rAndhra], # Chalukyans
	[rSItaly, rSicily, rIllyricum, rGermania, rSeptimania], # Lombards
	[rTarim, rGansu, rYan, rZhao, rBuyeo, rSogdiana], # Gokturks
	[rBorneo, rMalaya], # Srivajaya
	[rCaucasus, rArmenia, rDacia, rCrimea, rSarmatianSteppe], # Khazars
	[rNepal, rShu, rGansu, rBirma], # Tibet
	[rQin, rChu, rWu, rYan, rNanYue, rAnnam, rMinYue, rGansu, rTarim, rBuyeo], # Tang
	[rLibya, rAfrica, rPersia, rMedia, rParthia, rArachosia, rEgypt, rMesopotamia, rNumidia, rMargiana, rSindh, rGedrosia], # Arabs
	[rBuyeo, rYan, rZhao, rGansu, rTarim, rQinghai], # Xiongnu
	[rAfrica, rLibya], # Numidia
	[rArachosia, rBactria, rAvanti, rPunjab, rMargiana, rSogdiana, rGedrosia], # Scythians
	[rChu, rWu, rAnnam], # Nan Yue
	[rBangala, rPunjab, rAvanti, rKalinka], # Sungas
	[rThrace, rAsia, rSItaly], # Macedon
	[rEgypt, rAxum], # Makuria
	[rArabia, rAxum, rMakan], # Himyarites
	[rQin, rHan, rChu, rQi], # Shu
	[rBa, rShu, rHan, rQi], # Wu
	[rParthia, rArachosia, rBactria, rSindh, rTarim, rGedrosia, rMargiana, rBactria, rGandhara, rSindh, rArachosia], # Hepthalites
	[rBuyeo, rYan, rZhao, rGansu, rTarim, rQinghai], # Xianbei
	[rCaucasus, rSarmatianSteppe, rThrace, rMoesia], # Huns
	[rNItaly, rThrace, rGreece, rGermania, rMoesia], # Avars
	[rFerghana, rQin, rZhao, rYan, rSarmatianSteppe], # Rouran
	[rKerala, rSaurashtra, rAvanti, rAndhra], # Vakataka
	[rBa, rShu, rHan, rQi], # Song
	[rGandhara, rSindh, rAvanti, rKalinka, rBangala], # Magadha
	[rGreece, rMoesia, rAsia, rSyria, rJudea, rEgypt, rLibya, rAfrica, rBaetica, rIllyricum, rIberia, rSeptimania, rLusitania, rSicily, rCyprus, rCrete, rRhodes, rSardinia, rCorsica, rMallorca, rThrace, rNumidia], # Rebel Rome
	[rKalinka, rTamilNadu, rMagadha, rDeccan], # Pallavas
	[rKerala, rDeccan, rAndhra], # Kalabhras
	[rGaul, rScania, rNItaly, rIllyricum], # Saxons
	[rAfrica, rBaetica, rIllyricum, rIberia, rLusitania, rSicily, rSardinia, rCorsica, rMallorca, rNumidia, rSeptimania, rAquitania, rGaul], # Western Rome
	[rSeptimania, rAquitania, rAfrica, rSicily], # Moors
	[rFunan], # Champa
]

# Broader regions = RFC tBroaderAreasTL/BR and AIWars +2 srpt: no stability effect but allowable as AI conquest
lBroaderRegions = [
	[rCappadocia, rDacia, rJudea, rMesopotamia, rEgypt, rArmenia, rSItaly, rSicily], # Antigonids
	[rSindh, rGandhara, rBactria, rLibya, rNubia, rThrace, rIllyricum, rMoesia], # Seleucids
	[rAfrica, rArabia, rArabiaFelix, rGreece, rThrace, rSItaly, rSicily, rMacedonia], # Egypt
	[rSItaly, rNItaly, rGreece, rThrace, rAsia, rCappadocia, rSyria, rJudea, rEgypt, rCyprus, rCrete, rRhodes], # Carthage
	[rSaurashtra, rTamilNadu, rKerala, rBactria, rMargiana], # Mauryans
	[rMagadha, rBangala], # Kalinka
	[rGansu, rTarim, rAnnam, rBuyeo, rGoguryeo, rJin], # Qin
	[rZhao, rQi, rHan], # Gojoseon
	[rLibya, rArabia, rArabiaFelix], # Nubia
	[rJudea, rSyria, rMesopotamia, rEgypt, rNubia, rAxum], # Saba
	[rDeccan, rKalinka], # Pandyans
	[rGreece, rArmenia, rSyria, rDacia, rMoesia, rMacedonia], # Pontus
	[rBritannia, rGermania, rLusitania], # Celts
	[rBritannia, rGermania, rMesopotamia, rArmenia, rCrimea, rArabia, rArabiaFelix], # Rome
	[rChu, rShu, rBa, rBirma], # Vietnam
	[], # Tocharians
	[rParthia, rSaurashtra], # Bactria
	[rMongolianSteppe, rFerghana, rTibet, rBirma, rJin], # Han
	[rPunjab, rTamilNadu, rKalinka, rSindh], # Satavahana
	[rAsia, rPontus, rMedia, rMesopotamia, rJudea], # Armenia
	[rArabiaFelix, rMesopotamia, rEgypt], # Maccabees
	[rSogdiana, rGandhara, rSaurashtra, rJudea, rEgypt, rCappadocia, rAsia, rPontus, rCaucasus], # Parthia
	[rGreece, rNItaly, rGermania], # Dacia
	[rZhao, rQi, rHan], # Goguryeo
	[rEgypt, rArabia, rMakan, rSindh], # Axum
	[rTarim, rPersia, rMedia, rSarmatianSteppe, rAvanti], # Kushans
	[rSumatra, rJava, rNanYue], # Funan
	[rGansu, rTarim, rAnnam, rMongolianSteppe, rBuyeo, rGoguryeo, rJin], # Jin
	[rJudea, rArabia, rArabiaFelix, rEgypt, rCappadocia, rAsia, rPontus, rMakan, rSindh], # Sassanids
	[rJin, rGoguryeo, rBuyeo, rQi, rYan], # Yamato
	[rSindh, rArachosia, rGandhara, rBactria, rSaurashtra, rKerala, rTamilNadu, rGedrosia], # Gupta
	[rMesopotamia, rArmenia, rAfrica, rSItaly, rNItaly, rSicily, rBaetica, rIberia, rSeptimania, rNumidia, rMauretania], # Byzantines
	[rMauretania, rNumidia, rAfrica, rSicily, rSardinia, rCorsica, rSItaly, rNItaly], # Visigoths
	[rSItaly, rLibya, rCorsica], # Vandals
	[rAsia, rGermania, rGaul, rAquitania], # Ostrogoths
	[rIberia, rSItaly, rIllyricum], # Franks
	[rMagadha, rSaurashtra, rPunjab, rTamilNadu], # Chalukyans
	[rGaul, rAquitania, rCorsica, rSardinia], # Lombards
	[rScythianSteppe, rBactria, rMargiana, rParthia], # Gokturks
	[rBirma, rFunan, rLanka, rBangala, rChampa], # Srivajaya
	[rMargiana, rMedia, rThrace, rSogdiana, rFerghana], # Khazars
	[rTarim, rAnnam, rBangala], # Tibet
	[rFerghana, rGoguryeo, rMongolianSteppe, rSarmatianSteppe, rSogdiana], # Tang
	[rCappadocia, rBaetica, rIberia, rLusitania, rPontus, rAsia, rSogdiana, rArmenia, rCaucasus], # Arabs
	[], # Xiongnu
	[rAfrica, rLibya], # Numidia
	[rMagadha, rDeccan, rPersia, rFerghana, rSogdiana, rParthia], # Scythians
	[rChu, rWu, rAnnam], # Nan Yue
	[rGandhara, rSindh, rSaurashtra, rAndhra, rKerala, rTamilNadu], # Sungas
	[rThrace, rAsia, rSItaly], # Macedon
	[rEgypt, rAxum], # Makuria
	[rArabia, rAxum, rMakan], # Himyarites
	[rQin, rHan, rChu, rQi], # Shu
	[rBa, rShu, rHan, rQi], # Wu
	[rParthia, rBactria, rSindh, rFerghana, rTarim], # Hepthalites
	[], # Xianbei
	[rGreece, rAsia, rGaul, rNItaly], # Huns
	[], # Avars
	[rSogdiana, rBuyeo, rTibet], # Rouran
	[rKalinka, rSindh, rTamilNadu], # Vakataka
	[rBa, rShu, rHan, rQi], # Song
	[rGandhara, rSindh, rAvanti, rKalinka, rArachosia, rBangala], # Magadha
	[rGreece, rAsia, rSyria, rJudea, rEgypt, rLibya, rAfrica, rBaetica, rIllyricum, rIberia, rSeptimania, rLusitania, rSicily, rCyprus, rCrete, rRhodes, rSardinia, rCorsica, rMallorca, rThrace, rNumidia], # Rebel Rome
	[rKalinka, rTamilNadu, rMagadha, rDeccan], # Pallavas
	[rKerala, rDeccan, rAndhra], # Kalabhras
	[], # Saxons
	[rBritannia, rGermania], # Western Rome
	[rLibya, rSItaly], # Moors
	[rAnnam, rMalaya], # Champa
]

# Target regions: no stability effect but AI wars + 10
lTargetRegions = [
	[rThrace, rGreece, rSyria], # Antigonids
	[rJudea], # Seleucids
	[], # Egypt
	[rIberia, rSicily, rCyprus, rCrete, rRhodes, rSardinia, rCorsica, rMallorca], # Carthage
	[rGandhara, rSindh, rAvanti, rKalinka], # Mauryans
	[rMagadha], # Kalinka
	[rHan, rShu, rZhao, rChu, rQi, rWu], # Qin
	[rYan], # Gojoseon
	[rAxum, rEgypt], # Nubia
	[], # Saba
	[rKerala, rLanka], # Pandyans
	[rAsia, rCrimea, rCaucasus, rCappadocia], # Pontus
	[rGaul, rIberia, rNItaly, rIllyricum], # Celts
	[rSItaly, rNItaly, rSicily, rSeptimania, rIllyricum, rGreece, rAsia, rThrace, rSyria, rJudea, rEgypt, rLibya, rAfrica, rIberia, rSeptimania, rGaul, rCyprus, rCrete, rRhodes, rSardinia, rCorsica, rMallorca], # Rome
	[], # Vietnam
	[], # Tocharians
	[rGandhara, rPunjab], # Bactria
	[rChu, rZhao, rYan, rNanYue, rAnnam, rShu, rBa, rQin, rWu, rGansu, rTarim, rBuyeo], # Han
	[rKerala, rSaurashtra], # Satavahana
	[rCaucasus], # Armenia
	[], # Maccabees
	[rMesopotamia, rSogdiana, rArmenia, rSyria], # Parthia
	[rThrace, rIllyricum], # Dacia
	[rBuyeo], # Goguryeo
	[rNubia, rPunt, rArabiaFelix], # Axum
	[rArachosia, rSindh, rPunjab, rMagadha, rFerghana], # Kushans
	[rBirma, rAnnam], # Funan
	[rZhao, rNanYue, rAnnam, rChu, rWu], # Jin
	[rPersia, rMesopotamia, rMedia, rParthia, rMargiana, rArmenia, rArachosia, rSogdiana, rAsia, rSyria, rJudea, rEgypt, rCappadocia, rPontus], # Sassanids
	[rEmishi], # Yamato
	[rBangala, rPunjab, rDeccan, rKalinka, rSindh, rAvanti, rSaurashtra], # Gupta
	[rAfrica, rSicily, rSItaly, rIllyricum], # Byzantines
	[rLusitania, rBaetica, rGaul, rAquitania], # Visigoths
	[rMauretania, rSicily], # Vandals
	[rSeptimania, rSItaly, rGreece, rThrace], # Ostrogoths
	[rSeptimania, rGermania, rNItaly], # Franks
	[rDeccan, rMagadha], # Chalukyans
	[], # Lombards
	[rTarim, rGansu, rYan, rZhao, rGoguryeo, rSogdiana], # Gokturks
	[rBirma, rBorneo], # Srivajaya
	[rCaucasus, rArmenia, rDacia, rCrimea, rSarmatianSteppe], # Khazars
	[rNepal, rShu, rGansu, rTarim, rBirma], # Tibet
	[rChu, rQin, rZhao, rYan, rNanYue, rAnnam], # Tang
	[rArabiaFelix, rArabia, rJudea, rSyria, rMesopotamia, rEgypt, rPersia, rMedia, rParthia, rLibya, rAfrica, rMargiana, rNumidia, rBaetica, rArachosia, rIberia, rSindh], # Arabs
	[rMongolianSteppe, rBuyeo, rYan, rZhao, rGansu, rQin, rTarim], # Xiongnu
	[], # Numidia
	[rArachosia, rGandhara, rBactria, rPersia, rPunjab, rMargiana, rSogdiana], # Scythians
	[rChu, rWu, rAnnam], # Nan Yue
	[rBangala, rPunjab, rAvanti], # Sungas
	[rThrace, rAsia, rSItaly], # Macedon
	[rEgypt, rAxum], # Makuria
	[rArabia, rAxum, rMakan], # Himyarites
	[rQin, rHan, rChu, rQi], # Shu
	[rBa, rShu, rHan, rQi], # Wu
	[rParthia, rArachosia, rBactria, rSindh, rFerghana, rTarim], # Hepthalites
	[rMongolianSteppe, rBuyeo, rYan, rZhao, rGansu, rQin, rTarim], # Xianbei
	[rGermania, rIllyricum, rThrace, rGaul, rAquitania, rSeptimania, rNItaly, rSItaly, rCrimea, rGreece, rAsia], # Huns
	[rGermania, rIllyricum, rThrace, rGaul, rAquitania, rSeptimania, rNItaly, rSItaly, rCrimea, rGreece, rAsia], # Avars
	[rTarim, rGansu, rBuyeo, rYan, rZhao, rSogdiana], # Rouran
	[rKerala, rSaurashtra], # Vakataka
	[rBa, rShu, rHan, rQi], # Song
	[], # Magadha
	[rGreece, rAsia, rThrace, rSyria, rJudea, rEgypt, rLibya, rAfrica, rIberia, rSeptimania, rGaul, rCyprus, rCrete, rRhodes, rSardinia, rCorsica, rMallorca], # Rebel Rome
	[], # Pallavas
	[], # Kalabhras
	[rGaul], # Saxons
	[rSItaly, rNItaly, rSicily, rSeptimania, rIllyricum, rAfrica, rIberia, rSeptimania, rGaul, rSardinia, rCorsica, rMallorca], # Western Rome
	[], # Moors
	[], # Champa
]



lRevealRegions = [
	[rSyria, rMesopotamia, rAsia, rGreece, rJudea, rEgypt, rArmenia, rCrimea, rCyprus, rCrete, rThrace, rCappadocia, rPontus, rRhodes, rBlackSea, rMediterraneanSea], # Antigonids
	[rSyria, rMesopotamia, rAsia, rGreece, rJudea, rEgypt, rMedia, rArmenia, rPersia, rArachosia, rGedrosia, rMargiana, rParthia, rCyprus, rCrete, rThrace, rPontus, rCappadocia, rRhodes, rMediterraneanSea], # Seleucids
	[rArabia, rEgypt, rLibya, rJudea, rSyria, rMesopotamia, rAsia, rGreece, rNubia, rCyprus, rCrete, rThrace, rMediterraneanSea, rRedSea], # Egypt
	[rAfrica, rIberia, rSicily, rMauretania, rLibya, rEgypt, rJudea, rSyria, rAsia, rGreece, rSicily, rIberia, rSeptimania, rSItaly, rBaetica, rMallorca, rCorsica, rSardinia, rMediterraneanSea], # Carthage
	[rMagadha, rPunjab, rGandhara, rSindh, rAvanti, rKalinka, rArachosia, rGedrosia, rBangala], # Mauryans
	[rDeccan, rMagadha, rTamilNadu, rKerala, rKalinka], # Kalinka
	[rGansu, rQin, rShu, rHan, rZhao, rBa, rQi], # Qin
	[rGoguryeo, rBuyeo, rYan], # Gojoseon
	[rNubia, rAxum, rEgypt], # Nubia
	[rArabiaFelix, rRedSea], # Saba
	[rTamilNadu, rKerala, rLanka], # Pandyans
	[rPontus, rCappadocia, rAsia, rCaucasus, rArmenia, rThrace, rGreece, rCyprus, rCrete, rRhodes, rMesopotamia, rMedia, rPersia, rCrimea, rBlackSea], # Pontus 
	[rSeptimania, rAquitania, rGaul, rIberia, rNItaly, rIllyricum], # Celts
	[rNItaly, rSItaly, rSicily, rGreece, rAsia, rIllyricum, rThrace, rSyria, rJudea, rEgypt, rLibya, rAfrica, rIberia, rSeptimania, rCorsica, rSardinia, rMediterraneanSea], # Rome
	[rAnnam, rChampa], # Vietnam
	[rTarim, rFerghana], # Tocharians
	[rSogdiana, rGandhara, rArachosia, rGedrosia, rMargiana, rBactria, rParthia, rMedia, rPersia, rMesopotamia, rSyria], # Bactria
	[rHan, rChu, rQin, rQi, rZhao, rYan, rBa, rWu, rShu], # Han
	[rAvanti, rDeccan, rSindh, rKerala, rKalinka, rMagadha, rTamilNadu, rThar], # Satavahana
	[rArmenia, rCaucasus, rMedia, rMesopotamia, rSyria], # Armenia
	[rEgypt, rJudea, rSyria, rMesopotamia], # Maccabees
	[rParthia, rMedia, rArachosia, rGedrosia, rMesopotamia, rPersia, rSogdiana, rArmenia, rSyria, rMargiana], # Parthia
	[rDacia, rThrace, rIllyricum], # Dacia
	[rGoguryeo, rJin], # Goguryeo
	[rAxum, rNubia, rPunt, rArabiaFelix, rRedSea], # Axum
	[rSogdiana, rGandhara, rArachosia, rGedrosia, rSindh, rPunjab, rFerghana, rTarim, rMargiana, rBactria], # Kushans
	[rFunan, rAnnam, rChampa], # Funan
	[rHan, rChu, rQin, rQi, rZhao, rYan, rNanYue, rAnnam, rShu, rBa, rWu], # Jin
	[rPersia, rMedia, rArachosia, rGedrosia, rMesopotamia, rParthia, rArmenia, rSyria, rJudea, rEgypt, rSogdiana, rMargiana, rSindh], # Sassanids
	[rEmishi, rYamato, rJin], # Yamato
	[rMagadha, rBangala, rPunjab, rDeccan, rKalinka, rSindh, rAvanti], # Gupta
	[rMacedonia, rNItaly, rSItaly, rSicily, rGreece, rAsia, rIllyricum, rDacia, rThrace, rSyria, rJudea, rMesopotamia, rEgypt, rLibya, rAfrica, rMauretania, rIberia, rSeptimania, rAquitania, rGaul, rArmenia, rCorsica, rSardinia, rCrete, rCyprus, rMediterraneanSea, rBlackSea, rCappadocia], # Byzantines
	[rIberia, rSeptimania, rNItaly, rBaetica, rLusitania], # Visigoths
	[rIberia, rBaetica, rAfrica, rSicily, rSardinia, rMallorca], # Vandals
	[rIllyricum, rDacia, rNItaly, rSItaly, rThrace], # Ostrogoths
	[rGaul, rAquitania, rSeptimania, rGermania, rNItaly, rIberia], # Franks
	[rAvanti, rDeccan, rKerala, rTamilNadu, rAndhra, rKalinka, rMagadha], # Chalukyans
	[rNItaly, rSItaly, rGermania], # Lombards
	[rMongolianSteppe, rSarmatianSteppe, rTarim, rGansu, rZhao, rYan, rBuyeo], # Gokturks
	[rSumatra, rMalaya, rJava, rBorneo], # Srivajaya
	[rScythianSteppe, rCaucasus, rArmenia, rDacia, rCrimea, rSarmatianSteppe], # Khazars
	[rTibet, rShu, rBirma, rQinghai, rTarim], # Tibet
	[rHan, rChu, rQin, rQi, rZhao, rYan, rNanYue, rAnnam, rWu, rBa, rShu, rGansu, rMinYue], # Tang
	[rArabia, rSyria, rMesopotamia, rJudea, rEgypt, rArabiaFelix, rRedSea], # Arabs
	[rMongolianSteppe, rBuyeo, rYan, rZhao, rGansu, rQin, rTarim], # Xiongnu
	[], # Numidia
	[], # Scythians
	[], # Nan Yue
	[], # Sungas
	[], # Macedon
	[rNubia, rAxum, rEgypt], # Makuria
	[rArabiaFelix, rRedSea], # Himyarites
	[], # Shu
	[], # Wu
	[], # Hephthalites
	[rMongolianSteppe, rBuyeo, rYan, rZhao, rGansu, rQin, rTarim], # Xianbei
	[], # Huns
	[], # Avars
	[], # Rouran
	[rAvanti, rDeccan, rSindh, rKerala, rKalinka], # Vakataka
	[], # Song
	[], # Magadha
	[], # Rebel Rome
	[], # Pallavas
	[], # Kalabhras
	[], # Saxons
	[], # Western Rome
	[], # Moors
	[], # Champa
]


lSpecialRegions = [
	[], # Antigonids
	[], # Seleucids
	[], # Egypt
	[], # Carthage
	[], # Mauryans
	[], # Kalinka
	[rHan, rZhao], # Qin
	[], # Gojoseon
	[], # Nubia
	[], # Saba
	[], # Pandyans
	[], # Pontus
	[], # Celts
	[rSicily, rSeptimania], # Rome
	[], # Vietnam
	[], # Tocharians
	[], # Bactria
	[], # Han
	[], # Satavahana
	[], # Armenia
	[], # Maccabees
	[rMesopotamia], # Parthia
	[], # Dacia
	[], # Goguryeo
	[], # Axum
	[rMargiana, rArachosia, rSogdiana, rFerghana, rBactria], # Kushans
	[], # Funan
	[], # Sassanids
	[], # Yamato
	[rQi, rYan], # Jin
	[], # Gupta
	[], # Byzantines
	[], # Visigoths
	[], # Vandals
	[], # Ostrogoths
	[], # Franks
	[], # Chalukyans
	[], # Lombards
	[], # Gokturks
	[], # Srivajaya
	[], # Khazars
	[], # Tibet
	[], # Tang
	[], # Arabs
	[], # Xiongnu
	[], # Numidia
	[rArachosia], # Scythians
	[], # Nan Yue
	[], # Sungas
	[], # Macedon
	[], # Makuria
	[], # Himyarites
	[], # Shu
	[], # Wu
	[rArachosia], # Hepthalites
	[], # Xianbei
	[], # Huns
	[], # Avars
	[], # Rouran
	[], # Vakataka
	[], # Song
	[], # Magadha
	[], # Rebel Rome
	[], # Pallavas
	[], # Kalabhras
	[], # Saxons
	[], # Western Rome
	[], # Moors
	[], # Champa
]

# Cities in these regions like to be independent and in case of secession will declare independence before other cities
# (unless they are in the civ's core area)
lUnrulyRegions = [rCaledonia, rHibernia, rGermania, rScania, rSlavia, rScythianSteppe, rSarmatianSteppe, rMongolianSteppe, rSiberia, rSahara]

# Mediterranean provinces used by Roman conquerors
lMediterraneanProvinces = [rAfrica, rLibya, rEgypt, rJudea, rSyria, rAsia, rThrace, rGreece, rCappadocia]

iArea_Mediterranean = 1000
iArea_IndianOcean = 1001
iArea_PacificOcean = 1002
iArea_African = 1003
iArea_Greek = 1004
iArea_Persian = 1005
iArea_Scythian = 1006
iArea_Sarmatian = 1007
iArea_Mongolian = 1008
iArea_Indian = 1009
iArea_East_Asian = 1010

mercRegions = {
	iArea_Mediterranean: set([rNItaly, rSItaly, rGreece, rAsia, rSyria, rJudea, rEgypt, rLibya, rAfrica, rMauretania, rIberia, rSeptimania, rSicily]),
	iArea_IndianOcean: set([rPunt, rAxum, rArabiaFelix, rArabia, rPersia, rArachosia, rSindh, rAvanti, rKerala, rLanka, rTamilNadu, rKalinka, rBangala, rBirma, rMalaya, rSumatra]),
	iArea_PacificOcean: set([rChu, rQi, rJin, rGoguryeo, rYamato, rEmishi, rTaiwan, rNanYue, rAnnam, rSumatra, rMalaya, rJava]),
	iArea_African: set([rMauretania, rAfrica, rLibya, rEgypt, rNubia, rAxum, rPunt, rSahara, rAethiopia, rGuinea]),
	iArea_Greek: set ([rAsia, rArmenia, rMedia, rMesopotamia, rNItaly, rSItaly, rSicily, rGreece, rThrace]),
	iArea_Persian: set ([rPersia, rMedia, rParthia, rArachosia, rBactria, rMargiana, rSogdiana]),
	iArea_Scythian: set ([rThrace, rCaucasus, rScythianSteppe]),
	iArea_Sarmatian: set ([rMargiana, rSogdiana, rFerghana, rBactria, rParthia, rTarim, rSarmatianSteppe]),
	iArea_Mongolian: set ([rTarim, rGansu, rQin, rZhao, rYan, rBuyeo, rMongolianSteppe]),
	iArea_Indian: set ([rGandhara, rSindh, rPunjab, rSaurashtra, rAvanti, rMagadha, rBangala, rDeccan, rKerala, rTamilNadu, rKalinka]),
	iArea_East_Asian: set ([rTarim, rGansu, rQin, rZhao, rYan, rBuyeo, rGoguryeo, rQi, rShu, rBa, rHan, rChu, rWu, rNanYue, rMinYue, rAnnam, rFunan]), 
	iHorseman: set([rSyria, rMesopotamia, rAsia, rArmenia, rMedia, rParthia, rSogdiana, rFerghana, rTarim, rQin, rZhao, rCrimea, rScythianSteppe, rSarmatianSteppe, rMongolianSteppe, rLibya, rAfrica, rMauretania, rIberia]),
	iJavelinman: set([rAsia, rArmenia, rMedia, rMesopotamia, rNItaly, rSItaly, rSicily]),
	iJavelinman_Indian: set([rGandhara, rSindh, rThar, rPunjab, rSaurashtra, rAvanti, rMagadha, rNepal, rBangala, rDeccan, rKalinka, rTamilNadu, rKerala]),
	iJavelinman_Mediterranean: set([rNItaly, rSItaly, rGreece, rAsia, rSyria, rJudea, rEgypt, rLibya, rAfrica, rMauretania, rIberia, rSeptimania, rSicily]),
	iJavelinman_African: set([rMauretania, rAfrica, rLibya, rEgypt, rNubia, rAxum, rPunt, rSahara, rAethiopia, rGuinea]),
	iAxeman: set ([rAsia, rArmenia, rMedia, rMesopotamia, rNItaly, rSItaly, rSicily]),
	iAxeman_Teutonic: set([rGermania, rGaul, rIllyricum, rDacia, rThrace]),
	iAxeman_Indian: set([rGandhara, rSindh, rThar, rPunjab, rSaurashtra, rAvanti, rMagadha, rNepal, rBangala, rDeccan, rKalinka, rTamilNadu, rKerala]),
	iAxeman_East_Asian: set([rQin, rHan, rYan, rQi, rChu, rGoguryeo, rZhao, rJin, rYamato, rEmishi, rNanYue, rAnnam, rFunan]),
	iJavelinman_East_Asian: set([rQin, rHan, rYan, rQi, rChu, rGoguryeo, rZhao, rJin, rYamato, rEmishi, rNanYue, rAnnam, rFunan]),
	iSwordsman: set([rAsia, rArmenia, rMedia, rMesopotamia, rNItaly, rSItaly, rSicily]),
	iSwordsman_East_Asian: set([rQin, rHan, rYan, rQi, rChu, rGoguryeo, rZhao, rJin, rYamato, rEmishi, rNanYue, rAnnam, rFunan]),
	iSwordsman_Indian: set([rGandhara, rSindh, rThar, rPunjab, rSaurashtra, rAvanti, rMagadha, rNepal, rBangala, rDeccan, rKalinka, rTamilNadu, rKerala]),
	iHeavySwordsman: set([rAsia, rArmenia, rMedia, rMesopotamia, rNItaly, rSItaly, rSicily]),
	iHeavySwordsman_East_Asian: set([rQin, rHan, rYan, rQi, rChu, rGoguryeo, rZhao, rJin, rYamato, rEmishi, rNanYue, rAnnam, rFunan]),
	iHeavySwordsman_Indian: set([rGandhara, rSindh, rThar, rPunjab, rSaurashtra, rAvanti, rMagadha, rNepal, rBangala, rDeccan, rKalinka, rTamilNadu, rKerala]),
	iSpearman: set([rAsia, rArmenia, rMedia, rMesopotamia, rNItaly, rSItaly, rSicily]),
	iSpearman_East_Asian: set([rQin, rHan, rYan, rQi, rChu, rGoguryeo, rZhao, rJin, rYamato, rEmishi, rNanYue, rAnnam, rFunan]),
	iSpearman_African: set([rMauretania, rAfrica, rLibya, rEgypt, rNubia, rAxum, rPunt, rSahara, rAethiopia, rGuinea]),
	iSpearman_European: set([rGermania, rGaul, rIllyricum, rDacia, rThrace, rAquitania, rSeptimania, rIberia]),
	iSpearman_Indian: set([rGandhara, rSindh, rThar, rPunjab, rSaurashtra, rAvanti, rMagadha, rNepal, rBangala, rDeccan, rKalinka, rTamilNadu, rKerala]),
	iHeavySpearman: set([rAsia, rArmenia, rMedia, rMesopotamia,rNItaly, rSItaly, rSicily]),
	iHeavySpearman_Greek: set ([rAsia, rArmenia, rMedia, rMesopotamia, rNItaly, rSItaly, rSicily, rGreece, rThrace]),
	iHeavySpearman_Athenian: set ([rAsia, rArmenia, rMedia, rMesopotamia, rNItaly, rSItaly, rSicily, rGreece, rThrace]),
	iHeavySpearman_Corinthian: set ([rAsia, rArmenia, rMedia, rMesopotamia, rNItaly, rSItaly, rSicily, rGreece, rThrace]),
	iHeavySpearman_Spartan: set ([rAsia, rArmenia, rMedia, rMesopotamia, rNItaly, rSItaly, rSicily, rGreece, rThrace]),
	iHeavySpearman_Arab: set([rArabia, rArabiaFelix, rSyria, rJudea, rEgypt, rMesopotamia]), 
	iHeavySpearman_Indian: set([rGandhara, rSindh, rThar, rPunjab, rSaurashtra, rAvanti, rMagadha, rNepal, rBangala, rDeccan, rKalinka, rTamilNadu, rKerala]), 
	iHeavySpearman_East_Asian: set([rQin, rHan, rYan, rQi, rChu, rGoguryeo, rZhao, rJin, rYamato, rEmishi, rNanYue, rAnnam, rFunan]),
	iArcher: set([rAsia, rArmenia, rMedia, rMesopotamia, rNItaly, rSItaly, rSicily]),
	iArcher_East_Asian: set([rQin, rHan, rYan, rQi, rChu, rGoguryeo, rZhao, rJin, rYamato, rEmishi, rNanYue, rAnnam, rFunan]),
	iArcher_African: set([rMauretania, rAfrica, rLibya, rEgypt, rNubia, rAxum, rPunt, rSahara, rAethiopia, rGuinea]),
	iArcher_European: set([rGermania, rGaul, rIllyricum, rDacia, rThrace, rAquitania, rSeptimania, rIberia]),
	iArcher_Greek: set ([rAsia, rArmenia, rCaucasus, rMedia, rMesopotamia, rNItaly, rSItaly, rSicily, rGreece, rThrace]),
	iArcher_Arab: set([rArabia, rArabiaFelix, rSyria, rJudea, rEgypt, rMesopotamia]), 
	iArcher_Indian: set([rGandhara, rSindh, rThar, rPunjab, rSaurashtra, rAvanti, rMagadha, rNepal, rBangala, rDeccan, rKalinka, rTamilNadu, rKerala]),
	iMarksman: set([rAsia, rArmenia, rMedia, rMesopotamia, rNItaly, rSItaly, rSicily]), 
	iMarksman_East_Asian: set([rQin, rHan, rYan, rQi, rChu, rGoguryeo, rZhao, rJin, rYamato, rEmishi, rNanYue, rAnnam, rFunan]), 
	iMarksman_Persian: set([rMesopotamia, rMedia, rPersia, rParthia, rArachosia, rMargiana]), 
	iMarksman_Indian: set([rGandhara, rSindh, rThar, rPunjab, rSaurashtra, rAvanti, rMagadha, rNepal, rBangala, rDeccan, rKalinka, rTamilNadu, rKerala]), 
	iMarksman_Arab: set([rArabia, rArabiaFelix, rSyria, rJudea, rEgypt, rMesopotamia]),  
	iHorseman: set([rArmenia, rMedia, rParthia, rSogdiana, rFerghana, rTarim, rQin, rZhao, rCrimea, rScythianSteppe, rSarmatianSteppe, rMongolianSteppe]),
	iHorseman_Scythian: set([rArmenia, rMedia, rParthia, rSogdiana, rFerghana, rCrimea, rScythianSteppe, rSarmatianSteppe]),
	iHorseman_Sarmatian: set([rArmenia, rMedia, rParthia, rSogdiana, rFerghana, rTarim, rQin, rCrimea, rScythianSteppe, rSarmatianSteppe, rMongolianSteppe]),
	iHorseman_Xiongnu: set([rFerghana, rTarim, rQin, rZhao, rSarmatianSteppe, rMongolianSteppe, rGoguryeo]), 
	iHorseArcher: set([rArmenia, rMedia, rParthia, rSogdiana, rFerghana, rTarim, rQin, rZhao, rCrimea, rScythianSteppe, rSarmatianSteppe, rMongolianSteppe]),
	iHorseArcher_Scythian: set([rArmenia, rMedia, rParthia, rSogdiana, rFerghana, rCrimea, rScythianSteppe, rSarmatianSteppe]),
	iHorseArcher_Sarmatian: set([rArmenia, rMedia, rParthia, rSogdiana, rFerghana, rTarim, rQin, rCrimea, rScythianSteppe, rSarmatianSteppe, rMongolianSteppe]),
	iHorseArcher_Xiongnu: set([rFerghana, rTarim, rQin, rZhao, rSarmatianSteppe, rMongolianSteppe, rGoguryeo]),
	iBedouinCamelRider: set([rArabia, rArabiaFelix, rSyria, rJudea, rEgypt, rLibya]), 
	iNumidianCavalry: set([rNumidia, rAfrica, rMauretania]),
	iSlinger: set([rNumidia, rMauretania, rBaetica, rIberia, rAfrica, rSicily, rSardinia, rMallorca]),
	}

# Companies will only settle in their preferred regions
lCompanyRegions = [
# Grain Merchants
[], #all
# Fish Merchants
[], 
# Cloth Merchants
[],
# Spice Merchants
[],
# Master Artisans
[],
# Master Tradesmen
[],
]

# Plague
lBlackDeathRegions = [ rThrace, rAsia, rSyria, rMesopotamia, rJudea, rEgypt, rNubia, rLibya, rAfrica, rGreece, rNItaly, rSItaly, rSicily, rSeptimania ]

lBlackDeathSurvivors = [ iFranks, iGupta, iArabs, iCelts, iPandyans, iChalukyans, iSeleucids, iYamato, iSaba ]
lBlackDeathStarters = [ iEgypt, iCarthage, iParthia, iGoguryeo ]

# Egyptian UHV
lEasternMediterraneanRegions = [ rLibya, rEgypt, rJudea, rSyria, rAsia, rThrace, rGreece, rCyprus, rCrete, rRhodes]



tFavorLevelsBlessing = 			(  0,  0,  0,  0,  0,  0,  0,  0,  1,  1)
tFavorLevelsGiftBonus =			(  0,  0,  1,  1,  2,  2,  3,  3,  4,  5)
tFavorLevelsHappinessBonus = 	( -2, -1,  0,  0,  0,  0,  0,  1,  1,  2)
tFavorLevelsStabilityBonus = 	( -5, -2,  0,  0,  0,  1,  2,  3,  4,  5)



lFavorLevelsText = [
	"TXT_KEY_FAVOR_LEVEL_HEATHEN",
	"TXT_KEY_FAVOR_LEVEL_HEATHEN",
	"TXT_KEY_FAVOR_LEVEL_HEATHEN",
	"TXT_KEY_FAVOR_LEVEL_BELIEVER",
	"TXT_KEY_FAVOR_LEVEL_BELIEVER",
	"TXT_KEY_FAVOR_LEVEL_FAITHFUL",
	"TXT_KEY_FAVOR_LEVEL_RIGHTEOUS",
	"TXT_KEY_FAVOR_LEVEL_DEVOTED",
	"TXT_KEY_FAVOR_LEVEL_BLESSED",
	"TXT_KEY_FAVOR_LEVEL_SAINT",
	]


