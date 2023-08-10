#!/usr/bin/python3

""" Easy: Palindrome Number
Given an integer x, return true if x is a palindrome, and false otherwise.
"""

class Solution:

    # Runtime 94.54%, Memory 40.21%. It's a good solution.
    def isPalindrome_1(self, x: int) -> bool:
        # Of course we can make x to be a string, and x == reverse(x). But it's somehow cheating.
        div = x
        reverse = 0
        while div > 0:
            div, mod = divmod(div, 10)
            reverse = reverse * 10 + mod
        return reverse == x


    # A bit cheating solution.
    def isPalindrome_2(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
