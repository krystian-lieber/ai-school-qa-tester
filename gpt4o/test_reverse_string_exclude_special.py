import unittest
from app.string_reversal import reverse_string_exclude_special

class TestReverseStringExcludeSpecial(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(reverse_string_exclude_special('abc123'), '321cba', "Failed on typical case with alphanumeric characters")

    def test_with_special_characters(self):
        self.assertEqual(reverse_string_exclude_special('a!b@c#1$2%3^'), '3!2@1#c$b%a^', "Failed on case with special characters")

    def test_empty_string(self):
        self.assertEqual(reverse_string_exclude_special(''), '', "Failed on empty string")

    def test_all_special_characters(self):
        self.assertEqual(reverse_string_exclude_special('!@#$%^&*()'), '!@#$%^&*()', "Failed on string with all special characters")

    def test_single_character(self):
        self.assertEqual(reverse_string_exclude_special('a'), 'a', "Failed on single alphanumeric character")
        self.assertEqual(reverse_string_exclude_special('!'), '!', "Failed on single special character")

    def test_mixed_case(self):
        self.assertEqual(reverse_string_exclude_special('AbC123'), '321CbA', "Failed on mixed case alphanumeric characters")

    def test_unicode_characters(self):
        self.assertEqual(reverse_string_exclude_special('a\ud83d\ude0ab\ud83d\ude0ac'), 'c\ud83d\ude0ab\ud83d\ude0aa', "Failed on string with unicode characters")

if __name__ == '__main__':
    unittest.main()
