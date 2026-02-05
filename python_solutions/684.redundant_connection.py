import unittest
from typing import List
import heapq 
from collections import Counter, defaultdict, deque

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        adjList = [[]for _ in range(len(edges)+1)]

        def dfs(node, parent):
            if node in visited:
                return True
            
            visited.add(node)

            for neighbor in adjList[node]:
                if neighbor == parent:
                    continue
                if dfs(neighbor, node):
                    return True
                
        
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
            visited = set()

            if dfs(u, -1):
                return [u,v]
        
        return []
