#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)
        prefix = 1
        postfix = 1
        
        for i in range(1,len(nums)):
            prefix *= nums[i-1]
            answer[i] = prefix
        for i in range(len(nums)-2,-1,-1):
            postfix *= nums[i+1]
            answer[i] *= postfix
        return answer
# @lc code=end

