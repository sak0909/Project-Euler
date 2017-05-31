#!/bin/python3

'''
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

'''


from datetime import date


def solve_project_euler():
    sundays=0
    for year in range(1901, 2000 + 1):
        for month in range(1,12 + 1):
            if date(year,month,1).weekday()==6:
                sundays+=1
    print(sundays)

solve_project_euler()

