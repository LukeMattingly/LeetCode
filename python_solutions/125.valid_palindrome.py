from typing import List
import unittest
from collections import defaultdict

class Solution():
    def isPalindrome(self, s: str) -> bool:

        s = ''.join(c.lower() for c in s if c.isalnum())

        left = 0 
        right = len(s)-1

        while left < right:
            if s[left] != s[right]:
                return False
            else:
                left +=1
                right-=1

        return True


class test_isPalindrome(unittest.TestCase):
    def test_isPalindrome_1(self):
        solution = Solution()
        ans = True
        self.assertEqual(solution.isPalindrome("A man, a plan, a canal: Panama"), ans)

    def test_isPalindrome_2(self):
        solution = Solution()
        ans = False
        self.assertEqual(solution.isPalindrome( "race a car"), ans)
    
    def test_isPalindrome_3(self):
        solution = Solution()
        ans = True
        self.assertEqual(solution.isPalindrome( " "), ans)
    


if __name__ == '__main__':
    unittest.main()