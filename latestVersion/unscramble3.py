# Anthony Moore
# amoor131
# sorted alphabet
# 6/05/22
#
# What it does:
# Searches a json file to see if there is a key that matches users input, returns key's value if found
#
# Possible improvements:
# 
#

import json
from pprint import pprint

def printQuery(foundWords):
    foundWords = foundWords.split()
    list = ""
    for word in foundWords:
        if len(list) + len(word) + 1 <= 80:
            list += word + " "
        else:
            print(list)
            list = ""

def fitsIn(testWord, keyWord):
    comp = list(keyWord)
    if len(testWord) <= len(keyWord):
        for letter in testWord.strip('\n'):
            #print(f"letter: {letter}| keyWord: {keyWord}") #DEBUG
            if letter in comp:
                comp[comp.index(letter)] = '#'
            else:
                return False
        #only returns true if all letters were found in keyWord
        return True

def addKey(testKey,dict):
    #used to add new lines to f statements
    new_line = '\n'
    #check that the entry is only letters
    if testKey.isalpha() == False:
        return -1
    #double check that the user input isn't already a key in the database
    if testKey in dict.keys():
        return 0
    #user input in reverse alphabetical order, 
    sortedKey = ''.join(sorted(testKey.strip('\n')))
    foundWords = ''
    with open('sorted_length.txt','r') as engWords:
        for word in engWords:
            if fitsIn(word, testKey):
                foundWords += ' ' + ''.join(word.strip('\n')) # not sure if I need to strip new line
        newKey = {sortedKey: foundWords}
        dict.update(newKey)
        if len(foundWords) > 0:
            return 1
        else:
            return 2
def main():
    dict = {}
    new_line = '\n'
    indent = '   '
    
    #print("==============start==============") #DEBUG PRINT
    with open("dictionary.json","r") as dictionary:
        dict = json.load(dictionary)
        query = "a" #init value arbitrary
        #DEBUG PRINT
        print("see what words you can make with any set of letters!")
        while query != "q":
            query = input()
            orderedQuery = ''.join(sorted(query)).upper() #.strip('\n')
            #print(f"orderedQuery = {orderedQuery}") #DEBUG PRINT
            if orderedQuery in dict.keys():
                if len(dict[orderedQuery]) > 0:
                    print(f"!{dict[orderedQuery]}{new_line}")
                    #printQuery(f"!{dict[orderedQuery]}{new_line}")
                else:
                    print(f"*no words can be made from {query}{new_line}")
            else:
                tryAddKey = addKey(orderedQuery,dict)
                match tryAddKey:
                    case 2:
                        #
                        print(f"no words can be made from {query}{new_line}")
                    case 1:
                        #
                        print(f"1{dict[orderedQuery]}{new_line}")#DEBUG
                        #printQuery(f"1{dict[orderedQuery]}{new_line}")
                    case 0:
                        #
                        print(f"1{dict[orderedQuery]}{new_line}")#DEBUG
                        #printQuery(f"0{dict[orderedQuery]}{new_line}")
                    case -1:
                        print(f"tried adding {query} as key but it contains non alphabet characters{new_line}")
                #print(f"No words can be made from {query}")
            print(f"Test another set of letters or enter q to quit")
    #print("===============end===============") #DEBUG PRINT
if __name__ == "__main__":
    main()
