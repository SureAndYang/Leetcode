#!/usr/bin/python3

""" Medium: Search in Rotated Sorted Array II
There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values)

Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k <
nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1],
..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5
and become [4,5,6,6,7,0,1,2,4,4].

Given the array nums after the rotation and an integer target, return true if target is in nums, or
false if it is not in nums.

You must decrease the overall operation steps as much as possible.
"""

class Solution:

    # There is no better solution.
    # Someone makes joke on leetcode by one-line answer `return target in nums`.
    def search(self, nums: List[int], target: int) -> bool:
        def binary_search(nums):
            if len(nums) == 0:
                return False
            if len(nums) == 1:
                return nums[0] == target

            i, j = 0, len(nums) - 1
            while i < j:
                mid = (i + j) // 2
                if nums[mid] == target:
                    return True
                elif nums[mid] > target:
                    j = mid - 1
                else:
                    i = mid + 1
            return nums[i] == target

        start = 0
        for i, n in enumerate(nums):
            if i > 0 and nums[i-1] > n:
                start = i
                break

        return binary_search(nums[:start]) if target > nums[-1] else binary_search(nums[start:])
