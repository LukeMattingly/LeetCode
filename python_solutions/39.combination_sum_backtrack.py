import unittest
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def backtrack(index, combo, total):
            if total == 0:
                result.append(combo.copy())
                return
            
            if total < 0 or len(candidates)== index or candidates[index] > total:
                return
            
            combo.append(candidates[index])
            backtrack(index, combo, total - candidates[index])
            
            combo.pop()
            backtrack(index+1, combo, total)

        result = []
        candidates.sort()
        backtrack(0,[], target)
        return result

class test_combinationSum(unittest.TestCase):
    def test_combinationSum_1(self):
        solution = Solution()
        ans = [[2,2,3],[7]]
        self.assertEqual(solution.combinationSum([2,3,6,7], 7), ans)

    def test_combinationSum_2(self):
        solution = Solution()
        ans = [[2,2,2,2],[2,3,3],[3,5]]
        self.assertEqual(solution.combinationSum([2,3,5], 8), ans)

    def test_combinationSum_3(self):
        solution = Solution()
        ans = []
        self.assertEqual(solution.combinationSum([2],1), ans)


         

if __name__ == '__main__':
    unittest.main()