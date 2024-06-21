import unittest
from app.string_reversal import reverse_string_exclude_special

class TestReverseStringExcludeSpecial(unittest.TestCase):

    def test_reverse_string_exclude_special_typical_input(self):
        # Test with a typical input string
        result = reverse_string_exclude_special('abc$de%f')
        self.assertEqual(result, 'fed$cb%a')

    def test_reverse_string_exclude_special_edge_case(self):
        # Test with an edge case input string
        result = reverse_string_exclude_special('a$bcd$e%fgh$i')
        self.assertEqual(result, 'i$hgf$e%dcb$a')

    def test_reverse_string_exclude_special_invalid_input(self):
        # Test with an invalid input string
        result = reverse_string_exclude_special('12345')
        self.assertEqual(result, '54321')

if __name__ == '__main__':
    unittest.main()