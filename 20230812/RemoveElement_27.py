#!/usr/bin/python3

""" Easy: Remove Element
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The
order of the elements may be changed. Then return the number of elements in nums which are not equal
to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need
to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not
equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.
"""

class Solution:
    def removeElement_1(self, nums: List[int], val: int) -> int:
        i, j = 0, len(nums) - 1
        while True:
            while j >= 0 and nums[j] == val:
                j -= 1
            if j <= i:
                break
            if nums[i] == val:
                nums[i] = nums[j]
                j -= 1
            i += 1
        return max(j+1, 0)

    # Solution almost same, clear code.
    def removeElement_2(self, nums: List[int], val: int) -> int:
        index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
        return index
