from typing import List
import unittest
from collections import defaultdict

class Solution():
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i-index))
                start = index
            stack.append((start, h))

        for i,h in stack:
            maxArea = max(maxArea, h* (len(heights) -i ))
        return maxArea

class test_largestRectangleArea(unittest.TestCase):
    def test_largestRectangleArea_1(self):
        solution = Solution()
        ans = 8
        self.assertEqual(solution.largestRectangleArea([7,1,7,2,2,4]), ans)

    def test_largestRectangleArea_2(self):
        solution = Solution()
        ans = 7
        self.assertEqual(solution.largestRectangleArea([1,3,7]), ans)
    

if __name__ == '__main__':
    unittest.main()