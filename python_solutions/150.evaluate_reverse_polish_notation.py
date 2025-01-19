from typing import List
import unittest


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operator_set = set(["*", "-", "/", "+"])

        for token in tokens:
            if token not in operator_set:
                stack.append(int(token))
            else:
                second_val = stack.pop()
                first_val = stack.pop()
                if token == "*":
                    stack.append(first_val * second_val)
                if token == "/":
                    stack.append(int(first_val / second_val))
                if token == "-":
                    stack.append(first_val - second_val)
                if token == "+":
                    stack.append(first_val + second_val)

        return stack.pop()
    


class test_evalRPN(unittest.TestCase):
    def test_evalRPN_1(self):
        solution = Solution()
        ans = 9
        self.assertEqual(solution.evalRPN(["2","1","+","3","*"]), ans)
    
    def test_evalRPN_2(self):
        solution = Solution()
        ans = 6
        self.assertEqual(solution.evalRPN(["4","13","5","/","+"]), ans)

    def test_evalRPN_3(self):
        solution = Solution()
        ans = 22
        self.assertEqual(solution.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]), ans)
    
    def test_evalRPN_1(self):
        solution = Solution()
        ans = 18
        self.assertEqual(solution.evalRPN(["18"]), ans)


if __name__ == '__main__':
    unittest.main()