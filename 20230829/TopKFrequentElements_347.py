#!/usr/bin/python3

""" Medium: Top K Frequent Elements
Given an integer array nums and an integer k, return the k most frequent elements. You may return
the answer in any order.

"""

class Solution:
    """Runtime 91.69%, Memory 49.48%"""
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        for n in nums:
            counter[n] += 1

        res = sorted([(n, cnt) for n, cnt in counter.items()], key=lambda x:x[1], reverse=True)[:k]
        return [item[0] for item in res]


    """Runtime 74.58%, Memory 66.86%. Using heapq"""
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        for n in nums:
            counter[n] += 1

        queue = []
        for n, cnt in counter.items():
            heapq.heappush(queue, (-cnt, n))

        res = []
        for _ in range(k):
            res.append(heapq.heappop(queue)[1])
        return res
