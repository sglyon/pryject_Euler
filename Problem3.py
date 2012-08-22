"""
Project Euler problem 3
"""

from sympy.ntheory import factorint

y = 600851475143

factors = factorint(y)

ans = factors.keys()[0]