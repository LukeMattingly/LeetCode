from typing import List
import unittest

class Solution():
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])

        left = 0
        right = rows * columns -1
        while left <= right:
            mid = left + (right - left) //2 
            row = mid // columns
            col = mid % columns
            if target > matrix[row][col]:
                left = mid + 1
            elif target < matrix[row][col]:
                right = mid -1
            elif target ==  matrix[row][col]:
                return True
            
        return False



class test_searchMatrix(unittest.TestCase):
    def test_searchMatrix_1(self):
        solution = Solution()
        ans = True
        self.assertEqual(solution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3), ans)

    def test_searchMatrix_2(self):
        solution = Solution()
        ans = False
        self.assertEqual(solution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13), ans)
    

if __name__ == '__main__':
    unittest.main()