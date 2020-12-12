"""
day12-part2.py

Created on 2020-12-12
Updated on 2020-12-12

Copyright © Ryan Kan
"""

# INPUT
with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]
    instructions = [(line[0], int(line[1:])) for line in lines]
    f.close()

# COMPUTATION
# Execute instructions in order
movements = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # North, east, south, west
currPos = [0, 0]
waypointPos = [10, 1]  # 10 units east, 1 unit north

for instruction in instructions:
    if instruction[0] in ["N", "E", "S", "W"]:
        # Move the waypoint in the specified direction
        movement = movements[["N", "E", "S", "W"].index(instruction[0])]
        waypointPos[0] += movement[0] * instruction[1]
        waypointPos[1] += movement[1] * instruction[1]
    elif instruction[0] in ["L", "R"]:
        # Rotate the waypoint relative to the ship
        noRotations = instruction[1] // 90
        directionConst = -1 if instruction[0] == "L" else 1

        for _ in range(noRotations):
            waypointPos[0], waypointPos[1] = directionConst * waypointPos[1], -directionConst * waypointPos[0]
    else:
        # Move boat toward waypoint
        currPos[0] += waypointPos[0] * instruction[1]
        currPos[1] += waypointPos[1] * instruction[1]

# Compute manhattan distance
dist = abs(currPos[0]) + abs(currPos[1])

# OUTPUT
print(dist)
