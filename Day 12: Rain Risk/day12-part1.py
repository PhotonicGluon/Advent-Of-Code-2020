"""
day12-part1.py

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
currBearing = 90  # 90 degrees is east

for instruction in instructions:
    if instruction[0] in ["N", "E", "S", "W"]:
        # Move the boat in that direction
        movement = movements[["N", "E", "S", "W"].index(instruction[0])]
        currPos[0] += movement[0] * instruction[1]
        currPos[1] += movement[1] * instruction[1]
    elif instruction[0] in ["L", "R"]:
        # Turn the boat
        currBearing += (-1 if instruction[0] == "L" else 1) * instruction[1]
    else:
        # Move boat in current direction
        movement = movements[(currBearing // 90) % 4]
        currPos[0] += movement[0] * instruction[1]
        currPos[1] += movement[1] * instruction[1]

# Compute manhattan distance
dist = abs(currPos[0]) + abs(currPos[1])

# OUTPUT
print(dist)
