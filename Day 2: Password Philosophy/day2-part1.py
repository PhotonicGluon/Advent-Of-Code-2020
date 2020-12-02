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
    limits, character, password = line.split(" ")
    character = list(character)[0]  # Remove the trailing ":".

    # Count the number of instances of `character` in `password`
    noCharacter = 0
    for char in password:
        if char == character:
            noCharacter += 1

    # Check if `noCharacter` is within the limits
    lowerBound, upperBound = [int(x) for x in limits.split("-")]

    if lowerBound <= noCharacter <= upperBound:
        noValid += 1

# OUTPUT
print(noValid)
