"""
Created Nov 15, 2012

Author: Spencer Lyon

Project Euler Problem 26

I got the idea for how to do this from the following website:

    http://primes.utm.edu/glossary/xpage/PeriodOfADecimal.html
"""
import sympy as sym
import numpy as np

# The number must be prime and I am guessing it is big so start with highest.
primes = np.asarray(list(sym.primerange(1, 1000)))[::-1][:-3]

periods = np.asarray([sym.ntheory.n_order(10, i) for i in primes])
the_max = np.argmax(periods)

ans = primes[the_max]

print "The answer is: ", ans
