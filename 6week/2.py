"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/count-number-of-nice-subarrays
"""


class Solution(object):
    def numberOfSubarrays(self, nums, k):
        odd_count = 0
        prefix_counts = {0: 1}
        result = 0
        for num in nums:
            if num % 2 == 1:
                odd_count += 1
            if odd_count - k in prefix_counts:
                result += prefix_counts[odd_count - k]
            if odd_count in prefix_counts:
                prefix_counts[odd_count] += 1
            else:
                prefix_counts[odd_count] = 1

        return result
