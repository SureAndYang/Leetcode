#!/usr/bin/python3

""" Hard: Trapping Rain Water
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it can trap after raining.

"""

class Solution:
    """Runtime 75.47%, Memory 20.26%."""
    def trap(self, height: List[int]) -> int:
        if len(height) <= 1:
            return 0

        left, right, water = 0, 1, 0
        max_right, blocks = right, 0
        while right < len(height):
            if height[right] >= height[left]:
                # A pool generated, calculate the water.
                water += (right - left - 1) * height[left] - blocks
                left, right = right, right + 1

                if right >= len(height):
                    break
                blocks, max_right = 0, right
            else:
                # left is higher, we should remember the highest in the right.
                blocks += height[right]
                if height[right] >= height[max_right]:
                    max_right = right
                right += 1
        water += self.trap(height[left:][::-1])
        return max(water, 0)


    """Runtime 79.62%, Memory 87.46%.

    Improvements:
        1. Remove variable 'max_right', it's useless here.
        2. As we try to find the last pool backwards, water must be positive, remove 'max(water, 0)'
    """
    def trap(self, height: List[int]) -> int:
        if len(height) <= 1:
            return 0

        left, right, water, blocks = 0, 1, 0, 0
        while right < len(height):
            if height[right] >= height[left]:
                # A pool generated, calculate the water.
                water += (right - left - 1) * height[left] - blocks
                left, right = right, right + 1

                if right >= len(height):
                    break
                blocks = 0
            else:
                # left is higher, we should remember the highest in the right.
                blocks += height[right]
                right += 1
        if left < len(height) - 1:
            water += self.trap(height[left:][::-1])
        return water
