"""
day8-part2.py

Created on 2020-12-08
Updated on 2020-12-09

Copyright © Ryan Kan
"""

# IMPORTS
from copy import deepcopy  # We need this to properly copy a 2D list

# INPUT
with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]
    originalInstructions = [line.split(" ") for line in lines]  # The instructions themselves will be modified later
    f.close()

# COMPUTATION
# Loop through all lines to change one (and only one) line
for changedLine in range(len(lines)):
    instructions = deepcopy(originalInstructions)  # Make a through copy of the 2D instructions list

    # Modify the instruction on the `changedLine`
    if instructions[changedLine][0] == "acc":
        # No "acc" instructions were harmed ==> Don't change this line, just move on
        continue
    else:
        # Change the "jmp" to a "nop" and a "nop" to a "jmp"
        instructions[changedLine][0] = "jmp" if instructions[changedLine][0] == "nop" else "nop"

        # Run the boot code
        runLines = []  # Stores the lines that were already run once
        accumulator = 0
        lineNo = 0
        terminates = False  # Whether or not the boot code terminates

        while True:
            # Get the current instruction and append its line number to the `runLines` array
            instruction = instructions[lineNo]
            runLines.append(lineNo)

            # Execute the instruction
            if instruction[0] == "nop":
                # Does nothing; move on to the next line
                lineNo += 1
            elif instruction[0] == "acc":
                # Increments/Decrements the value of `accumulator` and then moves on to the next line
                accumulator += int(instruction[1])
                lineNo += 1
            else:  # This would be a "jmp" instruction
                # Goes to a new instruction relative to itself
                lineNo += int(instruction[1])

            # Try to see if the next line to be run has already been run
            if lineNo in runLines:
                # Since it already has, it will create an infinite loop, so this is not the line to be changed
                break

            # Check if the line number will be beyond the boot code's length
            if lineNo > len(lines) - 1:
                # Since it exceeds the boot code's length, it hence terminates
                terminates = True
                break

        # Check if boot code terminates
        if terminates:
            print(accumulator)
            break
