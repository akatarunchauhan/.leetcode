#
# @lc app=leetcode id=542 lang=python3
#
# [542] 01 Matrix
#

# @lc code=start
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        dist = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                else:
                    dist[i][j] = float('inf')
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] != 0:
                    if i > 0 :
                        dist[i][j] = min(
                            dist[i][j],
                            dist[i-1][j]+1
                        )
                    if j > 0:
                        dist[i][j] = min(
                            dist[i][j],
                            dist[i][j-1]+1
                        )
                    
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if mat[i][j] != 0:
                    if i < m-1:
                        dist[i][j] = min(
                            dist[i][j],
                            dist[i+1][j]+1
                        )
                    if j < n-1:
                        dist[i][j] = min(
                            dist[i][j],
                            dist[i][j+1]+1
                        )
                    
        return dist
# @lc code=end

