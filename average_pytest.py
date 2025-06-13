import pytest
from calculate_average import calculate_average

def test_empty_list():
    assert calculate_average([]) is None

def test_positive_numbers():
    assert calculate_average([1, 2, 3, 4, 5]) == 3
    assert calculate_average([10, 20, 30]) == 20

def test_negative_numbers():
    assert calculate_average([-1, -2, -3]) == -2
    assert calculate_average([-10, -20, -30]) == -20

def test_mixed_numbers():
    assert calculate_average([-1, 0, 1]) == 0
    assert calculate_average([5, -3, 2]) == 1

def test_float_numbers():
    assert calculate_average([1.9, 2.1, 3.5]) == 2
    assert calculate_average([10.9, 11.1]) == 10

@pytest.mark.parametrize("numbers,expected", [
    ([], None),
    ([5, 5, 5], 5),
    ([1.1, 2.2, 3.3], 2),
    ([-3, -2, -1], -2),
])
def test_parametrized(numbers, expected):
    assert calculate_average(numbers) == expected