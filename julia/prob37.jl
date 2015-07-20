"""
Project Euler Problem 37

The number 3797 has an interesting property. Being prime itself, it is possible
to continuously remove digits from left to right, and remain prime at each
stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797,
379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to
right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

Date: 2015-06-17 08:56

"""
function truncs{T<:Integer}(n::T, kind::Symbol=:left)
    sn = string(n)
    out = T[]
    while length(sn) > 1
        sn = kind == :right ? sn[1:end-1] : sn[2:end]
        push!(out, parse(T, sn))
    end
    out
end

is_trunc_prime(n::Integer) =
    ndigits(n) > 1 && isprime(n) ?
        all(map(x->all(map(isprime, x)), map(truncs, [n, n], [:left, :right]))) :
        false


euler37() = sum(filter(is_trunc_prime,  primes(800000)))
