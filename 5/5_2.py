# -*- coding: utf-8 -*-
"""
5 pratybos,  22 užduotis 
"""
#--------------kintamieji
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ciphertext = [[15, 91], [3, 80], [18, 75], [6, 95], [17, 83], [7, 64], [9, 69], [15, 75], [18, 91], [1, 84], [7, 66], [27, 82], [14, 75], [30, 84], [31, 80], [11, 74], [11, 88], [24, 84], [27, 72], [15, 95], [5, 74], [18, 83], [25, 82], [18, 83], [9, 77], [5, 65], [1, 84], [15, 86], [2, 71], [19, 71], [23, 68], [31, 84], [13, 65], [9, 92], [16, 81], [3, 79], [1, 84], [27, 66], [3, 74], [7, 76], [3, 80], [1, 85], [27, 82], [28, 85], [1, 78]]
#original ['?', 128]
keys = [128, 1]

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

def add_key(key, alphabet):
    for abc in alphabet:
        if fleisner == abc:
            break
            return True
        if fleisner != abc:
            old_key = key[-1]
            key[-1] = old_key + 1
            return key
    
def decode_ascii(nums):
    ascii_str = ''.join([chr(value) for lofl in nums for value in lofl])
    return ascii_str


fl_check = fleisner(ciphertext,keys) 

while False:
    final_key = add_key(keys, alphabet)
    fl = fleisner(ciphertext,final_key)
    if final_key == True:
        break
    
decoded = decode_ascii(fl)
print("Raktas: ", final_key)
print("Skaitines vertes: ", fl)
print("ASCII: ", decoded)
