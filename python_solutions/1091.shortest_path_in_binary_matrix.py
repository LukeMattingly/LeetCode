from typing import List
import unittest
from collections import deque

class Solution():
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] ==1 or grid[n-1][n-1]==1:
            return -1
        
        queue = deque()
        queue.append((0,0))
        length =1

        directions = [
            (-1, -1), (0, -1), (1, -1),
            (-1, 0),           (1, 0),
            (-1, 1), (0, 1), (1, 1)
        ]

        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                if x == n-1 and y == n-1:
                    return length
                
                for dx, dy in directions:
                    nx, ny = x + dx, y+dy
                    if 0<=nx<n and 0<= ny <n and grid[nx][ny]==0:
                        grid[nx][ny]=1
                        queue.append((nx,ny))
            length+=1
        return -1
        