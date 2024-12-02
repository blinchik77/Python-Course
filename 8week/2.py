"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/longest-turbulent-subarray
"""


class Solution(object):
    def maxTurbulenceSize(self, arr):
        n = len(arr)
        if n < 2:
            return n

        inc, dec = 1, 1
        max_length = 1

        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                inc = dec + 1
                dec = 1
            elif arr[i] < arr[i - 1]:
                dec = inc + 1
                inc = 1
            else:
                inc = dec = 1

            max_length = max(max_length, inc, dec)

        return max_length
