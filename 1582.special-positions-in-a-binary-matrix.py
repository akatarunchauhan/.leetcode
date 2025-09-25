#
# @lc app=leetcode id=1582 lang=python3
#
# [1582] Special Positions in a Binary Matrix
#

# @lc code=start
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        
        rowSum = [sum(row) for row in mat]
        colSum = [sum(mat[i][j] for i in range(m)) for j in range(n)]
        
        count = 0
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1 and rowSum[i]==1 and colSum[j]==1:
                    count+=1
        return count
# @lc code=end

