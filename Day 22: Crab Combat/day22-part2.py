"""
day22-part2.py

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


# FUNCTIONS
def recursive_combat(player1_cards, player2_cards, game_no=1):
    """
    Args:
        player1_cards (list[int])
        player2_cards (list[int])
        game_no (int)

    Returns:
        int:
            The number of the player who won.
        list[int]:
            Player 1's ending cards.
        list[int]:
            Player 2's ending cards.
    """

    # These lists help keep track of all the previous decks of the players
    player1_previous_decks = []
    player2_previous_decks = []

    # Simulate the game
    round_no = 1
    while len(player1_cards) != 0 and len(player2_cards) != 0:
        print(f"-- Game {game_no}, Round {round_no} --")
        print("Player 1's deck:", ", ".join([str(x) for x in player1_cards]))
        print("Player 2's deck:", ", ".join([str(x) for x in player2_cards]))

        # Check if this configuration of cards matches any of the previous decks
        if player1_cards in player1_previous_decks or player2_cards in player2_previous_decks:
            # Then player 1 instantly wins the GAME
            print("Player 1 instantly wins the GAME!")
            return 1, player1_cards, player2_cards
        else:
            # Append this deck to the previous decks list
            player1_previous_decks.append(player1_cards.copy())
            player2_previous_decks.append(player2_cards.copy())

        # Draw both top cards from the players' hands
        player1_card = player1_cards[0]
        player2_card = player2_cards[0]

        print("Player 1 plays:", player1_card)
        print("Player 2 plays:", player2_card)

        # Remove the cards from the players' hands
        player1_cards.pop(0)
        player2_cards.pop(0)

        # Check if both players have at least as many cards remaining in their deck as the value of the card they just
        # drew
        if len(player1_cards) >= player1_card and len(player2_cards) >= player2_card:
            # Then we play a sub-game of recursive combat
            print("Playing a sub-game to determine the winner...")
            player_who_wins, _, _ = recursive_combat(player1_cards.copy()[:player1_card],
                                                     player2_cards.copy()[:player2_card], game_no=game_no+1)
            print(f"...anyway, back to game {game_no}.")

        else:  # At least one player must not have enough cards left in their deck to recurse
            player_who_wins = 1 if player1_card > player2_card else 2

        # See who wins the round
        if player_who_wins == 1:  # Player 1 wins
            # Append `player1_card` and `player2_card` to the end of `player1_cards` in that order
            player1_cards = player1_cards[::-1]
            player1_cards.insert(0, player1_card)
            player1_cards.insert(0, player2_card)
            player1_cards = player1_cards[::-1]

            print(f"Player 1 wins round {round_no} of game {game_no}!")
        else:  # Player 2 wins
            # Append `player2_card` and `player1_card` to the end of `player2_cards` in that order
            player2_cards = player2_cards[::-1]
            player2_cards.insert(0, player2_card)
            player2_cards.insert(0, player1_card)
            player2_cards = player2_cards[::-1]

            print(f"Player 2 wins round {round_no} of game {game_no}!")

        round_no += 1
        print()

    # Return the player who has won
    if len(player1_cards) != 0:
        return 1, player1_cards, player2_cards
    else:
        return 2, player1_cards, player2_cards


# COMPUTATION
# Play recursive combat
winner, player1Cards, player2Cards = recursive_combat(player1Cards, player2Cards)

print()
print("== Post-game Results ==")
print("Player 1's deck:", ", ".join([str(x) for x in player1Cards]))
print("Player 2's deck:", ", ".join([str(x) for x in player2Cards]))
print()

# Get the winning hand
if winner == 1:
    winningDeck = player1Cards
else:
    winningDeck = player2Cards

# Calculate the score
score = 0
for i, card in enumerate(winningDeck[::-1]):
    score += card * (i + 1)

# OUTPUT
print("Score:", score)
