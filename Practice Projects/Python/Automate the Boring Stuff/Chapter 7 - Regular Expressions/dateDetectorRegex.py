#the purpose of this project is to create a regex that can detect 
#date and time, and then verify that it is a valid date.
import re

#create regex to find a date in DD/MM/YYYY format
#assume days range from 0 to 31, months from 01 to 12, and years from 1000 to 2999
#you should put each part in groups
dateRegex = re.compile(r'(\d\d)/(\d\d)/(\d\d\d\d)')

sen = "Today is 12/02/2016. My name is Christian Aruba"

#unpack the day, month, and year into separate variables
day = dateRegex.search(sen).group(1)
month = dateRegex.search(sen).group(2)
year = dateRegex.search(sen).group(3)


#write aditional code that'll detect if it's a valid date.

#convert the days, months and years to ints to make things easier to calculate

if day[0] == 0:
    day = int(day[1])
else: 
    day = int(day)

if month[0] == 0:
    month = int(month[1])
else:
    month = int(month)

year = int(year)

#variable to check if year is a leap year
isLeapYear = True

#check if the day, month, and year make sense
if day<=0 or day>31:
    print("ERROR: Days must be greater than 0 and cannot be greater than 31.")
    exit()
elif month<=0 or month>12:
    print("ERROR: Months must be greater than 0 and at most 12.")
    exit()
elif year<1000 or year>2999:
    print("ERROR: Years can only range from 1000 to 2999.")
    exit()

#April, June, September and November have 30 days, February has 28 days, and all other months have 31 days
if (month == 4 or month == 6 or month == 9) and day > 30:
    print("ERROR: APRIL, JUNE, and JULY HAVE AT MOST 30 DAYS.")
    exit()
elif month == 2 and day > 28:
    print("ERROR: FEBRUARY HAS AT MOST 28 DAYS.")
    exit()

#leap years are evenly divisible by 4, except if they're divisible by 100
#EXCEPT if they're also divisible by 400.

if (year % 100 == 0 and year % 400 !=0) or year % 4 != 0 : 
    isLeapYear = False

if isLeapYear == True:
    print("Your year is a leap year!")
else: 
    print("Your year is not a leap year.")



    





