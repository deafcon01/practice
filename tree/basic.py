"""
Binary Tree
- at most 2 children per node
- exactly 1 root
- exactly 1 path b/w root and any node
"""
class Node:
    def __init__(self, key) -> None:
        self.left = None
        self.right = None
        self.value = key

class BinaryTree:
    def DFS(self, root:Node):
        if root == None:
            return []
        stack = [root]
        while len(stack):
            current = stack.pop()
            print(current.value)
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)

    def BFS(self, root:None):
        if root == None:
            return []
        values = []
        queue = [root]
        while len(queue):
            current = queue.pop(0)
            values.append(current.value)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return values

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    obj = BinaryTree()
    obj.DFS(root)
    print(obj.BFS(root))