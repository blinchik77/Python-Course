"""
https://leetcode.com/problem-list/binary-tree/
url: https://leetcode.com/problems/sum-root-to-leaf-numbers
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sumNumbers(self, root):
        def dps(root, sum):
            if root == None:
                return 0
            sum = sum * 10 + root.val
            if root.left == None and root.right == None:
                return sum
            return dps(root.left, sum) + dps(root.right, sum)

        return dps(root, 0)
