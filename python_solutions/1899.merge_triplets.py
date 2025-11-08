from typing import List
import unittest


class Solution:
  def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        max_triplet = [0,0,0]

        for t in triplets:
            if all(t[i] <= target[i] for i in range(3)):
                for j in range(3):
                    max_triplet[j] = max(max_triplet[j], t[j])
        
        return max_triplet == target
    
    
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