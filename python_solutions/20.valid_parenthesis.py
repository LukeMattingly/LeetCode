from typing import List
import unittest

class Solution():
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False
        
        stack = []
        
        paren_map = {
            "]":"[",
            ")":"(",
            "}":"{"
        }
        
        for item in s:
            if item in paren_map.values():
                stack.append(item)
            else:
                if stack and stack[-1] == paren_map[item]:
                    stack.pop()
                else:
                    return False 
            
        if stack:
            return False
        
        return True 



class test_isValid(unittest.TestCase):

    def test_isValid_1(self):
        solution = Solution()
        ans = True
        self.assertEqual(solution.isValid("[]"), ans)

    def test_isValid_2(self):
        solution = Solution()
        ans = True
        self.assertEqual(solution.isValid("([{}])"), ans)

    def test_isValid_3(self):
        solution = Solution()
        ans = False
        self.assertEqual(solution.isValid("[(])"), ans)

    def test_isValid_4(self):
        solution = Solution()
        ans = True
        self.assertEqual(solution.isValid("()[]{}"), ans)
    
    def test_isValid_5(self):
        solution = Solution()
        ans = False
        self.assertEqual(solution.isValid("]]"), ans)



if __name__ == '__main__':
    unittest.main()