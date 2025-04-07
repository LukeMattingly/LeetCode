from typing import List, Optional
import unittest
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution():
  def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.result = root.val

        #return the max path sum without splitting
        def dfs(root):
            if not root:
                return 0
            
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            #compute max path sum WITH split
            self.result = max(self.result, root.val + leftMax + rightMax)

            return root.val + max(leftMax, rightMax)
        
        dfs(root)
        return self.result


if __name__ == '__main__':
    unittest.main()