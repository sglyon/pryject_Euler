"""
Created Mar 7, 2013

Author: Spencer Lyon

Project Euler Problem 56:


A googol (10 ** 100) is a massive number: one followed by one-hundred
zeros; 100 ** 100 is almost unimaginably large: one followed by
two-hundred zeros. Despite their size, the sum of the digits in each
number is only 1.

Considering natural numbers of the form, a ** b, where a, b < 100,
what is the maximum digital sum?
"""
from __future__ import division
from time import time
import numpy as np

start_time = time()

my_sum = lambda x: np.array(list(str(x)), dtype=int).sum()

ans = 0

for a in xrange(1, 100):
    for b in xrange(1, 100):
        temp = my_sum(a ** b)
        ans = temp if temp > ans else ans

print("The answer is: %i" % (ans))

running_time = time()
elapsed_time = running_time - start_time
print 'Total Execution time is ', elapsed_time, 'seconds'
