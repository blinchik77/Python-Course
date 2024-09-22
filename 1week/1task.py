"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/longest-substring-without-repeating-characters
"""


class Solution(object):
    def lengthOfLongestSubstring(self,s):

        left_pointer = 0
        current_res = []
        best_res = 0

        for right_pointer in range(len(s)):
            while s[right_pointer] in current_res:
                left_pointer+=1
                current_res.pop(0)

            current_res.append(s[right_pointer])
            best_res = max(best_res, right_pointer - left_pointer + 1)
        return best_res

solution = Solution()