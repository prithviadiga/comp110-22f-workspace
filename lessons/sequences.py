"""Examples of the tuple and range sequences."""

# An example of a tuple without type aliasing
goat: tuple[str, str] = ("MJ",23)

# Tuples are sequences so they're 0-indexed
print(goat[0]) == "MJ"

# Sequences have lengths
print(len(goat)) == 2

# Sequences are iterable for for.. in loops
# Meaning you can loop over them with for.. in
for item in goat:
    print(item) == "MJ", 23

# Tuples unlike lists are immutable and can't have items reassigned, appended, or popped. 

# We can invent our own types with tuples (Type Aliasing)
Player = tuple[str, int]

# Once we've aliased a type we can create variables of that type
unc_poy: Player = ("Bacot", 5)

# To change jersey number
unc_poy = (unc_poy[0], unc_poy[1]+1)

"------------------------------------------------------------------------------------------------"

# A range is another common sequence type
zero_to_nine: range = range(0,10,1) #range(start,stop,step) start and step parameters
                                    # are optional and their default values are 0 and 1 

# We can access items of the range
print(zero_to_nine[0])
print(zero_to_nine[9])

for i in zero_to_nine:
    print(i) # == 0 1 2 3 4 5 6 7 8 9 10

odds_to_99: range = range(1, 100, 2)
for i in odds_to_99:
    print(i) # == 1,3,5,7,9,11 ...


names: list[str] = ["Kris", "Alyssa", "Michael", "Lebron"]
for i in range(len(names)):
    print(f"{i}. {names[i]}") # == 0. Kris  1. Alyssa  2. Michael  3. Lebron
