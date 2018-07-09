"""
Tests more lists tool, the split method
"""
from sssdevops import split


def test_split_easy():
    arr = [1, 2, 3, 4, 5]
    list1, list2 = split(arr, 3)

    assert list1 == [1, 2, 3]
    assert list2 == [4, 5]
