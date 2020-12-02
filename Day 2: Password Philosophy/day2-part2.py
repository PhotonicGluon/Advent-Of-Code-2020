"""
day2-part1.py

Created on 2020-12-02
Updated on 2020-12-02

Copyright © Ryan Kan
"""

# INPUT
with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]
    f.close()

# COMPUTATION
noValid = 0

for line in lines:
    # Parse each line
    positions, character, password = line.split(" ")
    character = list(character)[0]  # Remove the trailing ":".
    firstPosition, secondPosition = [int(x) for x in positions.split("-")]

    # Check the positions
    firstPosHasChar = password[firstPosition - 1] == character
    secondPosHasChar = password[secondPosition - 1] == character

    # Check if only one of the conditions is true
    if firstPosHasChar ^ secondPosHasChar:  # XOR the conditions
        noValid += 1

# OUTPUT
print(noValid)
