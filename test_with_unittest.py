import unittest

def add(a, b):
    return a + b

class TestAddFunction(unittest.TestCase):
    
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(10, 15), 25)
    
    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -2), -3)
        self.assertEqual(add(-10, -5), -15)
    
    def test_add_mixed_numbers(self):
        self.assertEqual(add(-5, 5), 0)
        self.assertEqual(add(10, -3), 7)

if __name__ == '__main__':
    unittest.main()