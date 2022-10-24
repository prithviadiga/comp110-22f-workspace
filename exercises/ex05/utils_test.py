"""unit testing for utils.py."""
__author__ = "730480357"


from utils import only_evens, sub, concat


def test_only_evens_empty() -> None:
    """Asserts that an empty list using the only_evens function should return an empty list."""
    num_list: list[int] = []
    assert only_evens(num_list) == []


def test_only_evens_all_evens() -> None:
    """Asserts that a list with only even numbers using the only_evens function should return an identical list to what was inputted."""
    num_list: list[int] = [2, 4, 6]
    assert only_evens(num_list) == [2, 4, 6]


def test_only_evens_all_odds() -> None:
    """Asserts that a list with only odd numbers using the only_evens function should return an empty list."""
    num_list: list[int] = [1, 3, 5]
    assert only_evens(num_list) == []


def test_concat_empty() -> None:
    """Asserts that if both input lists using the concat function are empty, the returned list will be empty as well."""
    list1: list[int] = []
    list2: list[int] = []
    assert concat(list1, list2) == []


def test_concat_single() -> None:
    """Asserts that if both input lists using the concat function are single characters, the returned list will contain two characters."""
    list1: list[int] = [1]
    list2: list[int] = [2]
    assert concat(list1, list2) == [1, 2]


def test_concat_full() -> None:
    """Asserts that if both input lists using the concat function have multiple characters, all of them will be contained in the returned list."""
    list1: list[int] = [1, 2, 3]
    list2: list[int] = [1, 2, 3]
    assert concat(list1, list2) == [1, 2, 3, 1, 2, 3]


def test_sub_empty() -> None:
    """Asserts that regardless of the index numbers, if the input list is empty, the resulting list will be empty."""
    a_list: list[int] = []
    index1: int = 0
    index2: int = 1
    assert sub(a_list, index1, index2) == []


def test_sub_cramped() -> None:
    """Asserts that if the list is smaller than the index range, it will only return the first index number."""
    a_list: list[int] = [0, 1]
    index1: int = 0
    index2: int = 1
    assert sub(a_list, index1, index2) == [0]


def test_sub_normal() -> None:
    """Asserts that if the indices are in the middle of the list, outside numbers aren't included in the returned list."""
    a_list: list[int] = [0, 1, 2, 3, 4]
    index1: int = 1
    index2: int = 3
    assert sub(a_list, index1, index2) == [1, 2]