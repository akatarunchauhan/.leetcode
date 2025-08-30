#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        l = 0
        for r in range(len(nums)):
            if r-l>k:
                window.remove(l)
                l +=1
            if nums[r] in window:
                return True
            window.add(nums[r])
        return False
# @lc code=end

