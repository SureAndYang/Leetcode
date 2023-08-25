#!/usr/bin/python3

""" Easy, Majority Element
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the
majority element always exists in the array.
"""

class Solution:

    """Runtime 57.64% O(n), Memory 26.59%"""
    def majorityElement_1(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 1:
            return nums[0]
        counter = {}
        for n in nums:
            if n in counter:
                counter[n] += 1
                if counter[n] > l / 2:
                    return n
            else:
                counter[n] = 1


    """Runtime 97.69% O(nlogn), Memory 26.59%"""
    def majorityElement_2(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums)//2]


    """Runtime 5.11%, Memory 68.6%
    The time complexity of this solution seems to be O(n^2), but actually more than half elements
    are the Majority Element which means we 'should' get the majority by choosing two numbers
    randomly. Thus, the real time complexity is O(n).

    PS: Whether using `random.randint(0, len(nums))` or `random.choice(nums)` to get a number can
    get wrong answer randomly. I dont know why.
    """
    def majorityElement_3(self, nums: List[int]) -> int:
        random.shuffle(nums)
        for i in range(len(nums)):
            count = 0
            for n in nums:
                if n == nums[i]:
                    count +=1
                if count > len(nums) / 2:
                    return n
