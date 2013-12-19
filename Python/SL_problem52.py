"""
Created Mar 7, 2012

Author: Spencer Lyon

Project Euler Problem 52:

It can be seen that the number, 125874, and its double, 251748, contain
exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
contain the same digits.
"""
from __future__ import division
from time import time
import numpy as np

start_time = time()

x = True
y = 1

while x == True:
    y += 1
    # NOTE: only possible when y < 1.6 * 10 ** (len(str(y)) - 1).
    #       This is because larger numbers makes 6 * y have more digits than y
    if y < 1.666666666 * 10 ** (len(str(y)) - 1):
        s1 = set(str(y))
        s2 = set(str(2 * y))
        if s1 == s2:
            s3 = set(str(3 * y))
            if s1 == s3:
                s4 = set(str(4 * y))
                if s1 == s4:
                    s5 = set(str(5 * y))
                    if s1 == s5:
                        s6 = set(str(6 * y))
                        if s1 == s6:
                            ans = y
                            x = False

print("The answer is: %i" % (ans))

running_time = time()
elapsed_time = running_time - start_time
print 'Total Execution time is ', elapsed_time, 'seconds'
