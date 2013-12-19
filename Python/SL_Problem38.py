"""
Created Nov 20, 2012

Author: Spencer Lyon

Project Euler Problem 38
"""
the_max = 0
argmax = 0

for i in xrange(9999, 0, -1):
    st1 = str(i)
    st2 = str(2 * i)

    if (len(st1) + len(st2)) >= 9:
        if (len(st1) + len(st2)) > 9:
            pass
        elif (len(st1) + len(st2)) == 9:
            temp = set(st1 + st2)
            if len(temp) == 9 and '0' not in temp:
                if int(st1 + st2) > the_max:
                    the_max = int(st1 + st2)
                    argmax = i
