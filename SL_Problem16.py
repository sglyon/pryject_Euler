"""
Created August 22, 2012

Author: Spencer Lyon
"""
from time import time
start_time = time()

ans = 0
x = str(2 ** 1000)
for i in x:
    ans += int(i)


end_time = time()
elapsed_time = end_time - start_time
print "total time elapsed is ", elapsed_time, " seconds"
print ans