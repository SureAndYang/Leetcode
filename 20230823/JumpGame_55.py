#!/usr/bin/python3

""" Medium: Jump Game
You are given an integer array nums. You are initially positioned at the array's first index, and
each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.
"""

class Solution:

    """Runtime 82.55%, Memory 62.38%"""
    def canJump(self, nums: List[int]) -> bool:
        farest = 0
        for i in range(len(nums)):
            if farest < i:
                return False
            farest = max(farest, i + nums[i])
        return True
