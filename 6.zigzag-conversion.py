#
# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows>len(s):
            return s
        rows = [""] * len(s)
        curRow = 0
        goingDown = False
        
        for char in s:
            rows[curRow] += char
            if curRow == 0 or curRow == numRows - 1:
                goingDown = not goingDown
            if(goingDown):
                curRow += 1
            else: 
                curRow -= 1
        return "".join(rows)
        
# @lc code=end

