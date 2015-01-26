#=
Project Euler Problem 36

Problem text:

The decimal number, 585 = 1001001001 (binary), is palindromic in both
bases.

Find the sum of all numbers, less than one million, which are
palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not
(include leading zeros.)

Date: 2014-09-24 23:05:51

=#
using Tools.is_palindrome

@everywhere both_pal(i) = is_palindrome(i) && is_palindrome(base(2, i)) ? i : 0

euler36() = @parallel (+) for i=1:1000000
    both_pal(i)
end

