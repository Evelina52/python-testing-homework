def multiply(a, b):
    return a * b

def test_multiply_positive_numbers():
    assert multiply(2, 3) == 6
    assert multiply(10, 4) == 40

def test_multiply_negative_numbers():
    assert multiply(-2, -3) == 6
    assert multiply(-5, -2) == 10

def test_multiply_mixed_numbers():
    assert multiply(-2, 3) == -6
    assert multiply(5, -4) == -20