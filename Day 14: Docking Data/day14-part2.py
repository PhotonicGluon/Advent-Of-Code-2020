"""
day14-part2.py

Created on 2020-12-14
Updated on 2020-12-14

Copyright © Ryan Kan
"""

# IMPORTS
from itertools import product

# INPUT
with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

    processes = []
    for line in lines:
        if line.split(" ")[0] == "mask":
            processes.append(("MASK", line.split(" ")[2]))
        else:
            processes.append(("MEMO", f"{int(line.split(' ')[0][4:-1]):036b}", f"{int(line.split(' ')[2]):036b}"))
    f.close()

# COMPUTATION
mask = processes[0][1]
memory = {}
for process in processes:
    if process[0] == "MASK":
        mask = process[1]
    else:
        # Apply mask to address
        address = list(process[1])
        noXs = 0
        for i, bit in enumerate(mask):
            address[i] = bit if bit in ["1", "X"] else address[i]
            if bit == "X":
                noXs += 1

        address = "".join(address)

        possibleXValueList = product(["0", "1"], repeat=noXs)
        for possibleXValueSet in possibleXValueList:
            tempAddress = address
            for xValue in possibleXValueSet:
                tempAddress = (tempAddress[::-1].replace("X", xValue, 1))[::-1]
            memory[int(tempAddress, 2)] = process[2]

# OUTPUT
# Get the sum of all the values in memory
print(sum([int(x, 2) for x in memory.values()]))
