import re
#this program uses regular expressions to verify if a password is strong or not.
#a strong password is defined as: at least 8 characters long, with both uppercase and lowercase characters,
#and at least one digit.

def verifyStrong(password):

    #for each test, create a registry object and use custom character
    #classes to make a RE object. Then search and check if it returns a NoneType object.
    #if so, print a message telling the user what they should change and return False.

    lenRe = re.compile(r'[a-zA-Z0-9]{8,}')
    lenCheck = lenRe.search(password)
    if lenCheck == None:
        print("Passwords must contain a minimum of 8 characters.")
        return False

    upperRe = re.compile(r'[A-Z]{1,}')
    upperCheck = upperRe.search(password)
    if upperCheck == None: 
        print("Passwords must contain at least one uppercase character.")
        return False

    lowerRe = re.compile(r'[a-z]{1,}')
    lowerCheck = lowerRe.search(password)
    if lowerCheck == None:
        print("Passwords must contain at least one lowercase character.")
        return False

    digitRe = re.compile(r'[0-9]{1,}')
    digitCheck = digitRe.search(password)
    if digitCheck == None:
        print("Passwords must contain at least one digit.")
        return False

    print("Password is strong!")
    return True

    
verifyStrong("osdjfajsdfsJ")
        

    




