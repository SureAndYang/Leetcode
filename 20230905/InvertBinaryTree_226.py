#!/usr/bin/python3

""" Easy: Invert Binary Tree
Given the root of a binary tree, invert the tree, and return its root.

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """Runtime 73.67%, Memory 67.73%. Very simple"""
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
