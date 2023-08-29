#!/usr/bin/python3

""" Medium: Combinations
Given two integers n and k, return all possible combinations of k numbers chosen from the range
[1, n].

You may return the answer in any order.


SHOULD KNOW ABOUT itertools.combinations(iterable, r) WHICH CAN GENERATE ALL COMBINATIONS.
"""

class Solution:

    """Runtime 5.02%, Memory 5.56%, It's a valid but not-good solution.

    I read some solutions from other authors, a better thought is to use 'backtracking' whose time
    complexity is similar with the current solution even though they claim as 'beat 99%'.

    Most 'efficient' solutions are all the same using collections.combinations().
    """
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k > n:
            return []
        if k == 1:
            return [[i+1] for i in range(n)]
        """Combine two list using '+' is very slow and memory-consuming"""
        return [[n] + c for c in self.combine(n-1, k-1)] + self.combine(n-1, k)
