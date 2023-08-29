#!/usr/bin/python3

""" Medium: Check if There is a Valid Partition For The Array.

You are given a 0-indexed integer array nums. You have to partition the array into one or more
contiguous subarrays.

We call a partition of the array valid if each of the obtained subarrays satisfies one of the
following conditions:
    The subarray consists of exactly 2, equal elements. For example, the subarray [2,2] is good.
    The subarray consists of exactly 3, equal elements. For example, the subarray [4,4,4] is good.
    The subarray consists of exactly 3 consecutive increasing elements, that is, the difference
    between adjacent elements is 1. For example, the subarray [3,4,5] is good, but the subarray
    [1,3,5] is not.
Return true if the array has at least one valid partition. Otherwise, return false.
"""


class Solution:
    """Runtime 74.56%, Memory 64.04%"""
    def validPartition_1(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return False

        # DP
        valid = [False] * (len(nums) + 1)
        valid[0] = True
        valid[2] = nums[0] == nums[1]

        for i in range(2, len(nums)):
            if nums[i] == nums[i-1] == nums[i-2] and valid[i-2]:
                valid[i+1] = True
            elif nums[i] == nums[i-1] and valid[i-1]:
                valid[i+1] = True
            elif nums[i-2] + 1 == nums[i-1] and nums[i-1] + 1 == nums[i] and valid[i-2]:
                valid[i+1] = True

        return valid[-1]


    """Runtime 96.82%, Memory 64.04%"""
    def validPartition_2(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return False

        """DP"""
        valid = [False] * (len(nums) + 1)
        valid[0] = True
        valid[2] = nums[0] == nums[1]

        for i in range(2, len(nums)):
            """By reducing unnecessary comparison from solution 1, runtime goto to 96.82%

            As we only use valid[i-2] or valid[i-1], then we can reduce memory future.
            """
            if nums[i] == nums[i-1]:
                if valid[i-1] or (nums[i-1] == nums[i-2] and valid[i-2]):
                    valid[i+1] = True
            elif nums[i-2] + 1 == nums[i-1] and nums[i-1] + 1 == nums[i] and valid[i-2]:
                valid[i+1] = True

        return valid[-1]
