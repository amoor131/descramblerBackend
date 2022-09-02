# Anthony Moore
# amoor131
# sorted alphabet
# 1/22/21
#
# What it does:
# Organize4 works, but my goal here is to make this work faster than that.
# organized4 is terribly slow so this will hopefully cut the time down substantially
#
# Possible improvements:
# order letters in words by least to most frequent to reduce comparisons
# 

#dictionary that will hold keys and words made with them
engDict = {}

#used to see if key already exists
def isKey(testKey):
    if testKey in engDict.keys():
        return True
    else:
        return False
        
#not yet implemented!
#meant to sort each word by letter frequency
#not sure if the time saved in comparisons is greater than the time spent sorting very word
#def freqOrder(word):
    # according to https://www3.nd.edu/~busiforc/handouts/cryptography/letterfrequencies.html
    # this is the order of least to most frequent letters as they appear in the english language.
    # this will be used to reduce the number of comparisons
    #frequency = ['Q','J','Z','X','V','K','W','Y','F','B','G','H','M','P','D','U','C','L','S','N','T','O','I','R','A','E']

#returns true is all letters in testValue are in keyWord
def compare(testValue, keyWord):
    comp = list(keyWord)
    if len(testValue) <= len(keyWord):
        for letter in testValue.strip('\n'):
            #print(f"letter: {letter}| keyWord: {keyWord}") #DEBUG
            if letter in comp:
                comp[comp.index(letter)] = '#'
            else:
                return False
        #only returns true if all letters were found in keyWord
        return True
    else:
        return False

import json

def main():
    #used to add new lines to f statements
    new_line = '\n'
    #print("==============start==============")#DEBUG
    with open('sorted_lengthb.txt','r') as long, open('sorted_length.txt','r') as short:
        for keyWord in long:
            #keys are words with letters in alphabetical order, so we must strip newline key
            #and sort alphabetically before checking if that key exists
            #strip returns a list so we join to pass as a string
            key = ''.join(sorted(keyWord.strip('\n')))
            
            #prevents duplicate values or keys
            if isKey(key) == False:
                engDict[key] = '' #nested for loop will populate with words
            else:
                continue
                
            #read from beginning of file again
            short.seek(0)
            
            for testValue in short:
                if compare(testValue, key):
                    engDict[key] += ' ' + ''.join(testValue.strip('\n'))
    
    print("printing to file")
    with open('organized.txt','r+') as dictionary, open("dictionary.json","W") as save:
        #print to file
        for key in engDict:
            dictionary.write(f"{key}{new_line}")
            #print key values on seperate lines and indented
            seperate = engDict[key].split( )
            for value in seperate:
                dictionary.write(f"   {value}{new_line}")
        #also write to json file
        json.dump(engDict,save)
    #print("===============end===============")
if __name__ == "__main__":
    main()