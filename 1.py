#Program to find if today is spring or not
from datetime import *

#Get today's Date
today = date.today()
print("Today: " + today.strftime('%A %d, %b %Y'))

#Find out the starting dates of each season
thisYear = today.year
startOfSpring = date(thisYear,3,21)
startOfSummer = date(thisYear,6,21)


if today >= startOfSpring and today < startOfSummer:
    print("We are currently in spring season")
else:
    print("This is not a Spring Season!")
    
print("Spring starts from March 21 & ends on June 21")

#output
#Today: Wednesday 08, Jul 2020
#This is not a Spring Season!
#Spring starts from March 21 & ends on June 21
