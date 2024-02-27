import unittest
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(pointer , currentValues, total):
            if total == target:
                res.append(currentValues.copy())
                return
            if pointer >= len(candidates) or total > target:
                return
            
            currentValues.append(candidates[pointer])
            backtrack(pointer, currentValues, total+ candidates[pointer])
            currentValues.pop()
            backtrack(pointer+1, currentValues, total)
                
        backtrack(0, [], 0)
        return res


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