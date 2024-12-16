"""
https://leetcode.com/problem-list/binary-tree/
url: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
"""


class Solution(object):
    def findMin(self, nums):
        nums.sort()
        return nums[0]
