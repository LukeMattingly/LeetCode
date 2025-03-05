import unittest
from typing import List
from collections import Counter
import math

class TimeMap:

    def __init__(self):
        self.store = {} #key = string, value = [list of [value, timestamp]]
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.store.get(key, [])

        #binary search
        l = 0
        r = len(values) -1
        while l <= r:
            mid_index = l + (r - l) //2
            if values[mid_index][1] == timestamp:
                return values[mid_index][0]
            if values[mid_index][1] > timestamp:
                r = mid_index - 1
            else:
                res = values[mid_index][0]
                l = mid_index +1

        return res
        


"""
class test_minEatingSpeed(unittest.TestCase):
    def test_minEatingSpeed_1(self):
        solution = Solution()
        ans = 4
        self.assertEqual(solution.minEatingSpeed([3,6,7,11],8), ans)

    def test_minEatingSpeed_2(self):
        solution = Solution()
        ans = 30
        self.assertEqual(solution.minEatingSpeed([30,11,23,4,20],5), ans)
    
    def test_minEatingSpeed_2(self):
        solution = Solution()
        ans = 23
        self.assertEqual(solution.minEatingSpeed([30,11,23,4,20],6), ans)
"""