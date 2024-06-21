training_data= [
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef add(a, b):\n    return a + b\n```",
        "completion": "```python\nimport unittest\n\nclass TestAddFunction(unittest.TestCase):\n    def test_add_large_numbers(self):\n        self.assertEqual(add(1e10, 1e10), 2e10)\n\n    def test_add_float_numbers(self):\n        self.assertAlmostEqual(add(0.1, 0.2), 0.3, places=7)\n\n    def test_add_string_numbers(self):\n        with self.assertRaises(TypeError):\n            add('1', 1)\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef multiply(a, b):\n    return a * b\n```",
        "completion": "```python\nimport unittest\n\nclass TestMultiplyFunction(unittest.TestCase):\n    def test_multiply_large_numbers(self):\n        self.assertEqual(multiply(1e10, 1e10), 1e20)\n\n    def test_multiply_by_float_numbers(self):\n        self.assertAlmostEqual(multiply(0.1, 0.2), 0.02, places=7)\n\n    def test_multiply_by_string_numbers(self):\n        with self.assertRaises(TypeError):\n            multiply('1', 1)\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef divide(a, b):\n    if b == 0:\n        raise ValueError('Cannot divide by zero')\n    return a / b\n```",
        "completion": "```python\nimport unittest\n\nclass TestDivideFunction(unittest.TestCase):\n    def test_divide_large_numbers(self):\n        self.assertAlmostEqual(divide(1e10, 1e2), 1e8)\n\n    def test_divide_by_float_numbers(self):\n        self.assertAlmostEqual(divide(0.1, 0.2), 0.5, places=7)\n\n    def test_divide_by_zero_float(self):\n        with self.assertRaises(ValueError):\n            divide(1.0, 0.0)\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef subtract(a, b):\n    return a - b\n```",
        "completion": "```python\nimport unittest\n\nclass TestSubtractFunction(unittest.TestCase):\n    def test_subtract_large_numbers(self):\n        self.assertEqual(subtract(1e10, 1e9), 9e9)\n\n    def test_subtract_float_numbers(self):\n        self.assertAlmostEqual(subtract(0.1, 0.2), -0.1, places=7)\n\n    def test_subtract_string_numbers(self):\n        with self.assertRaises(TypeError):\n            subtract('1', 1)\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef power(a, b):\n    return a ** b\n```",
        "completion": "```python\nimport unittest\n\nclass TestPowerFunction(unittest.TestCase):\n    def test_power_large_numbers(self):\n        self.assertEqual(power(10, 10), 1e10)\n\n    def test_power_zero_exponent(self):\n        self.assertEqual(power(2, 0), 1)\n\n    def test_power_negative_exponent(self):\n        self.assertAlmostEqual(power(2, -1), 0.5, places=7)\n\n    def test_power_float_exponent(self):\n        self.assertAlmostEqual(power(9, 0.5), 3, places=7)\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef modulo(a, b):\n    return a % b\n```",
        "completion": "```python\nimport unittest\n\nclass TestModuloFunction(unittest.TestCase):\n    def test_modulo_positive_numbers(self):\n        self.assertEqual(modulo(10, 3), 1)\n\n    def test_modulo_negative_numbers(self):\n        self.assertEqual(modulo(-10, 3), -1)\n\n    def test_modulo_by_zero(self):\n        with self.assertRaises(ZeroDivisionError):\n            modulo(10, 0)\n\n    def test_modulo_float_numbers(self):\n        self.assertAlmostEqual(modulo(10.5, 3.2), 0.9, places=7)\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef factorial(n):\n    if n == 0:\n        return 1\n    else:\n        return n * factorial(n-1)\n```",
        "completion": "```python\nimport unittest\n\nclass TestFactorialFunction(unittest.TestCase):\n    def test_factorial_zero(self):\n        self.assertEqual(factorial(0), 1)\n\n    def test_factorial_positive_number(self):\n        self.assertEqual(factorial(5), 120)\n\n    def test_factorial_large_number(self):\n        self.assertEqual(factorial(10), 3628800)\n\n    def test_factorial_negative_number(self):\n        with self.assertRaises(RecursionError):\n            factorial(-1)\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef fibonacci(n):\n    if n <= 0:\n        return 0\n    elif n == 1:\n        return 1\n    else:\n        return fibonacci(n-1) + fibonacci(n-2)\n```",
        "completion": "```python\nimport unittest\n\nclass TestFibonacciFunction(unittest.TestCase):\n    def test_fibonacci_zero(self):\n        self.assertEqual(fibonacci(0), 0)\n\n    def test_fibonacci_one(self):\n        self.assertEqual(fibonacci(1), 1)\n\n    def test_fibonacci_positive_number(self):\n        self.assertEqual(fibonacci(5), 5)\n\n    def test_fibonacci_large_number(self):\n        self.assertEqual(fibonacci(10), 55)\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef is_prime(n):\n    if n <= 1:\n        return False\n    for i in range(2, int(n**0.5) + 1):\n        if n % i == 0:\n            return False\n    return True\n```",
        "completion": "```python\nimport unittest\n\nclass TestIsPrimeFunction(unittest.TestCase):\n    def test_is_prime_small_prime(self):\n        self.assertTrue(is_prime(7))\n\n    def test_is_prime_small_non_prime(self):\n        self.assertFalse(is_prime(4))\n\n    def test_is_prime_large_prime(self):\n        self.assertTrue(is_prime(29))\n\n    def test_is_prime_large_non_prime(self):\n        self.assertFalse(is_prime(30))\n\n    def test_is_prime_negative_number(self):\n        self.assertFalse(is_prime(-5))\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef is_even(n):\n    return n % 2 == 0\n```",
        "completion": "```python\nimport unittest\n\nclass TestIsEvenFunction(unittest.TestCase):\n    def test_is_even_positive_number(self):\n        self.assertTrue(is_even(4))\n\n    def test_is_even_negative_number(self):\n        self.assertTrue(is_even(-4))\n\n    def test_is_even_odd_number(self):\n        self.assertFalse(is_even(5))\n\n    def test_is_even_zero(self):\n        self.assertTrue(is_even(0))\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef is_palindrome(s):\n    return s == s[::-1]\n```",
        "completion": "```python\nimport unittest\n\nclass TestIsPalindromeFunction(unittest.TestCase):\n    def test_is_palindrome_even_length(self):\n        self.assertTrue(is_palindrome('abba'))\n\n    def test_is_palindrome_odd_length(self):\n        self.assertTrue(is_palindrome('racecar'))\n\n    def test_is_palindrome_not_palindrome(self):\n        self.assertFalse(is_palindrome('hello'))\n\n    def test_is_palindrome_empty_string(self):\n        self.assertTrue(is_palindrome(''))\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef reverse_string(s):\n    return s[::-1]\n```",
        "completion": "```python\nimport unittest\n\nclass TestReverseStringFunction(unittest.TestCase):\n    def test_reverse_string_regular(self):\n        self.assertEqual(reverse_string('hello'), 'olleh')\n\n    def test_reverse_string_empty(self):\n        self.assertEqual(reverse_string(''), '')\n\n    def test_reverse_string_single_character(self):\n        self.assertEqual(reverse_string('a'), 'a')\n\n    def test_reverse_string_palindrome(self):\n        self.assertEqual(reverse_string('racecar'), 'racecar')\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef find_max(arr):\n    return max(arr)\n```",
        "completion": "```python\nimport unittest\n\nclass TestFindMaxFunction(unittest.TestCase):\n    def test_find_max_positive_numbers(self):\n        self.assertEqual(find_max([1, 2, 3, 4, 5]), 5)\n\n    def test_find_max_negative_numbers(self):\n        self.assertEqual(find_max([-1, -2, -3, -4, -5]), -1)\n\n    def test_find_max_mixed_numbers(self):\n        self.assertEqual(find_max([-1, 0, 1, 2, 3]), 3)\n\n    def test_find_max_single_element(self):\n        self.assertEqual(find_max([42]), 42)\n\n    def test_find_max_empty_list(self):\n        with self.assertRaises(ValueError):\n            find_max([])\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef find_min(arr):\n    return min(arr)\n```",
        "completion": "```python\nimport unittest\n\nclass TestFindMinFunction(unittest.TestCase):\n    def test_find_min_positive_numbers(self):\n        self.assertEqual(find_min([1, 2, 3, 4, 5]), 1)\n\n    def test_find_min_negative_numbers(self):\n        self.assertEqual(find_min([-1, -2, -3, -4, -5]), -5)\n\n    def test_find_min_mixed_numbers(self):\n        self.assertEqual(find_min([-1, 0, 1, 2, 3]), -1)\n\n    def test_find_min_single_element(self):\n        self.assertEqual(find_min([42]), 42)\n\n    def test_find_min_empty_list(self):\n        with self.assertRaises(ValueError):\n            find_min([])\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef sum_list(arr):\n    return sum(arr)\n```",
        "completion": "```python\nimport unittest\n\nclass TestSumListFunction(unittest.TestCase):\n    def test_sum_list_positive_numbers(self):\n        self.assertEqual(sum_list([1, 2, 3, 4, 5]), 15)\n\n    def test_sum_list_negative_numbers(self):\n        self.assertEqual(sum_list([-1, -2, -3, -4, -5]), -15)\n\n    def test_sum_list_mixed_numbers(self):\n        self.assertEqual(sum_list([-1, 0, 1, 2, 3]), 5)\n\n    def test_sum_list_empty_list(self):\n        self.assertEqual(sum_list([]), 0)\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef average_list(arr):\n    return sum(arr) / len(arr) if arr else 0\n```",
        "completion": "```python\nimport unittest\n\nclass TestAverageListFunction(unittest.TestCase):\n    def test_average_list_positive_numbers(self):\n        self.assertAlmostEqual(average_list([1, 2, 3, 4, 5]), 3.0, places=7)\n\n    def test_average_list_negative_numbers(self):\n        self.assertAlmostEqual(average_list([-1, -2, -3, -4, -5]), -3.0, places=7)\n\n    def test_average_list_mixed_numbers(self):\n        self.assertAlmostEqual(average_list([-1, 0, 1, 2, 3]), 1.0, places=7)\n\n    def test_average_list_empty_list(self):\n        self.assertEqual(average_list([]), 0)\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef count_vowels(s):\n    return sum(1 for char in s if char.lower() in 'aeiou')\n```",
        "completion": "```python\nimport unittest\n\nclass TestCountVowelsFunction(unittest.TestCase):\n    def test_count_vowels_all_vowels(self):\n        self.assertEqual(count_vowels('aeiou'), 5)\n\n    def test_count_vowels_mixed_characters(self):\n        self.assertEqual(count_vowels('hello world'), 3)\n\n    def test_count_vowels_no_vowels(self):\n        self.assertEqual(count_vowels('bcdfg'), 0)\n\n    def test_count_vowels_empty_string(self):\n        self.assertEqual(count_vowels(''), 0)\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef count_consonants(s):\n    return sum(1 for char in s if char.lower() in 'bcdfghjklmnpqrstvwxyz')\n```",
        "completion": "```python\nimport unittest\n\nclass TestCountConsonantsFunction(unittest.TestCase):\n    def test_count_consonants_all_consonants(self):\n        self.assertEqual(count_consonants('bcdfg'), 5)\n\n    def test_count_consonants_mixed_characters(self):\n        self.assertEqual(count_consonants('hello world'), 7)\n\n    def test_count_consonants_no_consonants(self):\n        self.assertEqual(count_consonants('aeiou'), 0)\n\n    def test_count_consonants_empty_string(self):\n        self.assertEqual(count_consonants(''), 0)\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef is_anagram(s1, s2):\n    return sorted(s1) == sorted(s2)\n```",
        "completion": "```python\nimport unittest\n\nclass TestIsAnagramFunction(unittest.TestCase):\n    def test_is_anagram_positive(self):\n        self.assertTrue(is_anagram('listen', 'silent'))\n\n    def test_is_anagram_negative(self):\n        self.assertFalse(is_anagram('hello', 'world'))\n\n    def test_is_anagram_empty_strings(self):\n        self.assertTrue(is_anagram('', ''))\n\n    def test_is_anagram_case_sensitive(self):\n        self.assertFalse(is_anagram('Listen', 'Silent'))\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef is_unique_chars(s):\n    return len(s) == len(set(s))\n```",
        "completion": "```python\nimport unittest\n\nclass TestIsUniqueCharsFunction(unittest.TestCase):\n    def test_is_unique_chars_unique(self):\n        self.assertTrue(is_unique_chars('abcdef'))\n\n    def test_is_unique_chars_non_unique(self):\n        self.assertFalse(is_unique_chars('hello'))\n\n    def test_is_unique_chars_empty_string(self):\n        self.assertTrue(is_unique_chars(''))\n\n    def test_is_unique_chars_single_character(self):\n        self.assertTrue(is_unique_chars('a'))\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef is_sorted(arr):\n    return arr == sorted(arr)\n```",
        "completion": "```python\nimport unittest\n\nclass TestIsSortedFunction(unittest.TestCase):\n    def test_is_sorted_sorted_list(self):\n        self.assertTrue(is_sorted([1, 2, 3, 4, 5]))\n\n    def test_is_sorted_unsorted_list(self):\n        self.assertFalse(is_sorted([5, 3, 2, 4, 1]))\n\n    def test_is_sorted_single_element(self):\n        self.assertTrue(is_sorted([42]))\n\n    def test_is_sorted_empty_list(self):\n        self.assertTrue(is_sorted([]))\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef merge_dicts(d1, d2):\n    result = d1.copy()\n    result.update(d2)\n    return result\n```",
        "completion": "```python\nimport unittest\n\nclass TestMergeDictsFunction(unittest.TestCase):\n    def test_merge_dicts_non_overlapping_keys(self):\n        self.assertEqual(merge_dicts({'a': 1}, {'b': 2}), {'a': 1, 'b': 2})\n\n    def test_merge_dicts_overlapping_keys(self):\n        self.assertEqual(merge_dicts({'a': 1}, {'a': 2}), {'a': 2})\n\n    def test_merge_dicts_empty_dicts(self):\n        self.assertEqual(merge_dicts({}, {}), {})\n\n    def test_merge_dicts_one_empty_dict(self):\n        self.assertEqual(merge_dicts({'a': 1}, {}), {'a': 1})\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef flatten_list(nested_list):\n    return [item for sublist in nested_list for item in sublist]\n```",
        "completion": "```python\nimport unittest\n\nclass TestFlattenListFunction(unittest.TestCase):\n    def test_flatten_list_single_level(self):\n        self.assertEqual(flatten_list([[1, 2], [3, 4]]), [1, 2, 3, 4])\n\n    def test_flatten_list_nested(self):\n        self.assertEqual(flatten_list([[1, [2]], [3, 4]]), [1, [2], 3, 4])\n\n    def test_flatten_list_empty(self):\n        self.assertEqual(flatten_list([]), [])\n\n    def test_flatten_list_mixed_types(self):\n        self.assertEqual(flatten_list([[1, 'a'], [3, 4.0]]), [1, 'a', 3, 4.0])\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef square(a):\n    return a * a\n```",
        "completion": "```python\nimport unittest\n\nclass TestSquareFunction(unittest.TestCase):\n    def test_square_positive_number(self):\n        self.assertEqual(square(3), 9)\n\n    def test_square_negative_number(self):\n        self.assertEqual(square(-3), 9)\n\n    def test_square_zero(self):\n        self.assertEqual(square(0), 0)\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef cube(a):\n    return a * a * a\n```",
        "completion": "```python\nimport unittest\n\nclass TestCubeFunction(unittest.TestCase):\n    def test_cube_positive_number(self):\n        self.assertEqual(cube(3), 27)\n\n    def test_cube_negative_number(self):\n        self.assertEqual(cube(-3), -27)\n\n    def test_cube_zero(self):\n        self.assertEqual(cube(0), 0)\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef is_uppercase(s):\n    return s.isupper()\n```",
        "completion": "```python\nimport unittest\n\nclass TestIsUppercaseFunction(unittest.TestCase):\n    def test_is_uppercase_all_uppercase(self):\n        self.assertTrue(is_uppercase('HELLO'))\n\n    def test_is_uppercase_mixed_case(self):\n        self.assertFalse(is_uppercase('Hello'))\n\n    def test_is_uppercase_all_lowercase(self):\n        self.assertFalse(is_uppercase('hello'))\n\n    def test_is_uppercase_empty_string(self):\n        self.assertFalse(is_uppercase(''))\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef is_lowercase(s):\n    return s.islower()\n```",
        "completion": "```python\nimport unittest\n\nclass TestIsLowercaseFunction(unittest.TestCase):\n    def test_is_lowercase_all_lowercase(self):\n        self.assertTrue(is_lowercase('hello'))\n\n    def test_is_lowercase_mixed_case(self):\n        self.assertFalse(is_lowercase('Hello'))\n\n    def test_is_lowercase_all_uppercase(self):\n        self.assertFalse(is_lowercase('HELLO'))\n\n    def test_is_lowercase_empty_string(self):\n        self.assertFalse(is_lowercase(''))\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef is_empty(s):\n    return len(s) == 0\n```",
        "completion": "```python\nimport unittest\n\nclass TestIsEmptyFunction(unittest.TestCase):\n    def test_is_empty_empty_string(self):\n        self.assertTrue(is_empty(''))\n\n    def test_is_empty_non_empty_string(self):\n        self.assertFalse(is_empty('hello'))\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
        {
        "prompt": "Generate a unit test for this function: \n```python\ndef is_odd(n):\n    return n % 2 != 0\n```",
        "completion": "```python\nimport unittest\n\nclass TestIsOddFunction(unittest.TestCase):\n    def test_is_odd_positive_odd(self):\n        self.assertTrue(is_odd(3))\n\n    def test_is_odd_positive_even(self):\n        self.assertFalse(is_odd(4))\n\n    def test_is_odd_negative_odd(self):\n        self.assertTrue(is_odd(-3))\n\n    def test_is_odd_negative_even(self):\n        self.assertFalse(is_odd(-4))\n\n    def test_is_odd_zero(self):\n        self.assertFalse(is_odd(0))\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef is_leap_year(year):\n    if year % 4 == 0:\n        if year % 100 == 0:\n            if year % 400 == 0:\n                return True\n            else:\n                return False\n        else:\n            return True\n    else:\n        return False\n```",
        "completion": "```python\nimport unittest\n\nclass TestIsLeapYearFunction(unittest.TestCase):\n    def test_is_leap_year_divisible_by_4_not_100(self):\n        self.assertTrue(is_leap_year(2024))\n\n    def test_is_leap_year_divisible_by_100_not_400(self):\n        self.assertFalse(is_leap_year(1900))\n\n    def test_is_leap_year_divisible_by_400(self):\n        self.assertTrue(is_leap_year(2000))\n\n    def test_is_leap_year_not_divisible_by_4(self):\n        self.assertFalse(is_leap_year(2023))\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef gcd(a, b):\n    while b:\n        a, b = b, a % b\n    return a\n```",
        "completion": "```python\nimport unittest\n\nclass TestGcdFunction(unittest.TestCase):\n    def test_gcd_positive_numbers(self):\n        self.assertEqual(gcd(48, 18), 6)\n\n    def test_gcd_one_zero(self):\n        self.assertEqual(gcd(0, 18), 18)\n\n    def test_gcd_both_zeros(self):\n        self.assertEqual(gcd(0, 0), 0)\n\n    def test_gcd_negative_numbers(self):\n        self.assertEqual(gcd(-48, -18), 6)\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef lcm(a, b):\n    if a == 0 or b == 0:\n        return 0\n    else:\n        return abs(a * b) // gcd(a, b)\n```",
        "completion": "```python\nimport unittest\n\nclass TestLcmFunction(unittest.TestCase):\n    def test_lcm_positive_numbers(self):\n        self.assertEqual(lcm(4, 5), 20)\n\n    def test_lcm_one_zero(self):\n        self.assertEqual(lcm(0, 5), 0)\n\n    def test_lcm_both_zeros(self):\n        self.assertEqual(lcm(0, 0), 0)\n\n    def test_lcm_negative_numbers(self):\n        self.assertEqual(lcm(-4, 5), 20)\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef factorial_iterative(n):\n    result = 1\n    for i in range(2, n + 1):\n        result *= i\n    return result\n```",
        "completion": "```python\nimport unittest\n\nclass TestFactorialIterativeFunction(unittest.TestCase):\n    def test_factorial_iterative_zero(self):\n        self.assertEqual(factorial_iterative(0), 1)\n\n    def test_factorial_iterative_positive_number(self):\n        self.assertEqual(factorial_iterative(5), 120)\n\n    def test_factorial_iterative_large_number(self):\n        self.assertEqual(factorial_iterative(10), 3628800)\n\n    def test_factorial_iterative_negative_number(self):\n        with self.assertRaises(ValueError):\n            factorial_iterative(-1)\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef binary_search(arr, target):\n    left, right = 0, len(arr) - 1\n    while left <= right:\n        mid = (left + right) // 2\n        if arr[mid] == target:\n            return mid\n        elif arr[mid] < target:\n            left = mid + 1\n        else:\n            right = mid - 1\n    return -1\n```",
        "completion": "```python\nimport unittest\n\nclass TestBinarySearchFunction(unittest.TestCase):\n    def test_binary_search_found(self):\n        self.assertEqual(binary_search([1, 2, 3, 4, 5], 3), 2)\n\n    def test_binary_search_not_found(self):\n        self.assertEqual(binary_search([1, 2, 3, 4, 5], 6), -1)\n\n    def test_binary_search_empty_list(self):\n        self.assertEqual(binary_search([], 3), -1)\n\n    def test_binary_search_single_element_found(self):\n        self.assertEqual(binary_search([3], 3), 0)\n\n    def test_binary_search_single_element_not_found(self):\n        self.assertEqual(binary_search([3], 4), -1)\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef linear_search(arr, target):\n    for i, value in enumerate(arr):\n        if value == target:\n            return i\n    return -1\n```",
        "completion": "```python\nimport unittest\n\nclass TestLinearSearchFunction(unittest.TestCase):\n    def test_linear_search_found(self):\n        self.assertEqual(linear_search([1, 2, 3, 4, 5], 3), 2)\n\n    def test_linear_search_not_found(self):\n        self.assertEqual(linear_search([1, 2, 3, 4, 5], 6), -1)\n\n    def test_linear_search_empty_list(self):\n        self.assertEqual(linear_search([], 3), -1)\n\n    def test_linear_search_single_element_found(self):\n        self.assertEqual(linear_search([3], 3), 0)\n\n    def test_linear_search_single_element_not_found(self):\n        self.assertEqual(linear_search([3], 4), -1)\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef bubble_sort(arr):\n    n = len(arr)\n    for i in range(n):\n        for j in range(0, n-i-1):\n            if arr[j] > arr[j+1]:\n                arr[j], arr[j+1] = arr[j+1], arr[j]\n    return arr\n```",
        "completion": "```python\nimport unittest\n\nclass TestBubbleSortFunction(unittest.TestCase):\n    def test_bubble_sort_sorted_list(self):\n        self.assertEqual(bubble_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])\n\n    def test_bubble_sort_unsorted_list(self):\n        self.assertEqual(bubble_sort([5, 3, 2, 4, 1]), [1, 2, 3, 4, 5])\n\n    def test_bubble_sort_single_element(self):\n        self.assertEqual(bubble_sort([42]), [42])\n\n    def test_bubble_sort_empty_list(self):\n        self.assertEqual(bubble_sort([]), [])\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef quick_sort(arr):\n    if len(arr) <= 1:\n        return arr\n    pivot = arr[len(arr) // 2]\n    left = [x for x in arr if x < pivot]\n    middle = [x for x in arr if x == pivot]\n    right = [x for x in arr if x > pivot]\n    return quick_sort(left) + middle + quick_sort(right)\n```",
        "completion": "```python\nimport unittest\n\nclass TestQuickSortFunction(unittest.TestCase):\n    def test_quick_sort_sorted_list(self):\n        self.assertEqual(quick_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])\n\n    def test_quick_sort_unsorted_list(self):\n        self.assertEqual(quick_sort([5, 3, 2, 4, 1]), [1, 2, 3, 4, 5])\n\n    def test_quick_sort_single_element(self):\n        self.assertEqual(quick_sort([42]), [42])\n\n    def test_quick_sort_empty_list(self):\n        self.assertEqual(quick_sort([]), [])\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef merge_sort(arr):\n    if len(arr) > 1:\n        mid = len(arr) // 2\n        L = arr[:mid]\n        R = arr[mid:]\n\n        merge_sort(L)\n        merge_sort(R)\n\n        i = j = k = 0\n\n        while i < len(L) and j < len(R):\n            if L[i] < R[j]:\n                arr[k] = L[i]\n                i += 1\n            else:\n                arr[k] = R[j]\n                j += 1\n            k += 1\n\n        while i < len(L):\n            arr[k] = L[i]\n            i += 1\n            k += 1\n\n        while j < len(R):\n            arr[k] = R[j]\n            j += 1\n            k += 1\n    return arr\n```",
        "completion": "```python\nimport unittest\n\nclass TestMergeSortFunction(unittest.TestCase):\n    def test_merge_sort_sorted_list(self):\n        self.assertEqual(merge_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])\n\n    def test_merge_sort_unsorted_list(self):\n        self.assertEqual(merge_sort([5, 3, 2, 4, 1]), [1, 2, 3, 4, 5])\n\n    def test_merge_sort_single_element(self):\n        self.assertEqual(merge_sort([42]), [42])\n\n    def test_merge_sort_empty_list(self):\n        self.assertEqual(merge_sort([]), [])\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef add(a, b):\n    return a + b\n```",
        "completion": "```python\nimport unittest\n\nclass TestAddFunction(unittest.TestCase):\n    def test_add_positive_numbers(self):\n        self.assertEqual(add(2, 3), 5)\n\n    def test_add_negative_numbers(self):\n        self.assertEqual(add(-1, -1), -2)\n\n    def test_add_positive_and_negative_numbers(self):\n        self.assertEqual(add(-1, 1), 0)\n\n    def test_add_zero(self):\n        self.assertEqual(add(0, 0), 0)\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
        {
        "prompt": "Generate a unit test for this function: \n```python\ndef max_of_three(a, b, c):\n    return max(a, b, c)\n```",
        "completion": "```python\nimport unittest\n\nclass TestMaxOfThreeFunction(unittest.TestCase):\n    def test_max_of_three_all_positive(self):\n        self.assertEqual(max_of_three(1, 2, 3), 3)\n\n    def test_max_of_three_all_negative(self):\n        self.assertEqual(max_of_three(-1, -2, -3), -1)\n\n    def test_max_of_three_mixed(self):\n        self.assertEqual(max_of_three(-1, 0, 1), 1)\n\n    def test_max_of_three_same_values(self):\n        self.assertEqual(max_of_three(2, 2, 2), 2)\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef min_of_three(a, b, c):\n    return min(a, b, c)\n```",
        "completion": "```python\nimport unittest\n\nclass TestMinOfThreeFunction(unittest.TestCase):\n    def test_min_of_three_all_positive(self):\n        self.assertEqual(min_of_three(1, 2, 3), 1)\n\n    def test_min_of_three_all_negative(self):\n        self.assertEqual(min_of_three(-1, -2, -3), -3)\n\n    def test_min_of_three_mixed(self):\n        self.assertEqual(min_of_three(-1, 0, 1), -1)\n\n    def test_min_of_three_same_values(self):\n        self.assertEqual(min_of_three(2, 2, 2), 2)\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef is_palindrome_number(n):\n    return str(n) == str(n)[::-1]\n```",
        "completion": "```python\nimport unittest\n\nclass TestIsPalindromeNumberFunction(unittest.TestCase):\n    def test_is_palindrome_number_positive(self):\n        self.assertTrue(is_palindrome_number(121))\n\n    def test_is_palindrome_number_negative(self):\n        self.assertFalse(is_palindrome_number(-121))\n\n    def test_is_palindrome_number_not_palindrome(self):\n        self.assertFalse(is_palindrome_number(123))\n\n    def test_is_palindrome_number_single_digit(self):\n        self.assertTrue(is_palindrome_number(7))\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef is_armstrong_number(n):\n    num_str = str(n)\n    num_len = len(num_str)\n    return n == sum(int(digit) ** num_len for digit in num_str)\n```",
        "completion": "```python\nimport unittest\n\nclass TestIsArmstrongNumberFunction(unittest.TestCase):\n    def test_is_armstrong_number_positive(self):\n        self.assertTrue(is_armstrong_number(153))\n\n    def test_is_armstrong_number_negative(self):\n        self.assertFalse(is_armstrong_number(123))\n\n    def test_is_armstrong_number_single_digit(self):\n        self.assertTrue(is_armstrong_number(5))\n\n    def test_is_armstrong_number_large_number(self):\n        self.assertTrue(is_armstrong_number(9474))\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef is_perfect_square(n):\n    return int(n**0.5) ** 2 == n\n```",
        "completion": "```python\nimport unittest\n\nclass TestIsPerfectSquareFunction(unittest.TestCase):\n    def test_is_perfect_square_positive(self):\n        self.assertTrue(is_perfect_square(16))\n\n    def test_is_perfect_square_negative(self):\n        self.assertFalse(is_perfect_square(15))\n\n    def test_is_perfect_square_zero(self):\n        self.assertTrue(is_perfect_square(0))\n\n    def test_is_perfect_square_large_number(self):\n        self.assertTrue(is_perfect_square(10000))\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef is_perfect_number(n):\n    return n == sum(i for i in range(1, n) if n % i == 0)\n```",
        "completion": "```python\nimport unittest\n\nclass TestIsPerfectNumberFunction(unittest.TestCase):\n    def test_is_perfect_number_positive(self):\n        self.assertTrue(is_perfect_number(6))\n\n    def test_is_perfect_number_negative(self):\n        self.assertFalse(is_perfect_number(10))\n\n    def test_is_perfect_number_large_number(self):\n        self.assertTrue(is_perfect_number(28))\n\n    def test_is_perfect_number_non_perfect(self):\n        self.assertFalse(is_perfect_number(12))\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef is_fibonacci_number(n):\n    x1 = 5 * n * n + 4\n    x2 = 5 * n * n - 4\n    return int(x1**0.5) ** 2 == x1 or int(x2**0.5) ** 2 == x2\n```",
        "completion": "```python\nimport unittest\n\nclass TestIsFibonacciNumberFunction(unittest.TestCase):\n    def test_is_fibonacci_number_positive(self):\n        self.assertTrue(is_fibonacci_number(8))\n\n    def test_is_fibonacci_number_negative(self):\n        self.assertFalse(is_fibonacci_number(10))\n\n    def test_is_fibonacci_number_zero(self):\n        self.assertTrue(is_fibonacci_number(0))\n\n    def test_is_fibonacci_number_large_number(self):\n        self.assertTrue(is_fibonacci_number(144))\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef is_happy_number(n):\n    seen = set()\n    while n != 1 and n not in seen:\n        seen.add(n)\n        n = sum(int(digit) ** 2 for digit in str(n))\n    return n == 1\n```",
        "completion": "```python\nimport unittest\n\nclass TestIsHappyNumberFunction(unittest.TestCase):\n    def test_is_happy_number_positive(self):\n        self.assertTrue(is_happy_number(19))\n\n    def test_is_happy_number_negative(self):\n        self.assertFalse(is_happy_number(20))\n\n    def test_is_happy_number_single_digit(self):\n        self.assertTrue(is_happy_number(1))\n\n    def test_is_happy_number_large_number(self):\n        self.assertTrue(is_happy_number(100))\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef is_valid_parentheses(s):\n    stack = []\n    mapping = {')': '(', '}': '{', ']': '['}\n    for char in s:\n        if char in mapping:\n            top_element = stack.pop() if stack else '#'\n            if mapping[char] != top_element:\n                return False\n        else:\n            stack.append(char)\n    return not stack\n```",
        "completion": "```python\nimport unittest\n\nclass TestIsValidParenthesesFunction(unittest.TestCase):\n    def test_is_valid_parentheses_positive(self):\n        self.assertTrue(is_valid_parentheses('()'))\n\n    def test_is_valid_parentheses_negative(self):\n        self.assertFalse(is_valid_parentheses('([)]'))\n\n    def test_is_valid_parentheses_empty_string(self):\n        self.assertTrue(is_valid_parentheses(''))\n\n    def test_is_valid_parentheses_mixed(self):\n        self.assertTrue(is_valid_parentheses('{[]}'))\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef is_valid_email(email):\n    import re\n    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$'\n    return re.match(pattern, email) is not None\n```",
        "completion": "```python\nimport unittest\n\nclass TestIsValidEmailFunction(unittest.TestCase):\n    def test_is_valid_email_positive(self):\n        self.assertTrue(is_valid_email('test@example.com'))\n\n    def test_is_valid_email_negative(self):\n        self.assertFalse(is_valid_email('test@.com'))\n\n    def test_is_valid_email_missing_at(self):\n        self.assertFalse(is_valid_email('testexample.com'))\n\n    def test_is_valid_email_missing_domain(self):\n        self.assertFalse(is_valid_email('test@com'))\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef is_valid_url(url):\n    import re\n    pattern = re.compile(\n        r'^(?:http|ftp)s?://' # http:// or https://\n        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\\.)+(?:[A-Z]{2,6}\\.?|[A-Z0-9-]{2,}\\.?))' # domain...\n        r'(?:/?|[/?]\\S+)$', re.IGNORECASE)\n    return re.match(pattern, url) is not None\n```",
        "completion": "```python\nimport unittest\n\nclass TestIsValidUrlFunction(unittest.TestCase):\n    def test_is_valid_url_positive(self):\n        self.assertTrue(is_valid_url('http://example.com'))\n\n    def test_is_valid_url_negative(self):\n        self.assertFalse(is_valid_url('example.com'))\n\n    def test_is_valid_url_missing_protocol(self):\n        self.assertFalse(is_valid_url('www.example.com'))\n\n    def test_is_valid_url_ftp(self):\n        self.assertTrue(is_valid_url('ftp://example.com'))\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef is_valid_ip(ip):\n    import re\n    pattern = re.compile(\n        r'^(?:[0-9]{1,3}\\.){3}[0-9]{1,3}$'\n    )\n    return re.match(pattern, ip) is not None and all(0 <= int(num) <= 255 for num in ip.split('.'))\n```",
        "completion": "```python\nimport unittest\n\nclass TestIsValidIpFunction(unittest.TestCase):\n    def test_is_valid_ip_positive(self):\n        self.assertTrue(is_valid_ip('192.168.0.1'))\n\n    def test_is_valid_ip_negative(self):\n        self.assertFalse(is_valid_ip('256.256.256.256'))\n\n    def test_is_valid_ip_missing_octet(self):\n        self.assertFalse(is_valid_ip('192.168.0'))\n\n    def test_is_valid_ip_extra_octet(self):\n        self.assertFalse(is_valid_ip('192.168.0.1.1'))\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef is_valid_credit_card(number):\n    number = str(number)\n    total = 0\n    reverse_digits = number[::-1]\n    for i, digit in enumerate(reverse_digits):\n        n = int(digit)\n        if i % 2 == 1:\n            n *= 2\n            if n > 9:\n                n -= 9\n        total += n\n    return total % 10 == 0\n```",
        "completion": "```python\nimport unittest\n\nclass TestIsValidCreditCardFunction(unittest.TestCase):\n    def test_is_valid_credit_card_positive(self):\n        self.assertTrue(is_valid_credit_card('4532015112830366'))\n\n    def test_is_valid_credit_card_negative(self):\n        self.assertFalse(is_valid_credit_card('1234567812345670'))\n\n    def test_is_valid_credit_card_short_number(self):\n        self.assertFalse(is_valid_credit_card('1234'))\n\n    def test_is_valid_credit_card_non_digit(self):\n        self.assertFalse(is_valid_credit_card('4532a15112830366'))\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
         {
        "prompt": "Generate a unit test for this function: \n```python\ndef factorial(n):\n    if n == 0:\n        return 1\n    else:\n        return n * factorial(n-1)\n```",
        "completion": "```python\nimport unittest\n\nclass TestFactorialFunction(unittest.TestCase):\n    def test_factorial_zero(self):\n        self.assertEqual(factorial(0), 1)\n\n    def test_factorial_positive_number(self):\n        self.assertEqual(factorial(5), 120)\n\n    def test_factorial_large_number(self):\n        self.assertEqual(factorial(10), 3628800)\n\n    def test_factorial_negative_number(self):\n        with self.assertRaises(RecursionError):\n            factorial(-1)\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef fibonacci(n):\n    if n <= 0:\n        return 0\n    elif n == 1:\n        return 1\n    else:\n        return fibonacci(n-1) + fibonacci(n-2)\n```",
        "completion": "```python\nimport unittest\n\nclass TestFibonacciFunction(unittest.TestCase):\n    def test_fibonacci_zero(self):\n        self.assertEqual(fibonacci(0), 0)\n\n    def test_fibonacci_one(self):\n        self.assertEqual(fibonacci(1), 1)\n\n    def test_fibonacci_positive_number(self):\n        self.assertEqual(fibonacci(5), 5)\n\n    def test_fibonacci_large_number(self):\n        self.assertEqual(fibonacci(10), 55)\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef is_prime(n):\n    if n <= 1:\n        return False\n    for i in range(2, int(n**0.5) + 1):\n        if n % i == 0:\n            return False\n    return True\n```",
        "completion": "```python\nimport unittest\n\nclass TestIsPrimeFunction(unittest.TestCase):\n    def test_is_prime_small_prime(self):\n        self.assertTrue(is_prime(7))\n\n    def test_is_prime_small_non_prime(self):\n        self.assertFalse(is_prime(4))\n\n    def test_is_prime_large_prime(self):\n        self.assertTrue(is_prime(29))\n\n    def test_is_prime_large_non_prime(self):\n        self.assertFalse(is_prime(30))\n\n    def test_is_prime_negative_number(self):\n        self.assertFalse(is_prime(-5))\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef is_even(n):\n    return n % 2 == 0\n```",
        "completion": "```python\nimport unittest\n\nclass TestIsEvenFunction(unittest.TestCase):\n    def test_is_even_positive_number(self):\n        self.assertTrue(is_even(4))\n\n    def test_is_even_negative_number(self):\n        self.assertTrue(is_even(-4))\n\n    def test_is_even_odd_number(self):\n        self.assertFalse(is_even(5))\n\n    def test_is_even_zero(self):\n        self.assertTrue(is_even(0))\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef is_palindrome(s):\n    return s == s[::-1]\n```",
        "completion": "```python\nimport unittest\n\nclass TestIsPalindromeFunction(unittest.TestCase):\n    def test_is_palindrome_even_length(self):\n        self.assertTrue(is_palindrome('abba'))\n\n    def test_is_palindrome_odd_length(self):\n        self.assertTrue(is_palindrome('racecar'))\n\n    def test_is_palindrome_not_palindrome(self):\n        self.assertFalse(is_palindrome('hello'))\n\n    def test_is_palindrome_empty_string(self):\n        self.assertTrue(is_palindrome(''))\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef reverse_string(s):\n    return s[::-1]\n```",
        "completion": "```python\nimport unittest\n\nclass TestReverseStringFunction(unittest.TestCase):\n    def test_reverse_string_regular(self):\n        self.assertEqual(reverse_string('hello'), 'olleh')\n\n    def test_reverse_string_empty(self):\n        self.assertEqual(reverse_string(''), '')\n\n    def test_reverse_string_single_character(self):\n        self.assertEqual(reverse_string('a'), 'a')\n\n    def test_reverse_string_palindrome(self):\n        self.assertEqual(reverse_string('racecar'), 'racecar')\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef find_max(arr):\n    return max(arr)\n```",
        "completion": "```python\nimport unittest\n\nclass TestFindMaxFunction(unittest.TestCase):\n    def test_find_max_positive_numbers(self):\n        self.assertEqual(find_max([1, 2, 3, 4, 5]), 5)\n\n    def test_find_max_negative_numbers(self):\n        self.assertEqual(find_max([-1, -2, -3, -4, -5]), -1)\n\n    def test_find_max_mixed_numbers(self):\n        self.assertEqual(find_max([-1, 0, 1, 2, 3]), 3)\n\n    def test_find_max_single_element(self):\n        self.assertEqual(find_max([42]), 42)\n\n    def test_find_max_empty_list(self):\n        with self.assertRaises(ValueError):\n            find_max([])\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef find_min(arr):\n    return min(arr)\n```",
        "completion": "```python\nimport unittest\n\nclass TestFindMinFunction(unittest.TestCase):\n    def test_find_min_positive_numbers(self):\n        self.assertEqual(find_min([1, 2, 3, 4, 5]), 1)\n\n    def test_find_min_negative_numbers(self):\n        self.assertEqual(find_min([-1, -2, -3, -4, -5]), -5)\n\n    def test_find_min_mixed_numbers(self):\n        self.assertEqual(find_min([-1, 0, 1, 2, 3]), -1)\n\n    def test_find_min_single_element(self):\n        self.assertEqual(find_min([42]), 42)\n\n    def test_find_min_empty_list(self):\n        with self.assertRaises(ValueError):\n            find_min([])\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef count_vowels(s):\n    return sum(1 for char in s if char.lower() in 'aeiou')\n```",
        "completion": "```python\nimport unittest\n\nclass TestCountVowelsFunction(unittest.TestCase):\n    def test_count_vowels_all_vowels(self):\n        self.assertEqual(count_vowels('aeiou'), 5)\n\n    def test_count_vowels_mixed_characters(self):\n        self.assertEqual(count_vowels('hello world'), 3)\n\n    def test_count_vowels_no_vowels(self):\n        self.assertEqual(count_vowels('bcdfg'), 0)\n\n    def test_count_vowels_empty_string(self):\n        self.assertEqual(count_vowels(''), 0)\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef count_consonants(s):\n    return sum(1 for char in s if char.lower() in 'bcdfghjklmnpqrstvwxyz')\n```",
        "completion": "```python\nimport unittest\n\nclass TestCountConsonantsFunction(unittest.TestCase):\n    def test_count_consonants_all_consonants(self):\n        self.assertEqual(count_consonants('bcdfg'), 5)\n\n    def test_count_consonants_mixed_characters(self):\n        self.assertEqual(count_consonants('hello world'), 7)\n\n    def test_count_consonants_no_consonants(self):\n        self.assertEqual(count_consonants('aeiou'), 0)\n\n    def test_count_consonants_empty_string(self):\n        self.assertEqual(count_consonants(''), 0)\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef is_anagram(s1, s2):\n    return sorted(s1) == sorted(s2)\n```",
        "completion": "```python\nimport unittest\n\nclass TestIsAnagramFunction(unittest.TestCase):\n    def test_is_anagram_positive(self):\n        self.assertTrue(is_anagram('listen', 'silent'))\n\n    def test_is_anagram_negative(self):\n        self.assertFalse(is_anagram('hello', 'world'))\n\n    def test_is_anagram_empty_strings(self):\n        self.assertTrue(is_anagram('', ''))\n\n    def test_is_anagram_case_sensitive(self):\n        self.assertFalse(is_anagram('Listen', 'Silent'))\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef is_unique_chars(s):\n    return len(s) == len(set(s))\n```",
        "completion": "```python\nimport unittest\n\nclass TestIsUniqueCharsFunction(unittest.TestCase):\n    def test_is_unique_chars_unique(self):\n        self.assertTrue(is_unique_chars('abcdef'))\n\n    def test_is_unique_chars_non_unique(self):\n        self.assertFalse(is_unique_chars('hello'))\n\n    def test_is_unique_chars_empty_string(self):\n        self.assertTrue(is_unique_chars(''))\n\n    def test_is_unique_chars_single_character(self):\n        self.assertTrue(is_unique_chars('a'))\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef is_sorted(arr):\n    return arr == sorted(arr)\n```",
        "completion": "```python\nimport unittest\n\nclass TestIsSortedFunction(unittest.TestCase):\n    def test_is_sorted_sorted_list(self):\n        self.assertTrue(is_sorted([1, 2, 3, 4, 5]))\n\n    def test_is_sorted_unsorted_list(self):\n        self.assertFalse(is_sorted([5, 3, 2, 4, 1]))\n\n    def test_is_sorted_single_element(self):\n        self.assertTrue(is_sorted([42]))\n\n    def test_is_sorted_empty_list(self):\n        self.assertTrue(is_sorted([]))\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef merge_dicts(d1, d2):\n    result = d1.copy()\n    result.update(d2)\n    return result\n```",
        "completion": "```python\nimport unittest\n\nclass TestMergeDictsFunction(unittest.TestCase):\n    def test_merge_dicts_non_overlapping_keys(self):\n        self.assertEqual(merge_dicts({'a': 1}, {'b': 2}), {'a': 1, 'b': 2})\n\n    def test_merge_dicts_overlapping_keys(self):\n        self.assertEqual(merge_dicts({'a': 1}, {'a': 2}), {'a': 2})\n\n    def test_merge_dicts_empty_dicts(self):\n        self.assertEqual(merge_dicts({}, {}), {})\n\n    def test_merge_dicts_one_empty_dict(self):\n        self.assertEqual(merge_dicts({'a': 1}, {}), {'a': 1})\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef flatten_list(nested_list):\n    return [item for sublist in nested_list for item in sublist]\n```",
        "completion": "```python\nimport unittest\n\nclass TestFlattenListFunction(unittest.TestCase):\n    def test_flatten_list_single_level(self):\n        self.assertEqual(flatten_list([[1, 2], [3, 4]]), [1, 2, 3, 4])\n\n    def test_flatten_list_nested(self):\n        self.assertEqual(flatten_list([[1, [2]], [3, 4]]), [1, [2], 3, 4])\n\n    def test_flatten_list_empty(self):\n        self.assertEqual(flatten_list([]), [])\n\n    def test_flatten_list_mixed_types(self):\n        self.assertEqual(flatten_list([[1, 'a'], [3, 4.0]]), [1, 'a', 3, 4.0])\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef square(a):\n    return a * a\n```",
        "completion": "```python\nimport unittest\n\nclass TestSquareFunction(unittest.TestCase):\n    def test_square_positive_number(self):\n        self.assertEqual(square(3), 9)\n\n    def test_square_negative_number(self):\n        self.assertEqual(square(-3), 9)\n\n    def test_square_zero(self):\n        self.assertEqual(square(0), 0)\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef cube(a):\n    return a * a * a\n```",
        "completion": "```python\nimport unittest\n\nclass TestCubeFunction(unittest.TestCase):\n    def test_cube_positive_number(self):\n        self.assertEqual(cube(3), 27)\n\n    def test_cube_negative_number(self):\n        self.assertEqual(cube(-3), -27)\n\n    def test_cube_zero(self):\n        self.assertEqual(cube(0), 0)\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef factorial_iterative(n):\n    result = 1\n    for i in range(2, n + 1):\n        result *= i\n    return result\n```",
        "completion": "```python\nimport unittest\n\nclass TestFactorialIterativeFunction(unittest.TestCase):\n    def test_factorial_iterative_zero(self):\n        self.assertEqual(factorial_iterative(0), 1)\n\n    def test_factorial_iterative_positive_number(self):\n        self.assertEqual(factorial_iterative(5), 120)\n\n    def test_factorial_iterative_large_number(self):\n        self.assertEqual(factorial_iterative(10), 3628800)\n\n    def test_factorial_iterative_negative_number(self):\n        with self.assertRaises(ValueError):\n            factorial_iterative(-1)\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef binary_search(arr, target):\n    left, right = 0, len(arr) - 1\n    while left <= right:\n        mid = (left + right) // 2\n        if arr[mid] == target:\n            return mid\n        elif arr[mid] < target:\n            left = mid + 1\n        else:\n            right = mid - 1\n    return -1\n```",
        "completion": "```python\nimport unittest\n\nclass TestBinarySearchFunction(unittest.TestCase):\n    def test_binary_search_found(self):\n        self.assertEqual(binary_search([1, 2, 3, 4, 5], 3), 2)\n\n    def test_binary_search_not_found(self):\n        self.assertEqual(binary_search([1, 2, 3, 4, 5], 6), -1)\n\n    def test_binary_search_empty_list(self):\n        self.assertEqual(binary_search([], 3), -1)\n\n    def test_binary_search_single_element_found(self):\n        self.assertEqual(binary_search([3], 3), 0)\n\n    def test_binary_search_single_element_not_found(self):\n        self.assertEqual(binary_search([3], 4), -1)\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef linear_search(arr, target):\n    for i, value in enumerate(arr):\n        if value == target:\n            return i\n    return -1\n```",
        "completion": "```python\nimport unittest\n\nclass TestLinearSearchFunction(unittest.TestCase):\n    def test_linear_search_found(self):\n        self.assertEqual(linear_search([1, 2, 3, 4, 5], 3), 2)\n\n    def test_linear_search_not_found(self):\n        self.assertEqual(linear_search([1, 2, 3, 4, 5], 6), -1)\n\n    def test_linear_search_empty_list(self):\n        self.assertEqual(linear_search([], 3), -1)\n\n    def test_linear_search_single_element_found(self):\n        self.assertEqual(linear_search([3], 3), 0)\n\n    def test_linear_search_single_element_not_found(self):\n        self.assertEqual(linear_search([3], 4), -1)\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef bubble_sort(arr):\n    n = len(arr)\n    for i in range(n):\n        for j in range(0, n-i-1):\n            if arr[j] > arr[j+1]:\n                arr[j], arr[j+1] = arr[j+1], arr[j]\n    return arr\n```",
        "completion": "```python\nimport unittest\n\nclass TestBubbleSortFunction(unittest.TestCase):\n    def test_bubble_sort_sorted_list(self):\n        self.assertEqual(bubble_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])\n\n    def test_bubble_sort_unsorted_list(self):\n        self.assertEqual(bubble_sort([5, 3, 2, 4, 1]), [1, 2, 3, 4, 5])\n\n    def test_bubble_sort_single_element(self):\n        self.assertEqual(bubble_sort([42]), [42])\n\n    def test_bubble_sort_empty_list(self):\n        self.assertEqual(bubble_sort([]), [])\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef quick_sort(arr):\n    if len(arr) <= 1:\n        return arr\n    pivot = arr[len(arr) // 2]\n    left = [x for x in arr if x < pivot]\n    middle = [x for x in arr if x == pivot]\n    right = [x for x in arr if x > pivot]\n    return quick_sort(left) + middle + quick_sort(right)\n```",
        "completion": "```python\nimport unittest\n\nclass TestQuickSortFunction(unittest.TestCase):\n    def test_quick_sort_sorted_list(self):\n        self.assertEqual(quick_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])\n\n    def test_quick_sort_unsorted_list(self):\n        self.assertEqual(quick_sort([5, 3, 2, 4, 1]), [1, 2, 3, 4, 5])\n\n    def test_quick_sort_single_element(self):\n        self.assertEqual(quick_sort([42]), [42])\n\n    def test_quick_sort_empty_list(self):\n        self.assertEqual(quick_sort([]), [])\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef merge_sort(arr):\n    if len(arr) > 1:\n        mid = len(arr) // 2\n        L = arr[:mid]\n        R = arr[mid:]\n\n        merge_sort(L)\n        merge_sort(R)\n\n        i = j = k = 0\n\n        while i < len(L) and j < len(R):\n            if L[i] < R[j]:\n                arr[k] = L[i]\n                i += 1\n            else:\n                arr[k] = R[j]\n                j += 1\n            k += 1\n\n        while i < len(L):\n            arr[k] = L[i]\n            i += 1\n            k += 1\n\n        while j < len(R):\n            arr[k] = R[j]\n            j += 1\n            k += 1\n    return arr\n```",
        "completion": "```python\nimport unittest\n\nclass TestMergeSortFunction(unittest.TestCase):\n    def test_merge_sort_sorted_list(self):\n        self.assertEqual(merge_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])\n\n    def test_merge_sort_unsorted_list(self):\n        self.assertEqual(merge_sort([5, 3, 2, 4, 1]), [1, 2, 3, 4, 5])\n\n    def test_merge_sort_single_element(self):\n        self.assertEqual(merge_sort([42]), [42])\n\n    def test_merge_sort_empty_list(self):\n        self.assertEqual(merge_sort([]), [])\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef max_of_three(a, b, c):\n    return max(a, b, c)\n```",
        "completion": "```python\nimport unittest\n\nclass TestMaxOfThreeFunction(unittest.TestCase):\n    def test_max_of_three_all_positive(self):\n        self.assertEqual(max_of_three(1, 2, 3), 3)\n\n    def test_max_of_three_all_negative(self):\n        self.assertEqual(max_of_three(-1, -2, -3), -1)\n\n    def test_max_of_three_mixed(self):\n        self.assertEqual(max_of_three(-1, 0, 1), 1)\n\n    def test_max_of_three_same_values(self):\n        self.assertEqual(max_of_three(2, 2, 2), 2)\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef min_of_three(a, b, c):\n    return min(a, b, c)\n```",
        "completion": "```python\nimport unittest\n\nclass TestMinOfThreeFunction(unittest.TestCase):\n    def test_min_of_three_all_positive(self):\n        self.assertEqual(min_of_three(1, 2, 3), 1)\n\n    def test_min_of_three_all_negative(self):\n        self.assertEqual(min_of_three(-1, -2, -3), -3)\n\n    def test_min_of_three_mixed(self):\n        self.assertEqual(min_of_three(-1, 0, 1), -1)\n\n    def test_min_of_three_same_values(self):\n        self.assertEqual(min_of_three(2, 2, 2), 2)\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef is_palindrome_number(n):\n    return str(n) == str(n)[::-1]\n```",
        "completion": "```python\nimport unittest\n\nclass TestIsPalindromeNumberFunction(unittest.TestCase):\n    def test_is_palindrome_number_positive(self):\n        self.assertTrue(is_palindrome_number(121))\n\n    def test_is_palindrome_number_negative(self):\n        self.assertFalse(is_palindrome_number(-121))\n\n    def test_is_palindrome_number_not_palindrome(self):\n        self.assertFalse(is_palindrome_number(123))\n\n    def test_is_palindrome_number_single_digit(self):\n        self.assertTrue(is_palindrome_number(7))\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef is_armstrong_number(n):\n    num_str = str(n)\n    num_len = len(num_str)\n    return n == sum(int(digit) ** num_len for digit in num_str)\n```",
        "completion": "```python\nimport unittest\n\nclass TestIsArmstrongNumberFunction(unittest.TestCase):\n    def test_is_armstrong_number_positive(self):\n        self.assertTrue(is_armstrong_number(153))\n\n    def test_is_armstrong_number_negative(self):\n        self.assertFalse(is_armstrong_number(123))\n\n    def test_is_armstrong_number_single_digit(self):\n        self.assertTrue(is_armstrong_number(5))\n\n    def test_is_armstrong_number_large_number(self):\n        self.assertTrue(is_armstrong_number(9474))\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef is_perfect_square(n):\n    return int(n**0.5) ** 2 == n\n```",
        "completion": "```python\nimport unittest\n\nclass TestIsPerfectSquareFunction(unittest.TestCase):\n    def test_is_perfect_square_positive(self):\n        self.assertTrue(is_perfect_square(16))\n\n    def test_is_perfect_square_negative(self):\n        self.assertFalse(is_perfect_square(15))\n\n    def test_is_perfect_square_zero(self):\n        self.assertTrue(is_perfect_square(0))\n\n    def test_is_perfect_square_large_number(self):\n        self.assertTrue(is_perfect_square(10000))\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef is_perfect_number(n):\n    return n == sum(i for i in range(1, n) if n % i == 0)\n```",
        "completion": "```python\nimport unittest\n\nclass TestIsPerfectNumberFunction(unittest.TestCase):\n    def test_is_perfect_number_positive(self):\n        self.assertTrue(is_perfect_number(6))\n\n    def test_is_perfect_number_negative(self):\n        self.assertFalse(is_perfect_number(10))\n\n    def test_is_perfect_number_large_number(self):\n        self.assertTrue(is_perfect_number(28))\n\n    def test_is_perfect_number_non_perfect(self):\n        self.assertFalse(is_perfect_number(12))\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef is_fibonacci_number(n):\n    x1 = 5 * n * n + 4\n    x2 = 5 * n * n - 4\n    return int(x1**0.5) ** 2 == x1 or int(x2**0.5) ** 2 == x2\n```",
        "completion": "```python\nimport unittest\n\nclass TestIsFibonacciNumberFunction(unittest.TestCase):\n    def test_is_fibonacci_number_positive(self):\n        self.assertTrue(is_fibonacci_number(8))\n\n    def test_is_fibonacci_number_negative(self):\n        self.assertFalse(is_fibonacci_number(10))\n\n    def test_is_fibonacci_number_zero(self):\n        self.assertTrue(is_fibonacci_number(0))\n\n    def test_is_fibonacci_number_large_number(self):\n        self.assertTrue(is_fibonacci_number(144))\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef is_happy_number(n):\n    seen = set()\n    while n != 1 and n not in seen:\n        seen.add(n)\n        n = sum(int(digit) ** 2 for digit in str(n))\n    return n == 1\n```",
        "completion": "```python\nimport unittest\n\nclass TestIsHappyNumberFunction(unittest.TestCase):\n    def test_is_happy_number_positive(self):\n        self.assertTrue(is_happy_number(19))\n\n    def test_is_happy_number_negative(self):\n        self.assertFalse(is_happy_number(20))\n\n    def test_is_happy_number_single_digit(self):\n        self.assertTrue(is_happy_number(1))\n\n    def test_is_happy_number_large_number(self):\n        self.assertTrue(is_happy_number(100))\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef is_pangram(s):\n    return set('abcdefghijklmnopqrstuvwxyz') <= set(s.lower())\n```",
        "completion": "```python\nimport unittest\n\nclass TestIsPangramFunction(unittest.TestCase):\n    def test_is_pangram_positive(self):\n        self.assertTrue(is_pangram('The quick brown fox jumps over the lazy dog'))\n\n    def test_is_pangram_negative(self):\n        self.assertFalse(is_pangram('Hello world'))\n\n    def test_is_pangram_empty_string(self):\n        self.assertFalse(is_pangram(''))\n\n    def test_is_pangram_missing_letters(self):\n        self.assertFalse(is_pangram('The quick brown fox jumps over the lazy'))\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef is_substring(s1, s2):\n    return s1 in s2\n```",
        "completion": "```python\nimport unittest\n\nclass TestIsSubstringFunction(unittest.TestCase):\n    def test_is_substring_positive(self):\n        self.assertTrue(is_substring('hello', 'hello world'))\n\n    def test_is_substring_negative(self):\n        self.assertFalse(is_substring('world', 'hello'))\n\n    def test_is_substring_empty_string(self):\n        self.assertTrue(is_substring('', 'hello'))\n\n    def test_is_substring_same_string(self):\n        self.assertTrue(is_substring('hello', 'hello'))\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
        {
        "prompt": "Generate a unit test for this function: \n```python\ndef is_valid_parentheses(s):\n    stack = []\n    mapping = {')': '(', '}': '{', ']': '['}\n    for char in s:\n        if char in mapping:\n            top_element = stack.pop() if stack else '#'\n            if mapping[char] != top_element:\n                return False\n        else:\n            stack.append(char)\n    return not stack\n```",
        "completion": "```python\nimport unittest\n\nclass TestIsValidParenthesesFunction(unittest.TestCase):\n    def test_is_valid_parentheses_positive(self):\n        self.assertTrue(is_valid_parentheses('()'))\n\n    def test_is_valid_parentheses_negative(self):\n        self.assertFalse(is_valid_parentheses('([)]'))\n\n    def test_is_valid_parentheses_empty_string(self):\n        self.assertTrue(is_valid_parentheses(''))\n\n    def test_is_valid_parentheses_mixed(self):\n        self.assertTrue(is_valid_parentheses('{[]}'))\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef is_valid_email(email):\n    import re\n    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$'\n    return re.match(pattern, email) is not None\n```",
        "completion": "```python\nimport unittest\n\nclass TestIsValidEmailFunction(unittest.TestCase):\n    def test_is_valid_email_positive(self):\n        self.assertTrue(is_valid_email('test@example.com'))\n\n    def test_is_valid_email_negative(self):\n        self.assertFalse(is_valid_email('test@.com'))\n\n    def test_is_valid_email_missing_at(self):\n        self.assertFalse(is_valid_email('testexample.com'))\n\n    def test_is_valid_email_missing_domain(self):\n        self.assertFalse(is_valid_email('test@com'))\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef is_valid_url(url):\n    import re\n    pattern = re.compile(\n        r'^(?:http|ftp)s?://' # http:// or https://\n        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\\.)+(?:[A-Z]{2,6}\\.?|[A-Z0-9-]{2,}\\.?))' # domain...\n        r'(?:/?|[/?]\\S+)$', re.IGNORECASE)\n    return re.match(pattern, url) is not None\n```",
        "completion": "```python\nimport unittest\n\nclass TestIsValidUrlFunction(unittest.TestCase):\n    def test_is_valid_url_positive(self):\n        self.assertTrue(is_valid_url('http://example.com'))\n\n    def test_is_valid_url_negative(self):\n        self.assertFalse(is_valid_url('example.com'))\n\n    def test_is_valid_url_missing_protocol(self):\n        self.assertFalse(is_valid_url('www.example.com'))\n\n    def test_is_valid_url_ftp(self):\n        self.assertTrue(is_valid_url('ftp://example.com'))\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef is_valid_ip(ip):\n    import re\n    pattern = re.compile(\n        r'^(?:[0-9]{1,3}\\.){3}[0-9]{1,3}$'\n    )\n    return re.match(pattern, ip) is not None and all(0 <= int(num) <= 255 for num in ip.split('.'))\n```",
        "completion": "```python\nimport unittest\n\nclass TestIsValidIpFunction(unittest.TestCase):\n    def test_is_valid_ip_positive(self):\n        self.assertTrue(is_valid_ip('192.168.0.1'))\n\n    def test_is_valid_ip_negative(self):\n        self.assertFalse(is_valid_ip('256.256.256.256'))\n\n    def test_is_valid_ip_missing_octet(self):\n        self.assertFalse(is_valid_ip('192.168.0'))\n\n    def test_is_valid_ip_extra_octet(self):\n        self.assertFalse(is_valid_ip('192.168.0.1.1'))\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef is_valid_credit_card(number):\n    number = str(number)\n    total = 0\n    reverse_digits = number[::-1]\n    for i, digit in enumerate(reverse_digits):\n        n = int(digit)\n        if i % 2 == 1:\n            n *= 2\n            if n > 9:\n                n -= 9\n        total += n\n    return total % 10 == 0\n```",
        "completion": "```python\nimport unittest\n\nclass TestIsValidCreditCardFunction(unittest.TestCase):\n    def test_is_valid_credit_card_positive(self):\n        self.assertTrue(is_valid_credit_card('4532015112830366'))\n\n    def test_is_valid_credit_card_negative(self):\n        self.assertFalse(is_valid_credit_card('1234567812345670'))\n\n    def test_is_valid_credit_card_short_number(self):\n        self.assertFalse(is_valid_credit_card('1234'))\n\n    def test_is_valid_credit_card_non_digit(self):\n        self.assertFalse(is_valid_credit_card('4532a15112830366'))\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef gcd(a, b):\n    while b:\n        a, b = b, a % b\n    return a\n```",
        "completion": "```python\nimport unittest\n\nclass TestGcdFunction(unittest.TestCase):\n    def test_gcd_positive_numbers(self):\n        self.assertEqual(gcd(48, 18), 6)\n\n    def test_gcd_one_zero(self):\n        self.assertEqual(gcd(0, 18), 18)\n\n    def test_gcd_both_zeros(self):\n        self.assertEqual(gcd(0, 0), 0)\n\n    def test_gcd_negative_numbers(self):\n        self.assertEqual(gcd(-48, -18), 6)\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef is_lowercase(s):\n    return s.islower()\n```",
        "completion": "```python\nimport unittest\n\nclass TestIsLowercaseFunction(unittest.TestCase):\n    def test_is_lowercase_all_lowercase(self):\n        self.assertTrue(is_lowercase('hello'))\n\n    def test_is_lowercase_mixed_case(self):\n        self.assertFalse(is_lowercase('Hello'))\n\n    def test_is_lowercase_all_uppercase(self):\n        self.assertFalse(is_lowercase('HELLO'))\n\n    def test_is_lowercase_empty_string(self):\n        self.assertFalse(is_lowercase(''))\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef is_empty(s):\n    return len(s) == 0\n```",
        "completion": "```python\nimport unittest\n\nclass TestIsEmptyFunction(unittest.TestCase):\n    def test_is_empty_empty_string(self):\n        self.assertTrue(is_empty(''))\n\n    def test_is_empty_non_empty_string(self):\n        self.assertFalse(is_empty('hello'))\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef is_odd(n):\n    return n % 2 != 0\n```",
        "completion": "```python\nimport unittest\n\nclass TestIsOddFunction(unittest.TestCase):\n    def test_is_odd_positive_odd(self):\n        self.assertTrue(is_odd(3))\n\n    def test_is_odd_positive_even(self):\n        self.assertFalse(is_odd(4))\n\n    def test_is_odd_negative_odd(self):\n        self.assertTrue(is_odd(-3))\n\n    def test_is_odd_negative_even(self):\n        self.assertFalse(is_odd(-4))\n\n    def test_is_odd_zero(self):\n        self.assertFalse(is_odd(0))\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef is_leap_year(year):\n    if year % 4 == 0:\n        if year % 100 == 0:\n            if year % 400 == 0:\n                return True\n            else:\n                return False\n        else:\n            return True\n    else:\n        return False\n```",
        "completion": "```python\nimport unittest\n\nclass TestIsLeapYearFunction(unittest.TestCase):\n    def test_is_leap_year_divisible_by_4_not_100(self):\n        self.assertTrue(is_leap_year(2024))\n\n    def test_is_leap_year_divisible_by_100_not_400(self):\n        self.assertFalse(is_leap_year(1900))\n\n    def test_is_leap_year_divisible_by_400(self):\n        self.assertTrue(is_leap_year(2000))\n\n    def test_is_leap_year_not_divisible_by_4(self):\n        self.assertFalse(is_leap_year(2023))\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef factorial(n):\n    if n == 0:\n        return 1\n    else:\n        return n * factorial(n-1)\n```",
        "completion": "```python\nimport unittest\n\nclass TestFactorialFunction(unittest.TestCase):\n    def test_factorial_zero(self):\n        self.assertEqual(factorial(0), 1)\n\n    def test_factorial_positive_number(self):\n        self.assertEqual(factorial(5), 120)\n\n    def test_factorial_large_number(self):\n        self.assertEqual(factorial(10), 3628800)\n\n    def test_factorial_negative_number(self):\n        with self.assertRaises(RecursionError):\n            factorial(-1)\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef fibonacci(n):\n    if n <= 0:\n        return 0\n    elif n == 1:\n        return 1\n    else:\n        return fibonacci(n-1) + fibonacci(n-2)\n```",
        "completion": "```python\nimport unittest\n\nclass TestFibonacciFunction(unittest.TestCase):\n    def test_fibonacci_zero(self):\n        self.assertEqual(fibonacci(0), 0)\n\n    def test_fibonacci_one(self):\n        self.assertEqual(fibonacci(1), 1)\n\n    def test_fibonacci_positive_number(self):\n        self.assertEqual(fibonacci(5), 5)\n\n    def test_fibonacci_large_number(self):\n        self.assertEqual(fibonacci(10), 55)\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef is_prime(n):\n    if n <= 1:\n        return False\n    for i in range(2, int(n**0.5) + 1):\n        if n % i == 0:\n            return False\n    return True\n```",
        "completion": "```python\nimport unittest\n\nclass TestIsPrimeFunction(unittest.TestCase):\n    def test_is_prime_small_prime(self):\n        self.assertTrue(is_prime(7))\n\n    def test_is_prime_small_non_prime(self):\n        self.assertFalse(is_prime(4))\n\n    def test_is_prime_large_prime(self):\n        self.assertTrue(is_prime(29))\n\n    def test_is_prime_large_non_prime(self):\n        self.assertFalse(is_prime(30))\n\n    def test_is_prime_negative_number(self):\n        self.assertFalse(is_prime(-5))\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef is_even(n):\n    return n % 2 == 0\n```",
        "completion": "```python\nimport unittest\n\nclass TestIsEvenFunction(unittest.TestCase):\n    def test_is_even_positive_number(self):\n        self.assertTrue(is_even(4))\n\n    def test_is_even_negative_number(self):\n        self.assertTrue(is_even(-4))\n\n    def test_is_even_odd_number(self):\n        self.assertFalse(is_even(5))\n\n    def test_is_even_zero(self):\n        self.assertTrue(is_even(0))\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef is_palindrome(s):\n    return s == s[::-1]\n```",
        "completion": "```python\nimport unittest\n\nclass TestIsPalindromeFunction(unittest.TestCase):\n    def test_is_palindrome_even_length(self):\n        self.assertTrue(is_palindrome('abba'))\n\n    def test_is_palindrome_odd_length(self):\n        self.assertTrue(is_palindrome('racecar'))\n\n    def test_is_palindrome_not_palindrome(self):\n        self.assertFalse(is_palindrome('hello'))\n\n    def test_is_palindrome_empty_string(self):\n        self.assertTrue(is_palindrome(''))\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef reverse_string(s):\n    return s[::-1]\n```",
        "completion": "```python\nimport unittest\n\nclass TestReverseStringFunction(unittest.TestCase):\n    def test_reverse_string_regular(self):\n        self.assertEqual(reverse_string('hello'), 'olleh')\n\n    def test_reverse_string_empty(self):\n        self.assertEqual(reverse_string(''), '')\n\n    def test_reverse_string_single_character(self):\n        self.assertEqual(reverse_string('a'), 'a')\n\n    def test_reverse_string_palindrome(self):\n        self.assertEqual(reverse_string('racecar'), 'racecar')\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
        {
        "prompt": "Generate a unit test for this function: \n```python\ndef is_uppercase(s):\n    return s.isupper()\n```",
        "completion": "```python\nimport unittest\n\nclass TestIsUppercaseFunction(unittest.TestCase):\n    def test_is_uppercase_all_uppercase(self):\n        self.assertTrue(is_uppercase('HELLO'))\n\n    def test_is_uppercase_mixed_case(self):\n        self.assertFalse(is_uppercase('Hello'))\n\n    def test_is_uppercase_all_lowercase(self):\n        self.assertFalse(is_uppercase('hello'))\n\n    def test_is_uppercase_empty_string(self):\n        self.assertFalse(is_uppercase(''))\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef is_lowercase(s):\n    return s.islower()\n```",
        "completion": "```python\nimport unittest\n\nclass TestIsLowercaseFunction(unittest.TestCase):\n    def test_is_lowercase_all_lowercase(self):\n        self.assertTrue(is_lowercase('hello'))\n\n    def test_is_lowercase_mixed_case(self):\n        self.assertFalse(is_lowercase('Hello'))\n\n    def test_is_lowercase_all_uppercase(self):\n        self.assertFalse(is_lowercase('HELLO'))\n\n    def test_is_lowercase_empty_string(self):\n        self.assertFalse(is_lowercase(''))\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef is_empty(s):\n    return len(s) == 0\n```",
        "completion": "```python\nimport unittest\n\nclass TestIsEmptyFunction(unittest.TestCase):\n    def test_is_empty_empty_string(self):\n        self.assertTrue(is_empty(''))\n\n    def test_is_empty_non_empty_string(self):\n        self.assertFalse(is_empty('hello'))\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef is_odd(n):\n    return n % 2 != 0\n```",
        "completion": "```python\nimport unittest\n\nclass TestIsOddFunction(unittest.TestCase):\n    def test_is_odd_positive_odd(self):\n        self.assertTrue(is_odd(3))\n\n    def test_is_odd_positive_even(self):\n        self.assertFalse(is_odd(4))\n\n    def test_is_odd_negative_odd(self):\n        self.assertTrue(is_odd(-3))\n\n    def test_is_odd_negative_even(self):\n        self.assertFalse(is_odd(-4))\n\n    def test_is_odd_zero(self):\n        self.assertFalse(is_odd(0))\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef is_leap_year(year):\n    if year % 4 == 0:\n        if year % 100 == 0:\n            if year % 400 == 0:\n                return True\n            else:\n                return False\n        else:\n            return True\n    else:\n        return False\n```",
        "completion": "```python\nimport unittest\n\nclass TestIsLeapYearFunction(unittest.TestCase):\n    def test_is_leap_year_divisible_by_4_not_100(self):\n        self.assertTrue(is_leap_year(2024))\n\n    def test_is_leap_year_divisible_by_100_not_400(self):\n        self.assertFalse(is_leap_year(1900))\n\n    def test_is_leap_year_divisible_by_400(self):\n        self.assertTrue(is_leap_year(2000))\n\n    def test_is_leap_year_not_divisible_by_4(self):\n        self.assertFalse(is_leap_year(2023))\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef gcd(a, b):\n    while b:\n        a, b = b, a % b\n    return a\n```",
        "completion": "```python\nimport unittest\n\nclass TestGcdFunction(unittest.TestCase):\n    def test_gcd_positive_numbers(self):\n        self.assertEqual(gcd(48, 18), 6)\n\n    def test_gcd_one_zero(self):\n        self.assertEqual(gcd(0, 18), 18)\n\n    def test_gcd_both_zeros(self):\n        self.assertEqual(gcd(0, 0), 0)\n\n    def test_gcd_negative_numbers(self):\n        self.assertEqual(gcd(-48, -18), 6)\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef lcm(a, b):\n    if a == 0 or b == 0:\n        return 0\n    else:\n        return abs(a * b) // gcd(a, b)\n```",
        "completion": "```python\nimport unittest\n\nclass TestLcmFunction(unittest.TestCase):\n    def test_lcm_positive_numbers(self):\n        self.assertEqual(lcm(4, 5), 20)\n\n    def test_lcm_one_zero(self):\n        self.assertEqual(lcm(0, 5), 0)\n\n    def test_lcm_both_zeros(self):\n        self.assertEqual(lcm(0, 0), 0)\n\n    def test_lcm_negative_numbers(self):\n        self.assertEqual(lcm(-4, 5), 20)\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef factorial_iterative(n):\n    result = 1\n    for i in range(2, n + 1):\n        result *= i\n    return result\n```",
        "completion": "```python\nimport unittest\n\nclass TestFactorialIterativeFunction(unittest.TestCase):\n    def test_factorial_iterative_zero(self):\n        self.assertEqual(factorial_iterative(0), 1)\n\n    def test_factorial_iterative_positive_number(self):\n        self.assertEqual(factorial_iterative(5), 120)\n\n    def test_factorial_iterative_large_number(self):\n        self.assertEqual(factorial_iterative(10), 3628800)\n\n    def test_factorial_iterative_negative_number(self):\n        with self.assertRaises(ValueError):\n            factorial_iterative(-1)\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef binary_search(arr, target):\n    left, right = 0, len(arr) - 1\n    while left <= right:\n        mid = (left + right) // 2\n        if arr[mid] == target:\n            return mid\n        elif arr[mid] < target:\n            left = mid + 1\n        else:\n            right = mid - 1\n    return -1\n```",
        "completion": "```python\nimport unittest\n\nclass TestBinarySearchFunction(unittest.TestCase):\n    def test_binary_search_found(self):\n        self.assertEqual(binary_search([1, 2, 3, 4, 5], 3), 2)\n\n    def test_binary_search_not_found(self):\n        self.assertEqual(binary_search([1, 2, 3, 4, 5], 6), -1)\n\n    def test_binary_search_empty_list(self):\n        self.assertEqual(binary_search([], 3), -1)\n\n    def test_binary_search_single_element_found(self):\n        self.assertEqual(binary_search([3], 3), 0)\n\n    def test_binary_search_single_element_not_found(self):\n        self.assertEqual(binary_search([3], 4), -1)\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef linear_search(arr, target):\n    for i, value in enumerate(arr):\n        if value == target:\n            return i\n    return -1\n```",
        "completion": "```python\nimport unittest\n\nclass TestLinearSearchFunction(unittest.TestCase):\n    def test_linear_search_found(self):\n        self.assertEqual(linear_search([1, 2, 3, 4, 5], 3), 2)\n\n    def test_linear_search_not_found(self):\n        self.assertEqual(linear_search([1, 2, 3, 4, 5], 6), -1)\n\n    def test_linear_search_empty_list(self):\n        self.assertEqual(linear_search([], 3), -1)\n\n    def test_linear_search_single_element_found(self):\n        self.assertEqual(linear_search([3], 3), 0)\n\n    def test_linear_search_single_element_not_found(self):\n        self.assertEqual(linear_search([3], 4), -1)\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef bubble_sort(arr):\n    n = len(arr)\n    for i in range(n):\n        for j in range(0, n-i-1):\n            if arr[j] > arr[j+1]:\n                arr[j], arr[j+1] = arr[j+1], arr[j]\n    return arr\n```",
        "completion": "```python\nimport unittest\n\nclass TestBubbleSortFunction(unittest.TestCase):\n    def test_bubble_sort_sorted_list(self):\n        self.assertEqual(bubble_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])\n\n    def test_bubble_sort_unsorted_list(self):\n        self.assertEqual(bubble_sort([5, 3, 2, 4, 1]), [1, 2, 3, 4, 5])\n\n    def test_bubble_sort_single_element(self):\n        self.assertEqual(bubble_sort([42]), [42])\n\n    def test_bubble_sort_empty_list(self):\n        self.assertEqual(bubble_sort([]), [])\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef quick_sort(arr):\n    if len(arr) <= 1:\n        return arr\n    pivot = arr[len(arr) // 2]\n    left = [x for x in arr if x < pivot]\n    middle = [x for x in arr if x == pivot]\n    right = [x for x in arr if x > pivot]\n    return quick_sort(left) + middle + quick_sort(right)\n```",
        "completion": "```python\nimport unittest\n\nclass TestQuickSortFunction(unittest.TestCase):\n    def test_quick_sort_sorted_list(self):\n        self.assertEqual(quick_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])\n\n    def test_quick_sort_unsorted_list(self):\n        self.assertEqual(quick_sort([5, 3, 2, 4, 1]), [1, 2, 3, 4, 5])\n\n    def test_quick_sort_single_element(self):\n        self.assertEqual(quick_sort([42]), [42])\n\n    def test_quick_sort_empty_list(self):\n        self.assertEqual(quick_sort([]), [])\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef merge_sort(arr):\n    if len(arr) > 1:\n        mid = len(arr) // 2\n        L = arr[:mid]\n        R = arr[mid:]\n\n        merge_sort(L)\n        merge_sort(R)\n\n        i = j = k = 0\n\n        while i < len(L) and j < len(R):\n            if L[i] < R[j]:\n                arr[k] = L[i]\n                i += 1\n            else:\n                arr[k] = R[j]\n                j += 1\n            k += 1\n\n        while i < len(L):\n            arr[k] = L[i]\n            i += 1\n            k += 1\n\n        while j < len(R):\n            arr[k] = R[j]\n            j += 1\n            k += 1\n    return arr\n```",
        "completion": "```python\nimport unittest\n\nclass TestMergeSortFunction(unittest.TestCase):\n    def test_merge_sort_sorted_list(self):\n        self.assertEqual(merge_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])\n\n    def test_merge_sort_unsorted_list(self):\n        self.assertEqual(merge_sort([5, 3, 2, 4, 1]), [1, 2, 3, 4, 5])\n\n    def test_merge_sort_single_element(self):\n        self.assertEqual(merge_sort([42]), [42])\n\n    def test_merge_sort_empty_list(self):\n        self.assertEqual(merge_sort([]), [])\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
       {
        "prompt": "Generate a unit test for this function: \n```python\ndef is_palindrome_number(n):\n    return str(n) == str(n)[::-1]\n```",
        "completion": "```python\nimport unittest\n\nclass TestIsPalindromeNumberFunction(unittest.TestCase):\n    def test_is_palindrome_number_positive(self):\n        self.assertTrue(is_palindrome_number(121))\n\n    def test_is_palindrome_number_negative(self):\n        self.assertFalse(is_palindrome_number(-121))\n\n    def test_is_palindrome_number_not_palindrome(self):\n        self.assertFalse(is_palindrome_number(123))\n\n    def test_is_palindrome_number_single_digit(self):\n        self.assertTrue(is_palindrome_number(7))\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef is_armstrong_number(n):\n    num_str = str(n)\n    num_len = len(num_str)\n    return n == sum(int(digit) ** num_len for digit in num_str)\n```",
        "completion": "```python\nimport unittest\n\nclass TestIsArmstrongNumberFunction(unittest.TestCase):\n    def test_is_armstrong_number_positive(self):\n        self.assertTrue(is_armstrong_number(153))\n\n    def test_is_armstrong_number_negative(self):\n        self.assertFalse(is_armstrong_number(123))\n\n    def test_is_armstrong_number_single_digit(self):\n        self.assertTrue(is_armstrong_number(5))\n\n    def test_is_armstrong_number_large_number(self):\n        self.assertTrue(is_armstrong_number(9474))\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef is_perfect_square(n):\n    return int(n**0.5) ** 2 == n\n```",
        "completion": "```python\nimport unittest\n\nclass TestIsPerfectSquareFunction(unittest.TestCase):\n    def test_is_perfect_square_positive(self):\n        self.assertTrue(is_perfect_square(16))\n\n    def test_is_perfect_square_negative(self):\n        self.assertFalse(is_perfect_square(15))\n\n    def test_is_perfect_square_zero(self):\n        self.assertTrue(is_perfect_square(0))\n\n    def test_is_perfect_square_large_number(self):\n        self.assertTrue(is_perfect_square(10000))\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef is_perfect_number(n):\n    return n == sum(i for i in range(1, n) if n % i == 0)\n```",
        "completion": "```python\nimport unittest\n\nclass TestIsPerfectNumberFunction(unittest.TestCase):\n    def test_is_perfect_number_positive(self):\n        self.assertTrue(is_perfect_number(6))\n\n    def test_is_perfect_number_negative(self):\n        self.assertFalse(is_perfect_number(10))\n\n    def test_is_perfect_number_large_number(self):\n        self.assertTrue(is_perfect_number(28))\n\n    def test_is_perfect_number_non_perfect(self):\n        self.assertFalse(is_perfect_number(12))\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef is_fibonacci_number(n):\n    x1 = 5 * n * n + 4\n    x2 = 5 * n * n - 4\n    return int(x1**0.5) ** 2 == x1 or int(x2**0.5) ** 2 == x2\n```",
        "completion": "```python\nimport unittest\n\nclass TestIsFibonacciNumberFunction(unittest.TestCase):\n    def test_is_fibonacci_number_positive(self):\n        self.assertTrue(is_fibonacci_number(8))\n\n    def test_is_fibonacci_number_negative(self):\n        self.assertFalse(is_fibonacci_number(10))\n\n    def test_is_fibonacci_number_zero(self):\n        self.assertTrue(is_fibonacci_number(0))\n\n    def test_is_fibonacci_number_large_number(self):\n        self.assertTrue(is_fibonacci_number(144))\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef is_happy_number(n):\n    seen = set()\n    while n != 1 and n not in seen:\n        seen.add(n)\n        n = sum(int(digit) ** 2 for digit in str(n))\n    return n == 1\n```",
        "completion": "```python\nimport unittest\n\nclass TestIsHappyNumberFunction(unittest.TestCase):\n    def test_is_happy_number_positive(self):\n        self.assertTrue(is_happy_number(19))\n\n    def test_is_happy_number_negative(self):\n        self.assertFalse(is_happy_number(20))\n\n    def test_is_happy_number_single_digit(self):\n        self.assertTrue(is_happy_number(1))\n\n    def test_is_happy_number_large_number(self):\n        self.assertTrue(is_happy_number(100))\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef is_pangram(s):\n    return set('abcdefghijklmnopqrstuvwxyz') <= set(s.lower())\n```",
        "completion": "```python\nimport unittest\n\nclass TestIsPangramFunction(unittest.TestCase):\n    def test_is_pangram_positive(self):\n        self.assertTrue(is_pangram('The quick brown fox jumps over the lazy dog'))\n\n    def test_is_pangram_negative(self):\n        self.assertFalse(is_pangram('Hello world'))\n\n    def test_is_pangram_empty_string(self):\n        self.assertFalse(is_pangram(''))\n\n    def test_is_pangram_missing_letters(self):\n        self.assertFalse(is_pangram('The quick brown fox jumps over the lazy'))\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef is_substring(s1, s2):\n    return s1 in s2\n```",
        "completion": "```python\nimport unittest\n\nclass TestIsSubstringFunction(unittest.TestCase):\n    def test_is_substring_positive(self):\n        self.assertTrue(is_substring('hello', 'hello world'))\n\n    def test_is_substring_negative(self):\n        self.assertFalse(is_substring('world', 'hello'))\n\n    def test_is_substring_empty_string(self):\n        self.assertTrue(is_substring('', 'hello'))\n\n    def test_is_substring_same_string(self):\n        self.assertTrue(is_substring('hello', 'hello'))\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef is_valid_parentheses(s):\n    stack = []\n    mapping = {')': '(', '}': '{', ']': '['}\n    for char in s:\n        if char in mapping:\n            top_element = stack.pop() if stack else '#'\n            if mapping[char] != top_element:\n                return False\n        else:\n            stack.append(char)\n    return not stack\n```",
        "completion": "```python\nimport unittest\n\nclass TestIsValidParenthesesFunction(unittest.TestCase):\n    def test_is_valid_parentheses_positive(self):\n        self.assertTrue(is_valid_parentheses('()'))\n\n    def test_is_valid_parentheses_negative(self):\n        self.assertFalse(is_valid_parentheses('([)]'))\n\n    def test_is_valid_parentheses_empty_string(self):\n        self.assertTrue(is_valid_parentheses(''))\n\n    def test_is_valid_parentheses_mixed(self):\n        self.assertTrue(is_valid_parentheses('{[]}'))\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef is_valid_email(email):\n    import re\n    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$'\n    return re.match(pattern, email) is not None\n```",
        "completion": "```python\nimport unittest\n\nclass TestIsValidEmailFunction(unittest.TestCase):\n    def test_is_valid_email_positive(self):\n        self.assertTrue(is_valid_email('test@example.com'))\n\n    def test_is_valid_email_negative(self):\n        self.assertFalse(is_valid_email('test@.com'))\n\n    def test_is_valid_email_missing_at(self):\n        self.assertFalse(is_valid_email('testexample.com'))\n\n    def test_is_valid_email_missing_domain(self):\n        self.assertFalse(is_valid_email('test@com'))\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef is_valid_url(url):\n    import re\n    pattern = re.compile(\n        r'^(?:http|ftp)s?://' # http:// or https://\n        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\\.)+(?:[A-Z]{2,6}\\.?|[A-Z0-9-]{2,}\\.?))' # domain...\n        r'(?:/?|[/?]\\S+)$', re.IGNORECASE)\n    return re.match(pattern, url) is not None\n```",
        "completion": "```python\nimport unittest\n\nclass TestIsValidUrlFunction(unittest.TestCase):\n    def test_is_valid_url_positive(self):\n        self.assertTrue(is_valid_url('http://example.com'))\n\n    def test_is_valid_url_negative(self):\n        self.assertFalse(is_valid_url('example.com'))\n\n    def test_is_valid_url_missing_protocol(self):\n        self.assertFalse(is_valid_url('www.example.com'))\n\n    def test_is_valid_url_ftp(self):\n        self.assertTrue(is_valid_url('ftp://example.com'))\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef is_valid_ip(ip):\n    import re\n    pattern = re.compile(\n        r'^(?:[0-9]{1,3}\\.){3}[0-9]{1,3}$'\n    )\n    return re.match(pattern, ip) is not None and all(0 <= int(num) <= 255 for num in ip.split('.'))\n```",
        "completion": "```python\nimport unittest\n\nclass TestIsValidIpFunction(unittest.TestCase):\n    def test_is_valid_ip_positive(self):\n        self.assertTrue(is_valid_ip('192.168.0.1'))\n\n    def test_is_valid_ip_negative(self):\n        self.assertFalse(is_valid_ip('256.256.256.256'))\n\n    def test_is_valid_ip_missing_octet(self):\n        self.assertFalse(is_valid_ip('192.168.0'))\n\n    def test_is_valid_ip_extra_octet(self):\n        self.assertFalse(is_valid_ip('192.168.0.1.1'))\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef is_valid_credit_card(number):\n    number = str(number)\n    total = 0\n    reverse_digits = number[::-1]\n    for i, digit in enumerate(reverse_digits):\n        n = int(digit)\n        if i % 2 == 1:\n            n *= 2\n            if n > 9:\n                n -= 9\n        total += n\n    return total % 10 == 0\n```",
        "completion": "```python\nimport unittest\n\nclass TestIsValidCreditCardFunction(unittest.TestCase):\n    def test_is_valid_credit_card_positive(self):\n        self.assertTrue(is_valid_credit_card('4532015112830366'))\n\n    def test_is_valid_credit_card_negative(self):\n        self.assertFalse(is_valid_credit_card('1234567812345670'))\n\n    def test_is_valid_credit_card_short_number(self):\n        self.assertFalse(is_valid_credit_card('1234'))\n\n    def test_is_valid_credit_card_non_digit(self):\n        self.assertFalse(is_valid_credit_card('4532a15112830366'))\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef is_valid_ssn(ssn):\n    if len(ssn) != 11:\n        return False\n    for i in range(0, 3):\n        if not ssn[i].isdigit():\n            return False\n    if ssn[3] != '-':\n        return False\n    for i in range(4, 6):\n        if not ssn[i].isdigit():\n            return False\n    if ssn[6] != '-':\n        return False\n    for i in range(7, 11):\n        if not ssn[i].isdigit():\n            return False\n    return True\n```",
        "completion": "```python\nimport unittest\n\nclass TestIsValidSsnFunction(unittest.TestCase):\n    def test_is_valid_ssn_positive(self):\n        self.assertTrue(is_valid_ssn('123-45-6789'))\n\n    def test_is_valid_ssn_negative(self):\n        self.assertFalse(is_valid_ssn('123-45-678'))\n\n    def test_is_valid_ssn_invalid_delimiter(self):\n        self.assertFalse(is_valid_ssn('123.45.6789'))\n\n    def test_is_valid_ssn_invalid_character(self):\n        self.assertFalse(is_valid_ssn('123-45-678X'))\n\n    def test_is_valid_ssn_invalid_length(self):\n        self.assertFalse(is_valid_ssn('1234-45-6789'))\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef is_valid_phone_number(phone_number):\n    import re\n    pattern = re.compile(r'^\\+?1?\\d{9,15}$')\n    return pattern.match(phone_number) is not None\n```",
        "completion": "```python\nimport unittest\n\nclass TestIsValidPhoneNumberFunction(unittest.TestCase):\n    def test_is_valid_phone_number_positive(self):\n        self.assertTrue(is_valid_phone_number('+1234567890'))\n\n    def test_is_valid_phone_number_negative(self):\n        self.assertFalse(is_valid_phone_number('+123456789'))\n\n    def test_is_valid_phone_number_no_country_code(self):\n        self.assertTrue(is_valid_phone_number('1234567890'))\n\n    def test_is_valid_phone_number_invalid_character(self):\n        self.assertFalse(is_valid_phone_number('+1234567890a'))\n\n    def test_is_valid_phone_number_too_long(self):\n        self.assertFalse(is_valid_phone_number('+12345678901234567'))\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef is_valid_date(date):\n    import re\n    pattern = re.compile(r'^\\d{4}-\\d{2}-\\d{2}$')\n    if not pattern.match(date):\n        return False\n    year, month, day = map(int, date.split('-'))\n    if month < 1 or month > 12:\n        return False\n    if day < 1 or day > 31:\n        return False\n    if month in [4, 6, 9, 11] and day > 30:\n        return False\n    if month == 2:\n        if is_leap_year(year) and day > 29:\n            return False\n        if not is_leap_year(year) and day > 28:\n            return False\n    return True\n```",
        "completion": "```python\nimport unittest\n\nclass TestIsValidDateFunction(unittest.TestCase):\n    def test_is_valid_date_positive(self):\n        self.assertTrue(is_valid_date('2023-05-17'))\n\n    def test_is_valid_date_negative(self):\n        self.assertFalse(is_valid_date('2023-13-17'))\n\n    def test_is_valid_date_invalid_format(self):\n        self.assertFalse(is_valid_date('2023/05/17'))\n\n    def test_is_valid_date_invalid_day(self):\n        self.assertFalse(is_valid_date('2023-05-32'))\n\n    def test_is_valid_date_leap_year(self):\n        self.assertTrue(is_valid_date('2024-02-29'))\n\n    def test_is_valid_date_non_leap_year(self):\n        self.assertFalse(is_valid_date('2023-02-29'))\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef is_valid_hex_color(color):\n    import re\n    pattern = re.compile(r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$')\n    return pattern.match(color) is not None\n```",
        "completion": "```python\nimport unittest\n\nclass TestIsValidHexColorFunction(unittest.TestCase):\n    def test_is_valid_hex_color_positive_six_digits(self):\n        self.assertTrue(is_valid_hex_color('#FF0000'))\n\n    def test_is_valid_hex_color_positive_three_digits(self):\n        self.assertTrue(is_valid_hex_color('#F00'))\n\n    def test_is_valid_hex_color_negative_invalid_character(self):\n        self.assertFalse(is_valid_hex_color('#FF00GG'))\n\n    def test_is_valid_hex_color_negative_missing_hash(self):\n        self.assertFalse(is_valid_hex_color('FF0000'))\n\n    def test_is_valid_hex_color_negative_invalid_length(self):\n        self.assertFalse(is_valid_hex_color('#FF00'))\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef is_valid_password(password):\n    import re\n    pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)(?=.*[@$!%*?&])[A-Za-z\\d@$!%*?&]{8,}$')\n    return pattern.match(password) is not None\n```",
        "completion": "```python\nimport unittest\n\nclass TestIsValidPasswordFunction(unittest.TestCase):\n    def test_is_valid_password_positive(self):\n        self.assertTrue(is_valid_password('Abcdef1@'))\n\n    def test_is_valid_password_negative_missing_lowercase(self):\n        self.assertFalse(is_valid_password('ABCDEF1@'))\n\n    def test_is_valid_password_negative_missing_uppercase(self):\n        self.assertFalse(is_valid_password('abcdef1@'))\n\n    def test_is_valid_password_negative_missing_digit(self):\n        self.assertFalse(is_valid_password('Abcdefg@'))\n\n    def test_is_valid_password_negative_missing_special_char(self):\n        self.assertFalse(is_valid_password('Abcdef12'))\n\n    def test_is_valid_password_negative_too_short(self):\n        self.assertFalse(is_valid_password('Abc1@'))\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef is_valid_uuid(uuid):\n    import re\n    pattern = re.compile(r'^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$', re.I)\n    return pattern.match(uuid) is not None\n```",
        "completion": "```python\nimport unittest\n\nclass TestIsValidUuidFunction(unittest.TestCase):\n    def test_is_valid_uuid_positive(self):\n        self.assertTrue(is_valid_uuid('123e4567-e89b-12d3-a456-426655440000'))\n\n    def test_is_valid_uuid_negative_invalid_version(self):\n        self.assertFalse(is_valid_uuid('123e4567-e89b-02d3-a456-426655440000'))\n\n    def test_is_valid_uuid_negative_invalid_variant(self):\n        self.assertFalse(is_valid_uuid('123e4567-e89b-12d3-c456-426655440000'))\n\n    def test_is_valid_uuid_negative_invalid_format(self):\n        self.assertFalse(is_valid_uuid('123e4567e89b12d3a456426655440000'))\n\n    def test_is_valid_uuid_negative_invalid_character(self):\n        self.assertFalse(is_valid_uuid('123e4567-e89b-12d3-a456-42665544000g'))\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef is_valid_json(json_string):\n    import json\n    try:\n        json.loads(json_string)\n    except ValueError:\n        return False\n    return True\n```",
        "completion": "```python\nimport unittest\n\nclass TestIsValidJsonFunction(unittest.TestCase):\n    def test_is_valid_json_positive(self):\n        self.assertTrue(is_valid_json('{\"name\": \"John\", \"age\": 30}'))\n\n    def test_is_valid_json_negative_invalid_syntax(self):\n        self.assertFalse(is_valid_json('{\"name\": \"John\", \"age\": 30'))\n\n    def test_is_valid_json_negative_empty_string(self):\n        self.assertFalse(is_valid_json(''))\n\n    def test_is_valid_json_positive_empty_object(self):\n        self.assertTrue(is_valid_json('{}'))\n\n    def test_is_valid_json_positive_empty_array(self):\n        self.assertTrue(is_valid_json('[]'))\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    }
]

validation_data= [
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef add(a, b):\n    return a + b\n```",
        "completion": "```python\nimport unittest\n\nclass TestAddFunction(unittest.TestCase):\n    def test_add_positive_numbers(self):\n        self.assertEqual(add(2, 3), 5)\n\n    def test_add_negative_numbers(self):\n        self.assertEqual(add(-1, -1), -2)\n\n    def test_add_positive_and_negative_numbers(self):\n        self.assertEqual(add(-1, 1), 0)\n\n    def test_add_zero(self):\n        self.assertEqual(add(0, 0), 0)\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef multiply(a, b):\n    return a * b\n```",
        "completion": "```python\nimport unittest\n\nclass TestMultiplyFunction(unittest.TestCase):\n    def test_multiply_positive_numbers(self):\n        self.assertEqual(multiply(2, 3), 6)\n\n    def test_multiply_negative_numbers(self):\n        self.assertEqual(multiply(-1, -1), 1)\n\n    def test_multiply_positive_and_negative_numbers(self):\n        self.assertEqual(multiply(-1, 1), -1)\n\n    def test_multiply_by_zero(self):\n        self.assertEqual(multiply(0, 5), 0)\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef divide(a, b):\n    if b == 0:\n        raise ValueError('Cannot divide by zero')\n    return a / b\n```",
        "completion": "```python\nimport unittest\n\nclass TestDivideFunction(unittest.TestCase):\n    def test_divide_positive_numbers(self):\n        self.assertEqual(divide(6, 3), 2)\n\n    def test_divide_negative_numbers(self):\n        self.assertEqual(divide(-6, -3), 2)\n\n    def test_divide_positive_and_negative_numbers(self):\n        self.assertEqual(divide(-6, 3), -2)\n\n    def test_divide_by_zero(self):\n        with self.assertRaises(ValueError):\n            divide(6, 0)\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef subtract(a, b):\n    return a - b\n```",
        "completion": "```python\nimport unittest\n\nclass TestSubtractFunction(unittest.TestCase):\n    def test_subtract_positive_numbers(self):\n        self.assertEqual(subtract(5, 3), 2)\n\n    def test_subtract_negative_numbers(self):\n        self.assertEqual(subtract(-5, -3), -2)\n\n    def test_subtract_positive_and_negative_numbers(self):\n        self.assertEqual(subtract(-5, 3), -8)\n\n    def test_subtract_zero(self):\n        self.assertEqual(subtract(0, 0), 0)\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef is_pangram(s):\n    return set('abcdefghijklmnopqrstuvwxyz') <= set(s.lower())\n```",
        "completion": "```python\nimport unittest\n\nclass TestIsPangramFunction(unittest.TestCase):\n    def test_is_pangram_positive(self):\n        self.assertTrue(is_pangram('The quick brown fox jumps over the lazy dog'))\n\n    def test_is_pangram_negative(self):\n        self.assertFalse(is_pangram('Hello world'))\n\n    def test_is_pangram_empty_string(self):\n        self.assertFalse(is_pangram(''))\n\n    def test_is_pangram_missing_letters(self):\n        self.assertFalse(is_pangram('The quick brown fox jumps over the lazy'))\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef is_substring(s1, s2):\n    return s1 in s2\n```",
        "completion": "```python\nimport unittest\n\nclass TestIsSubstringFunction(unittest.TestCase):\n    def test_is_substring_positive(self):\n        self.assertTrue(is_substring('hello', 'hello world'))\n\n    def test_is_substring_negative(self):\n        self.assertFalse(is_substring('world', 'hello'))\n\n    def test_is_substring_empty_string(self):\n        self.assertTrue(is_substring('', 'hello'))\n\n    def test_is_substring_same_string(self):\n        self.assertTrue(is_substring('hello', 'hello'))\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },    
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef is_valid_roman_numeral(s):\n    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}\n    total = 0\n    prev_value = 0\n    for char in s[::-1]:\n        curr_value = roman_numerals[char]\n        if curr_value < prev_value:\n            total -= curr_value\n        else:\n            total += curr_value\n        prev_value = curr_value\n    return total > 0\n```",
        "completion": "```python\nimport unittest\n\nclass TestIsValidRomanNumeralFunction(unittest.TestCase):\n    def test_is_valid_roman_numeral_positive(self):\n        self.assertTrue(is_valid_roman_numeral('XIV'))\n\n    def test_is_valid_roman_numeral_negative(self):\n        self.assertFalse(is_valid_roman_numeral('IIII'))\n\n    def test_is_valid_roman_numeral_empty_string(self):\n        self.assertFalse(is_valid_roman_numeral(''))\n\n    def test_is_valid_roman_numeral_invalid_character(self):\n        self.assertFalse(is_valid_roman_numeral('XIVY'))\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef is_valid_isbn(isbn):\n    isbn = isbn.replace('-', '')\n    if len(isbn) != 10:\n        return False\n    total = 0\n    for i in range(9):\n        if not isbn[i].isdigit():\n            return False\n        total += int(isbn[i]) * (10 - i)\n    if isbn[9] != 'X' and not isbn[9].isdigit():\n        return False\n    if isbn[9] == 'X':\n        total += 10\n    else:\n        total += int(isbn[9])\n    return total % 11 == 0\n```",
        "completion": "```python\nimport unittest\n\nclass TestIsValidIsbnFunction(unittest.TestCase):\n    def test_is_valid_isbn_positive(self):\n        self.assertTrue(is_valid_isbn('0-306-40615-2'))\n\n    def test_is_valid_isbn_negative(self):\n        self.assertFalse(is_valid_isbn('0-306-40615-1'))\n\n    def test_is_valid_isbn_x_check_digit(self):\n        self.assertTrue(is_valid_isbn('0-306-40615-X'))\n\n    def test_is_valid_isbn_invalid_length(self):\n        self.assertFalse(is_valid_isbn('0-306-40615-22'))\n\n    def test_is_valid_isbn_invalid_character(self):\n        self.assertFalse(is_valid_isbn('0-306-4061A-2'))\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef lcm(a, b):\n    if a == 0 or b == 0:\n        return 0\n    else:\n        return abs(a * b) // gcd(a, b)\n```",
        "completion": "```python\nimport unittest\n\nclass TestLcmFunction(unittest.TestCase):\n    def test_lcm_positive_numbers(self):\n        self.assertEqual(lcm(4, 5), 20)\n\n    def test_lcm_one_zero(self):\n        self.assertEqual(lcm(0, 5), 0)\n\n    def test_lcm_both_zeros(self):\n        self.assertEqual(lcm(0, 0), 0)\n\n    def test_lcm_negative_numbers(self):\n        self.assertEqual(lcm(-4, 5), 20)\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef is_uppercase(s):\n    return s.isupper()\n```",
        "completion": "```python\nimport unittest\n\nclass TestIsUppercaseFunction(unittest.TestCase):\n    def test_is_uppercase_all_uppercase(self):\n        self.assertTrue(is_uppercase('HELLO'))\n\n    def test_is_uppercase_mixed_case(self):\n        self.assertFalse(is_uppercase('Hello'))\n\n    def test_is_uppercase_all_lowercase(self):\n        self.assertFalse(is_uppercase('hello'))\n\n    def test_is_uppercase_empty_string(self):\n        self.assertFalse(is_uppercase(''))\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef sum_list(arr):\n    return sum(arr)\n```",
        "completion": "```python\nimport unittest\n\nclass TestSumListFunction(unittest.TestCase):\n    def test_sum_list_positive_numbers(self):\n        self.assertEqual(sum_list([1, 2, 3, 4, 5]), 15)\n\n    def test_sum_list_negative_numbers(self):\n        self.assertEqual(sum_list([-1, -2, -3, -4, -5]), -15)\n\n    def test_sum_list_mixed_numbers(self):\n        self.assertEqual(sum_list([-1, 0, 1, 2, 3]), 5)\n\n    def test_sum_list_empty_list(self):\n        self.assertEqual(sum_list([]), 0)\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    },
    {
        "prompt": "Generate a unit test for this function: \n```python\ndef average_list(arr):\n    return sum(arr) / len(arr) if arr else 0\n```",
        "completion": "```python\nimport unittest\n\nclass TestAverageListFunction(unittest.TestCase):\n    def test_average_list_positive_numbers(self):\n        self.assertAlmostEqual(average_list([1, 2, 3, 4, 5]), 3.0, places=7)\n\n    def test_average_list_negative_numbers(self):\n        self.assertAlmostEqual(average_list([-1, -2, -3, -4, -5]), -3.0, places=7)\n\n    def test_average_list_mixed_numbers(self):\n        self.assertAlmostEqual(average_list([-1, 0, 1, 2, 3]), 1.0, places=7)\n\n    def test_average_list_empty_list(self):\n        self.assertEqual(average_list([]), 0)\n\nif __name__ == '__main__':\n    unittest.main()\n```"
    }
]
