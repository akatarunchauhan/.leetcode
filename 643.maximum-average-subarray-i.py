#
# @lc app=leetcode id=643 lang=python3
#
# [643] Maximum Average Subarray I
#

# @lc code=start
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        currSum = 0
        for i in range(k):
            currSum+=nums[i]
        maxAvg = currSum/k
        for i in range(k,len(nums)):
            currSum+=nums[i]
            currSum-=nums[i-k]
            avg = currSum/k
            maxAvg = max(maxAvg,avg)
        return maxAvg
# @lc code=end

