"""
day5-part2.py

Created on 2020-12-05
Updated on 2020-12-05

Copyright © Ryan Kan
"""

# INPUT
with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]
    f.close()

# COMPUTATION & OUTPUT
seatIDs = []
for line in lines:
    # Based on the rules given, 'F' and 'L' will mean a '0' and 'B' and 'R' will mean a 1
    row = int(line[:7].replace("F", "0").replace("B", "1"), 2)
    col = int(line[7:].replace("L", "0").replace("R", "1"), 2)

    # Calculate seat id and append it to the `seatIDs` list
    seatID = row * 8 + col
    seatIDs.append(seatID)

# Search for missing seat IDs
for row in range(1, 127 + 1):
    for col in range(0, 7 + 1):
        if row * 8 + col not in seatIDs:
            # Compute the seat ID
            seatID = row * 8 + col

            # Check if `seatID + 1` and `seatID - 1` exists, because if they do we found the seat ID
            if (seatID - 1 in seatIDs) and (seatID + 1 in seatIDs):
                # We found the seat!
                print(seatID)
                exit()
