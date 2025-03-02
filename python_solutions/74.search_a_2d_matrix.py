from typing import List
import unittest

class Solution():
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])
        top= 0
        bot = rows -1

        #determine row
        while top<=bot:
            mid_row = bot + (top - bot) //2
            if target > matrix[mid_row][-1]:
                top = mid_row +1
            elif target < matrix[mid_row][-0]:
                bot = mid_row -1
            else:
                break 
        
        if not (top <= bot):
            return False
        
        #binary search within the row
        l,r=0, columns-1
        while l<=r:
            mid_index = l + (r - l) //2
            if matrix[mid_row][mid_index] < target:
                l = mid_index + 1
            elif matrix[mid_row][mid_index] > target:
                r = mid_index - 1
            elif matrix[mid_row][mid_index] == target:
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