from typing import List
import unittest
from collections import defaultdict

class Solution():
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = []
        accounted_for = defaultdict(int)

        sorted_nums = sorted(nums)
        for num in sorted_nums:
            accounted_for[num] +=1

        for k in range(1, len(nums)+1):
            if k not in accounted_for.keys():
                result.append(k)
            
        return result



class test_findDisappearedNumbers(unittest.TestCase):
    def test_findDisappearedNumbers_1(self):
        solution = Solution()
        ans = [5,6]
        self.assertEqual(solution.findDisappearedNumbers([4,3,2,7,8,2,3,1]), ans)

    def test_findDisappearedNumbers_2(self):
        solution = Solution()
        ans = [2]
        self.assertEqual(solution.findDisappearedNumbers([1,1]), ans)
    
    def test_findDisappearedNumbers_3(self):
        solution = Solution()
        ans = [1]
        self.assertEqual(solution.findDisappearedNumbers([2,3,4]), ans)


if __name__ == '__main__':
    unittest.main()