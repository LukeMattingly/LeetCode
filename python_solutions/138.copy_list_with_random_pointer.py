from typing import Optional
import unittest
from collections import defaultdict

class Node:
    def __init__(self, x: int, next=None, random:'Node'=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution():
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = {None:None} #initialize for none to be equal to none

        current = head
        while current:
            copy = Node(current.val)
            oldToCopy[current] = copy
            current = current.next

        current = head
        while current:
            copy = oldToCopy[current]
            copy.next = oldToCopy[current.next]
            copy.random = oldToCopy[current.random]
            current = current.next

        return oldToCopy[head]


if __name__ == '__main__':
    unittest.main()