"""
project euler problem 4
"""
biggest = 0

for i in range(100,1000):
    for j in range(100, i):
        t = i * j
        if t > biggest:
            y = str(t)
            if y[::-1] == y:
                biggest = t

print biggest
