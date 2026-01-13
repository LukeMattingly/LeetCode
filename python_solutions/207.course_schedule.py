from typing import List
from collections import defaultdict
import unittest


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        adjList = defaultdict(list)

        for course, prerequisite in prerequisites:
            adjList[course].append(prerequisite)
        
        def dfs(course):
            if course in visited:
                return False
            
            visited.add(course)
            for newCourse in adjList[course]:
                if not dfs(newCourse):
                    return False
            visited.remove(course)
            adjList[course] = []
            return True
        
        for c in numCourses:
            if not dfs(c):
                return False
        return True