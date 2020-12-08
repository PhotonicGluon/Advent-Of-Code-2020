"""
day8-part1.py

Created on 2020-12-08
Updated on 2020-12-08

Copyright © Ryan Kan
"""

# INPUT
with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]
    instructions = [line.split(" ") for line in lines]
    f.close()

# COMPUTATION
runLines = []  # Stores the lines that were already run once
accumulator = 0
lineNo = 0

while True:
    # Get the current instruction and append its line number to the `runLines` array
    instruction = instructions[lineNo]
    runLines.append(lineNo)

    # Execute the instruction
    if instruction[0] == "nop":
        # Does nothing; move onto the next line
        lineNo += 1
    elif instruction[0] == "acc":
        # Increments/Decrements the value of `accumulator` and then moves onto the next line
        accumulator += int(instruction[1])
        lineNo += 1
    else:  # This would be a "jmp" instruction
        # "Jumps" to a new instruction relative to itself
        lineNo += int(instruction[1])

    # Try to see if the next line to be run has already been run
    if lineNo in runLines:
        # Since it already has, it will create an infinite loop, so output the accumulator value
        print(accumulator)
        break
