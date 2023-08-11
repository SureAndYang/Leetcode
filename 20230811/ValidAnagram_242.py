#!/usr/bin/python3

""" Easy: Valid Anagram
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Input: s = "anagram", t = "nagaram"
Output: true
"""

class Solution:

    # Runtime 82.91%, Memory 63.91%.
    def isAnagram_1(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        exists = {}
        for char in s:
            if char not in exists:
                exists[char] = 1
            else:
                exists[char] += 1
        for char in t:
            if char not in exists:
                return False
            exists[char] -= 1

        # Using any(), all() sometimes can make things easy.
        return not any(exists.values())


    # From leetcode, this solution can save memory which is the difference bwtween dict and list.
    def isAnagram_2(self, s: str, t: str) -> bool:
            if len(s) != len(t):
                return False

            counter_s = [0] * 26
            counter_t = [0] * 26

            for char in s:
                counter_s[ord(char) - ord('a')] += 1

            for char in t:
                counter_t[ord(char) - ord('a')] += 1

            return counter_s == counter_t


    # Combine solution1 and solution2, I can get the following one.
    def isAnagram_3(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counter = [0] * 26

        for char in s:
            counter[ord(char) - ord('a')] += 1

        for char in t:
            counter[ord(char) - ord('a')] -= 1

        return not any(counter)
