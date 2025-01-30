from typing import List
import unittest
from collections import defaultdict

class Solution():
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        result = []

        for i, num in enumerate(sorted_nums):
            if i > 0 and num == sorted_nums[i-1]: #check to see if the current value is same as the previous value(hence why we need i+1)
                continue

            left = i +1 
            right = len(sorted_nums)-1

            while left < right:
                target = num + sorted_nums[left] + sorted_nums[right]
                if target > 0:
                    right -=1
                elif target <0:
                    left +=1
                elif target == 0:
                    result.append([num, sorted_nums[left], sorted_nums[right]])
                    left +=1
                    right -=1
                    while left < right and sorted_nums[left] == sorted_nums[left -1]:
                        left +=1
                    while left < right and sorted_nums[right] == sorted_nums[right +1]:
                        right -=1


        return result



class test_threeSum(unittest.TestCase):
    def test_threeSum_1(self):
        solution = Solution()
        ans = [[-1,-1,2],[-1,0,1]]
        self.assertEqual(solution.threeSum([-1,0,1,2,-1,-4]), ans)

    def test_threeSum_2(self):
        solution = Solution()
        ans = []
        self.assertEqual(solution.threeSum([0,1,1]), ans)
    
    def test_threeSum_3(self):
        solution = Solution()
        ans = [[0,0,0]]
        self.assertEqual(solution.threeSum([0,0,0]), ans)


if __name__ == '__main__':
    unittest.main()