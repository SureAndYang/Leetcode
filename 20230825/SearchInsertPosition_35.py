#!/usr/bin/python3

""" Easy: Search Insert Position
Given a sorted array of distinct integers and a target value, return the index if the target is
found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
"""

class Solution:
    """Runtime 71.98%, Memory 54.62%, O(logn)"""
    def searchInsert(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums) - 1
        while i < j:
            mid = (i + j) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                i = mid + 1
            else:
                j = mid - 1
        return i + 1 if nums[i] < target else i


    """Runtime 71.98%, Memory 99.07%, O(n) doesn't meet the requirement """
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)

