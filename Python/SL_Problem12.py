"""
Created August 22, 2012

Author: Spencer Lyon
"""
from sympy import divisor_count
from time import time
start_time = time()

total = 0
its = 1
while total < 500:
    num = sum(range(its))
    total = divisor_count(num)
    its += 1


end_time = time()
elapsed_time = end_time - start_time
print "total time elapsed is ", elapsed_time, " seconds"
print num
