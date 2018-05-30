# Huffman Text Keys and Huffman Words Keys

Generate Bitcoin private/public key from text **deterministically**.

Using Huffman coding based on measuring occurence of characters in the string. 

- tree nodes are generated  
- based on occurence build balanced tree
- from tree code is generated
- use generated code to encode the string

The string is converted to bitstring. If bitstring is long enough (len >= 256), 
the first 256 bits are used as private key. 

## How the string is created?

The string can be simple UTF-8 text in case of `HuffmanTextKeys.py`.

For example:

```
$ ./HuffmanTextKeys.py "1234567890 one two three four five six seven eight nine ten 1234567890"
```

In case of `HuffmanWordsKeys.py` the string is constructed by 
- stacking space separated words in rows and reading characters by columns 
plus
- concatenating words without spaces.

For example:

```
$ ./HuffmanWordsKeys.py "one two three four fivei" **
```

The first part is
```
one 
two 
three 
four 
five
```
and reading these words by columns we get `ottff`+`nwhoi`+`eoruv`+`ere`+`e` =
`ottffnwhoieoruveree`. And the second part is simply `onetwothreefourfive`. 

** Actually this does not give us enough bits for private key. This is just 
an illustration of the algorithm used.


## Output formats

Private key is output as 
- hex string and as 
- WIF (Wallet Interchange Format).

Public key is output as 
- hex string and as 
- Bitcoin address.


