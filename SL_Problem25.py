"""
Created Nov 15, 2012

Author: Spencer Lyon

Project Euler Problem 25
"""
import sympy as sym
import numpy as np

fibs = [str(sym.fibonacci(n)) for n in xrange(5000)]
lens = np.array([len(fibs[i]) for i in xrange(5000)])

ans = np.where(lens == 1000)[0][0]

print 'The answer is: ', ans
