"""
Project Euler Problem 21

Problem text:

    Let d(n) be defined as the sum of proper divisors of n (numbers less
    than n which divide evenly into n). If d(a) = b and d(b) = a,
    where a ≠ b, then a and b are an amicable pair and each of a and
    b are called amicable numbers. For example, the proper divisors of
    220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220)
    = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284)
    = 220. Evaluate the sum of all the amicable numbers under 10000.

Date: Wed Dec 18 14:38:25 MST 2013

"""
import Tools.divisors

d_n(n::Int) = sum(divisors(n)[1:end-1])::Int

function euler21()
    ans = 0
    for i=1:10000
        a = d_n(i)
        b = d_n(a)
        if i == b
            if b != a
                ans += i
            end
        end
    end
    return ans
end
