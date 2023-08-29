#!/usr/bin/python3

""" Medium: House Robber
You are a professional robber planning to rob houses along a street. Each house has a certain amount
of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses
have security systems connected and it will automatically contact the police if two adjacent houses
were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum
amount of money you can rob tonight without alerting the police.


POINT IS: can not robber two adjacent houses.
"""

class Solution:
    """Runtime 52.02%, Memory 36.40%"""
    def rob(self, nums: List[int]) -> int:
        amount = [0] * (len(nums) + 1)
        amount[0] = 0
        amount[1] = nums[0]

        for i in range(1, len(nums)):
            if nums[i] + amount[i-1] > amount[i]:
                amount[i+1] = nums[i] + amount[i-1]
            else:
                amount[i+1] = amount[i]
        return amount[-1]


    """Runtime 58.99%, Memory 70.79%, because when we meet a new house, the profit we can have only
    depends on cur_house, profit_till_pre_house (if not robber the current), and
    profit_till_pre_pre_house if we robber the current.
    """
    def rob(self, nums: List[int]) -> int:
        pre2, pre1 = 0, nums[0]
        for i in range(1, len(nums)):
            pre2, pre1 = pre1, pre1 if pre1 > nums[i] + pre2 else nums[i] + pre2
        return pre1
