"""
Created Nov 15, 2012

Author: Spencer Lyon

Project Euler Problem 24
"""
import itertools

x = itertools.permutations('0123456789', 10)

count = 0
for i in x:
    count += 1
    if count == 1000000:
        ans = i
    else:
        pass

ans2 = [int(i) for i in ans]
ans = str(ans2).strip('[]').replace(", ","")
print 'the answer is: ', ans
