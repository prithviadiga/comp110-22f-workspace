"""Functions involving dictionaries."""
__author__ = "730480357"


def invert(dictionary1: dict[str, str]) -> dict[str, str]:
    """Takes a list of dictionary with strings in the key and values and inverts their placements."""
    dictionary2: dict[str, str] = dict()
    for key in dictionary1:
        if dictionary1[key] in dictionary2:
            raise KeyError("You cannot have two keys that share the same name!")
        dictionary2[dictionary1[key]] = key
    return dictionary2


def favorite_color(dictionary1: dict[str, str]) -> str:
    """Takes a dictionary with names and favorite colors and returns the most popular favorite color."""
    vlist: dict[str, int] = {}
    for key in dictionary1:
        if dictionary1[key] in vlist:
            vlist[dictionary1[key]] += 1
        else:
            vlist[dictionary1[key]] = 1
    color: str = ""
    color_num: int = 0
    for key in vlist:
        if vlist[key] > color_num:
            color_num = vlist[key]
            color = key
    return color


def count(list1: list[str]) -> dict[str, int]:
    """A list of strings is given and a dictionary that returns the strings in key and the amount of times they appear in the values is returned."""
    dictionary1: dict[str, int] = dict()
    i: int = 0
    while i < len(list1):
        if list1[i] in dictionary1:
            dictionary1[list1[i]] += 1
        else:
            dictionary1[list1[i]] = 1
        i += 1
    return dictionary1