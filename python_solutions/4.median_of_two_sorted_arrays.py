from typing import List
import unittest

class Solution():
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        total = len(nums1) + len(nums2)
        half = total //2 

        if len(nums2) < len(nums1):
            nums1 , nums2 = nums2, nums1 #swap them if 2 is larger than 1

        #log(min(n, m)) bc just running 1  binary search on smaller of the two
        #num1 is the smaller one always from this point on
        l = 0
        r = len(nums1) -1

        while True:
            nums1_index = (l + r) //2
            nums2_index = half - nums1_index - 2 #both indexes start at 0 so -2 is to accoutn for this
        
            nums1_left = nums1[nums1_index] if nums1_index >= 0 else float("-infinity")
            nums1_right = nums1[nums1_index + 1] if (nums1_index +1) < len(nums1) else float("infinity")
            nums2_left = nums2[nums2_index] if nums2_index >=0 else float("-infinity")
            nums2_right = nums2[nums2_index + 1] if (nums2_index +1) < len(nums2) else float("infinity")

            #partition is correct
            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                #odd
                if total %2:
                    return min(nums1_right, nums2_right)
                
                #even
                return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) /2        
            elif nums1_left> nums2_right:
                r = nums1_index -1
            else:
                l = nums1_index +1


class test_findMedianSortedArrays(unittest.TestCase):
    def test_findMedianSortedArrays_1(self):
        solution = Solution()
        ans = 2
        self.assertEqual(solution.findMedianSortedArrays([1,3],[2]), ans)

    def test_findMedianSortedArrays_2(self):
        solution = Solution()
        ans = 2.5
        self.assertEqual(solution.findMedianSortedArrays([1,2],[3,4]), ans)
    
    

if __name__ == '__main__':
    unittest.main()