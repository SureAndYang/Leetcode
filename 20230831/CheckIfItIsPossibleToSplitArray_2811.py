#!/usr/bin/python3

""" Medium: Check if it is Possible to Split Array
You are given an array nums of length n and an integer m. You need to determine if it is possible to
split the array into n non-empty arrays by performing a series of steps.

In each step, you can select an existing array (which may be the result of previous steps) with a
length of at least two and split it into two subarrays, if, for each resulting subarray, at least
one of the following holds:

The length of the subarray is one, or
The sum of elements of the subarray is greater than or equal to m.
Return true if you can split the given array into n arrays, otherwise return false.

Note: A subarray is a contiguous non-empty sequence of elements within an array.
"""


class Solution:
    """Runtime 48.28%, Memory 56.78%. Find the real aim is very important!

    That makes the solution clear. It's medium for understanding the problem fully.
    """
    def canSplitArray(self, nums: List[int], m: int) -> bool:
        if len(nums) <= 2:
            return True
        # Check if there are two adjacent numbers whose sum is greater or equal to m.
        # This pair of numbers will be the last pair to split.
        for i in range(len(nums)-1):
            if nums[i] + nums[i+1] >= m:
                return True
        return False


    """Runtime 82.80%, Memory 56.78%.

    Small change makes big difference in runtime.
    """
    def canSplitArray(self, nums: List[int], m: int) -> bool:
        # Check if there are two adjacent numbers whose sum is greater or equal to m.
        # This pair of numbers will be the last pair to split.
        for i in range(len(nums)-1):
            if nums[i] + nums[i+1] >= m:
                return True

        # Avoid running this judgement for every case. Only run for special cases.
        return len(nums) <= 2


    """Runtime 66.99%, Memory 95.23%.

    Small change makes big difference in memory.
    """
    def canSplitArray(self, nums: List[int], m: int) -> bool:
        # Check if there are two adjacent numbers whose sum is greater or equal to m.
        # This pair of numbers will be the last pair to split.
        i = 0
        """By removing the function calling 'range()', reduce the final memory"""
        while i < len(nums)-1:
            if nums[i] + nums[i+1] >= m:
                return True
            i += 1
        return len(nums) <= 2
