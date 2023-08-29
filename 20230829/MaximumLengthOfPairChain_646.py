#!/usr/bin/python3

""" Medium: Maximum Length of Pair Chain
You are given an array of n pairs pairs where pairs[i] = [lefti, righti] and lefti < righti.

A pair p2 = [c, d] follows a pair p1 = [a, b] if b < c. A chain of pairs can be formed in this
fashion.

Return the length longest chain which can be formed.
You do not need to use up all the given intervals. You can select pairs in any order.
"""

class Solution:
    """Runtime 56.95%, Memory 31.78%"""
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pair_dict = {}
        for l, r in pairs:
            if l not in pair_dict or r < pair_dict[l]:
                pair_dict[l] = r

        """Sort all pairs by 'end' point. When a pair contains or interacts another pair, we choose
        the pair whose end point is small, this can leave more space for the following pairs."""
        pairs = sorted(pair_dict.items(), key=lambda x: x[1])
        cnt, pivot = 1, pairs[0]
        for i in range(1, len(pairs)):
            if pairs[i][0] > pivot[1]:
                cnt += 1
                pivot = pairs[i]
        return cnt


    """Runtime 54.03%, Memory 63.51%.

    The aim of using dict is to choose a small-gap pair when two
    pairs having the same start. With the improvment in time & memory from 1st solution, we can find
    there aren't many pairs with definitely same starts.
    """
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs = sorted(pairs, key=lambda x: x[1])
        """Replace 'pivot' from a set to just a integer because we only use pivot[1].
        This can make the time going to 60.65% and memory going to 63.51%.
        """
        cnt, pivot = 1, pairs[0]
        for i in range(1, len(pairs)):
            if pairs[i][0] > pivot[1]:
                cnt += 1
                pivot = pairs[i]
        return cnt
