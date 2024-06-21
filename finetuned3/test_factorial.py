import unittest
from app.factorial import factorial

class TestFactorialFunction(unittest.TestCase):
    def test_factorial_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_positive_number(self):
        self.assertEqual(factorial(5), 120)

    def test_factorial_large_number(self):
        self.assertEqual(factorial(10), 3628800)

    def test_factorial_negative_number(self):
        with self.assertRaises(ValueError):
            factorial(-1)

if __name__ == '__main__':
    unittest.main()