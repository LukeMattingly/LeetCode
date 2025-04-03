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
        if not root:
            return True
        queue = deque()
        queue.append([(root, float("inf"), float("-inf"))])

        while queue:
            node, largestLeft, smallestRight = queue.popleft()

            if not (node.val > smallestRight and node.val < largestLeft):
                return False
            
            if node.left:
                queue.append([node.left, largestLeft, node.val])
            
            if node.right:
                queue.append([node.right, node.val, smallestRight])

        return True

if __name__ == '__main__':
    unittest.main()