#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        for _ in prices:
            buy_index = prices.index(min(prices))
            sell_index =  prices.index(max(prices))
            
            if (buy_index < sell_index):
                profit = max(prices) - min(prices)
            elif(prices.index(max(prices))<prices.index(min(prices))):
                prices.remove(max(prices))
            # elif(prices.index(max(prices))<prices.index(min(prices))):
            #     prices.remove(max(prices))
                # prices.remove(min(prices))
                
        return profit
        
        
# @lc code=end

