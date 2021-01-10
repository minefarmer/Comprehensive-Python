"""                 Working with calendars
The calendar module contains different classes that you can use to create calendars.







"""
import calendar

cal = calendar.TextCalendar(calendar.SUNDAY)  # SUNDAY is the first day of the week. == If I want to use Monday instead than enter MONDAY.

str = cal.formatmonth()
