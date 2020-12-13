"""
day13-part1.py

Created on 2020-12-13
Updated on 2020-12-13

Copyright © Ryan Kan
"""

# INPUT
with open("input.txt", "r") as f:
    timestamp = int(f.readline().strip())
    busServices = set([x.strip() for x in f.readline().split(",")])

    try:
        busServices.remove("x")  # Remove non-functioning bus services
    except ValueError:
        pass

    busServices = [int(x) for x in list(busServices)]
    f.close()

# COMPUTATION
currTimestamp = timestamp
while True:
    for busService in busServices:
        if currTimestamp % busService == 0:  # Bus is there at that timestamp
            difference = currTimestamp - timestamp
            print(busService * difference)
            exit()

    currTimestamp += 1
