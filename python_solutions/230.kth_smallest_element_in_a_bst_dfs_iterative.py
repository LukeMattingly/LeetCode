from typing import List, Optional, Deque
import unittest

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution():
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []

        curr = root

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
        k-=1
        if k ==0:
            return curr.val
        curr = curr.right



if __name__ == '__main__':
    unittest.main()