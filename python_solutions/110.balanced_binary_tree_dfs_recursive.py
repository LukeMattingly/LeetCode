from typing import Optional, Deque
import unittest

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution():
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True
        
        def dfs(root):         
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)

            if (abs(left - right) > 1):
                self.balanced= False

            return max(left, right) + 1
        
        dfs(root)       
        return self.balanced



if __name__ == '__main__':
    unittest.main()