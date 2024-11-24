"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/find-k-closest-elements
"""

from bisect import bisect_left


class Solution(object):
    def findClosestElements(self, arr, k, x):
        pos = bisect_left(arr, x)

        left, right = pos - 1, pos

        while k > 0:
            if left < 0:
                right += 1
            elif right >= len(arr):
                left -= 1
            elif abs(arr[left] - x) <= abs(arr[right] - x):
                left -= 1
            else:
                right += 1
            k -= 1
        return sorted(arr[left + 1 : right])
