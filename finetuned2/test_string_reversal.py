import unittest
from app.string_reversal import reverse_string_exclude_special

class TestReverseStringExcludeSpecialFunction(unittest.TestCase):
    def test_reverse_string_exclude_special_all_letters(self):
        self.assertEqual(reverse_string_exclude_special('hello world'), 'dlrow olleh')

    def test_reverse_string_exclude_special_mixed(self):
        self.assertEqual(reverse_string_exclude_special('a!b@c'), 'c!b@a')

    def test_reverse_string_exclude_special_numbers(self):
        self.assertEqual(reverse_string_exclude_special('123!456'), '654!321')

if __name__ == '__main__':
    unittest.main()