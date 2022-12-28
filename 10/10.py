#10 pratybos
#5 uzduotis
from fractions import Fraction

#KINTAMIEJI
#viesasis raktas/sugadintas privatusis
public = [58531478, 2196017, 3737311, 14328587, 24692154, 41749138, 13603354, 41680060]

#private[0], w_1
private1 = 579346

#modulis
p = 80403907

#sifras
cipher = [72374620, 47613388, 72305542, 5504989, 72305542, 5574067, 47613388, 75545329, 3737311, 19536682, 23287206, 62011053, 47613388, 75545329]

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

#naujas kuprines kraustymas
def decrypt(private,cn):
    sv=cn #svoris
    private_len = len(private)-1
    bit = ''
    #N > w1 + w2 + ··· + wn,(t,N) = 1.
    while sv > 0 and 0 <= private_len:
        if private[private_len] <= sv:
            bit += '1'
            sv -= private[private_len]
            private_len -= 1
        else:
            bit += '0'
            private_len -= 1
        
    return (int(bit[::-1].zfill(len(private)),2))

#pagal sage math atsakymus
#https://sagecell.sagemath.org/?z=eJx1UM1q4zAQvhv8DnMJtrvKdkb_CtVe_A7JweRQUqc1a9Rgpwrs068Up9BAK11G38_Mp9mCh05ZJUgay4CT00iGgTDpEjEgKbhVNkFcasdJSQaSjHQkkp6ERiEWTFtEjfuyuKSeyjghdVmcUm1RonBoyqLN0wwXRmqOyWM0CWFTn4ShUpIzUAqls-4eMhK1udMnRgnuvgZ1Smhtk56nxIajZpCmEKES31lT0Eh-2-XEZTH7y2Ok1aksdjnj_BBXJzi-TxBhCLBNmjYsxOFGHDLRXs0v_RGG-W-9Y7HZlAWkM0cflyr4sQ_1rlnT8u59VS3V5W0Y-6T8g_AcXgCffLi58xmOsOvC_snP8Qt67fDLV1TdY2neHNfZcI8HHz4HX63j3H_TDasfXVN__pgCHN6megjnuu82mzXtf_87DuNYLz9rGG-avIfTlCUZbENG8pqGvKbpObz2NbJP6hZh0S-ba0M37JvmP5uMkJg=&lang=sage&interacts=eJyLjgUAARUAuQ==
s = 738678
W = [579346, 621801, 1268013, 2478320, 5033369, 10017993, 20048687, 40100054]
Cn = [16941176, 41989868, 47023237, 67071924, 47023237, 36989863, 41989868, 64516875, 1268013, 21938501, 54486181, 14386127, 41989868, 64516875]

msg = ""
for i in range(0, len(Cn)):
    #desifravimas
    m = decrypt(W, Cn[i]) #private)
    #desimtaine -> ascii
    msg += chr(m)
print ("Issifruotas tekstas:", msg)



#============================================================================================
#NEVEIKIA TAIP KAIP TURI :(
def neveikiantis_fragmentas():
    #senas kuprines kraustymas
    def decrypt(c, key):
        #bitu sudarymas
        m = [0] * 8
        rev = reversed(list(enumerate(key)))
        #i - iteracija range(0-7)
        #k - kuprines svoriai
        for i, k in rev:
            #tikrinamas dydis, jeigu didesnis arba lygus
            if k <= c:
                #tuomet atimame svori
                c -= k
                m[i] = 1 #pagal indeksa, m bitas = 1
        #konvertavimas is bitu i desimtaine
        decimal = 0
        for bits in m:
            decimal = decimal*2 + int(bits)
        return decimal  
    #bendras didziausias dalikilis
    #bdd = math.gcd(cipher[0],p)
    #print("Didziausias bendras daliklis:",bdd)

    #svorio atkurimas
    #s = private1/public[0]%p
    #s = Fraction(private1/public[0])%p
    s = modinv((private1/public[0]),p)

    #sparciai didejanti seka, sutvarkomi svoriai, private=w
    #vi ≡ wi*t (mod N)
    private = []
    for publ in public:
        private.append(modinv((int(s*publ)),p))
        #private.append(int(s * publ) % p)

    #pagal kriptosistemos desifravimo formule
    #C1 ≡ Cs (mod p)
    #naujos kuprines
    #c1 = [(c * s) % p for c in cipher]
    c1 = [modinv((c * s), p) for c in cipher]

    #python ats: [579346, 21736, 36991, 141824, 244403, 413233, 134646, 412550]
    #sage cell: [579346, 621801, 1268013, 2478320, 5033369, 10017993, 20048687, 40100054]

    msg = ""
    for i in range(0, len(c1)):
        #desifravimas
        m = decrypt(private, c1[i]) #private)
        #desimtaine -> ascii
        msg += chr(m)
    print ("Issifruotas tekstas:", msg)