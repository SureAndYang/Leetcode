#!/usr/bin/python3

""" Medium: Reverse Integer
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value
to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
"""

class Solution:

    # Runtime 74.42%, Memory 68.41%. Runtime O(n), n is length of number.
    def reverse(self, x: int) -> int:
        MAX = 2**31

        positive = x >= 0
        x, y = abs(x), 0
        while x > 0:
            x, mod = divmod(x, 10)
            y = y * 10 + mod
        if positive:
            return y if y <= MAX - 1 else 0
        return -y if -y >= -MAX else 0
