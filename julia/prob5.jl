"""
Project Euler Problem 5

Problem text:

    2520 is the smallest number that can be divided by each of the
    numbers from 1 to 10 without any remainder. What is the smallest
    positive number that is evenly divisible by all of the numbers from
    1 to 20?

Date: Wed Dec 18 14:38:25 MST 2013

"""
function euler5()
    return reduce(lcm, 1:20)
end
