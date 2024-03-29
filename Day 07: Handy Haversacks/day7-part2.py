"""
day7-part2.py

Created on 2020-12-07
Updated on 2020-12-20

Copyright © Ryan Kan
"""

# INPUT
rules = {}
with open("input.txt", "r") as f:
    lines = [line.strip()[:-1] for line in f.readlines()]
    rawRules = [[[y.split(" ")[:-1] for y in x.split(", ")] for x in line.split(" contain ")] for line in lines]

    for rule in rawRules:
        if " ".join(rule[1][0]) == "no other":
            # This bag contains nothing else, so just leave its contents as an empty list
            bagContents = []
        else:
            # Put the quantity and the bag type into a tuple that is in a list
            bagContents = [(int(x[0]), " ".join(x[1:])) for x in rule[1]]

        # Update what each bag type should contain
        rules[" ".join(rule[0][0])] = bagContents

    f.close()

# COMPUTATION
queue = [(1, "shiny gold")]  # This is what we have: 1 shiny gold bag
noBagsNeeded = 0

while len(queue) != 0:
    bag = queue[0]  # Get the first item in the queue and call it our `bag`
    inCurrentBag = rules[bag[1]]  # These are the bags that must be inside the current `bag`

    for requiredBag in inCurrentBag:
        queue.append((bag[0] * requiredBag[0], requiredBag[1]))  # We append the number of the needed bags to the queue

    noBagsInCurrentBag = sum([bag[0] for bag in inCurrentBag])  # This is the number of bags in the `bag`
    noBagsNeeded += bag[0] * noBagsInCurrentBag

    queue.pop(0)  # Remove the first item in the queue since we just processed it

# OUTPUT
print(noBagsNeeded)
