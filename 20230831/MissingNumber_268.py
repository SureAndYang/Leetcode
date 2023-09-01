#!/usr/bin/python3

""" Easy: Missing Number
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the
range that is missing from the array.
"""


class Solution:
    """Runtime 97.89%, Memory 49.27%"""
    def missingNumber(self, nums: List[int]) -> int:
        # Using math. If there is no missing number between [0, n], the sum should be 'n*(n+1)/2'.
        return len(nums) * (len(nums) + 1) // 2 - sum(nums)
