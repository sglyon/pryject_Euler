"""
Project Euler Problem 16

Problem text:

    2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

    What is the sum of the digits of the number 2^1000?

Date: Wed Dec 18 14:38:25 MST 2013

"""
euler16() = sum(digits(BigInt(2)^1000))
