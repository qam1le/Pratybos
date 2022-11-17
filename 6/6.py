# -*- coding: utf-8 -*-
"""
6 pratybos,  19 užduotis 
CBC
"""
#--------------kintamieji
ciphertext = [[198, 157], [45, 50], [103, 144], [131, 45], [201, 132], [63, 52], [115, 135], [154, 61], [195, 147], [58, 32], [101, 159], [138, 60], [217, 129], [54, 41], [100, 139], [151, 43], [205, 132], [35, 58], [123, 152], [134, 59], [211, 134], [58, 47], [119, 145], [156, 50], [196, 139], [56, 58], [114, 158], [128, 38], [201, 145], [51, 57], [104, 155], [128, 35], [220, 138], [49, 36], [105, 128], [128, 61], [205, 147], [58, 40], [111, 159], [150, 60], [200, 140], [60, 54], [104, 140], [152, 56], [198, 138], [40, 57], [124, 138], [135, 46], [213, 151], [13, 78]]

#original [204, 255, 106]
keys = [106, 255, 204]
vector = [142, 40]

#iteracijos funkcija F = (m|k)^((m//16)&k)
#m - desine puse
#k - iteracijos raktas

def fleisner(text, keys, vector):
    counter = 0
    while counter != len(keys):
        for key in keys:
            for lofl in text: #lofl - list of lists
                right = lofl[1] 
                F = (right|key)^((right//16)&key) 
                lofl[1] = F
                lofl[0], lofl[1] = lofl[1], lofl[0] #apkeiciamos puses
                #xor 
                xor1 = lofl[0] ^ vector[0] #^ - XOR simbolis python kalboje
                xor2 = lofl[1] ^ vector[1]
                vector[0] = xor1 #priskiriamos naujai gautos reiksmes
                vector[1] = xor2
                lofl[0] = xor1 
                lofl[1] = xor2
                
        counter += 1
    return text

def decode_ascii(nums):
    ascii_str = ''.join([chr(value) for lofl in nums for value in lofl])
    return ascii_str

fl = fleisner(ciphertext,keys, vector)
decoded = decode_ascii(fl)
print("Skaitines vertes: ", fl)
print("ASCII: ", decoded)
