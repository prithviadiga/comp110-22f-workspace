"""Wordle but fr this time."""
__author__ = "730480357"


def contains_char(word: str, char: str) -> bool:
    """The contains_char function checks whether or not the inputted word has the given character anywhere in it."""
    assert len(char) == 1
    i = 0
    while i < len(word):
        if word[i] == char:
            return True
        i += 1
    return False

      
def emojified(guess: str, secret: str) -> str:
    """The emojified function assigns green, yellow, and white boxes to guess words based on the results of the contains_char function."""
    assert len(guess) == len(secret) 

    emoji: str = ""
    i = 0
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    while i < len(secret):
        if contains_char(secret[i], guess[i]): 
            emoji += GREEN_BOX
        elif contains_char(secret, guess[i]):
            emoji += YELLOW_BOX
        elif not contains_char(secret, guess[i]):
            emoji += WHITE_BOX
        i += 1
    return emoji


def input_guess(expected_len: int) -> str:
    """Defines the expected length of the guess word and acts as ui for the user to interact with."""
    guess_word: str = (input(f"Enter a {expected_len} character word: "))
    while (expected_len != len(guess_word)):
        guess_word = input(f"That wasn't {expected_len} chars! Try again: ")
    return guess_word


def main() -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1
    secret: str = "codes"

    while turn <= 6:
        print(f"=== Turn {turn}/6 ===")
        guess: str = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            print(f"You won in {turn}/6 turns!")
            turn = 8
        turn += 1
    if turn == 7:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()