"""
Created Nov 14, 2012

Author: Spencer Lyon

Project Euler problem 22
"""
import pandas as pd
import numpy as np

df = pd.DataFrame.from_csv('names.txt')

df.sort_index(inplace=1)
df['rank'] = np.arange(1, 5164)

newdf = pd.DataFrame(df.index, index=df['rank'], columns=['Name'])
newdf.ix[1]['Name'] = 'NA'  # this is because pandas converts 'NA' to NaN
newdf = newdf.sort('Name')
newdf['Real Rank'] = range(1, 5164)
newdf = newdf.set_index('Real Rank')


scores = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8,
          'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15,
          'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22,
          'W': 23, 'X': 24, 'Y': 25, 'Z': 26}


def name_score(x):
    temp = 0
    for i in str(x):
        temp += scores[i]
    return temp

newdf['Name Score'] = newdf['Name'].map(name_score)
newdf['Total Score'] = newdf.index.values * newdf['Name Score'].values

ans = newdf['Total Score'].sum()

print 'The answer is: ', ans
