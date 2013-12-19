"""
Created Mar 7, 2012

Author: Spencer Lyon

Project Euler Problem 51:

If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.
Not all numbers produce palindromes so quickly. For example,

349 + 943 = 1292,
1292 + 2921 = 4213
4213 + 3124 = 7337

That is, 349 took three iterations to arrive at a palindrome.
Although no one has proved it yet, it is thought that some numbers,
like 196, never produce a palindrome. A number that never forms a
palindrome through the reverse and add process is called a Lychrel
number. Due to the theoretical nature of these numbers, and for the
purpose of this problem, we shall assume that a number is Lychrel until
proven otherwise. In addition you are given that for every number below
ten-thousand, it will either (i) become a palindrome in less than fifty
iterations, or, (ii) no one, with all the computing power that exists,
has managed so far to map it to a palindrome. In fact, 10677 is the
first number to be shown to require over fifty iterations before
producing a palindrome: 4668731596684224866951378664 (53 iterations,
                                                      28-digits).

Surprisingly, there are palindromic numbers that are themselves Lychrel
numbers; the first example is 4994.

How many Lychrel numbers are there below ten-thousand?
"""
from __future__ import division
from time import time

start_time = time()

lychrels = set()

for num in range(10, 10001):
    for_num = num  # Forward number
    for i in range(50):
        back_num = int(str(for_num)[::-1])  # reverse number
        for_num += back_num  # Update forward number
        if str(for_num) == str(for_num)[::-1]:  # Check if palindrome
            break  # break out of 'i' loop if it is
    if i == 49:  # See if we lasted all 50 iterations
        lychrels.add(num)  # Add to lychrels if we did last that long

ans = len(lychrels)
print("The answer is: %i" % (ans))

running_time = time()
elapsed_time = running_time - start_time
print 'Total Execution time is ', elapsed_time, 'seconds'
