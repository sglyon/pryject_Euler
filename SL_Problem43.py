"""
Created Nov 21, 2012

Author: Spencer Lyon

Project Euler Problem 40
"""
from time import time
from itertools import permutations

start_time = time()

ans = 0

pans = permutations('1234567890', 10)

by17 = set([17 * i for i in range(1, 1000 // 17 + 1)])
by13 = set([13 * i for i in range(1, 1000 // 13 + 1)])
by11 = set([11 * i for i in range(1, 1000 // 11 + 1)])
by7 = set([7 * i for i in range(1, 1000 // 7 + 1)])
by5 = set([5 * i for i in range(1, 1000 // 5 + 1)])
by3 = set([3 * i for i in range(1, 1000 // 3 + 1)])
by2 = set([2 * i for i in range(1, 1000 // 2 + 1)])

for num in pans:
    ts = ''
    for digit in num:
        ts += digit
    if int(ts[7:10]) in by17:
        if int(ts[6:9]) in by13:
            if int(ts[5:8]) in by11:
                if int(ts[4:7]) in by7:
                    if int(ts[3:6]) in by5:
                        if int(ts[2:5]) in by3:
                            if int(ts[1:4]) in by2:
                                ans += int(ts)

print("The answer is: %s") % (str(ans))

running_time = time()
elapsed_time = running_time - start_time
print 'Total Execution time is ', elapsed_time, 'seconds'
