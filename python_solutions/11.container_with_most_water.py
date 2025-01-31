import unittest
from typing import List

class Solution():
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        left = 0
        right = len(height) -1

        while left < right:
            smaller = min(height[left], height[right])
            currArea = smaller  * (right - left )
            if currArea > maxArea:
                maxArea = currArea
            if height[left] < height[right]:
                left +=1
            else:
                right -=1

        return maxArea


class test_MaxArea(unittest.TestCase):
    def test_maxArea_1(self):
        solution = Solution()
        ans = 49
        self.assertEqual(solution.maxArea([1,8,6,2,5,4,8,3,7]), ans)
    def test_maxArea_2(self):
        solution = Solution()
        ans = 4
        self.assertEqual(solution.maxArea([2,2,2]), ans)
    def test_maxArea_3(self):
        solution = Solution()
        ans = 36
        self.assertEqual(solution.maxArea([1,7,2,5,4,7,3,6]), ans)


if __name__ =='__main__':
    unittest.main()