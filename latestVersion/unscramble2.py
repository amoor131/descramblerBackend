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
    print(f"testing key: {testKey}")
    #used to add new lines to f statements
    new_line = '\n'
    #check that the entry is only letters
    if testKey.isalpha() == False:
        return -1
    #double check that the user input isn't already a key in the database
    if testKey in descrambler.keys():
        return 0
    #user input in reverse alphabetical order, 
    sortedKey = ''.join(sorted(testKey.strip('\n')))
    foundWords = ''
    with open('sorted_length.txt','r') as engWords:
        for word in engWords:
            if fitsIn(word, testKey):
                foundWords += ' ' + ''.join(word.strip('\n')) # not sure if I need to strip new line
        if len(foundWords) > 0:
            #dict[sortedKey] = foundWords
            newKey = {sortedKey: foundWords}
            dict.update(newKey)
            #json.dump(dict,dictionary)
            return 1

def main():
    dict = {}
    new_line = '\n'
    indent = '   '
    
    #print("==============start==============") #DEBUG PRINT
    with open("dictionary.json","r") as dictionary:
        dict = json.loads(dictionary)
        #DEBUG PRINT
        #print(f"dictionary length: {len(dict)}")
        query = "a" #init value arbitrary
        #DEBUG PRINT
        print("see what words you can make with any set of letters!")
        while query != "q":
            query = input()
            orderedQuery = ''.join(sorted(query)).upper() #.strip('\n')
            #print(f"orderedQuery = {orderedQuery}") #DEBUG PRINT
            #print(f"{dict.keys()}")
            if orderedQuery in dict.keys():
                    print(f"{dict[orderedQuery]}")
            else:
                tryAddKey = addKey(orderedQuery,dict)
                match tryAddKey:
                    case 1:
                        print(f"{dict[orderedQuery]}")
                    case 0:
                        print(f"*{dict[orderedQuery]}")
                    case -1:
                        print(f"tried adding key {orderedQuery} but it contains non alphabet characters")
                #print(f"No words can be made from {query}")
            print(f"Enter another set to test for or enter q to quit")
    #print("===============end===============") #DEBUG PRINT
if __name__ == "__main__":
    main()
