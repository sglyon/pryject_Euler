"""
Created Mar 7, 2013

Author: Spencer Lyon

Project Euler Problem 58:


Starting with 1 and spiralling anticlockwise in the following way, a
square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom
right diagonal, but what is more interesting is that 8 out of the 13
numbers lying along both diagonals are prime; that is, a ratio of 8/13
62%.

If one complete new layer is wrapped around the spiral above, a square
spiral with side length 9 will be formed. If this process is continued,
what is the side length of the square spiral for which the ratio of
primes along both diagonals first falls below 10%?
"""
from __future__ import division
from time import time
import numpy as np
from sympy import isprime

start_time = time()

primes = 0
for n in range(3, 100000, 2):

    # Build the diagonal, one direction at a time
    dse = (np.arange(1, n // 2 + 1) * 8).cumsum() + 1  # South-east
    dnw = (np.arange(1, n // 2 + 1) * 8 - 4).cumsum() + 1  # North-west
    dne = (np.arange(1, n // 2 + 1) * 8 - 6).cumsum() + 1  # North-east
    dsw = (np.arange(1, n // 2 + 1) * 8 - 2).cumsum() + 1  # South-west

    new = np.array([dse[-1], dnw[-1], dne[-1], dsw[-1]])
    for i in new:
        if isprime(i):
            primes += 1

    percent = primes / (2 * n - 1)
    if percent < .1:
        break

ans = n

print("The answer is: %i" % (ans))

running_time = time()
elapsed_time = running_time - start_time
print 'Total Execution time is ', elapsed_time, 'seconds'
