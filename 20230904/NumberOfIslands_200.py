#!/usr/bin/python3

""" Medium: Number of Islands
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return
the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or
vertically. You may assume all four edges of the grid are all surrounded by water.
"""

class Solution:
    """Runtime 63.51%, Memory 49.56%"""
    def numIslands(self, grid: List[List[str]]) -> int:
        # DFS.
        def dfs(i, j):
            if visited[i][j] or grid[i][j] == '0':
                return
            visited[i][j] = True
            for ns, nj in [(i-1, j), (i, j-1), (i+1, j), (i, j+1)]:
                if 0 <= ns < len(grid) and 0 <= nj < len(grid[0]):
                    print('ns {}, nj {}'.format(ns, nj))
                    dfs(ns, nj)

        count = 0
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if visited[i][j] or grid[i][j] == '0':
                    continue
                dfs(i, j)
                count += 1
        return count


    """Runtime 75.35%, Memory 54.07%. Best thought."""
    def numIslands(self, grid: List[List[str]]) -> int:
        # DFS.
        def dfs(i, j):
            if grid[i][j] == '0':
                return
            grid[i][j] = '0'
            for ns, nj in [(i-1, j), (i, j-1), (i+1, j), (i, j+1)]:
                if 0 <= ns < len(grid) and 0 <= nj < len(grid[0]):
                    dfs(ns, nj)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '0':
                    continue
                dfs(i, j)
                count += 1
        return count
