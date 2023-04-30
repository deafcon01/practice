class Node:
    def __init__(self, value) -> None:
        self.left = None
        self.right = None
        self.value = value

class BinaryTree:
    def spiral(self, root):
        if not root:
            return
        stack1 = []
        stack2 = []
        stack1.append(root)
        while stack1 or stack2:
            while stack1:
                item = stack1.pop()
                print(item.value, end=" ")
                if item.left:
                    stack2.append(item.left)
                if item.right:
                    stack2.append(item.right)
            while stack2:
                item = stack2.pop()
                print(item.value, end=" ")
                if item.right:
                    stack1.append(item.right)
                if item.left:
                    stack1.append(item.left)

if __name__ ==  "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    obj = BinaryTree()
    obj.spiral(root)