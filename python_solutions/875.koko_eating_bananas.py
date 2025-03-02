import unittest
from typing import List
from collections import Counter
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = math.ceil(sum(piles)/h)
        r = max(piles)
        result = r #max the solution could be


        while l <= r:
            k = l + (r-l) //2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/k)

            if hours > h:
                l = k +1
            else:
                result = k
                r = k -1
            
        return result 



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

         

if __name__ == '__main__':
    unittest.main()