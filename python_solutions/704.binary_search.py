from typing import List
import unittest
from collections import defaultdict

class Solution():
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        while left <= right:
            middle_index = left + ((right - left) // 2)
            middle_value = nums[middle_index]
            if target > middle_value:
                left = middle_index + 1
            if target < middle_value:
                right = middle_index - 1
            if target == middle_value:
                return middle_index
        
        return -1


class test_search(unittest.TestCase):
    def test_search_1(self):
        solution = Solution()
        ans = 4
        self.assertEqual(solution.search([-1,0,3,5,9,12], 9), ans)

    def test_search_2(self):
        solution = Solution()
        ans = -1
        self.assertEqual(solution.search([-1,0,3,5,9,12],2), ans)
    


if __name__ == '__main__':
    unittest.main()