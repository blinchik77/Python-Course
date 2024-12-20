"""
https://leetcode.com/problem-list/array/
url: https://leetcode.com/problems/jump-game
"""


class Solution(object):
    def canJump(self, nums):
        farthest = 0
        for i in range(len(nums)):
            if i > farthest:
                return False
            farthest = max(farthest, i + nums[i])
        return True
