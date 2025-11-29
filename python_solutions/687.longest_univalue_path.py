from typing import Optional, Deque
import unittest

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution():
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        maxPathLength = 0 
        def dfs(node):
            nonlocal maxPathLength
            if not node:
                return 0
            
            leftPathLength = dfs(root.left)
            rightPathLength = dfs(root.right)

            newLeftPathLength = newRightPathLength = 0
            if node.left and node.left.val == node.val:
                newLeftPathLength = leftPathLength +1
            if node.right and node.right.val == node.val:
                newRightPathLength = rightPathLength +1
            
            maxPathLength = max(maxPathLength, newLeftPathLength + newRightPathLength)

            return max(newLeftPathLength, newRightPathLength)
        
        dfs(root)
        return maxPathLength