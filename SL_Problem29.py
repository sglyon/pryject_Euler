"""
Created Nov 16, 2012

Author: Spencer Lyon

Project Euler Problem 29
"""
from itertools import product
from time import time
start_time = time()

nums = range(2, 101)

tests = list(product(nums, nums))

els = set([i[0] ** i[1] for i in tests])

ans = len(els)

print "The answer is: ", ans


running_time = time()
elapsed_time = running_time - start_time
print 'Total Execution time is ', elapsed_time, 'seconds'
