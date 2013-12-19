"""
Created Nov 19, 2012

Author: Spencer Lyon

Project Euler Problem 35
"""
from sympy import primerange
from time import time
start_time = time()

nums = list(primerange(0, 1000000))
num_set = set(nums)


def cyclic_prime(x):
    sx = str(x)
    els = len(sx)
    if x in num_set:
        good = 1
    else:
        return 0
    for i in range(els):
        sx = sx[-1] + sx[:-1]
        if int(sx) in num_set:
            pass
        else:
            return 0
    return good


count = 0
for i in range(len(nums)):
    cur_num = nums[i]
    if cyclic_prime(cur_num) == 1:
        count += 1

running_time = time()
elapsed_time = running_time - start_time
print 'Total Execution time is ', elapsed_time, 'seconds'
