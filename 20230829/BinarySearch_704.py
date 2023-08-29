#!/usr/bin/python3

""" Easy: Binary Search
Given an array of integers nums which is sorted in ascending order, and an integer target, write a
function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

"""

class Solution:
    """Runtime 80.62%, Memory 28.93%"""
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums)
        while i < j:
            mid = int((i + j) // 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                j = mid - 1
            else:
                i = mid + 1
        return i if i < len(nums) and nums[i] == target else -1


    """Recursion, Runtime 60.23%, Memory 65.67%"""
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        mid = int(len(nums) // 2)
        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            return self.search(nums[:mid], target)

        res = self.search(nums[mid+1:], target)
        return res + mid + 1 if res != -1 else -1
