"""
Created July 8, 2013

Author: Spencer Lyon

Project Euler Problem 60:

The primes 3, 7, 109, and 673, are quite remarkable. By taking any two
primes and concatenating them in any order the result will always be
prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The
sum of these four primes, 792, represents the lowest sum for a set of
four primes with this property.

Find the lowest sum for a set of five primes for which any two primes
concatenate to produce another prime.
"""
from __future__ import division
from time import time
from sympy import isprime
from tools.primes import primesfrom2to

start_time = time()

n = 10000

p_list = primesfrom2to(n)
p_set = set(p_list)
num = len(p_list)


def concat_prime(x, y):
    return isprime(int(str(x) + str(y))) and isprime(int(str(y) + str(x)))


concats = {}

for i, x in enumerate(p_list):
    concats[x] = set()
    for k in xrange(i, num):
        y = p_list[k]
        if concat_prime(x, y):
            concats[x].add(y)

for x, s_x in concats.iteritems():
    for y in s_x:
        intersect1 = concats[x] & concats[y]

        # Go one more level
        if len(intersect1) > 0:
            for z in intersect1:
                intersect2 = intersect1 & concats[z]

                # Go one more level
                if len(intersect2) > 0:
                    for w in intersect2:
                        intersect3 = intersect2 & concats[w]

                        if len(intersect3) > 0:
                            family = [x, y, z, w, intersect3]
                            break

ans = sum(family[:4]) + family[-1].pop()

print("The answer is: %i" % (ans))

running_time = time()
elapsed_time = running_time - start_time
print('Total Execution time is %.3f seconds' % elapsed_time)
