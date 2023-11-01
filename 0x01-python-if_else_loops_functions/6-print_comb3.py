#!/usr/bin/python3
for a in range(0, 9):
    for z in range(a + 1, 10):
        if a != 8:
            print("{}{}".format(a, z), end=", ")
print("89")
