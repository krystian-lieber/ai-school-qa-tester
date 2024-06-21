import unittest
from unittest.mock import patch
from app.factorial import factorial

class TestFactorial(unittest.TestCase):

    def test_factorial_with_positive_number(self):
        result = factorial(5)
        self.assertEqual(result, 120)

    def test_factorial_with_zero(self):
        result = factorial(0)
        self.assertEqual(result, 1)

    def test_factorial_with_negative_number(self):
        with self.assertRaises(ValueError):
            factorial(-1)

    @patch('app.factorial.factorial')
    def test_factorial_with_mocked_recursive_call(self, mock_factorial):
        mock_factorial.side_effect = lambda x: 1 if x == 0 else x * mock_factorial(x - 1)
        result = factorial(3)
        self.assertEqual(result, 6)

if __name__ == '__main__':
    unittest.main()