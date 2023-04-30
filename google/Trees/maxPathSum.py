"""
Binary Tree Maximum Path Sum

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
"""
from typing import Optional
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def max_gain(node):
            nonlocal max_sum # mentioning the variable outside this func
            if not node:
                return 0
            left_gain = max(max_gain(node.left),0)
            right_gain = max(max_gain(node.right),0)
            price_newpath = node.val+left_gain+right_gain

            max_sum = max(max_sum, price_newpath)
            return node.val +  max(left_gain, right_gain)
        max_sum = float('-inf')
        max_gain(root)
        return max_sum