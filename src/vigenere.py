#!/usr/bin/python

import argparse             # Standard Library module

# Create command line argument parser
parser = argparse.ArgumentParser(description = "Enciphers or Deciphers text using the Vigenere Cipher")
group = parser.add_mutually_exclusive_group(required = True)
group.add_argument("-e", "--encipher", action = "store_true", help = "Encipher plaintext into CIPHERTEXT")
group.add_argument("-d", "--decipher", action = "store_false", help = "Decipher CIPHERTEXT into plaintext")
args = parser.parse_args()

# Create Vigenere Square
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# Dict comprehension and list slicing is used to create a dictionary of key: value pairs, where key is a character from ALPHABET
# and value is a list of the characters in ALPHABET starting with key and wrapping back to the start of ALPHABET, then up to, but not
# including key.
VIGENERE_SQUARE = {ALPHABET[x]: list(ALPHABET[x:] + ALPHABET[:x]) for x in range(len(ALPHABET))}

if args.encipher:
    # Ask user for a keyword, then uppercase it
    keyword = raw_input("Enter Keyword: ").upper()
    # Ask user for the text to encipher, then lowercase it, then remove spaces
    plaintext = raw_input("Enter Plaintext: ").lower().replace(' ','')
    # Create a new string that is the characters in keytext repeating for the length of the plaintext
    keytext = (keyword * ((len(plaintext)/len(keyword)) + 1))[:len(plaintext)]
    # Create a list of integers where each element is the index of the corresponding character in the plaintext, in the ALPHABET
    cipherlist = [ALPHABET.find(plaintext[i].upper()) for i in range(len(plaintext))]
    # Build a new string 
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