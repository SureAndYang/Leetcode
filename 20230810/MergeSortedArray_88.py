#!/usr/bin/python3

""" Easy: Merge Sorted Array
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m
and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the
array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the
elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2
has a length of n.

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
"""

class Solution:

    # Runtime 74%, Memory 84.41%.
    def merge_1(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return

        # Because the nums1 has the full length, we need to do it backward always fill 'blank cell'
        # or 'used cell'.
        i, j = m - 1, n - 1
        cur = m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[cur] = nums1[i]
                i -= 1
            else:
                nums1[cur] = nums2[j]
                j -= 1
            cur -= 1

        # Not hard, but we should be careful about the boundary.
        if i < 0:
            for v in range(j+1):
                nums1[v] = nums2[v]


    # Almost same as mine. but it's more smart.
    def merge_2(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        a, b, write_index = m-1, n-1, m + n - 1

        while b >= 0:
            if a >= 0 and A[a] > B[b]:
                A[write_index] = A[a]
                a -= 1
            else:
                A[write_index] = B[b]
                b -= 1

            write_index -= 1
