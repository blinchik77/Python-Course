"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/longest-palindromic-substring
"""


class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        current_row = 0
        going_down = False

        for char in s:
            rows[current_row] += char
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            current_row += 1 if going_down else -1
        return "".join(rows)
