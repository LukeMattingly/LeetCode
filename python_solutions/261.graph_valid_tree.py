from typing import List
import unittest


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        adjacencyList = [[] for _ in range(n)]
        for u, v in edges:
            adjacencyList[u].append(v)
            adjacencyList[v].append(u)
        
        def dfs(parent, node):
            if node in visited:
                return False
        
            visited.add(node)
            for neighbor in adjacencyList[node]:
                if neighbor == parent:
                    continue
                if not dfs(neighbor, node):
                    return False
            return True
            
        return dfs(-1, 0) and len(visited) == n