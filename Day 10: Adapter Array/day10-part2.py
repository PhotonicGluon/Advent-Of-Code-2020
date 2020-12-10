"""
day10-part2.py

Created on 2020-12-10
Updated on 2020-12-10

Copyright © Ryan Kan
"""

# INPUT
with open("input.txt", "r") as f:
    adaptors = [int(line.strip()) for line in f.readlines()]
    f.close()

# COMPUTATION
adaptors.append(0)  # This is the charging port
adaptors.append(max(adaptors) + 3)  # This is the device
adaptors = sorted(adaptors)  # Sort the list
memo = {}


def no_ways(index):
    """
    Returns the number of ways to complete the chain given that we are currently at adaptor index `index`.

    Args:
        index (int):
            The index of the adaptor.

    Returns:
        int:
            The number of ways to complete the chain.
    """

    # 1. Termination conditions
    if index == len(adaptors) - 1:  # The last index
        return 1

    # 2. Check if already processed
    if index in memo:
        return memo[index]

    # 3. Process ALL possible options
    no_possibilities = 0
    for i in range(index + 1, len(adaptors)):
        if adaptors[i] - adaptors[index] <= 3:  # Difference is at most 3
            no_possibilities += no_ways(i)  # Add the number of ways from index `i` to the number of possibilities here

    # 4. Save the result to memory
    memo[index] = no_possibilities

    # 5. Return the result
    return no_possibilities


# OUTPUT
print(no_ways(0))
