"""
Created August 22, 2012

Author: Spencer Lyon
"""
from time import time
import numpy as np
start_time = time()

def pascal(n):
    """
    Yield up to row ``n`` of Pascal's triangle, one row at a time.

    The first row is row 0.
    """
    def newrow(row):
        "Calculate a row of Pascal's triangle given the previous one."
        prev = 0
        for x in row:
            yield prev + x
            prev = x
        yield 1

    prevrow = [1]
    yield prevrow
    for x in xrange(n):
        prevrow = list(newrow(prevrow))
        yield prevrow


def coefs(h, j):
    """
    Parameters
    ----------
    h: number, int
        The number of parameters in the polynomial expansion.
    j: number, int
        The degree of the expansion.

    Returns
    -------
    element: number, int
        The number of coefficients in a jth order polynomial expansion in terms
        of h parameters.
    """
    # gather all rows into a list
    pas = np.asarray(list(pascal(h + j)))

    #Pull out the last row
    theRow = pas[-1]

    # grab the correct element.
    element = theRow[j]



    return element

ans = coefs(20, 20)

end_time = time()
elapsed_time = end_time - start_time
print "total time elapsed is ", elapsed_time, " seconds"
print ans