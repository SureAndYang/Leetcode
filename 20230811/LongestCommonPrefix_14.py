#!/usr/bin/python3

""" Easy: Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""

class Solution:

    # Runtime 97.82%, Memory 34.02%.
    def longestCommonPrefix_1(self, strs: List[str]) -> str:
        min_len = 200
        for s in strs:
            min_len = min(min_len, len(s))

        for i in range(min_len):
            if len(set([s[i] for s in strs])) != 1:
                return strs[0][:i]
        return strs[0][:min_len]


    # Runtime 91.57%, Memory 34.2%. This solution should have better performance.
    def longestCommonPrefix_2(self, strs: List[str]) -> str:
        min_str, max_str = min(strs), max(strs)
        for i, char in enumerate(min_str):
            if char != max_str[i]:
                return min_str[:i]
        return min_str
