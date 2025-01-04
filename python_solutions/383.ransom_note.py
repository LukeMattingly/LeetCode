from typing import List
import unittest
from collections import defaultdict

class Solution():
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letter_map = defaultdict(int)

        if len(magazine) < len(ransomNote):
            return False
        
        for l in magazine:
            letter_map[l] +=1
        
        for r in ransomNote:
            if letter_map[r] <= 0:
                return False
            letter_map[r] -= 1

        return True


class test_canConstruct(unittest.TestCase):
    def test_canConstruct_1(self):
        solution = Solution()
        ans = False
        self.assertEqual(solution.canConstruct("a", "b" ), ans)

    def test_canConstruct_2(self):
        solution = Solution()
        ans = False
        self.assertEqual(solution.canConstruct("aa", "ab"), ans)
    
    def test_canConstruct_3(self):
        solution = Solution()
        ans = True
        self.assertEqual(solution.canConstruct("aa", "aab"), ans)


if __name__ == '__main__':
    unittest.main()