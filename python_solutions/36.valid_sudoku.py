from typing import List
import unittest
from collections import defaultdict

class Solution():
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                else:
                    if board[r][c] in rows[r] or board[r][c] in columns[c] or board[r][c] in squares[(r//3, c//3)]:
                        return False
                    
                    columns[c].add(board[r][c])
                    rows[r].add(board[r][c])
                    squares[(r//3, c//3)].add(board[r][c])

        return True 
    
class test_isValidSudoku(unittest.TestCase):
    def test_isValidSudoku_1(self):
        solution = Solution()
        ans = True
        s= [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
        self.assertEqual(ans, solution.isValidSudoku(s))

    def test_canConstruct_2(self):
        solution = Solution()
        ans = False
        board = [["8","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
        self.assertEqual(ans, solution.isValidSudoku(board))

if __name__ == '__main__':
    unittest.main()
