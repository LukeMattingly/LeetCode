import unittest
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        l = 0
        r = len(height)-1
        maxL = height[l]
        maxR = height[r]

        while l < r:
            if maxL < maxR:
                l+=1
                maxL = max(maxL, height[l])
                result += maxL - height[l]
            else:
                r-=1
                maxR = max(maxR, height[r])
                result += maxR - height[r]

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