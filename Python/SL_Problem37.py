"""
Created Nov 19, 2012

Author: Spencer Lyon

Project Euler Problem 37
"""
from sympy import primerange
from time import time
start_time = time()

nums = primerange(10, 800000)
primes = set(list(primerange(0, 10)))


def choppable(x):
    sx = str(x)
    els = len(sx)
    ans = 1
    for el in range(1, els):
        if int(sx[el:]) in primes:
            pass
        else:
            return 0

        if int(sx[:-el]) in primes:
            pass
        else:
            return 0

    return ans


truncs = []
for i in nums:
    primes.add(i)
    if choppable(i) == 1:
        truncs.append(i)

ans = sum(truncs)
print "The answer is: ", ans
running_time = time()
elapsed_time = running_time - start_time
print 'Total Execution time is ', elapsed_time, 'seconds'

