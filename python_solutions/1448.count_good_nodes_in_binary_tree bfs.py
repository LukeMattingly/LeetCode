from typing import List, Optional
import unittest
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution():
    def goodNodes(self, root: TreeNode) -> int: 
        total_len =0

        queue = deque()
        queue.append(root, -float("inf"))

        while queue:
            node, maxVal = queue.popleft()

            if node.val >= maxVal:
                total_len +=1
            
            #do somethign wtih node

            if node.left:
                queue.append(node.left, max(node.val, maxVal))
            if node.right:
                queue.append(node.right, max(node.val, maxVal))
                
        
        return total_len



if __name__ == '__main__':
    unittest.main()