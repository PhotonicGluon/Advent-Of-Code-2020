"""
day5-part1.py

Created on 2020-12-05
Updated on 2020-12-05

Copyright © Ryan Kan
"""

# INPUT
with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]
    f.close()

# COMPUTATION
maxSeatID = 0
for line in lines:
    # Based on the rules given, 'F' and 'L' will mean a '0' and 'B' and 'R' will mean a 1
    row = int(line[:7].replace("F", "0").replace("B", "1"), 2)
    col = int(line[7:].replace("L", "0").replace("R", "1"), 2)

    # Calculate seat id and compare it with the maximum
    seatID = row * 8 + col
    maxSeatID = max(maxSeatID, seatID)

# OUTPUT
print(maxSeatID)
