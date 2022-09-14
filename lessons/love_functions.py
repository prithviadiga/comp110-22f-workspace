
"""Given a subject as a parameter, returns a loving string"""
def love(subject : str) -> str:
    return(f"I love you {subject}!")


"""Generates a str repeating a loving message n times."""
def spreadlove(to : str, n : int) -> str:
    love_note: str = ""
    i: int = 0
    while i < n:
        love_note += love(to) + "\n"
        i += 1
    return love_note

