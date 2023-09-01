#!/usr/bin/python3

""" Medium: Minimum ASCII Delete Sum for Two Strings
Given two strings s1 and s2, return the lowest ASCII sum of deleted characters to make two strings
equal.
"""

class Solution:
    """2D DP, Runtime 69.57%, Memory 46.25%"""
    def minimumDeleteSum_1(self, s1: str, s2: str) -> int:
        mat = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        for i in range(1, len(s2) + 1):
            mat[0][i] = mat[0][i-1] + ord(s2[i-1])

        for i1 in range(1, len(s1) + 1):
            mat[i1][0] = mat[i1-1][0] + ord(s1[i1-1])
            for i2 in range(1, len(s2) + 1):
                if s1[i1-1] == s2[i2-1]:
                    mat[i1][i2] = mat[i1-1][i2-1]
                else:
                    mat[i1][i2] = min(mat[i1-1][i2] + ord(s1[i1-1]), mat[i1][i2-1] + ord(s2[i2-1]))
        return mat[-1][-1]


    """Runtime 52.98%, Memory 94.60%.

    2D DP problems, if any element relies on only the last line and the current line, this 2D DP can
    be compressed into 2-lines-DP. Thus, space complexity goes from O(m*n) to O(n).

    And if any element relies on only the current line (items before), it can be compressed into 1D
    DP, or even O(1) space using several variables.
    """
    def minimumDeleteSum_2(self, s1: str, s2: str) -> int:
        # 2D DP, when any element relies only on the last line and current line, it can be
        # compressed into 2-lines-DP.
        mat = [[0] * (len(s2) + 1) for _ in range(2)]
        for i in range(1, len(s2) + 1):
            mat[0][i] = mat[0][i-1] + ord(s2[i-1])

        for i1 in range(1, len(s1) + 1):
            mat[i1%2][0] = mat[i1%2-1][0] + ord(s1[i1-1])
            for i2 in range(1, len(s2) + 1):
                if s1[i1-1] == s2[i2-1]:
                    mat[i1%2][i2] = mat[i1%2-1][i2-1]
                else:
                    mat[i1%2][i2] = min(mat[i1%2-1][i2] + ord(s1[i1-1]),
                                        mat[i1%2][i2-1] + ord(s2[i2-1]))
        return mat[i1%2][-1]


    """Runtime 66.83%, Memory 89.16%. Small change makes big difference in memory."""
    def minimumDeleteSum_3(self, s1: str, s2: str) -> int:
        # 2D DP, when any element relies only on the last line and current line, it can be
        # compressed into 2-lines-DP.
        mat = [[0] * (len(s2) + 1) for _ in range(2)]
        for i in range(1, len(s2) + 1):
            mat[0][i] = mat[0][i-1] + ord(s2[i-1])

        for i1 in range(1, len(s1) + 1):
            # Computing 'i1 % 2' only once saves much time compared with solution 2.
            i1_fix = i1 % 2
            mat[i1_fix][0] = mat[i1_fix-1][0] + ord(s1[i1-1])
            for i2 in range(1, len(s2) + 1):
                if s1[i1-1] == s2[i2-1]:
                    mat[i1_fix][i2] = mat[i1_fix-1][i2-1]
                else:
                    mat[i1_fix][i2] = min(mat[i1_fix-1][i2] + ord(s1[i1-1]),
                                        mat[i1_fix][i2-1] + ord(s2[i2-1]))
        return mat[i1%2][-1]


    """Runtime 79.09%, Memory 98.50%. Small improvement from solution 3.

    By using 'last' and 'cur', we avoid calculate the 'i % 2' repeatedly, this can save some time.
    """
    def minimumDeleteSum_4(self, s1: str, s2: str) -> int:
        # 2D DP, when any element relies only on the last line and current line, it can be
        # compressed into 2-lines-DP.
        cur = [0] * (len(s2) + 1)
        last = [0] * (len(s2) + 1)
        for i in range(1, len(s2) + 1):
            last[i] = last[i-1] + ord(s2[i-1])

        for i1 in range(1, len(s1) + 1):
            cur[0] = last[0] + ord(s1[i1-1])
            for i2 in range(1, len(s2) + 1):
                if s1[i1-1] == s2[i2-1]:
                    cur[i2] = last[i2-1]
                else:
                    cur[i2] = min(last[i2] + ord(s1[i1-1]), cur[i2-1] + ord(s2[i2-1]))
            cur, last = last, cur
        return last[-1]
