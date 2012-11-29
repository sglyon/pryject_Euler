"""
Created Nov 21, 2012

Author: Spencer Lyon

Project Euler Problem 45

I got the idea for pent_check from here:
    http://en.wikipedia.org/wiki/Pentagonal_number

I am not checking triangular numbers because all hex nums are tri:
    http://en.wikipedia.org/wiki/Hexagonal_number
"""
from __future__ import division
from math import sqrt
from time import time
start_time = time()

hexn = lambda n: int(n * (2 * n - 1))


def pent_check(x):
    n = (sqrt(24 * x + 1) + 1) / 6.
    return n == int(n)

n = 144
found = 0
while found == 0:
    next_hex = hexn(n)
    if pent_check(next_hex):
        ans = next_hex
        found = 1
    n += 1

print("The answer is: %i") % (ans)

running_time = time()
elapsed_time = running_time - start_time
print 'Total Execution time is ', elapsed_time, 'seconds'

