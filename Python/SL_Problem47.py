"""
Created Nov 21, 2012

Author: Spencer Lyon

Project Euler Problem 47
"""
from time import time
start_time = time()

from sympy import primefactors

found = 0
n1 = 1
n2 = 2
n3 = 3
n4 = 4
while found == 0:
    if len(primefactors(n1)) == 4:
        if len(primefactors(n2)) == 4:
            if len(primefactors(n3)) == 4:
                if len(primefactors(n4)) == 4:
                    ans = n1
                    found = 1

    n1 += 1
    n2 += 1
    n3 += 1
    n4 += 1

print("The answer is: %i") % (ans)

running_time = time()
elapsed_time = running_time - start_time
print 'Total Execution time is ', elapsed_time, 'seconds'
