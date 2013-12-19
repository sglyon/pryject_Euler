"""
Created Nov 20, 2012

Author: Spencer Lyon

Project Euler Problem 39
"""
import numpy as np
import pandas as pd
from itertools import product
from time import time
start_time = time()

x = np.arange(2, 500, 1)

legs = np.array(list(product(x, x)))

hypot = np.hypot(legs[:, 0], legs[:, 1])

hyint = np.array(hypot, dtype=int)

take = hypot / hyint == 1

good_leg = legs[take]

good_hypot = hypot[take]

triangles = np.column_stack((good_leg, good_hypot))

data = pd.DataFrame(np.column_stack((triangles, triangles.sum(1))),
                    columns=['a', 'b', 'c', 'perimeter'])

ans = data.perimeter.value_counts().index[0]

print "The answer is: ", ans

running_time = time()
elapsed_time = running_time - start_time
print 'Total Execution time is ', elapsed_time, 'seconds'


