from typing import List
import unittest

class Solution():
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                res +=1
                prevEnd = min(end, prevEnd)
        return res



class test_eraseOverlapIntervals(unittest.TestCase):
    def test_eraseOverlapIntervals_1(self):
        solution = Solution()
        ans = [[1,5],[6,9]]
        self.assertEqual(solution.eraseOverlapIntervals([[1,3],[6,9]],[2,5] ), ans)

    def test_eraseOverlapIntervals_2(self):
        solution = Solution()
        ans = [[1,2],[3,10],[12,16]]
        self.assertEqual(solution.eraseOverlapIntervals([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]), ans)
    
    def test_eraseOverlapIntervals_3(self):
        solution = Solution()
        ans = [[1,6]]
        self.assertEqual(solution.eraseOverlapIntervals([[1,3],[4,6]], [2,5]), ans)

if __name__ == '__main__':
    unittest.main()