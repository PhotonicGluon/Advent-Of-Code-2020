"""
day10-part1.py

Created on 2020-12-10
Updated on 2020-12-10

Copyright © Ryan Kan
"""

# INPUT
with open("input.txt", "r") as f:
    adaptors = [int(line.strip()) for line in f.readlines()]
    f.close()

# COMPUTATION
adaptors.append(0)  # This is the charging port
adaptors.append(max(adaptors) + 3)  # This is the device
adaptors = sorted(adaptors)  # Sort the list

differenceOf1 = 0
differenceOf3 = 0

for i in range(len(adaptors) - 1):
    difference = adaptors[i + 1] - adaptors[i]
    if difference == 1:
        differenceOf1 += 1
    if difference == 3:
        differenceOf3 += 1

# OUTPUT
print(differenceOf1 * differenceOf3)
