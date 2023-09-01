#!/usr/bin/python3

""" Medium: Jump Game II
You are given a 0-indexed array of integers nums of length n. You are initially positioned at
nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words,
if you are at nums[i], you can jump to any nums[i + j] where:
    0 <= j <= nums[i] and
    i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you
can reach nums[n - 1].

"""


class Solution:
    """Runtime 20.21%, Memory 19.32%"""
    def jump(self, nums: List[int]) -> int:
        steps = [math.inf] * len(nums)
        steps[0] = 0
        for i in range(1, len(nums)):
            for j in range(nums[i-1]):
                if i + j >= len(nums):
                    return steps[-1]
                steps[i + j] = steps[i + j] if steps[i + j] < steps[i - 1] + 1 else steps[i - 1] + 1
        return steps[-1]


    """Runtime 29.17%, Memory 75.76%. Definitely same solution with 1, small change makes big
    difference.
    """
    def jump(self, nums: List[int]) -> int:
        steps = [math.inf] * len(nums)
        steps[0] = 0
        for i in range(len(nums)):
            # Make math caculation in `range` to avoid further 'index fix' actions.
            for j in range(i+1, min(len(nums), i+nums[i]+1)):
                if steps[i]+1 < steps[j]:
                    steps[j] = steps[i]+1
        return steps[-1]
