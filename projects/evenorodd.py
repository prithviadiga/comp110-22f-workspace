"""This program tracks whether a program is even or odd."""
num: int = input("gimme any number: ")
if float(num) % 2 == 0:
    print(f"{num} is even.")
elif float(num) % 2 == 1: 
    print(f"{num} is odd.")

