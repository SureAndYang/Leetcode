#!/usr/bin/python3

""" Easy: Merge Strings Alternately
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order,
starting with word1. If a string is longer than the other, append the additional letters onto the
end of the merged string.

Return the merged string.
"""

class Solution:
    """Runtime 69.90%, Memory 34.48%"""
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        min_len = min(len(word1), len(word2))
        for i in range(min_len):
            res.append(word1[i])
            res.append(word2[i])
        return ''.join(res) + (word1[min_len:] or word2[min_len:])


    """Runtime 86.52%, Memory 70.13%"""
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        """Small change here makes big difference !"""
        min_len = len(word1) if len(word1) < len(word2) else len(word2)
        for i in range(min_len):
            res.append(word1[i])
            res.append(word2[i])
        return ''.join(res) + (word1[min_len:] or word2[min_len:])
