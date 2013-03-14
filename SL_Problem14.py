"""
Created August 22, 2012

Author: Spencer Lyon
"""
from time import time

start_time = time()
ans = 0
max_len = 0

def get_chain_length(n, count=1):
    while n > 1:
        count += 1
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1

    return count

for i in xrange(999999, 3, -2):
    c = get_chain_length(i)
    if c > max_len:
        max_len = c
        ans = i


end_time = time()
elapsed_time = end_time - start_time
print "total time elapsed is ", elapsed_time, " seconds"
print [ans, max_len]


def get_chain(n):
    chain = []
    while n > 1:
        chain.append(n)
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1

    return chain
