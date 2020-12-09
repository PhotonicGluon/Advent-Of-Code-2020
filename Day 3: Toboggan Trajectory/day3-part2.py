"""
day3-part2.py

Created on 2020-12-03
Updated on 2020-12-09

Copyright © Ryan Kan
"""

# INPUT
with open("input.txt", "r") as f:
    matrix = [[char for char in line.strip()] for line in f.readlines()]
    f.close()

# COMPUTATION
gradients = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]  # These are the gradients that need to be processed
product = 1

for gradient in gradients:
    x, y = (0, 0)  # Starting coordinates
    noTrees = 0

    while y < len(matrix) - 1:
        x, y = ((x + gradient[0]) % len(matrix[0]), y + gradient[1])  # Update the coordinates according to the gradient

        if matrix[y][x] == "#":  # Hit a tree!
            noTrees += 1

    product *= noTrees

# OUTPUT
print(product)
