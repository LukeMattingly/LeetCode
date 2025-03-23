from typing import Optional, Deque
import unittest

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution():
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        max_length = 0
        stack = [[root, 1]]
        while stack:
            node, depth = stack.pop()
            if node:
                max_length = max(max_length, depth)
                stack.append([node.left, 1+ depth])
                stack.append([node.right, 1+ depth])
        
        return max_length




if __name__ == '__main__':
    unittest.main()