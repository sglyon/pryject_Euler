"""
project euler problem 5
"""
from numpy import arange

divisors = arange(1,21)
x = True
i = 1
while x:
    test = i * 20
    if sum(test % divisors) == 0:
        print test
        x = False
    i += 1

answer = test  # From Josh

print(answer)
