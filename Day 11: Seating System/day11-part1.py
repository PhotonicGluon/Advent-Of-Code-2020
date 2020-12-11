"""
day11-part1.py

Created on 2020-12-11
Updated on 2020-12-11

Copyright © Ryan Kan
"""

# IMPORTS
from copy import deepcopy

# INPUT
with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]
    tileArrangement = [list(line) for line in lines]
    f.close()


# FUNCTIONS
def is_occupied(index_i, index_j, tile_arrangement):
    """
    Determines whether or not the tile at (`index_i`, `index_j`) is occupied.

    Args:
        index_i (int):
            Row index.
        index_j (int):
            Column index.
        tile_arrangement (List[List[str]]):
            Arrangement of the tiles as a 2D grid.

    Returns:
        bool:
            Whether or not the tile is occupied.
    """

    # Validate inputs
    if not (0 <= index_i <= len(tile_arrangement) - 1):
        raise IndexError
    if not (0 <= index_j <= len(tile_arrangement[0]) - 1):
        raise IndexError

    # Check occupancy
    if tile_arrangement[index_i][index_j] == "#":
        return True
    else:
        return False


def no_occupied_adjacent_seats(index_i, index_j, tile_arrangement):
    """
    Obtains the number of occupied adjacent seats to the tile at (`index_i`, `index_j`).

    Args:
        index_i (int):
            Row index.
        index_j (int):
            Column index.
        tile_arrangement (List[List[str]]):
            Arrangement of the tiles as a 2D grid.

    Returns:
        int:
            The number of occupied adjacent seats.
    """

    occupied_seats = 0

    # Right, Left, Down and Up
    try:
        if is_occupied(index_i + 1, index_j, tile_arrangement):
            occupied_seats += 1
    except IndexError:
        pass

    try:
        if is_occupied(index_i - 1, index_j, tile_arrangement):
            occupied_seats += 1
    except IndexError:
        pass

    try:
        if is_occupied(index_i, index_j + 1, tile_arrangement):
            occupied_seats += 1
    except IndexError:
        pass

    try:
        if is_occupied(index_i, index_j - 1, tile_arrangement):
            occupied_seats += 1
    except IndexError:
        pass

    # Diagonals (Right-Down, Left-Down, Right-Up, Left-Up)
    try:
        if is_occupied(index_i + 1, index_j + 1, tile_arrangement):
            occupied_seats += 1
    except IndexError:
        pass

    try:
        if is_occupied(index_i - 1, index_j + 1, tile_arrangement):
            occupied_seats += 1
    except IndexError:
        pass

    try:
        if is_occupied(index_i + 1, index_j - 1, tile_arrangement):
            occupied_seats += 1
    except IndexError:
        pass

    try:
        if is_occupied(index_i - 1, index_j - 1, tile_arrangement):
            occupied_seats += 1
    except IndexError:
        pass

    # Return the total number of occupied seats around the current seat
    return occupied_seats


def print_arrangement(tile_arrangement):
    """
    Prints the tile arrangement as a string.

    Args:
        tile_arrangement (List[List[str]]):
            Arrangement of the tiles as a 2D grid.

    Returns:
        str:
            String representation of the tiles.
    """

    temp = []
    for tile_row in tile_arrangement:
        temp.append("".join(tile_row))

    return "\n".join(temp)


# COMPUTATION
previousArrangement = deepcopy(tileArrangement)
iteration = 1

while True:
    print(f"=== Iteration {iteration} ===")
    # print(print_arrangement(previousArrangement))
    for i in range(len(previousArrangement)):
        for j in range(len(previousArrangement[0])):
            adjacent_filled_seats = no_occupied_adjacent_seats(i, j, previousArrangement)

            if previousArrangement[i][j] == "L" and adjacent_filled_seats == 0:
                tileArrangement[i][j] = "#"
            elif previousArrangement[i][j] == "#" and adjacent_filled_seats >= 4:
                tileArrangement[i][j] = "L"
            else:
                pass

    if previousArrangement == tileArrangement:  # If the arrangement no longer changes then we terminate the process
        break
    else:
        previousArrangement = deepcopy(tileArrangement)

    iteration += 1

finalArrangement = deepcopy(tileArrangement)

# Count number of filled seats
noFilled = 0
for row in finalArrangement:
    for seat in row:
        if seat == "#":
            noFilled += 1

print(noFilled)
