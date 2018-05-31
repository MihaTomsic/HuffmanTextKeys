#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from huffman import Huffman			
from bitstring import Bits, BitArray
import keyUtils3

if len(sys.argv) == 2:
	t0 = sys.argv[1]
else:  
	t0 = "1234567890 abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLNOPQRSTUVWXYZ" 

words = t0.split()
wordcount = len(words)    
lens = map(len,words)
maxlen = max(lens)

string1 = ""
for c in range(maxlen):
    for w in words:
        if c < len(w):
            string1 += w[c]

string2 = "".join(words)
    
string = string1 + string2    
#print(string)    
huff = Huffman(string)  
huff.huffman_code()
b = huff.huffman_encode()

if len(b) < 256:
	print("Not enough bits of information for private key: ", len(b) ,"< 256 bits")
	sys.exit(1)

# take first 256 bits for private key
priv = b[:256].hex	  # hex private key
print("Priv:", priv)

wif = keyUtils3.privateKeyToWif(priv)
print("WIF:", wif)

pub = keyUtils3.privateKeyToPublicKey(priv)
print("Public:", pub)

addr = keyUtils3.keyToAddr(priv)
print("Address:", addr)
