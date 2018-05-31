#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

from bitstring import Bits, BitArray
import unittest
import sys


DEBUG = 0

class Huffman():
    """
    Huffman class accepts string (unicode string - what do you expect in 
    Python 3.x :)
    """
    def __init__(self, text):
        "initializes the algorithm with text/string"
        self.code = None
        self.tree = None
        self.string = None
        self.text = text
        self.d = {}

        for a in self.text:
            if a in self.d:
                self.d[a] = self.d[a]+1
            else:
                self.d[a] = 1

        if DEBUG:
            print(self.text)
            print(self.d)
            print(sorted(self.d.items(), key=lambda x:(x[1],x[0]), reverse = True))
        
    def assign_code(self, nodes, label, result, prefix = ''):
        "function for assembling nodes in recursion"
        if DEBUG == 2:
            print("assign =", nodes, label, result, prefix)
        child = nodes[label]
        tree = {}
        if len(child) == 2:
            tree['0'] = self.assign_code(nodes, child[0], result, prefix+'0')
            tree['1'] = self.assign_code(nodes, child[1], result, prefix+'1')
            return tree
        else:
            result[label] = prefix
            return label


    def huffman_code(self):
        "generate tree/code from text/string"
        vals = self.d.copy()
        # leafs initialization
        nodes = { n: [] for n in vals.keys() }

        while len(vals) > 1: # binary tree creation
            # key= double key sort: numerical by occurence, lexical by label
            # this ensures the determinism of the generated code and encoded bitstring
            s_vals = sorted(vals.items(), key=lambda x: (x[1],x[0]))
            a1 = s_vals[0][0]
            a2 = s_vals[1][0]
            vals[a1+a2] = vals.pop(a1) + vals.pop(a2)
            nodes[a1+a2] = [a1, a2]
            if DEBUG:
                print("vals =", vals)
        if DEBUG:
            print("nodes =", nodes)
        code = {}
        root = a1+a2
        self.tree = self.assign_code(nodes, root, code)   # assignment of the code for the given binary tree
        self.code = code
        if DEBUG:
            print("Code = ")
            for i in sorted(code.items(), key=lambda x:len(x[1])):
                print(i)
            print("tree =",self.tree)

    def huffman_encode(self):
        "encode given text/string with generated tree/code"
        self.string = BitArray()
        for a in self.text:
            self.string.append(Bits(bin=self.code[a]))
        return self.string


class TestUtils(unittest.TestCase):
    def test_huffman_encode(self):
        huff = Huffman("1112234")
        huff.huffman_code()
        huff.huffman_encode()        
        self.assertEqual(huff.tree, 
            {'0': '1', '1': {'0': '2', '1': {'0': '3', '1': '4'}}})
        self.assertEqual(huff.code,
            {'1': '0', '2': '10', '3': '110', '4': '111'})
        self.assertEqual(huff.string.bin,"0001010110111")  

    def test_huffman_encode2(self):
        huff = Huffman("žääčööš")
        huff.huffman_code()
        huff.huffman_encode()        
        self.assertEqual(huff.tree, 
            {'0': {'0': 'ž', '1': 'ä'}, '1': {'0': 'ö', '1': {'0': 'č', '1': 'š'}}}
            )
        self.assertEqual(huff.code,
            {'ž': '00', 'ä': '01', 'ö': '10', 'č': '110', 'š': '111'}
            )
        self.assertEqual(huff.string.bin,"0001011101010111")  
        
    def test_assign_code(self):
        nodes = {'a': [], 'b': [], 'c': [], 'ab': ['a', 'b'], 'cab': ['c', 'ab']}
        root = "cab"
        code = {}
        huff = Huffman("")
        self.assertEqual(huff.assign_code(nodes, root, code), 
            {'0': 'c', '1': {'0': 'a', '1': 'b'}}
            )

def main():
    if len(sys.argv) == 2:
        t0 = sys.argv[1]
    else:
        t0 = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLNOPQRSTUVWXYZ"
        
    huff = Huffman(t0)
    huff.huffman_code()
    b = huff.huffman_encode()
    if DEBUG:
        print("code =", huff.code)
    print(len(b))
    print(b.bin)


if __name__ == "__main__":
    # execute only if run as a script
    #main()
    #unittest.main()
    unittest.main(argv=[""])
   

