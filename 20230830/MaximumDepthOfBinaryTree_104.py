#!/usr/bin/python3

""" Easy: Maximum Depth of Binary Tree
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down
to the farthest leaf node.

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """Runtime 91.73%, Memory 12.4%"""
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def recur(tree, level):
            if tree is None:
                return level
            return max(recur(tree.left, level+1), recur(tree.right, level+1))
        return recur(root, 0)


    """Runtime 61.62%, Memory 82.03%"""
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        queue, max_level = deque([(root, 0)]), 0
        while queue:
            cur, level = queue.popleft()
            if cur is None:
                if level > max_level:
                    max_level = level
                continue
            queue.append((cur.left, level+1))
            queue.append((cur.right, level+1))
        return max_level
