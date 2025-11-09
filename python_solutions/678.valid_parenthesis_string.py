import unittest
from typing import List
import heapq 
from collections import Counter, defaultdict, deque

class Solution:
    def checkValidString(self, s: str) -> bool:
        open_stack = []
        star_stack = []

        for i, paren in enumerate(s):
            if paren == ')':
                if open_stack:
                    open_stack.pop()
                elif star_stack:
                    star_stack.pop()
                else:
                    return False
            elif paren == "*":
                star_stack.append(i)
            else:
                open_stack.append(i)

        while open_stack and star_stack:
            if open_stack[-1] < star_stack[-1]:
                open_stack.pop()
                star_stack.pop()
            else:
                return False

        if open_stack:
            return False
        else:
            return True