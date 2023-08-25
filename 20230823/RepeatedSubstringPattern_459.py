#!/usr/bin/python3

""" Easy: Repeated Substring Pattern, https://leetcode.com/problems/repeated-substring-pattern/

Given a string s, check if it can be constructed by taking a substring of it and appending multiple
copies of the substring together.
"""

class Solution:

    """Runtime 39.52%, Memory 13.65%"""
    def repeatedSubstringPattern_1(self, s: str) -> bool:
        if len(s) == 1:
            return False

        last_char = s[-1]
        for i, char in enumerate(s):
            if i >= len(s) / 2:
                break

            if char == last_char and len(s) % (i+1) == 0:
                mul = len(s) // (i+1)
                if s[:i+1] * mul == s:
                    return True
        return False

    """Runtime 37.99%, Memory 94.58%
    Same solution with 1, but removed unnecessary variables to reduce memory consuming.
    """
    def repeatedSubstringPattern_2(self, s: str) -> bool:
        if len(s) == 1:
            return False

        for i, char in enumerate(s):
            if i >= len(s) / 2:
                break

            if char == s[-1] and len(s) % (i+1) == 0:
                if s[:i+1] * (len(s)//(i+1)) == s:
                    return True
        return False


    """From other author"""
    def repeatedSubstringPattern_3(self, s: str) -> bool:
        return s in (s + s)[1:-1]
