from typing import List
import unittest

class WordNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = WordNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for letter in word:
            if letter not in node.children:
                node.children[letter] = WordNode()
            node = node.children[letter]
        node.isWord = True


    def search(self, word: str) -> bool:
        def dfs(j, root):
            node = root
            for i in range(j, len(word)):
                letter = word[i]
                if letter == '.':
                    for child in node.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                    
                else: 
                    if letter not in node.children:
                        return False
                    node =node.children[letter]

            return node.isWord
        
        return dfs(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)


if __name__ == '__main__':
    unittest.main()