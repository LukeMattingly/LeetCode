from typing import List
import unittest

class Solution():
    def search(self, nums: List[int], target: int) -> int:
        left =0
        right = len(nums) -1

        #= because if [1] then r and l are equal
        while left <= right:
            mid_index = left + (right -left ) //2
            if target == nums[mid_index]:
                return mid_index
            #sorted left
            if nums[left] <= nums[mid_index]:
                if target > nums[mid_index] or target < nums[left]:
                    left = mid_index +1
                else:
                    right = mid_index -1
            #sorted right
            if nums[right] >= nums[mid_index]:
                if target < nums[mid_index] or target > nums[right]:
                    right = mid_index -1
                else:
                    left = mid_index +1
        
        return -1





class test_search_test(unittest.TestCase):
    def test_search_1(self):
        solution = Solution()
        ans = 4
        self.assertEqual(solution.search( [3,4,5,6,1,2], 1), ans)

    def test_search_2(self):
        solution = Solution()
        ans = -1
        self.assertEqual(solution.search( [3,5,6,0,1,2], 4), ans)
    
    def test_search_3(self):
        solution = Solution()
        ans = 4
        self.assertEqual(solution.search([4,5,6,7,0,1,2], 0), ans)

    def test_search_4(self):
        solution = Solution()
        ans = -1
        self.assertEqual(solution.search([4,5,6,7,0,1,2], 3), ans)


if __name__ == '__main__':
    unittest.main()