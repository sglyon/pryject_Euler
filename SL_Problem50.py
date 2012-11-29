"""
Created Nov 21, 2012

Author: Spencer Lyon

Project Euler Problem 50:

The prime 41, can be written as the sum of six consecutive primes:
                    41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime
below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a
prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most
consecutive primes?
"""
from time import time
import numpy as np
from sympy import primerange, isprime
start_time = time()

# I found 7 below by trial and error. Wrong answer starting with 2, 3, 5 ...
primes = np.array(list(primerange(7, 4000)))

cs = np.cumsum(primes)

ip = np.vectorize(isprime)

smalls = cs[cs <= 1000000][::-1]  # Ordered descending

bools = ip(smalls)

ans = smalls[bools][0]

print("The answer is: %i") % (ans)

running_time = time()
elapsed_time = running_time - start_time
print 'Total Execution time is ', elapsed_time, 'seconds'
