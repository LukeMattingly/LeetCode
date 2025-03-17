from typing import List
import unittest
from collections import defaultdict

class Solution():
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                if nums[i] == nums[j]:
                    return nums[j]


class test_findDuplicate(unittest.TestCase):
    def test_findDuplicate_1(self):
        solution = Solution()
        ans = 2
        self.assertEqual(solution.findDuplicate([1,3,4,2,2]), ans)

    def test_findDuplicate_2(self):
        solution = Solution()
        ans = 3
        self.assertEqual(solution.findDuplicate([3,1,3,4,2]), ans)
    
    def test_findDuplicate_3(self):
        solution = Solution()
        ans = 3
        self.assertEqual(solution.findDuplicate([3,3,3,3,3]), ans)


if __name__ == '__main__':
    unittest.main()