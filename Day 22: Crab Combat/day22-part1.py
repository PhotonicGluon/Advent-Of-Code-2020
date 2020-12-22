"""
day22-part1.py

Created on 2020-12-22
Updated on 2020-12-22

Copyright © Ryan Kan
"""

# INPUT
with open("input.txt", "r") as f:
    content = f.read()[:-1]
    f.close()

# Split the content into player 1's cards and player 2's cards
sections = content.split("\n\n")

player1Cards = [int(x) for x in sections[0][10:].split("\n")]
player2Cards = [int(x) for x in sections[1][10:].split("\n")]

# COMPUTATION
# Simulate the game
roundNo = 1

while len(player1Cards) != 0 and len(player2Cards) != 0:
    print(f"-- Round {roundNo} --")
    print("Player 1's deck:", ", ".join([str(x) for x in player1Cards]))
    print("Player 2's deck:", ", ".join([str(x) for x in player2Cards]))

    # Draw both top cards from the players' hands
    player1Card = player1Cards[0]
    player2Card = player2Cards[0]

    print("Player 1 plays:", player1Card)
    print("Player 2 plays:", player2Card)

    # Remove the cards from the players' hands
    player1Cards.pop(0)
    player2Cards.pop(0)

    # See who wins the round
    if player1Card > player2Card:
        # Append `player1Card` and `player2Card` to the end of `player1Cards` in that order
        player1Cards = player1Cards[::-1]
        player1Cards.insert(0, player1Card)
        player1Cards.insert(0, player2Card)
        player1Cards = player1Cards[::-1]

        print("Player 1 wins the round!")
    else:
        # Append `player2Card` and `player1Card` to the end of `player2Cards` in that order
        player2Cards = player2Cards[::-1]
        player2Cards.insert(0, player2Card)
        player2Cards.insert(0, player1Card)
        player2Cards = player2Cards[::-1]

        print("Player 2 wins the round!")

    roundNo += 1
    print()

print("== Post-game Results ==")
print("Player 1's deck:", ", ".join([str(x) for x in player1Cards]))
print("Player 2's deck:", ", ".join([str(x) for x in player2Cards]))
print()

# Get the winning hand
if len(player1Cards) != 0:
    winningDeck = player1Cards
else:
    winningDeck = player2Cards

# Calculate the score
score = 0
for i, card in enumerate(winningDeck[::-1]):
    score += card * (i + 1)

# OUTPUT
print("Score:", score)
