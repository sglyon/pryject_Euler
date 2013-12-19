"""
Created Nov 21, 2012

Author: Spencer Lyon

Project Euler Problem 48
"""
from time import time
start_time = time()

ans = str(sum([ i ** i for i in range(1, 1001)]))[-10:]

print("The answer is: %s") % ans

running_time = time()
elapsed_time = running_time - start_time
print 'Total Execution time is ', elapsed_time, 'seconds'
