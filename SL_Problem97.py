"""
Created Date

Author: Spencer Lyon

Project Euler Problem PROBLEM NUMBER:

PROBLEM TEXT
"""
from __future__ import division
from time import time

start_time = time()

ans = str(28433 * 2 ** 7830457 + 1)[-10:]

print("The answer is: %i" % (ans))

running_time = time()
elapsed_time = running_time - start_time
print 'Total Execution time is ', elapsed_time, 'seconds'
