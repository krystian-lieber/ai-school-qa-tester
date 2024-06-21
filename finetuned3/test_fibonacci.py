import unittest
from app.fibonacci import fibonacci

class TestFibonacciFunction(unittest.TestCase):
    def test_fibonacci_zero(self):
        self.assertEqual(fibonacci(0), 0)

    def test_fibonacci_one(self):
        self.assertEqual(fibonacci(1), 1)

    def test_fibonacci_positive_number(self):
        self.assertEqual(fibonacci(5), 5)

    def test_fibonacci_large_number(self):
        self.assertEqual(fibonacci(10), 55)

if __name__ == '__main__':
    unittest.main()