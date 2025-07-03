import pyinputplus as pyip
import random, time

numOfQuestions = 10
correctAns = 0

for questionNumber in range(numOfQuestions):
    
    #Pick 2 random numbers: 
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    
    #make prompt with placeholders
    prompt = '#%s: %s x %s = ' % (questionNumber,num1,num2)

    try:
        # Right answers are handled by allowRegexes.
        # Wrong answers are handled by blockRegexes, with a custom message.
        pyip.inputStr(prompt, allowRegexes = ['^%s$' % (num1 * num2)],
                      blockRegexes = [('.*','incorrect!')],
                      timeout = 8, limit = 3)
        
    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')
    else:
        #This block runs if no exceptions were raised in the try 
        #block.
        print('Correct!')
        correctAns+=1
        
        time.sleep(1) #Brief pause to let user see the result.
        print('Score %s / %s' % (correctAns,numOfQuestions))

