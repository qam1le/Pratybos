# -*- coding: utf-8 -*-
"""
4 pratybos 20 uzduotis
"""
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
        indeksas = s.index(ltr) #suindeksuojam raides pagal abc eilute
        rez.append(indeksas) #pridedam indeksus, kad galetume grazinti verciu sarasa
    return rez

def index2str(numbers):
    rez = ''
    for number in numbers: #iteracija
        letter = s_reverse[number] #pagal indeksa randama raide
        rez += letter #i tuscia sarasa sudedamos raides pagal indeksa
    print (rez) #galutinis ats

#3 uzd 
abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
raktas = [8, 12]
L_1=[20, 3, 24, 18, 8, 5, 15, 4, 7, 11, 0, 13, 9, 22, 12, 23, 10, 1, 19, 21, 17, 16, 2, 25, 6, 14]
L_2=[8, 13, 24, 18, 9, 0, 7, 14, 10, 11, 19, 25, 4, 17, 12, 21, 15, 3, 22, 2, 20, 16, 23, 1, 6, 5]
s='CEAGBLDIHNQFPJSMKTORZWVYXU'
s_reverse = 'UXYVWZROTKMSJPFQNHIDLBGAEC'
text = 'XQITLZWEKHEFEJZHDFDEOLKSFJVCUEGDMCDHRNCBVKBFWDBUJVJYMRUBBNBLPUZEBCXTCSOUTKBOZDALXSUTAUWZDMOXDGYMDOWDWBLJKSAXBAUIBAQNGJKVXGJHGNHHGRXCVDDQBERISIUSPJIGWBKDOVIGANICYJGRSYSPNDAVXZLOZUCQODOVIYDJGEPOVHWUFUGQXSTVXLFQNRFLPZKWUCWONAYTRCFHANHEXTDDILKCEWDDFUEUJNGJVGZIPKAGTNSUOUIGPHBQOCHHTNFVORUUEGLNVJQHJCTSFYNAYAHEOTDJVQKEIYMPEGEMGCLUJJDTLAHUYDLAZCRXPFIORYKYGQKIY'
decipher(raktas, L_1, L_2, text)
