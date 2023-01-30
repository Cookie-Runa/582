import random

from params import p
from params import g

def keygen():
    sk = 0
    pk = 0
    sk = random.randint(1, p)
    pk = pow(g, sk, p)
    return pk,sk

def encrypt(pk,m):
    c1 = 0
    c2 = 0
    r = random.randint(1, p)
    c1 = pow(g, r, p)
    c2 = (pow(pk, r, p) * (m % p)) % p
    return [c1,c2]

def decrypt(sk,c):
    m = 0
    m = ((c[1] % p) * pow(c[0], -sk, p)) % p
    return m

