#
# @lc app=leetcode id=843 lang=python3
#
# [843] Guess the Word
#

# @lc code=start
# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        candidate = words[:]
        while True:
            w = random.choice(candidate)
            match = master.guess(w)
            if match == 6:
                return
            else:
                candidate = [x for x in candidate if sum(a==b for a, b in zip(x,w)) == match]
        
# @lc code=end

