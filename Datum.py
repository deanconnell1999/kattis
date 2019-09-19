from datetime import date
import calendar
given = input().split()
D = int(given[0])
M = int(given[1])
print(calendar.day_name[date(2009, M, D).weekday()])