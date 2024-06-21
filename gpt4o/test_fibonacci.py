import unittest
from app.fibonacci import fibonacci

class TestFibonacci(unittest.TestCase):

    def test_fibonacci_typical_cases(self):
        self.assertEqual(fibonacci(0), 0, 'Expected fibonacci(0) to be 0')
        self.assertEqual(fibonacci(1), 1, 'Expected fibonacci(1) to be 1')
        self.assertEqual(fibonacci(2), 1, 'Expected fibonacci(2) to be 1')
        self.assertEqual(fibonacci(3), 2, 'Expected fibonacci(3) to be 2')
        self.assertEqual(fibonacci(4), 3, 'Expected fibonacci(4) to be 3')
        self.assertEqual(fibonacci(5), 5, 'Expected fibonacci(5) to be 5')
        self.assertEqual(fibonacci(10), 55, 'Expected fibonacci(10) to be 55')

    def test_fibonacci_edge_cases(self):
        self.assertEqual(fibonacci(20), 6765, 'Expected fibonacci(20) to be 6765')
        self.assertEqual(fibonacci(30), 832040, 'Expected fibonacci(30) to be 832040')

    def test_fibonacci_invalid_input(self):
        with self.assertRaises(ValueError, msg='Fibonacci is not defined for negative numbers'):
            fibonacci(-1)
        with self.assertRaises(ValueError, msg='Fibonacci is not defined for negative numbers'):
            fibonacci(-10)

    def test_fibonacci_large_input(self):
        self.assertEqual(fibonacci(50), 12586269025, 'Expected fibonacci(50) to be 12586269025')
        self.assertEqual(fibonacci(100), 354224848179261915075, 'Expected fibonacci(100) to be 354224848179261915075')

if __name__ == '__main__':
    unittest.main()
