#
# @lc app=leetcode id=1351 lang=python3
#
# [1351] Count Negative Numbers in a Sorted Matrix
#

# @lc code=start
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        res = 0
        for i in range(len(grid)):
            l = 0
            r = len(grid[i])-1
            while l<=r:
                mid = (l + r)//2
                if grid[i][mid]>=0:
                    l = mid+1
                else:
                    r = mid-1
            res += len(grid[i])-l
        return res
# @lc code=end

