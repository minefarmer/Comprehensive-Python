"""                 Working with calendars
The calendar module contains different classes that you can use to create calendars.

A text based calendar  # 11
# A HTML based calendar  # 32

Part 2:  # 50

Part 3:  # 120
"""
import calendar
# A text based calendar
# cal = calendar.TextCalendar(calendar.SUNDAY)  # SUNDAY is the first day of the week. == If I want to use Monday instead than enter MONDAY.

# str = cal.formatmonth(2020,1)

# print(str)  #     January 2020
#             # Su Mo Tu We Th Fr Sa
#             #         1  2  3  4
#             # 5  6  7  8  9 10 11
#             # 12 13 14 15 16 17 18
#             # 19 20 21 22 23 24 25
#             # 26 27 28 29 30 31








# A HTML based calendar
# cal = calendar.HTMLCalendar(calendar.MONDAY)  # MONDAY is the first day of the week. == If I want to use Sunday instead than enter SUNDAY.

# str = cal.formatmonth(2020,1)

# print(str)  # 
# <table border="0" cellpadding="0" cellspacing="0" class="month">
# <tr><th colspan="7" class="month">January 2020</th></tr>
# <tr><th class="mon">Mon</th><th class="tue">Tue</th><th class="wed">Wed</th><th class="thu">Thu</th><th class="fri">Fri</th><th class="sat">Sat</th><th class="sun">Sun</th></tr>
# <tr><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="wed">1</td><td class="thu">2</td><td class="fri">3</td><td class="sat">4</td><td class="sun">5</td></tr>
# <tr><td class="mon">6</td><td class="tue">7</td><td class="wed">8</td><td class="thu">9</td><td class="fri">10</td><td class="sat">11</td><td class="sun">12</td></tr>
# <tr><td class="mon">13</td><td class="tue">14</td><td class="wed">15</td><td class="thu">16</td><td class="fri">17</td><td class="sat">18</td><td class="sun">19</td></tr>
# <tr><td class="mon">20</td><td class="tue">21</td><td class="wed">22</td><td class="thu">23</td><td class="fri">24</td><td class="sat">25</td><td class="sun">26</td></tr>
# <tr><td class="mon">27</td><td class="tue">28</td><td class="wed">29</td><td class="thu">30</td><td class="fri">31</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td></tr>
# </table

# The MyCal.html shows a calendar with Monday as the first day of the week.

# Part 2  *********************************************************
cal = calendar.TextCalendar(calendar.SUNDAY)

for days in cal.itermonthdates(2021,1):  

    print(days)  # 2020-12-27
                # 2020-12-28
                # 2020-12-29
                # 2020-12-30
                # 2020-12-31
                # 2021-01-01
                # 2021-01-02
                # 2021-01-03
                # 2021-01-04
                # 2021-01-05
                # 2021-01-06
                # 2021-01-07
                # 2021-01-08
                # 2021-01-09
                # 2021-01-10
                # 2021-01-11
                # 2021-01-12
                # 2021-01-13
                # 2021-01-14
                # 2021-01-15
                # 2021-01-16
                # 2021-01-17
                # 2021-01-18
                # 2021-01-19
                # 2021-01-20
                # 2021-01-21
                # 2021-01-22
                # 2021-01-23
                # 2021-01-24
                # 2021-01-25
                # 2021-01-26
                # 2021-01-27
                # 2021-01-28
                # 2021-01-29
                # 2021-01-30
                # 2021-01-31
                # 2021-02-01
                # 2021-02-02
                # 2021-02-03
                # 2021-02-04
                # 2021-02-05
                # 2021-02-06

for name in calendar.month_name:
    print(name)  # January
                # February
                # March
                # April
                # May
                # June
                # July
                # August
                # September
                # October
                # November
                # December
for day in calendar.day_name:
    print(day)  # Monday
                # Tuesday
                # Wednesday
                # Thursday
                # Friday
                # Saturday
                # Sunday

# Part 3


print("The team meeting will be on : ")
for m in range(1,13):
    cal = calendar.monthcalendar(2021,m)
    wk1 = cal[0]
    wk2 = cal[1]

    if wk1[calendar.FRIDAY]  != 0:
        meeting = wk1[calendar.FRIDAY]
    else:
        me
