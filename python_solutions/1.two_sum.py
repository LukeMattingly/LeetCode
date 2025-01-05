from typing import List
import unittest
from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = defaultdict(int)
        for i, num in enumerate(nums):
            sub = target-num
            if sub in index_map:
                return[index_map[sub], i]
            else:
                index_map[num] = i   

class test_twoSum(unittest.TestCase):
    def test_twoSum_1(self):
        solution = Solution()
        ans = [0,1]
        self.assertEqual(solution.twoSum([2,7,11,15], 9 ), ans)

    def test_twoSum_2(self):
        solution = Solution()
        ans = [1,2]
        self.assertEqual(solution.twoSum([3,2,4], 6), ans)

    def test_twoSum_3(self):
        solution = Solution()
        ans = [0,1]
        self.assertEqual(solution.twoSum([3,3],6), ans)

if __name__ == '__main__':
    unittest.main()