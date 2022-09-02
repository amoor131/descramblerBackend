# Anthony Moore
# amoor131
# Unscrambler / Decoder
# 1/22/21
#
# What it does:
# This code takes a string of input and tests it against a list of every
# english word. returns the words that can be made with the letters
#
# Possible improvements:
# remove non alpha characters from user input
# include words that don't require all letters
#
# List of english words taken from http://www.mieliestronk.com/wordlist.html

#removes spaces from user input and converts all letters to their capital form, gives processed data to list_of_letters
def processedInput(rawInput,list_of_letters):
    InputWOspaces = rawInput.strip(' ')                                         #removes any spaces from input
    userInput = InputWOspaces.upper()                                           #make all letters uppercase
    list_of_letters += userInput                                                #populates list_of_letters with scrambled letters in uppercase
    return list_of_letters

#reads in one word at a time from a file and tests if it could be made with the scrambled letters provided
def test_words(wordString, scrambleList, wordsList):
    wordString = wordString.strip('\n')                                         #remove newline char so we can compare against tryWord
    tryWord = []                                                                #making an empty list and += a string will populate each element
    tryWord += wordString                                                       #of the list with a letter in the string
    if len(tryWord) != len(scrambleList):                                       #check if word has same number of letters as scrambled letters
        return                                                                  #if different leave function
    if sorted(tryWord) == sorted(scrambleList):                                 #see if word shares the same letters as scrambled letters
        wordsThatWork.append(wordString)                                        #add the unscrambled word to the list of words that work

#prints what words can be made, if any, to console
def print_results(scrambleList):
    print("   {} can be used to make ".format(scrambleList.lower()), end='')
    if len(wordsThatWork) == 0:
        print("no english words")
    else:
        print(', '.join(wordsThatWork).lower())

#prompts user to enter a new set of letters to test or how to quit
def next_set_or_quit_instructions():
    print("   Enter Q to quit or enter another set of letters")

#main starts here
print("Enter letters you wish to decode; input is not case sensitive:",end='')
with open('English_language_words.txt', 'r') as wordList:                       #open the file with all the english words in it
    keepGoing = 1                                                               #used to end while loop when user wants to quit
    wordsThatWork = []                                                          #empty list of words that can be made with letters given
    while keepGoing:
        rawInput = input()                                                      #places user input into a string for processing
        if rawInput == 'Q' or rawInput == 'q':                                  #check if user wants to quit
            keepGoing = 0                                                       #if they do want to quit keepGoing is set to zero to exit loop
            break                                                               #end this loop early
        scrambled = []                                                          #empty list of letters we'll use to look for words
        processedInput(rawInput,scrambled)                                      #populate scrambled with just scrambled captial letters
        wordList.seek(0)                                                        #start reading the list of words from the beginning
        for wordString in wordList:                                             #loops until there are no lines to read
            test_words(wordString, scrambled, wordsThatWork)                    #tests one word at a time against the letters given
        print_results(rawInput)                                                 #prints what words can be made
        next_set_or_quit_instructions()                                         #prints instructions for another test or quit
        wordsThatWork.clear()                                                   #empties list of words that can be made for next test
