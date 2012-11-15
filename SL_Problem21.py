"""
Created Nov 14, 2012

Author: Spencer Lyon

Project Euler Problem 21
"""
import sympy as sym
import numpy as np
import pandas as pd


def d(n):
    """
    Implementation of the d(n) function in the problem description
    """
    return sum(sym.divisors(n)[:-1])

the_range = np.arange(1, 10001)
all_ds = np.asarray([d(i) for i in the_range])
all_d_ds = np.asarray([d(i) for i in all_ds])

data = pd.DataFrame(np.column_stack([all_ds, all_d_ds]), index=the_range,
                    columns=['d(n)', 'd(d(n))'])
data.index.name = 'n'

matches = data[data.index == data['d(d(n))']]

amicables = matches[matches.index != matches['d(n)']]

ans = amicables.sum()['d(n)']

print 'The answer is: ', ans
