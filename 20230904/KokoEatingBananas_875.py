#!/usr/bin/python3

""" Medium: Koko Eating Bananas
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The
guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas
and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead
and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

"""

class Solution:
    """Runtime 79.86%, Memory 96.82%"""
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == h:
            return max(piles)
        if sum(piles) <= h:
            return 1

        i, j, speed = sum(piles) // h, max(piles) + 1, 1
        while i < j:
            mid = (i + j) // 2
            need_hour = sum([math.ceil(p / mid) for p in piles])
            if need_hour <= h:
                j = mid
                speed = mid
            else:
                i = mid + 1
        return speed
