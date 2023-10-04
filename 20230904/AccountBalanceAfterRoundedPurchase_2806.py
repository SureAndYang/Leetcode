#!/usr/bin/python3

""" Easy: Account Balance After Rounded Purchase
Initially, you have a bank account balance of 100 dollars.

You are given an integer purchaseAmount representing the amount you will spend on a purchase in
dollars.

At the store where you will make the purchase, the purchase amount is rounded to the nearest
multiple of 10. In other words, you pay a non-negative amount, roundedAmount, such that
roundedAmount is a multiple of 10 and abs(roundedAmount - purchaseAmount) is minimized.

If there is more than one nearest multiple of 10, the largest multiple is chosen.

Return an integer denoting your account balance after making a purchase worth purchaseAmount dollars
from the store.

Note: 0 is considered to be a multiple of 10 in this problem.
"""

class Solution:
    """Efficiency change randomly, simple enough."""
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        divide, purchaseAmount = divmod(purchaseAmount, 10)
        return 100 - divide * 10 - (10 if purchaseAmount >= 5 else 0)

    """From other author, good solution."""
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        return (104 -purchaseAmount)//10*10
