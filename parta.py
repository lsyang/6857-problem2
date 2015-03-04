import hashlib
import base64
import numpy as np

#works for http://6857coin.csail.mit.edu/block/0000005a67fc720f55953ee20e47b96c47b751bb0214c2a6d4593b066ecc3738

PrevHash='00000099e3f4ca4995c4558b32de66203a323c8aea77a273c86c7ee029ac7b4b'
Contents='32'.encode('hex')
Length="{0:0{1}x}".format(2,8)
difficulty=24



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
try_hash("{0:0{1}x}".format(15610264,16))
