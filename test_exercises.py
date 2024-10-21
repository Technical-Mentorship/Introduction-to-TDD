import unittest

import exercises

class TestNumberGame(unittest.TestCase):
    def test_reverse_list(self):
        self.assertEqual(exercises.reverse_list([1, 2, 3, 4, 5]), [5, 4, 3, 2, 1])
        self.assertEqual(exercises.reverse_list([]), [])
        self.assertEqual(exercises.reverse_list([7]), [7])

    def test_reverse_string(self):
        self.assertEqual(exercises.reverse_string("foobar"), "raboof")
        self.assertEqual(exercises.reverse_string(""), "")
        self.assertEqual(exercises.reverse_string("a"), "a")

    def test_is_english_vowel(self):
        self.assertTrue(exercises.is_english_vowel('a'))
        self.assertTrue(exercises.is_english_vowel('E'))
        self.assertFalse(exercises.is_english_vowel('z'))
        self.assertFalse(exercises.is_english_vowel('K'))

    def test_count_vowels(self):
        self.assertEqual(exercises.count_vowels("hello world"), 3)
        self.assertEqual(exercises.count_vowels("xyz"), 0)
        self.assertEqual(exercises.count_vowels("aeiou"), 5)

    def test_is_palindrome(self):
        self.assertTrue(exercises.is_palindrome("racecar"))
        self.assertTrue(exercises.is_palindrome("A man a plan a canal Panama"))
        self.assertFalse(exercises.is_palindrome("hello"))
        self.assertTrue(exercises.is_palindrome(""))

    def test_find_minimum(self):
        self.assertEqual(exercises.find_minimum([4, 2, 9, 1, 5]), 1)
        self.assertEqual(exercises.find_minimum([10, -2, 3, 99]), -2)
        self.assertEqual(exercises.find_minimum([42]), 42)

    def test_sum_numbers(self):
        self.assertEqual(exercises.sum_numbers([1, 2, 3, 4, 5]), 15)
        self.assertEqual(exercises.sum_numbers([]), 0)
        self.assertEqual(exercises.sum_numbers([10, 20, 30]), 60)

    def test_factorial(self):
        self.assertEqual(exercises.factorial(5), 120)
        self.assertEqual(exercises.factorial(0), 1)
        self.assertEqual(exercises.factorial(3), 6)

if __name__ == '__main__':
    unittest.main()
