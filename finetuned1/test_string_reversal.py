import unittest
from app.string_reversal import reverse_string_exclude_special

class TestStringReversal(unittest.TestCase):
    def test_reverse_string_typical(self):
        self.assertEqual(reverse_string_exclude_special('abc123'), '321cba')
        self.assertEqual(reverse_string_exclude_special('a!b@c'), 'c!b@a')

    def test_reverse_string_empty(self):
        self.assertEqual(reverse_string_exclude_special(''), '')

    def test_reverse_string_special_chars(self):
        self.assertEqual(reverse_string_exclude_special('!@#$'), '!@#$')

if __name__ == '__main__':
    unittest.main()