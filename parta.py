import hashlib
import base64
import numpy as np

PrevHash='0000000000000000000000000000000000000000000000000000000000000000'[::-1]
Contents="1"
Length=np.uint32(1)
difficulty=24

Nonce=np.uint64(15610264)

def try_hash(Nonce):
    Hash = hashlib.sha256()
    Hash.update(PrevHash.decode("hex"))
    Hash.update(Contents)
    Hash.update(Nonce)
    Hash.update(Length)
    b = Hash.digest()[::-1].encode("hex")[0:difficulty]
    ##    print Nonce
##    print Hash.digest().encode("hex")
##    print Hash.digest()[::-1].encode('hex_codec')
##    print b
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
 

loop()
