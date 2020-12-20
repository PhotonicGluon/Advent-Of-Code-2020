"""
day19-part2.py

Created on 2020-12-19
Updated on 2020-12-20

Copyright © Ryan Kan
"""

# IMPORTS
import re

# INPUT
with open("input-part2.txt", "r") as f:
    sections = f.read().split("\n\n")
    f.close()

# Process rules
lines = [line.strip() for line in sections[0].split("\n")]
rules = {}
for line in lines:
    splitLine = line.split(": ")
    rules[splitLine[0]] = splitLine[1]

# Process messages
messages = [line.strip() for line in sections[1].split("\n")[:-1]]


# FUNCTIONS
def generate_regex(rule_no):
    """
    Args:
        rule_no (str)

    Returns:
        str:
            The final RegEx expression.
    """

    # Process the 'special two rules' -- rule 8 and rule 11
    if rule_no == "8":
        return generate_regex("42") + "+"  # Continue matching the regex for rule 42
    elif rule_no == "11":
        regex_for_31 = generate_regex("31")
        regex_for_42 = generate_regex("42")

        # We want to continue getting `n` more of the preceding regex
        final_regex = f"(?:{'|'.join([f'{regex_for_42}{{{n}}}{regex_for_31}{{{n}}}' for n in range(1, 5)])})"

        return final_regex
    # Get the rule that corresponds with the rule number
    rule = rules[rule_no]

    # If the rule matches the RegEx for a SINGLE character, just return the character
    if re.fullmatch(r'"."', rule):
        return rule[1]  # The second character of the rule will the SINGLE character
    else:
        # Split the rule into parts
        rule_parts = rule.split(" | ")

        # Process each part and generate their RegExes
        resulting_regexes = []

        for part in rule_parts:
            rule_numbers = part.split(" ")
            resulting_regexes.append("".join([generate_regex(rule_number) for rule_number in rule_numbers]))

        # Form the final RegEx
        return f"(?:{'|'.join(resulting_regexes)})"


# COMPUTATION
# Form the RegEx for rule number 0
ruleZeroRegEx = generate_regex("0")

# Check all the given messages to see if they fully match the RegEx pattern
matchRuleZero = 0
for message in messages:
    if re.fullmatch(ruleZeroRegEx, message):
        matchRuleZero += 1

# OUTPUT
print(matchRuleZero)
