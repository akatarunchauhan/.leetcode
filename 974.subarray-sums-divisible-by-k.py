#
# @lc app=leetcode id=974 lang=python3
#
# [974] Subarray Sums Divisible by K
#

# @lc code=start
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        currSum = 0
        res = 0
        prefixCount = defaultdict(int)
        prefixCount[0] = 1
        for n in nums:
            currSum += n
            remainder = currSum % k 
            res += prefixCount[remainder]
            prefixCount[remainder] += 1
        return res
# @lc code=end

