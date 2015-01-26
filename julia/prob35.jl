#=
Project Euler Problem 35

Problem text:

The number, 197, is called a circular prime because all rotations of the
digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31,
37, 71, 73, 79, and 97.

How many circular primes are there below one million?

Date: Wed Dec 18 14:38:25 MST 2013

=#
import Base: length, start, next, done

immutable Rotation{T, S <: String}
    a::T
    sa::S
end

Rotation{T <: Integer}(a::T) = Rotation(a, string(a))
Rotation{S <: String}(a::S) = Rotation(a, a)
length(r::Rotation) = length(r.sa)

# Define iteration stuff
start(r::Rotation) = 1:length(r)  # start with range so last done func is easy
next{T <: Integer}(r::Rotation{T}, s) = (parseint(T, r.sa[s]), [s[2:end], s[1]])
done(r::Rotation, s) = s[1] == 1 && typeof(s) <: Array

is_cyclical(a::Integer) = all(isprime, Rotation(a))

euler35() = length(filter(is_cyclical, primes(1000000)))
