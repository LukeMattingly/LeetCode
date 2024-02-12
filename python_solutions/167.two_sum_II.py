from typing import List
import unittest

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l =0
        r = len(numbers)-1
        while l < r:
            cSum = numbers[l] + numbers[r]
            if cSum == target:
                return [l+1, r+1]
            elif cSum > target:
                r -=1
            elif cSum <target:
                l +=1

class test_twoSum(unittest.TestCase):
    def test_twoSum_1(self):
        solution = Solution()
        ans = [1,2]
        self.assertEqual(solution.twoSum([2,7,11,15], 9), ans)

    def test_twoSum_2(self):
        solution = Solution()
        ans = [1,3]
        self.assertEqual(solution.twoSum([2,3,4], 6), ans)

    def test_twoSum_3(self):
        solution = Solution()
        ans = [1,2]
        self.assertEqual(solution.twoSum([-1,0], -1), ans)


if __name__ == '__main__':
    unittest.main()
