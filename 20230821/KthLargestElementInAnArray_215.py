#!/usr/bin/python3

"""
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

Constraints:
    1 <= k <= nums.length <= 10^5
    -10^4 <= nums[i] <= 10^4
"""

import heapq as hq
class Solution:
    """Runtime 27.29%, Memory 22.51%"""
    def findKthLargest_1(self, nums: List[int], k: int) -> int:
        l = []
        for n in nums:
            hq.heappush(l, -n)

        for i in range(k):
            n = - hq.heappop(l)
        else:
            return n


    """Runtime 52.62%, Memory 66.84%
    This solution is simpler and better in ether time or space complexity.

    Based on the constraints '-10^4 <= nums[i] <= 10^4', we can get the maximum length of the
    'counter' as 20001 which is acceptable.
    Without this constraint, this solution can't be passed because the input [1, 1000000000000] will
    generate a counter whose length is 1000000000000.


    time complexity of worst case as O(n).
    """
    def findKthLargest_2(self, nums: List[int], k: int) -> int:
        _min, _max = min(nums), max(nums)
        counter = [0] * (_max - _min + 1)
        for n in nums:
            counter[n-_min] += 1

        largest_n = 0
        for i in range(len(counter)-1, -1, -1):
            largest_n += counter[i]
            if largest_n >= k:
                return _min + i


    """Runtime 22.86%, Memory 46.95%
    O(nlogn), because the time complexity of 'heappush' or 'heappop' is O(logn).
    """
    def findKthLargest_3(self, nums: List[int], k: int) -> int:
        min_heap = []

        for n in nums:
            heapq.heappush(min_heap, n)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return min_heap[0]


    """Best algorithm but not passed.
    If the input has only distinct numbers or the count of duplicated elements is not large, this
    solution will be the best.

    This solution will get 'out of time limit' when the input is like '[1, 2, 3, 4, 5, ..., 5, 10]',
    in which the number '5' repeated about 10^5 times.
    And in this worst case, the time complexity is nearly O(n^2).
    """
    def findKthLargest_3(self, nums: List[int], k: int) -> int:
        l, mid, r = 0, 0, len(nums)
        while l < r:
            for i in range(l, r-1):
                if nums[i] < nums[r-1]:
                    nums[i], nums[mid] = nums[mid], nums[i]
                    mid += 1
            # Last element is in its right place
            nums[r-1], nums[mid] = nums[mid], nums[r-1]

            if r - mid == k:
                return nums[mid]
            elif r - mid > k:
                mid += 1
                l = mid
            else:
                k = k - (r - mid)
                mid, r = l, mid
        return nums[mid]
