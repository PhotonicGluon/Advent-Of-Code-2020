"""
day18-part2.py

Created on 2020-12-18
Updated on 2020-12-18

Copyright © Ryan Kan
"""

# INPUT
with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]
    f.close()


# FUNCTIONS
def compute_answer(math_string):
    """
    Computes the answer of the math string using the new math rules

    Args:
        math_string (str)

    Returns:
        int:
            The answer.
    """

    parts = math_string.split(" ")

    if math_string.count("(") == 0:  # No parentheses, hooray!
        # Find and process all the addition operators first
        index = 0
        while parts.count("+") != 0:
            if parts[index] == "+":
                # Take the three adjacent parts and evaluate them
                new_part = str(eval(" ".join(parts[index - 1:index + 2])))

                # Remove the those three elements and replace them with the `new_part`
                del parts[index - 1:index + 2]
                parts.insert(index - 1, new_part)

                # Reset the index because we have to process it again
                index = 0
            else:
                index += 1

        # Next, find and process all the multiplication operators
        index = 0
        while parts.count("*") != 0:
            if parts[index] == "*":
                # Take the three adjacent parts and evaluate them
                new_part = str(eval(" ".join(parts[index - 1:index + 2])))

                # Remove the those three elements and replace them with the `new_part`
                del parts[index - 1:index + 2]
                parts.insert(index - 1, new_part)

                # Reset the index because we have to process it again
                index = 0
            else:
                index += 1

        # Once there is only one part remaining, just return it
        return int(parts[0])

    else:  # Oh no we have to do recursion
        # Find the EARLIEST opening parenthesis and the FIRST closing parenthesis that completes the expression inside
        # the parentheses
        earliest_opening_bracket = None
        closing_bracket_position = None
        no_opening_brackets = 0
        for i, char in enumerate(math_string):
            if char == "(":
                if earliest_opening_bracket is None:
                    earliest_opening_bracket = i
                no_opening_brackets += 1
            elif char == ")":
                no_opening_brackets -= 1

            if earliest_opening_bracket is not None and no_opening_brackets == 0:
                closing_bracket_position = i
                break

        # Process the string inside the parentheses
        string_inside = math_string[earliest_opening_bracket + 1: closing_bracket_position]
        bracket_answer = compute_answer(string_inside)

        # Replace the original string's parentheses with the new answer
        math_string = math_string.replace(f"({string_inside})", str(bracket_answer))

        # Get the new string's answer
        return compute_answer(math_string)


# COMPUTATION
answers = []
for line in lines:
    answers.append(compute_answer(line))

# OUTPUT
print(sum(answers))
