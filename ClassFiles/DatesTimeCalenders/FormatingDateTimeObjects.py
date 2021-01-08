'''                 Formatting date and time objects
The datetime object has a method for formating date objects into readable strings. It is called strftime().
It takes one parameter, format to specify the format of the Returned string.






'''
from datetime import date
from datetime import time
from datetime import datetime

today = datetime.now()

print(today)  # 2021-01-08 13:23:55.969347

print(today.strftime("The current year is: %Y"))  # The current year is: 2021

print(today.strftime("%a, %d %B, %y"))  # Fri, 08 January, 21

print(today.strftime("%c"))  # Fri Jan  8 13:35:17 2021

print(today.strftime("%x"))  # 01/08/21

print(today.strftime("%X"))   # 13:49:28

print(today.strftime("%I:%M:%S %p"))  # 01:53:44 PM

print(today.strftime("%I:%M"))  # 01:55
