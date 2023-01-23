import hashlib
import os
import string
import random

def hash_preimage(target_string):
    if not all( [x in '01' for x in target_string ] ):
        print( "Input should be a string of bits" )
        return
    
    target_len = len(target_string)
    letters = string.ascii_letters
    str_x = ''.join(random.choice(letters) for i in range(10))
    x = str_x.encode('utf-8')
    hash_x = hashlib.sha256(x).hexdigest()
    hash_x_bin = bin(int(hash_x, 16))

    while  hash_x_bin[-len_target:] != target_string:
        str_x = ''.join(random.choice(letters) for i in range(10))
        x = str_x.encode('utf-8')
        hash_x = hashlib.sha256(x).hexdigest()
        hash_x_bin = bin(int(hash_x, 16))

    return(x)

