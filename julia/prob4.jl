"""
Project Euler Problem 4

Problem text:

    A palindromic number reads the same both ways. The largest
    palindrome made from the product of two 2-digit numbers is 9009 = 91
    × 99. Find the largest palindrome made from the product of two
    3-digit numbers.

Date: Wed Dec 18 14:38:25 MST 2013

"""
import Tools.is_palindrome


function euler4()
    ans = 0
    for i=100:999
        for j=i:999
            test = i * j
            ans = is_palindrome(test) && test > ans ? test : ans
        end
    end
    return ans
end
