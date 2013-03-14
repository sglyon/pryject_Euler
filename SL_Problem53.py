"""
Created Mar 7, 2012

Author: Spencer Lyon

Project Euler Problem 53:


There are exactly ten ways of selecting three from five, 12345:
123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5C3 = 10.

In general,
nCr = n!  / (r!(nr)!) ,where r <= n

It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

How many, not necessarily distinct, values of  nCr, for 1 <= n <= 100,
are greater than one-million?
"""
from __future__ import division
from time import time
import numpy as np
from scipy.misc import comb

start_time = time()
n, r = np.meshgrid(np.arange(1, 101), np.arange(1, 101))

choose = comb(n, r)

ans = (choose > 1000000).sum()

print("The answer is: %i" % (ans))

running_time = time()
elapsed_time = running_time - start_time
print 'Total Execution time is ', elapsed_time, 'seconds'
