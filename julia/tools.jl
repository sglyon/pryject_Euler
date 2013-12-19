using DataFrames
using Benchmark

module Tools

export
    my_bench,
    new_bench,
    primes1,
    primes2,
    fibn,
    fiblt,
    is_palindrome,
    pascal,
    pascal_row,
    divisors,
    tri_producer,
    gen_prob_skeleton

# TODO: Why do we do this? I do it b/c everyone else does
using DataFrames
using Benchmark

## ------------ ##
#- benchmarking -#
## ------------ ##

function my_bench(args...)
    return benchmark(args...)[["Benchmark", "Iterations", "AverageWall",
                               "TotalWall", "MaxWall", "MinWall"]]
end

# function new_bench(n::Int, m::Int=10)
#     # Create benchmark df for euler problems 1 to n by running m times

#     if isfile("./benchmarks.jld")
#     df =
#     df = my_bench(euler1, "Problems", "euler1()", m)
#     for i=2:n
#         df = [df; my_bench(eval(parse("euler$i")), "Problems", "euler$i()", m)]
#     end
#     return df
# end


function new_bench(n::Int, m::Array{Int, 1})
    # Create benchmark df for euler problems 1 to n by running m times
    if length(m) != n
        error("length(m) must equal n")
    end
    df = my_bench(euler1, "Problems", "euler1()", m[1])
    for i=2:n
        df = [df; my_bench(eval(parse("euler$i")), "Problems", "euler$i()", m[i])]
    end
    return df
end

## ------------- ##
#- Prime Numbers -#
## ------------- ##

function primes1(bound::Integer)
    primes = Array(Int64, bound)
    i = 1
    worthtesting = trues(bound)
    worthtesting[1] = false
    for index in 2:bound
        if worthtesting[index] && isprime(index)
            primes[i] = index
            i += 1
            multiples = index:index:(index * fld(bound, index))
            for multiple in multiples
                worthtesting[multiple] = false
            end
        end
    end
    return primes[1:(i - 1)]
end


function primes2(n::Int)
    s = falses(n)
    n < 2 && return s; s[2] = true
    n < 3 && return s; s[3] = true
    r = ifloor(sqrt(n))
    for x = 1:r
        xx = x*x
        for y = 1:r
            yy = y*y
            i, j, k = 4xx+yy, 3xx+yy, 3xx-yy
            i <= n && (s[i] $= (i%12==1)|(i%12==5))
            j <= n && (s[j] $= (j%12==7))
            1 <= k <= n && (s[k] $= (x>y)&(k%12==11))
        end
    end
    for i = 5:r
        s[i] && (s[i*i:i*i:n] = false)
    end
    return [1:n][s]
end


## ----------------- ##
#- Fibonacci Numbers -#
## ----------------- ##

function fibn(n)
    # Yield the first n fibonacci numbers
    if n < 2 && n > 0
        return n
    end
    x = zeros(n)
    x[1:2] = [1, 2]
    for i=3:n
        x[i] = x[i-1] + x[i-2]
    end
    return x
end


function fiblt(n)
    # List all the fibonacci numbers less than n
    if n <= 3
        return fibn(n)
    end
    x = [1 2]
    new = 5
    ind = 3
    while new <= n
        new = x[ind-1] + x[ind-2]
        ind += 1
        x = [x new]
    end
    return x
end

## ----------- ##
#- Palindromes -#
## ----------- ##

function is_palindrome(n::Integer)
    x = string(n)
    return x == reverse(x)
end


## ---------------- ##
#- Pascal's triange -#
## ---------------- ##

function pascal(n)
    # Yield up to row ``n`` of Pascal's triangle, one row at a time.
    # The first row is row 0.
    function newrow(row)
        #Calculate a row of Pascal's triangle given the previous one."
        prev = 0
        new = zeros(length(row)+1)
        ind = 1
        for x in row
            new[ind] = prev + x
            prev = x
            ind += 1
        end
        new[end] = 1
        return new
    end

    prevrow = [1]
    produce(prevrow)
    for x=1:n
        prevrow = newrow(prevrow)
        produce(prevrow)
    end
end


function pascal_row(n::Int)
    # Return nth row of pascal's triangle
    p_temp() = pascal(n)
    p = Task(p_temp)
    row = 0
    for i=1:n
        row = consume(p)
    end
    return row
end


## -------- ##
#- divisors -#
## -------- ##

divisor_count(n) = prod(collect(values(factor(n))) + 1)


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

## --------------- ##
#- Special Numbers -#
## --------------- ##
function tri_producer(nmax=int(1e6))
    nums = [1:nmax]
    ans = nums[1]
    produce(ans)
    for n=2:nmax
        ans += nums[n]
        produce(ans)
    end
end

## ------- ##
#- Generic -#
## ------- ##


function gen_prob_skeleton(ending::Int; starting::Int=1)
    date = readchomp(`date`)
    for i=starting:ending
        msg = """\"\"\"
        Project Euler Problem $i

        Problem text:

        Date: $date

        \"\"\""""
        f = open("prob$i.jl", "w")
        print(f, msg)
        close(f)
    end
    nothing
end

end  # module
