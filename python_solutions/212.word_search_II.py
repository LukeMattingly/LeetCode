from typing import List
import unittest

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

    def insertWord(self, word):
        node = self
        for letter in word:
            if letter not in node.children:
                node.children[letter] = TrieNode()
            node = node.children[letter]
        node.endOfWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for word in words:
            root.insertWord(word)

        ROWS = len(board)
        COLUMNS = len(board[0])
        visited = set()
        result = set()

        def dfs(r, c, node, word):
            #base case handle all diretions
            if(r<0 or c<0 or r>=ROWS or c>= COLUMNS or (r,c) in visited or board[r][c] not in node.children):
                return
            
            visited.add((r,c))

            node = node.children[board[r][c]]
            word += board[r][c]

            if node.endOfWord:
                result.add(word)
            
            dfs(r+1, c, node, word)
            dfs(r-1, c, node, word)
            dfs(r, c+1, node, word)
            dfs(r, c-1, node, word)

            visited.remove((r,c))

        for r in range(ROWS):
            for c in range(COLUMNS):
                dfs(r,c,root, "")
        
        return list(result)
        




if __name__ == '__main__':
    unittest.main()