"""
day3-part2.py

Created on 2020-12-03
Updated on 2020-12-03

Copyright © Ryan Kan
"""

# INPUT
with open("input.txt", "r") as f:
    matrix = [[char for char in line.strip()] for line in f.readlines()]
    f.close()

# COMPUTATION
gradients = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
product = 1

for gradient in gradients:
    i, j = (0, 0)  # Starting indices
    noTrees = 0

    while j < len(matrix) - 1:
        i, j = ((i + gradient[0]) % len(matrix[0]), j + gradient[1])

        if matrix[j][i] == "#":
            noTrees += 1

    product *= noTrees

# OUTPUT
print(product)
