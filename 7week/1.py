"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/find-all-anagrams-in-a-string
"""

from collections import Counter


class Solution(object):
    def findAnagrams(self, s, p):
        result = []
        p_count = Counter(p)
        window_count = Counter()

        p_len = len(p)

        for i in range(len(s)):
            window_count[s[i]] += 1

            if i >= p_len:
                if window_count[s[i - p_len]] == 1:
                    del window_count[s[i - p_len]]
                else:
                    window_count[s[i - p_len]] -= 1

            if window_count == p_count:
                result.append(i - p_len + 1)

        return result
