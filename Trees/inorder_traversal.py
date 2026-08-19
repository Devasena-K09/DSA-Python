class TreeNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def inorder(root):

    if root:

        inorder(root.left)
        print(root.value, end=" ")
        inorder(root.right)
