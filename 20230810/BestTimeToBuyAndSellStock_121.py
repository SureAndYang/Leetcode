#!/usr/bin/python3

""" Easy: Best Time to Buy and Sell Stock
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different
day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit,
return 0.

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
"""

class Solution:

    # Runtime 92.81%, Memory 62.85%.
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            # Bad input.
            return 0

        buy_price = prices[0]
        max_profit = 0
        for p in prices[1:]:
            if p >= buy_price:
                max_profit = max(max_profit, p - buy_price)
            else:
                # If there will be another maximum price after current price, reset buy-price will
                # get a higher profit.
                # If there will not be any price greater than before, we can't get a higher profit
                # when we don't reset the buy-price. And by resetting the buy-price may get a higher
                # profit in good case like '5, 6, 7, 8, 1, 6'.
                buy_price = p
        return max_profit
