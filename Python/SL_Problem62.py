"""
Created 9-6-13

Author: Spencer Lyon

Project Euler Problem 62:

The cube, 41063625 (345^3), can be permuted to produce two other cubes:
56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest
cube which has exactly three permutations of its digits which are also
cube.

Find the smallest cube for which exactly five permutations of its digits
are cube.
"""
from __future__ import division
from time import time

start_time = time()


def permute(x):
    """
    Generator to give cyclic permutations of a given number.

    Example
    =======
    In [1]: list(permute(1234))
    Out[1]: [1234, 2341, 3412, 4123]
    """
    x = str(x)
    n = len(x)
    for i in xrange(n):
        yield int(x[i:] + x[:i])

x = False
num = 12345

while x is False:
    tested = set(num)

    num += 1


ans = 0
print("The answer is: %i" % (ans))

running_time = time()
elapsed_time = running_time - start_time
print('Total Execution time is %.3e seconds' % elapsed_time)
