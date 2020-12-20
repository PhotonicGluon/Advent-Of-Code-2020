"""
day16-part1.py

Created on 2020-12-16
Updated on 2020-12-20

Copyright © Ryan Kan
"""

# INPUT
with open("input-part1.txt", "r") as f:
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

    # Nearby tickets
    nearbyTickets = []
    for line in sections[2].split("\n")[1:-1]:
        nearbyTickets.append([int(x) for x in line.split(",")])

    f.close()

# COMPUTATION
# Get ticket scanning error rate
ticketScanningErrorRate = 0
invalidTickets = []  # We'll need this for part 2
for nearbyTicket in nearbyTickets:
    for field in nearbyTicket:
        valid = False
        for possibleFieldValues in ticketFields.values():
            if field in possibleFieldValues:
                valid = True
                break

        if not valid:
            # Field is not valid; add to ticket scanning error rate
            invalidTickets.append(nearbyTicket)
            ticketScanningErrorRate += field

# Generate the input file for part 2
for invalidTicket in invalidTickets:
    invalidTicket = ",".join([str(x) for x in invalidTicket])
    content = content.replace(invalidTicket + "\n", "")  # Remove the ticket entirely

# OUTPUT
print("Part 1 Answer:", ticketScanningErrorRate)
print("-" * 50)
print("New input file for part 2:\n")
print(content)
