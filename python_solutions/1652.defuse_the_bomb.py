from typing import List
import unittest


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        result = [0]*n            

        if k == 0:
            return result

        for i in range(n):
            if k > 0:
                for j in range(i +1, i + 1 + k):
                    result[i] +=code[j % n ]

            elif k < 0:
                for j in range(i -1, i-1 -abs(k), -1):
                    result[i] +=code[j % n ]

        return result

        
    
    
class test_decrypt(unittest.TestCase):
    def test_decrypt_1(self):
        solution = Solution()
        ans = [12,10,16,13]
        self.assertEqual(solution.decrypt([5,7,1,4], 3), ans)

    def test_decrypt_2(self):
        solution = Solution()
        ans = [0,0,0,0]
        self.assertEqual(solution.decrypt([1,2,3,4],0), ans)
    
    def test_decrypt_3(self):
        solution = Solution()
        ans = [12,5,6,13]
        self.assertEqual(solution.decrypt([2,4,9,3],-2), ans)


if __name__ == '__main__':
    unittest.main()