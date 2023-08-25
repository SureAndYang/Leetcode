#!/usr/bin/python3

""" Easy: Move Zeros

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of
the non-zero elements.

Note that you must do this in-place without making a copy of the array.
"""

class Solution:

    """Runtime 75.97%, Memory 47.40%"""
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = 0, 0
        while i < len(nums) or j < len(nums):
            if i >= len(nums):
                nums[j] = 0
                j += 1
            elif nums[i] != 0:
                nums[j] = nums[i]
                j += 1
            i += 1


    """Runtime 90.11%, Memory 84.56%"""
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
        for i in range(j, len(nums)):
            nums[i] = 0
