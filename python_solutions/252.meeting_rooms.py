from typing import List
import unittest

"""
Definition of Interval:
"""
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        intervals.sort(key=lambda pair: pair.start)
        if intervals:
            prevEnd = intervals[0].end

        for interval in intervals[1:]:
            start, end = interval.start, interval.end
            if prevEnd > start:
                return False
            prevEnd = end 
        return True





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