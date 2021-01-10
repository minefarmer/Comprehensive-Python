"""                 Working with calendars
The calendar module contains different classes that you can use to create calendars.

A text based calendar  # 





"""
import calendar
# A text based calendar
# cal = calendar.TextCalendar(calendar.SUNDAY)  # SUNDAY is the first day of the week. == If I want to use Monday instead than enter MONDAY.

# str = cal.formatmonth(2020,1)

# print(str)  #     January 2020
            # Su Mo Tu We Th Fr Sa
            #         1  2  3  4
            # 5  6  7  8  9 10 11
            # 12 13 14 15 16 17 18
            # 19 20 21 22 23 24 25
            # 26 27 28 29 30 31








# A HTML based calendar
cal = calendar.TextCalendar(calendar.SUNDAY)  # SUNDAY is the first day of the week. == If I want to use Monday instead than enter MONDAY.

str = cal.formatmonth(2020,1)

print(str)