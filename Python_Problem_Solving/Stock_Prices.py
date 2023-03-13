'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
'''

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        global_profit = 0
        left = 0
        right =1
        while right<len(prices):
            if prices[left] < prices[right]:
                local_profit = prices[right] - prices[left]
                global_profit = max(local_profit, global_profit)
            else:
                left = right
            right += 1
        return global_profit
                
        