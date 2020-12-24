"""
day24-part1.py

Created on 2020-12-24
Updated on 2020-12-24

Copyright © Ryan Kan
"""

# IMPORTS
import re
from collections import defaultdict

from tqdm import trange

# CONSTANTS
NEIGHBOUR_OFFSETS = [(0, -1), (1, -1), (-1, 0), (1, 0), (0, 1), (-1, 1)]  # There are exactly 6 neighbours for each tile

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

# Run 100 days worth of floor tile toggling
for day in trange(1, 101, desc="Simulating 100 days"):
    # Make a copy of the previous floor arrangement
    newFloorTiles = defaultdict(lambda: False)

    # Add the outer ring of tiles
    for tileCoord in floorTiles.keys():
        for offset in NEIGHBOUR_OFFSETS:
            newTileCoord = (tileCoord[0] + offset[0], tileCoord[1] + offset[1])

            # If the tile was not already in the `newFloorTiles` dictionary, add it in
            if newTileCoord not in newFloorTiles:
                newFloorTiles[newTileCoord] = floorTiles.get(newTileCoord, False)  # Set it to false if cannot find

    # Find every tiles' number of neighbours
    for tileCoord, isBlack in newFloorTiles.items():
        noAdjacentBlackTiles = sum(
            [floorTiles[(tileCoord[0] + offset[0], tileCoord[1] + offset[1])] for offset in NEIGHBOUR_OFFSETS])

        if isBlack:
            if noAdjacentBlackTiles == 0 or noAdjacentBlackTiles > 2:
                # The tile is immediately flipped to white
                newFloorTiles[tileCoord] = False  # This means white
        else:  # Is a white tile
            if noAdjacentBlackTiles == 2:
                # The tile is immediately flipped to black
                newFloorTiles[tileCoord] = True

    # Update the current floor tiles dictionary
    floorTiles = newFloorTiles

# Count the number of black tiles at the end
noBlack = sum([isBlack is True for isBlack in floorTiles.values()])

# OUTPUT
print(noBlack)
