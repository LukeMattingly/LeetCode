from typing import List
from collections import defaultdict
import unittest

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        count = 0

        def dfs(r,c, visited):
            #bounds checking
            ROWS = len(grid)
            COLUMNS = len(grid[0])
            if r <0 or c < 0 or r >=ROWS or c>= COLUMNS or (r,c) in visited or grid[r][c]=="0":
                return

            visited.add((r,c))

            dfs(r+1,c,visited)
            dfs(r-1,c,visited)
            dfs(r,c+1,visited)
            dfs(r,c-1,visited)

        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r,c) not in visited and grid[r][c]=="1":
                    count+=1
                    dfs(r,c, visited)
        
        return count