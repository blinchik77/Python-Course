"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold
"""


class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        target_sum = k * threshold
        current_sum = sum(arr[:k])
        count = 1 if current_sum >= target_sum else 0

        for i in range(k, len(arr)):
            current_sum += arr[i] - arr[i - k]
            if current_sum >= target_sum:
                count += 1

        return count
