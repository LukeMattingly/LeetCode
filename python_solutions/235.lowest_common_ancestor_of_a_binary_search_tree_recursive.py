from typing import List, Optional, Deque
import unittest

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution():
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or not p or not q:
            return None
        
        if((max(p.val,q.val)) < root.val):
            return self.lowestCommonAncestor(root.left)
        elif((min(p.val, q.val)) > root.val):
            return self.lowestCommonAncestor(root.right)
        else:
            return root



if __name__ == '__main__':
    unittest.main()