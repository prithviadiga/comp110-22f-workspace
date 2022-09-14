"""Wordle but fr this time"""
__author__= "730480357"


"""The contains_char function checks whether or not the inputted word has the given character anywhere in it."""
def contains_char(word: str, char: str) -> bool:
    assert len(char) == 1
    i = 0
    while i < len(word) :
        if word[i] == char:
            return True
        i += 1
    return False


"""The emojified function assigns green, yellow, and white boxes to guess words based on the results of the contains_char function"""      
def emojified(guess: str, secret: str) -> str:
    assert len(guess) == len(secret) 

    emoji: str = ""
    i = 0
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    while i < len(secret):
        if contains_char(secret[i], guess[i]) == True: 
            emoji += GREEN_BOX
        elif contains_char(secret, guess[i]) == True:
            emoji += YELLOW_BOX
        elif contains_char(secret, guess[i]) == False:
            emoji += WHITE_BOX
        i += 1
    return emoji


"""defines the expected length of the guess word and acts as ui for the user to interact with"""
def input_guess(expected_len: int):
    guess_word: str = (input(f"Enter a {expected_len} character word: "))
    while (expected_len != len(guess_word)):
        guess_word = input(f"That wasn't {expected_len} chars! Try again: ")
    return guess_word


"""The entrypoint of the program and main game loop."""
def main() -> None:
    turn: int = 1
    secret: str = "python"

    while turn <= 6:
        print(f"=== Turn {turn}/6 ===")
        guess: str = input_guess(len(secret))
        print(emojified(guess,secret))
        if guess == secret:
            print(f"You won in {turn}/6 turns!")
            turn = 8
        turn += 1
    if turn == 7:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()


    
    



    