'''
Problem Description
===================
    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''

MONDAY = 1
TUESDAY = 2
WEDNESDAY = 3
THURSDAY = 4
FRIDAY = 5
SATURDAY = 6
SUNDAY = 7

JANUARY = 1
FEBRUARY = 2
MARCH = 3
APRIL = 4
MAY = 5
JUNE = 6
JULY = 7
AUGUST = 8
SEPTEMBER = 9
OCTOBER = 10
NOVEMBER = 11
DECEMBER = 12

days_map = {
        1: 31,
        2: (28, 29),
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }


def is_leap_year(year):
    is_leap_year = False
    if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
        is_leap_year = True

    return is_leap_year


def days_in_month(month, year):
    days = 0
    if is_leap_year(year) and month == FEBRUARY:
        days = days_map[month][1]
    elif not is_leap_year(year) and month == FEBRUARY:
        days = days_map[month][0]
    else:
        days = days_map[month]
    return days


def is_sunday(month, year):
    tot_days = 0
    for yr in xrange(1900, year):
        if is_leap_year(yr):
            tot_days += 366
        else:
            tot_days += 365

    for mnth in range(1, month):
        tot_days += days_in_month(mnth, year)

    last_day_of_prev_month = tot_days % 7 or SUNDAY

    if last_day_of_prev_month == SUNDAY:
        first_day_of_month = MONDAY
    else:
        first_day_of_month = last_day_of_prev_month + 1

    if first_day_of_month == SUNDAY:
        return True
    else:
        return False

if __name__ == '__main__':
    tot_sundays = 0
    for year in range(1901, 2001):
        for month in range(1, 13):
            if is_sunday(month, year):
                tot_sundays += 1
            else:
                continue
    print tot_sundays
