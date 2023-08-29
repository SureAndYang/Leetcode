#!/usr/bin/python3

""" Easy: Length of Last Word
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.
"""

class Solution:
    """Runtime 67.56%, Memory 53.45%"""
    def lengthOfLastWord(self, s: str) -> int:
        res, l = 0, 0
        for char in s:
            if char == " ":
                res, l = l or res, 0
            else:
                l += 1
        return l or res
