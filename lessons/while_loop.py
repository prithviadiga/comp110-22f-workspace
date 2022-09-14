"""An example of a while loop statement"""

counter: int = 0
maximum: int = int(input("Count upto "))
while counter <= maximum:
    print(f"The square of {counter} is {counter ** 2}")
    counter = counter + 1

print("Done!")

