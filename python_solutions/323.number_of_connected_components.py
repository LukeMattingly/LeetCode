from typing import List, Optional, Deque
import unittest

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        adjList = [[] for _ in range(n)]

        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)


        def dfs(node):
            for neighbor in adjList[node]:
                if neighbor not in visited:
                    visited.add(node)
                    dfs(neighbor)
        

        result = 0
        for node in range(n):
            if node not in visited:
                visited.add(node)
                dfs(node)
                result +=1
        
        return result 

