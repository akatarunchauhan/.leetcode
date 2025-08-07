#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        profit = 0
        while (r < len(prices)):
            if (prices[r] > prices[l]):
                curr_profit = prices[r] - prices[l]
                profit = max(profit, curr_profit)
            else:
                l = r
            r += 1
        
        return profit
                
        
        
# @lc code=end

