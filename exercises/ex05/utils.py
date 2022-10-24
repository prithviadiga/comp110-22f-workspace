"""implementing functions."""
__author__ = "730480357"


def only_evens(num_list: list[int]) -> list[int]:
    """Isolates even numbers from the inputted list and displays them in a seperate list."""
    even_list: list[int] = []
    i = 0
    while i < len(num_list):
        if num_list[i] % 2 == 0:
            even_list.append(num_list[i])
        i += 1
    return (even_list)


def concat(list1: list[int], list2: list[int]) -> list[int]:
    """Concatenates two lists into one larger list."""
    concat_list: list[int] = []
    for list_entry in list1:
        concat_list.append(list_entry)
    for list_entry in list2:
        concat_list.append(list_entry)
    return (concat_list)


def sub(a_list: list[int], index1: int, index2: int) -> list[int]:
    """Returns numbers between the index numbers from the input list."""
    if index1 <= 0:
        index1 = 0
    if index2 > len(a_list):
        index2 = len(a_list)
    if len(a_list) == 0:
        return list()
    i: int = index1
    b_list: list[int] = []
    while i < index2:
        b_list.append(a_list[i]) 
        i += 1
    return b_list