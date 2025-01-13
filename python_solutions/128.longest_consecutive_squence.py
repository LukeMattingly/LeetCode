from typing import List
import unittest

class Solution():
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        longest_count = 1
        counts_array = []

        sorted_array = sorted(nums)

        prev = 0
        for i , current in enumerate(sorted_array):
            if i == 0:
                prev = current
                continue
            if prev == current:
                continue
            if (prev + 1) == current:
                longest_count += 1
            else:
                counts_array.append(longest_count)
                longest_count = 1
            prev = current

        counts_array.append(longest_count)
        return max(counts_array)

class test_longestConsecutive(unittest.TestCase):

    def test_longestConsecutive_1(self):
        solution = Solution()
        ans = 4
        self.assertEqual(solution.longestConsecutive([100,4,200,1,3,2]), ans)

    def test_longestConsecutive_2(self):
        solution = Solution()
        ans = 9
        self.assertEqual(solution.longestConsecutive([0,3,7,2,5,8,4,6,0,1]), ans)
    
    def test_longestConsecutive_3(self):
        solution = Solution()
        ans = 4
        self.assertEqual(solution.longestConsecutive([2,20,4,10,3,4,5]), ans)

    def test_longestConsecutive_4(self):
        solution = Solution()
        ans = 7
        self.assertEqual(solution.longestConsecutive([0,3,2,5,4,6,1,1]), ans)


if __name__ == '__main__':
    unittest.main()