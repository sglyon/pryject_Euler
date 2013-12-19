"""
Project Euler Problem 1

Problem text:

    If we list all the natural numbers below 10 that are multiples of 3
    or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23. Find
    the sum of all the multiples of 3 or 5 below 1000.

Date: Wed Dec 18 14:38:42 MST 2013

"""

function euler1()
    ans = 0.0
    for i=1:999
        if mod(i, 3) == 0 || mod(i, 5) == 0
            ans += i
        end
    end
    return ans
end
