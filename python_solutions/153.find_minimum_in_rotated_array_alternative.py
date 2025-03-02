from typing import List
import unittest

class Solution():
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        result =nums[0]

        while left <= right:
            if nums[left] < nums[right]:
                result = min(result, nums[left])
                break

            mid_index = left + (right - left) // 2
            result = min(result, nums[mid_index])
            if  nums[left] <= nums[mid_index]:
                left = mid_index +1
            else:
                right = mid_index -1
            
            return result



class test_findMin_test(unittest.TestCase):
    def test_findMin_1(self):
        solution = Solution()
        ans = 1
        self.assertEqual(solution.findMin([3,4,5,1,2]), ans)

    def test_findMin_2(self):
        solution = Solution()
        ans = 0
        self.assertEqual(solution.findMin([4,5,6,7,0,1,2]), ans)
    
    def test_findMin_3(self):
        solution = Solution()
        ans = 11
        self.assertEqual(solution.findMin([11,13,15,17]), ans)

if __name__ == '__main__':
    unittest.main()