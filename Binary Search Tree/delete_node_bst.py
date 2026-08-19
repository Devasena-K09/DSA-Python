class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def find_min(node):
    while node.left:
        node = node.left
    return node


def delete(root, key):
    if not root:
        return root

    if key < root.val:
        root.left = delete(root.left, key)

    elif key > root.val:
        root.right = delete(root.right, key)

    else:
        if not root.left:
            return root.right

        if not root.right:
            return root.left

        temp = find_min(root.right)
        root.val = temp.val
        root.right = delete(root.right, temp.val)

    return root


root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)

delete(root, 3)

print(root.val)
