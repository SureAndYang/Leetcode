#!/usr/bin/python3

""" Medium: Peak Index in a Mountain Array
An array arr is a mountain if the following properties hold:

1. arr.length >= 3
2. There exists some i with 0 < i < arr.length - 1 such that:
    arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
    arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given a mountain array arr, return the index i such that arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
> arr[i + 1] > ... > arr[arr.length - 1].

You must solve it in O(log(arr.length)) time complexity.
"""

class Solution:

    # Runtime 94.73% O(logN), Memory 8.28% O(1).
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        """Same as find the minimum nunmber in a rotated sorted array"""
        i, j = 0, len(arr) + 1
        while i < j:
            mid = (i + j) // 2
            if arr[mid-1] < arr[mid] > arr[mid+1]:
                return mid
            elif arr[0] <= arr[mid-1] <  arr[mid]:
                # Left side is sorted.
                i = mid
            else:
                j = mid
        return i
