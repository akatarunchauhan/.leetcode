#
# @lc app=leetcode id=493 lang=python3
#
# [493] Reverse Pairs
#

# @lc code=start
from typing import List

class Solution:
    def merge_sort(self, nums, low, high):
        if low >= high:
            return 0
        
        mid = (low + high) // 2

        count = self.merge_sort(nums, low, mid) + self.merge_sort(nums, mid + 1, high)

        j = mid + 1
        for i in range(low, mid + 1):
            while j <= high and nums[i] > 2 * nums[j]:
                j += 1
            count += (j - (mid + 1))

        self.merge(nums, low, mid, high)
        return count

    def merge(self, nums, low, mid, high):
        temp = []
        i, j = low, mid + 1

        while i <= mid and j <= high:
            if nums[i] <= nums[j]:
                temp.append(nums[i])
                i += 1
            else:
                temp.append(nums[j])
                j += 1

        while i <= mid:
            temp.append(nums[i])
            i += 1
        while j <= high:
            temp.append(nums[j])
            j += 1

        for i in range(len(temp)):
            nums[low + i] = temp[i]

    def reversePairs(self, nums: List[int]) -> int:
        return self.merge_sort(nums, 0, len(nums) - 1)

# @lc code=end

