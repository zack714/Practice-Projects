#this is meant to recreate the multiplication quiz manually without using pyinput plus
import time
from datetime import datetime as dt, timedelta
import random

#create a variable that tracks how many questions have been asked
numQAsked = 0
#initialize the number of tries as 0
numTries = 0
#create a list that will hold which questions were right and wrong
questionStatus = []
#start a while loop that will end when the number of questions is no longer<10
while numQAsked < 10:
    #create variables to hold the operands, and number of tries
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    numTries = 0
    #create a bool that tells if the user got the answer right or wrong. Initalize it as false
    questionCorrect = False
    #initalize the answer as the product of these operands
    ans = int(num1*num2)
    
    #get the starting time and ending time
    startingTime = dt.now()
    endingTime = dt.now() + timedelta(seconds = 8)

    #create a inner while loop that will run as long as the countdown is greater than 0 and numtries is <3
    while numTries < 3:
       #ask the user what the product of num1 x num2 is (as a input question)
       userAns = input(f"What is {num1} * {num2}? Answer: ")
       userAns = int(userAns)
        #if they get it correct, tell them 'CORRECT!' for one second, change correct var to true, and break
       if dt.now()>endingTime:
           print("Time's up!")
           break
       if userAns == ans:
           print("Correct!")
           time.sleep(1)
           questionCorrect = True
           break
       else:
           numTries+=1
           print("Wrong answer. Try again.")
       
    if numTries > 3:
        print("You've used the maximum number of Tries") #if the user gets ejected from the loop, tell them why

    #if bool var is false, initalize i'th element of question list as 'W' for wrong
    if questionCorrect == False:
        questionStatus+='W'
    else:
        questionStatus+= 'R' #otherwise, initialize it as 'R' for right
    numQAsked+=1

    
#create var numQuestionsRight and numQuestionsWrong 
numQuestionsRight = 0
numQuestionsWrong = 0

#loop through list and increment or decrement above vars depending on the character in the ith element
for i in range(0,10):
    if questionStatus[i] == 'W':
        numQuestionWrong +=1
    else:
        numQuestionsRight+=1

#tell user how many questions they got right and how many questions they got wrong
print(f"You got {numQuestionsRight} questions right and {numQuestionsWrong} questions wrong.")
    

    



    