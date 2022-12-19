A ="abcdefghijklmnopqrstuvwxyz"

#https://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def i_teksta(M):
    n=M
    text=''
    while n>0:
        ind=n%100
        ind=ind-1
        if (ind>=0) & (ind<len(A)):
            text+=A[ind]
            n=(n-ind+1)//100
        else:
            text+='?'
            n=(n-ind+1)//100            
    return text[::-1]

def decrypt_rabin(p, q, cipher):
    message = []
    for c in cipher:
        #Prane²imai ir sifrai - aibes Zn, n = pq
        n = p * q
        m1 = pow(c, (p + 1) // 4, p)
        m2 = pow(c, (q + 1) // 4, q)
        #u ≡ M (mod p)
        u = modinv(q, p)
        #v ≡ M (mod q)
        v = modinv(p, q)
        #M1 ≡ u (mod p), M1 ≡ v (mod q)
        #x1 ≡ vap + ubq (mod n)
        m_1 = ((m1 * u * q) + (m2 * v * p)) % n
        #M2 ≡ −u (mod p), M2 ≡ v (mod q),
        #x2 ≡ −vap + ubq (mod n),
        m_2 = ((m1 * u * q * -1) + (m2 * v * p)) % n
        #M3 ≡ u (mod p), M3 ≡ −v (mod q),
        m_3 = ((m1 * u * q) + (m2 * v * p * -1)) % n
        #M4 ≡ −u (mod p), M4 ≡ v (mod q)
        m_4 = ((m1 * u * q * -1) + (m2 * v * p * -1)) % n
        message.append([i_teksta(m_1), i_teksta(m_2), i_teksta(m_3), i_teksta(m_4)])
    return message#[i_teksta(m_1), i_teksta(m_2), i_teksta(m_3), i_teksta(m_4)]

p = 79496847203390844133441739
q = 79496847203390844133441987
cipher = [369412936784193964016448726382270848904560824373225]
message = decrypt_rabin(p, q, cipher)
print ("Rabino atsakymas:", message)


#======================BLUMAS GOLDWASSERIS
def private_key(p, q, n):
    #x^2  (mod n)
    # i−1
    x = 0
    while (x**2 - 1) % n != 0:
        x += 1
    return (p, q, x)

def decrypt_blum(C, K, n):
    (C, r) = C
    (p, q, x) = K
    P = []
    for C_i in C:
        #C_i * x^(-r) (mod n)
        M_i = [(C_i[j] * pow(x, -r, n)) % (n) for j in range(len(C_i))]
        P.append(M_i)
    return [bit for block in P for bit in block]

#https://github.com/qam1le/Pratybos/blob/main/8/8.py
def dec_to_bits(d):
    result = []
    bits = [int(x) for x in list('{0:0b}'.format(d))]
    for i in range(0, 8 - len(bits)):
        result.append(0)
    for b in bits:
        result.append(b)
    return result
def bits_to_decimal(bits):
    out = 0
    for bit in bits:
        out = (out << 1) | bit
    return out
#===============
p1 = 78691
q1 = 78707
h = 8
cipher1 = [65, 76, 181, 188, 186, 254, 22, 58, 179, 247, 8, 22, 111]
r = 1412592686 #atsitiktinis sk
n = p * q
cipher_bin = []
for c in cipher1:
     cipher_bin.append(dec_to_bits(c))
#cipher_bin += (r,)

K = private_key(p1, q1, n)
#print(K)
(p, q, x) = K
C = cipher_bin
P = decrypt_blum((C, r), K, n)
print("Blumo Goldwasserio atsakymas:", P)
print(i_teksta(bits_to_decimal(P)))
#'didelis akmuo'
#https://doc.sagemath.org/html/en/reference/cryptography/sage/crypto/public_key/blum_goldwasser.html