"""
Created Mar 11, 2013

Author: Spencer Lyon

Project Euler Problem 67:

By starting at the top of the triangle below and moving to adjacent
numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click
and 'Save Link/Target As...'), a 15K text file containing a triangle
with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not
possible to try every route to solve this problem, as there are 2 ** 99
altogether! If you could check one trillion (10 ** 12) routes every second
it would take over twenty billion years to check them all. There is an
efficient algorithm to solve it. ;o)
"""
from __future__ import division
from time import time

start_time = time()

triangle_file = open('triangle.txt', 'r')
data = []

for line in triangle_file:
    data.append([int(x) for x in line.split()])


def remove_last(data):
    last_row = data[-1]
    second_to_last = data[-2]
    for i in range(len(second_to_last)):
        second_to_last[i] += max(last_row[i:i + 2])
    del data[-1]
    del data[-1]
    data.append(second_to_last)
    return data

while len(data) > 1:
    remove_last(data)

print 'The answer is: ', data[0][0]
running_time = time()
elapsed_time = running_time - start_time
print 'Total Execution time is ', elapsed_time, 'seconds'
