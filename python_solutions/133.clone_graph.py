from typing import List, Optional
import unittest

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old_to_new = {}

        def dfs(node):
            if not node:
                return 
            
            if node in old_to_new:
                return old_to_new[node]

            newNode = Node(node.val)
            old_to_new[node] = newNode

            for neighbor in node.neighbors:
                newNode.neighbors.append(dfs(neighbor))
            
            return newNode
        
        return dfs(node)