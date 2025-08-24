#
# @lc app=leetcode id=260 lang=python3
#
# [260] Single Number III
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for num in nums:
            xor ^= num
        
        diff_bit = xor & (-xor)
        
        a, b = 0
        
        for num in nums:
            if num & diff_bit:
                a ^= num
            else:
                b ^= num
        return [a,b]
        
# @lc code=end

