"""
day15-part1.py

Created on 2020-12-15
Updated on 2020-12-15

Copyright © Ryan Kan
"""

# INPUT
with open("input.txt", "r") as f:
    numbers = [int(number) for number in f.readline().split(",")]
    f.close()

# COMPUTATION
saidNumbers = {}

# Process the first numbers
for i, number in enumerate(numbers):
    # print(number)
    saidNumbers[number] = (i + 1, 0)  # Turn no., never spoken before so there is no previous turn

turnNo = len(numbers) + 1
mostRecentNumber = numbers[-1]
while turnNo != 2021:
    if mostRecentNumber in saidNumbers and saidNumbers[mostRecentNumber][1] != 0:
        mostRecentNumber = saidNumbers[mostRecentNumber][0] - saidNumbers[mostRecentNumber][1]
    else:
        mostRecentNumber = 0

    # print(mostRecentNumber)
    if mostRecentNumber in saidNumbers:
        saidNumbers[mostRecentNumber] = (turnNo, saidNumbers[mostRecentNumber][0])
    else:
        saidNumbers[mostRecentNumber] = (turnNo, 0)
    turnNo += 1

# OUTPUT
print(mostRecentNumber)
