import datetime

import calendar



def get_days_passed(before, after):

    d1 = before.date()

    d2 = after.date()

    return abs(d1 - d2).days



d1 = datetime.datetime(2014, 05, 24, 17, 0, 0)

d2 = datetime.datetime(2014, 05, 24, 18, 5, 0)

print get_days_passed(d1, d2)  # returns 0

d1 = datetime.datetime(2014, 05, 24, 17, 0, 0)

d2 = datetime.datetime(2014, 05, 25, 5, 5, 0)

print get_days_passed(d1, d2)  # returns 1

d1 = datetime.datetime(2014, 05, 30, 17, 0, 0)

d2 = datetime.datetime(2014, 06, 1, 5, 5, 0)

print get_days_passed(d1, d2)  # returns 2