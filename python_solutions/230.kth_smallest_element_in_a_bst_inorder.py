from typing import List, Optional, Deque
import unittest

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution():
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.result = []
        def inOrderTrav(node):            
            if node.left:
                inOrderTrav(node.left)
            
            self.result.append(node.val)

            if node.right:
                inOrderTrav(node.right)
        
        inOrderTrav(root)
        return self.result[k-1]



if __name__ == '__main__':
    unittest.main()