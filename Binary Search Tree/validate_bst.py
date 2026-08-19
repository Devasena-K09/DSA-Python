class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def is_valid(root, low=float('-inf'), high=float('inf')):
    if root is None:
        return True

    if root.val <= low or root.val >= high:
        return False

    return (
        is_valid(root.left, low, root.val)
        and
        is_valid(root.right, root.val, high)
    )


root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

print(is_valid(root))
