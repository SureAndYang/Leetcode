#!/usr/bin/python3

""" Easy: Is Subsequence.
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some
(can be none) of the characters without disturbing the relative positions of the remaining
characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
"""

class Solution:
    """Runtime 62.76%, Memory 88.88%.

    Somehow this is the best solution. A same one is claimed as 'beat 100%' by other author.
    """
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)
