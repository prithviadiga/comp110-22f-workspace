"""Unit tests for dictionary functions."""
__author__ = "730480357"


from dictionary import invert, favorite_color, count


def test_invert_empty() -> None:
    """Edge Case: Asserts that an empty dictionary when inverted will return nothing."""
    empty_dict: dict[str, str] = dict()
    assert invert(empty_dict) == []


def test_invert_single_pair() -> None:
    """Use Case: Asserts that when a dictionary containing a single key value pair is inverted, it returns just the single pair but inverted."""
    single_pair: dict[str, str] = {"Pear": "Apple"}
    assert invert(single_pair) == {"Apple": "Pear"}


def test_invert_many_pairs() -> None:
    """Use Case: Asserts that when a dictionary contains many pairs, they are returned inverted but ordered correctly."""
    many_pairs: dict[str, str] = {"Pear": "Apple", "Triangle": "Rectangle"}
    assert invert(many_pairs) == {"Apple": "Pear", "Rectangle": "Triangle"}


def test_favorite_color_empty() -> None:
    """Edge Case: Asserts that when the dictionary is empty the result will also be empty."""
    empty_dict: dict[str, str] = {}
    assert favorite_color(empty_dict) == ""


def test_favorite_color_single() -> None:
    """Use Case: Asserts that when the dictionary has only one color, that color will be returned."""
    single: dict[str, str] = {"Name1": "Blue", "Name2": "Blue", "Name3": "Blue"}
    assert favorite_color(single) == "Blue"


def test_favorite_color_many() -> None:
    """Use Case: Asserts that when many people have many favorite colors, the one with the most and the one that appears first will be returned."""
    many: dict[str, str] = {"Name1": "Blue", "Name2": "Blue", "Name3": "Red", "Name4": "Red", "Name5": "Green"}
    assert favorite_color(many) == "Blue"


def test_count_none() -> None:
    """Edge Case: Asserts that if the list is empty, an empty dictionary is returned."""
    none: list[str] = []
    assert count(none) == {}


def test_count_single() -> None:
    """Use Case: Asserts that if a single value is repeated in the list, it will appear once in the returned dictionary."""
    single: list[str] = ["dynamite", "dynamite", "dynamite"]
    assert count(single) == {"dynamite": 3}


def test_count_many() -> None:
    """Use Case: Asserts that if many values are repeated in the list, they will appear several times in the returned dictionary."""
    single: list[str] = ["dynamite", "dynamite", "dynamite", "dynamic", "dynamo", "dynamic"]
    assert count(single) == {"dynamite": 3, "dynamic": 2, "dynamo": 1}