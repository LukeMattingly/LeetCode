from typing import List


class Solution():
    def exist(self, board: List[List[str]], word: str) -> bool: 

        def dfs(row, column, currentIndex, visited):
            if currentIndex == len(word):
                return True
            
            if row < 0 or column < 0 or row >=len(board) or column >= len(board[0]):
                return False
        
            if ((row,column) in visited):
                return False
            
            if board[row][column] == word[currentIndex]:
                currentIndex+=1
                visited.add((row,column))
            else:
                return False
            
            if (
                dfs(row+1, column, currentIndex, visited) or
                dfs(row-1, column, currentIndex, visited) or
                dfs(row, column+1, currentIndex, visited) or
                dfs(row, column-1, currentIndex, visited) 
            ):
                return True

            visited.remove((row,column))
            return False
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r,c,0,set()):
                    return True
        return False