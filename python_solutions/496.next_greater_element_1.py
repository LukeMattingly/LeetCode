from typing import List
import unittest
from collections import defaultdict

class Solution():
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        result = [-1] * len(nums1)
        nums1Idx = {n:i for i , n in enumerate(nums1)}

        for num in nums2:
            while stack and stack[-1] < num:
                value = stack.pop()
                index = nums1Idx[value]
                result[index] = num
            
            if num in nums1Idx:
                stack.append(num)
        
        return result

class test_nextGreaterElement(unittest.TestCase):
    def test_nextGreaterElement_1(self):
        solution = Solution()
        ans = [-1,3,-1]
        self.assertEqual(solution.nextGreaterElement([4,1,2],[1,3,4,2]), ans)

    def test_nextGreaterElement_2(self):
        solution = Solution()
        ans = [3,-1]
        self.assertEqual(solution.nextGreaterElement( [2,4],[1,2,3,4]), ans)
    


if __name__ == '__main__':
    unittest.main()