from typing import List, Optional
import unittest
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution():
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, largestLeft, smallestRight):
            if not node:
                return True
            
            if not (largestLeft < node.val < smallestRight):
                return False
            
            return dfs(node.left, largestLeft, node.val) and dfs(smallestRight, node.val, smallestRight)

        
        dfs(root, float("-inf"), float("inf"))
        return True

if __name__ == '__main__':
    unittest.main()