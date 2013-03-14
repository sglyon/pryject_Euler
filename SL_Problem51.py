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
from sympy import isprime

start_time = time()
digits = int(raw_input('Enter the number of digits: '))

primes = set()
checked = set()

if digits == 2:
    for num in xrange(11, 100, 2):
        temp = 0
        st_num = str(num)
        if isprime(num):
            primes.add(num)
            checked
