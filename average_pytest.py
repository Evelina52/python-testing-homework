from calculate_average import calculate_average

def test_empty_list():
    assert calculate_average([]) is None

def test_positive_numbers():
    assert calculate_average([1, 2, 3, 4, 5]) == 3

def test_negative_numbers():
    assert calculate_average([-1, -2, -3]) == -2

def test_mixed_numbers():
    assert calculate_average([-1, 0, 1]) == 0

def test_single_element():
    assert calculate_average([42]) == 42