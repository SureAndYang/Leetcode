#!/usr/bin/python3

""" Medium: Rotate Array
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
"""

class Solution:

    # Runtime 85.3%, Memory 99.4%. This method is just like a joke, but it's still a solution.
    def rotate_1(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        k %= l
        nums[:] = nums[l-k:] + nums[:l-k]


    def rotate_2(self, nums: List[int], k: int) -> None:
        pass
