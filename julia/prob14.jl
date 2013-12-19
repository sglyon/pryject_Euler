"""
Project Euler Problem 14

Problem text:

    The following iterative sequence is defined for the set of positive integers:

    n ->  n/2 (n is even)
    n -> 3n + 1 (n is odd)

    Using the rule above and starting with 13, we generate the following sequence:

    13  40  20  10  5  16  8  4  2  1

    It can be seen that this sequence (starting at 13 and finishing at
    1) contains 10 terms. Although it has not been proved yet (Collatz
    Problem), it is thought that all starting numbers finish at 1. Which
    starting number, under one million, produces the longest chain?
    NOTE: Once the chain starts the terms are allowed to go above one
    million.

Date: Wed Dec 18 14:38:25 MST 2013

"""
function collatz_length(n::Int)
    ans = 1
    new_num = n
    while new_num > 1
        ans += 1
        new_num::Int = iseven(new_num) ? new_num / 2 : 3 * new_num + 1
    end
    return ans
end

function euler14()
    ans = 0
    new_len = 0
    old_len = 0
    for i=1:2:1e6
        new_len::Int = collatz_length(int(i))
        if new_len > old_len
            ans::Int = i
            old_len::Int = new_len
        end
    end
    return ans
end

println(euler14())
