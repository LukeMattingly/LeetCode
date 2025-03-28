from typing import List, Optional
import unittest
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution():
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        queue.append(root)
        res = []

        while queue:
            qlen = len(queue)
            level = []
            for _ in range(qlen):
                node = queue.popleft()
                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if level:
                res.append(level)
        return res

if __name__ == '__main__':
    unittest.main()