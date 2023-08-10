#!/usr/bin/python3

""" Easy: Contains Duplicate
Given an integer array nums, return true if any value appears at least twice in the array, and
return false if every element is distinct.

Input: nums = [1,2,3,1]
Output: true
"""

class Solution:

    # Runtime 98.27%, Memory 81.02%. Not much comments, too easy.
    def containsDuplicate(self, nums: List[int]) -> bool:
        exists = set()

        for n in nums:
            if n in exists:
                return True
            exists.add(n)
        return False
