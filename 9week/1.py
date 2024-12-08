"""
https://leetcode.com/problem-list/binary-tree/
url: https://leetcode.com/problems/unique-binary-search-trees
"""

import math


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def numTrees(self, n):
        return math.factorial(2 * n) / (math.factorial(n) * math.factorial(n + 1))
