from typing import Optional
import unittest

class Node:
    def __init__(self):
         self.children = {}
         self.isComplete = False

class Trie:

    def __init__(self):
        self.root = Node()
        

    def insert(self, word: str) -> None:
        node = self.root
        for letter in word:
            if letter not in node.children:
                node.children[letter] = Node()
            node = node.children[letter] #update current node to the child of the one we just inserted
        
        node.isComplete= True #done with word, mark the last node as completed


    def search(self, word: str) -> bool:
        node = self.root
        for letter in word:
            if letter not in node.children:
                return False
            node = node.children[letter]
        return node.isComplete 
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for letter in prefix:
            if letter not in node.children:
                return False
            node = node.children[letter]
        return True



if __name__ == '__main__':
    unittest.main()
