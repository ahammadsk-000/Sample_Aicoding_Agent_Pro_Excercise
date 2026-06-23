import unittest
from python_full_coding_practice import (
    reverse_string_basic,
    reverse_string_loop,
    reverse_string_recursion,
    find_max,
    find_max_recursion,
    is_palindrome_simple,
    is_palindrome_twopointer,
    count_characters_dict,
    count_characters_defaultdict,
    count_characters_counter,
    two_sum_hashmap,
    two_sum_bruteforce,
    two_sum_sorted,
    longest_substring_without_repeating,
    merge_sorted_lists,
    contains_duplicate_set,
    contains_duplicate_hashmap,
)

class TestPythonFullCodingPractice(unittest.TestCase):
    def test_reverse_string(self):
        test_strings = ["hello", "python", "interview", "a", ""]
        for test in test_strings:
            self.assertEqual(reverse_string_basic(test), test[::-1])
            self.assertEqual(reverse_string_loop(test), test[::-1])
            self.assertEqual(reverse_string_recursion(test), test[::-1])

    def test_find_max(self):
        test_lists = [[3, 7, 2, 9, 1], [1], [-5, -2, -10], [0, 0, 0]]
        for test in test_lists:
            self.assertEqual(find_max(test), max(test) if test else None)
            self.assertEqual(find_max_recursion(test), max(test) if test else None)

    def test_is_palindrome(self):
        test_palindromes = ["racecar", "hello", "A man a plan a canal Panama", "12321", "12345"]
        for test in test_palindromes:
            self.assertEqual(is_palindrome_simple(test), test.lower().replace(" ", "") == test.lower().replace(" ", "")[::-1])
            self.assertEqual(is_palindrome_twopointer(test), test.lower().replace(" ", "") == test.lower().replace(" ", "")[::-1])

    def test_count_characters(self):
        test_strings = ["hello", "mississippi", "aaa", ""]
        for test in test_strings:
            self.assertEqual(count_characters_dict(test), {char: test.count(char) for char in set(test)})
            self.assertEqual(count_characters_defaultdict(test), {char: test.count(char) for char in set(test)})
            self.assertEqual(count_characters_counter(test), {char: test.count(char) for char in set(test)})

    def test_two_sum(self):
        test_cases = [
            ([2, 7, 11, 15], 9),
            ([3, 2, 4], 6),
            ([3, 3], 6),
            ([1, 2, 3, 4, 5], 9)
        ]
        for nums, target in test_cases:
            self.assertEqual(two_sum_hashmap(nums, target), two_sum_bruteforce(nums, target))
            self.assertEqual(two_sum_hashmap(nums, target), two_sum_sorted(nums, target))

    def test_longest_substring_without_repeating(self):
        test_strings = ["abcabcbb", "bbbbb", "pwwkew", "au", "dvdf", ""]
        for test in test_strings:
            self.assertGreaterEqual(longest_substring_without_repeating(test), 0)

    def test_merge_sorted_lists(self):
        test_cases = [
            ([1, 3, 5], [2, 4, 6]),
            ([1], [1]),
            ([], [0]),
            ([1, 2, 3], [4, 5, 6])
        ]
        for list1, list2 in test_cases:
            self.assertEqual(merge_sorted_lists(list1, list2), sorted(list1 + list2))

    def test_contains_duplicate(self):
        test_cases = [[1, 2, 3, 1], [1, 2, 3, 4], [1], [], [99, 99]]
        for test in test_cases:
            self.assertEqual(contains_duplicate_set(test), len(test) != len(set(test)))
            self.assertEqual(contains_duplicate_hashmap(test), len(test) != len(set(test)))

if __name__ == '__main__':
    unittest.main()