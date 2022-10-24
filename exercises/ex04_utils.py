"""practicing list utility functions."""
__author__ = "730480357"


def all(a_list: list[int], an_int: int) -> bool:
    """Indicates whether all the ints in the list are equal to the given int."""
    i = 0
    if len(a_list) == 0:
        return False
    while i < len(a_list):
        if a_list[i] != an_int:
            return False
        i += 1
    return True
    

def max(a_list: list[int]) -> int:
    """Finds the highest value within the list."""
    if len(a_list) == 0:
        raise ValueError("max() arg is an empty List")
    i = 1
    large: int = a_list[0]
    while i < len(a_list):
        if large < a_list[i]:
            large = a_list[i]
        i += 1
    return large


def is_equal(a_list: list[int], b_list: list[int]) -> bool:
    """Finds whether the two lists are exactly equal to one another."""
    if a_list == b_list:
        return True
    else:
        return False