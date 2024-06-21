import unittest
from app.fibonacci import fibonacci

class TestFibonacciFunction(unittest.TestCase):
    def test_fibonacci_positive(self):
        self.assertEqual(fibonacci(10), 55)
        self.assertEqual(fibonacci(5), 5)

    def test_fibonacci_zero(self):
        self.assertEqual(fibonacci(0), 0)

    def test_fibonacci_negative(self):
        with self.assertRaises(ValueError):
            fibonacci(-1)

if __name__ == '__main__':
    unittest.main()