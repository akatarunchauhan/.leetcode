#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans =  []
        for i in range(len(nums)):
            low = i+1
            high = len(nums)-1
            if nums[i]>0:
                break
            elif i>0 and nums[i] == nums[i-1]:
                continue
            while low<high:
                if nums[i]+nums[low]+nums[high] == 0:
                    ans.append([nums[i],nums[low],nums[high]])
                    low +=1
                    high -=1
                    while low<high and nums[low] == nums[low-1]:
                        low+=1
                    while low<high and nums[high] == nums[high+1]:
                        high-=1
                elif nums[i]+nums[low]+nums[high] < 0:
                    low+=1
                elif nums[i]+nums[low]+nums[high] > 0:
                    high-=1
        return ans
# @lc code=end

