"""
Created Nov 16, 2012

Author: Spencer Lyon

Project Euler Problem 28
"""
import numpy as np
from time import time

start_time = time()

ur_stride = np.arange(8, 8 * 500 + 1, 8)
dr_stride = ur_stride - 6
dl_stride = ur_stride - 4
ul_stride = ur_stride - 2

ur = np.zeros(500)
dr = np.zeros(500)
dl = np.zeros(500)
ul = np.zeros(500)

ur[0] = 9
dr[0] = 3
dl[0] = 5
ul[0] = 7

for i in range(1, 500):
    ur[i] = ur[i - 1] + ur_stride[i]
    dr[i] = dr[i - 1] + dr_stride[i]
    dl[i] = dl[i - 1] + dl_stride[i]
    ul[i] = ul[i - 1] + ul_stride[i]

ans = ur.sum() + dr.sum() + dl.sum() + ul.sum() + 1

print 'The answer is: ', ans

running_time = time()
elapsed_time = running_time - start_time
print 'Total Execution time is ', elapsed_time, 'seconds'
