#
# @lc app=leetcode id=190 lang=python3
#
# [190] Reverse Bits
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        binary = ''
        for _ in range(32):
            binary = str(n % 2) + binary
            n //= 2
        number = binary[::-1]
        return int(number, 2)
# @lc code=end

