from typing import List, Optional, Deque
import unittest

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution():
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, currMax):
            if not node:
                return 0
            
            count = 0
            if node.val >= currMax:
                currMax = node.val
                count+=1
            
            left = dfs(node.left, currMax)
            right = dfs(node.right, currMax)
            return count+left+right
        
        return dfs(root, -float("inf"))