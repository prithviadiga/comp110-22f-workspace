def v_and_t(x: str) -> str:
    vowels: list[str] = ["a", "e", "i", "o", "u"]
    return_value: str = ""
    v = 0
    i = 0
    is_vowel: bool = False
    while i < len(x):
        while v < len(vowels):
            is_vowel = False
            if vowels[v] == x[i]:
                is_vowel = True
            if is_vowel and i % 3 == 0: 
                return_value += ""
            elif is_vowel or i % 3 == 0:
                return_value += x[i]
            v += 1
        i += 1
    return return_value


print(v_and_t("hello world"))