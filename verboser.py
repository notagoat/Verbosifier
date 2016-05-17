#!/usr/bin/env python
from PyDictionary import PyDictionary
import json, random, math
dictionary=PyDictionary()

def main():
    datain = input('Enter a string to fancify: ')

    words = datain.split(" ")
    replacement = " ".join([findword(word) for word in words])

    print(replacement)

def findword(word):
    wordchance = random.randrange(10)

    if (wordchance > 5):
        data = dictionary.synonym(word)
        if data != None:
            return random.choice(data)

    return word

if __name__ == "__main__":
    main()
