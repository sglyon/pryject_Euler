"""
Problem 1 Project Euler
"""
y=0

for x in range(0,1000):

    if x%3==0 or x%5==0:
        y+=x
print y
