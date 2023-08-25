#!/usr/bin/python3

""" Medium: Product of Array Except Self
Given an integer array nums, return an array answer such that answer[i] is equal to the product of
all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.
"""

class Solution:

    """Do not meet the requirement 'without using division', Runtime 78%, Memory 49%"""
    def productExceptSelf_1(self, nums: List[int]) -> List[int]:
        # Point is O(n) without using division.
        def mul(nums):
            return functools.reduce(lambda x, y: x*y, nums)
        zeros = []
        for i, n in enumerate(nums):
            if n == 0:
                zeros.append(i)
        if len(zeros) > 1:
            return [0] * len(nums)

        if len(zeros) == 1:
            return [0] * zeros[0] + [mul(filter(lambda x: x!=0, nums))] + [0] * (
                    len(nums)-zeros[0]-1)

        res = [mul(nums)] * len(nums)
        for i, n in enumerate(nums):
            # This solution is a test solution.
            # It can't fit the requirement 'without using division'
            """'res[i] *= n**-1' can meet the requirement? """
            res[i] //= n
        return res


    """Runtime 72%, Memory 24%, inspired by other author."""
    def productExceptSelf_2(self, nums: List[int]) -> List[int]:
        mul_from_left, mul_from_right = [1], [1]
        for i in range(len(nums)-1):
            if mul_from_left:
                mul_from_left.append(mul_from_left[-1] * nums[i])
            else:
                mul_from_left.append(nums[i])

        for i in range(len(nums)-1, 0, -1):
            if mul_from_right:
                mul_from_right.append(mul_from_right[-1] * nums[i])
            else:
                mul_from_right.append(nums[i])

        res = []
        for i in range(len(nums)):
            res.append(mul_from_left[i] * mul_from_right[len(nums)-i-1])
        return res


    """Improved from solution2, there is no need to store all left-multiplation result
    Runtime 85.55%, Memory 69.88%.
    """
    def productExceptSelf_3(self, nums: List[int]) -> List[int]:
        mul_from_right = [1]
        for i in range(len(nums)-1, 0, -1):
            if mul_from_right:
                mul_from_right.append(mul_from_right[-1] * nums[i])
            else:
                mul_from_right.append(nums[i])

        mul_left, res = 1, []
        for i in range(len(nums)):
            res.append(mul_left * mul_from_right[len(nums)-i-1])
            mul_left *= nums[i]
        return res


    """From other author
    This is definitely an improvement from solution 2 by 'Storing the right products straight into
    the output array'. I don't try this code, but its thought is right.
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length=len(nums)
        sol=[1]*length
        pre = 1
        post = 1
        for i in range(length):
            sol[i] *= pre
            pre = pre*nums[i]
            sol[length-i-1] *= post
            post = post*nums[length-i-1]
        return(sol)
