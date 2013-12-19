"""
Project Euler problem 2

8-21-12
"""

import numpy as np

x1 = 1
x2 = 2
vals = np.array([x1, x2])

new_val = 3
i = 0
while new_val < 4e6:
    new_val = vals[i] + vals[i+1]
    vals = np.append(vals, new_val)
    i += 1

vals = vals[:-1]
ans = sum(vals[vals %2 == 0])
