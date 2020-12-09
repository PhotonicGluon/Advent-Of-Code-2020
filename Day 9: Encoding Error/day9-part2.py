"""
day9-part2.py

Created on 2020-12-09
Updated on 2020-12-09

Copyright © Ryan Kan
"""

# INPUT
with open("input.txt", "r") as f:
    numbers = [int(line.strip()) for line in f.readlines()]
    f.close()


# FUNCTIONS
def subarray_sum(arr, no_elements, target_no):
    # Initialize `curr_sum` as value of first element and starting point as 0
    curr_sum = arr[0]
    start_index = 0

    # Add elements one by one to `curr_sum` and if the `curr_sum` exceeds the sum, then remove the starting element
    i = 1
    while i <= no_elements:
        # If `curr_sum` exceeds the sum, then remove the starting elements
        while curr_sum > target_no and start_index < i - 1:
            curr_sum = curr_sum - arr[start_index]
            start_index += 1

        # If `curr_sum` becomes equal to sum, then return the start and ending indices
        if curr_sum == target_no:
            return start_index, i

        # Add this element to `curr_sum`
        if i < no_elements:
            curr_sum = curr_sum + arr[i]
        i += 1

    # If we reach here, then there exists no such subarray, so return negative indices
    return -1, -1


# COMPUTATION & OUTPUT
target = 1309761972  # This was the result from part 1
n = 2  # We can safely assume that no single element will sum to our target number

while n < len(numbers) - 1:
    print(f"=== Trying a subarray with {n:03d} elements ===")
    start, end = subarray_sum(numbers, n, target)  # Use the algorithm above to try and find valid indices

    if (start, end) != (-1, -1):  # We found the subarray!
        subarray = numbers[start:end]
        weakness = max(subarray) + min(subarray)
        print(weakness)
        exit()

    # If not found then increment `n`
    n += 1
