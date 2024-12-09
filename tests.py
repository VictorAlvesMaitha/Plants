import unittest
from fibo import fibonacci

class TestFibonacci(unittest.TestCase):
    def test_fibonacci_sequence(self):
        # Test with n = 5
        result = fibonacci(5)
        expected = [0, 1, 1, 2, 3]
        self.assertEqual(result, expected)
    
    def test_fibonacci_zero(self):
        # Test with n = 0
        result = fibonacci(0)
        expected = []
        self.assertEqual(result, expected)
    
    def test_fibonacci_one(self):
        # Test with n = 1
        result = fibonacci(1)
        expected = [0]
        self.assertEqual(result, expected)
    
    def test_fibonacci_negative(self):
        # Test with negative n
        with self.assertRaises(ValueError):
            fibonacci(-5)
    
    def test_fibonacci_large_n(self):
        # Test with n = 10
        result = fibonacci(10)
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()

# Output:
# .....
    # assert result == expected