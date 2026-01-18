from typing import List
import unittest
from collections import defaultdict

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac = set()
        atl = set()
        ROWS = len(heights)
        COLUMNS = len(heights[0])

        def dfs(r,c,visited,parent):
            if r<0 or c<0 or r>=ROWS or c>=COLUMNS:
                return
            
            if (r,c) in visited or heights[r][c] < parent:
                return
            
            visited.add((r,c))
            
            dfs(r+1,c,visited,heights[r][c])
            dfs(r-1,c,visited,heights[r][c])
            dfs(r,c+1,visited,heights[r][c])
            dfs(r,c-1,visited,heights[r][c])

        
        #first row, last row
        for c in range(COLUMNS):
            dfs(0,c,pac, heights[0][c])
            dfs(ROWS-1,c,atl,heights[ROWS-1][c])

        for r in range(ROWS):
            dfs(r,0,pac,heights[r][0])
            dfs(r,COLUMNS-1, atl, heights[r][COLUMNS-1])

        
        return list(atl&pac)