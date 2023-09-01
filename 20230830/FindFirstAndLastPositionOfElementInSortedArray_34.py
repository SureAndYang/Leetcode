#!/usr/bin/python3

""" Medium: Find First and Last Position of Element in Sorted Array
Given an array of integers nums sorted in non-decreasing order, find the starting and ending
position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
"""

class Solution:
    """Runtime 92.98%, Memory 95.51%. time = 2*log(n)"""
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(find_first=True):
            i, j, res = 0, len(nums), -1
            while i < j:
                mid = (i+j) // 2
                if nums[mid] == target:
                    res = mid
                    if find_first:
                        j = mid
                    else:
                        i = mid + 1
                elif nums[mid] > target:
                    j = mid
                else:
                    i = mid + 1
            return res
        return [binary_search(True), binary_search(False)]

