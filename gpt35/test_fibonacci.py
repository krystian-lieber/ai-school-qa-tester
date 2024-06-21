import unittest

def fibonacci(n):
    if n < 0:
        raise ValueError('Fibonacci is not defined for negative numbers')
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b

class TestFibonacci(unittest.TestCase):
    def test_fibonacci_with_positive_number(self):
        result = fibonacci(5)
        self.assertEqual(result, 5)

    def test_fibonacci_with_zero(self):
        result = fibonacci(0)
        self.assertEqual(result, 0)

    def test_fibonacci_with_negative_number(self):
        with self.assertRaises(ValueError):
            fibonacci(-1)

if __name__ == '__main__':
    unittest.main()