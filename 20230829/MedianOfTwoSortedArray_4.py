#!/usr/bin/python3

""" Hard: Median of Two Sorted Array
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two
sorted arrays.

The overall run time complexity should be O(log (m+n)).
"""

class Solution:
    """Runtime 57.97%, Memory 10.65%"""
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """This problem is solved easily because the following several lines are definitely the same
        logic with the 'merge' function in MergeSort"""
        merge = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                merge.append(nums2[j])
                j += 1
            else:
                merge.append(nums1[i])
                i += 1
        merge.extend(nums1[i:] or nums2[j:])

        if len(merge) % 2 == 0:
            return (merge[len(merge) // 2 - 1] + merge[len(merge) // 2]) / 2
        else:
            return merge[len(merge) // 2]


    """Runtime 80.68%, Memory 40.24%.

    Maybe this solution is the aim of this problem. Some faster solutions are using list.sort()
    functions.
    """
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if (len(nums1) + len(nums2)) % 2 == 0:
            medians = {(len(nums1) + len(nums2)) // 2, (len(nums1) + len(nums2)) // 2 - 1}
        else:
            medians = {(len(nums1) + len(nums2)) // 2}

        i, j, count = 0, 0, []
        while i < len(nums1) and j < len(nums2):
            if i + j in medians:
                count.append(min(nums1[i], nums2[j]))
                medians.remove(i + j)
            if nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1

        for m in medians:
            count.append((nums1[i:] or nums2[j:])[m-i-j])

        return sum(count) / len(count)
