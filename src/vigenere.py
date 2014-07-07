#!/usr/bin/python

import argparse

# Create command line argument parser
parser = argparse.ArgumentParser(description = "Enciphers or Deciphers text using the Vigenere Cipher")
group = parser.add_mutually_exclusive_group(required = True)
group.add_argument("-e", "--encipher", action = "store_true", help = "Encipher plaintext into CIPHERTEXT")
group.add_argument("-d", "--decipher", action = "store_false", help = "Decipher CIPHERTEXT into plaintext")
args = parser.parse_args()

# Create Vigenere Square
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
VIGENERE_SQUARE = {ALPHABET[x]: list(ALPHABET[x:] + ALPHABET[:x]) for x in range(len(ALPHABET))}

if args.encipher:
    keyword = raw_input("Enter Keyword: ").upper()
    plaintext = raw_input("Enter Plaintext: ").lower().replace(' ','')
    keytext = (keyword * ((len(plaintext)/len(keyword)) + 1))[:len(plaintext)]
    cipherlist = [ALPHABET.find(plaintext[i].upper()) for i in range(len(plaintext))]
    ciphertext = "".join([VIGENERE_SQUARE[keytext[n]][cipherlist[n]] for n in range(len(plaintext))])
    print "Key:        ", keytext
    print "plaintext:  ", plaintext
    print "CIPHERTEXT: ", ciphertext

else:
    keyword = raw_input("Enter Keyword: ").upper()
    ciphertext = raw_input("Enter CIPHERTEXT: ").upper()
    keytext = (keyword * ((len(ciphertext)/len(keyword)) + 1))[:len(ciphertext)]
    cipherlist = [VIGENERE_SQUARE[keytext[i]].index(ciphertext[i]) for i in range(len(keytext))]
    plaintext = "".join([ALPHABET[cipherlist[n]] for n in range(len(ciphertext))]).lower()
    print "Key:        ", keytext
    print "plaintext:  ", plaintext
    print "CIPHERTEXT: ", ciphertext