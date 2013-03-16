"""
Created Mar 7, 2013

Author: Spencer Lyon

Project Euler Problem 51:


By replacing the 1st digit of *3, it turns out that six of the nine
possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this
5-digit number is the first example having seven primes among the ten
generated numbers, yielding the family: 56003, 56113, 56333, 56443,
56663, 56773, and 56993. Consequently 56003, being the first member of
this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not
necessarily adjacent digits) with the same digit, is part of an eight
prime value family.
"""
from __future__ import division
from time import time
from sympy import primerange

start_time = time()

# Guess 5 or 6 digit number
nums = list(primerange(10000, 999999))
num_set = set(nums)

str_nums1 = [str(i) for i in range(10)]
str_nums = [str(i) for i in range(1, 10)]

for i in nums:
    count = 1
    si = str(i)
    for repl1 in str_nums1:
        for repl2 in str_nums:
            if si.count(repl1) == 3:  # Found this hint online.
                new_int = int(si.replace(repl1, repl2))
                if new_int != i and new_int in num_set:
                    count += 1
    if count == 8:
        break

ans = i

print 'The answer is: ', ans
running_time = time()
elapsed_time = running_time - start_time
print 'Total Execution time is ', elapsed_time, 'seconds'
