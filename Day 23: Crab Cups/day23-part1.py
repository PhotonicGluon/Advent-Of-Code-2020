"""
day23-part1.py

Created on 2020-12-23
Updated on 2020-12-23

Copyright © Ryan Kan
"""

# INPUT
with open("input.txt", "r") as f:
    cups = [int(x) for x in list(f.read().strip())]
    f.close()

# COMPUTATION
# Run 100 moves
currentCupIndex = 0
currentCup = cups[currentCupIndex]
for move in range(1, 101):
    print(f"-- Move {move} --")
    print("Cups:", " ".join([f"({currentCup})" if i == currentCupIndex else f" {cups[i]} " for i in range(9)]))

    # Pick up the three cups that are immediately clockwise to the current cup
    removedCups = [cups[(currentCupIndex + 1) % 9], cups[(currentCupIndex + 2) % 9], cups[(currentCupIndex + 3) % 9]]
    print("Pick up:", ", ".join([str(x) for x in removedCups]))

    # Remove the picked-up cups from the circle
    for cup in removedCups:
        cups.remove(cup)
    print(cups)

    # Find the destination cup
    destinationCup = currentCup - 1
    while destinationCup in removedCups or destinationCup == 0:
        if destinationCup <= 1:
            destinationCup = 9
        else:
            destinationCup -= 1

    print("Destination:", destinationCup)

    # Place the removed cup immediately clockwise of the destination cup
    destinationCupIndex = cups.index(destinationCup)
    for cup in reversed(removedCups):
        cups.insert((destinationCupIndex + 1) % 9, cup)

    # Find the new current cup
    currentCupIndex = (cups.index(currentCup) + 1) % 9
    currentCup = cups[currentCupIndex]
    print()

# Get the index of the cup labeled "1"
cupLabeled1Index = cups.index(1)

# OUTPUT
# Print the cups in the clockwise order, starting after the cup labeled "1"
for i in range(cupLabeled1Index + 1, cupLabeled1Index + 9):
    print(cups[i % 9], end="")
