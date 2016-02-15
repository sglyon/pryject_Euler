"""
Created Nov 21, 2012

Author: Spencer Lyon

Project Euler Problem 49:

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
increases by 3330, is unusual in two ways: (i) each of the three terms
are prime, and, (ii) each of the 4-digit numbers are permutations of
one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit
primes, exhibiting this property, but there is one other 4-digit
increasing sequence.

What 12-digit number do you form by concatenating the three terms in
this sequence?
"""
from time import time
from sympy import primerange
from itertools import permutations

start_time = time()

nums = list(primerange(1000, 10000))
num_set = set(nums)


def is_perm(x, y):
    sx = str(x)
    sy = str(y)
    test_set = set(tuple(permutations(sy, len(sy))))
    test_tup = tuple(sx)
    return test_tup in test_set

set1 = 0

for num in nums:
    a = num
    b = num + 3330
    c = num + 3330 * 2
    if b in num_set and c in num_set:
        if all([is_perm(a, b), is_perm(a, c)]):
            if not set1:
                set1 = (a, b, c)
            else:
                set2 = (a, b, c)

ans = str(set2[0]) + str(set2[1]) + str(set2[2])
print("The answer is: %s" % str(ans))


running_time = time()
elapsed_time = running_time - start_time
print('Total Execution time is ', elapsed_time, 'seconds')
