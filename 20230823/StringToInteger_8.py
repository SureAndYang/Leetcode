#!/usr/bin/python3

""" Medium: String to Integer (atoi)
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar
to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:
    Read in and ignore any leading whitespace.
    Check if the next character (if not already at the end of the string) is '-' or '+'. Read this
        character in if it is either. This determines if the final result is negative or positive
        respectively. Assume the result is positive if neither is present.
    Read in next the characters until the next non-digit character or the end of the input is
        reached. The rest of the string is ignored.
    Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read,
        then the integer is 0. Change the sign as necessary (from step 2).
    If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer
        so that it remains in the range. Specifically, integers less than -231 should be clamped to
        -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
    Return the integer as the final result.

Note:
    Only the space character ' ' is considered a whitespace character.
    Do not ignore any characters other than the leading whitespace or the rest of the string after
        the digits.

Constraints:
    0 <= s.length <= 200
    s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.
"""

class Solution:

    """Runtime 54.13%, Memory 41.28%"""
    def myAtoi(self, s: str) -> int:
        MIN = - 2**31

        res, meet_number, positive = 0, False, True
        for char in s:
            if char == ' ' and not meet_number:
                continue
            if char in {"+", "-"} and not meet_number:
                positive = char == "+"
                meet_number = True
                continue

            if not char.isdigit():
                break
            meet_number = True
            res = res * 10 + ord(char) - ord("0")
        return min(res, -MIN-1) if positive else max(-res, MIN)

    """From other author"""
    def myAtoi_2(self, s: str) -> int:
        length, i, sign, res = len(s), 0, +1, 0

        while i < length and s[i] == ' ':
            i = i + 1

        if i < length and s[i] in ('-', '+'):
			sign, i = -1 if s[i] == '-' else +1, i + 1

        while i < length and s[i].isdigit():
			res, i = res * 10 + ord(s[i]) - ord("0"), i + 1

        return max( -2**31, min(sign * res, 2**31 - 1))
