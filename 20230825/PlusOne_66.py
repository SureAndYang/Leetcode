#!/usr/bin/python3

""" Easy: Plus One

"""


class Solution:
    """Runtime 87.19%, Memory 99.51%"""
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.append(0)
        plus = 1
        for i in range(len(digits)-2, -1, -1):
            if digits[i] + plus == 10:
                digits[i+1] = 0
            else:
                digits[i+1] = digits[i] + plus
                plus = 0
        digits[0] = plus
        return digits if plus else digits[1:]
