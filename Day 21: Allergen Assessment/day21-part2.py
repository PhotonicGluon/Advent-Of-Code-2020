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


# FUNCTIONS
def get_correct_ingredient_allergen_mapping(allergen_map, processed_allergens_dict=None):
    """
    A recursive function that helps find the correct allergen mapping.

    Args:
        allergen_map (dict[str, set[str]])
        processed_allergens_dict (dict[str, str])

    Returns:
        dict[str, str]:
            The correct allergen mapping.
    """

    if processed_allergens_dict is None:
        processed_allergens_dict = {}

    # Termination conditions
    length_of_processed_allergens_dict = len(processed_allergens_dict)

    if length_of_processed_allergens_dict == len(allergen_map):  # We processed all the allergens
        return processed_allergens_dict

    # Get the next unprocessed allergen
    current_allergen = list(allergen_map.keys())[length_of_processed_allergens_dict]
    current_ingredient_set = allergenMap[current_allergen]

    for ingredient in current_ingredient_set:
        if ingredient not in processed_allergens_dict.values():  # Ingredient hasn't been processed
            # Make a copy of the processed allergens and map the `current_allergen` to the `ingredient`
            processed_ingredients_dict_temp = processed_allergens_dict.copy()
            processed_ingredients_dict_temp[current_allergen] = ingredient

            # Solve for the rest of the processed allergens dictionary
            processed_ingredients_dict_temp = get_correct_ingredient_allergen_mapping(allergen_map,
                                                                                      processed_ingredients_dict_temp)

            # If something was returned then we found the correct list
            if processed_ingredients_dict_temp is not None:
                return processed_ingredients_dict_temp  # This is the resulting processed ingredients dictionary


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

# Find each ingredient's allergen
allergenMap = get_correct_ingredient_allergen_mapping(allergenMap)

# Sort the allergen map in alphabetical order according to the allergens
sortedIngredients = [entry[1] for entry in sorted(allergenMap.items(), key=lambda entry: entry[0])]

# OUTPUT
print(",".join(sortedIngredients))
