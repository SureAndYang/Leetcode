#!/usr/bin/python3

""" Easy: Find the index of the First Occurrence in a String.

Given two strings needle and haystack, return the index of the first occurrence of needle in
haystack, or -1 if needle is not part of haystack.

"""

class Solution:

    """Runtime 85.75%, Memory 92.77%"""
    def strStr(self, haystack: str, needle: str) -> int:
        l = len(needle)
        for i in range(len(haystack)-l+1):
            if haystack[i:i+l] == needle:
                return i
        return -1
