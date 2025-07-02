#! python3
#bulletPointAdder.py - Adds Wikipedia bullet points to the start
#of each line of text on the clipboard.

import pyperclip
text = pyperclip.paste()

#TODO: Separate lines and add stars.

pyperclip.copy(text)

#Separate lines and add stars.
lines = text.split('\n')

for i in range(len(lines)): #loop through all indexes in the "lines" list
    lines[i] = '* '+ lines[i] #add star to each string in "lines" list

#pyperclip.copy expects a single string value, not a list
#so join these modified lines together with the .join() method
text = '\n'.join(lines)
pyperclip.copy(text)

print("BULLET POINTS ADDED.")