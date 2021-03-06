# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        depth_left = self.maxDepth(root.left)
        depth_right = self.maxDepth(root.right)
        return max(depth_left, depth_right) + 1