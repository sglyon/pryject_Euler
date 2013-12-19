"""
Project Euler Problem 9

Problem text:

    A Pythagorean triplet is a set of three natural numbers, a  b  c,
    for which, a^2 + b^2 = c^2 For example,$3^2 + 4^2 = 9 + 16 = 25 =
    5^2. There exists exactly one Pythagorean triplet for which a + b +
    c = 1000. Find the product abc.

Date: Wed Dec 18 14:38:25 MST 2013

"""
function euler9()
    for a=1:1000
        for b=a:1000
            c = sqrt(a^2 + b^2)
            if a + b + c == 1000
                return int(a * b * c)
            end
        end
    end
end
