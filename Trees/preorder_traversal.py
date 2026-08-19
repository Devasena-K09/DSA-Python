def preorder(root):

    if root:

        print(root.value, end=" ")
        preorder(root.left)
        preorder(root.right)
