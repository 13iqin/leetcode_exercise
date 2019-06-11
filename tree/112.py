# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root: return False
        if not root.left and not root.right and sum == root.val:
            return True
        left, right = False, False
        if root.left:
            left = self.hasPathSum(root.left, sum - root.val)
        if root.right:
            right = self.hasPathSum(root.right, sum - root.val)
        return True if left or right else False
