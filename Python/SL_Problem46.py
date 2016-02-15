"""
Created Nov 21, 2012

Author: Spencer Lyon

Project Euler Problem 46
"""
from sympy import isprime
from time import time
import numpy as np
start_time = time()

twice_sq = 2 * (np.arange(1, 100) ** 2)

n = 35
done = 0
while done == 0:
    if isprime(n):
        pass
    else:
        possible = n - twice_sq[twice_sq < n]
        if not any([isprime(i) for i in possible]):
            done = 1
            ans = n
    n += 2

print("The answer is: %i" %(ans))

running_time = time()
elapsed_time = running_time - start_time
print('Total Execution time is ', elapsed_time, 'seconds')
