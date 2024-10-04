"""
https://leetcode.com/problem-list/array/
url: https://leetcode.com/problems/maximum-product-subarray
"""


class Solution(object):
    def maxProduct(self, nums):
        if not nums:
            return 0

        maxx = minn = result = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            if num < 0:
                maxx, minn = minn, maxx

            maxx = max(num, maxx * num)
            minn = min(num, minn * num)
            result = max(result, maxx)

        return result
