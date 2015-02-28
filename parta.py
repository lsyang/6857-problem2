import hashlib
import base64

PrevHash='77a22709b4f6ad7c13c1a5c898cb63872ed00be3eadbd94e6b32482fe7518d51'
Contents="1"
Length=1
difficulty=24

def try_hash(Nonce):
    Hash = hashlib.sha256(PrevHash.decode("hex") + bytes(Contents) + bytes(Nonce) + bytes(Length))
##    print Nonce
##    print Hash.digest().encode("hex")
    b = Hash.digest().encode("hex")[0:difficulty]
    if (b=='0'*24):
        return True
    else:
        return False

def loop():
    
    for i in range(2**20,2**30):
        if try_hash(i):
            print i
            return i

loop()
