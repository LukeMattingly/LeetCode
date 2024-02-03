import unittest
import numpy as np

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        outputList = []

        for i in range(numRows):
            incr = 2 * (numRows - 1)
            for j in range(i, len(s), incr):
                outputList.append(s[j])
                if i > 0 and i < numRows - 1:
                    if j + incr - 2 * i < len(s):
                        outputList.append(s[j + incr - 2 * i])

        return "".join(outputList)
    
        






class testAddTwoNumbers(unittest.TestCase):
    def test_convert(self):
        solution = Solution()
        ans = "PAHNAPLSIIGYIR"
        self.assertEqual(solution.convert("PAYPALISHIRING", 3), ans)
    


if __name__ == '__main__':
    unittest.main()
