"""
Created Nov 21, 2012

Author: Spencer Lyon

Project Euler Problem 40
"""
from time import time
from sympy import isprime
from itertools import permutations

start_time = time()

ans = 0

pans = permutations('7654321', 7)

for num in pans:
    ts = ''
    for digit in num:
        ts += digit
    temp = int(ts)
    if isprime(temp):
        if temp > ans:
            ans = temp

print("The answer is: %s") % (str(ans))

running_time = time()
elapsed_time = running_time - start_time
print 'Total Execution time is ', elapsed_time, 'seconds'
