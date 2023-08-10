#!/usr/bin/python3

""" Easy: Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the
input string is valid.

An input string is valid if:
    1. Open brackets must be closed by the same type of brackets.
    2. Open brackets must be closed in the correct order.
    3. Every close bracket has a corresponding open bracket of the same type.
"""

class Solution:

    # Runtime 92.6%, Memory: 54.32%.
    def isValid(self, s: str) -> bool:
        open_dict = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for char in s:
            if char in open_dict:
                stack.append(char)

            # Note that: When the program run to `stack.pop()`, the stack will truely delete one
            # element. Thus even the input doesn't meet this if-condition, the stack changed already
            elif len(stack) == 0 or open_dict[stack.pop()] != char:
                return False
        return len(stack) == 0
