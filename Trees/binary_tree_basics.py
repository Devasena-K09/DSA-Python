class TreeNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(3)

print(root.value)
print(root.left.value)
print(root.right.value)
