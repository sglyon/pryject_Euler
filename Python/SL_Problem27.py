"""
Created Nov 16, 2012

Author: Spencer Lyon

Project Euler Problem 27
"""
import sympy as sym
import numpy as np
from time import time
from itertools import product

start_time = time()

a = np.arange(-999, 1000, 2)
primes = np.asarray(list(sym.primerange(3, 1000)))
b = np.concatenate((primes, primes * -1))
b.sort()


def is_prime(x):
    return np.asarray([sym.isprime(abs(i)) for i in x])

n = np.arange(0, 150)


def test(a, b, n):
    vals = n ** 2 + a * n + b
    bools = is_prime(vals)
    length = np.where(bools < 1)[0][0]
    return length

tries = product(a, b)
num_tries = len(list(product(a, b)))

longest = 0
arg_longest = 0

for i in range(num_tries):
    this_try = tries.next()
    this_length = test(this_try[0], this_try[1], n)
    if this_length > longest:
        longest = this_length
        arg_longest = i

tries2 = list(product(a, b))
ans = tries2[arg_longest][0] * tries2[arg_longest][1]

print 'The answer is: ', ans

running_time = time()
elapsed_time = running_time - start_time
print 'Total Execution time is ', elapsed_time, 'seconds'
