
def encrypt(key,plaintext):
    ciphertext=""
    for c in plaintext:
        ciphertext += chr((ord(c) + key - 65) % 26 + 65)
    return ciphertext

def decrypt(key,ciphertext):
    plaintext=""
    for c in ciphertext:
        plaintext += chr((ord(c) + 65 - key) % 26 + 65)
    return plaintext


