import unittest
from typing import List

class Solution:
        def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
            result = []
            candidates.sort()

            def backtrack(startIndex, combo, currentTotal):
                  if currentTotal == 0:
                        result.append(combo.copy())
                        return
                  
                  for i in range(startIndex, len(candidates)):
                        if i> startIndex and candidates[i] == candidates[i-1]:
                              continue
                        
                        if candidates[i]> currentTotal:
                              break
                        
                        combo.append(candidates[i])
                        backtrack(i+1, combo, currentTotal - candidates[i])
                        combo.pop()

            backtrack(0, [], target)
            return result
        

class test_combinationSum(unittest.TestCase):
    def test_combinationSum_1(self):
        solution = Solution()
        ans = [[1,1,6],[1,2,5],[1,7],[2,6]]
        self.assertEqual(solution.combinationSum2([10,1,2,7,6,1,5], 8), ans)

    def test_combinationSum_2(self):
        solution = Solution()
        ans = [[1,2,2],[5]]
        self.assertEqual(solution.combinationSum2([2,5,2,1,2], 5), ans)


         

if __name__ == '__main__':
    unittest.main()