from typing import List
import unittest


class Solution():
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        nums1_set = set()

        for n1 in nums1:
            nums1_set.add(n1)
        
        for n2 in nums2:
            if n2 in nums1_set and n2 not in result:
                result.append(n2)

        return result




class test_intersection(unittest.TestCase):
    def test_intersection_1(self):
        solution = Solution()
        ans = [9,4]
        self.assertEqual(solution.intersection([4,9,5], [9,4,9,8,4] ), ans)

    def test_intersection_2(self):
        solution = Solution()
        ans = [2]
        self.assertEqual(solution.intersection( [1,2,2,1],[2,2]), ans)
    
    def test_intersection_3(self):
        solution = Solution()
        ans = []
        self.assertEqual(solution.intersection([1, 2, 2, 3, 4, 4, 4], [5]), ans)


if __name__ == '__main__':
    unittest.main()