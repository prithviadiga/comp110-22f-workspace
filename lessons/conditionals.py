"""An example of conditional (if-else) statements."""

SECRET: int = 3

print("I'm thinking of a number between 1 and 5. What is it? ")
guess: int= int(input("What is your guess? "))

if guess == SECRET: 
    print("You guessed correctly!!!")
    print("Have a wonderful day!")

else: 
    print("You guessed wrong :(((")
    print("Please try again.")

print("Game Over!")