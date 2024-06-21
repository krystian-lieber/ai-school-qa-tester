import unittest
from app.string_reversal import reverse_string_exclude_special

class TestReverseStringExcludeSpecialFunction(unittest.TestCase):
    def test_reverse_string_exclude_special_all_alphanumeric(self):
        self.assertEqual(reverse_string_exclude_special('abcdefg'), 'gfedcba')

    def test_reverse_string_exclude_special_mixed_characters(self):
        self.assertEqual(reverse_string_exclude_special('hello world'), 'dlroW olleH')

    def test_reverse_string_exclude_special_no_alphanumeric(self):
        self.assertEqual(reverse_string_exclude_special('bcdfg'), 'bcdfg')

    def test_reverse_string_exclude_special_empty_string(self):
        self.assertEqual(reverse_string_exclude_special(''), '')

if __name__ == '__main__':
    unittest.main()