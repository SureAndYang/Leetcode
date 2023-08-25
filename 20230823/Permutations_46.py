#!/usr/bin/python3

""" Medium: Permutations
Given an array nums of distinct integers, return all the possible permutations. You can return the
answer in any order.
"""

class Solution:

    """Runtime 91.59%, Memory 67.62%"""
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]

        res = []
        for i, n in enumerate(nums):
            res.extend([[n] + com for com in self.permute(nums[:i]+nums[i+1:])])
        return res
