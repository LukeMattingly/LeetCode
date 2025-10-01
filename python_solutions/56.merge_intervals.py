from typing import List
import unittest

class Solution():
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda pair: pair[0])
        
        res = [intervals[0]]

        for start, end in intervals:
            lastEnd = res[-1][1]

            if start<= lastEnd:
                res[-1][1]= max(lastEnd, end)
            else:
                res.append([start,end])
        return res

class test_insert(unittest.TestCase):
    def test_insert_1(self):
        solution = Solution()
        ans = [[1,5],[6,9]]
        self.assertEqual(solution.insert([[1,3],[6,9]],[2,5] ), ans)

    def test_insert_2(self):
        solution = Solution()
        ans = [[1,2],[3,10],[12,16]]
        self.assertEqual(solution.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]), ans)
    
    def test_insert_3(self):
        solution = Solution()
        ans = [[1,6]]
        self.assertEqual(solution.insert([[1,3],[4,6]], [2,5]), ans)

if __name__ == '__main__':
    unittest.main()