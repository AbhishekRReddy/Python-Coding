'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
122. Best Time to Buy and Sell Stock II

'''

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        i = 0 #Buy day
        profit = 0
        for j in range(1,len(prices)):
            #j is Sell Day
            if prices[j] > prices[i]: 
                #Greedily check for the profit each and everyay
                profit += prices[j] - prices[i]
            i += 1
            j += 1
        return profit    
            
