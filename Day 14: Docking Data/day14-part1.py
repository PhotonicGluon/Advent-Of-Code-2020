"""
day14-part1.py

Created on 2020-12-14
Updated on 2020-12-14

Copyright © Ryan Kan
"""

# INPUT
with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

    processes = []
    for line in lines:
        if line.split(" ")[0] == "mask":
            processes.append(("MASK", line.split(" ")[2]))
        else:
            processes.append(("MEMO", line.split(" ")[0][4:-1], f"{int(line.split(' ')[2]):036b}"))
    f.close()

# COMPUTATION
mask = processes[0][1]
memory = {}
for process in processes:
    if process[0] == "MASK":
        mask = process[1]
    else:
        # Apply mask
        finalInteger = list(process[2])
        for i, bit in enumerate(mask):
            if bit != "X":
                finalInteger[i] = bit

        # Save to memory
        memory[process[1]] = "".join(finalInteger)

# OUTPUT
# Get the sum of all the values in memory
print(sum([int(x, 2) for x in memory.values()]))
