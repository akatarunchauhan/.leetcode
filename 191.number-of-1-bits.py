#
# @lc app=leetcode id=191 lang=python3
#
# [191] Number of 1 Bits
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = ''
        while n > 0:
            binary = str(n%2) + binary
            n = n//2
        return list(binary).count('1')
# @lc code=end

