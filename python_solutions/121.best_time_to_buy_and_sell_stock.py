from typing import List
import unittest

class Solution():
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        if sorted(prices, reverse=True) == prices:
            return 0
        
        window_size = 1
        
        for i in range(len(prices)-1):
            left = 0
            while (left + window_size) < len(prices):
                maxProfit = max(maxProfit, prices[left + window_size] - prices[left]) #right value minus the left 10 - 1 ( want profit), then max of current value or prev saved
                left+=1
            window_size +=1

        return maxProfit
    
class test_maxProfits(unittest.TestCase):
    def test_maxProfits_1(self):
        solution = Solution()
        ans = 5
        self.assertEqual(solution.maxProfit([7,1,5,3,6,4]), ans)

    def test_maxProfit_2(self):
        solution = Solution()
        ans = 0
        self.assertEqual(solution.maxProfit([7,6,4,3,1]), ans)
    
    def test_maxProfit_3(self):
        solution = Solution()
        ans = 6
        self.assertEqual(solution.maxProfit([10,1,5,6,7,1]), ans)

if __name__ == '__main__':
    unittest.main()