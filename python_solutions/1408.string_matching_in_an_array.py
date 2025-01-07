from typing import List
import unittest


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i == j:
                    continue
                if words[i] in words[j]:
                    result.append(words[i])
                    break
        
        return result
    
    
class test_stringMatching(unittest.TestCase):
    def test_stringMatching_1(self):
        solution = Solution()
        ans = ["as","hero"]
        self.assertEqual(solution.stringMatching(["mass","as","hero","superhero"]), ans)

    def test_stringMatching_2(self):
        solution = Solution()
        ans = ["et","code"]
        self.assertEqual(solution.stringMatching(["leetcode","et","code"]), ans)
    
    def test_stringMatching_3(self):
        solution = Solution()
        ans = []
        self.assertEqual(solution.stringMatching(["blue","green","bu"]), ans)


if __name__ == '__main__':
    unittest.main()