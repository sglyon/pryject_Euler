"""
Project Euler Problem 6

Problem text:

    The sum of the squares of the first ten natural numbers is, 1^2 +
    2^2 + ... + 10^2 = 385 The square of the sum of the first ten
    natural numbers is, (1 + 2 + \\dots b + 10)2 = 552 = 3025$$ Hence
    the difference between the sum of the squares of the first ten
    natural numbers and the square of the sum is $3025 − 385 = 2640$.
    Find the difference between the sum of the squares of the first one
    hundred natural numbers and the square of the sum.

Date: Wed Dec 18 14:38:25 MST 2013

"""
euler6() = sum([1:100])^2 - sum([1:100].^2)
