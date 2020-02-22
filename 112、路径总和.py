# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        if not root:
            return False
        if not root.left and not root.right:
            return sum == root.val
        left_flag = self.hasPathSum(root.left, sum-root.val)
        right_flag = self.hasPathSum(root.right, sum-root.val)
        return left_flag or right_flag