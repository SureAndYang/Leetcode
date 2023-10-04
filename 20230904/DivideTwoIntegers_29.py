#!/usr/bin/python3

""" Medium: Divide Two Integers
Given two integers dividend and divisor, divide two integers without using multiplication, division,
and mod operator.

The integer division should truncate toward zero, which means losing its fractional part. For
example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit
signed integer range: [−2^31, 2^31 − 1]. For this problem, if the quotient is strictly greater than
2^31 - 1, then return 2^31 - 1, and if the quotient is strictly less than -2^31, then return -2^31.
"""

class Solution:
    """Runtime 71.87%, Memory 70.87%"""
    def divide(self, dividend: int, divisor: int) -> int:
        positive = True
        if dividend < 0 or divisor < 0:
            if dividend > 0 or divisor > 0:
                positive = False
            dividend, divisor = abs(dividend), abs(divisor)

        if dividend < divisor:
            return 0

        cur, total = [1], [divisor]
        while total[-1] < dividend:
            total.append(total[-1] + total[-1])
            cur.append(cur[-1] + cur[-1])

        res = 0
        for i in range(len(total)-1, -1, -1):
            if dividend < total[i]:
                continue
            dividend -= total[i]
            res += cur[i]
        return min(res, 2**31 - 1) if positive else max(-res, -2**31)


    """From other author. Actually this's not a good solution, because when 'dividend' is a big
    number and the 'divisor' is 1 meanwhile, the time should be very long.
    But, thanks to the effieiency of function 'range', this solution can be passed.

    BUT, it's a valid thought anyway when we think about the funtion 'range'.
    """
    def divide(self, dividend: int, divisor: int) -> int:
        sign = -1 if (dividend >= 0 and divisor < 0) or (dividend < 0 and divisor >= 0) else 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        result = len(range(0, dividend-divisor+1, divisor))
        if sign == -1:
            result = -result
        minus_limit = -(2**31)
        plus_limit = (2**31 - 1)
        result = min(max(result, minus_limit), plus_limit)
        return result
