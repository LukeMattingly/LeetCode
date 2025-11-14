from typing import Optional, Deque
import unittest

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution():
    def sumOfAllNodes(self, root:Optional[TreeNode])->int:
        if not root:
            return 0
        
        left = self.sumOfAllNodes(root.left)
        right = self.sumOfAllNodes(root.right)

        return root.val + left + right