#
# @lc app=leetcode id=659 lang=python3
#
# [659] Split Array into Consecutive Subsequences
#

# @lc code=start
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        avail = Counter(nums)
        vacancy = defaultdict(int)
        
        for num in nums:
            if avail[num] == 0:
                continue
            if vacancy[num]:
                vacancy[num] -= 1
                vacancy[num+1] += 1
            elif avail[num+1]>0 and avail[num+2]>0:
                avail[num+1] -=1
                avail[num+2] -=1
                vacancy[num+3] +=1
            else:
                return False
            avail[num] -= 1
        return True
# @lc code=end

