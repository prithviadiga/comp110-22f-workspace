"""One Shot Wordle."""
__author__ = "730480357"

"""Variable List"""
secret_word: str = "python"
guess_word: str = input("What is your 6-letter guess? ")
i: int = 0
ii: int = 0
emoji: str = ""
yellow: bool = False
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

"""While Loop to ensure character count is right"""
while len(guess_word) != len(secret_word):
    guess_word = input("That was not 6 letters! Try again: ")

"""Nested while loop to add emojis"""
while i < 6:
    if guess_word[i] == secret_word[i]:
        emoji += GREEN_BOX

    ii = 0
    yellow = False

    while yellow == False and ii < 6:
        if guess_word[i] == secret_word[ii]:
            yellow = True
        ii += 1
    if yellow == True and guess_word[i] != secret_word[i]:
        emoji += YELLOW_BOX
    if yellow == False:
        emoji += WHITE_BOX
    i += 1

"""End Text"""
print(emoji)
if guess_word == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")