import unittest
from typing import List
import heapq 
import math 
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        distMap = {}
        result = []

        for point in points:
            dist = math.sqrt((point[0] - 0)**2 + (point[1]- 0)**2)
            distMap.setdefault(dist, []).append(point)
            heapq.heappush(minHeap, dist)
        
        while(len(result) < k):
            x = heapq.heappop(minHeap)
            points = distMap[x]
            for point in points:
                result.append(point)
            
        
        return result





if __name__ == '__main__':
    unittest.main()




