#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<nums[i+1]:
                for j in range(len(nums)-1,i,-1):
                    if nums[j]>nums[i]:
                        nums[j],nums[i] = nums[i], nums[j]
                        nums[i+1:] = nums[i+1:][::-1]
                        return
        nums[::] = nums[::-1]          
        
# @lc code=end

