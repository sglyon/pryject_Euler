"""
Project Euler Problem 3

Problem text:

    The prime factors of 13195 are 5, 7, 13 and 29. What is the largest
    prime factor of the number 600851475143 ?

Date: Wed Dec 18 14:38:25 MST 2013

"""
euler3() = maximum(keys(factor(600851475143)))
