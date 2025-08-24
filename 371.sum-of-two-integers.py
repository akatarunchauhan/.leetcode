#
# @lc app=leetcode id=371 lang=python3
#
# [371] Sum of Two Integers
#

# @lc code=start
class Solution:
    def getSum(self, a: int, b: int) -> int:
        xor = a^b
        shift = a&b<<1
        res = xor ^ shift
        while (a^b) & (a & b << 1) != 0:
            res = xor ^ shift
        return res
# @lc code=end

