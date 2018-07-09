from sssdevops import mean
import pytest


@pytest.fixture
def num_list_3():
    return [1, 2, 3, 4, 5]

# def test_simple():
#     assert mean([1, 2, 3, 4, 5]) == 3.0

def test_simple(num_list_3):
    assert mean(num_list_3) == 3.0


def test_empty():
    with pytest.raises(ZeroDivisionError):
        mean([])

# def test_size_one():
#     assert mean([5]) == 5

@pytest.mark.parametrize("num_list, expected_mean", [
    ([1, 2, 3, 4, 5], 3),
    ([5], 5),
    ([1, 2], 1.5),
])
def test_many(num_list, expected_mean):
    assert mean(num_list) == expected_mean
