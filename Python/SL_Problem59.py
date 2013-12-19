"""
Created Mar 16, 2013

Author: Spencer Lyon

Project Euler Problem 59:

Each character on a computer is assigned a unique code and the preferred
standard is ASCII (American Standard Code for Information Interchange).
For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to
ASCII, then XOR each byte with a given value, taken from a secret key.
The advantage with the XOR function is that using the same encryption
key on the cipher text, restores the plain text; for example,
65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text
message, and the key is made up of random bytes. The user would keep the
encrypted message and the encryption key in different locations, and
without both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified
method is to use a password as a key. If the password is shorter than
the message, which is likely, the key is repeated cyclically throughout
the message. The balance for this method is using a sufficiently long
password key for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three
lower case characters. Using cipher1.txt, a file containing the
encrypted ASCII codes, and the knowledge that the plain text must
contain common English words, decrypt the message and find the sum of
the ASCII values in the original text.
"""
from __future__ import division
from time import time
from itertools import permutations


def apply_cipher(key):
    big_key = list(key * factor)
    for i in range(extra):
        big_key.append(key[i])
    new_msg = []
    for i in range(len(big_key)):
        new_msg.append(str(int(msg_list[i]) ^ ord(big_key[i])))

    return new_msg


def convert_to_str(msg):
    text_list = []
    for i in msg:
        text_list.append(chr(int(i)))
    return ''.join(text_list)


start_time = time()

f = open('cipher1.txt')
msg_list = f.readline().strip().split(',')
msg_size = len(msg_list)
factor = msg_size // 3
extra = msg_size % 3

# NOTE: In python ord goes str -> ASCII and chr goes ASCII to str
test_group = permutations('abcdefghijklmnopqrstuvwxyz', 3)

# I guess that the space the most common character. I use this to find the key
space = ord(' ')

current_max = 0
current_code = None

for i in test_group:
    new_msg = apply_cipher(i)
    text = convert_to_str(new_msg)
    if 'the' in text and 'and' in text and 'in' in text and 'this' in text:
        break

print text
ans = sum([int(n) for n in new_msg])

print("The answer is: %i" % (ans))

running_time = time()
elapsed_time = running_time - start_time
print 'Total Execution time is ', elapsed_time, 'seconds'
