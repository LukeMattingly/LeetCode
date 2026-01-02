from typing import List
import unittest

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.'] * n for _ in range(n)]
        boards = []
        cols = set()
        negDiag = set() #r-c
        posDiag = set() #r+c

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                boards.append(copy)
                return
            
            for c in range(n):
                if c in cols or (r-c) in negDiag or (r+c) in posDiag:
                    continue

                cols.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                board[r][c] = 'Q'

                backtrack(r+1)

                cols.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                board[r][c] = '.'

        backtrack(0)
        return boards