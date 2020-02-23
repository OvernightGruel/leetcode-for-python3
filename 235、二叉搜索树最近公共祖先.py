# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if q.val < root.val > p.val:
            root = self.lowestCommonAncestor(root.left, p, q)
        if q.val > root.val < p.val:
            root = self.lowestCommonAncestor(root.right, p, q)
        return root
