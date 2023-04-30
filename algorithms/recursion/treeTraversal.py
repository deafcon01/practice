class Node:
    def __init__(self, key):
        self.left = None
        self.right =None
        self.key = key

def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)

def preorder(root):
    if root:
        print(root.key, end = " ")
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.key, end = " ")
if __name__ ==  "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("\nInorder traversal:\n")
    inorder(root)
    print("\nPreorder traversal:\n")
    preorder(root)
    print("\nPostorder traversal:\n")
    postorder(root)