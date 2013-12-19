"""
Created Nov 21, 2012

Author: Spencer Lyon

Project Euler Problem 42
"""
from __future__ import division
import pandas as pd
from time import time
start_time = time()

let_vals = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7,
            'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14,
            'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20,
            'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
f = open('words.txt')
ff = str(f.readline())

words = pd.Series(ff.split(',')).map(lambda s: s.lower())
words = words.map(lambda s: s.strip('"'))

triangles = set([int(1 / 2 * n * (n + 1)) for n in range(1, 21)])

df = pd.DataFrame(words, columns=['word'])


def score_word(s):
    s
    score = 0
    for char in s:
        score += let_vals[char]
    return score

df['scores'] = df.word.map(score_word)

df['triangles'] = df.scores.map(lambda x: x in triangles)

ans = df.triangles.sum()

print('The answer is: %i') % (ans)

running_time = time()
elapsed_time = running_time - start_time
print 'Total Execution time is ', elapsed_time, 'seconds'
