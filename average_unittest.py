import unittest
from calculate_average import calculate_average
class TestCalculateAverage(unittest.TestCase):
    
    def test_empty_list(self):
        self.assertIsNone(calculate_average([]))
    def test_positive_numbers(self):
        self.assertEqual(calculate_average([1, 2, 3, 4, 5]), 3)  
        self.assertEqual(calculate_average([10, 20, 30]), 20)     
    def test_negative_numbers(self):
        self.assertEqual(calculate_average([-1, -2, -3]), -2) 
        self.assertEqual(calculate_average([-10, -20, -30]), -20)
    def test_mixed_numbers(self):
        self.assertEqual(calculate_average([-1, 0, 1]), 0)      
        self.assertEqual(calculate_average([5, -3, 2]), 1)        
    def test_float_numbers(self):
        self.assertEqual(calculate_average([1.9, 2.1, 3.5]), 2)   
        self.assertEqual(calculate_average([10.9, 11.1]), 10)     

if __name__ == '__main__':
    unittest.main()