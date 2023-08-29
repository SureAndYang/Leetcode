#!/usr/bin/python3

""" Medium: Reorganize String

Given a string s, rearrange the characters of s so that any two adjacent characters are not the same
Return any possible rearrangement of s or return "" if not possible.
"""

class Solution:
    """Runtime 5.51%, Memory 76.57%"""
    def reorganizeString_1(self, s: str) -> str:
        """Using list will save memory but waste time"""
        counter = [0] * 26
        for char in s:
            counter[ord(char)-ord("a")] += 1

        if max(counter) > (len(s) + 1) // 2:
            return ""

        res, last = [], None
        while sum(counter) > 0:
            """I should find the best data structure to store data, so that I can get the max fast.
            Thus, I should think about data structures returning maximum in O(1) time.

            SHOULD BE MORE FAMALIAR WITH heapq.
            """
            index = max([(i, n) for i, n in enumerate(counter) if i != last], key=lambda x:x[1])[0]
            res.append(chr(ord("a") + index))
            last = index
            counter[index] -= 1

        return ''.join(res)


    """Runtime 17.35%, Memory 76.57%"""
    def reorganizeString_2(self, s: str) -> str:
        counter = defaultdict(int)
        for char in s:
            counter[char] += 1

        if max(counter.values()) > (len(s) + 1) // 2:
            return ""

        res = ['A']
        while len(res) < len(s) + 1:
            char = max([(k, v) for k, v in counter.items() if k != res[-1]], key=lambda x:x[1])[0]
            res.append(char)
            counter[char] -= 1

        return ''.join(res[1:])


    """ Runtime 89.53%, Memory 76.57%

    Inspired by other author, talking about priorityqueue.
    """
    def reorganizeString(self, s: str) -> str:
        counter = [0] * 26
        for char in s:
            counter[ord(char) - ord("a")] += 1

        if max(counter) > (len(s) + 1) // 2:
            return ""

        queue = []
        for i, n in enumerate(counter):
            if n == 0:
                continue
            char = chr(ord("a") + i)
            heapq.heappush(queue, (-n, char))

        res, last = [], (0, '')
        while queue:
            n, char = heapq.heappop(queue)
            res.append(char)
            if last[0] < 0:
                heapq.heappush(queue, last)
            last = (n+1, char)
        return ''.join(res)
