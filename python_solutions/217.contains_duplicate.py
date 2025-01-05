from typing import List
import unittest

class Solution():
    def containsDuplicate(self, nums: List[int]) -> bool:
        dup_map = set()
        for num in nums:
            if num in dup_map:
                return True
            else:
                dup_map.add(num)

        return False

class test_containsDuplicate(unittest.TestCase):
    def test_containsDuplicate_1(self):
        solution = Solution()
        ans = True
        self.assertEqual(solution.containsDuplicate([1,2,3,1] ), ans)

    def test_containsDuplicate_2(self):
        solution = Solution()
        ans = False
        self.assertEqual(solution.containsDuplicate([1,2,3,4]), ans)
    
    def test_containsDuplicate_3(self):
        solution = Solution()
        ans = True
        self.assertEqual(solution.containsDuplicate([1,1,1,3,3,4,3,2,4,2]), ans)

if __name__ == '__main__':
    unittest.main()