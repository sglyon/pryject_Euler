"""
Project Euler Problem 17

Problem text:

    If the numbers 1 to 5 are written out in words: one, two, three,
    four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in
    total. If all the numbers from 1 to 1000 (one thousand) inclusive
    were written out in words, how many letters would be used?

    NOTE: Do not count spaces or hyphens. For example, 342 (three
    hundred and forty-two) contains 23 letters and 115 (one hundred and
    fifteen) contains 20 letters. The use of "and" when writing out
    numbers is in compliance with British usage.

Date: Wed Dec 18 14:38:25 MST 2013

"""
function euler17()
    # Note, I just did this by hand
    one2nine = 3+3+5+4+4+3+5+5+4
    ten2nineteen = 3+6+6+8+8+7+7+9+8+8
    twenty2ninetynine = 10*(6+6+5+5+5+7+6+6) + 8*one2nine

    one2ninetynine = one2nine + ten2nineteen + twenty2ninetynine

    ## Just some simple tricks
    #1-9 appears 100 times
    internal = one2nine * 100

    #1-99 comes up 10 times
    mains = one2ninetynine * 10

    hundereds = 7 * 9

    #hundered_and
    hundered_and = 9*99*10

    one_thousand = 11

    internal + mains + hundereds + hundered_and + one_thousand
end
