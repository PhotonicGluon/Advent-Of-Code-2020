"""
day7-part1.py

Created on 2020-12-07
Updated on 2020-12-07

Copyright © Ryan Kan
"""

# INPUT
rules = {}
with open("input.txt", "r") as f:
    lines = [line.strip()[:-1] for line in f.readlines()]
    rawRules = [[[y.split(" ")[:-1] for y in x.split(", ")] for x in line.split(" contain ")] for line in lines]

    for rule in rawRules:
        if " ".join(rule[1][0]) == "no other":
            value = []
        else:
            value = [(int(x[0]), " ".join(x[1:])) for x in rule[1]]

        rules[" ".join(rule[0][0])] = value
    f.close()

# COMPUTATION
queue = ["shiny gold"]  # We have a shiny gold bag
canHoldGoldBag = set()

while len(queue) != 0:
    bag = queue[0]

    # Search through the rules to find bags that can contain the current `bag`
    for containerBag in rules:
        possibleBags = rules[containerBag]  # These are the bags that are contained within the `containerBag`
        for possibleBag in possibleBags:
            if possibleBag[1] == bag:  # This possible bag is the desired `bag`
                canHoldGoldBag = canHoldGoldBag.union({containerBag})  # Only keep unique elements
                queue.append(containerBag)  # Now we need to process which bags can contain the `containerBag`

    queue.pop(0)  # Remove the first item in the queue since we just processed it

# OUTPUT
print(len(canHoldGoldBag))
