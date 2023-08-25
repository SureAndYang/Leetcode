#!/usr/bin/python3

""" Easy, Sqrt(x)
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.
    For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
"""

class Solution:
    """Runtime 19.60%, Memory 23.77% Brute Force"""
    def mySqrt(self, x: int) -> int:
        i = 0
        while True:
            if i * i > x:
                return i - 1
            i += 1


    """Runtime 24.59%, Memory 62.36%"""
    def mySqrt(self, x: int) -> int:
        def search(x, start=0):
            while True:
                if start * start > x:
                    return start - 1
                start += 1

        sx, start = str(x), 1
        if len(sx) % 2 != 0:
            start = search(int(sx[0]))
        else:
            start = search(int(sx[:2]))

        for i in range((len(sx)-1)//2):
            start = start * 10

        return search(x, start)


    """Runtime 86%, Memory 89%, Binary search


    Binary search, Find something in sorted array.
    1. Find target number in distinct sorted array.
    2. Find target number with smallest or largest index in duplicated sorted array.
    3. Find certain number having fixed relation with target in sorted array.
        # Thus, like this problem. The relation is the 'number' you find meet: n * n ~ x.
        # Similar will be (n^3) < x < ((n+1)^3), or just some formula like n^2+2n+1.
    """
    def mySqrt(self, x: int) -> int:
        i, j = 1, x
        while i < j:
            mid = (i+j) // 2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                j = mid - 1
            else:
                i = mid + 1
        return i - 1 if i * i > x else i
