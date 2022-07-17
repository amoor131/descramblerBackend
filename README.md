# descrambler
This is a fun project I made that returns the words that can be made from a given set of letters including all subsets of those letters.

The English_language_words.txt file was sourced from this link http://www.mieliestronk.com/wordlist.html

I currently have a demo of this code working on my website at amooreprojects.info/descrambler

The Unscramble.py script in the oldVersions folder is the first version of this project made in January of 2021. It is meant for use in command line interfaces.
In this older version, the script was only meant to find words that perfectly matched with the set of letters given
An example would be entering LIVE and getting back EVIL, LIVE LEVI, VEIL, and VILE.

#Methodology

This summer I decided to expand upon this project so that it could also return words that only use a subset of the letter provided
An example would be entering LIVE and getting back IVE, LIE, VIE, EVIL, LEVI, LIVE, VEIL, and VILE. This was achieved by reorganizing the list of words
and writing a script to make a python dictionary that the final script would refer to. This dictionary used the letters from words in alphabetical order as keys
and the words that can be made from those keys as values. An example would be adding LIVE, which would be alphabetized to EILV. If the key did not already
exist, the script will run through all words that are four letters long or shorter and any words that can be made from the letters in EILV will be appended to
the value of that key. Setting the keys are the alphabetized letters reduces the amount of keys needed from 58,000 to around 54,000 by consolidating duplicates
(LIVE, EVIL, ect) into a single key. This also means user input that searches for keys can be easily alphabetized to search for results. Next, I'll cover
more of the developement process.

#V1

First, I made two scripts to reorganize the words in English_language_words.txt so that they are organized by length and then in alphabetical order.
'sortByLength.py' is one of the two scripts I made to organize and rewrite the dictionary. 'sorted_length.txt' and 'sorted_lengthb.txt' are the
resulting files from these scripts; the former is ordered from shortest to longest while the latter is the opposite (b for backwards). Using these files,
I created 'organized.py', which printed the dictionary to a text file named 'organized'. With the organized file, I wrote 'make_dictionary.py', which 
recreated the dictionary from the organized file and created 'dicionary.json' from the python dictionary. The operations of these files could have been combined,
but I have left them seperate as on occasion I have found there to be missing words in the dictionary, and rather than having to wait for 'organized.py' to execute
I can manually change the 'oranized.txt' files and update the 'dictionary.json' file with 'make_dicionary.py' within seconds.

#V2

The current version of the project is in 'organized2.py' and 'unscrambled2.py'. This is a rework of 'organized.py' that is much easier to read in addition to 
being sigificantly faster. This doesn't improve the performance of 'unscrambled2.py' nor does it improve the performance of how my website executes the script,
but it does serve as practice for making code that's easier to read and performs well.
