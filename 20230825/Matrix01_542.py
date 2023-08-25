#!/usr/bin/python3

""" Medium: 01 Matrix, https://leetcode.com/problems/01-matrix/
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.
"""

class Solution:

    """Runtime 65.70%, Memory 53.83%"""
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        def update(mat, i, j, val, to_check) -> int:
            if i < 0 or j < 0 or i >= len(mat) or j >= len(mat[0]) or mat[i][j] != -1:
                return 0
            mat[i][j] = val
            to_check.append((i, j))
            return 1

        res = [[-1] * len(mat[0]) for _ in range(len(mat))]
        checking = []
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    res[i][j] = 0
                    checking.append((i, j))
        cnt, dist, to_check = len(checking), 1, []
        while cnt < len(mat) * len(mat[0]):
            for i, j in checking:
                cnt += update(res, i-1, j, dist, to_check)
                cnt += update(res, i+1, j, dist, to_check)
                cnt += update(res, i, j-1, dist, to_check)
                cnt += update(res, i, j+1, dist, to_check)
            checking, to_check = to_check, []
            dist += 1
        return res


    """Runtime 46.56%, Memory 79.29%, Committed twice and the runtime is worse than solution 1.

    This code is almost copied from other author. Similar thought with solution 1 but less memory
    consuming using `deque()` and `MAX_VALUE`.

    It's more time consuming. Dont know why.
    """
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        MAX_VALUE = m * n
        queue = deque()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    queue.append((i, j))
                else:
                    mat[i][j] = MAX_VALUE

        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        while queue:
            row, col = queue.popleft()
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if 0 <= r < len(mat) and 0 <= c < len(mat[0]) and mat[r][c] > mat[row][col] + 1:
                    queue.append((r, c))
                    mat[r][c] = mat[row][col] + 1
        return mat
