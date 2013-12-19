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
n_set = set(nums)

classy = np.array([classify(i) for i in nums])

abuns = nums[classy == 2]

a = np.tile(abuns, (abuns.size, 1))

all_sums = a + a.T
flat = np.ravel(all_sums)
candidates = set(np.unique(flat[flat <= 28123]))
ans = sum(n_set.difference(candidates))

print('The answer is: %i' % ans)

end = time() - start
print('Total execution time is: %.5f' % end)
