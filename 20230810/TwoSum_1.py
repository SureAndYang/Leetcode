#!/usr/bin/python3

""" Easy: Two Sum
Given an array of integers `nums` and an integer `target`, return `indices` of the two numbers such
that they add up to `target`.

You may assume that each input would have 'exactly' one solution, and you may not use the same
element twice.

You can return the answer in any order.
"""

from collections import defaultdict

class Solution:

    # Runtime 80.34%, Memory 5.85%
    def twoSum_1(self, nums: List[int], target: int) -> List[int]:
        num_index = defaultdict(set) # defaultdict needs more memory
        for i, n in enumerate(nums):
            num_index[n].add(i)      # Save all numbers and the value is set, need more memory.

        for n in nums:
            left = target - n
            if left == n and len(num_index[n]) > 1:
                return list(num_index[n])[:2]
            if left != n and left in num_index:
                return [num_index[n].pop(), num_index[left].pop()]


    # Runtime 97.92%, Memory 15%, BEST solution.
    def twoSum_2(self, nums: List[int], target: int) -> List[int]:
        """ This method can early stop when we meet the answer, thus we can get the answer before
        checking the entire list. This can save some time especially when the list is large.

        The dict will only store a part of the numbers, this will save memory.
        """
        left_dict = {}
        for i, n in enumerate(nums):
            if n in left_dict:
                return [left_dict[n], i]
            left_dict[target - n] = i
