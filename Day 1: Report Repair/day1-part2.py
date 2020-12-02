"""
day1-part2.py

Created on 2020-12-02
Updated on 2020-12-02

Copyright © Ryan Kan
"""

# INPUT
with open("input.txt", "r") as f:
    numbers = [int(line.strip()) for line in f.readlines()]
    f.close()

noNumbers = len(numbers)

# COMPUTATION: Use the 3Sum algorithm
# Edit: I'm lazy so use three nested for loops
for i in range(noNumbers):
    for j in range(1, noNumbers):
        for k in range(2, noNumbers):
            if numbers[i] + numbers[j] + numbers[k] == 2020:
                print(numbers[i] * numbers[j] * numbers[k])
                exit()
