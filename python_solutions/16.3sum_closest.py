from typing import List
import unittest

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        currentSum = nums[0] + nums[1] + nums[2]
        if len(nums) == 3:
            return currentSum
        
        nums.sort()
    
        for i in range(0, len(nums)-2):
            low = i+1
            high = len(nums)-1
            while low < high:
                sum = nums[i] + nums[low] + nums[high]
                if abs(sum - target) < abs(currentSum - target):
                    currentSum = sum
                if sum > target:
                    high -= 1
                elif sum < target:
                    low += 1
                else:
                    return sum
                
        return currentSum
            
                

class test_threeSumClosest(unittest.TestCase):
    def test_threeSumClosest_1(self):
        solution = Solution()
        ans = 6
        self.assertEqual(solution.threeSumClosest([1, 2, 3, 4, 5, 6, 7, 8, 9], 5), ans)

    def test_threeSumClosest_2(self):
        solution = Solution()
        ans = 0
        self.assertEqual(solution.threeSumClosest([0,0,0], 1), ans)

    def test_threeSumClosest_3(self):
        solution = Solution()
        ans = 2
        self.assertEqual(solution.threeSumClosest([-1,2,1,-4], 1), ans)

    def test_threeSumClosest_4(self):
        solution = Solution()
        ans = 2
        self.assertEqual(solution.threeSumClosest([-1000,-1,13,24,58,1003], 2), ans)

         

if __name__ == '__main__':
    unittest.main()
