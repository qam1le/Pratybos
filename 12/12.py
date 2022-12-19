import gmpy2
from math import gcd

A='abcdefghijklmnopqrstuvwxyz'
public = [4640650289117164100520051333566036654627, 2, 2978675639431475214837358429644057997973]
msg1 = 19130107211927040118020119
sig1 = [3594658015327966835087644512794278199790, 3319192495962269328721702216759443138043]
msg2 = 701212001192712010919110119
sig2 = [3594658015327966835087644512794278199790, 143224101638928577828557256037105910993]
c = [109320863373406004233377601232309351335, 1489094878362670937560980717170368864721]

#https://www.geeksforgeeks.org/multiplicative-inverse-under-modulo-m/
def modinv(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

#def convert(text):
#    t=''
#    for r in text:
#        if r in A:
#            ind=A.index(r)+1
#            if ind<10: t=t+'0'+str(ind)
#            else: t=t+str(ind)
#    return int(t,10)     

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

#β^γ γ^δ ≡ α^x(mod p) -> beta^gama gama^beta = alpha^message (mod p)
def valid(key,sig,x):
    b = (pow(key[2], sig[0], key[0]) * pow(sig[0], sig[1], key[0])) % key[0]
    g = pow(key[1], x, key[0])

    if (b == g):
        return b, "Geras"
    else:
        return b,g,"blogas"

def private_key(public_key, sig1, msg1, sig2, msg2):
    n = public_key[0]
    g = public_key[1]
    s1, m1 = sig1[1], msg1
    s2, m2 = sig2[1], msg2
    g_inv = modinv(g, n)
    s_inv = modinv(s1 - s2, n)
    k = (((m1 - m2) * s_inv) % n + n) % n
    return k

def decrypt(cipher, private, public):
    return (cipher[1] * pow(gmpy2.invert(cipher[0], public), private, public)) % public

#msg1_n = convert(msg1)
#msg2_n = convert(msg2)
#print(msg1_n)

#1 punktas
print("1-o paraso validavimas: ", valid(public,sig1,msg1))
print("2-o paraso validavimas: ", valid(public,sig2,msg2))

#2 punktas
#Para²o sudarymas: pasirenkamas atsitiktinis k,(k, p−1) = 1 ir skai£iuojama:
#γ ≡ αk(mod p), δ ≡ (x − aγ)k−1(mod (p − 1)), hγ, δi = sig(x|Kp).
#γ ≡ α^iβ^j(mod p), δ ≡ −γj^−1(mod p − 1), x ≡ −γij^−1(mod p − 1)

#private = private_key(public, sig1, msg1, sig2, msg2)
#print(private)
private = 3319192495962269328721702216759443138043

#3 punktas
msg = decrypt(c, private, public[0])

print("Atsakymas:", msg, i_teksta(msg))