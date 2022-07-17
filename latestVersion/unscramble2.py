# Anthony Moore
# amoor131
# sorted alphabet
# 6/05/22
#
# What it does:
# This code make a dictionary from a JSON file that will have key values 
#
# Possible improvements:
# 
#

import json

def main():
    dict = {}
    new_line = '\n'
    indent = '   '
    
    #DEBUG PRINT
    #print("==============start==============")
    with open("dictionary.json","r") as dictionary:
        dict = json.load(dictionary)
        #DEBUG PRINT
        print(f"dictionary length: {len(dict)}")
        query = "a" #init value arbitrary
        #DEBUG PRINT
        print("see what words you can make with any set of letters!")
        while query != "q":
            query = input()
            orderedQuery = ''.join(sorted(query)).upper() #.strip('\n')
            #DEBUG PRINT
            print(f"orderedQuery = {orderedQuery}")
            #print(f"{dict.keys()}")
            if orderedQuery in dict.keys():
                    print(f"{dict[orderedQuery]}")
            else:
                print(f"No words can be made from {query}")
            '''
            try:
                if orderedQuery in dict.keys():
                    print(f"{dict[orderedQuery]}")
                    print("exists")
            except:
                print("No words can be made")
            '''
            print(f"Enter another set to test for or enter q to quit")
    #DEBUG PRINT
    #print("===============end===============")
if __name__ == "__main__":
    main()
