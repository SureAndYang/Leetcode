#!/usr/bin/python3

""" Easy, Can Place Flowers
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers
cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty,
and an integer n, return true if n new flowers can be planted in the flowerbed without violating the
no-adjacent-flowers rule and false otherwise.

Constraints:
    1 <= flowerbed.length <= 2 * 10^4
    flowerbed[i] is 0 or 1.
    There are no two adjacent flowers in flowerbed.
    0 <= n <= flowerbed.length
"""

class Solution:
    """Runtime 84.26% O(n), Memory 60.15%"""
    def canPlaceFlowers_1(self, flowerbed: List[int], n: int) -> bool:
        i, valid = 0, 0
        while i < len(flowerbed) - 1:
            if flowerbed[i] == 1:
                i += 2
            elif flowerbed[i+1] == 0:
                valid += 1
                if valid >= n: # Early stop.
                    return True
                i += 2
            else:
                i += 1
        else:
            if i == len(flowerbed) - 1 and (flowerbed[i] + flowerbed[i-1]) == 0:
                valid += 1
        return valid >= n


    """Runtime 99%, Memory 90%"""
    def canPlaceFlowers_2(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        while i < len(flowerbed) - 1:
            if flowerbed[i] == 1:
                i += 2
            elif flowerbed[i+1] == 0:
                n -= 1
                if n <= 0: # Early stop if possible.
                    return True
                i += 2
            else:
                i += 1
        else:
            if i == len(flowerbed) - 1 and (flowerbed[i] + flowerbed[i-1]) == 0:
                n -= 1
        return n <= 0
