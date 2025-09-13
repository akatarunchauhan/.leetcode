#
# @lc app=leetcode id=523 lang=python3
#
# [523] Continuous Subarray Sum
#

# @lc code=start
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder = {0:-1}
        currSum = 0
        for i,n in enumerate(nums):
            currSum += n
            r = currSum % k 
            if r not in remainder:
                remainder[r] = i
            elif i-remainder[r] > 1:
                return True
        return False
# @lc code=end

