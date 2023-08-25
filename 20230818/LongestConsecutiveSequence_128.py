#!/usr/bin/python3

""" Medium: Longest Consecutive Sequence
Given an unsorted array of integers nums, return the length of the longest consecutive elements
sequence.

You must write an algorithm that runs in O(n) time.

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
"""

class Solution:

    # Runtime 74.11%, Memory 14.45%. Some 'better' solution takes O(nlogn) time which doesn't meet
    # the requirement.
    # Someone say, it should be 'hard' for O(n).
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        # {start: (end, longest_sequence_len)} {end: (start, longest_sequence_len)}
        starts, ends = {}, {}
        for n in nums:
            if n in starts or n in ends:
                continue
            if n + 1 in starts or n - 1 in ends:
                if n + 1 in starts:
                    starts[n] = starts[n+1]
                    del starts[n+1]
                    ends[starts[n]] = n
                if n - 1 in ends:
                    ends[n] = ends[n-1]
                    del ends[n-1]
                    starts[ends[n]] = n
                if n in starts and n in ends:
                    starts[ends[n]] = starts[n]
                    ends[starts[n]] = ends[n]
                    del starts[n], ends[n]
            else:
                starts[n] = n
                ends[n] = n

        return max([v - k + 1 for k, v in starts.items()])


    # Runtime: 90.18%, Memort 36.59%. From Leetcode, though there is two 'while' loop, every number
    # will only be hanlded once and the time complexity is O(n).
    def longestConsecutive_2(self, nums: List[int]) -> int:
        uniques = set(nums)
        max_length = 0

        while uniques:
            low = high = uniques.pop()

            while low - 1 in uniques or high + 1 in uniques:
                if low - 1 in uniques:
                    uniques.remove(low - 1)
                    low -= 1

                if high + 1 in uniques:
                    uniques.remove(high + 1)
                    high += 1

            max_length = max(high - low + 1, max_length)

        return max_length
