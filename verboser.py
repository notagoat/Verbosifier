#!/usr/bin/env python
from PyDictionary import PyDictionary
import json, random, math
dictionary=PyDictionary()

exception = set(["kiddo","Fucking","fucking","Your","your""Me","me","my","My","the","The","a","A","Only","What","what","fuck","Fuck","You","you"])
def main():
    i = 0
    input = '''Makes any string a lot more fancy '''
    words = input.split()
    replacement = " ".join([findword(word) for word in words])
    print(input)
    print(replacement)

def findword(word):
    wordchance = random.randrange(10)
    print(wordchance)
    if any(word in s for s in exception):
        return word
    if (wordchance > 5):
        data = dictionary.synonym(word)
        return random.choice(data)
    else:
        return word

if __name__ == "__main__": main()

#Character length = chance of selection?
''' Test Code

word = "Test Test"
data = dictionary.synonym(word)
for i in range(len(data)):
    print(data[i])
    print(len(data[i]))

'''
