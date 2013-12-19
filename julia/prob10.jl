"""
Project Euler Problem 10

Problem text:

    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17. Find the sum
    of all the primes below two million.

Date: Wed Dec 18 14:38:25 MST 2013

"""
euler10() = sum(primes2(int(2e6)))
