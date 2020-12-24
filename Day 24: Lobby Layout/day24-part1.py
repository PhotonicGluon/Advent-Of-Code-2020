"""
day24-part1.py

Created on 2020-12-24
Updated on 2020-12-24

Copyright © Ryan Kan
"""

# IMPORTS
import re
from collections import defaultdict

# INPUT
with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]
    f.close()

# COMPUTATION
# Determine which tiles are black
floorTiles = defaultdict(lambda: False)  # Set all the floor tiles to white
for line in lines:
    # Determine the individual directions from each line
    directions = re.findall(r"e|se|sw|w|nw|ne", line)

    # Parse the northings and eastings
    northings = directions.count("ne") + directions.count("nw") - directions.count("se") - directions.count("sw")
    eastings = directions.count("e") + directions.count("se") - directions.count("w") - directions.count("nw")

    # Form the coordinate tuple
    coordinate = (northings, eastings)

    # Toggle the state of the floor tile
    floorTiles[coordinate] = not floorTiles[coordinate]

# Count the number of black tiles
noBlack = sum([isBlack is True for isBlack in floorTiles.values()])

# OUTPUT
print(noBlack)
