from typing import List
import unittest
from collections import deque

class Solution():
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r =0 ,0 
        result = []
        queue = deque()

        while r < len(nums):
            while queue and nums[queue[-1]] < nums[r]:
                queue.pop()
            queue.append(r)

            if l > queue[0]:
                queue.popleft()
            
            if (r + 1)>=k:
                result.append(nums[queue[0]])
                l+=1
            r+=1

        return result

class test_maxSlidingWindow(unittest.TestCase):
    def test_maxSlidingWindow_1(self):
        solution = Solution()
        ans = [3,3,5,5,6,7]
        self.assertEqual(solution.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3), ans)
    
    def test_maxSlidingWindow_2(self):
        solution = Solution()
        ans = [1]
        self.assertEqual(solution.maxSlidingWindow([1], 1), ans)


if __name__ == '__main__':
    unittest.main()