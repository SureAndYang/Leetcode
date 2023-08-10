#!/usr/bin/python3

""" Medium: Longest Substring Without Repeating Characters
Given a string `s`, find the length of the longest substring without repeating characters.

Ex.
Input: s = 'abcabcbb'
Output: 3
Explanation: The answer is "abc" (or "bca", "cab"), with the length of 3.
"""
class Solution:

    # Runtime 98.31%, Memory: 48.53%. Same idea with the best while code a bit different.
    def lengthOfLongestSubstring_1(self, s: str) -> int:
        if len(s) == 0:
            return 0

        char_index = {s[0]: 0}
        i, j = 0, 1
        max_len = 1
        while j < len(s):
            if s[j] in char_index and char_index[s[j]] >= i:
                if j - i > max_len:
                    # `j - i` means the length from 'i' to 'j-1'.
                    max_len = j - i
                i = char_index[s[j]] + 1
            char_index[s[j]] = j
            j += 1

        # In case, all characters in the string are all different.
        return max_len if max_len > j - i else j - i
