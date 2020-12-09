"""
day6-part1.py

Created on 2020-12-06
Updated on 2020-12-09

Copyright © Ryan Kan
"""

# INPUT
with open("input.txt", "r") as f:
    contents = f.read()[:-1]
    groups = [form.replace("\n", "") for form in contents.split("\n\n")]  # We can count each group as one person
    f.close()

# COMPUTATION
totalSum = 0  # Total sum of questions which ANYONE answered "yes" to
for group in groups:
    yesQuestions = set(group)  # Only keep unique elements
    totalSum += len(yesQuestions)

# OUTPUT
print(totalSum)
