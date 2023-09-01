#!/usr/bin/python3

""" Medium: Sort Colors
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects
of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.
"""

class Solution:
    """Runtime 85.42%, Memory 69.14%. Write down a general case, and find the pattern in it.

    [2, 0, 2, 1, 1, 0], ends = [0, 0] , which memorizing the end (+1) of 0 or 1.
    When we meet 0, we exchange 0 with 2 (which is at the position 'ends[1]'), and then exchange 0
    with 1 (which is at the position 'ends[0]'). PS: If we exchange 0 directly with 1, what will
    happen? --> Some 1s will be after 2.
    After this, both ends[0] and ends[1] need add 1, which means their 'tail' move backward by 1.

    When we meet 1, we exchange 1 with 2 (which is at the position 'ends[1]').
    After this, ends[1] needs add 1.

    Initial status: [2, 0, 2, 1, 1, 0], ends = [0, 0]
    Cur: nums[1] = 0, [0, 2, 2, 1, 1, 0], ends = [1, 1]
    Cur: nums[2] = 2, [0, 2, 2, 1, 1, 0], ends = [1, 1]
    Cur: nums[3] = 1, [0, 1, 2, 2, 1, 0], ends = [1, 2]
    Cur: nums[4] = 1, [0, 1, 1, 2, 2, 0], ends = [1, 3]
    Cur: nums[5] = 0, [0, 0, 1, 1, 2, 2], Ex(nums[5], nums[3]) and Ex(nums[3], nums[1]).
    """
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ends = [0, 0]
        for i, n in enumerate(nums):
            if n == 2:
                continue
            nums[i], nums[ends[1]] = nums[ends[1]], nums[i]
            if n == 0:
                nums[ends[1]], nums[ends[0]] = nums[ends[0]], nums[ends[1]]
                ends[0] += 1
            ends[1] += 1
