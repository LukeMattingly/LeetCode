from typing import List
import unittest


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        right = len(numbers) -1
        left = 0

        while left < right:
            curr = numbers[left] + numbers[right]
            if curr == target:
                return [left+1, right+1]
            if curr < target:
                left +=1
            if curr > target:
                right -=1

    
    
class test_twoSum(unittest.TestCase):
    def test_twoSum_1(self):
        solution = Solution()
        ans = [1,2]
        self.assertEqual(solution.twoSum([2,7,11,15], 9), ans)

    def test_twoSum_2(self):
        solution = Solution()
        ans = [1,3]
        self.assertEqual(solution.twoSum( [2,3,4], 6), ans)
    
    def test_twoSum_3(self):
        solution = Solution()
        ans = [1,2]
        self.assertEqual(solution.twoSum([-1,0], -1), ans)

    def test_twoSum_4(self):
        solution = Solution()
        ans = [2,3]
        self.assertEqual(solution.twoSum([2,7,11,15], 18), ans)

if __name__ == '__main__':
    unittest.main()