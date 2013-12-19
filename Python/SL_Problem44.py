"""
Created Nov 21, 2012

Author: Spencer Lyon

Project Euler Problem 44
"""
from itertools import product
from time import time

start_time = time()

pents = set([int(n * (3 * n - 1) / 2.) for n in range(1, 3000)])

ans = 1e8

for p1 in pents:
    for p2 in pents:
        if abs(p1 - p2) in pents and (p1 + p2) in pents:
            if abs(p1 - p2) < ans:
                ans = abs(p1 - p2)

print("The answer is: %i") % (ans)

running_time = time()
elapsed_time = running_time - start_time
print 'Total Execution time is ', elapsed_time, 'seconds'
