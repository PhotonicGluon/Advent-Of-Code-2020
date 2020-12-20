"""
day10-part1.py

Created on 2020-12-10
Updated on 2020-12-20

Copyright © Ryan Kan
"""

# INPUT
with open("input.txt", "r") as f:
    adaptors = [int(line.strip()) for line in f.readlines()]
    f.close()

# COMPUTATION
# Arrange the adaptors to form the adaptor array
adaptors.append(0)  # This is the charging port
adaptors = sorted(adaptors)  # Sort the list to form the chain of adaptors
adaptors.append(adaptors[-1] + 3)  # This is the device

# Find the adaptors which have a difference of 1 or a difference of 3
noOfDifferenceOf1 = 0
noOfDifferenceOf3 = 0

for i in range(len(adaptors) - 1):
    difference = adaptors[i + 1] - adaptors[i]
    if difference == 1:
        noOfDifferenceOf1 += 1
    if difference == 3:
        noOfDifferenceOf3 += 1

# OUTPUT
print(noOfDifferenceOf1 * noOfDifferenceOf3)
