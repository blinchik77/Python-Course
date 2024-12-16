"""
https://leetcode.com/problem-list/binary-tree/
url: https://leetcode.com/problems/single-number-ii
"""


class Solution(object):
    def singleNumber(self, nums):
        ones = 0
        twos = 0

        for num in nums:
            ones = (ones ^ num) & ~twos
            twos = (twos ^ num) & ~ones

        return ones
