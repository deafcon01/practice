"""
Given the root of a binary tree, invert the tree, and return its root.

input: [4,2,7,1,3,6,9]
output: [4,7,2,9,6,3,1]
"""
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root==None:
            return root
        queue=[root]
        while len(queue):
            cur = queue.pop(0)
            cur.left, cur.right= cur.right, cur.left
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        return root