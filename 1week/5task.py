"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/reverse-words-in-a-string
"""


class Solution(object):
    def reverseWords(self, s):

        res = ""
        current_word = ""

        for i in range(len(s) - 1, -1, -1):
            if s[i] != " ":
                current_word += s[i]
            else:
                if current_word:
                    current_word = current_word[::-1] + " "
                    res += current_word
                    current_word = ""

        res += current_word[::-1]
        if res[-1] == " ":
            res = res[:-1]
        return res


solution = Solution()
