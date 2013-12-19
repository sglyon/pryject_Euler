"""
Project Euler Problem 22

Problem text:

    Using names.txt, a 46K text file containing over five-thousand first
    names, begin by sorting it into alphabetical order. Then working out
    the alphabetical value for each name, multiply this value by its
    alphabetical position in the list to obtain a name score. For
    example, when the list is sorted into alphabetical order, COLIN,
    which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the
    list. So, COLIN would obtain a score of 938  53 = 49714. What is the
    total of all the name scores in the file?s

Date: Wed Dec 18 14:38:25 MST 2013

"""
scores = Dict(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
               "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
               "U", "V", "W", "X", "Y", "Z"], [1:26])

score(name) = int(sum([scores[string(i)] for i in name]))

function euler22()
    f = open("../data/names.txt")
    text = readall(f)
    close(f)
    names = sort([strip(i, ['\\', '"', ',']) for i in split(text, '\n')[2:end]])
    n_names = length(names)::Int
    raw_scores = zeros(Int, n_names)::Array{Int, 1}
    for i=1:n_names
        raw_scores[i] = score(names[i])
    end
    scores = raw_scores .* [1:length(names)]
    return sum(scores)
end

println(euler22())
