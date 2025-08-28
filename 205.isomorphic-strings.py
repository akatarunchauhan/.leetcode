#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sMap={}
        tMap = {}
        for a, b in zip(s,t):
            if (a in sMap and sMap[a] != b) or (b in tMap and tMap[b] != a):
                return False
            sMap[a] = b
            tMap[b] = a
        return True
# @lc code=end

