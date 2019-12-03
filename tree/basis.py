class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# 前序遍历
def preorder(root):
    if root:
        print(root.val)
        preorder(root.left)
        preorder(root.right)


# 中序遍历
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)


# 后序遍历
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val)


if __name__ == '__main__':
    a = TreeNode('a')
    b = TreeNode('b')
    c = TreeNode('c')
    d = TreeNode('d')
    e = TreeNode('e')
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    # inorder(a)
    # preorder(a)
    postorder(a)
