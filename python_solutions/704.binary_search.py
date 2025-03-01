from typing import List
import unittest
from collections import defaultdict

class Solution():
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) -1

        while l <= r:
            mid_index = (l + r) //2
            if nums[mid_index] == target:
                return mid_index
            if nums[mid_index] > target:
                r = mid_index -1
            if nums[mid_index] < target:
                l = mid_index + 1
        
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