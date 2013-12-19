"""
Created 2013-10-09 07:51:26

Author: Spencer Lyon

Project Euler Problem 23

A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper divisors of 28
would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n
and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
number that can be written as the sum of two abundant numbers is 24. By
mathematical analysis, it can be shown that all integers greater than 28123 can
be written as the sum of two abundant numbers. However, this upper limit cannot
be reduced any further by analysis even though it is known that the greatest
number that cannot be expressed as the sum of two abundant numbers is less than
this limit.

Find the sum of all the positive integers which cannot be written as the sum of
two abundant numbers.

"""
flatten{T}(a::Array{T}) = reshape(a,prod(size(a)))

function divisors(x::Int)
    i = 2::Int
    divs = [1]::Array{Int, 1}
    for i=2:(ceil(sqrt(x)) + 1)
        if mod(x, i) == 0
            if i != x / i
                append!(divs, [i, x / i])
            else
                append!(divs, [i])
            end
        end
    end
    append!(divs, [x])
    return unique(sort(divs))
end

function classify(n::Int)
    sum_divs::Int = sum(divisors(n)[1:end-1])
    if sum_divs == n
        return int(0)
    elseif sum_divs < n
        return int(1)
    else
        return int(2)
    end
end

function euler23()

    nums = [1:28123]
    classy = [classify(i) for i in nums]
    abuns = nums[classy .== 2]
    a = repmat(abuns, 1, length(abuns))
    all_sums = a + a'

    candidates = unique(flatten(all_sums))
    candidates = candidates[candidates .<= 28123]
    ans = sum(setdiff(nums, candidates))

    return ans
end

ans = @time euler23()
