from typing import List, Optional
import unittest
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution():
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        queue.append(root)
        result = []

        while queue:
            rightSide = None
            queueLen = len(queue)

            for i in range(queueLen):

                node = queue.popleft()
                if node:
                    rightSide = node
                    queue.append(node.left)
                    queue.append(node.right)
            if rightSide:
                result.append(rightSide.val)

        return result

if __name__ == '__main__':
    unittest.main()