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


    """Runtime 17.48% O(k*n), Memory 70.04%."""
    def rotate_2(self, nums: List[int], k: int) -> None:
        for i in range(k):
            nums.insert(0, nums.pop()) # Time complexity of list.insert(0, n) is O(n).
                                       # Time complexity of list.pop() is O(1).


    """Runtime 98.44%, Memory 94.02%"""
    def rotate_3(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        nums[:] = nums[::-1]
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]
