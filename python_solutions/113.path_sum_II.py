from typing import Optional, Deque, List
import unittest

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution():
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]: 
        result = []

        def dfs(node, path, remainingTarget):
            if not node:
                return
            
            path.append(node.val)
            remainingTarget -= node.val

            if not node.left and not node.right and remainingTarget==0:
                result.append(path[:])
            
            dfs(node.left, path, remainingTarget)
            dfs(node.right, path, remainingTarget)

            path.pop()

        dfs(root, [], targetSum)
        return result



if __name__ == '__main__':
    unittest.main()