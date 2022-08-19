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

def main():
    dict = {}
    new_line = '\n'
    indent = '   '
    
    #print("==============start==============") #DEBUG PRINT
    with open("dictionary.json","r") as dictionary:
        dict = json.load(dictionary)
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
                print(f"No words can be made from {query}")
            print(f"Enter another set to test for or enter q to quit")
    #print("===============end===============") #DEBUG PRINT
if __name__ == "__main__":
    main()
