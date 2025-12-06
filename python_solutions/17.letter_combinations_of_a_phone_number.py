from typing import List
import unittest

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def backtrack(path, index):
            if len(digits) == index:
                result.append(path)
                return
            
            for letter in phone[digits[index]]:
                backtrack(path + letter, index+1)
            
        
        result =[]
        if digits:
            backtrack("",0)
        return result


class test_letterCombinations(unittest.TestCase):
    def test_letterCombinations_1(self):
        solution = Solution()
        ans = ["ad","ae","af","bd","be","bf","cd","ce","cf"]
        self.assertEqual(solution.letterCombinations("23"), ans)

    def test_letterCombinations_2(self):
        solution = Solution()
        ans = []
        self.assertEqual(solution.letterCombinations(""), ans)

    def test_letterCombinations_3(self):
        solution = Solution()
        ans = ["a","b","c"]
        self.assertEqual(solution.letterCombinations("2"), ans)


         

if __name__ == '__main__':
    unittest.main()
