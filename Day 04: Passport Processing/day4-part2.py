"""
day4-part2.py

Created on 2020-12-04
Updated on 2020-12-09

Copyright © Ryan Kan
"""

# INPUT
with open("input.txt", "r") as f:
    contents = f.read()[:-1]
    passports = [passport.replace("\n", " ") for passport in contents.split("\n\n")]
    f.close()

# COMPUTATION
# Process each passport
noValid = 0
for passport in passports:
    # Convert each passport into a dictionary of sorts
    dictionary = {}
    entries = passport.split(" ")

    for entry in entries:
        key, value = entry.split(":")
        dictionary[key] = value

    # Remove the "cid" key since it is optional
    try:
        dictionary.pop("cid")
    except KeyError:
        pass

    # Check if all required fields are there
    if set(dictionary.keys()) != {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}:
        continue  # Skip this passport because it is most definitely invalid

    # Check birth year
    try:
        dictionary["byr"] = int(dictionary["byr"])
    except ValueError:
        continue

    if not (1920 <= dictionary["byr"] <= 2002):
        continue

    # Check issue year
    try:
        dictionary["iyr"] = int(dictionary["iyr"])
    except ValueError:
        continue

    if not (2010 <= dictionary["iyr"] <= 2020):
        continue

    # Check expiration year
    try:
        dictionary["eyr"] = int(dictionary["eyr"])
    except ValueError:
        continue

    if not (2020 <= dictionary["eyr"] <= 2030):
        continue

    # Check height
    try:
        height = int(dictionary["hgt"][:-2])
    except ValueError:
        continue

    heightValid = False
    if dictionary["hgt"][-2:] == "cm" and 150 <= height <= 193:
        heightValid = True

    if dictionary["hgt"][-2:] == "in" and 59 <= height <= 76:
        heightValid = True

    if not heightValid:
        continue

    # Check hair colour
    if dictionary["hcl"][0] != "#":
        continue

    if len(dictionary["hcl"]) != 7:
        continue

    try:
        hairColour = int(dictionary["hcl"][1:], 16)
    except ValueError:
        continue

    # Check eye colour
    if dictionary["ecl"] not in "amb blu brn gry grn hzl oth".split(" "):
        continue

    # Check passport id
    if len(dictionary["pid"]) != 9:
        continue

    try:
        int(dictionary["pid"])
    except ValueError:
        continue

    # If everything above is okay then it means that this passport is valid
    noValid += 1

# OUTPUT
print(noValid)
