'''                 Working with dates and Time
Python has a module called datetime that contains predefined classes and methods that I can use to manipulate dates and time.







'''
from datetime import date
from datetime import time
from datetime import datetime

today = date.today()

print('Today is ', today)  # Today is  2021-01-07
print('The date components are ',today.day,today.month, today.year)  # The date components are  7 1 2021

print('The weekday number is', today.weekday())  # The weekday number is 3

days = ["monday", "tuesday","wednesday","thursday","friday","saturday","sunday"]
print("the weekday is", days[today.weekday()])  # the weekday is thursday

today = datetime.now()  # now is the method

print("The current time is ", today)  # The current time is  2021-01-08 12:07:39.262720

t = datetime.time(datetime.now())
print("The time now is ", t)  # The time noe is  12:12:41.306702
