from typing import List
import unittest

class Solution():
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums_set = set(nums)
        longest_count = 1

        for num in nums_set:
            if num -1 not in nums_set: #found start
                streak = 1
                while num + streak in nums_set:
                    streak+=1
                longest_count = max(streak, longest_count)
        
        return longest_count



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