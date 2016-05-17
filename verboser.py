#!/usr/bin/env python
from PyDictionary import PyDictionary
import json, random, math
dictionary=PyDictionary()

def main():
    datain = input('Enter a string to fancify: ')

    words = datain.split(" ")
    replacement = " ".join([findword(word) for word in words])

    print()
    fancy = u'\u25ac' * (len(replacement)//2 - 1) + u'\u0b9c\u06e9\u06de\u06e9\u0b9c' + u'\u25ac' * (len(replacement)//2 - 1)
    print(fancy)
    print(' ' + replacement)
    print(fancy)

def findword(word):
    wordchance = random.randrange(10)

    if (wordchance > 5):
        data = dictionary.synonym(word)
        if data != None:
            return random.choice(data)

    return word

if __name__ == "__main__":
    main()
