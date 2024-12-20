"""
https://leetcode.com/problem-list/hash-table
url: https://leetcode.com/problems/top-k-frequent-elements
"""

import heapq
from collections import Counter


class Solution(object):
    def topKFrequent(self, nums, k):

        count = Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)
