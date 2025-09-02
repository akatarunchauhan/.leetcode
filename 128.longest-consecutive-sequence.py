#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0
        for num in numSet:
            if (num-1) not in numSet:
                length = 0
                while (num+length) in numSet:
                    length+=1
                res = max(length,res)
        return res
# @lc code=end

