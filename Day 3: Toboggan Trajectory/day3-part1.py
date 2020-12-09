"""
day3-part1.py

Created on 2020-12-03
Updated on 2020-12-09

Copyright © Ryan Kan
"""

# INPUT
with open("input.txt", "r") as f:
    matrix = [[char for char in line.strip()] for line in f.readlines()]
    f.close()

# COMPUTATION
gradient = (3, 1)  # Represents the gradient of "right 3, down 1"
x, y = (0, 0)  # Starting coordinates

noTrees = 0  # Number of trees that were collided
while y < len(matrix) - 1:
    x, y = ((x + gradient[0]) % len(matrix[0]), y + gradient[1])  # Update the coordinates according to the gradient

    if matrix[y][x] == "#":  # Hit a tree!
        noTrees += 1

# OUTPUT
print(noTrees)
