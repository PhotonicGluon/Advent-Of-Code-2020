"""
day1-part1.py

Created on 2020-12-02
Updated on 2020-12-09

Copyright © Ryan Kan
"""

# INPUT
with open("input.txt", "r") as f:
    numbers = [int(line.strip()) for line in f.readlines()]
    f.close()

# COMPUTATION: Use the 2Sum algorithm
# Let array A be `numbers` in ascending order and array B be `numbers` in descending order
A = sorted(numbers)
B = sorted(numbers)[::-1]

# Define indices `i` and `j`
i = 0
j = 1  # Note that i != j

# Loop until exhausted all possibilities
while i != len(A) - 1 and j != len(B) - 1:
    # If A[i] + B[j] - 2020 is positive then increment `j` by 1
    if A[i] + B[j] - 2020 > 0:
        j += 1

    # If A[i] + B[j] - 2020 is negative then increment `i` by 1
    elif A[i] + B[j] - 2020 < 0:
        i += 1

    # Else break as we found `i` and `j`
    else:
        break

# OUTPUT: Return `A[i] * B[j]`
print(A[i] * B[j])
