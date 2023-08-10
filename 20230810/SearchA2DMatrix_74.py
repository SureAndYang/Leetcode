#!/usr/bin/python3

""" Medium: Search a 2D Matrix

You are given an m x n integer matrix matrix with the following two properties:
1. Each row is sorted in non-decreasing order.
2. The first integer of each row is greater than the last integer of the previous row.

Given an integer target, return true if target is in matrix or false otherwise.
You must write a solution in O(log(m * n)) time complexity.

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
"""

class Solution:

    # Runtime 29.78%, Memory 22.84%.
    def searchMatrix_1(self, matrix: List[List[int]], target: int) -> bool:

        # Remove this function and just copy code to its caller.
        # Runtime 46.43%, Memory 87.57% when removing this function.
        def getItem(index, m):
            row, col = divmod(index, m)
            return matrix[row][col]

        # Regard the matrix as a long sorted array. This will make the problem as a easy one.
        m = len(matrix[0])
        n = len(matrix)
        i, j = 0, m * n - 1
        while i < j:
            mid = (i + j) // 2
            val = getItem(mid, m)
            if val == target:
                return True
            elif val > target:
                # Search the previous half.
                j = mid - 1
            else:
                i = mid + 1
        return getItem(i, m) == target


    # This is a copy from leetcode, using bisect.bisect_left(). Very quick.
    def searchMatrix_2(self, matrix: List[List[int]], target: int) -> bool:
        # Handle the Boundary.
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False

        # Find the correct row whose last number is larger than target at the first time.
        row = matrix[bisect_left(matrix, target, key = lambda x: x[-1])]

        idx = bisect_left(row, target)

        return row[idx] == target
