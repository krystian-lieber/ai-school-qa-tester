import unittest
from app.factorial import factorial

class TestFactorial(unittest.TestCase):

    def test_factorial_positive_integer(self):
        self.assertEqual(factorial(5), 120, 'Expected factorial(5) to be 120')

    def test_factorial_zero(self):
        self.assertEqual(factorial(0), 1, 'Expected factorial(0) to be 1')

    def test_factorial_negative_integer(self):
        with self.assertRaises(ValueError, msg='Factorial is not defined for negative numbers'):
            factorial(-1)

    def test_factorial_one(self):
        self.assertEqual(factorial(1), 1, 'Expected factorial(1) to be 1')

    def test_factorial_large_number(self):
        self.assertEqual(factorial(10), 3628800, 'Expected factorial(10) to be 3628800')

if __name__ == '__main__':
    unittest.main()
