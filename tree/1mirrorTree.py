class Node:
    def __init__(self, value) -> None:
        self.left = None
        self.right = None
        self.value = value

class BinaryTree:
    def mirror(self, root):
        """
        swap left and right child in post order traversal
        """
        if root==None:
            return
        self.mirror(root.left)
        self.mirror(root.right)
        tmp = root.left
        root.left=root.right
        root.right=tmp

def inorder(root):
    if root:
        inorder(root.left)
        print(root.value, end=" ")
        inorder(root.right)


if __name__ ==  "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("\nInorder traversal:\n")
    inorder(root)
    obj = BinaryTree()
    obj.mirror(root)
    print("\nInorder traversal:\n")
    inorder(root)