import unittest
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #only add open parenthesis if open < n
        #only add a closing parenthesis if closed < open
        #if and only if open == closed == n is it valid

        stack = []
        res = []

        def backtrack(openCount, closedCount):
            if openCount == closedCount == n:
                res.append("".join(stack))
                return
            
            if openCount < n:
                stack.append("(")
                backtrack(openCount+1, closedCount)
                stack.pop()
            
            if closedCount < openCount:
                stack.append(")")
                backtrack(openCount, closedCount + 1)
                stack.pop()

        backtrack(0, 0)
        
        return res


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