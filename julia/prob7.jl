"""
Project Euler Problem 7

Problem text:

    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we
    can see that the 6th prime is 13. What is the 10001st prime number?

Date: Wed Dec 18 14:38:25 MST 2013

"""
function euler7()
    n = 10001
    p, f = 5, 1
    while n > 3
        p += 3-f
        f = -f
        if isprime(p)
            n -= 1
        end
    end
    return p
end
