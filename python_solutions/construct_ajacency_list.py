from typing import List
import unittest
from collections import defaultdict

class Solution:
    def constructAjacencyList(self, edges: List[List[int]]) -> List[int]:
        adjacencyMap = defaultdict(list)
        for vertex, neighbor in edges:
            adjacencyMap[vertex].append(neighbor)
            adjacencyMap[neighbor].append(vertex)
        return adjacencyMap
