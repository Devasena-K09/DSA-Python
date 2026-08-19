class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def lca(root, p, q):
    if p < root.val and q < root.val:
        return lca(root.left, p, q)

    if p > root.val and q > root.val:
        return lca(root.right, p, q)

    return root


root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)

ancestor = lca(root, 2, 8)

print(ancestor.val)
