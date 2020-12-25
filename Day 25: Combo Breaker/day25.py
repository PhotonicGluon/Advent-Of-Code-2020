"""
day25.py

Created on 2020-12-25
Updated on 2020-12-25

Copyright © Ryan Kan
"""

# INPUT
with open("input.txt", "r") as f:
    cardPublicKey = int(f.readline().strip())
    doorPublicKey = int(f.readline().strip())
    f.close()


# FUNCTIONS
memo = {}


def transform_subject_number(subject_number, loop_size):
    """
    Args:
        subject_number (int)
        loop_size (int)

    Returns:
        int:
            The resulting subject number.
    """

    return pow(subject_number, loop_size, 20201227)


# COMPUTATIONS
# Find the card's loop size
cardLoopSize = 1
while True:
    print("Trying card loop size of", cardLoopSize)
    resultingNumber = transform_subject_number(7, cardLoopSize)

    if resultingNumber == cardPublicKey:
        break
    else:
        cardLoopSize += 1

print()
print("Card loop size is", cardLoopSize)
print()

# Find the door's loop size
doorLoopSize = 1
while True:
    print("Trying door loop size of", doorLoopSize)
    resultingNumber = transform_subject_number(7, doorLoopSize)

    if resultingNumber == doorPublicKey:
        break
    else:
        doorLoopSize += 1

print()
print("Door loop size is", doorLoopSize)
print()

# Determine the encryption key
encryptionKey = transform_subject_number(doorPublicKey, cardLoopSize)

# OUTPUT
print(encryptionKey)
