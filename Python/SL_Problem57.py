"""
Created Mar 7, 2013

Author: Spencer Lyon

Project Euler Problem 57:


It is possible to show that the square root of two can be expressed as
an infinite continued fraction:

sqrt(2) = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:
1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the
eighth expansion, 1393/985, is the first example where the number of
digits in the numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a
numerator with more digits than denominator?
"""
from __future__ import division
from time import time

start_time = time()

f1 = (3, 2)

ans = 0

for i in range(1, 1000):
    # Just study the first 5 or 6 and you'll see this is true
    f2 = (f1[0] + f1[1] * 2, f1[0] + f1[1])
    if len(str(f2[0])) > len(str(f2[1])):
        ans += 1
    f1 = f2

print("The answer is: %i" % (ans))

running_time = time()
elapsed_time = running_time - start_time
print 'Total Execution time is ', elapsed_time, 'seconds'
