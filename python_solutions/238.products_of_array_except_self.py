from typing import List
import unittest

class Solution():
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i] 

        suffix =1
        for i in range(len(nums)-1, -1, -1):
            result[i] = suffix * result[i]
            suffix *= nums[i]

        return result
      

class test_productExceptSelf(unittest.TestCase):
    def test_productExceptSelf_1(self):
        solution = Solution()
        ans = [24,12,8,6]
        self.assertEqual(solution.productExceptSelf([1,2,3,4]), ans)
    
    def test_productExceptSelf_2(self):
        solution = Solution()
        ans = [0,0,9,0,0]
        self.assertEqual(solution.productExceptSelf([-1,1,0,-3,3]), ans)


if __name__ == '__main__':
    unittest.main()