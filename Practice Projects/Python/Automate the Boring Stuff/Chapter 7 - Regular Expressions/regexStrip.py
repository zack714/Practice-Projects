#this project is to make the strip() string function using regular expressions.
import re
#function to perform the strip
def regStrip(text, target=None):
    #make our Re object
    
    #how do I get target in the raw string?
    #solution: assume they're not using escape characters

    if target is None:
        stripRegex = re.compile(r'^\s+|\s+$')
        a = stripRegex.sub('',text)
        return a
    
    stripRegex = re.compile(rf'^[{target}]+|[{target}]+$') #make it based on the target
    a = stripRegex.sub('', text) #use character classes so that the characters will be removed in any order
 
    #sweep through text for target with the sub method

    #return stripped string
    return a

out = regStrip('This is test text.','text')
print(out)