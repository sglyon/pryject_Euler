"""
Created Mar 7, 2013

Author: Spencer Lyon

Project Euler Problem 57:


It is possible to show that the square root of two can be expressed as
an infinite continued fraction:

sqrt(2) = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:
1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the
eighth expansion, 1393/985, is the first example where the number of
digits in the numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a
numerator with more digits than denominator?
"""
from __future__ import division
from time import time

start_time = time()


def gen_expr(n):
    """generate string expression for nth iteration"""
    ans = '1 + 1/'
    if n == 1:
        ans += 2
    return ans

# TODO: Haven't done this.

print("The answer is: %i" % (ans))

running_time = time()
elapsed_time = running_time - start_time
print 'Total Execution time is ', elapsed_time, 'seconds'
