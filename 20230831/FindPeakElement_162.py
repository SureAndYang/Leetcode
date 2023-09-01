#!/usr/bin/python3

""" Medium: Find Peak Element
A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array
contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be
strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.
"""

class Solution:
    """Runtime 83.89%, Memory 87.89%"""
    def findPeakElement(self, nums: List[int]) -> int:
        # For O(logn), this must be binary and the problem becomes how to judge the next direction.
        i, j = 0, len(nums) - 1
        while i < j:
            mid = (i + j) // 2
            if nums[mid-1] < nums[mid] > nums[mid+1]:
                return mid
            if nums[mid-1] >= nums[mid]:
                j = mid
            else:
                i = mid + 1
        return 0 if nums[0] > nums[-1] else len(nums) - 1
