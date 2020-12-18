"""
day17-part1.py

Created on 2020-12-17
Updated on 2020-12-17

Copyright © Ryan Kan
"""

# IMPORTS
from copy import deepcopy
from itertools import product

# INPUT
activeNodes = []  # Will store the coordinates of the activated nodes
xRanges = [0, 0]
yRanges = [0, 0]
zRanges = [0, 0]

with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]
    for y, line in enumerate(lines):
        for x, node in enumerate(line):
            if node == "#":
                activeNodes.append((x, y, 0))

            # Update ranges
            xRanges = [min(xRanges[0], x), max(xRanges[1], x)]
            yRanges = [min(yRanges[0], y), max(yRanges[1], y)]

    f.close()


# FUNCTIONS
def determine_no_neighbouring_cubes_of_type(position, active_nodes):
    """
    Determine the number of neighbouring cubes of a specific type.

    Args:
        position (tuple[int]):
            The triplet representing the position of the cube.
        active_nodes (list[tuple[int]]):
            The list of active nodes.

    Returns:
        int:
            The number of cubes that are of a specific type.
    """

    no_of_type = 0
    all_coordinate_differences = list(product([1, 0, -1], repeat=3))
    all_coordinate_differences.remove((0, 0, 0))

    for coordinate_difference in all_coordinate_differences:
        if (position[0] + coordinate_difference[0], position[1] + coordinate_difference[1],
                position[2] + coordinate_difference[2]) in active_nodes:
            no_of_type += 1

    return no_of_type


# COMPUTATION
for cycle in range(1, 6 + 1):
    print("Cycle", cycle)
    tempActiveNodes = deepcopy(activeNodes)

    for x in range(xRanges[0] - 1, (xRanges[1] + 1) + 1):
        for y in range(yRanges[0] - 1, (yRanges[1] + 1) + 1):
            for z in range(zRanges[0] - 1, (zRanges[1] + 1) + 1):
                noActiveCubes = determine_no_neighbouring_cubes_of_type((x, y, z), activeNodes)

                if (x, y, z) in activeNodes:
                    if noActiveCubes not in [2, 3]:
                        tempActiveNodes.remove((x, y, z))  # It is no longer active
                elif noActiveCubes == 3:
                    tempActiveNodes.append((x, y, z))  # It becomes active

    # Update the live nodes
    activeNodes = deepcopy(tempActiveNodes)

    # Update the x, y and z ranges
    xRanges = [xRanges[0] - 1, xRanges[1] + 1]
    yRanges = [yRanges[0] - 1, yRanges[1] + 1]
    zRanges = [zRanges[0] - 1, zRanges[1] + 1]

# OUTPUT
print(len(activeNodes))
