#
# @lc app=leetcode id=1979 lang=python3
#
# [1979] Find Greatest Common Divisor of Array
#

# @lc code=start
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        a=max(nums)
        b=min(nums)
        while b:
            a, b = b, a%b
        return a
# @lc code=end

