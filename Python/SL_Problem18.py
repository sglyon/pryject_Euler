"""
Created Nov 14, 2012

Author: Spencer Lyon

Project Euler Problem 18
"""
triangle_file = open('prob_18.txt', 'r')
data = []

for line in triangle_file:
    data.append([int(x) for x in line.split()])


def remove_last(data):
    last_row = data[-1]
    second_to_last = data[-2]
    for i in range(len(second_to_last)):
        second_to_last[i] += max(last_row[i:i + 2])
    del data[-1]
    del data[-1]
    data.append(second_to_last)
    return data

while len(data) > 1:
    remove_last(data)

print 'The answer is: ', data[0][0]
