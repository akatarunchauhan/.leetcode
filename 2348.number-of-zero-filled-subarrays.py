#
# @lc app=leetcode id=2348 lang=python3
#
# [2348] Number of Zero-Filled Subarrays
#

# @lc code=start
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        result = 0
        count = 0
        
        for i in range(len(nums)):
            if(nums[i] == 0):
                count += 1
                result += count
            else:
                count = 0
        return result
# @lc code=end

