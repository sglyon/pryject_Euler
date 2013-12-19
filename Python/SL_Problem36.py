"""
Created Nov 19, 2012

Author: Spencer Lyon

Project Euler Problem 36
"""
import numpy as np
from time import time
start_time = time()

the_sum = 0

for i in xrange(1, 1000000):
    si = str(i)
    if si == si[::-1]:
        b2i = np.base_repr(i)
        if b2i == b2i[::-1]:
            the_sum += i

print 'The answer is: ', the_sum
running_time = time()
elapsed_time = running_time - start_time
print 'Total Execution time is ', elapsed_time, 'seconds'
