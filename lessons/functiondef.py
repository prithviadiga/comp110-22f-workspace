def my_max(a: int, b: int) -> int:
    if a >= b:
        return a
    else: 
        return b
y_age: int = input("How old are you? ")
s_age: int = input("How old is your sibling? ")

print(f"The older sibling is {my_max(y_age, s_age)}")

