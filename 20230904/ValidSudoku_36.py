#!/usr/bin/python3

""" Medium: Valid Sudoku
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to
the following rules:
    Each row must contain the digits 1-9 without repetition.
    Each column must contain the digits 1-9 without repetition.
    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:
    A Sudoku board (partially filled) could be valid but is not necessarily solvable.
    Only the filled cells need to be validated according to the mentioned rules.
"""

class Solution:
    """Runtime 60.32%, Memory 13.16%"""
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def is_valid(nums):
            nums = [n for n in nums if n != "."]
            return len(set(nums)) == len(nums)

        for row in board:
            if not is_valid(row):
                return False

        for col in range(9):
            nums = []
            for row in range(9):
                nums.append(board[row][col])
            if not is_valid(nums):
                return False

        for subbox_col in range(3):
            for subbox_row in range(3):
                nums = board[subbox_row * 3][subbox_col * 3: (subbox_col + 1) * 3]
                nums.extend(board[subbox_row * 3 + 1][subbox_col * 3: (subbox_col + 1) * 3])
                nums.extend(board[subbox_row * 3 + 2][subbox_col * 3: (subbox_col + 1) * 3])
                if not is_valid(nums):
                    return False

        return True


    """Runtime 79.42%, Memory 49.29%. By pre-process the nums before calling is_valid(), reduce much
    memory"""
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def is_valid(nums):
            return len(set(nums)) == len(nums)

        for row in board:
            if not is_valid([n for n in row if n != "."]):
                return False

        for col in range(9):
            if not is_valid([row[col] for row in board if row[col] != "."]):
                return False

        for subbox_col in range(3):
            for subbox_row in range(3):
                nums = [n for n in board[subbox_row * 3][subbox_col * 3: (subbox_col + 1) * 3]
                        if n != "."]
                nums.extend([
                    n for n in board[subbox_row * 3 + 1][subbox_col * 3: (subbox_col + 1) * 3]
                    if n != "."])
                nums.extend([
                    n for n in board[subbox_row * 3 + 2][subbox_col * 3: (subbox_col + 1) * 3]
                    if n != "."])
                if not is_valid(nums):
                    return False

        return True
