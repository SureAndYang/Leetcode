#!/usr/bin/python3

""" Medium: Longest Palindromic Substring
Given a string s, return the longest palindromic substring in s.
"""

class Solution:

    # Runtime 34.70%, Memory 28.13%.
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        # 2-dimension DP.
        longest_substr = s[0]
        matrix = [[0]*len(s), [1]*len(s)]
        for length in range(2, len(s)+1):
            for start in range(len(s)-length+1):
                if s[start] == s[start+length-1] and matrix[length%2][start+1]==length-2:
                    matrix[length%2][start] = length
                    longest_substr = s[start:start+length]
        return longest_substr


