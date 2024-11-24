"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/longest-repeating-character-replacement
"""

from collections import Counter


class Solution:
    def characterReplacement(self, s, k):
        max_length = 0
        max_freq = 0
        count = Counter()
        left = 0
        for right in range(len(s)):
            count[s[right]] += 1
            max_freq = max(max_freq, count[s[right]])

            if (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length
