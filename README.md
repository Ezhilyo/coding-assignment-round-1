# Card Game Simulater
## These are the rules for the custom card game
- Use a standard deck of cards (no Joker).
- Each player is dealt only three cards.
- 'A' is considered to have a number value of 1.
- 'A' is considered the top card in a face-off. So the order is A > K > Q > J > 10...2
## This is the condition for victory in a custom card game
- A trail (three cards of the same number) is the highest possible combination.
- The next highest is a sequence (numbers in order, e.g., 4,5,6. A is considered to have a value of 1).
- The next highest is a pair of cards (e.g.: two Kings or two 10s).
- If all else fails, the top card (by number value wins).
- If the top card has the same value, each of the tied players draws a single card from the deck until a winner is found.
- Only the newly drawn cards are compared to decide a tie. The top card wins a tie.
- For now the suit (spades/hearts etc...), does not matter.

## The code in the file assignment.py does the following:
1. Simulates a game between 4 players.
2. Randomly deals them cards from a deck.
3. Determines the winner.

## The code in test_game.py does the following:
1. Has a number of test cases and unit test is performed on them using python's unittest library
