#!/usr/bin/python3

""" Medium: Unique Binary Search Tree
Given an integer n, return all the structurally unique BST's (binary search trees), which has
exactly n nodes of unique values from 1 to n. Return the answer in any order.

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """Runtime 64.88%, Memory 11.04%. Similar with the best solution.
    """
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def tree(start, end):
            if end < start:
                return [None]
            if start == end:
                return [TreeNode(start)]
            res = []
            for i in range(start, end + 1):
                for left in tree(start, i-1):
                    for right in tree(i+1, end):
                        res.append(TreeNode(i, left, right))
            return res

        return tree(1, n)
