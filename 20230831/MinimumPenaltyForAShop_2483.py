#!/usr/bin/python3

""" Medium: Minimum Penalty for a Shop
You are given the customer visit log of a shop represented by a 0-indexed string customers
consisting only of characters 'N' and 'Y':
    if the ith character is 'Y', it means that customers come at the ith hour
    whereas 'N' indicates that no customers come at the ith hour.

If the shop closes at the jth hour (0 <= j <= n), the penalty is calculated as follows:
    For every hour when the shop is open and no customers come, the penalty increases by 1.
    For every hour when the shop is closed and customers come, the penalty increases by 1.
    Return the earliest hour at which the shop must be closed to incur a minimum penalty.

Note that if a shop closes at the jth hour, it means the shop is closed at the hour j.

"""

class Solution:
    """Runtime 42.51% O(n), Memory 90.56% O(1). Two Round"""
    def bestClosingTime_3(self, customers: str) -> int:
        close_time, total_Y = 0, 0
        for status in customers:
            if status == 'Y':
                total_Y += 1
        total_N = len(customers) - total_Y

        close_time, penalty, cur_Y, cur_N = -1, total_Y, 0, 0
        for i in range(len(customers)):
            if customers[i] == 'Y':
                cur_Y += 1
            else:
                cur_N += 1
            if cur_N + total_Y - cur_Y < penalty:
                close_time = i
                penalty = cur_N + total_Y - cur_Y
        return close_time + 1


    """Runtime 99.73% O(n), Memory 66.28% O(1). One Round. Improved from solution3"""
    def bestClosingTime_2(self, customers: str) -> int:
        min_penalty, close_time, last_penalty = 0, 0, 0
        for i, status in enumerate(customers, start=1):
            if status == 'Y':
                min_penalty += 1
                if last_penalty < min_penalty:
                    min_penalty = last_penalty
                    close_time = i
            else:
                last_penalty += 1
        return close_time

    """The 3rd solution is improved from the below code which I tried to use 1D DP. And I
    found 1D DP can be compressed into O(1) in advance.

    Note: the following code needs 2 rounds too, and time complexity tends to be O(n^2) which
    beyonds the limit. But it's still a hint to the O(1) DP.

    Solution valid but time beyonds the limit.
    """
    def bestClosingTime_3(self, customers: str) -> int:
         penalty = [0] * (len(customers) + 1)
         for i, status in enumerate(customers, start=1):
             # Close after the current status.
             if status == 'Y':
                 penalty[i] = penalty[i-1]
                 for j in range(i):
                     penalty[j] += 1
             else:
                 penalty[i] = penalty[i-1] + 1

         min_penalty, close_time = len(penalty), 0
         for i in range(len(penalty)):
             if penalty[i] < min_penalty:
                 min_penalty = penalty[i]
                 close_time = i
         return close_time
