#!/usr/bin/python3

""" Medium: Container With Most Water
You are given an integer array height of length n. There are n vertical lines drawn such that the
two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the
most water.

Return the maximum amount of water a container can store.
Notice that you may not slant the container.
"""

class Solution:
    """Runtime 87.88%, Memory 46.23%"""
    def maxArea(self, height: List[int]) -> int:
        # Two pointers.
        i, j = 0, len(height) - 1
        max_volumn = 0
        while i < j:
            volumn = min(height[i], height[j]) * (j - i)
            max_volumn = max(max_volumn, volumn)
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return max_volumn

