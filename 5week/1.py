"""
https://leetcode.com/problem-list/hash-table
url: https://leetcode.com/problems/majority-element-ii
"""


class Solution(object):
    def majorityElement(self, nums):
        n = len(nums)
        if n == 0:
            return []
        counts = {}
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        result = []
        threshold = n // 3
        for num, count in counts.items():
            if count > threshold:
                result.append(num)

        return result
