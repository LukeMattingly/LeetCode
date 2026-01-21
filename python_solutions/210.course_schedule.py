from typing import List
from collections import defaultdict
import unittest


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)
        path = set()
        visited = set()
        result = []

        for course, pre in prerequisites:
            adjList[course].append(pre)

        def dfs(node):
            if node in path:
                return False
            if node in visited:
                return True
            
            path.add(node)

            for neighbor in adjList[node]:
                if dfs(neighbor) == False:
                    return False

            path.remove(node)
            visited.add(node)
            result.append(node)
            return True
        
        for c in range(numCourses):
            if dfs(c) == False:
                return []
            
        return result