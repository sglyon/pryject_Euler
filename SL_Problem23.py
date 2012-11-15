"""
Created Nov 15, 2012

Author: Spencer Lyon

Project Euler Problem 23
"""
import sympy as sym
import numpy as np
from time import time

start = time()


def classify(n):
    """
    Classifies a number n as being perfect, decifient, or abundant

    If 0 is returned the number is perfect.

    If 1 is returned the number is deficient.

    If 2 is returned the number is abundant.
    """
    sum_divs = sum(sym.divisors(n)[:-1])
    if sum_divs == n:
        return 0
    elif sum_divs < n:
        return 1
    else:
        return 2

nums = np.arange(1, 28123 + 1)

classy = np.array([classify(i) for i in nums])

abuns = nums[classy == 2]

abun = set(abuns)

ans = 0

for i in xrange(28123):
    if not any((i - a in abun) for a in abun):
        ans += i

print 'The answer is: ', ans

end = time() - start
print 'Total execution time is: ', end
