"""
day15-part2.py

Created on 2020-12-15
Updated on 2020-12-20

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
    print(number)
    saidNumbers[number] = (i + 1, 0)  # Turn no., never spoken before so there is no previous turn

# Process the rest of the numbers, all the way until turn 2020
turnNo = len(numbers) + 1
mostRecentNumber = numbers[-1]
while turnNo != 30000001:
    if mostRecentNumber in saidNumbers and saidNumbers[mostRecentNumber][1] != 0:
        mostRecentNumber = saidNumbers[mostRecentNumber][0] - saidNumbers[mostRecentNumber][1]
    else:
        mostRecentNumber = 0

    print(f"Turn {turnNo}:", mostRecentNumber)
    if mostRecentNumber in saidNumbers:
        saidNumbers[mostRecentNumber] = (turnNo, saidNumbers[mostRecentNumber][0])
    else:
        saidNumbers[mostRecentNumber] = (turnNo, 0)
    turnNo += 1

# OUTPUT
print(mostRecentNumber)
