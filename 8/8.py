#8 pratybos
#39 uzduotis

#	c8 c7 c6 c5 c4 c3 c2 c1  (laisv)
#	1  0  1  1  0  0  0  0   0
#	1  1  0  0  0  0  0  0   1
#	0  1  0  0  0  0  0  1   1
#	0  0  1  0  0  0  0  0   1
#	0  0  0  1  0  1  1  0   0
#	0  0  0  0  1  0  1  1   0
#	0  0  0  0  0  1  0  1   1
#	0  0  0  0  0  0  1  0   1

cipher = [250, 101, 33, 51, 209, 221, 102, 212, 33, 20, 145, 148, 95, 97, 27, 111, 135, 244, 221, 239, 95, 25, 227, 31, 209, 42, 113, 7, 112, 248, 7, 218, 82, 135, 13, 221, 42, 5, 230, 114, 95, 197, 204, 121, 184, 208, 29, 63, 76, 75, 83, 36, 167, 67, 229, 139, 67, 97, 125, 145, 143, 91, 2, 241, 127, 37, 60, 205, 219, 100, 220, 52, 29, 134, 152, 78, 125, 25, 111, 149, 250, 208, 239, 72, 21, 230, 30, 212, 48, 106, 8, 121, 242, 0, 212, 70, 135, 15, 211, 45, 3, 231, 127, 87, 220, 196, 98, 185, 201, 11, 63, 91, 88, 87, 32, 177, 69, 230, 157, 90, 115, 125, 136, 139, 70, 25, 252, 109, 55, 61, 198, 223, 107, 220, 52, 23, 130, 154, 95, 100, 20, 117, 148, 240, 218, 231, 77, 5, 225, 4, 195, 54, 112, 5, 111, 244, 6, 218, 76, 141, 7, 209, 43, 22, 232, 114, 68, 203, 196, 124, 166, 204, 28, 41, 74, 77, 73, 40, 182, 94, 235, 146, 87, 121, 125, 151, 139, 69, 28, 227, 127, 48, 40, 203, 219, 99, 193, 41, 11, 133, 150, 70, 111, 28, 103, 137, 225, 216, 244, 85, 28, 227, 12, 202, 42, 112]

#ZINOMAS TEKSTAS -> JI cipher[0] = 250, cipher[1] = 101
#bin(ord('J')^250),bin(ord('I')^101)
#10110000 101100 -> 10110000 00101100
registers = [0, 1, 1, 0 ,0 ,0 ,0, 0]
coefficients = [1, 1, 0, 0, 1, 0, 0, 1]

def shift(c,x): # c - coefficients, x - initial state, len(c)=len(x)
    bt=0
    n=len(x)
    for j in range(0,n):
        bt+=c[j]*x[j]
    for j in range(1,n):
        x[n-j]=x[n-1-j]
    x[0]=bt%2
    return x

#pagal https://www.geeksforgeeks.org/break-list-chunks-size-n-python/
#skaldymas i bitus, po 8
def chunks(message, step):
    chunk = [message[i * step:(i + 1) * step] for i in range((len(message) + step - 1) // step )]
    return chunk

def dec_to_bits(decimal):
    result = []
    #bitu srasas
    bits = [int(x) for x in list('{0:0b}'.format(decimal))]
    #sudarom sarasa, 8 bitai, kurie = 0
    for i in range(0, 8):
        result.append(0)
    #sudedame bitus i sarasa
    for b in bits:
        result.append(b)
    return result

def bits_to_dec(bits):
    decimal = 0
    for bit in bits:
        decimal = decimal*2 + int(bit)
    return decimal

#nauja reiksme
shifted = shift(coefficients, registers)
print("Shift:", shifted)

#sarasai binarinems reiksmems saugoti
cipher_bin = []
message_bin = []

#desimtaini keiciam i binarini issikviete funkcija
for c in cipher:
    for bit in dec_to_bits(c):
        cipher_bin.append(bit)

#def c_shift(cipher,shift):
#    result = []
#    for c, s in zip(cipher,shift):
#        result += [c^s] 
#    return result
#message_bin.append(c_shift(cipher_bin,shifted))

for c in cipher_bin:
    message_bin.append(c ^ shifted[0])

#turime issifruota zinute, is binarinio kodo konvertuojam i ascii
message = ''
for m in chunks(message_bin, 8):
    message += chr(bits_to_dec(m))

print(message)