class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def search(root, target):
    if root is None or root.val == target:
        return root

    if target < root.val:
        return search(root.left, target)

    return search(root.right, target)


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)

result = search(root, 7)

if result:
    print("Found:", result.val)
