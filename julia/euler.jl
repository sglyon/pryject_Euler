module Euler

using Iterators
using DataStructures
using Benchmarks

function prob39()
    d = Dict{Int,Int}()
    sizehint!(d, 498)
    for l1 in 2:499
        for l2 in l1:499
            h = hypot(l1, l2)
            if isinteger(h)
                k = l1 + l2 + Int(h)
                d[k] = get(d, k, 0) + 1
            end
        end
    end
    collect(keys(d))[indmax(values(d))]
end

function prob40()
    io = IOBuffer()
    for i in 1:1000000
        print(io, i)
    end
    data = takebuf_array(io)
    c = Int('0')
    reduce(*, 1, [Int(data[10^i]) - c for i in 1:6])
end

function prob41()
    pans = permutations(collect(1:7))
    out = 0
    for num in pans
        if iseven(num[end])
            continue
        end
        temp = parse(Int, join(num))
        if isprime(temp)
            out = max(temp, out)
        end
    end
    out
end

function prob42()
    words = vec(readdlm("../data/words.txt", ',', ASCIIString))
    table = Dict(zip('A':'Z', 1:26))

    score_word(w) = reduce(+, 0, [table[i] for i in w])::Int
    scores = map(score_word, words)
    max_score = maximum(scores)

    triangles = Int[]
    for i in 1:100
        t = (i*(i+1)) >> 1
        if t > max_score
            break
        end
        push!(triangles, t)
    end

    out = 0
    for s in scores
        if s in triangles
            out += 1
        end
    end
    out
end

function prob43()
    by17 = Set([17i for i in 1:div(1000, 17)])
    by13 = Set([13i for i in 1:div(1000, 13)])
    by11 = Set([11i for i in 1:div(1000, 11)])
    by7 = Set([7i for i in 1:div(1000, 7)])
    by5 = Set([5i for i in 1:div(1000, 5)])
    by3 = Set([3i for i in 1:div(1000, 3)])
    by2 = Set([2i for i in 1:div(1000, 2)])

    pans = permutations(collect(0:9))
    out = 0
    for num in pans
        if parse(Int, join(num[8:10])) in by17
            if parse(Int, join(num[7:9])) in by13
                if parse(Int, join(num[6:8])) in by11
                    if parse(Int, join(num[5:7])) in by7
                        if parse(Int, join(num[4:6])) in by5
                            if parse(Int, join(num[3:5])) in by3
                                if parse(Int, join(num[2:4])) in by2
                                    out += parse(Int, join(num))
                                end
                            end
                        end
                    end
                end
            end
        end
    end
    out
end

function prob44()
    pents = Set([(i*(3i-1)) >> 1 for i in 1:3000])
    out = typemax(Int)
    for p1 in pents, p2 in pents
        if (abs(p1 - p2) in pents) & (p1 + p2 in pents)
            if abs(p1 - p2) < out
                out = abs(p1 - p2)
            end
        end
    end
    out
end

function prob45()
    hex_num(n) = n*(2n-1)
    pent_check(x) = isinteger((sqrt(24x +1) + 1) / 6)

    n = 144
    local out
    while true
        next_hex = hex_num(n)
        if pent_check(next_hex)
            out = next_hex
            break
        end
        n += 1
    end
    out
end

function prob46()
    twice_sq = 2 * (1:100).^2

    n = 35
    local out
    while true
        if !isprime(n)
            possible = n - twice_sq[twice_sq .< n]
            if !any(map(isprime, possible))
                out = n
                break
            end
        end
        n += 2
    end
    out
end

function prob47()
    n1, n2, n3, n4 = 1, 2, 3, 4
    while true
        if length(factor(n1)) == 4
            if length(factor(n2)) == 4
                if length(factor(n3)) == 4
                    if length(factor(n4)) == 4
                        break
                    end
                end
            end
        end
        n1, n2, n3, n4 = n2, n3, n4, n4 +1
    end
    n1
end

prob48() = string(sum([big(i)^i for i in 1:1000]))[end-9:end]

function prob49()

end


end  # module
