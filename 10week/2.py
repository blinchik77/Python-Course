"""
https://leetcode.com/problem-list/binary-tree/
url: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii
"""


class Solution(object):
    def maxProfit(self, prices):
        maximumProfit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                maximumProfit += prices[i] - prices[i - 1]
        return maximumProfit
