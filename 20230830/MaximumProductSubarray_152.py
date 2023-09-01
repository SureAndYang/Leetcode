#!/usr/bin/python3

""" Medium: Maximum Product Subarray
Given an integer array nums, find a subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.
"""


class Solution:
    """Runtime 5.35%, Memory 59.37%"""
    def maxProduct(self, nums: List[int]) -> int:
        # Interval DP
        if 1 in nums:
            products = [n for n in nums if n != 1]
            max_product = max(products + [1])
            nums = products[:]
        else:
            products = nums[:]
            max_product = max(products)

        for interval in range(1, len(nums)):
            # interval = 1, means two elements [i, i+1].
            for start in range(len(nums) - interval):
                products[start] = products[start] * nums[start+interval]
                if products[start] > max_product:
                    max_product = products[start]
        return max_product


    """Runtime 70.69%, Memory 89.87%.
    This solution is from other author. Actually I compressed the above 2D into 1D solution. But
    that doesn't help either in Runtime nor in Memory.

    This solution goes further compressing 1D into O(1) solution.
    """
    def maxProduct(self, nums: List[int]) -> int:
        curMax, curMin = 1, 1
        res = nums[0]

        for n in nums:
            vals = (n, n * curMax, n * curMin)
            curMax, curMin = max(vals), min(vals)

            res = max(res, curMax)

        return res
