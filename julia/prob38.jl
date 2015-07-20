"""
Project Euler Problem 38

Problem text:

Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We will
call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and
5, giving the pandigital, 918273645, which is the concatenated product of 9 and
(1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the
concatenated product of an integer with (1,2, ... , n) where n > 1?

Date: Wed Dec 18 14:38:25 MST 2013

"""

function euler38()
    ans = 0
    for i=9999:-1:1
        s1 = string(i)
        s2 = string(2i)

        if length(s1) + length(s2) == 9
            tmp = Set(s1*s2)
            if length(tmp) == 9 && !('0' in tmp)
                ci = parse(Int, s1*s2)
                ans = max(ans, ci)
            end
        end
    end
    ans
end
