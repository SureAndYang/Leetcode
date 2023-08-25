#!/usr/bin/python3

""" Sliding Window Maximum
You are given an array of integers nums, there is a sliding window of size k which is moving from
the very left of the array to the very right. You can only see the k numbers in the window. Each
time the sliding window moves right by one position.

Return the max sliding window.
"""

import heapq
class Solution:

    """Runtime 5.02%, Memory 90.01%"""
    def maxSlidingWindow_1(self, nums: List[int], k: int) -> List[int]:
        if len(nums) <= k:
            return [max(nums[:k])]

        result, counter = [nums[0]], {}
        for i in range(k):
            if nums[i] not in counter:
                counter[nums[i]] = 1
            else:
                counter[nums[i]] += 1
            result[0] = max(result[0], nums[i])

        for i in range(1, len(nums)-k+1):
            counter[nums[i-1]] -= 1
            if counter[nums[i-1]] == 0:
                del counter[nums[i-1]]
            if nums[i+k-1] in counter:
                counter[nums[i+k-1]] += 1
            else:
                counter[nums[i+k-1]] = 1

            if nums[i+k-1] >= result[-1]:
                result.append(nums[i+k-1])
            elif nums[i-1] < result[-1]:
                result.append(result[-1])
            elif nums[i-1] in counter:
                result.append(result[-1])
            else:
                result.append(max(counter.keys()))

        return result

    import heapq as hq


    """Runtime 53.68%, Memory 12.04%, Should be familiar with `heapq`"""
    def maxSlidingWindow_2(self, nums: List[int], k: int) -> List[int]:
        max_index = {}
        for i in range(k):
            max_index[nums[i]] = i

        queue = []
        for n in max_index:
            hq.heappush(queue, -n)

        max_num = - hq.heappop(queue)
        max_numlist, cur_max_index = [max_num], max_index[max_num]
        del max_index[max_num]

        for i in range(1, len(nums)-k+1):
            while cur_max_index < i:
                if not queue:
                    max_num, cur_max_index = None, None
                    break
                max_num = - hq.heappop(queue)
                cur_max_index = max_index[max_num]
                del max_index[max_num]
            if max_num is None or nums[i+k-1] >= max_num:
                max_num = nums[i+k-1]
                cur_max_index = i + k - 1
            else:
                if nums[i+k-1] not in max_index:
                    hq.heappush(queue, -nums[i+k-1])
                max_index[nums[i+k-1]] = i + k - 1
            max_numlist.append(max_num)

        return max_numlist


    """ Best way ever seen. More memory saving by using only a list.
    https://leetcode.com/problems/sliding-window-maximum/solutions/3919643/python-short-and-clean/
    """
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        mq = deque()
        maxes = []

        for i in range(len(nums)):
            if mq and mq[0] <= i - k:
                mq.popleft()
            while mq and nums[mq[-1]] <= nums[i]:
                mq.pop()

            mq.append(i)
            if i >= k - 1:
                maxes.append(nums[mq[0]])

        return maxes
