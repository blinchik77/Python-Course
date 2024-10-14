"""
https://leetcode.com/problem-list/array/
url: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii
"""


class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums) <= 2:
            return len(nums)

        i = 2
        for j in range(2, len(nums)):
            if nums[j] != nums[i - 2]:
                nums[i] = nums[j]
                i += 1

        return i
