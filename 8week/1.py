"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/binary-subarrays-with-sum
"""


class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        prefix_count = {0: 1}
        prefix_sum = 0
        count = 0

        for num in nums:
            prefix_sum += num
            count += prefix_count.get(prefix_sum - goal, 0)
            prefix_count[prefix_sum] = prefix_count.get(prefix_sum, 0) + 1

        return count
