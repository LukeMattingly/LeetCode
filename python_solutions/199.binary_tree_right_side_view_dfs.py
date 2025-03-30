from typing import List, Optional, Deque
import unittest

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution():
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def dfs(node, depth):
            if not node:
                return []
            #at the current depth we're only adding one result each time, need to keept rack of left too incase right runs out
            if depth == len(result):
                result.append(node.val)
                
            dfs(node.right, depth +1)
            dfs(node.left, depth +1)
        
        dfs(root,0)
        return result



if __name__ == '__main__':
    unittest.main()