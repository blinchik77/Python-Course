"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/permutation-in-string
"""

from collections import Counter


class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False
        s1_count = Counter(s1)
        window_count = Counter()
        s1_len = len(s1)
        for i in range(len(s2)):
            window_count[s2[i]] += 1
            if i >= s1_len:
                if window_count[s2[i - s1_len]] == 1:
                    del window_count[s2[i - s1_len]]
                else:
                    window_count[s2[i - s1_len]] -= 1
            if window_count == s1_count:
                return True
        return False
