#!/usr/bin/python3

""" Medium: Search in Rotated Sorted Array
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k
(1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1],
nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at
pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target
if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.
"""

class Solution:

    # Runtime 73.41%, Memory 6.15%. As I use recursion, the memory will be high.
    def search_1(self, nums: List[int], target: int) -> int:
        # When we got a runtime as O(logN), we should use binary search.
        # It's similar with the 'binary search in sorted array', but it's more complex in diciding
        # which half we should check.
        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        mid = len(nums) // 2
        if nums[0] < nums[mid]:
            # Left half is sorted.
            if target >= nums[0] and target <= nums[mid-1]:
                return self.search(nums[:mid], target)
            else:
                found = self.search(nums[mid:], target)
                return mid + found if found > -1 else -1
        else:
            # Right half is sorted.
            if target >= nums[mid] and target <= nums[-1]:
                found = self.search(nums[mid:], target)
                return mid + found if found > -1 else -1
            else:
                return self.search(nums[:mid], target)


    # Runtime 73.41%, Memory 37.38%. Use list two pointer to cut the sub-list.
    # Code is exactly the same with one solution whose authur noted runtime as 99.8%.
    def search_2(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1
        while i < j:
            mid = (i + j + 1) // 2

            # If left part has one number, it's sorted.
            if i == mid - 1 or nums[i] < nums[mid-1]:
                # Left half is sorted.
                if nums[i] <= target <= nums[mid-1]:
                    j = mid - 1
                else:
                    i = mid
            else:
                # Right half is sorted.
                if nums[mid] <= target <= nums[j]:
                    i = mid
                else:
                    j = mid - 1
        return i if nums[i] == target else -1


    # Runtime 92%, Memory 94% as author noted. I can learn about the package `bisect`.
    def search_3(self, nums: List[int], target: int) -> int:
        """ Actually, this should not be a solution, but why I put it here is to let me know some
        packages those I'm not familar with.

        With the help of function 'bisect.bisect_left' from package `bisect`, we can easily get the
        "rotate times in a rotated sorted array" or "index of the minimum number in a rotated sorted
        array".
        This is a cheating solution. But we can still learn something in it, even when we meet a
        similar question in real work, there is no limit what solution we use.
        """

        # Find the first element which is smaller than nums[0]. Thus, find the minimum number index.
        # As the function uses binary search to find it, the runtime will be O(logN).
        k = bisect_left(nums, True, key = lambda x: x < nums[0])

        # Seperate the array into two 'sorted' parts. All numbers in right parts are smaller than
        # those in the left part.
        if target  >= nums[0]:
            left = bisect_left(nums, target, hi = k-1)
            return left if nums[left] == target else -1
        rght = bisect_left(nums, target, lo = k)

        # (this line to avoid index out of range)
        return rght if rght < len(nums) and nums[rght] == target else -1           #
