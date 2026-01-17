from typing import List
import unittest

class Solution:
    def solve(self, grid: List[List[str]]) -> None:
        ROWS = len(grid)
        COLUMNS = len(grid)

        def dfs(r,c):
            if r<0 or c<0 or r>=ROWS or c>=COLUMNS or grid[r][c] !="O":
                return
            
            grid[r][c] = "S"

            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        for c in range(COLUMNS):
            if grid[0][c] == "O":
                dfs(0,c)
            if grid[ROWS-1][c] == "O":
                dfs(ROWS-1,c)

        for r in range(ROWS):
            if grid[r][0] == "O":
                dfs(r,0)
            if grid[r][COLUMNS-1] == "O":
                dfs(r, COLUMNS-1)

        
        for r in range(ROWS):
            for c in range(COLUMNS):
                if grid[r][c] == "O":
                    grid[r][c] = "X"
                if grid[r][c] == "S":
                    grid[r][c] = "O"