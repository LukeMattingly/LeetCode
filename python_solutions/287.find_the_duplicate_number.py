from typing import List
import unittest
from collections import defaultdict

class Solution():
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0,0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow==fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow==slow2:
                return slow

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