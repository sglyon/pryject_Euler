"""
Created Nov 14, 2012

Author: Spencer Lyon

Project Euler Problem 19
"""
import pandas as pd
sundays = pd.date_range('1/1/1901', '12/31/2000', freq='W-SUN')

count = 0

for month in sundays:
    if month.day == 1:
        count += 1

print 'The answer is:', count
