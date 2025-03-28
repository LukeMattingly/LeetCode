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
        res = []
        if not root:
            return []
        
        def dfs(node, depth):
            if not node:
                return None
            
            #if len(res) ==depth:
            #    res.append([]) #if empty 

            res[depth].append(node.val)

            dfs(node.left, depth+1)
            dfs(node.right, depth+1)
             
        
        dfs(root, 0)
        return res
if __name__ == '__main__':
    unittest.main()