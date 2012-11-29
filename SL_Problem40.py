"""
Created Nov 21, 2012

Author: Spencer Lyon

Project Euler Problem 40
"""
from time import time
start_time = time()

x = ''

for i in xrange(1, 1000000):
    x += str(i)

ans = int(str(x[0])) * int(str(x[9])) * int(str(x[99])) * int(str(x[999])) * \
      int(str(x[9999])) * int(str(x[99999])) * int(str(x[999999]))

print('The answer is %s') % (str(ans))

running_time = time()
elapsed_time = running_time - start_time
print 'Total Execution time is ', elapsed_time, 'seconds'

