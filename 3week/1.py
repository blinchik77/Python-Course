"""
https://leetcode.com/problem-list/array/
url: https://leetcode.com/problems/permutations
"""

from itertools import permutations


class Solution(object):
    def permute(self, nums):
        return list(permutations(nums))
