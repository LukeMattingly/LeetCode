from typing import List
import unittest

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: 
            return []
        
        nums = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"], 
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        res = []

        def backtrack(comb, nxt_digits):
            if len(nxt_digits) == 0:
                res.append(comb)
            else:
                for letter in nums[nxt_digits[0]]:
                    backtrack(comb + letter, nxt_digits[1:])

        backtrack("", digits)

        return res



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
