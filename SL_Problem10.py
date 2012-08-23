"""
Created August 22, 2012

Author: Spencer Lyon

Project Euler #10
"""
from sympy import primerange
from time import time
start_time = time()

ans = sum(list(primerange(0, 2e6)))


end_time = time()
elapsed_time = end_time - start_time
print "total time elapsed is ", elapsed_time, " seconds"
print ans