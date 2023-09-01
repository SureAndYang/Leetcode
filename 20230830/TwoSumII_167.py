#!/usr/bin/python3

""" Medium: Two Sum II - Input Array Is Sorted
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two
numbers such that they add up to a specific target number. Let these two numbers be numbers[index1]
and numbers[index2] where 1 <= index1 < index2 < numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1,
index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element
twice.

Your solution must use only constant extra space.
"""


class Solution:
    """Runtime 52.25%, Memory 57.76%, Two pointers"""
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 1, len(numbers)
        while i < j:
            if numbers[i-1] + numbers[j-1] == target:
                break
            if numbers[i-1] + numbers[j-1] > target:
                j -= 1
            else:
                i += 1
        return [i, j]


    """Almost same, but much faster, Runtime 94.19%, Memory 57.76%, Two pointers"""
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # In solution 1, we set i=1, j=len(numbers). This will cause many meaningless 'i-1'/'j-1',
        # thus minus caculation, when indexing a number from list numbers.
        """Small change improves much"""
        i, j = 0, len(numbers) - 1
        while i < j:
            if numbers[i] + numbers[j] == target:
                break
            if numbers[i] + numbers[j] > target:
                j -= 1
            else:
                i += 1
        return [i + 1, j + 1] # Index fixed only once.
