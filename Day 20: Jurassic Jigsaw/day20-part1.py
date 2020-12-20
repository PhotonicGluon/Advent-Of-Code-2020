"""
day20-part1.py

Created on 2020-12-20
Updated on 2020-12-20

Adapted from https://github.com/msullivan/advent-of-code/blob/master/2020/20a.py.
"""

# IMPORTS
from collections import defaultdict
import re

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

    return [int(x) for x in re.findall(r"-?\d+", string)]


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
    for i in range(len(lines)):
        new_line = "".join(line[i] for line in lines)  # Rotate the lines 90 degrees clockwise
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
    return sorted(edges + ["".join(reversed(x)) for x in edges])


# COMPUTATION
# Process the data as a dictionary
tiles = {}
for tile in data:
    tileID = extract_ids(tile[0])[0]
    tiles[tileID] = flip(tile[1:])

# Find out which edges are shared by which tile id
edgeMap = defaultdict(list)
for tileID, tile in tiles.items():
    for edge in all_edges(tile):
        edgeMap[edge].append(tileID)

# Find the corner tiles' IDs
cornerTilesIDs = []
for tileID, tile in tiles.items():
    edgeCount = 0
    for edge in get_edges(tile):
        edgeCount += len(edgeMap[edge]) - 1  # Exclude the original tile

    if edgeCount == 2:  # This is a corner tile because it only has two edges
        cornerTilesIDs.append(tileID)

# OUTPUT
# Multiply all corner tiles' IDs together
answer = 1
for tileID in cornerTilesIDs:
    answer *= tileID

print(answer)
