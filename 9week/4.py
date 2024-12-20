"""
https://leetcode.com/problem-list/binary-tree/
url: https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def buildTree(self, inorder, postorder):
        if not inorder:
            return None
        root_val = postorder.pop()
        root = TreeNode(root_val)
        inorder_index = inorder.index(root_val)
        root.right = self.buildTree(inorder[inorder_index + 1 :], postorder)
        root.left = self.buildTree(inorder[:inorder_index], postorder)
        return root
