from typing import List
import unittest


class Solution:
  def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        matchedFirst =False
        matchedSecond =False
        matchedThird =False
        for t in triplets:
            if target[0]== t[0] and target[1] >= t[1] and target[2] >= t[2]:
                matchedFirst =True

            if target[1] == t[1] and target[2] >= t[2] and target[0] >= t[0]:
                 matchedSecond = True
            
            if target[2] == t[2] and target[1] >= t[1] and target[0] >= t[0]:
                 matchedThird = True

        return matchedFirst and matchedSecond and matchedThird
    
    
class test_mergeTriplets(unittest.TestCase):
    def test_mergeTriplets_1(self):
        solution = Solution()
        ans = True
        self.assertEqual(solution.mergeTriplets([[1,2,3],[7,1,1]], [7,2,3]), ans)

    def test_mergeTriplets_2(self):
        solution = Solution()
        ans = False
        self.assertEqual(solution.mergeTriplets([[2,5,6],[1,4,4],[5,7,5]], [5,4,6]), ans)

    def test_mergeTriplets_3(self):
        solution = Solution()
        ans = False
        self.assertEqual(solution.mergeTriplets([[3,5,1],[10,5,7]],[3,5,7]), ans)

if __name__ == '__main__':
    unittest.main()