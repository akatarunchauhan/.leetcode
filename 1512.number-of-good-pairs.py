#
# @lc app=leetcode id=1512 lang=python3
#
# [1512] Number of Good Pairs
#

# @lc code=start
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        good_pair = 0
        count = {}
        for n in nums:
            if n in count:
                good_pair += count[n]
                count[n] += 1
            else:
                count[n] = 1
        return good_pair
# @lc code=end

