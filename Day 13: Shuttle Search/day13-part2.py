"""
day13-part2.py

Created on 2020-12-13
Updated on 2020-12-13

Copyright © Ryan Kan
"""

# INPUT
with open("input.txt", "r") as f:
    _ = int(f.readline().strip())  # We don't care about this anymore
    busServices = [x.strip() for x in f.readline().split(",")]
    f.close()

# COMPUTATION
# Suppose a bus with ID of `B` appears at index `i`.
# Then for our 'goal timestamp' `T` we must have `T + i == 0 (mod B)`.
# This means that `T == -i == B - i (mod B)`.
#
# We shall use the Chinese Remainder Theorem (CRT):
#    If the n_i are pairwise coprime, and if a_1, ..., a_k are integers such that 0 ≤ ai < ni for every i, then there is
#    one and only one integer x, such that 0 ≤ x < N and the remainder of the Euclidean division of x by ni is ai for
#    every i.
# Using https://exploringnumbertheory.wordpress.com/2015/11/15/how-to-chinese-remainder-part-1/, we are able to find the
# timestamp `T` easily.

# Create the list of `c_i`, `C`, and calculate m = m_1 * m_2 * ... * m_t
C = []
m = 1
for i, bus in enumerate(busServices):
    if bus == "x":
        continue
    else:
        C.append(int(bus) - i)
        m *= int(bus)

# Fix the list of bus services
temp = []
for bus in busServices:
    if bus != "x":
        temp.append(bus)

busServices = temp.copy()

# For each index `i`, compute `n_i` and place it into the array `N`.
N = []
for i in range(len(busServices)):
    N.append(m // int(busServices[i]))

# Each n_i in N is relatively prime to every bus `B`. Thus n_i has a multiplicative inverse modulo m_i, w_i. So let's
# find it.
W = []
for i in range(len(busServices)):
     W.append(pow(N[i], -1, int(busServices[i])))  # Fix index `i`

# The solution is given by
#   x == c_1 * n_1 * w_1 + c_2 * n_2 * w_2 + ... + c_t * n_t * w_t  (mod m)
# where
m = 1
for i in range(len(busServices)):
    m *= int(busServices[i])

earliestTimestamp = 0
for i in range(len(C)):
    earliestTimestamp += C[i] * N[i] * W[i]

earliestTimestamp = earliestTimestamp % m

# OUTPUT
print(earliestTimestamp)
