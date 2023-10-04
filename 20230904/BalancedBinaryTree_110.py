#!/usr/bin/python3

""" Easy: Balanced Binary Tree
Given a binary tree, determine if it is height-balanced.

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """Runtime 41.59%, Memory 47.67%"""
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def get_depth(root):
            if root:
                return 1 + max(get_depth(root.left), get_depth(root.right))
            else:
                return 1

        if not root:
            return True
        return abs(get_depth(root.left) - get_depth (root.right)) <= 1 and (
            self.isBalanced(root.left) and self.isBalanced(root.right)
        )


    """Runtime 95.03%, Memory 33.08%"""
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def is_balanced(root, depth):
            if root is None:
                return True, depth

            left, left_dep = is_balanced(root.left, depth + 1)
            right, right_dep = is_balanced(root.right, depth + 1)
            return left and right and abs(left_dep - right_dep) <= 1, max(left_dep, right_dep)

        return is_balanced(root, 0)[0]
