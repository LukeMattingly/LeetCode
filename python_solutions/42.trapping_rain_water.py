import unittest
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0

        for i in range(len(height)):
            leftMax = rightMax = height[i]

            for j in range(i):
                leftMax = max(leftMax, height[j])
            for j in range(i +1, len(height)):
                rightMax = max(rightMax, height[j])
            
            result += min(leftMax, rightMax) - height[i]
        return result




class test_trap(unittest.TestCase):
    def test_trap_1(self):
        solution = Solution()
        ans = 6
        self.assertEqual(solution.trap([0,1,0,2,1,0,1,3,2,1,2,1]), ans)

    def test_trap_2(self):
        solution = Solution()
        ans = 9
        self.assertEqual(solution.trap([4,2,0,3,2,5]), ans)



         

if __name__ == '__main__':
    unittest.main()