from typing import List
import unittest
from collections import defaultdict

class Solution():
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        print("problem start")
        result = [0] * len(temperatures)
        mono_decrease_stack = []

        for i, temp in enumerate(temperatures):
            while mono_decrease_stack and temp > temperatures[mono_decrease_stack[-1]]: #current temp is large than top element on decreasing stack
                index = mono_decrease_stack.pop()
                result[index] = i - index #current index - stored index
            mono_decrease_stack.append(i) #storing indexes in stack
            print(mono_decrease_stack)
        return result



class test_dailyTemperatures(unittest.TestCase):
    def test_dailyTemperatures_1(self):
        solution = Solution()
        ans = [1,1,4,2,1,1,0,0]
        self.assertEqual(solution.dailyTemperatures([73,74,75,71,69,72,76,73]), ans)

    def test_dailyTemperatures_2(self):
        solution = Solution()
        ans = [1,1,1,0]
        self.assertEqual(solution.dailyTemperatures([30,40,50,60]), ans)
    
    def test_dailyTemperatures_3(self):
        solution = Solution()
        ans = [1,1,0]
        self.assertEqual(solution.dailyTemperatures([30,60,90]), ans)


if __name__ == '__main__':
    unittest.main()