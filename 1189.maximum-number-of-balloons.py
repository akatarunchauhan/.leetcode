#
# @lc app=leetcode id=1189 lang=python3
#
# [1189] Maximum Number of Balloons
#

# @lc code=start
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counterText = Counter(text)
        balloon = Counter("balloon")
        
        res = len(text)
        
        for char in balloon:
            res = min(res, counterText[char] // balloon[char])
        return res
# @lc code=end

