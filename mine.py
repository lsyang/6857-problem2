import hashlib
import base64
import re
import requests
import json
import random
import time, threading
#import numpy as np


class Bitcoin:
    

    def __init__(self):
        self.PrevHash='77a22709b4f6ad7c13c1a5c898cb63872ed00be3eadbd94e6b32482fe7518d51'
        self.Contents='1'.encode('hex')
        self.length_numeral=1
        self.Length="{0:0{1}x}".format(1,8)
        self.difficulty=6

    def update(self):
        r = requests.get("http://6857coin.csail.mit.edu/head").json()
        newLength = r.get("Length")
        if (self.length_numeral-1!=newLength):
            print "new block!"
            #compute latest hash
            self.PrevHash=r.get("PrevHash")
            self.Contents=r.get("Contents").encode('hex')
            self.Length = hex(r.get("Length"))[2:].zfill(8)
            Nonce = re.sub('[L]', '', hex(r.get("Nonce"))[2:])
            Nonce = Nonce.zfill(16)
            #set new variables
            self.PrevHash= self.compute_hash(Nonce)
            self.Contents='1'.encode('hex')
            self.Length = hex(r.get("Length")+1)[2:].zfill(8)
            self.length_numeral=r.get("Length")+1
            self.difficulty = ( r.get("Length")/100 + 24 )/4
        print 'updating'
        print self.PrevHash
        threading.Timer(10, self.update).start()



    def compute_hash(self,Nonce):
        Hash = hashlib.sha256()
        Hash.update(self.PrevHash.decode("hex"))
        Hash.update(self.Contents.decode("hex"))
        Hash.update(Nonce.decode("hex"))
        Hash.update(self.Length.decode("hex"))
        result = Hash.digest().encode("hex")
        #print result
        return result
    
    def check_hash(self,Hash):
        b=Hash[0:self.difficulty]
        if (b=='0'*self.difficulty):
            return True
        else:
            return False
        

    def seq_loop(self):
        i=0
        zeros=0
        while i<2**64:
            nonce = re.sub('[L]', '',hex(i)[2:]).zfill(16)
            if self.check_hash(self.compute_hash(nonce)):
                self.post(i)
                print "horray!"
                print i
               # return i
            i+=1


    def rand_loop(self):
        while True:
            i = random.getrandbits(64)
            #print i
            nonce = re.sub('[L]', '',hex(i)[2:]).zfill(16)
            if self.check_hash(self.compute_hash(nonce)):
                self.post(i)
                print "horray!"
                print i
               # return i


    def post(self,nonce):
        payload ={
          "PrevHash": self.PrevHash,
          "Contents": "1",
          "Nonce": nonce,
          "Length": self.length_numeral
        }
        url="http://6857coin.csail.mit.edu/add"

        r = requests.post(url, data=json.dumps(payload))
        print r.text

b=Bitcoin()
b.update()
b.seq_loop()


