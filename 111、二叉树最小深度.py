# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        if not root:
            return 0
        depth_left = self.minDepth(root.left)
        depth_right = self.minDepth(root.right)
        if not depth_left or not depth_right:
            return depth_left + depth_right + 1
        return min(depth_left, depth_right) + 1