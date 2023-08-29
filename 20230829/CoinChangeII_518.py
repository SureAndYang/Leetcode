#!/usr/bin/python3

""" Medium: Coin Change II
You are given an integer array coins representing coins of different denominations and an integer
amount representing a total amount of money.

Return the number of combinations that make up that amount. If that amount of money cannot be made
up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.
The answer is guaranteed to fit into a signed 32-bit integer.

"""

class Solution:
    """FAIL, even if change this solution into memorized-version skipping duplicated computating.

    RecursionError: maximum recursion depth exceeded while calling a Python object.
    """
    def change(self, amount: int, coins: List[int]) -> int:
        if amount <= 0:
            return int(amount == 0)
        if len(coins) == 1:
            return int(amount % coins[0] == 0)

        return self.change(amount - coins[-1], coins) + self.change(amount, coins[:-1])


    """DP, Runtime 47.46%, Memory 42.86%"""
    def change(self, amount: int, coins: List[int]) -> int:
        if amount <= 0:
            return int(amount == 0)
        if len(coins) == 1:
            return int(amount % coins[0] == 0)

        """1, Adding this line, Runtime goes to 48.07%, Memory goes to 45.24%. A little better"""
        # Remove useless coins.
        coins = [n for n in coins if n <= amount]

        # row: coins, col: amount
        solutions = [[0] * (amount+1) for _ in range(len(coins))]
        for i in range(len(coins)):
            for j in range(amount + 1):
                """2, By seperating i==0 and j==0, Runtime goes to 49.12%.
                Because when j == 0, we can assign solutions[i][0] = 1 without any comparision.
                """
                if i == 0 or j == 0:
                    # One coin
                    solutions[i][j] = int(j % coins[i] == 0)
                elif j >= coins[i]:
                    solutions[i][j] = solutions[i][j-coins[i]] + solutions[i-1][j]
                else:
                    solutions[i][j] = solutions[i-1][j]

        return solutions[-1][-1]


    """Optimized 1D DP, from other author, Runtime 94.98%, Memory 68.12%.

    Very important, try to optimize 2D DP into 1D can save a lot of time and memory.
    """
    def change(self, amount: int, coins: List[int]) -> int:
        dp=[1]+[0]*amount
        for c in coins:
            for i in range(c, amount+1):
                dp[i]+=dp[i-c]
        return dp[amount]
