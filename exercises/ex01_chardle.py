"""EX01 - Chardle - A cute step towards Wordle."""

__author__ = "730480357"

five_letter_word: str = str(input("Enter a 5-character word: "))
if len(five_letter_word) != 5: 
    print("Error: Word must contain 5 characters.")
    quit()
single_character: str = str(input("Enter a single character: "))
if len(single_character) != 1: 
    print("Error: Character must be a single character.")
    quit()
print("Searching for " + single_character + " in " + five_letter_word + ".")

match_count: int = 0 

if five_letter_word[0] == single_character:
    print(single_character + " found at index 0")
    match_count = match_count + 1 
if five_letter_word[1] == single_character:
    print(single_character + " found at index 1")
    match_count = match_count + 1
if five_letter_word[2] == single_character:
    print(single_character + " found at index 2")      
    match_count = match_count + 1
if five_letter_word[3] == single_character:
    print(single_character + " found at index 3")   
    match_count = match_count + 1
if five_letter_word[4] == single_character:
    print(single_character + " found at index 4")   
    match_count = match_count + 1

if match_count == 0:
    print("No instances of " + single_character + " found in " + five_letter_word)
else:
    if match_count == 1:
        print(str(match_count) + " instance of " + single_character + " found in " + five_letter_word)
    else: 
        print(str(match_count) + " instances of " + single_character + " found in " + five_letter_word)