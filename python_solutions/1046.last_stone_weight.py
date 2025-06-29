import unittest
from typing import List
import heapq 

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-n for n in stones] #turning all values into negative to use the existing heap implementation
        heapq.heapify(max_heap)

        while len(max_heap) >= 2:
            y = heapq.heappop(max_heap)
            x = heapq.heappop(max_heap)
            if y > x: 
                z_new = abs(y) - abs(x)
                heapq.heappush(max_heap, -z_new)
        
        if len(max_heap) == 1:
            return abs(max_heap[0])
        if len(max_heap) == 0:
            return 0


if __name__ == '__main__':
    unittest.main()


    import heapq 

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.k = k
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)


    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)