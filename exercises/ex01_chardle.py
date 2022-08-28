"""EX01 - Chardle - A cute step towards Wordle"""

__author__ = "730480357"

from operator import index

five_word: str = str(input("Enter a 5-character word: "))
if len(five_word)!=5: 
    print("Word must contain 5 characters.")
    then: quit()
single_char: str=str(input("Enter a single character: "))
if len(single_char)!=1: 
    print("Error: Character must be a single character.")
    then: quit()
print("Searching for " + single_char + " in " + five_word + ".")

match_char: int = 0

if five_word[0]==single_char:
    print(single_char + " found at index 0")
    match_char=match_char+1
if five_word[1]==single_char:
    print(single_char + " found at index 1")
    match_char=match_char+1
if five_word[2]==single_char:
    print(single_char + " found at index 2")      
    match_char=match_char+1
if five_word[3]==single_char:
    print(single_char + " found at index 3")   
    match_char=match_char+1
if five_word[4]==single_char:
    print(single_char + " found at index 4")   
    match_char=match_char+1

if match_char==0:
    print("No instances of " + single_char + " found in " + five_word)
else:
    if match_char==1:
     print(str(match_char) + " instance of " + single_char + " found in " + five_word)
    else: 
         print(str(match_char) + " instances of " + single_char + " found in " + five_word)





    


