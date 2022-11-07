# -*- coding: utf-8 -*-
"""
4 pratybos 20 užduotis
"""
#eilute - string

def rot(m, a): #sukimosi funkcija
    return (a+m) % 26 #pagal formule

def rotind(rot, a):#sukimosi indeksavimas
    return rot.index(a)

def decipher(raktas, L1, L2, sifras):
    sifroInd = indexing(sifras) #gaunami sifruojamo teksto indeksai
    deText = [] #deciphered Text, sarasas saugoti issifruotam tekstui
    m1 = raktas[0]
    m2 = raktas[1]
    rotInd = 0 #sukimosi indeksas

    for value in sifroInd: #iteracija per sifruojamo teksto elementus, value - elementai
        val = value
        val = rot(m2, val) 
        val = rotind(L2, val)
        val = rot(-m2, val)
        val = rot(m1, val)
        val = rotind(L1, val)
        val = rot(-m1, val)
        #perduodamos reiksmes rot ir rotind funkcijoms
        m1 += 1
        rotInd += 1
        if (rotInd % 26) == 0:
            m2 += 1

        deText.append(val)

    return index2str(deText)

def indexing(text):
    rez = [] #tuscias sarasas
    for ltr in text: #einam per visas raides esancias tekstas eiluteje
        indeksas = abc.index(ltr) #suindeksuojam raides pagal abc eilute
        rez.append(indeksas) #pridedam indeksus, kad galetume grazinti verciu sarasa
    return rez

def index2str(numbers):
    rez = ''
    for number in numbers: #iteracija
        letter = abc[number] #pagal indeksa randama raide
        rez += letter #i tuscia sarasa sudedamos raides pagal indeksa
    print (rez) #galutinis ats
    
#--------------------antrai uzd, kai nezinoma antra rakto dalis

def decipherBF(raktas, L1, L2, sifras, knownTxt):
    sifroInd = indexing(sifras) #gaunami sifruojamo teksto indeksai
    deText = [] #deciphered Text, sarasas saugoti issifruotam tekstui
    m1 = raktas[0]
    m2 = raktas[1]
    rotInd = 0 #sukimosi indeksas

    for value in sifroInd: #iteracija per sifruojamo teksto elementus, value - elementai
        val = value
        val = rot(m2, val) 
        val = rotind(L2, val)
        val = rot(-m2, val) 
        val = rot(m1, val)
        val = rotind(L1, val)
        val = rot(-m1, val)
        #perduodamos reiksmes rot ir rotind funkcijoms
        m1 += 1
        rotInd += 1
        if (rotInd % 26) == 0:
            m2 += 1

        deText.append(val)
        
    return in2Str_BF(deText, knownTxt)

def in2Str_BF(numbers, knownTxt): #index2str bet brute force
    rez = ''
    for number in numbers: 
        letter = abc[number] 
        rez += letter 
        if rez[0:len(knownTxt)] == knownTxt:#range(rez[:len(knownTxt):1]) == knownTxt:
            print (rez)
#------------------------------------------------------------------------------

#-----------------------kintamieji
abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#1uzd------------------------------------------
raktas = [5, 7]
L_1 = [10, 2, 11, 18, 8, 20, 19, 25, 23, 1, 15, 9, 14, 6, 24, 0, 17, 7, 22, 21, 4, 12, 5, 3, 16, 13]
L_2 = [14, 2, 7, 20, 18, 9, 19, 25, 23, 1, 13, 17, 22, 5, 3, 0, 24, 8, 21, 10, 11, 12, 15, 4, 6, 16]
text = 'KJIVCHITIIFZJFYFZDKAHAHCNZPEJJUDGFSCICKNADBBIGNNAEVQOMMBTTAIOUZVFQBLTKLJIBHXEBSUDONHPMYSBTVKEFPQPCMBIBGBPJGDSNKNKAHLBPVGGQNVBZYLDZBYEHBSDTXISAVIDINAMGCLYATMZZNIWISMLAAQOCWFNDIJPAHEOTGMKRJMQENSSCZVKCDQSLDSPNGKDKQDINPTOIXTGITRPNXPFYMSVTGMHGHHFIXWROMVSHZAPJCZKFZQYXXSWFJKILPFUGXYNTTKIFRJCTHCVLRAQTYJIANFULRNQVDHCTXKAFYOVTOHXBSSZLSPFAXDRDKENDLMYKLBWIIVPWWFCEIZUGRITAGYNZJCPTOWDAPQHKCLYPAZKOIMVQINLNHBEKMXZCAOLPOGGGTLQBVSACDUIMC'
#2 uzd------------------------------
#raktas = [4]
#L_1 = [5, 3, 2, 0, 17, 10, 8, 24, 20, 11, 1, 12, 9, 22, 16, 6, 25, 4, 18, 21, 7, 13, 15, 23, 19, 14]
#L_2 = [20, 3, 24, 18, 8, 5, 15, 4, 7, 11, 0, 13, 9, 22, 12, 23, 10, 1, 19, 21, 17, 16, 2, 25, 6, 14]
#text = 'WGSKWSLTZHSODZWQNTACSBDGAEPZAXNKOZXVRAZFBMHGQETGDVWUDRWCTTORPBHRFPRLYIHWFSJWPPCRSAAKBGCFWKCYRQIHSJYSCTXGOOOGCPRKGLDALLGWCAIULOIDAIRCEISOHMQIEDSRMEYHBRNFUMLWLHMFQEVOFQZSYARGKVVZDJIOFOWYZIMZBONTXSYRQZOJFWQANZXFYWZBVVER'
#----------------------------------
if raktas[0] != None and len(raktas) < 2: #jeigu rakto saraso pirmas elementas ne tuscias ir nera daugiau nei 1 elemento
    for num in range(1,27):
        raktas.append(num)
    knownTxt = 'J'
    decipherBF(raktas, L_1, L_2, text, knownTxt) #funkcijos kvietimas, perduodami 5 par
else:
    decipher(raktas, L_1, L_2, text) #funkcijos kvietimas, perduodami 4 par



