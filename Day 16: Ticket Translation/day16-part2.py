"""
day16-part2.py

Created on 2020-12-16
Updated on 2020-12-20

Copyright © Ryan Kan
"""

# IMPORTS
from collections import defaultdict

# INPUT
with open("input-part2.txt", "r") as f:
    content = f.read()
    sections = content.split("\n\n")

    # The possible ticket fields
    ticketFields = {}
    for line in sections[0].split("\n"):
        components = line.split(": ")

        possibleValues = []
        temp = [list(range(int(x.split("-")[0]), int(x.split("-")[1]) + 1)) for x in components[1].split(" or ")]
        for value in temp:
            [possibleValues.append(x) for x in value]

        ticketFields[components[0]] = possibleValues

    # Your ticket
    yourTicket = [int(x) for x in sections[1].split("\n")[1].split(",")]

    # Nearby (but valid) tickets
    tickets = []
    for line in sections[2].split("\n")[1:-1]:
        tickets.append([int(x) for x in line.split(",")])

    f.close()

# COMPUTATION
# Determine which fields are possible for each index
possibleFieldLocations = defaultdict(set)  # Make the default index be an empty set
for index in range(len(ticketFields)):
    for field, scope in ticketFields.items():
        if all(ticket[index] in scope for ticket in tickets):
            possibleFieldLocations[field].add(index)

# Determine the correct fields
fieldLocations = dict()
for field in sorted(possibleFieldLocations, key=lambda _field: len(possibleFieldLocations[_field])):
    for index in possibleFieldLocations[field]:  # For each possible index that the field can be in
        if index not in fieldLocations.values():  # If that index has not yet been chosen
            fieldLocations[field] = index

# Determine which indices contain field
departureLocations = []
for field in fieldLocations:
    if field.count("departure") > 0:  # The field contains the word "departure"
        departureLocations.append(fieldLocations[field])

# Get the values on your ticket that have departure and multiply them together
answer = 1
for departureLocation in departureLocations:
    answer *= yourTicket[departureLocation]

# OUTPUT
print(answer)
