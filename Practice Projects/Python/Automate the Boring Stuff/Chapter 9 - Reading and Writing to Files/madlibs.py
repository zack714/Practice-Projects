#madlibs.py - create a madlibs game where users can replace nouns, adjectives, or words with their own input
#8/5/2025
import pyinputplus as pyip #for user input
import os


madFile = open("C:/Users/User/Desktop/Personal Programming/Practice Projects/Python/Automate the Boring Stuff/Chapter 9 - Reading and Writing to Files/madLibsTxt.txt", 'r')
origString = madFile.read()
print(origString)
newMadText = [] #initalize the text as an empty list that will hold the characters
i = 0
#add characters to the new list from the original text 
#for each character, look at the neighboring characters to check
#if they add up to the word noun, adjective or fence
while i  < len(origString) or i != len(origString) :
    if origString[i:i+4] == 'NOUN':
        newNoun = pyip.inputStr("Enter a noun: ")
        newMadText+= newNoun
        i+=4
    elif origString[i:i+4] == 'VERB':
        newVerb = pyip.inputStr("Enter a verb: ")
        newMadText+= newVerb
        i+=4
    elif origString[i:i+9] == 'ADJECTIVE':
        newAdj = pyip.inputStr("Enter a adjective: ")
        newMadText+= newAdj
        i+=9
    else:
         newMadText+=origString[i]
         i+=1

    newMadText = ''.join(newMadText)
print(newMadText)

newMadLib = open('newMadLib.txt','w')
newMadLib.write(newMadText)
newMadLib.close()
madFile.close()


        
