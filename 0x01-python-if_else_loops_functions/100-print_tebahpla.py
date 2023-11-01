#!/usr/bin/python3
for char in range(ord('Z'), ord('A')-1, -1):
    if char % 2 == 0:
        char = char + 32
    print("{:c}".format(char), end='')
