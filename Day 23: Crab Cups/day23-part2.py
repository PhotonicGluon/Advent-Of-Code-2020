"""
day23-part2.py

Created on 2020-12-23
Updated on 2020-12-23

Adapted from https://github.com/tylanmm/comp_prog/blob/master/advent_of_code/2020/day23/part2.py.
"""

# IMPORTS
from tqdm import trange

# INPUT
with open("input.txt", "r") as f:
    firstFewCupsLabels = [int(x) for x in list(f.read().strip())]
    f.close()


# CLASSES
class Cup:
    def __init__(self, label):
        """
        Args:
            label (int):
                The cup's label
        """

        self.label = label
        self.next_cup = None


# FUNCTIONS
def move(current_cup):
    """
    Performs a move.

    Args:
        current_cup (Cup)
    """

    # Pick up the three cups that are immediately clockwise to the current cup
    removed_cups = [current_cup.next_cup, current_cup.next_cup.next_cup, current_cup.next_cup.next_cup.next_cup]
    removed_cups_labels = {_cup.label for _cup in removed_cups}

    # 'Fix' the circle
    current_cup.next_cup = current_cup.next_cup.next_cup.next_cup.next_cup

    # Find the destination cup
    destination_cup = current_cup.label - 1 + (10 ** 6 if current_cup.label == 1 else 0)
    while destination_cup in removed_cups_labels:
        destination_cup -= 1
        if destination_cup == 0:
            destination_cup = 10 ** 6

    # Insert those three cups immediately clockwise of the destination cup
    removed_cups[-1].next_cup = cups[destination_cup].next_cup
    cups[destination_cup].next_cup = removed_cups[0]


# COMPUTATION
# Create all the `Cup` objects
cups = [Cup(i) for i in range(10 ** 6 + 1)]

# Set up the first 9 cups' connections
for i in range(len(firstFewCupsLabels) - 1):
    cups[firstFewCupsLabels[i]].next_cup = cups[firstFewCupsLabels[i + 1]]
cups[firstFewCupsLabels[-1]].next_cup = cups[len(firstFewCupsLabels) + 1]

# Connect the rest of the cups
for i in trange(len(firstFewCupsLabels) + 1, 10 ** 6, desc="Setting up other cups' connections"):
    cups[i].next_cup = cups[i + 1]
cups[-1].next_cup = cups[firstFewCupsLabels[0]]

# Run the simulation for 10,000,000 moves
currentCup = cups[firstFewCupsLabels[0]]
for _ in trange(10 ** 7, desc="Simulating 10,000,000 moves"):
    move(currentCup)
    currentCup = currentCup.next_cup

# OUTPUT
print(cups[1].next_cup.label * cups[1].next_cup.next_cup.label)
