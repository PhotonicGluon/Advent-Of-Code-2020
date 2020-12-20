"""
day20-part1.py

Created on 2020-12-20
Updated on 2020-12-20

Adapted from https://github.com/msullivan/advent-of-code/blob/master/2020/20b.py.
"""

# IMPORTS
import re
from collections import defaultdict

from math import sqrt

# CONSTANTS
MONSTER = """\
                  #
#    ##    ##    ###
 #  #  #  #  #  #   """.split("\n")

# INPUT
with open("input.txt", "r") as f:
    content = f.read()
    data = [tile.strip().split("\n") for tile in content.split("\n\n")]

    f.close()


# FUNCTIONS
def extract_ids(string):
    """
    Extract the IDs from the input file.

    Args:
        string (str):
            The contents of the input file.

    Returns:
        list[int]:
            The list of IDs.
    """

    return [int(_x) for _x in re.findall(r"-?\d+", string)]


def rotate(lines):
    """
    Rotate the lines 90 degrees anticlockwise.

    Args:
        lines (list[str])

    Returns:
        list[str]:
            The rotated lines.
    """

    final_lines = []
    for _i in range(len(lines)):
        new_line = "".join(line[_i] for line in lines)  # Rotate the lines 90 degrees clockwise
        final_lines.append(new_line)

    return tuple(reversed(final_lines))


def flip(lines):
    """
    Reverses the order of the lines.

    Args:
        lines (list[str])

    Returns:
        list[str]:
            The flipped lines.
    """

    return tuple(reversed(lines))


def left_edge(lines):
    """
    Gets the left left_tile_edge of the lines.

    Args:
        lines (list[str])

    Returns:
        str:
            The `left_tile_edge` of the lines.
    """

    return "".join(line[0] for line in lines)


def right_edge(lines):
    """
    Gets the right left_tile_edge of the lines.

    Args:
        lines (list[str])

    Returns:
        str:
            The `right_tile_edge` of the lines.
    """

    return "".join(line[-1] for line in lines)


def get_edges(lines):
    """
    Gets the edges of the lines.

    Args:
        lines (list[str])

    Returns:
        list[str]:
            The edges of the lines.
    """

    return [lines[0], lines[-1], left_edge(lines), right_edge(lines)]


def all_edges(lines):
    """
    Get all the possible edges of the lines.

    Args:
        lines (list[str])

    Returns:
        list[str]:
            All possible edges of the lines.
    """

    edges = get_edges(lines)
    return sorted(edges + ["".join(reversed(_x)) for _x in edges])


def moves(lines):
    """
    Performs all possible moves on the grid"s lines.

    Args:
        lines (list[str])

    Returns:
        list[str]:
            The correct orientation of the grid"s lines.
    """

    for _ in range(4):
        yield lines
        yield flip(lines)
        lines = rotate(lines)


def place_tile(left_tile_id, left_tile_edge, get_edge):
    """
    Find a tile and rotation of it that matches with the left tile"s ID or the left tile"s left_tile_edge.

    Args:
        left_tile_id (int)
        left_tile_edge (str)
        get_edge (Function):
            The `get_edge` function picks the `left_tile_edge` of the new tile to compare against.

    Returns:
        tuple[int, list[str]]
    """

    my_edge = [_tile_id for _tile_id in edgeMap[left_tile_edge] if _tile_id != left_tile_id][0]
    my_tile = tiles[my_edge]

    for my_tile in moves(my_tile):
        if left_tile_edge == get_edge(my_tile):
            break

    return my_edge, my_tile


# COMPUTATION
# Process the data as a dictionary
tiles = {}
for tile in data:
    tileID = extract_ids(tile[0])[0]
    tiles[tileID] = flip(tile[1:])

# Get the number of tiles on each side of the image
noTilesPerSide = int(sqrt(len(tiles)))

# Find out which edges are shared by which tile id
edgeMap = defaultdict(list)
for tileID, tile in tiles.items():
    for edge in all_edges(tile):
        edgeMap[edge].append(tileID)

# Find the corner tiles" IDs
cornerTilesIDs = []
for tileID, tile in tiles.items():
    edgeCount = 0
    for edge in get_edges(tile):
        edgeCount += len(edgeMap[edge])

    if edgeCount == 6:  # This is a corner tile
        cornerTilesIDs.append(tileID)

# Pick a corner to be the top-left, and try rotations until the unmatched edges are facing up and left.
firstCornerID = cornerTilesIDs[0]
leftmostTile = tiles[firstCornerID]

while len(edgeMap[left_edge(leftmostTile)]) == 2:
    leftmostTile = rotate(leftmostTile)

# Place the tiles one at a time
# Since they are uniquely matched up, there"s always one unique option for each spot. When going across rows, we pick
# the one that lines up to the left, and in the first column pick the one that matches at the top.
myGrid = [[(-1, [""])] * noTilesPerSide for _ in range(noTilesPerSide)]
myGrid[0][0] = firstCornerID, leftmostTile

for y in range(noTilesPerSide):
    if y != 0:
        leftID, leftTile = myGrid[y - 1][0]
        myGrid[y][0] = place_tile(leftID, leftTile[-1], get_edge=lambda g: g[0])

    for x in range(1, noTilesPerSide):
        leftID, leftTile = myGrid[y][x - 1]
        myGrid[y][x] = place_tile(leftID, right_edge(leftTile), get_edge=left_edge)

# Strip the borders off the tiles
newGrid = [[[""]] * noTilesPerSide for _ in range(noTilesPerSide)]

for i, row in enumerate(myGrid):
    for j, (_, col) in enumerate(row):
        newGrid[i][j] = [character[1:-1] for character in col[1:-1]]

# Build one big image
picture = []

for row in newGrid:
    for i in range(len(row[0])):
        picture += ["".join(col[i] for col in row)]

# Look for monsters
finalCount = 0
for pic in moves(picture):
    count = 0
    for y in range(len(pic) - len(MONSTER)):
        for x in range(len(pic) - len(MONSTER[0])):
            # Check if there"s a monster starting at this position
            match = True
            for y0 in range(len(MONSTER)):
                for x0 in range(len(MONSTER[y0])):
                    if MONSTER[y0][x0] == "#" and pic[y + y0][x + x0] != "#":
                        match = False
                        break
                if not match:
                    break

            if match:
                count += 1

    if count:  # Count is non-zero
        finalCount = count
        break

# OUTPUT
everything = "".join(picture).count("#")
monster = "".join(MONSTER).count("#")

print(everything - monster * finalCount)
