import unittest
from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position, speed), reverse=True)
        stack = []

        for pos , speed in pairs:
            dist = target - pos
            stack.append(dist / speed)
            if len(stack) >=2 and stack[-1] <= stack[-2]: #collide so we must pop top of stack
                stack.pop()

        return len(stack) #total length is total number of fleets


class test_carFleet(unittest.TestCase):
    def test_carFleet_1(self):
        solution = Solution()
        ans = 3
        self.assertEqual(solution.carFleet(12, [10,8,0,5,3], [2,4,1,1,3]), ans)

    def test_carFleet_2(self):
        solution = Solution()
        ans = 1
        self.assertEqual(solution.carFleet(10, [3], [3]), ans)

         

if __name__ == '__main__':
    unittest.main()