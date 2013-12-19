"""
Created Nov 19, 2012

Author: Spencer Lyon

Project Euler Problem 34
"""
from sympy import factorial as fac
from time import time
start_time = time()

upper = fac(9) * 7

facs = [fac(i) for i in range(10)]

the_sum = 0
for x in xrange(3, upper + 1):
    if x == sum([facs[int(i)] for i in str(x)]):
        the_sum += x

print the_sum

running_time = time()
elapsed_time = running_time - start_time
print 'Total Execution time is ', elapsed_time, 'seconds'
