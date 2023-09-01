#!/usr/bin/python3

""" Medium: Coin Change
You are given an integer array coins representing coins of different denominations and an integer
amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money
cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
"""

class Solution:
    """Runtime 24.20%, Memory 27.06%.

    It seems that we can't improve this solution easily. All codes seem to be essential.
    """
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 2D DP. Row: coins, Col: amount.
        nums = [[-1] * (amount + 1) for _ in range(len(coins))]
        for i in range(len(coins)):
            nums[i][0] = 0
            for j in range(1, amount + 1):
                if i == 0:
                    nums[0][j] = j // coins[i] if j % coins[i] == 0 else -1
                else:
                    nums[i][j] = nums[i-1][j]
                    if j >= coins[i] and nums[i][j-coins[i]] > -1:
                        """Change the if-else as below, runtime goes to 37.81%, memory goes to
                        28.16%. Reduce function 'min' call.

                        + -------
                        if nums[i-1][j] == -1 or nums[i][j-coins[i]] + 1 < nums[i-1][j]:
                            nums[i][j] = nums[i][j-coins[i]] + 1
                        """
                        if nums[i-1][j] == -1:
                            nums[i][j] = nums[i][j-coins[i]] + 1
                        else:
                            nums[i][j] = min(nums[i-1][j], nums[i][j-coins[i]] + 1)
        return nums[-1][-1]


    """A better 2D solution copied from other author, Runtime 72.66%, Memory 52.65%"""
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Very imoortant! `math.inf + 1 == math.inf`.
        dp=[math.inf] * (amount+1)
        dp[0]=0

        for coin in coins:
            for i in range(coin, amount+1):
                if i-coin>=0:
                    dp[i]=min(dp[i], dp[i-coin]+1)

        return -1 if dp[-1]==math.inf else dp[-1]


    """1D DP, I should carefully analysis this solution.

    Runtime 97.43%, Memory 99.67%. This solution is inspired by Coin Change II which was finished
    before.

    For a 2D DP problem, if any cell of the matrix belongs only the last row and the current row,
    this 2D can be compressed into 1D.
    """
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 1D DP.
        nums = [-1] * (amount + 1)
        nums[0] = 0
        for c in coins:
            # c: current coin
            """IMPORTANT !!!
            Can changed into `for j in range(c, amount+1)`, because nums[j] stays still when `j < c`
            """
            for j in range(1, amount+1): # range(c, amount+1)
                # j: current money
                if j >= c and nums[j-c] > -1 and (nums[j] == -1 or nums[j] > nums[j-c] + 1):
                    nums[j] = 1 + nums[j-c]
        return nums[-1]
