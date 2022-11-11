# -*- coding: utf-8 -*-
"""
5 pratybos,  22 užduotis 
"""
#--------------kintamieji
ciphertext = [[179, 165], [169, 180], [174, 188], [171, 175], [163, 185], [182, 164], [169, 181], [179, 180], [166, 189], [163, 161], [174, 179], [165, 161], [172, 170], [182, 161], [178, 163], [169, 169], [170, 191], [182, 165], [160, 186], [174, 179], [170, 189], [170, 186], [174, 176], [185, 164], [179, 178], [166, 190], [188, 162], [171, 169], [187, 165], [165, 175], [186, 164], [180, 180], [161, 165], [165, 169], [170, 176], [172, 170], [162, 179], [178, 163], [166, 190], [188, 162], [171, 170], [178, 177], [170, 190], [166, 190], [166, 186], [182, 162], [163, 161], [163, 177], [163, 181], [165, 191], [172, 168]]

#original [88, 224, 175]
keys = [175, 224, 88]

#iteracijos funkcija F = (m|k)^((k//16)&m)
#m - desine puse
#k - iteracijos raktas

def fleisner(text, keys):
    counter = 0
    while counter != len(keys):
        for key in keys:
            for lofl in text: #lofl - list of lists
                right = lofl[1] 
                F = (right|key)^((key//16)&right)
                lofl[1] = F
                lofl[0], lofl[1] = lofl[1], lofl[0] #apkeiciamos puses
        counter += 1
    return text
    
def decode_ascii(nums):
    ascii_str = ''.join([chr(value) for lofl in nums for value in lofl])
    return ascii_str

fl = fleisner(ciphertext,keys)
decoded = decode_ascii(fl)
print("Skaitines vertes: ", fl)
print("ASCII: ", decoded)