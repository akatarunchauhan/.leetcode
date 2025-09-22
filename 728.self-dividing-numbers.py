#
# @lc app=leetcode id=728 lang=python3
#
# [728] Self Dividing Numbers
#

# @lc code=start
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for num in range(left, right+1):
            valid = True
            for digit in str(num):
                if digit=='0' or int(num)%int(digit) != 0:
                    valid=False
                    break
            if valid:
                res.append(num)
        return res
# @lc code=end

