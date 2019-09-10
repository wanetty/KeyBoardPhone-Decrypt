#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Python 2.7
one = []
two =['a','b','c']
three = ['d','e','f']
four = ['g','h','i']
five = ['j','k','l']
six = ['m','n','o']
seven = ['p','q','r','s']
eight = ['t','u','v']
nine = ['w','x','y','z']
cero = ['_']
keyboard = [cero,one,two,three,four,five,six,seven,eight,nine]

def decrypt(wword):
    pharword = wword.split()
    decryptWord = ''
    for word in pharword:
        primer = 1
        letter = ''
        count = 0
        lastletter  = ''
        for number in word:
            if primer == 1:
                lastletter = number
                primer = 0
            else:
                if number == lastletter:
                    count = count + 1                
                else:
                    #print("Count: " + str(count))
                    letter = keyboard[int(lastletter)][count]
                    count = 0
                    lastletter = number
                    decryptWord += letter
        decryptWord += keyboard[int(lastletter)][count]
        decryptWord += ' '
    return decryptWord



if __name__ == "__main__":
    wword = raw_input('Enter word in numbers: ')
    print(decrypt(wword))
    exit()
                
