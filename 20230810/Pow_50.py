#!/usr/bin/python3

""" Medium: Pow(x, n)

Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
"""
class Solution:

    # Runtime 75%, Memory 75.59%. Recursion will use more memory.
    def myPow_1(self, x: float, n: int) -> float:
        if n == 0:
            return 1.

        # This is very important.
        if n < 0:
            x = 1 / x
            n = -n

        if n % 2 == 1:
            return x * self.myPow(x, n//2) ** 2
        return self.myPow(x, n//2) ** 2


    # Runtime 99.75%, Memory 75.59%.
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            x = 1 / x
            n = -n

        res = x
        multi = 1
        while n > 1:
            if n % 2 == 1:

                # This is very important and hard to think about. Originally I let `multi *= x`,
                # this will make 'inner power' do not affect the outside.
                multi *= res # Try to find the difference between `multi *= x` and `multi *= res`.
            res = res ** 2
            n //= 2
        return res * multi
