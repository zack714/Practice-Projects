#this program will perform the collatz sequence on any integer the user enters.
#INPUT VALIDATION: added a try and except clause to catch the user entering non-integer values.
def collatz(n):
    #if n is even...
    if n%2==0:
        #preform floor division on it
        n//=2
    else:
        #otherwise, it's odd. Multiply it by 3 and add one.
        n=n*3+1
    return n

print("This program preforms the collatz sequence on any *integer* you enter. Please enter a integer.")
#see if the user gave a valid input
try:
    num = int(input())
except ValueError:
    print("///***ERROR: You must input an integer for this program.***///")


#store the original number to display it later
origNum = num
attempts = 0

#preform collatz until the input is 1. Increment attempts each iteration.
while num!=1:
    num = collatz(num)
    print(num)
    attempts +=1

#tell the user how many attempts it took!
print("Collatz sequence complete. Your number, "+str(origNum)+ " took "+str(attempts) +" operations to reach 1.")