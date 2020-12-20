"""
day11-part2.py

Created on 2020-12-11
Updated on 2020-12-20

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
def get_tile_type(index_i, index_j, tile_arrangement):
    """
    Gets the tile type at (`index_i`, `index_j`).

    Args:
        index_i (int):
            Row index.
        index_j (int):
            Column index.
        tile_arrangement (List[List[str]]):
            Arrangement of the tiles as a 2D grid.

    Returns:
        str:
            The type of tile, chosen from the list ["Occupied", "Free", "Floor"].
    """

    # Validate inputs
    if not (0 <= index_i <= len(tile_arrangement) - 1):
        raise IndexError
    if not (0 <= index_j <= len(tile_arrangement[0]) - 1):
        raise IndexError

    # Check occupancy
    if tile_arrangement[index_i][index_j] == "#":
        return "Occupied"
    elif tile_arrangement[index_i][index_j] == "L":
        return "Free"
    else:
        return "Floor"


def no_occupied_visible_seats(index_i, index_j, tile_arrangement):
    """
    Obtains the number of visible occupied seats to the tile at (`index_i`, `index_j`).

    Args:
        index_i (int):
            Row index.
        index_j (int):
            Column index.
        tile_arrangement (List[List[str]]):
            Arrangement of the tiles as a 2D grid.

    Returns:
        int:
            The number of occupied visible seats.
    """

    occupied_seats = 0

    # Right, Left, Down and Up
    try:
        value = 1
        while True:
            occupancy = get_tile_type(index_i + value, index_j, tile_arrangement)
            if occupancy == "Occupied":
                occupied_seats += 1
                break
            elif occupancy == "Free":
                break
            else:
                value += 1
    except IndexError:
        pass

    try:
        value = 1
        while True:
            occupancy = get_tile_type(index_i - value, index_j, tile_arrangement)
            if occupancy == "Occupied":
                occupied_seats += 1
                break
            elif occupancy == "Free":
                break
            else:
                value += 1
    except IndexError:
        pass

    try:
        value = 1
        while True:
            occupancy = get_tile_type(index_i, index_j + value, tile_arrangement)
            if occupancy == "Occupied":
                occupied_seats += 1
                break
            elif occupancy == "Free":
                break
            else:
                value += 1
    except IndexError:
        pass

    try:
        value = 1
        while True:
            occupancy = get_tile_type(index_i, index_j - value, tile_arrangement)
            if occupancy == "Occupied":
                occupied_seats += 1
                break
            elif occupancy == "Free":
                break
            else:
                value += 1
    except IndexError:
        pass

    # Diagonals (Right-Down, Left-Down, Right-Up, Left-Up)
    try:
        value = 1
        while True:
            occupancy = get_tile_type(index_i + value, index_j + value, tile_arrangement)
            if occupancy == "Occupied":
                occupied_seats += 1
                break
            elif occupancy == "Free":
                break
            else:
                value += 1
    except IndexError:
        pass

    try:
        value = 1
        while True:
            occupancy = get_tile_type(index_i - value, index_j + value, tile_arrangement)
            if occupancy == "Occupied":
                occupied_seats += 1
                break
            elif occupancy == "Free":
                break
            else:
                value += 1
    except IndexError:
        pass

    try:
        value = 1
        while True:
            occupancy = get_tile_type(index_i + value, index_j - value, tile_arrangement)
            if occupancy == "Occupied":
                occupied_seats += 1
                break
            elif occupancy == "Free":
                break
            else:
                value += 1
    except IndexError:
        pass

    try:
        value = 1
        while True:
            occupancy = get_tile_type(index_i - value, index_j - value, tile_arrangement)
            if occupancy == "Occupied":
                occupied_seats += 1
                break
            elif occupancy == "Free":
                break
            else:
                value += 1
    except IndexError:
        pass

    return occupied_seats


def print_arrangement(tile_arrangement):
    """
    Prints the tile arrangement as a string.

    Args:
       tile_arrangement (List[List[str]])

    Returns:
       str:
           String representation of the tiles.
    """

    arr = []
    for tile_row in tile_arrangement:
        arr.append("".join(tile_row))

    return "\n".join(arr)


# COMPUTATION
# Run the simulation
previousArrangement = deepcopy(tileArrangement)
iteration = 1

while True:
    print(f"=== Iteration {iteration} ===")
    for i in range(len(previousArrangement)):
        for j in range(len(previousArrangement[0])):
            tile_type = get_tile_type(i, j, previousArrangement)
            adjacent_filled_seats = no_occupied_visible_seats(i, j, previousArrangement)

            if tile_type == "Free" and adjacent_filled_seats == 0:
                tileArrangement[i][j] = "#"
            elif tile_type == "Occupied" and adjacent_filled_seats >= 5:
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

# OUTPUT
print(noFilled)
