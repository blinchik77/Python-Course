"""
https://leetcode.com/problem-list/hash-table
url: https://leetcode.com/problems/set-matrix-zeroes
"""


class Solution(object):
    def setZeroes(self, matrix):
        if not matrix:
            return
        m, n = len(matrix), len(matrix[0])
        rows = set()
        cols = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        for row in rows:
            for j in range(n):
                matrix[row][j] = 0
        for col in cols:
            for i in range(m):
                matrix[i][col] = 0
