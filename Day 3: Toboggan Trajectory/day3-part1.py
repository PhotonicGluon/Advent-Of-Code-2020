"""
day3-part1.py

Created on 2020-12-03
Updated on 2020-12-03

Copyright © Ryan Kan
"""

# INPUT
with open("input.txt", "r") as f:
    matrix = [[char for char in line.strip()] for line in f.readlines()]
    f.close()

# COMPUTATION
gradient = (3, 1)  # Right 3, Down 1
i, j = (0, 0)  # Starting indices

noTrees = 0
while j < len(matrix) - 1:
    i, j = ((i + gradient[0]) % len(matrix[0]), j + gradient[1])

    if matrix[j][i] == "#":
        noTrees += 1

# OUTPUT
print(noTrees)
