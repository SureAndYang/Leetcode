#!/usr/bin/python3

""" Medium: Unique Paths II
You are given an m x n integer array grid. There is a robot initially located at the top-left corner
(i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]).
The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot
include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2 * 10^9.
"""

class Solution:

    """Runtime 73.86% O(m*n), Memory 53.51% O(m*n)"""
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # BFS. The robot can not go up and left, so the path will not have circle.
        # Thus, we dont need to memorize 'seen'.
        counters = [[0]*(len(obstacleGrid[0])+1) for _ in range(len(obstacleGrid)+1)]
        for i in range(1, len(obstacleGrid)+1):
            for j in range(1, len(obstacleGrid[0])+1):
                if obstacleGrid[i-1][j-1] == 0:
                    if i == 1 and j == 1:
                        counters[i][j] = 1
                    else:
                        counters[i][j] = counters[i-1][j] + counters[i][j-1]
        return counters[-1][-1]
