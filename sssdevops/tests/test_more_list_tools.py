"""
Tests more lists tool, the split method
"""
from sssdevops import split
import pytest


# @pytest.mark.skip
def test_split_edge():
    list1, list2 = split([1, 2], 0)
    assert list1 == [] and list2 == [1, 2]

@pytest.mark.my_easy_test
def test_split_easy():
    arr = [1, 2, 3, 4, 5]
    list1, list2 = split(arr, 3)

    assert list1 == [1, 2, 3] and list2 == [4, 5]

def test_split_error_index():
    with pytest.raises(TypeError):
        split([1, 2, 3], 'd')

def test_split_error_list():
    with pytest.raises(TypeError):
        split(45, 4)