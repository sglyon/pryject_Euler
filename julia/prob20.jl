"""
Project Euler Problem 20

Problem text:

    n! means n × (n − 1) × ... × 3 × 2 × 1 For example, 10! = 10 × 9 ×
    ... × 3 × 2 × 1 = 3628800, and the sum of the digits in the number
    10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27. Find the sum of the digits in
    the number 100!

Date: Wed Dec 18 14:38:25 MST 2013

"""
euler20() = sum(digits(factorial(BigInt(100))))

println(euler20())
