"""
day4-part1.py

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
    if set(dictionary.keys()) == {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}:
        noValid += 1

# OUTPUT
print(noValid)
