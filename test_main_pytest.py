import pytest
from main import calculate_average

def test_empty_list():
    assert calculate_average([]) is None

def test_positive_numbers():
    assert calculate_average([1, 2, 3, 4, 5]) == 3

@pytest.mark.parametrize("numbers,expected", [
    ([], None),
    ([5, 5, 5], 5),
    ([1.1, 2.2, 3.3], 2),
    ([-3, -2, -1], -2),
])
def test_parametrized(numbers, expected):
    assert calculate_average(numbers) == expected