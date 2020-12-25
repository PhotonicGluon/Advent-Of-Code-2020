"""
day3-part1.py

Created on 2020-12-03
Updated on 2020-12-20

Copyright © Ryan Kan
"""

# INPUT
with open("input.txt", "r") as f:
    matrix = [[char for char in line.strip()] for line in f.readlines()]
    f.close()

# COMPUTATION
gradient = (3, 1)  # Represents the gradient of "right 3, down 1"
x, y = (0, 0)  # Starting coordinates

noCollidedTrees = 0
while y < len(matrix) - 1:
    x, y = ((x + gradient[0]) % len(matrix[0]), y + gradient[1])  # Update the coordinates according to the gradient

    if matrix[y][x] == "#":  # A tree was hit!
        noCollidedTrees += 1

# OUTPUT
print(noCollidedTrees)
