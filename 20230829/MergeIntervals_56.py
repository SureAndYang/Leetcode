#!/usr/bin/python3

""" Medium: Merge Intervals
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
and return an array of the non-overlapping intervals that cover all the intervals in the input.
"""

class Solution:
    """Runtime 5.09%, Memory 56.07%"""
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals

        intervals.sort(key=lambda x:x[1])
        res = []
        for i in range(len(intervals)):
            for j in range(len(res)):
                if intervals[i][0] <= res[j][1]:
                    res[j:] = [[min(intervals[i][0], res[j][0]), intervals[i][1]]]
                    break
            else:
                res.append(intervals[i])
        return res


    """Runtime 36.51%, Memory 56.07%"""
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals

        """The sorting should be chosen properly. In some cases, we need to sort the array by
        ending, but in this case we should sort it by starting"""
        intervals.sort()
        res, cur = [], intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= cur[1]:
                """By replacing the 'min' and 'max' functions with if-condition, the Runtime goes to
                96.26%. It's a giant improvement !

                Change the following code like,

                if cur[0] > intervals[i][0]:
                    cur[0] = intervals[i][0]
                if cur[1] < intervals[i][1]:
                    cur[1] = intervals[i][1]

                This can reduce function-calling actions and value-assigning actions (no value
                assignment when if-condition is False).
                """
                cur[0] = min(cur[0], intervals[i][0])
                cur[1] = max(cur[1], intervals[i][1])
            else:
                res.append(cur)
                cur = intervals[i]
        res.append(cur)
        return res
