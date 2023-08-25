#!/usr/bin/python3

""" Medium: Maximum Subarray, https://leetcode.com/problems/maximum-subarray/
Given an integer array nums, find the subarray with the largest sum, and return its sum.
"""

class Solution:

    """Runtime 74.42%, Memory 81.11%"""
    def maxSubArray(self, nums: List[int]) -> int:
        # Because the range of the number is -10^4 - 10^4.
        cur_sum, max_sum = 0, -10001
        for n in nums:
            cur_sum += n
            max_sum = max(cur_sum, max_sum)
            if cur_sum < 0:
                cur_sum = 0
        return max_sum
