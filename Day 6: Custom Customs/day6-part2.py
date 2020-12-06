"""
day6-part2.py

Created on 2020-12-06
Updated on 2020-12-06

Copyright © Ryan Kan
"""

# INPUT
with open("input.txt", "r") as f:
    contents = f.read()[:-1]
    groups = [form.replace("\n", " ") for form in contents.split("\n\n")]
    f.close()

# COMPUTATION
totalSum = 0  # Total sum of questions which EVERYONE answered 'yes' to
for group in groups:
    yesQuestionSet = set("abcdefghijklmnopqrstuvwxyz")
    for person in group.split(" "):
        # Only keep the questions which EVERYONE answered 'yes' to <==> Set intersections
        yesQuestionSet = yesQuestionSet.intersection(set(person))

    totalSum += len(list(yesQuestionSet))

# OUTPUT
print(totalSum)
