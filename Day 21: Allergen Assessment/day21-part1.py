"""
day21-part1.py

Created on 2020-12-21
Updated on 2020-12-21

Copyright © Ryan Kan
"""

# INPUT
with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

    # Process each line and format it into a dictionary
    allFoods = []
    for line in lines:
        parts = line.split(" ")

        for i, part in enumerate(parts):
            if part[0] == "(":
                ingredients = set(parts[:i])
                allergens = set(" ".join(parts[i + 1:])[:-1].split(", "))
                break

        allFoods.append((ingredients, allergens))

    f.close()

# COMPUTATION
# Get all the allergens and all the ingredients
allAllergens = set()
allIngredients = set()

for ingredientSet, allergenSet in allFoods:
    allAllergens = allAllergens.union(allergenSet)
    allIngredients = allIngredients.union(ingredientSet)

# Get the possible ingredients for each allergen
allergenMap = {}

for allergen in allAllergens:
    possibleIngredients = set()

    for ingredientSet, allergenSet in allFoods:
        if allergen in allergenSet:
            possibleIngredients = possibleIngredients.intersection(ingredientSet) if len(
                possibleIngredients) != 0 else ingredientSet

    allergenMap[allergen] = possibleIngredients

# Get all ingredients that cannot contain any allergen
safeIngredients = allIngredients.copy()

for _, possibleIngredients in allergenMap.items():
    safeIngredients = safeIngredients.difference(possibleIngredients)

# Count the number of appearance of the safe ingredients
safeIngredientCount = 0
for ingredientSet, _ in allFoods:
    safeIngredientCount += len(safeIngredients.intersection(ingredientSet))

# OUTPUT
print(safeIngredientCount)
