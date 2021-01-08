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
print()

