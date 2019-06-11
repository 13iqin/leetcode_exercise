# Definition for a binary tree node.
import sys


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        MAX = sys.maxint
        MIN = -sys.maxint - 1

        def isValidBSTUtil(root, min, max):
            if root is None:
                return True

            if root.left is None and root.right is None:
                return min < root.val < max

            if root.val <= min or root.val >= max:
                return False

            return isValidBSTUtil(root.left, min, root.val) and isValidBSTUtil(root.right, root.val, max)

        return isValidBSTUtil(root, MIN, MAX)
