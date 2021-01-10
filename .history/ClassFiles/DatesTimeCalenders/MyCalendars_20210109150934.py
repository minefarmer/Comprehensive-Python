"""                 Working with calendars
The calendar module contains different classes that you can use to create calendars.

A text based calendar  # 11
# A HTML based calendar  # 32

Part 2:  # 50


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

    print(days)
