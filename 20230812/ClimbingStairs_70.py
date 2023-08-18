#!/usr/bin/python3

""" Easy: Climbing Stairs

You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

class Solution:
    # The best. Fibonacci sequence. DP problem.
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        i, j = 1, 2
        for _ in range(2, n):
            i, j = j, i + j
        return j
