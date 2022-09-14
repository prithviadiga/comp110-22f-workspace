"""looping through all characters of a string."""

user_string: str=(input("Gimme a string! "))

#i is a common counter variable name, i stands for iteration
i: int = 0
while i < len(user_string):
    print (user_string[i])
    i = i + 1