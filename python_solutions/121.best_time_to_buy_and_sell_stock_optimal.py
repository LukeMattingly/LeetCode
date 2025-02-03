from typing import List
import unittest

class Solution():
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 #buying
        r = 1 #selling
        maxProfit = 0

        while r < len(prices):
            profit = prices[r] - prices[l]
            if profit > 0:
                maxProfit = max(profit, maxProfit)
            else:
                l=r
            r+=1

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
    
    def test_maxProfit_4(self):
        solution = Solution()
        ans = 6
        self.assertEqual(solution.maxProfit([10,9,15,6,8,1]), ans)

if __name__ == '__main__':
    unittest.main()