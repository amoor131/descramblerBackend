# Anthony Moore
# sorted alphabet
# 6/05/22
#
# What it does:
# This code populates a dictionary by reading from file
# lines that do not start with three spaces are keys
# lines that do start with three spaces are appended to the value
# of the last key in the file
# The dictionary is then dumped as a json file
#
# Possible improvements:
# 
#

import json

def main():
    dict = { 
    }
    new_line = '\n'
    indent = '   '
    #print("==============start==============")#DEBUG
    with open('organized.txt','r') as makeDict, open("dictionary.json","w") as save:
        lastKey = ''
        for line in makeDict:
            strippedLine = line.strip('\n')
            if indent in strippedLine:
                strippedLine = strippedLine.strip(indent)
                if dict[lastKey] != None:
                    dict[lastKey] += ' ' + strippedLine
                else:
                    dict[lastKey] = strippedLine
            else:
                #reassign lastKey to new key
                lastKey = strippedLine
                dict[lastKey] = None
        #now save dictionary as json
        json.dump(dict,save)
    print("===============end===============")
if __name__ == "__main__":
    main()