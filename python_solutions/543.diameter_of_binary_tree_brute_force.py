from typing import Optional, Deque
import unittest

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution():
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        leftHeight = self.maxHeight(root.left)
        rightHeight = self.maxHeight(root.right)
        max_diameter = leftHeight + rightHeight
        
        sub = max(self.diameterOfBinaryTree(root.left),self.diameterOfBinaryTree(root.right))

        return max(max_diameter, sub)

    def maxHeight(self, root:Optional[TreeNode]):
        if not root:
            return 0
        
        return 1+ max(self.maxHeight(root.left), self.maxHeight(root.right))

if __name__ == '__main__':
    unittest.main()