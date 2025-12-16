import unittest
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        totalSets = []

        def backtrack(openCount, closedCount, currentString):
            if openCount == n and closedCount ==n:
                totalSets.append(currentString)
                return
            
            if openCount< n:
                backtrack(openCount +1, closedCount, currentString + "(")
            
            if closedCount < openCount:
                backtrack(openCount, closedCount +1, currentString + ")")

        
        backtrack(0,0, "")
        return totalSets

class test_generateParenthesis(unittest.TestCase):
    def test_generateParenthesis_1(self):
        solution = Solution()
        ans = ["((()))","(()())","(())()","()(())","()()()"]
        self.assertEqual(solution.generateParenthesis(3), ans)

    def test_generateParenthesis_2(self):
        solution = Solution()
        ans = ["()"]
        self.assertEqual(solution.generateParenthesis(1), ans)

         

if __name__ == '__main__':
    unittest.main()