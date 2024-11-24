"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters
"""


class Solution(object):
    def longestSubstring(self, s, k):
        def helper(s, k):
            if not s:
                return 0

            char_count = {}
            for char in s:
                char_count[char] = char_count.get(char, 0) + 1

            for char in char_count:
                if char_count[char] < k:
                    return max(helper(sub, k) for sub in s.split(char))

            return len(s)

        return helper(s, k)
