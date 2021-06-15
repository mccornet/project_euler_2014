# How many Sundays fell on the first of the month during
# the twentieth century (1 Jan 1901 to 31 Dec 2000)?
import calendar

sundays = 0

for year in range(1901,2001):
    for month in range(1,13):

        res = calendar.monthrange(year, month)

        if(res[0] == calendar.SUNDAY):
            sundays += 1

print(sundays)


