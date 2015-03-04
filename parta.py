import hashlib
import base64
import numpy as np

PrevHash='77a22709b4f6ad7c13c1a5c898cb63872ed00be3eadbd94e6b32482fe7518d51'
Contents='11'.encode('hex')
Length="{0:0{1}x}".format(1,8)
difficulty=6



def try_hash(Nonce):
    Hash = hashlib.sha256()
    Hash.update(PrevHash.decode("hex"))
    Hash.update(Contents.decode("hex"))
    Hash.update(Nonce.decode("hex"))
    Hash.update(Length.decode("hex"))
    b = Hash.digest().encode("hex")[0:difficulty]
    ##    print Nonce
    print Hash.digest().encode("hex")
    print b
    if (b=='0'*24):
        return True
    else:
        return False

def loop():
    i=0
    while i<2**64:
        if try_hash(np.uint64(i)):
            print i
            return i
        i+=1
 

#loop()
try_hash(hex(6732080969929779909)[2:][0:-1].zfill(16))
