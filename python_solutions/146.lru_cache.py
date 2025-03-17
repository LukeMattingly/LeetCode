from typing import Optional
import unittest
from collections import defaultdict

class Node:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        #left = LRU, right = most recent
        self.left = Node (0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    #remove from linked list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    #insert at right
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev


    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            #remove from ll and delete lru from the cache from the hashmap
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]



if __name__ == '__main__':
    unittest.main()