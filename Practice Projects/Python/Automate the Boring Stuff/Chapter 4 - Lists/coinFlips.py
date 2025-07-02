#this program is to see how common streaks of 6 Heads
#or tails is common in evens of 10 coin flips.
import random

numberOfStreaks = 0
for experimentNumber in range(10000):
    flips = []
    # Code that creates a list of 100 'heads' or 'tails' values.
    for i in range(0,100):
        flip = random.randint(0,1)
        #heads
        if flip == 0:
            flips.append('H')
        else:
            flips.append('T') #Tails
        
    # Code that checks if there is a streak of 6 heads or tails in a row.
    i=0
    while i<94:
        if flips[i]==flips[i+1]==flips[i+2]==flips[i+3]==flips[i+4]==flips[i+5]:
            numberOfStreaks+=1
            i+=6 #skips the next six numbers to avoid overlapping
        else: 
            i+=1

    


print('Chance of streak: %s%%' % (numberOfStreaks / (100.0)))