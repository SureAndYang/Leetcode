#!/usr/bin/python3

""" Easy: Valid Palindrome
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and
removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric
characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
"""

class Solution:

    # Runtime 98.71%, Memory 60.09%.
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        char_set = set('abcdefghijklmnopqrstuvwxyz0123456789')
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] not in char_set:
                i += 1
                continue
            if s[j] not in char_set:
                j -= 1
                continue
            if s[i] == s[j]:
                i += 1
                j -= 1
                continue
            else:
                return False
        return True


    # From other author, similar solution but simpler code.
    def isPalindrome(self, s: str) -> bool:
        s = [c.lower() for c in s if c.isalnum()]
        return all (s[i] == s[-i] for i in range(len(s)//2))
