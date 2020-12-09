"""
day1-part2.py

Created on 2020-12-02
Updated on 2020-12-09

Copyright © Ryan Kan
"""

# INPUT
with open("input.txt", "r") as f:
    numbers = [int(line.strip()) for line in f.readlines()]
    f.close()

noNumbers = len(numbers)

# COMPUTATION
# Use three nested for loops because it's easier to implement than the 3Sum algorithm
for i in range(noNumbers):
    for j in range(1, noNumbers):
        for k in range(2, noNumbers):
            if numbers[i] + numbers[j] + numbers[k] == 2020:
                print(numbers[i] * numbers[j] * numbers[k])
                exit()
