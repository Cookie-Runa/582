import hashlib
import os
import random
import string

def hash_collision(k):
    if not isinstance(k,int):
        print( "hash_collision expects an integer" )
        return( b'\x00',b'\x00' )
    if k < 0:
        print( "Specify a positive number of bits" )
        return( b'\x00',b'\x00' )
   
    #Collision finding code goes here
    letters = string.ascii_letters
    str_x = ''.join(random.choice(letters) for i in range(10))
    x = str_x.encode('utf-8')
    hash_x = hashlib.sha256(x).hexdigest()
    hash_x_bin = bin(int(hash_x, 16))

    str_y = ''.join(random.choice(letters) for i in range(10))
    y = str_y.encode('utf-8')
    hash_y = hashlib.sha256(y).hexdigest()
    hash_y_bin = bin(int(hash_y, 16))


    while hash_y_bin[-k:] != hash_x_bin[-k:]:
        str_y = ''.join(random.choice(letters) for i in range(10))
        y = str_y.encode('utf-8')
        hash_y = hashlib.sha256(y).hexdigest()
        hash_y_bin = bin(int(hash_y, 16))
    return (x, y)
