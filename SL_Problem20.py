"""
Created Nov 14, 2012

Author: Spencer Lyon

Project Euler Problem 20
"""
import sympy as sym
import numpy as np

x = str(sym.factorial(100))

xarr = np.array([int(i) for i in x])

ans = xarr.sum()

print 'The answer is: ', ans
