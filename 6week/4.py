"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/arithmetic-slices
"""


class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        if len(nums) < 3:
            return 0
        dp = [0] * len(nums)
        total_subs = 0
        for i in range(2, len(nums)):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                dp[i] = dp[i - 1] + 1
                total_subs += dp[i]
            else:
                dp[i] = 0
        return total_subs
