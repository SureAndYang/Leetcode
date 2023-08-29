#!/usr/bin/python3

""" Medium: Minimize the Maximum Difference of Pairs
You are given a 0-indexed integer array nums and an integer p. Find p pairs of indices of nums such
that the maximum difference amongst all the pairs is minimized. Also, ensure no index appears more
than once amongst the p pairs.

Note that for a pair of elements at the index i and j, the difference of this pair is |nums[i] -
nums[j]|, where |x| represents the absolute value of x.

Return the minimum maximum difference among all p pairs. We define the maximum of an empty set to be
zero.

Examples:
    Input: nums = [10,1,2,7,1,3], p = 2
    Output: 1
    Explanation: The first pair is formed from the indices 1 and 4, and the second pair is formed
        from the indices 2 and 5. The maximum difference is max(|nums[1] - nums[4]|, |nums[2] - 
        nums[5]|) = max(0, 1) = 1. Therefore, we return 1.

    Input: nums = [1, 0, 1, 3], p = 2
    Output: 2
    Explanation: Pairs (0, 1) and (1, 3). The maximum difference is 2.
"""

class Solution:
    """Very Important !!! This problem is solved by hints. Runtime 92.4%, Memory 66.93%.

    This problem shows that 'unfamiliar variant' from 'binary search' !
    """
    def minimizeMax(self, nums: List[int], p: int) -> int:
        def pair_counter(diffs, threshold):
            i, pairs = 0, 0
            while i < len(diffs):
                if diffs[i] <= threshold:
                    i += 2
                    pairs += 1
                else:
                    i += 1
            return pairs

        if len(nums) < 2 or not p:
            return 0

        # O(nlogn)
        nums = sorted(nums)
        diffs = [nums[i+1] - nums[i+1] for i in range(len(nums)-1)]
        min_diff, max_diff = 0, nums[-1] - nums[0]
        res = max_diff
        while min_diff < max_diff:
            mid = (max_diff + min_diff) // 2
            pairs = pair_counter(diffs, mid)
            if pairs >= p:
                res = min(res, mid)
                max_diff = mid - 1
            else:
                min_diff = mid + 1

        return min_diff if pair_counter(diffs, min_diff) >= p else res
