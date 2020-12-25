"""
day9-part1.py

Created on 2020-12-09
Updated on 2020-12-09

Copyright © Ryan Kan
"""

# INPUT
with open("input.txt", "r") as f:
    numbers = [int(line.strip()) for line in f.readlines()]
    f.close()

# COMPUTATION
preamble = numbers[:25]  # The preamble is the first 25 numbers
restOfNumbers = numbers[25:]

for number in restOfNumbers:
    found = False

    # Check if the `number` can be formed as the sum of two numbers in the `preamble`
    for i in range(25):
        for j in range(i, 25):
            if preamble[i] + preamble[j] == number:
                # The number can be made from two numbers from the `preamble`
                found = True
                break

        if found:
            break

    # If the number CANNOT be made from two numbers from the `preamble` then output it
    if not found:
        print(number)
        exit()  # We don't care about any other numbers
    else:
        # Shift the preamble window along
        preamble.pop(0)  # Remove first element
        preamble.append(number)  # Append this new number to the preamble
