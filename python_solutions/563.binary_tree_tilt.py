from typing import Optional, Deque
import unittest

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution():
    def findTilt(self, root: Optional[TreeNode]) -> int:

        result =0
        def dfs(node):
            nonlocal result
            if not node:
                return 0
            
            leftSum = dfs(node.left)
            rightSum = dfs(node.right)
            result += abs(leftSum-rightSum)

            return leftSum + node.val + rightSum
        
        dfs(root)
        return result
            


if __name__ == '__main__':
    unittest.main()