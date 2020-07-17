# coding-assignment-round-1

## This is the condition for victory in a custom card game
- 4 players are dealt 3 cards each
- A trail (three cards of the same number) is the highest possible combination.
- The next highest is a sequence (numbers in order, e.g., 4,5,6. A is considered to have a value of 1).
- The next highest is a pair of cards (e.g.: two Kings or two 10s).
- If all else fails, the top card (by number value wins).
- If the top card has the same value, each of the tied players draws a single card from the deck until a winner is found.
- Only the newly drawn cards are compared to decide a tie. The top card wins a tie.
- For now the suit (spades/hearts etc...), does not matter.

## The code in the file assignment.py does the following:
1. Simulate a game between 4 players.
2. Randomly deal them cards from a deck.
3. Determine the winner.

## The code in test_game.py does the following:
1. Has a number of test cases and unit test is performed on them using python's unittest library
