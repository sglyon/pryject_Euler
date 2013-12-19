"""
Project Euler Problem 19

Problem text:

    You are given the following information, but you may prefer to do some research for yourself.

    * 1 Jan 1900 was a Monday.

    * Thirty days has September, April, June and November. All the rest
      have thirty-one, Saving February alone, Which has twenty-eight,
      rain or shine. And on leap years, twenty-nine.

    * A leap year occurs on any year evenly divisible by 4, but not on
      a century unless it is divisible by 400.

    How many Sundays fell on the first of the month during the twentieth
    century (1 Jan 1901 to 31 Dec 2000)?

Date: Wed Dec 18 14:38:25 MST 2013

"""
using Datetime

function euler19()
    d1 = date(1901, 1, 1)
    d2 = date(2000, 12, 31)
    firstDaySunday = x -> dayofweek(x) == 0 && day(x) == 1
    return length([d1:firstDaySunday:d2])
end
