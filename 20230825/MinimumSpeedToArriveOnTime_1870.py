#!/usr/bin/python3

""" Medium: Minimum Speed to Arrive on Time
You are given a floating-point number hour, representing the amount of time you have to reach the
office. To commute to the office, you must take n trains in sequential order. You are also given an
integer array dist of length n, where dist[i] describes the distance (in kilometers) of the ith
train ride.

Each train can only depart at an integer hour, so you may need to wait in between each train ride.

For example, if the 1st train ride takes 1.5 hours, you must wait for an additional 0.5 hours before
you can depart on the 2nd train ride at the 2 hour mark.
Return the minimum positive integer min_speed (in kilometers per hour) that all the trains must travel
at for you to reach the office on time, or -1 if it is impossible to be on time.

Tests are generated such that the answer will not exceed 107 and hour will have at most two digits
after the decimal point.

"""

class Solution:

    """Runtime 5% !!! Memory 90.32%, not a good solution
    Brute force way.

    Should take care the numeric precision very very carefully !!!
    """
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        CEIL = lambda x: math.ceil(round(x, 2))

        if hour <= len(dist) - 1:
            return -1
        elif hour <= len(dist):
            return max(max(dist[:-1]), CEIL(dist[-1] / (hour - len(dist) + 1)))
        elif len(dist) == 1:
            return CEIL(dist[0] / hour)

        _min = int(sum(dist) / hour) or 1
        _max = max(max(dist[:-1]), CEIL(dist[-1] / (hour - len(dist) + 1)))
        for i in range(_min, _max+1):
            take_hour = round(sum([math.ceil(d / i) for d in dist[:-1]]) + dist[-1] / i, 2)
            if take_hour <= hour:
                return i
        return -1


    """Runtime 98.93%, Memory 60.88%, Using binary search

    We can use binary search to 'find' a valid value, and 'find' the smallest or largest valid value
    too. The difference is 'we stop' when we want to find 'a' target, and 'go on' when we need to
    find the smallest or largest 'target'.
    """
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        ROUND_CEIL = lambda x: math.ceil(round(x, 2))

        if hour <= len(dist) - 1:
            return -1
        elif hour <= len(dist):
            return max(max(dist[:-1]), ROUND_CEIL(dist[-1] / (hour - len(dist) + 1)))
        elif len(dist) == 1:
            return ROUND_CEIL(dist[0] / hour)

        i = int(sum(dist) / hour) or 1
        j = max(max(dist[:-1]), ROUND_CEIL(dist[-1] / (hour - len(dist) + 1)))
        min_speed = j
        while i <= j:
            mid = (i + j) // 2
            take_hour = round(sum([math.ceil(d / mid) for d in dist[:-1]]) + dist[-1] / mid, 2)
            if take_hour == hour:
                return mid
            elif take_hour < hour:
                min_speed = min(min_speed, mid)
                j = mid - 1
            else:
                i = mid + 1
        return min_speed
