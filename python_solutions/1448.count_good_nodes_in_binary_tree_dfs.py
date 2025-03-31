from typing import List, Optional, Deque
import unittest

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution():
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        def dfs(node, currMax):
            if not node:
                return
            if node.val >= currMax:
                self.goodNodeCount +=1
                currMax = node.val
            dfs(node.left, currMax)
            dfs(node.right, currMax)

        self.goodNodeCount =0
        dfs(root, root.val)
        return self.goodNodeCount



if __name__ == '__main__':
    unittest.main()