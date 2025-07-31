import unittest
from typing import List
import heapq 


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        max_heap = [-n for n in nums] #turning all values into negative to use the existing heap implementation
        heapq.heapify(max_heap)

        for i in range(k):
            result = heapq.heappop(max_heap)
            if k == i+1:
                return -result
        
class test_findKthLargest(unittest.TestCase):
    def test_findKthLargest_1(self):
        solution = Solution()
        ans = 5
        self.assertEqual(solution.findKthLargest([3,2,1,5,6,4],2), ans)

    def test_findKthLargest_2(self):
        solution = Solution()
        ans = 4
        self.assertEqual(solution.findKthLargest([3,2,3,1,2,4,5,5,6],4), ans)
    

if __name__ == '__main__':
    unittest.main()
