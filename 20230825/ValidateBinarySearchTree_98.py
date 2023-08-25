#!/usr/bin/python3

""" Medium: ValidateBinarySearchTree
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:
    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMin(self, root):
        while root.left is not None:
            root = root.left
        return root.val

    def getMax(self, root):
        while root.right is not None:
            root = root.right
        return root.val

    """Runtime 97.73%, Memory 72.37%"""
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        if root.left and self.getMax(root.left) >= root.val:
            return False
        if root.right and self.getMin(root.right) <= root.val:
            return False
        return self.isValidBST(root.left) and self.isValidBST(root.right)
