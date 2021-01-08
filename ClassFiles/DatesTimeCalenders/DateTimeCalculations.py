'''                 Datetime calculations
timedelta is basically a span of time and date, so it's not a particular date. It allows me to perform time based calculations.

How to calculate the days to Christmas 2021.  # 28





'''
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

today = datetime.now()
print(today)  # 2021-01-08 15:00:38.757575

print(str(today + timedelta(365))) # 2022-01-08 15:03:46.601979

print(timedelta(days=365,hours=7,minutes=5))  # 365 days, 7:05:00

print(str(today + timedelta(days=4,weeks=5)))  # 2021-02-16 15:14:34.927608




# calculating a date from the past.

x = datetime.now() - timedelta(weeks=2)
y = x.strftime("%A %B %d, %Y")

print(y)  # Friday December 25, 2020

# How to calculate the days to Christmas 2021.
daysAhead = date.today()

xmas = date(daysAhead.year,12,25)

timetoxmas = xmas - daysAhead

print("It is just",timetoxmas.days, "days to christmas 2021")  # It is just 351 days to christmas 2021
