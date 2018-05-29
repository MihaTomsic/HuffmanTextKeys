#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from huffman import Huffman			
from bitstring import Bits, BitArray
import keyUtils3

if len(sys.argv) == 2:
	t0 = sys.argv[1]
else:  
	t0 = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLNOPQRSTUVWXYZ" 

huff = Huffman(t0)  
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
