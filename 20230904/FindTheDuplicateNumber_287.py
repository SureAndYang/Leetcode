#!/usr/bin/python3

""" Medium: Find the Duplicate Number
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n]
inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

This problem belongs to 'Floyd’s Tortoise and Hare algorithm'.
"""

class Solution:
    """ From other author, I cann't finish it in time.

    Runtime 70.42%, Memory 57.86%"""
    def findDuplicate(self, nums: List[int]) -> int:
        slow1, slow2, fast3 = nums[0], 0, nums[nums[0]]

        while slow1 != fast3:
            slow1, fast3 = nums[slow1], nums[nums[fast3]]

        while slow1 != slow2:
            slow1, slow2 = nums[slow1], nums[slow2]

        return slow2


    """Similar with 1st solution. From other author. Two pointers.

    Actually, I thought about two pointers solution, but I didn't thinking that
    'nums[nums[pointer]]'.
    """
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast= nums[nums[fast]]
            if slow == fast:
                break

        fast = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow


    """Bit manufication, it's a cheat to call this solution as O(1) space.
    From other author.
    """
    def findDuplicate(self, nums: List[int]) -> int:
        seen = 0
        for n in nums:
            """Using '1 << n' as a dict for seen or not. This will create a really big number when n
            is 10^5, thus 2**10**5. But this solution passed.

            It's a cheat to call this solution as O(1) space.
            """
            if seen & (1 << n):
                return n
            seen |= 1 << n
