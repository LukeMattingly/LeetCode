from typing import List
import unittest

class Solution():
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [
                    min(newInterval[0],intervals[i][0]),
                    max(newInterval[1], intervals[i][1])
                ]
            res.append(newInterval)
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