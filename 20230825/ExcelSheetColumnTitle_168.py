#!/usr/bin/python3

""" Easy: Excel Sheet Column Title
Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet
"""

# Thus, convert number based on 10 into new number based on 26.
class Solution:
    char2num = dict(enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ', start=1))

    """Runtime 45.93%, Memory 21.43%"""
    def convertToTitle(self, columnNumber: int) -> str:
        res = ''
        while columnNumber > 26:
            """Notice: you should be very careful about the `columnNumber-1`"""
            columnNumber, mod = divmod(columnNumber-1, 26)
            res = self.char2num[mod+1] + res
        return self.char2num[columnNumber] + res


class Solution:
    """Useing list is more efficient in memory and time. Though the speeds of indexing in both dict
    and list are O(1), but indexing in list should be faster without hashing calculation"""
    char2num = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    """Runtime 56.97%, Memory 60.98%"""
    def convertToTitle(self, columnNumber: int) -> str:
        res = ''
        while columnNumber > 26:
            columnNumber, mod = divmod(columnNumber-1, 26)
            res = self.char2num[mod] + res
        return self.char2num[columnNumber-1] + res


class Solution:
    """Runtime 99.64%, Memory 60.98%, Best solution using chr().
    """
    def convertToTitle(self, columnNumber: int) -> str:
        res = ''
        while columnNumber:
            columnNumber, mod = divmod(columnNumber-1, 26)
            res = chr(65 + mod) + res
        return res
