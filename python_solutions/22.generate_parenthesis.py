import unittest
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return ""


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