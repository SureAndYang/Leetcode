#!/usr/bin/python3

""" Medium: 3 Sum
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j,
i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""

class Solution:

    # Runtime 24%, Memory 40.94%.
    def threeSum_1(self, nums: List[int]) -> List[List[int]]:
        results = set()

        number_indexes = {}
        for i, n in enumerate(nums):
            if n in number_indexes:
                number_indexes[n].append(i)
            else:
                number_indexes[n] = [i]

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)):

                left = 0 - nums[i] - nums[j]
                if left not in number_indexes:
                    continue
                if left in {nums[i], nums[j]} and len(number_indexes[left]) == 1:
                    continue

                for v in number_indexes[left]:
                    if v <= j:
                        continue

                    # I think this is very bad code.
                    results.add(tuple(sorted([nums[i], nums[j], nums[v]])))

        return list(results)


    # Runtime 95.16%, Memory 12.4%. Better solution than threeSum_1.
    def threeSum_2(self, nums: List[int]) -> List[List[int]]:
        results = []

        counter = {}
        for i, n in enumerate(nums):
            if n in counter:
                counter[n] += 1
            else:
                counter[n] = 1

        # Normal time complexity is O(N**2), then sort algorithm as O(N*logN) is acceptable.
        nums = sorted(counter.keys())

        # nums is sorted now.
        for i in range(len(nums)):

            if nums[i] == 0:
                # When the first number is 0, all following numbers are bigger than 0. Thus there is
                # only one possible combination which is [0, 0, 0].
                if counter[nums[i]] >= 3:
                    results.append([0, 0, 0])
                break

            for j in range(i+1, len(nums)):
                left = 0 - nums[i] - nums[j]
                if left not in counter:
                    continue

                # `left > nums[j]` means to deduplicate.
                if left in {nums[i], nums[j]} and counter[left] > 1 or left > nums[j]:
                    results.append([nums[i], nums[j], left])

        return results
