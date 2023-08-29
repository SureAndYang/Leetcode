#!/usr/bin/python3

""" Medium: Group Anagrams
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Example 1:
    Input: strs = ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
"""

class Solution:

    """Runtime 66.16%, Memory 65.44%"""
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            ss = ''.join(sorted(s))
            if ss in groups:
                groups[ss].append(s)
            else:
                groups[ss] = [s]
        return groups.values()
