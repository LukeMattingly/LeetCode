from typing import List
import unittest
from collections import defaultdict

class Solution():
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for char in s:
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)

        return ''.join(stack)


class test_removeDuplicates(unittest.TestCase):
    def test_removeDuplicates_1(self):
        solution = Solution()
        ans = "ca"
        self.assertEqual(solution.removeDuplicates("abbaca"), ans)

    def test_findDisappearedNumbers_2(self):
        solution = Solution()
        ans = "ay"
        self.assertEqual(solution.removeDuplicates("azxxzy"), ans)
    


if __name__ == '__main__':
    unittest.main()