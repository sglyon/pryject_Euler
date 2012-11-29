"""
Created Nov 19, 2012

Author: Spencer Lyon

Project Euler Problem 33
"""
import numpy as np
from sympy import fraction, Rational
from time import time
start_time = time()

ll = []
for a in xrange(10, 100):
    for b in xrange(a + 1, 100):
        sa = str(a)
        sb = str(b)
        a_set = set(list(sa))
        b_set = set(list(sb))
        if len(a_set) == 2 and len(b_set) == 2:
            unn = a_set & b_set
            if unn:
                if list(unn)[0] != str(0):
                    dup = list(unn)[0]
                    stripa = float(sa.strip(dup))
                    stripb = float(sb.strip(dup))
                    if stripb != 0. and stripa != 0.:
                        diff = stripa / stripb
                        if diff == float(a) / float(b):
                            ll.append((a, b))
arr = np.array(ll)
ans = fraction(Rational(arr.prod(axis=0)[0], arr.prod(axis=0)[1]))[1]

running_time = time()
elapsed_time = running_time - start_time
print 'Total Execution time is ', elapsed_time, 'seconds'
